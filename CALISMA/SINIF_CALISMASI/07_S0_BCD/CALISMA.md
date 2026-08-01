# 07_S0_BCD — Disklerin iki ucu: mercek ve tıkız cüce · Çalışma dosyası

> ### ⚡ NİHAİ KURULUM (1 Ağustos 2026 · karar: [86_NIHAI](../86_NIHAI/CALISMA.md))
>
> Bu dosyanın analizi **eski (A) kurulumla** yapıldı ve tarihsel kayıt olarak duruyor.
> Nihai kurulum: yerel $\ell_\omega$ + $a_0=1{,}75\times cH_0/16{,}1$. Nihai sayılar: Nihai kurulumla yeniden koşuldu (`SONUC.csv` yenilendi): S0 medyan RMS **27,9** (eski 41,4), çarpanlar S0 **×2,71** · BCD **×4,37** (nihai $a_0$'a göre). 'Uçlarda band genişliyor' sonucu niteliksel olarak **değişmedi.**


**8 galaksi · yeni fit yok · kaynak: 99_KARMASIK'ın kendi hesabı, buradan ayrıştırıldı**

Hesap: `../../s0_bcd_sinavi.py` · Çıktılar: [`SONUC.csv`](SONUC.csv) · [`YONTEM.md`](YONTEM.md) ·
[`s0_bcd.png`](s0_bcd.png)

---

## 0. Bu sekiz galaksi neden ayrı okundu

`00_SINIFLAMA.csv`'nin 4. ölçütü — *"kendi Hubble tipinde $N<5$ galaksi kalıyor"* — iki tipi
tümüyle `99_KARMASIK`'a atmıştı: **S0** (mercek, 3) ve **BCD** (mavi tıkız cüce, 5).
Hesapları orada yapılmıştı; burada **yeni fit yok**, yalnız ayrıştırma. Tek yeni hesap gereken
$a_0$ çarpanının sayısal çözümü ve tipik ivme.

Ayrı okumaya değer, çünkü bu iki tip örneklemin **iki ucunda** oturur — S0'lar kadran baskın ve
yüksek ivmeli, BCD'ler gaz baskın ve en düşük ivmeli. Yani açık duran "çarpan sınıftan sınıfa
×1,47–3,76 değişiyor" sorusunun **uç noktalarını** verirler.

> ### ⚠ Örneklem kalitesi eşit değil — bu raporun omurgası
>
> | | temiz | kirli | ayrıntı |
> |---|---|---|---|
> | **S0** | **3/3** | 0 | üçü de *yalnız* tip kuralından düştü; **ikisi $Q=1$** (en yüksek kalite), $N=7,17,45$ |
> | **BCD** | **1/5** | 4 | üçü $Q=3$ (düşük kalite), biri $N=4$ (eğri sınanamaz) |
>
> **İki sonuç aynı ağırlıkta okunamaz.** S0 satırı gerçek bir ölçümdür; BCD satırı ağırlıklı
> olarak SPARC'ın kendi düşük kalite bayrağı taşıyan galaksilerden gelir.

---

## 1. Galaksi galaksi

| Galaksi | Tip | N | Q | RMS Evr | RMS ΛCDM | sapma | F4 payı | gereken $a_0$ | temiz |
|---|---|---|---|---|---|---|---|---|---|
| NGC4138 | S0 | 7 | 2 | 24,9 | **12,2** | $-15{,}1\%$ | 0,54 | ×2,96 | ✔ |
| UGC02487 | S0 | 17 | 1 | **114,9** | 153,4 | $-32{,}2\%$ | 0,58 | ×9,39 | ✔ |
| UGC06786 | S0 | 45 | 1 | 41,4 | **30,7** | $-22{,}5\%$ | 0,49 | ×5,48 | ✔ |
| NGC1705 | BCD | 14 | 3 | 25,8 | **14,0** | $-37{,}3\%$ | 0,78 | ×8,90 | ✘ |
| NGC2915 | BCD | 30 | 2 | 34,5 | **15,5** | $-41{,}4\%$ | 0,78 | ×11,91 | ✔ |
| NGC6789 | BCD | 4 | 2 | 19,1 | **15,7** | $-46{,}1\%$ | 0,57 | ×27,94 | ✘ |
| PGC51017 | BCD | 6 | 3 | **14,1** | 26,2 | $\mathbf{+94{,}0\%}$ | 0,76 | **<0,01** | ✘ |
| UGCA281 | BCD | 7 | 3 | **2,2** | 6,1 | $-4{,}0\%$ | 0,68 | ×1,26 | ✘ |

**Öngörü yarışı: Evrenakı 3/8.** Fit yok, iki tarafta da sıfır serbest parametre.

---

## 2. Asıl sonuç — **açık duran saçılma iki katına çıkıyor**

| Sınıf / tip | n | gereken $a_0$ | $\log g_{bar}$ (dış) |
|---|---|---|---|
| Sb–Sbc | 29 | ×1,69 | $-10{,}79$ |
| Im | 26 | ×1,47 | $-11{,}40$ |
| Sc–Scd | 30 | ×2,33 | $-11{,}16$ |
| Sa–Sab | 12 | ×2,67 | $-11{,}15$ |
| Sdm–Sm | 28 | ×2,84 | $-11{,}31$ |
| Sd | 16 | ×3,76 | $-11{,}31$ |
| **S0 (mercek)** | **3** | **×5,48** | $-11{,}17$ |
| **BCD (tıkız cüce)** | **5** | **×8,90** | $-11{,}56$ |
| *BCD — yalnız temiz olan* | *1* | *×11,91* | $-11{,}76$ |

**Band ×1,47–3,76 (2,6 kat) iken ×1,47–8,90 (6,1 kat) oluyor.** 97_BTFR'nin "en kritik açık
maddesi" bu sekiz galaksiyle **iki katından fazla** genişliyor.

Bu sonuç teorinin **aleyhinedir** ve yumuşatılacak bir yanı yok. Ama üç kayıt yanında durmalı:

1. **$n=3$ ve $n=5$.** Hiçbiri tek başına bir hüküm taşımaz.
2. **BCD'lerin 4/5'i kirli** (md. 0). Temiz olan tek galaksi (NGC2915) ×11,91 istiyor — yani
   temizlik BCD sonucunu **düzeltmiyor**, ağırlaştırıyor.
3. **S0 tarafı temiz ve yine de ×5,48.** Bu satır savunulamaz; üç galaksinin ikisi SPARC'ın en
   yüksek kalite bayrağını ($Q=1$) taşıyor.

---

## 3. İvme hipotezine ikinci darbe

95_RAR "düşük ivme → büyük çarpan" eğilimini ölçmüştü (×2,86 → ×0,92). Bu sekiz galaksi o
eğilimin **çok dışında** duruyor:

| | $\log g_{bar}$ | 95_RAR'ın öngördüğü | ölçülen |
|---|---|---|---|
| BCD | $-11{,}56$ | ~×2,4 | **×8,90** |
| S0 | $-11{,}17$ | ~×2,0 | **×5,48** |

İkisi de eğilimin **3–4 katı**. Yani gereken çarpanı ivme tek başına yönetmiyor — 97_BTFR'nin
md. 2'si için ivme adayı, bu veriyle de zayıflıyor.

---

## 4. PGC51017 — teorinin **fazla** öngördüğü galaksi

Sekizin yedisinde teori eksik itim veriyor. PGC51017'de **tam tersi:** $+94\%$. Grafikte
görülüyor — gözlenen eğri 19 km/s'de düz, yalnız baryonların eğrisi (gri) onu **birebir**
yakalıyor, teori 38 km/s'ye çıkıyor.

Yani bu galakside **F4'e hiç yer yok.** Gereken çarpan $<0{,}01$ — bir sayı değil, bir sınır.
Tabloda ve grafikte sayı olarak gösterilmedi; grafikte eksen dışına ok ile işaretlendi.

**Ama:** $Q=3$, $N=6$. Tek başına bir şey kanıtlamaz. Kaydedilmesinin sebebi, örneklemde
**iki yönde birden** sapma olduğunu göstermesi — bütün sapmalar tek yönlü olsaydı sistematik
bir kalibrasyon açığı denebilirdi; öyle değil.

---

## 5. S0'lar ↔ 96_ETG karşılaştırması

Aynı morfoloji, iki farklı ölçüm türü:

| | veri | gereken $a_0$ |
|---|---|---|
| [96_ETG](../96_ETG/CALISMA.md) dış nokta | 16 galaksi × 2 ivme noktası | **×1,85** |
| **Bu sınav, S0** | 3 galaksi × dönüş eğrisi | **×5,48** |

**Üç kat fark var ve açıklanmadı.** Aday sebepler, hiçbiri sınanmadı:

- İki küme **aynı galaksiler değil.** 96_ETG'nin ETG'leri HI halkalı, dönen sistemler;
  buradaki üç S0 SPARC diski.
- 96_ETG $g_{bar}$'ı **ölçüm** olarak alır; burada $V_{bar}$ SPARC ayrıştırmasından
  $\Upsilon_*=0{,}50$ ile kurulur. 96_ETG md. 4 zaten ETG'lerin daha yüksek $\Upsilon_*$
  isteyebileceğini ölçmüştü ($\approx 0{,}93$). Buradaki S0'lara $\Upsilon_*=0{,}50$ verilmesi
  $V_{bar}$'ı **düşük** gösterir ve çarpanı **şişirir** — yani farkın bir kısmı bu olabilir.
- $n=3$.

Bu, sınanabilir ve ucuz bir iş: S0'ları $\Upsilon_*=0{,}7$ ve $0{,}9$ ile tekrar oku.
Md. 7'de iş listesine girdi.

---

## 6. Dürüstlük kayıtları

1. **Yeni fit yapılmadı.** RMS, $\chi^2$, hata içi, $\Upsilon_*$ değerlerinin hepsi
   99_KARMASIK'ın kayıtlı sonuçlarıdır. Yalnız çarpan ve ivme yeniden hesaplandı.
2. **Öz denetim yapıldı.** Betik $V_{bar}^2$, $M_{kaps}$ ve $\ell_\omega$'yı sıfırdan kurup
   kayıtlı `DIS_evr_sapma_yuzde`'yi yeniden üretiyor; en büyük fark **0,043 puan** (CSV'nin
   0,1 yuvarlamasının içinde). Üretemezse betik **duruyor**.
3. **$n=3$ ve $n=5$.** Bu dosyadaki hiçbir medyan, altı sınıfın medyanlarıyla aynı ağırlıkta
   okunamaz. Zaten `99_KARMASIK`'a atılma sebepleri buydu ve o karar **doğruydu** — bu dosya
   o kararı geri almıyor, yalnız gizli kalanı görünür kılıyor.
4. **BCD örneklemi kirli** (4/5). Md. 0'daki tablo her okumada yanında durmalı.
5. **PGC51017'nin çarpanı bir sayı değil, alt sınır** ($<0{,}01$). Grafikte eksen dışında,
   ok ile. Silinmedi.
6. **UGC02487 iki modelde de kötü** (RMS 114,9 / 153,4). Bu galaksi hiçbir tarafın
   başarısı değil; $V_{max}\approx380$ km/s ile örneklemin en ağır sistemi ve $R$ 80 kpc'ye
   gidiyor. Ortalamaları tek başına oynatıyor.
7. **S0'lara $\Upsilon_*=0{,}50$ verildi** — altı sınıfla tutarlı olsun diye. Erken tipler için
   bu değer büyük olasılıkla **düşüktür** (md. 5) ve çarpanı şişirir. Yani S0 satırı teorinin
   aleyhine **fazla** okunuyor olabilir; ölçülmedi.

---

## 7. Ne çıktı — üç cümle

1. **Açık duran çarpan saçılması 2,6 kattan 6,1 kata çıkıyor** (×1,47–8,90). 97_BTFR md. 2
   bu sekiz galaksiyle belirgin biçimde **ağırlaştı.**
2. **S0 tarafı temiz ve yine de ×5,48 istiyor** — örneklem kalitesiyle savunulamaz.
   BCD tarafı kirli ama temiz olan tek galaksi en yükseğini istiyor (×11,91).
3. **İvme hipotezi burada da zayıf:** iki tip de 95_RAR eğiliminin 3–4 katı çarpan istiyor.

## 8. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **S0'ları $\Upsilon_*=0{,}7$ ve $0{,}9$ ile tekrar oku** | md. 5 — 96_ETG ile üç kat farkın en olası sebebi; ucuz ve sınanabilir |
| 2 | UGC02487'yi ayrı incele | md. 6.6 — iki modelde de başarısız, sebebi bilinmiyor |
| 3 | PGC51017'yi eğiklik/mesafe duyarlılığıyla sına | md. 4 — tek ters işaretli sapma; $Q=3$ ama açıklanmalı |
| 4 | BCD'leri daha temiz bir kaynakla (SPARC dışı) tekrarla | md. 0 — 4/5 kirli, sonuç bu hâliyle taşınamaz |

**Madde 1 en verimli.** Doğru çıkarsa hem 96_ETG ile fark kapanır, hem S0'ın ×5,48'i düşer,
hem de 97_BTFR md. 2'nin bandı daralır. Yanlış çıkarsa açık daha da netleşir — iki durumda da
bilgi kazanılır.
