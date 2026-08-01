# 94_YEREL_LOMEGA — Yöntem

Üreten betik: `../../yerel_lomega_sinavi.py` · Sonuçlar: [`CALISMA.md`](CALISMA.md)

## 1. İki kurulum

Tek fark $\ell_\omega$'nın hangi kütleden kurulduğudur. Başka hiçbir şey değişmez —
$a_0$, $\Upsilon_*$, $R_B$, $V_{bar}$ ayrıştırması, kütle integrali, hepsi aynı.

| | $\ell_\omega$ | $v_{F4}^2$ |
|---|---|---|
| **A** (mevcut) | $\sqrt{\mathcal{G}M_{bar}/a_0}$ — galaksinin tamamı | $\mathcal{G}M_{kaps}(R)\big/\sqrt{\mathcal{G}M_{bar}/a_0}$ |
| **B** (yerel) | $\sqrt{\mathcal{G}M_{kaps}(R)/a_0}$ — yarıçap içi | $\sqrt{\mathcal{G}M_{kaps}(R)\,a_0}$ |

Her iki kurulumda da $v^2 = V_{bar}^2 + v_{F4}^2$.

$a_0 = cH_0/16{,}1$ — **[S] kalibre**, oynatılmadı. Sabitler `sinif_ongoru_vs_fit.py`,
`btfr_sinavi.py`, `etg_sinavi.py`, `rar_sinavi.py` ile birebir aynı.

## 2. Kütle ve $V_{bar}$ kurulumu

`sinif_ongoru_vs_fit.py`'den birebir kopyalandı:

```
Vbar2 = sign(Vg)·Vg² + Υ*·Vd² + R_B·Υ*·Vb²        Υ* = 0,50 · R_B = 1,4
Mgas  = max(R·sign(Vg)·Vg²/𝒢 , 0)
Mkaps = Υ*·L(SBd) + R_B·Υ*·L(SBb) + Mgas          L: kümülatif yüzey parlaklığı integrali
Mbar  = Mkaps[-1]
```

Örneklem: 01–06 sınıflarının tamamı, **141 galaksi.** Seçim yok, eşik yok.

## 3. $\ell_\omega$'nın doğrudan ölçümü — $a_0$ kullanmadan

Her galakside her yarıçapta:

$$\ell_\omega^{ölç}(R) = \frac{\mathcal{G}M_{kaps}(R)}{v_{gözl}^2 - V_{bar}^2}$$

Bu bir çözümdür, fit değil: iki terimli denklem $\ell_\omega$ için tersine çevrilir. Ne $a_0$
girer, ne bir parametre uydurulur.

**Süzgeçler ve gerekçeleri:**

| Süzgeç | Neden |
|---|---|
| $v^2 - V_{bar}^2 > 1$ (km/s)² | negatif fark → $\ell_\omega$ tanımsız |
| F4 payı $> 0{,}40$ | düşük payda ölçüm kötü koşullu (96_ETG md. 3 kuralı, burada daha sıkı) |
| $M_{kaps} > 10^{-3} M_{bar}$ | **en iç noktada $M_{kaps}\to 0$** olur, $\ell_\omega^{ölç}\to 0$, $\log$ eğimini şişirir |
| $R_{max}/R_{min} > 1{,}5$ | tek decade'in altında eğim ölçülemez |

Üçüncü satır bir kez hataya yol açtı: koruma yokken A'nın eğimi $+1{,}26$ çıkıyordu, doğrusu
$+0{,}56$. Koruma betikte yorumla birlikte duruyor.

### Yasa sınavı

Ölçülen $\ell_\omega$, kurulumun varsaydığına bölünür ve **yarıçapa göre** eğimi alınır:

$$\text{eğim} = \frac{d\log\left(\ell_\omega^{ölç}/\ell_\omega^{yasa}\right)}{d\log R}$$

Yasa doğruysa bu **sıfırdır** — artıkta yarıçap izi kalmaz. A için $+0{,}558$, B için
$-0{,}025$.

## 4. Gereken $a_0$ çarpanı

$a_0 \to k\,a_0$ olunca her iki kurulumda da yalnız F4 terimi $\sqrt{k}$ ile ölçeklenir
($V_{bar}^2$ hiç ölçeklenmez). Kapalı formül yoktur; dış yarıdaki ortalama sapmayı sıfırlayan
$k$ **ikiye bölmeyle** çözülür (200 iterasyon, $k\in[10^{-4},10^4]$).

Tanım `sinif_carpan_duzeltme.py` ile **aynıdır** (oranların ortalaması) — A ile B ve altı
sınıfla karşılaştırılabilsin diye.

> ⛔ Naif $10^{-4\Delta}$ formülü kullanılmadı; gerekçesi
> [04_cok_gec_spiral](../04_cok_gec_spiral/CALISMA.md) düzeltme kaydında.

## 5. RAR artığı

Kendi dönüş eğrilerimizden kurulur (Lelli'nin `_RAR.mrt` dosyasından değil):

$$g_{bar}=\frac{V_{bar}^2}{R},\qquad g_{gözl}=\frac{V_{gözl}^2}{R},\qquad
g_{öng}=\frac{v_{öng}^2}{R}$$

0,25 dex'lik kuşaklar, en az 25 nokta. Artık $\log(g_{öng}/g_{gözl})$; kuşak medyanlarına
doğrusal fit → **biçim eğimi.** 95_RAR aynı ölçütü Lelli'nin bağımsız dosyasında $+0{,}0836$
bulmuştu; buradaki A değeri $+0{,}1013$ — aynı mertebe, iki bağımsız veri yolu.

## 6. BTFR denetimi

Dış ölçüm noktasındaki $v_{öng}$ ile $\log M_{bar}$'a doğrusal fit. Amaç sonuç üretmek değil,
**A ile B'nin orada örtüştüğünü doğrulamak.** $M_{kaps}(R_{dış})/M_{bar}$ medyanı 1,000
olduğu için ikisi de 3,660 verir. (Bu sayı 97_BTFR'nin 3,632'sinden farklıdır: orada örneklem
$V_f$ ölçülmüş 121 galaksi, burada 141 galaksinin son noktası. Karşılaştırma A↔B içindir.)

## 7. Çıktı — `SONUC.csv`

Galaksi başına bir satır (141):

| Sütun | Anlamı |
|---|---|
| `A_rms`, `B_rms` | tüm eğri üzerinden öngörü RMS (km/s) |
| `kazanc_yuzde` | $100(B/A-1)$ — negatif = B daha iyi |
| `A_dis_sapma_yuzde`, `B_dis_sapma_yuzde` | dış yarıda ortalama işaretli sapma |
| `A_carpan`, `B_carpan` | sayısal çözülmüş gereken $a_0$ çarpanı, 4 hane |

## 8. Tekrarlanabilirlik

```bash
python yerel_lomega_sinavi.py
```

`SINIF_CALISMASI/94_YEREL_LOMEGA/` altına `SONUC.csv` ve `yerel_lomega.png` yazar.
Bağımlılık: `numpy`, `matplotlib`. Rastgelelik yok, fit yok; iterasyon yalnız çarpan
çözümündedir (deterministik ikiye bölme).

## 9. Bu yöntemin sınırı

Betik **B'nin teoriden çıktığını göstermez** — yalnız B'nin veriyle A'dan tutarlı olduğunu
ölçer. $\ell_\omega=q_n/2\gamma_n$'nin yarıçap bağımlılığının M-38'den türetilmesi ayrı bir
iştir ve yapılmamıştır (CALISMA.md md. 6.1). Ayrıca $V_bar$ hâlâ SPARC'ın evrensel Newton
$G$'siyle hesaplanmış bir dış girdidir (md. 6.5).
