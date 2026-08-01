# 96_ETG — Yöntem

Üreten betik: `../../etg_sinavi.py` · Sonuçlar: [`CALISMA.md`](CALISMA.md)

## 1. Veri

| Dosya | İçerik | Kaynak |
|---|---|---|
| `veri/_etg.mrt` | **16 erken tip galaksi**, her biri için iki ivme noktası | Lelli+2017 (ApJ 836, 152) Tablo 2 |
| `veri/_RAR.mrt` | **2693 disk noktası** ($g_{bar}$, $g_{obs}$ ve hataları) | Lelli+2017 Şekil 2'nin arkasındaki veri |

`_etg.mrt` sütunları: `Dist errD M Inc erI L[3.6] errL Reff SBeff Rexp SBexp` +
`Aobs1 eAobs1 Aobs2 eAobs2 Abar1 eAbar1 Abar2 eAbar2`. İvmeler $\log_{10}$ m/s²'dir.
İndis 1 = HI halkasının **iç** kenarı, 2 = **dış** kenarı.

**Ayrıştırma kuralı:** `L[3.6]` SPARC birimiyle $10^9 L_\odot$'dir; `* 1e9` zorunludur.
(Bu tuzak [97_BTFR](../97_BTFR/CALISMA.md) panelinde bir kez hataya yol açtı.)
Okuma **belirteç tabanlıdır** (`split()`), sabit genişlikli değil.

## 2. Teorinin öngörüsü

M-37 merkezcil dengesi:

$$a_{tam} = a_{bar} + \frac{\mathcal{G}M}{\ell_\omega R}, \qquad
\ell_\omega = \sqrt{\frac{\mathcal{G}M}{a_0}}$$

$\mathcal{G}M = a_{bar}R^2$ konur:

$$g_{öng} = g_{bar} + \sqrt{g_{bar}\,a_0}$$

- $a_0 = cH_0/16{,}1 = 4{,}224\times10^{-11}$ m/s² — **[S] kalibre**, bu sınavda oynatılmadı.
- Sabitler `btfr_sinavi.py` ile **birebir** aynıdır (aynı $c$, $H_0$, 16,1, aynı birim çevrimi).
- $g_{bar}$ **ölçülendir**, hesaplanmaz. Bu yüzden $\Upsilon_*$ öngörüye hiç girmez.

### Ne fitlenmedi
Hiçbir şey. Galaksi başına 2 nokta vardır; bir serbest parametre uydurmak için gereken
serbestlik yoktur. Bu, betiğin bir tercihi değil, verinin bir özelliğidir.

## 3. Gereken $a_0$ çarpanı — sayısal çözülür

$a_0 \to k\,a_0$ olunca:

$$g_{öng} = g_{bar} + \sqrt{k}\,\sqrt{g_{bar}a_0}$$

$g_{bar}$ (F1) **ölçeklenmez.** İki terimli olduğu için kapalı formül yoktur; medyan
$\log(g_{öng}/g_{gözl})=0$ koşulu **ikiye bölmeyle** (200 iterasyon, $k\in[10^{-3},10^3]$)
çözülür. Aynı gerekçe ve aynı yöntem `btfr_sinavi.py`'de de kullanılır.

**Geçerlilik eşiği.** Çarpan yalnız F4'ün öngörüye katkısının anlamlı olduğu yerde okunabilir:

$$\frac{\partial \log g_{öng}}{\partial \log k} = \frac{1}{2}\cdot\frac{F4}{g_{bar}+F4}$$

Dış noktada pay 0,52 → çarpan anlamlı. İç noktada 0,10 → çarpan **kötü koşullanmış**, sayı
olarak raporlanmaz (CALISMA.md md. 3).

## 4. Karşı taraf — ΛCDM zinciri

$M_* \to M_{200}$ (Moster+2013: $\log M_1{=}11{,}59$, $N{=}0{,}0351$, $\beta{=}1{,}376$,
$\gamma{=}0{,}608$) $\to c_{200}$ (Dutton & Macciò 2014) → NFW kapsanan kütle → $a_{DM}(R)$.
Sıfır serbest parametre. Sonra $g_{ΛCDM} = g_{bar} + a_{DM}$.

**Yarıçap geri çözümü (yalnız ΛCDM için gerekli):**
$R = \sqrt{\mathcal{G}M_*/g_{bar}}$, $M_* = \Upsilon_* L_{3,6}$, $\Upsilon_*=0{,}70$.
Bu değer disk çalışmasının çekirdek değeriyle tutarlıdır ($R_B\Upsilon_* = 1{,}4\times0{,}50$).

Çıkan yarıçaplar: iç medyan 1,0 kpc ($0{,}8\,R_{eff}$), dış medyan 12,1 kpc ($7{,}5\,R_{eff}$),
aralık 7,2–25,7 kpc. Lelli+2017'nin ETG HI halkaları tipik olarak 5–30 kpc'dir → **makul**,
ama doğrulanmadı.

**$\Upsilon_*$ duyarlılığı** (yalnız ΛCDM'i etkiler):

| $\Upsilon_*$ | ΛCDM dış nokta medyan | TEORİ dış nokta medyan |
|---|---|---|
| 0,50 | $+0{,}027$ | $-0{,}090$ |
| 0,70 | $+0{,}045$ | $-0{,}090$ |
| 0,90 | $+0{,}069$ | $-0{,}090$ |

Teori sütunu **sabittir** — $g_{bar}$ ölçüldüğü için.

## 5. Disk RAR karşılaştırması

Disk noktaları aynı $g_{öng}$ formülüyle, aynı ölçütle işlenir. Üç kesit raporlanır:
tümü (2693), ETG-dış ivme aralığı (1553), ETG-iç ivme aralığı (195). Aralık kısıtı
**zorunludur**: ETG dış noktaları disklerin ortalamasından yüksek ivmededir, kısıtsız
karşılaştırma iki farklı rejimi kıyaslar.

## 6. İstatistik

- **Spearman** sıra korelasyonu (elle, `scipy` bağımlılığı yok).
- $n=16$'da 2σ çözünürlüğü $\lvert\rho\rvert \approx 2/\sqrt{n-1} = 0{,}52$ olarak alındı ve
  her korelasyon sonucunun yanında **basıldı.**
- Merkezî eğilim için **medyan**, yayılım için standart sapma (dex).
- Ortalama kullanılmadı: $n=16$'da tek bir uç değer medyanı oynatmaz, ortalamayı oynatır.

## 7. Çıktı sütunları — `SONUC.csv`

| Önek | Anlamı |
|---|---|
| `YAY_` | **Yayınlanmış** — Lelli+2017'den olduğu gibi ($g_{bar}$, $g_{obs}$ ve hataları) |
| `TEORI_` | Teorinin öngörüsü ve gözlemden farkı (dex) |
| `KUR_` | **Yeniden kurulmuş** — geri çözülen yarıçap (md. 4). Ölçüm değildir. |
| `LCDM_` | ΛCDM zincirinin öngörüsü |

Satırlar $L_{[3,6]}$'ya göre büyükten küçüğe sıralıdır.

## 8. Tekrarlanabilirlik

```bash
python etg_sinavi.py
```

Betik `SINIF_CALISMASI/96_ETG/` altına `SONUC.csv` ve `etg.png` yazar. Dış bağımlılık:
`numpy`, `matplotlib`. Rastgelelik yok, fit yok, iterasyon yalnız çarpan çözümündedir
(deterministik ikiye bölme).
