# Yöntem — BTFR sınavı (v2)

Üreten betikler: `../../btfr_sinavi.py` (hesap + `btfr.png`) ve
`../../kur_etkilesimli_btfr.py` (`panel.html`)
Çıktılar: `SONUC.csv`, `btfr.png`, `panel.html`

`panel.html` aynı veriyi ve aynı formülleri kullanır; gereken $a_0$ çarpanını da aynı şekilde
(ikiye bölmeyle) çözer. Panelin ürettiği sayılar betiğin çıktısıyla denetlenmiştir: $V_f$ ×2,02 ·
dış yarının ortası ×1,73 · $W_{p20}$ $W/2$ ×4,72 / ham ×99,25 — **hepsi birebir aynı.**

Panelde **yalnız doğru kurulum** vardır: $v^2=V_{bar}^2+\mathcal{G}M_{bar}/\ell_\omega$. v1'in
terk edilen asimptotik kurulumu ve naif $10^{-4\Delta}$ çarpanı panele konmamıştır — ikisi de
yanlış hesaptır ve bir çalışma aracında seçilebilir durmamalıdır. İkisinin de kaydı aşağıda ve
`CALISMA.md`'nin düzeltme kaydında durur.

> **Sürüm uyarısı.** Bu dosyanın **v1'i teoriyi yalnız F4'ün asimptotik limitiyle sınadı** ve
> yanlış sonuç verdi. Gerekçe ve etkisi [`CALISMA.md`](CALISMA.md)'nin başındaki ⛔ düzeltme
> kaydındadır. v1'in sayıları (eğim 4,000 · gereken $a_0$ ×3,63) **kullanılmamalıdır.**

## Referans veri

**Lelli F., McGaugh S. S., Schombert J. M., Desmond H., Katz H.** — *The baryonic Tully-Fisher
relation for different velocity definitions and implications for galaxy angular momentum.*
Dosya: SPARC sitesinden `BTFR_Lelli2019.mrt` → `veri/_BTFR_Lelli2019.mrt` (**153 galaksi**).

| Sütun | Ne |
|---|---|
| `log(Mb)`, `e_log(Mb)` | baryonik kütle (yıldız $+$ gaz) ve hatası |
| `Inc`, `e_Inc` | varsayılan disk eğikliği |
| `Vf`, `e_Vf` | **düz (asimptotik) dönme hızı** |
| `V2exp`, `e_V2exp` | 2,2 eksponansiyel ölçek uzunluğunda hız |
| `V2eff`, `e_V2eff` | 2 etkin yarıçapta hız |
| `Vmax`, `e_Vmax` | azami dönme hızı |
| `Wp20`, `Wm50`, `Wm50c` $+$ hataları | HI çizgi genişlikleri |

> **Yayının Not 1'i:** *"These values assume a stellar mass-to-light ratio of 0.5 at 3.6 μm."*
> Yani yayınlanmış $M_b$, bu çalışmanın öngörülerinde kullanılan $\Upsilon_*=0{,}50$ ile
> hesaplanmıştır. **Bu sınavda $\Upsilon_*$ seçimi yoktur** — iki taraf aynı değeri kullanır.

**İkinci dosya:** `Rotmod_LTG` → `veri/*_rotmod.dat`. $V_{bar}$ buradan gelir, dolayısıyla
**rotmod dosyası zorunludur.**

**Örneklem daralması:** 153 → $V_f$ ölçülemeyen 30 düşer → rotmod eşleşmeyen 2 daha düşer →
**$n=121$.**

**Ayrıştırma:** `.mrt` dosyaları belirteç (token) tabanlı okunur, sabit genişlikle değil
(gerekçe: ana katalogda bir bayt kayma var ve sabit genişlik sessizce yanlış sonuç veriyor).

**SPARC kuralı:** bir hız alanı $0{,}0$ ise **ölçülememiştir**, sıfır değildir. Bu satırlar o
hız tanımından düşürülür — bu yüzden her tanımda $n$ farklı.

## Teorinin öngörüsü — sıfır serbest parametre

M-37 profil teoremi merkezcil dengedir ve **radyal ivmenin tamamını** alır. Teorinin galaktik
ölçekte iki radyal terimi vardır:

$$v^2(R) = \underbrace{V_{bar}^2(\Upsilon_*)}_{\text{F1 — pulsasyon, küresel akı}} \;+\; \underbrace{\frac{\mathcal{G}\,M_{kaps}(R)}{\ell_\omega}}_{\text{F4 — silindirik akı}}, \qquad \ell_\omega=\sqrt{\frac{\mathcal{G}M_{bar}}{a_0}}$$

$\ell_\omega$ yerine konunca ikinci terim sadeleşir:

$$\frac{\mathcal{G}M_{bar}}{\ell_\omega} = \sqrt{\mathcal{G}\,M_{bar}\,a_0}$$

Bu sınavda $R=R_{dış}$ (son ölçüm noktası) alınır ve orada $M_{kaps}\approx M_{bar}$ varsayılır:

$$\boxed{\;v_{öng}^2 = V_{bar}^2(R_{dış}) + \sqrt{\mathcal{G}\,M_{bar}\,a_0}\;}$$

**$V_{bar}$ nereden gelir:** SPARC `Rotmod_LTG`'nin bileşen hızlarından,

$$V_{bar}^2 = \mathrm{sgn}(V_{gaz})V_{gaz}^2 + \Upsilon_* V_{disk}^2 + 1{,}4\,\Upsilon_* V_{kovan}^2$$

Bunlar bileşenlerin **Newton** dönüş hızlarıdır. $\mathcal{G}=\alpha/\rho_n$ sayısal olarak
Newton'un $G$'sine eşit olduğu için bu, **F1'in ta kendisidir** — ve küresel yaklaşımdan
($\sqrt{\mathcal{G}M/R}$) daha doğrudur, çünkü disk geometrisini içerir.

### Terk edilen asimptotik sürüm

$R\gg\ell_\omega$ olsaydı $V_{bar}^2$ ihmal edilebilir ve

$$v^4=\mathcal{G}M_{bar}a_0 \;\Longleftrightarrow\; \log M_b = 4{,}000\log v + 2{,}251$$

çıkardı. **Bu varsayım geçersizdir:** ölçülen $\ell_\omega/R_{dış}$ medyanı $0{,}36$, aralığı
$0{,}13$–$1{,}61$, ve **6 galakside $\ell_\omega>R_{dış}$.** Betik bu sürümü yalnız
**karşılaştırma** olarak çizer.

| Girdi | Değer | Statü |
|---|---|---|
| $\mathcal{G}=\alpha/\rho_n$ | $4{,}300917\times10^{-6}$ kpc(km/s)²/M☉ | **T** teoriden |
| $a_0=cH_0/16{,}1$ | $4{,}224\times10^{-11}$ m/s² $=0{,}04224$ (km/s)²/kpc | **S** kalibre |
| $H_0$ | 70 km/s/Mpc | **Ö** gözlem |
| $\Upsilon_*$ | 0,50 (3,6 μm) | **Ö** yayınlanmış, iki tarafta aynı |
| $\Upsilon_{kovan}/\Upsilon_{disk}$ | 1,4 | **Ö** SPARC kuralı |

Birim denetimi: $v^4$ (km/s)⁴ $=$ [kpc(km/s)²/M☉] × M☉ × [(km/s)²/kpc] $=$ (km/s)⁴ ✓

## Gözlenen ilişkinin fiti

$\log M_b = a\log v + b$, **ağırlıklı** en küçük kareler, ağırlık $w=1/e_{\log M_b}^2$
(taban 0,02 dex). $M_b$ bağımlı değişken alınmıştır — hız hatası daha küçük olduğu için standart
pratik budur. **Ters regresyon ve dikey (ODR) fit yapılmamıştır**; eğim buna duyarlıdır
(ağırlıksız 3,530 · ağırlıklı 3,738 · yayınlanmış literatür $\sim3{,}85$).

## Gereken $a_0$ çarpanı — sayısal çözülür, formülle bulunmaz

Bu, v2'de düzeltilen **ikinci** hatadır. Naif formül

$$k = 10^{-4\Delta}, \qquad \Delta=\mathrm{med}\!\left[\log\frac{v_{öng}}{v_{ölç}}\right]$$

**yalnız saf-F4 asimptotunda** geçerlidir, çünkü orada $v\propto a_0^{1/4}$. Tam formülde
$a_0\to k\,a_0$ yapılınca $\ell_\omega\propto1/\sqrt{k}$ olur ve

$$v^2 = V_{bar}^2 + \sqrt{k}\,\sqrt{\mathcal{G}M_b a_0}$$

— **$V_{bar}^2$ hiç ölçeklenmez.** Dolayısıyla $k$, $\mathrm{med}[\log(v_k/v_{ölç})]=0$
denklemini sağlayan değer olarak **ikiye bölmeyle** çözülür (`a0_carpani`, 200 iterasyon,
logaritmik ortalama). Naif değer ×1,63, doğru çözüm **×2,02** verir; fark F4'ün $v^2$ içindeki
payından gelir (medyan 0,70; aralık 0,36–0,87). Betik ikisini de yazdırır ki formülün nerede
kırıldığı görülsün.

## ΛCDM zinciri — en yakın karşılık, sıfır serbest parametre

$$M_* = 0{,}5\times L_{3,6} \;\xrightarrow{\text{Moster+2013}}\; M_{200} \;\xrightarrow{\text{Dutton \& Macciò 2014}}\; c_{200} \;\longrightarrow\; V_{max}^{NFW}$$

NFW'nin azami hızı $x=r/r_s=2{,}1626$'da:

$$V_{max} = V_{200}\sqrt{\frac{0{,}2162\,c_{200}}{\mu(c_{200})}},\qquad \mu(x)=\ln(1+x)-\frac{x}{1+x},\qquad V_{200}=\sqrt{\frac{\mathcal{G}M_{200}}{R_{200}}}$$

**Uyarı:** ΛCDM BTFR'yi analitik olarak vermez; geri-besleme ayarıyla üretmesi gerekir. Bu zincir
**makul bir karşılık**, resmî bir ΛCDM öngörüsü değildir. Farklı $M_*$–$M_h$ ilişkisi ya da
farklı karakteristik hız ($V_{200}$, $V_{2{,}2}$) farklı eğim verir.

$M_*$ için `_sparc.mrt`'ten $L_{3,6}$ alınır ve aynı $\Upsilon_*=0{,}5$ uygulanır — BTFR
tablosuyla tutarlı olması için.

## Çizgi genişliği düzeltmesi

HI çizgi genişliği $W\approx2V_{rot}$'tur. Aynı yasa $W$ ile yazılırsa kesim
$4\log_{10}2=1{,}204$ dex kayar. **Ham `W` satırları teoriyle doğrudan karşılaştırılamaz:**
ham çarpanlar ×65–99 çıkar, $W/2$ ile ×2,7–4,7. Betik $W$ satırlarında otomatik olarak $W/2$
kullanır ve satırı `(W/2)` ile işaretler; ham değerler `CALISMA.md` madde 5'tedir.

## Ölçütler

- **Eğim** — gözlenen ilişki için (ağırlıklı ve ağırlıksız, ikisi de raporlanır)
- **$v_{öng}/v_{ölç}$** $= 10^{\Delta}$, medyan; teorinin hız açığı
- **Saçılma** — $\log(v_{öng}/v_{ölç})$'nin standart sapması (medyan çıkarılmış), yani teorinin
  *şeklinin* ne kadar iyi tuttuğu. Kütle dex'ine çevirmek için ×4.
- **Gereken $a_0$ çarpanı** — yukarıda anlatıldığı gibi **sayısal çözülür**
- **$\ell_\omega/R_{dış}$** — asimptot varsayımının geçerliliği

## Duyarlılık denetimleri (betik hepsini yazdırır)

1. **Sürüm karşılaştırması** — yalnız F4 vs F1+F4
2. **$V_{bar}$ okuma yarıçapı** — son nokta / bir içerisi / dış yarının ortası
3. **Yedi hız tanımı** — her biri ayrı $n$, eğim, saçılma, çarpan
4. **Naif vs çözülmüş $a_0$ çarpanı** — yan yana

## Dairesellik uyarısı

Kitabın $a_0$'ı SPARC **dönüş eğrilerine** kalibre edilmiştir (BTFR tablosuna değil). Dolayısıyla
doğrudan dairesellik yok. **Ama ikisi aynı gözlemlerden gelir** — bu, tam bağımsız bir sınav
değildir ve `CALISMA.md` madde 6.5'te öyle kaydedilmiştir.

## SONUC.csv sütunları

`Galaksi · Tip · YAY_logMb · YAY_elogMb ·` (yedi hız tanımı için `YAY_<hız>` ve `YAY_e<hız>`) `·
R_dis_kpc · Vbar_dis_kms · l_omega_kpc · l_om_bolu_R · TEORI_v_yalnizF4 · TEORI_v_TAM ·
FARK_dex_TAM · LCDM_Vmax_kms`

`YAY_*` sütunları **yayınlanmış değerlerdir**, bu çalışmada hesaplanmamıştır.
`R_dis`, `Vbar_dis` SPARC rotmod'dan **okunmuştur**. `l_omega`, `TEORI_*`, `FARK_*`, `LCDM_*`
bu çalışmanın çıktısıdır.
