# 07_S0_BCD — Yöntem

Üreten betik: `../../s0_bcd_sinavi.py` · Sonuçlar: [`CALISMA.md`](CALISMA.md)

## 1. Örneklem nasıl seçildi

`99_KARMASIK/GEREKCE.csv`'de `Tip` sütunu **S0** ya da **BCD** olan bütün galaksiler — 8 tane,
seçim yok, eşik yok. Sıralama: önce S0, sonra BCD, her biri kendi içinde alfabetik.

| Tip | n | Galaksiler |
|---|---|---|
| S0 | 3 | NGC4138 · UGC02487 · UGC06786 |
| BCD | 5 | NGC1705 · NGC2915 · NGC6789 · PGC51017 · UGCA281 |

**Temizlik ölçütü:** `Gerekce` alanında `Q=3` ya da `nokta` geçmiyorsa galaksi *temiz* sayılır —
yani yalnız tip kuralından düşmüş demektir. S0'ların 3/3'ü, BCD'lerin 1/5'i temiz.

## 2. Ne yeniden hesaplandı, ne okundu

| Okunan (99_KARMASIK'ın kaydı) | Yeniden hesaplanan |
|---|---|
| `ONG_evr_rms`, `ONG_lcdm_rms` | $V_{bar}^2$, $M_{kaps}$, $\ell_\omega$, F4 |
| `ONG_*_chi2ind`, `ONG_*_hataici` | gereken $a_0$ çarpanı (sayısal) |
| `FIT_evr_Ystar`, `FIT_lcdm_Ystar` | F4'ün $v^2$ içindeki payı |
| `ONG_lcdm_M200_Msun`, `ONG_lcdm_c200` | tipik ivme $g_{bar}$ (iki tanım) |
| `DIS_evr_sapma_yuzde` | dönüş eğrisi çizimleri (Evrenakı / ΛCDM / baryon) |

**Yeni fit yoktur.** Serbest parametre uydurulan hiçbir adım eklenmedi.

## 3. Öz denetim — zorunlu geçiş

Betik $V_{bar}^2$, $M_{kaps}$ ve $\ell_\omega$'yı `sinif_ongoru_vs_fit.py`'nin kurulumundan
**birebir** tekrarlar, sonra kayıtlı `DIS_evr_sapma_yuzde`'yi yeniden üretir:

$$\text{sapma} = \left\langle \frac{v_{öng}-V_{obs}}{V_{obs}} \right\rangle_{R>\text{medyan}(R)}$$

En büyük fark **0,043 puan** — CSV'nin `%+.1f` yuvarlamasının içinde. Fark 0,06'yı geçerse
betik `SystemExit` ile **durur** ve hiçbir çıktı yazmaz.

Kopyalanan kurulum:

```
Vbar2  = sign(Vg)·Vg² + Υ*·Vd² + 1,4·Υ*·Vb²          Υ* = 0,50
Mgas   = max(R·sign(Vg)·Vg²/𝒢 , 0)
Mkaps  = Υ*·L(SBd) + 1,4·Υ*·L(SBb) + Mgas            L: kümülatif yüzey parlaklığı
ℓ_ω    = √(𝒢·Mkaps[-1] / a₀)
v_öng  = √(Vbar2 + 𝒢·Mkaps/ℓ_ω)
```

$a_0 = cH_0/16{,}1$ — **[S] kalibre**, oynatılmadı. Sabitler `btfr_sinavi.py`, `etg_sinavi.py`,
`rar_sinavi.py` ve `sinif_carpan_duzeltme.py` ile birebir aynı.

## 4. Gereken $a_0$ çarpanı

$a_0 \to k\,a_0$ olunca $\ell_\omega \to \ell_\omega/\sqrt{k}$, yani **yalnız F4 terimi**
$\sqrt{k}$ ile ölçeklenir; $V_{bar}^2$ hiç ölçeklenmez. Kapalı formül yoktur:

$$\left\langle \frac{\sqrt{V_{bar}^2+\sqrt{k}\,F4}-V_{obs}}{V_{obs}} \right\rangle_{R>\text{medyan}} = 0$$

kökü **ikiye bölmeyle** çözülür (200 iterasyon, $k\in[10^{-4},10^4]$).

Tanım `sinif_carpan_duzeltme.py` ile **aynıdır** (oranların ortalaması, medyan log değil) — yoksa
altı sınıfla karşılaştırma iki farklı büyüklüğü kıyaslardı.

> ⛔ **Naif $10^{-4\Delta}$ formülü kullanılmadı.** O formül yalnız saf-F4 asimptotunda
> geçerlidir ve sınıf çalışmasında bir kez hataya yol açtı; kaydı
> [04_cok_gec_spiral](../04_cok_gec_spiral/CALISMA.md) düzeltme kutusunda.

**Sınır değerler sayı gibi gösterilmez.** `KG()` fonksiyonu: çözülemeyen → *"çözülemedi"*,
$k<0{,}01$ → *"<0,01"*. PGC51017 bu ikinci durumdadır.

## 5. Tipik ivme — iki tanım

| Sütun | Tanım |
|---|---|
| `g_bar_dis_nokta_ms2` | $V_{bar}^2(R_{son})/R_{son}$ — 97_BTFR'nin $V_{bar}$ okuma yarıçapıyla aynı |
| `g_bar_medyan_ms2` | $\mathrm{medyan}(V_{bar}^2/R)$ — eğrinin tamamı |

İkisi de yazılır, hiçbiri seçilmez. Grafik ve karşılaştırma tabloları **dış nokta** tanımını
kullanır (altı sınıfla tutarlı olsun diye); md. 3'teki 95_RAR karşılaştırması da öyle.

Birim çevrimi: $1\ (\mathrm{km/s})^2/\mathrm{kpc} = 10^6/3{,}0857\times10^{19}$ m/s².

## 6. ΛCDM eğrisi

$v_{ΛCDM} = \sqrt{V_{bar}^2 + v_{NFW}^2(R)}$, burada $M_{200}$ ve $c_{200}$
**99_KARMASIK'ın kaydından okunur** (Moster+2013 → Dutton & Macciò 2014 zinciri, sıfır serbest
parametre). Yeniden türetilmez.

## 7. Çıktı — `SONUC.csv`

Galaksi başına bir satır (8 satır). Öne çıkan sütunlar:

| Sütun | Anlamı |
|---|---|
| `temiz_ornek` | `evet` / `HAYIR` — md. 1'deki ölçüt |
| `99_KARMASIK_gerekcesi` | galaksinin oraya neden düştüğü, tam metin |
| `ONG_*` , `FIT_*` | 99_KARMASIK'tan **okunan** değerler |
| `F4_payi` | çarpanın okunabilirliğini belirler (eşik 0,25) |
| `carpan_DOGRU_sayisal` | ikiye bölme çözümü, 4 hane |
| `g_bar_dis_nokta_ms2`, `g_bar_medyan_ms2` | iki ivme tanımı |

## 8. Tekrarlanabilirlik

```bash
python s0_bcd_sinavi.py
```

`SINIF_CALISMASI/07_S0_BCD/` altına `SONUC.csv` ve `s0_bcd.png` yazar.
Bağımlılık: `numpy`, `matplotlib`. Altı sınıfla karşılaştırma paneli için
`_HESAPLAR/sinif_carpan_duzeltme.csv` gerekir; yoksa o panel boş kalır, betik yine çalışır.
Rastgelelik yok, fit yok.
