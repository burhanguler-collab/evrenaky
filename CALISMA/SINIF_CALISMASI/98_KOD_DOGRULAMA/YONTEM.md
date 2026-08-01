# Yöntem — kod doğrulama

Üreten betik: `../../kod_dogrulama.py` · Çıktılar: `SONUC.csv`, `dogrulama.png`

## Referans veri

**Li P., Lelli F., McGaugh S. S., Pawlowski M. S., Zwaan M., Schombert J. M.** —
*The Halo Mass Function of Late-Type Galaxies from HI Kinematics.*
Dosya: SPARC sitesinden `WP50_M200.mrt` → `veri/_WP50_M200.mrt` (175 galaksi).

| Sütun | Ne |
|---|---|
| `WP50`, `e_WP50` | HI çizgi genişliği (%50 tepe akısında) ve hatası |
| `log(M_NFW)`, hata | **NFW** profiliyle fitlenmiş halo kütlesi |
| `log(M_Ein)`, hata | **Einasto** profiliyle |
| `log(M_DC14)`, hata | **DC14** (geri-besleme ile değiştirilmiş) profiliyle |

Halo kütlesi $R_{200}$'de tanımlı (karanlık madde yoğunluğu $=200\times$ kritik yoğunluk) —
**bizim tanımımızla aynı.**

**Ayrıştırma uyarısı:** `.mrt` dosyaları **belirteç (token) tabanlı** okunur, sabit genişlikle
değil. Gerekçe: SPARC ana kataloğunda sütun başlığı ile veri satırları arasında bir bayt kayma
vardır ve sabit genişlikli okuma **sessizce** yanlış sonuç verir — ana kataloğun `T` sütununda
bu hata bir kez yapıldı ve tip dağılımı denetlenerek yakalandı.

## Bizim fitimiz — sınıf çalışmasının geri kalanıyla birebir aynı

$$v^2(R) = V_{bar}^2(\Upsilon_*) + v_{NFW}^2(R;M_{200},c_{200})$$

$$V_{bar}^2 = \mathrm{sgn}(V_{gaz})V_{gaz}^2 + \Upsilon_* V_{disk}^2 + 1{,}4\,\Upsilon_* V_{kovan}^2$$

- Serbest: $\Upsilon_*$ (sınır $0{,}05$–$2{,}0$) ve $\log M_{200}$ (sınır $7$–$13{,}5$)
- $c_{200} \leftarrow$ Dutton & Macciò 2014, **saçılma yok** (tam dayatılmış)
- $D$ ve $i$ katalog değerlerinde **sabit**
- Yöntem: en küçük kareler (`scipy.optimize.curve_fit`), önsel **yok**
- Hata: `errV`, taban 1 km/s; noktalar **bağımsız** sayıldı

## Karşılaştırma ölçütü

Galaksi başına $\Delta = \log_{10}M_{200}^{\text{bizim}} - \log M_{NFW}^{\text{yayınlanmış}}$ (dex).
Ayrıca yayınlanmış hataya normalize edilmiş $z = \Delta / e_{\log M_{NFW}}$.

## Sıfır fark beklenmez — bilinen yöntem farkları

| Li ve ark. | Biz |
|---|---|
| MCMC örneklemesi | en küçük kareler |
| $\Upsilon_*$ için lognormal önsel | düz sınır |
| $c$–$M$ saçılması serbest (0,11 dex) | tam dayatılmış |
| $D$, $i$ için Gauss önsel | sabit |

Bu nedenle **aranan şey sıfır fark değil, korelasyonun sıkı olmasıdır.** Ölçek olarak
yayınlanmış üç halo modelinin kendi arasındaki saçılma kullanılır:

| Karşılaştırma | Medyan | Saçılma |
|---|---|---|
| NFW – Einasto | $+0{,}060$ dex | 0,245 dex |
| NFW – DC14 | $-0{,}040$ dex | 0,151 dex |

Bizim saçılmamız bu mertebedeyse implementasyon sağlıklı; kat kat üstündeyse değil.

## Sonuç

Saçılma **0,815 dex** — halo modelini tamamen değiştirmenin yarattığının **3–5 katı**.
Medyan sapma yayınlanmış hata çubuklarının **2,8 katı.** Sebep önsel yokluğu; tanı
[`CALISMA.md`](CALISMA.md) madde 3'te. **Doğrulama geçilmedi.**

## SONUC.csv sütunları

`Galaksi · Tip · Q · N · Vmax_kms · BIZIM_logM200 · BIZIM_Ystar · BIZIM_chi2ind · BIZIM_rms ·
YAY_logM_NFW · YAY_hata · FARK_dex · FARK_sigma · YAY_logM_Einasto · YAY_logM_DC14`

`FARK_dex` ve `FARK_sigma` dışındaki bütün `YAY_*` sütunları **yayınlanmış değerlerdir**, bu
çalışmada hesaplanmamıştır. `BIZIM_*` sütunları bu çalışmanın çıktısıdır.
