# Yöntem — 99_KARMASIK / öngörü vs fit

Üreten betik: `sinif_ongoru_vs_fit.py` · Çıktı: `SONUC.csv`, `ongoru_vs_fit.png`

## Dört eğri

| # | Eğri | Serbest parametre | Girdiler |
|---|---|---|---|
| 1 | **ÖLÇÜM** | — | SPARC `Rotmod_LTG`, gerçek hata çubukları |
| 2 | **Standart bilim öngörüsü** | **0** | $\Upsilon_*=0{,}50$; $M_*=\Upsilon_*L_{3,6}$; $M_{200}\leftarrow$ abundance matching (Moster+2013); $c_{200}\leftarrow$ Dutton & Macciò 2014 |
| 3 | **Evrenakı öngörüsü** | **0** | $\Upsilon_*=0{,}50$; yerel biçim $v_{F4}^2=\sqrt{a_0\mathcal{G}M_{kaps}(R)}$; $a_0=1{,}75\,cH_0/16{,}1=7{,}39\times10^{-11}$ m/s² (nihai, 86_NIHAI) |
| 4 | Evrenakı fit | 2 | $\Upsilon_*$, $b$ |
| 5 | ΛCDM fit | 2 | $\Upsilon_*$, $M_{200}$ |

Öngörülerin ikisi de **dönüş eğrisine bakmadan** kurulur. Ortak girdi $\Upsilon_*=0{,}50$
(3,6 μm popülasyon sentezi orta değeri) — adil olması için her ikisinde aynı.

## Denklemler

Baryonik katkı (her ikisinde ortak, SPARC ayrıştırmasından):

$$V_{bar}^2 = \mathrm{sgn}(V_{gaz})V_{gaz}^2 + \Upsilon_* V_{disk}^2 + 1{,}4\,\Upsilon_* V_{kovan}^2$$

Kapsanan kütle:

$$M_{kaps}(R) = \Upsilon_* L_{disk}(R) + 1{,}4\,\Upsilon_* L_{kovan}(R) + M_{gaz}(R),
\qquad M_{gaz}(R)=\frac{R\,\mathrm{sgn}(V_{gaz})V_{gaz}^2}{\mathcal{G}}$$

Evrenakı (nihai kurulum): $\;v^2 = V_{bar}^2 + \sqrt{a_0\,\mathcal{G}M_{kaps}(R)}$
(eşdeğer yazım: $\mathcal{G}M_{kaps}/\ell_\omega^{etkin}(R)$, $\ell_\omega^{etkin}=\sqrt{\mathcal{G}M_{kaps}/a_0}$)

ΛCDM: $\;v^2 = V_{bar}^2 + v_{NFW}^2(R;M_{200},c_{200})$

## Dürüstlük kaydı — hiçbir öngörü "saf" değildir

| Büyüklük | Statü |
|---|---|
| $a_0$ ($7{,}39\times10^{-11}$ m/s²) | biçimi türetilmiş ($\mathcal{G}m_n/\ell_\omega^2$), değeri SPARC'a **kalibre**; çapraz doğrulamada katsayı $\pm$%40 oynar |
| $c_{200}$–$M_{200}$ katsayıları | N-cisim simülasyonlarına **fitlenmiş** iki sayı |
| Abundance matching | gözlemsel kütle fonksiyonuna **fitlenmiş** dört sayı |
| $\Upsilon_*=0{,}50$ | IMF varsayımına bağlı bandın **orta değeri**, ölçülmüş bir sayı değil |

Yani bu, "türetim vs türetim" değil **"kalibre edilmiş öngörü vs kalibre edilmiş öngörü"**
karşılaştırmasıdır. İki taraf bu bakımdan denktir ve karşılaştırma bu nedenle adildir.

## Ölçütler

- `rms` — modelin ölçümden RMS sapması (km/s), ağırlıksız
- `chi2ind` — $\chi^2/(N-k)$; öngörüler için $k=0$, fitler için $k=2$
- `hataici` — model noktalarının kaçı ölçüm hata çubuğunun içinde ($|z|\leq1$)

`chi2ind`'in öngörüde $k=0$ ile hesaplandığına dikkat: öngörü hiç parametre harcamadığı için
bütün noktalar serbestlik derecesidir.
