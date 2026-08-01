# 92_M_TUT — Tutarlılık kütlesi **türetildi**: $M_{tut}=m_n$ · Çalışma dosyası

**Sıfır serbest parametre · 133 galaksi · ölçümde $a_0$ hiç kullanılmadı**

Hesap: `../../m_tut_sinavi.py` · Çıktılar: [`SONUC.csv`](SONUC.csv) · [`m_tut.png`](m_tut.png)
Ön adım: [94_YEREL_LOMEGA/TURETIM.md](../94_YEREL_LOMEGA/TURETIM.md)

---

## 1. Türetim

[TURETIM.md](../94_YEREL_LOMEGA/TURETIM.md) açığı tek cümleye indirmişti: 6.5.4.3'ün **Adım 2**'si
nükleon dolanımlarının **birebir tutarlı** toplandığını *varsayar* —

$$\Gamma(R)=\frac{\gamma_n}{m_n}M_{kaps}(R)=\gamma_n N$$

— ve bu varsayım 6.5.4'ün kendi açık kalemleri arasında **gerekçelendirilmemiş** olarak kayıtlı.

**Nükleon dolanım vektörleri hizalı değilse**, halkadan geçen net dolanım bir rastgele
yürüyüştür:

$$\Gamma_{etkin}(R)=\gamma_n\sqrt{N}$$

Bunu Adım 4'e koyalım. $\mathcal{G}=Cq_n/4\pi\rho_n m_n \Rightarrow C/\rho_n=4\pi\mathcal{G}m_n/q_n$
ve $\ell_\omega=q_n/2\gamma_n \Rightarrow 2\gamma_n/q_n=1/\ell_\omega$:

$$a_{F4}=\frac{C}{\rho_n}\frac{\Gamma_{etkin}}{2\pi R}
=\frac{4\pi\mathcal{G}m_n}{q_n}\cdot\frac{\gamma_n\sqrt{M/m_n}}{2\pi R}
=\frac{\mathcal{G}\sqrt{M\,m_n}}{\ell_\omega R}$$

[94_YEREL_LOMEGA](../94_YEREL_LOMEGA/CALISMA.md)'nın B kurulumu $a_{F4}=\sqrt{\mathcal{G}Ma_0}/R$
diyordu. İkisini eşitleyelim:

$$\frac{\mathcal{G}\sqrt{Mm_n}}{\ell_\omega}=\sqrt{\mathcal{G}Ma_0}
\;\Longrightarrow\;
\boxed{\;a_0=\frac{\mathcal{G}\,m_n}{\ell_\omega^{2}}\;}
\qquad\text{ve}\qquad
\boxed{\;M_{tut}=m_n\;}$$

> ### Tutarlılık kütlesi **nükleon kütlesidir**
>
> Ortam, mikro dolanımları **tek bir nükleondan öteye** tutarlı toplayamıyor; ötesi rastgele
> yürüyüş. Bu, serbest parametre içermeyen bir sonuçtur — $M_{tut}$ apriori $10^{-30}$ ile
> $10^{60}$ kg arasında **herhangi bir şey** olabilirdi.

### Mikro ile galaktik arasındaki köprü

$$\ell_\omega^{etkin}(R)=\sqrt{\frac{\mathcal{G}M_{kaps}(R)}{a_0}}
=\ell_\omega^{mikro}\sqrt{N(R)}$$

Kitap 6.5.4.3'ün kutusu $\ell_\omega$'nın 0,22 kpc ile $2\times10^4$ kpc arasında, yani **beş
mertebe** değiştiğini kaydedip *"sabit değil, yasalı"* demişti. **Bu türetim o değişimin
tamamını $\sqrt{N}$ ile açıklar** — geriye kalan bir sabit olmalıdır.

---

## 2. Ölçüm — $a_0$ hiç kullanılmadan

$$\ell_\omega^{mikro}=\frac{\ell_\omega^{etkin}(R)}{\sqrt{N(R)}},\qquad
\ell_\omega^{etkin}(R)=\frac{\mathcal{G}M_{kaps}(R)}{v_{gözl}^2-V_{bar}^2}$$

| | |
|---|---|
| n | **133 galaksi** (F4 payı > 0,40) |
| $\ell_\omega^{mikro}$ medyan | $3{,}57\times10^{-14}$ m = **35,7 fm** |
| saçılma (galaksiler arası) | 0,171 dex |
| saçılma (galaksi **içinde**) | **0,090 dex** |
| aralık | 13,6 – 121,9 fm |

**Nükleer ölçekte bir uzunluk.** Proton yarıçapının ~42 katı.

---

## 3. Türetimin sınavı

| | $M_{tut}/m_n$ |
|---|---|
| **TÜRETİM ÖNGÖRÜSÜ** | **1,000** |
| ölçülen (F4 payı > 0,40) | **0,481** |
| duyarlılık: pay > 0,25 (n=140) | 0,518 |
| duyarlılık: pay > 0,55 (n=122) | 0,460 |
| duyarlılık: pay > 0,70 (n=94) | 0,379 |

**2,1 kat fark.** Bir büyüklüğün $10^{90}$ mertebelik bir aralıkta olabileceği yerde, sıfır
parametreli bir türetim onu iki kat içinde vuruyor.

Fark küçük değil ama **türetim defterinin içindedir**: zincirde $\ell_\omega=q_n/2\gamma_n$'nin
2'si, $2\pi Rh$'nin $2\pi$'si, $\mathcal{G}=Cq_n/4\pi\rho_n m_n$'nin $4\pi$'si var. Rastgele
yürüyüşün de tam katsayısı hizalanma dağılımına bağlıdır ($\langle\cos\theta\rangle$ türü bir
faktör). **2 katlık bir sapma bu kalemlerden herhangi biriyle kapanabilir; bu bir çürütme
değildir, ama bir doğrulama da değildir.**

---

## 4. Asıl sınav — $\ell_\omega^{mikro}$ gerçekten **sabit mi**?

Bir mikro sabitse galaktik hiçbir büyüklükle ilişkili olmamalı.

| | |
|---|---|
| Spearman[$\log\ell_\omega^{mikro}$, $\log M_{bar}$] | $\mathbf{+0{,}029}$ |
| $M_{bar}$ yayılımı | **3,8 decade** |
| Spearman[$\log\ell_\omega^{mikro}$, $\log\Sigma_*$] | $-0{,}140$ |

**Kütleyle ilişki sıfır.** Dört decade boyunca. Bu, "$\ell_\omega$ bir mikro sabittir"
iddiasının doğrudan doğrulanmasıdır — ve kitabın beş mertebelik değişim gözlemi yüzünden
**terk ettiği** iddianın geri gelmesidir.

### Köprü yasası

| | |
|---|---|
| $d\log\ell_\omega^{etkin}/d\log N$ ölçülen | $\mathbf{0{,}503}$ |
| türetimin öngördüğü | **0,500** |
| fark | $+0{,}003$ |
| $N$ aralığı | $3{,}0\times10^{64}$ – $2{,}8\times10^{68}$ (4,0 decade) |
| $\ell_\omega^{etkin}$ aralığı | 0,30 – 37 kpc |

$\sqrt{N}$ yasası, dört decade boyunca **0,003** hassasiyetle tutuyor.

### Sınıf sınıf

| Sınıf | n | $\ell_\omega^{mikro}$ (fm) | saçılma |
|---|---|---|---|
| Sa–Sab | 12 | 34,3 | 0,099 |
| Sb–Sbc | 25 | 36,5 | 0,170 |
| Sc–Scd | 29 | 35,6 | 0,145 |
| Sd | 16 | **30,1** | 0,118 |
| Sdm–Sm | 27 | 32,0 | 0,171 |
| Im | 24 | **43,9** | 0,201 |

**Band ×1,46** — $a_0$ cinsinden ×2,12. Bu, 97_BTFR md. 2'nin sınıf saçılmasının **aynısıdır**,
yalnız mikro dile çevrilmiştir. Yani o açık kalem **kapanmadı**; ama artık "galaksi başına
$a_0$ neden farklı" değil, **"nükleonun debi oranı neden sınıftan sınıfa %46 oynuyor"** sorusu.
İkincisi ilkinden çok daha dar bir sorudur — ölçme hatası, $\Upsilon_*$ ya da hizalanma
istatistiği ile açıklanabilir; ilki bir doğa sabitinin değişmesini gerektiriyordu.

---

## 5. Ne değişti — teorinin defteri

| | Önce | Şimdi |
|---|---|---|
| $a_0$ | **[S] kalibre** — $cH_0/16{,}1$, katsayı gözlemden | $\mathcal{G}m_n/\ell_\omega^2$ — **türetilmiş biçim**, tek girdi $q_n/\gamma_n$ |
| $\ell_\omega$ | "sabit değil, yasası var" (yasa kalibre) | **mikro sabit** — kütleyle Spearman $+0{,}03$ |
| Beş mertebelik $\ell_\omega$ değişimi | açıklanmamış | **tamamı $\sqrt{N}$** |
| Serbest parametre sayısı | $a_0$ (1) | $q_n/\gamma_n$ (1) — **sayı aynı** |

**Parametre sayısı azalmadı; yeri değişti.** Ama yer değişikliği önemlidir:

- $a_0$ makroskopik bir ivmeydi ve teorinin mikro katmanında **karşılığı yoktu.**
- $q_n/\gamma_n$ nükleonun $\omega_2$/$\omega_1$ kollarının oranıdır — teorinin **kendi
  yapısının** üretmesi gereken bir sayı (Blok H'nin iki kolu).
- Ve artık **sayısal bir hedefi var: 2ℓ_ω ≈ 7,1×10⁻¹⁴ m** (ölçülen), türetimin kitabın
  $a_0$'ıyla verdiği $1{,}03\times10^{-13}$ m'ye karşı.

> ### Kitapta düzeltilmesi gereken bir sayı
>
> 6.5.4.4'ün tablosu $q_n/\gamma_n=2\ell_\omega=4{,}36\times10^{20}$ m yazıyor. O sayı
> **galaktik** $\ell_\omega$'dan okunmuş; mikro oran değil. Doğrusu $\sim7\times10^{-14}$ m —
> **34 mertebe fark.** Aradaki fark tam olarak $\sqrt{N}$'dir.

---

## 6. Dürüstlük kayıtları

1. **$\sqrt{N}$ tek olası yorum değildir.** $\Gamma_{etkin}\propto\sqrt{M}$ başka
   mekanizmalarla da doğabilir (dolanımın bir üst sınıra doyması, $\gamma_n$'nin ortam
   yoğunluğuna bağlı olması). Rastgele yürüyüş **en basit** olandır, kanıtlanmış olan değil.
2. **2,1 katlık fark açıklanmadı** (md. 3). Türetim defterindeki katsayılarla kapanabilir
   ama hangisiyle kapandığı **gösterilmedi.** Bu yapılmadan "$M_{tut}=m_n$ doğrulandı"
   denemez; denebilecek olan "mertebe ve yapı doğrulandı"dır.
3. **Ölçüm B kurulumunu varsayar.** $\ell_\omega^{etkin}=\mathcal{G}M_{kaps}/(v^2-V_{bar}^2)$
   ifadesi doğrudan çözümdür ($a_0$ geçmez), ama $M_{kaps}$ ve $V_{bar}$ SPARC'ın
   $\Upsilon_*=0{,}50$ ayrıştırmasından gelir. $\Upsilon_*$ yanlışsa $\ell_\omega^{mikro}$ da
   kayar.
4. **$V_{bar}$ hâlâ evrensel Newton $G$'siyle hesaplanmış** — teori $\mathcal{G}$'nin değişken
   olduğunu söylerken. [93_G_YEREL](../93_G_YEREL/CALISMA.md) bunun mertebesini ölçtü
   (medyan 0,93, eğim $-0{,}093$); düzeltilmedi.
5. **Sınıf bandı ×1,46 duruyor.** Bu dosya onu açıklamıyor, yalnız yeniden adlandırıyor.
6. **$m_n$ olarak nötron kütlesi alındı** ($1{,}6749\times10^{-27}$ kg). Proton kütlesiyle
   fark %0,14 — sonuçta anlamsız.
7. **Noktalar bağımsız değil** ve galaksi başına medyan alındı; galaksiler arası 0,171 dex'in
   ne kadarı gerçek değişim, ne kadarı ölçüm hatası — ayrılmadı. Galaksi **içi** saçılmanın
   0,090 dex olması, hatanın önemli bir kısmının ölçümden geldiğini düşündürüyor.

---

## 7. Ne çıktı — üç cümle

1. **$M_{tut}=m_n$ türetildi** — 6.5.4.3 Adım 2'nin tutarlı toplanma varsayımı yerine
   rastgele yürüyüş konarak, sıfır serbest parametreyle. Ölçülen $0{,}48\,m_n$.
2. **$\ell_\omega$ bir mikro sabittir ve ölçüldü: 35,7 fm.** Kütleyle Spearman $+0{,}029$
   (3,8 decade). Kitabın "beş mertebe değişiyor" gözleminin tamamı $\sqrt{N}$'dir; köprü
   üssü 0,503 ölçüldü, türetim 0,500 diyor.
3. **$a_0$ artık kalibre bir ivme değil, türetilmiş bir biçimdir:** $a_0=\mathcal{G}m_n/\ell_\omega^2$.
   Serbestlik $a_0$'dan nükleonun $q_n/\gamma_n$ oranına taşındı.

## 8. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **$q_n/\gamma_n$'yi nükleon yapısından türet** ($\omega_1$/$\omega_2$, Blok H) | tek kalan serbestlik burası; hedef sayı $\sim7\times10^{-14}$ m |
| **2** | 2,1 katlık farkı türetim katsayılarından kapat (ya da kapanmadığını göster) | md. 6.2 |
| 3 | $\mathcal{G}m_n/\ell_\omega^2 = cH_0/16{,}1$ **rastlantısını** ele al | mikro ile kozmik arasında bir bağ iddia ediliyor; açıklanmalı ya da rastlantı ilan edilmeli |
| 4 | Kitapta $q_n/\gamma_n=4{,}36\times10^{20}$ m satırını düzelt | md. 5 kutusu — 34 mertebe hata |
| 5 | Sınıf bandını (×1,46) $\Upsilon_*$ ve eğiklik hatasıyla açıklamayı dene | md. 6.5 |

**Madde 3 kritik ve teorinin lehine bir fırsat.** $a_0$ artık iki ayrı yoldan yazılabiliyor:
mikro ($\mathcal{G}m_n/\ell_\omega^2$) ve kozmik ($cH_0/16{,}1$). İkisinin eşit olması ya bir
rastlantıdır ya da teorinin **mikro–kozmik köprüsüdür.** Eğer köprüyse, $H_0$ ile nükleon
yapısı arasında sınanabilir bir bağ doğar — ve bu, $a_0$'ın kozmik zamanla nasıl değiştiği
üzerinden **yanlışlanabilir.**
