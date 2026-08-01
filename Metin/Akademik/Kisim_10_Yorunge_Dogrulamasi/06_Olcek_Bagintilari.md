# 10.6 Ölçek Bağıntıları — BTFR, Radyal İvme Bağıntısı, Erken Tip Galaksiler

*(Hesaplar: `CALISMA/btfr_sinavi.py`, `CALISMA/rar_sinavi.py`, `CALISMA/etg_sinavi.py` · kayıtlar: `97_BTFR/`, `95_RAR/`, `96_ETG/`)*

Dönüş eğrileri galaksi galaksi sınavdır; bu bölümün üç sınavı ise galaktik dinamiğin **ölçek bağıntılarını** — literatürün en sağlam ampirik düzenliliklerini — teorinin denklemiyle karşılaştırır. Üçünde de fit yoktur; üçüncüsünde fit **yapılamaz**.

---

## 10.6.1 Baryonik Tully-Fisher İlişkisi (117 galaksi)

Teorinin denklemi dış limitte tek satırda BTFR'yi verir: $\ell_\omega$ sadeleşir ve

$$v^4=\mathcal{G}\,M_{bar}\,a_0$$

çıkar. **Teori BTFR'yi varsaymaz, türetir** — hem eğimini hem normalizasyonunu.

<iframe src="Simulasyon/kisim10/panel_btfr.html" style="width:100%;height:740px;border:1px solid #333;border-radius:8px;background:#0d0d0f" loading="lazy" title="BTFR etkileşimli panel"></iframe>

| Kaynak | BTFR eğimi | Normalizasyon |
|---|---|---|
| **Teori (öngörü, sıfır parametre)** | **3,734** | **0,984** |
| Gözlenen band ($V_f$; ağırlıksız–ağırlıklı) | 3,530 – 3,738 | 1 |
| ΛCDM zinciri (abundance matching + NFW) | 2,716 | 1,027 |

**Teorinin eğimi gözlenen bandın içindedir; ΛCDM zinciri 0,81 dışındadır.** ΛCDM normalizasyonu iyi tutturur ama hız aralığını gerer (kütleli galaksilerin hızını fazla tahmin eder) ve eğimi düşer. İki model **ters türden** başarısızlık gösterir; fit içermeyen bu sınavda eğim tarafındaki fark daha büyüktür ve o satırda teori öndedir.

Panel, bu sınavın bütün duyarlılıklarını düğmelere bağlar ve iki ölçüm kaydı özellikle önemlidir:

- **Hız tanımı hükmü oynatır:** gözlenen eğim, yedi hız tanımı arasında 2,58 ($V_{2{,}2R_d}$) ile 3,74 ($V_f$) arasında değişir. Teorinin $V_f$ ile karşılaştırılması keyfî değildir — yasa kütlenin tamamına bağlıdır, fiziksel karşılığı eğrinin **düz kısmıdır**; gerekçe yazılmıştır ve $V_f$ teori için en elverişli seçim de değildir.
- **Çizgi genişliği tuzağı:** HI çizgi genişliği $W\approx2V_{rot}$ olduğundan, $W/2$ düzeltmesi yapılmadan kurulan karşılaştırma ~×99'luk sahte bir açık üretir. Düzeltmeyle aynı mertebeye iner. Çizgi genişliği satırları düzeltmesiz hiçbir yerde alıntılanmamalıdır.

![BTFR sınavı — ölçüm kaydı](Gorseller/k10_btfr.png)

**Gaz-kafes denetimi.** "Gazda kafes yapısı yok, F4'e katkısı az olmalı" hipotezi ayrıca sınanmıştır (`97_BTFR/GAZ_KAFES.md`): BTFR artığı ile gaz kesri arasında korelasyon **sıfırdır** (Spearman $+0{,}01$; gaz oranı 47 kat değişirken artık sabit). Doğru okuma teorinin lehinedir: **F4'ün kaynağı, bileşiminden bağımsız olarak toplam baryonik kütledir** — yıldız da gaz da aynı nükleon debisini taşır.

![Gaz-kafes denetimi](Gorseller/k10_gaz_kafes.png)

## 10.6.2 Radyal İvme Bağıntısı (2693 nokta, 3,9 decade)

Bu sınav ölçeği değil **biçimi** sorar. Erken tip dahil her sistemde teorinin yerel öngörüsü

$$g_{öng}=g_{bar}+\sqrt{g_{bar}\,a_0}$$

biçimindedir ve biçim sabittir: $a_0$ yanlış kalibre olsaydı bütün noktalar aynı miktarda kayardı ama artıkta ivmeye bağlı **eğilim** oluşmazdı. 2693 nokta ve dört decade, bunu ayırt edecek güçtedir.

![Radyal ivme bağıntısı sınavı](Gorseller/k10_rar.png)

| Ölçüt | Değer |
|---|---|
| Medyan artık (fit yok) | **−0,003 dex** |
| Artığın ivmeyle eğimi (biçim sınavı) | **+0,051 dex/dex — açık kalem** |
| Gözlenen saçılma | 0,146 dex |
| Bildirilen ölçüm bütçesi | 0,126 dex (saçılmanın ~%74'ü) |
| **İç saçılma** | **~0,08 dex** |

Üç sonuç:

1. **Ölçek doğrudur:** medyan artık sıfırdır ve iki asimptot da doğru yerdedir — derin limitte $\sqrt{g_{bar}a_0}$, Newton limitinde $g_{bar}$.
2. **Geçiş biçiminde küçük ama gerçek bir artık kalır:** $+0{,}051$ dex/dex. Bu, $a_0$'ın değeriyle kapatılamaz (değeri oynatmak ortayı düzeltir, iki ucu birden bozar); F1 ile F4'ün **toplanma biçiminin** türetilmesini bekleyen açık kalemdir (10.10).
3. **"Tek yasa" iddiasının sayısal karşılığı:** gözlenen saçılmanın dörtte üçü bildirilen ölçüm hatasıdır; fitsiz bir eğri 2693 noktayı ~0,08 dex'lik iç saçılmayla toplar.

*(Yöntem kaydı: noktalar bağımsız değildir — 2693 nokta 153 galaksiden gelir ve veri kümesi galaksi kimliği içermediği için kümeleme yapılamamıştır; bütün "n" değerleri bu yüzden iyimserdir. Ayrıca F4 payı 0,25'in altına düşen yüksek-ivme kuşaklarında "gereken $a_0$" tersine çözümü kötü koşullanmıştır ve raporlanmaz — bkz. 10.6.3'ün kuralı.)*

## 10.6.3 Erken Tip Galaksiler (16 galaksi, 32 ivme noktası) — fit **yapılamayan** sınav

Erken tip galaksilerin HI halkalarında Lelli ve ark. (2017) galaksi başına yalnız **iki** ivme noktası verir: halkanın iç ve dış kenarı. İki nokta, sıfır serbestlik — ayar yapılacak yer yoktur. Üstelik teorinin öngörüsünde $R$ sadeleşir: formülde ne yarıçap, ne $\Upsilon_*$, ne kütle vardır; $g_{bar}$ ölçülen büyüklüktür.

<iframe src="Simulasyon/kisim10/panel_etg.html" style="width:100%;height:740px;border:1px solid #333;border-radius:8px;background:#0d0d0f" loading="lazy" title="Erken tip galaksiler etkileşimli panel"></iframe>

| Küme | Medyan artık | Saçılma |
|---|---|---|
| **Teori — ETG dış nokta** | **−0,008 dex** | ~0,15 |
| ΛCDM — ETG dış nokta | +0,045 dex | ~0,14 |

![Erken tip galaksiler — radyal ivme düzlemi](Gorseller/k10_etg.png)

Dört sonuç:

1. **Erken tipler disklerle aynı yasaya uyar ve teori ikisini tek formülle verir.** Dış noktada ETG'ler ile aynı ivme aralığındaki 1553 disk noktası arasındaki fark **0,013 dex**'tir — binde üç hız. "Tek yasa" (Lelli ve ark. 2017'nin başlığı) teorinin kurulumunda kendiliğinden çıkar.
2. **Sağlamlık asimetriktir:** ΛCDM bu düzlemde sonuç üretmek için yarıçapı geri kurmak ve $\Upsilon_*$ seçmek zorundadır (panelde **K** rozetli beş büyüklük); teori tarafında tek bir K rozeti yoktur. Panelin $\Upsilon_*$ kaydıracı bunu canlı gösterir: ΛCDM'in medyanı oynar, teorininki kıpırdamaz.
3. **İç noktada iki model de aynı yönde şaşar** — iki bağımsız model aynı yönde aynı büyüklükte şaşıyorsa sorun ortak girdidedir: iç nokta saf Newton rejimidir ve $g_{bar}$ orada doğrudan $\Upsilon_*L$'dir; erken tiplerin yaşlı yıldız nüfusu 3,6 μm'de daha yüksek $\Upsilon_*$ gerektirir. Bu bir açıklamadır, savunma değildir — bütün sayılar yayınlanmış $g_{bar}$ iledir ve $\Upsilon_*$'a dokunulmamıştır; dokunmak bu sınavın tek üstünlüğünü (fit yapılamazlığı) yok ederdi.
4. **Yöntem kuralı buradan doğmuştur:** "gereken $a_0$ çarpanı", yalnız F4'ün öngörüye katkısının anlamlı olduğu ($\gtrsim0{,}3$) rejimde raporlanır; katkı %10'a düşen iç noktada tersine çözüm kötü koşullanmıştır ve anlamsız sayılar üretir.

*(Kapsam kaydı: bu 16 galaksi HI halkası olan, **dönen** erken tiplerdir; M-37 dairesel yörünge için kuruludur ve geçerlidir. Basınç-destekli sistemler — eliptiklerin yıldız kinematiği, cüce küreseller — teorinin bugünkü geçerlilik alanının dışındadır; 6.5.4.9.)*

## 10.6.4 Bu bölümün okunması

Üç bağımsız veri kümesi, üç bağımsız gözlem türü (hız, ivme, ivme halkası) — ve üçü de aynı tabloyu verir: **ölçek doğru, biçim neredeyse doğru.** BTFR eğimi bandın içinde, radyal ivme medyanı sıfırda, erken tipler disklerle aynı çizgide. Kalan iki gerçek artık — geçiş biçimindeki $+0{,}051$ ve sınıf bandı — 10.10'un açık kalemleridir.
