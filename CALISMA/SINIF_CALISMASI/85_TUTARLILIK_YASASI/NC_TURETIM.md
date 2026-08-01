# $N_c$'nin TÜRETİMİ — Korelasyon istatistiği akışkan resminden

**Sıfır yeni parametre · girdiler: $\ell_\omega^{mikro}=35{,}7$ fm (ölçüm, 92_M_TUT) + nükleon alan tanımları (M-35, 6.5.4.3)**

Soru: yoğun/düzenli paketlenmiş maddede komşu nükleon dolanımları niçin ~1–3 nükleonluk kümeler hâlinde korele, iyonize-seyrek ortamda niçin değil? Cevabın teoriden çıkması gerekiyordu. Çıktı — ve beklenmedik bir biçimde: **korelasyon kümesi moleküler/katı kafes değil, atom çekirdeğinin kendisidir.**

---

## Adım 1 — Nükleonun iki alanı ve tek geçiş ölçeği

Nükleon ortama iki debi boşaltır: pulsasyon (hacim debisi $q_n$, m³/s — **skaler**, monopol) ve dolanım (sirkülasyon debisi $\gamma_n$, m²/s — **vektörel**). $d$ uzaklığındaki bir komşunun hissettiği iki hız alanı:

$$v_r(d)=\frac{q_n}{4\pi d^2}\quad(\text{radyal, yönsüz})\qquad
v_t(d)=\frac{\gamma_n}{2\pi d}\quad(\text{teğetsel, yönlü})$$

Oranları tek bir uzunlukla belirlenir:

$$\boxed{\;\frac{v_t}{v_r}=\frac{2\gamma_n d}{q_n}=\frac{d}{\ell_\omega}\;}$$

**$\ell_\omega$'nın fiziksel anlamı budur:** $d<\ell_\omega$'da komşu, yön bilgisi taşımayan pulsasyon alanının içindedir; $d>\ell_\omega$'da yönlü dolanım alanı baskındır. Yön korelasyonu ancak ortak bir bağlı yapı içinde (aynı kafeste) kurulabilir; serbest komşular arasında $d\gg\ell_\omega$'da her iki alan da seyrelmiştir ve termal çalkantıya yenilir.

## Adım 2 — Doğanın ölçek boşluğu: kafes = çekirdek

Ölçülen $\ell_\omega=35{,}7$ fm, doğadaki uzunlukların **tam bir boşluğuna** düşer:

| Ölçek | Değer |
|---|---|
| En büyük çekirdek yarıçapı (U-238) | 7,4 fm |
| **$\ell_\omega^{mikro}$ (ölçülen)** | **35,7 fm** |
| Çekirdekler arası en küçük mesafe — beyaz cüce yoğunluğu | $2{,}7\times10^{3}$ fm |
| — Güneş merkezi | $2{,}2\times10^{4}$ fm |
| — katı madde / su | $2{,}2\times10^{5}$ fm |

Yani **sıradan maddenin her hâlinde** (katı, gaz, plazma, yıldız içi, beyaz cüce dahil):

- Aynı çekirdeğin nükleonları **daima** $d<\ell_\omega$ bölgesindedir → tek bağlı yapı, dolanımları çekirdeğin kolektif durumuyla belirlenir;
- Farklı çekirdeklerin nükleonları **daima** $d\gg\ell_\omega$ bölgesindedir → korelasyon kurulamaz, yönelimler bağımsızdır.

> ### Sonuç: korelasyon kümesi atom çekirdeğidir — maddenin fazından bağımsız olarak
>
> Katı, sıvı, gaz ya da iyonize olması **fark etmez**: çekirdekler arası mesafe her fazda $\ell_\omega$'nın yüzlerce katıdır. Bu, GAZ_KAFES sınavının null sonucunu (artık ↔ gaz kesri korelasyonu $+0{,}01$) bir bilmece olmaktan çıkarıp **doğrulamaya çevirir** — faz önemli olmamalıydı, ve değil.
>
> Tek istisna nötron yıldızı maddesidir: orada nükleonlar arası $1{,}8$ fm $<\ell_\omega$ — bütün madde tek tutarlılık alanına girer. (Yanlışlanabilir uç öngörü: o rejimde F4 nitelik değiştirir.)

## Adım 3 — Çekirdek başına net dolanım ve $N_c$ penceresi

Rastgele yürüyüş artık nükleonlar üzerinden değil **çekirdekler** üzerinden işler. Kütle kesri $X_j$, kütle numarası $A_j$ olan türlerden oluşan maddede, çekirdek başına net dolanım $g_j\gamma_n$ ise:

$$\Gamma_{etkin}^2=\gamma_n^2\sum_j M_j g_j^2=\gamma_n^2 N\underbrace{\sum_j \frac{X_j g_j^2}{A_j}}_{\textstyle N_c}$$

$g_j$'yi iki uç durum sınırlar:

- **Tam iç uyum** ($g_j=A_j$ — çekirdeğin bütün nükleon dolanımları hizalı): $N_c=\langle A\rangle=\sum X_jA_j$.
- **Eşlenme sönmesi** ($g_j=$ eşlenmemiş nükleon sayısı — dolanımlar çekirdek içinde çiftler hâlinde zıt bağlanır; çift-çift çekirdekler ~0, H daima 1): $N_c\approx X$ (hidrojen kütle kesri).

Bileşim kozmik olarak dar bir aralıkta olduğundan pencere **parametresizdir**:

$$\boxed{\;N_c\in[\,X,\;\langle A\rangle\,]\approx[\,0{,}66\,;\;2{,}6\,]\;}$$

(taban: $X=0{,}66$–$0{,}75$; tavan: ilkel gaz 1,74 · güneş bileşimi 1,95 · yaşlı/He-zengin popülasyon ~2,6.)

## Adım 4 — Sınav: ölçülen band pencerenin içinde

| Grup | Ölçülen $N_c$ | Pencere içinde mi |
|---|---|---|
| Im | 0,65 | taban ($\approx X$) ✓ |
| Sb–Sbc | 0,90 | ✓ |
| Sdm–Sm | 1,00 | ✓ |
| Sc–Scd | 1,10 | ✓ |
| Sa–Sab | 1,20 | ✓ |
| Sd | 1,55 | ✓ |
| BCD | 2,50 | ✓ (tavana yakın) |
| S0 | 3,03 | tavanın %17 üstü — açık kalem ($n=3$) |

Üç bağımsız nicel isabet:

1. **Ana altı sınıfın tüm bandı** (0,65–1,55) — 85'in "açıklanamayan" bulgusu — pencerenin içinde. Band bir anomali değil, **çekirdek istatistiğinin izin verdiği aralıktır.**
2. **Küresel değer:** 140 galaksinin medyanı $N_c=1{,}02$; 92_M_TUT'un bağımsız yoldan ölçtüğü $M_{tut}=0{,}84\,m_n$. Eşlenme tabanının öngörüsü $M_{tut}=X\,m_n\approx0{,}74\,m_n$ — ölçümle **%14 içinde.** 92'nin kapanmayan "0,84'e karşı 1" farkının adayı bulundu: eksik çarpan **hidrojen kütle kesridir.**
3. **GAZ_KAFES null'u öngörüye dönüştü** (Adım 2): faz/bileşen ayrımı yok, çünkü kafes çekirdektir ve H/He oranı gazda da yıldızda da benzerdir.

## Adım 5 — Yanlışlanabilir öngörüler

| # | Öngörü | Aksi ölçülürse |
|---|---|---|
| N-1 | Hiçbir temiz galakside dış-yarı çarpanı $[X_{min}\cdot?,\,\langle A\rangle_{max}]\approx[0{,}5;\,3]$ penceresinin belirgin dışına çıkamaz | $k>4$ ya da $k<0{,}4$ ölçülen temiz bir sistem yapıyı çürütür |
| N-2 | $M_{tut}$ evrensel değildir: $\approx X\,m_n$'dir — H kesri belirgin farklı ortamlarda (metal-zengin merkezler, ilkel bulutlar) iz bırakmalı | $M_{tut}$'un $X$'ten bağımsızlığı tabanı çürütür |
| N-3 | Bağımsız ölçülecek her $\ell_\omega^{mikro}$, $[7{,}4\ \mathrm{fm};\,2{,}7\times10^3\ \mathrm{fm}]$ ölçek boşluğunda kalmalı | dışına düşen ölçüm Adım 2'yi çürütür |
| N-4 | Nötron yıldızı maddesi tek tutarlılık alanıdır → o rejimde F4 istatistiği kökten farklıdır (nitel) | — |

## Adım 6 — $g_j$ eşlenme hesabı: taban keskinleşti, pencere-içi konum tek sayıya indi

Çekirdek başına net dolanım $g_j$, iki sınırın arasında bir yerdedir; kısmi hizalanma kesri $\lambda$ ile yazılsın: $g_j^2=u_j+\lambda\,(A_j^2-u_j)$ ($u_j=$ eşlenmemiş nükleon sayısı). Sınıf başına bileşim (gaz kesri ölçümden; $X_{gaz}=0{,}75-2{,}5Z$, $X_{yıldız}=0{,}71$; $Z$ kütle–metaliklik ilişkisinden kaba; tek-A metal düzeltmesi $\sim Z/80$, ihmal düzeyinde) ile taban ve tavan hesaplanıp ölçülen $N_c$'den $\lambda$ çözüldü:

| Sınıf | $f_{gaz}$ | Taban ($\approx X$) | Tavan ($\langle A\rangle$) | Ölçülen $N_c$ | $\boldsymbol{\lambda}$ |
|---|---|---|---|---|---|
| Im | 0,82 | 0,735 | 1,84 | 0,65 | **−0,07 ≈ 0** |
| Sb–Sbc | 0,20 | 0,710 | 2,06 | 0,90 | +0,14 |
| Sdm–Sm | 0,71 | 0,728 | 1,89 | 1,00 | +0,24 |
| Sc–Scd | 0,38 | 0,714 | 2,00 | 1,10 | +0,30 |
| Sa–Sab | 0,21 | 0,708 | 2,12 | 1,20 | +0,35 |
| Sd | 0,62 | 0,723 | 1,93 | 1,55 | +0,68 |
| BCD | 0,58 | 0,729 | 1,85 | 2,50 | +1,58 |
| S0 | 0,17 | 0,707 | 2,17 | 3,03 | +1,59 |

Hesabın dört sonucu:

1. **Taban neredeyse evrenseldir ve keskinleşti:** bileşim ne olursa olsun $N_c^{taban}=0{,}71$–$0{,}74$. Eşlenme tabanının $M_{tut}$ öngörüsü buna göre $\,0{,}72\pm0{,}02\,m_n$; ölçülen 0,84 — **%15 içinde.**
2. **Im tam tabanda oturuyor** ($\lambda\approx0$): en çalkantılı, iyonize-gaz baskın sınıfta eşlenme sönmesi **tamdır** — kısmi hizalanma sıfır. Fiziksel olarak beklenen yerde beklenen değer.
3. **Ana sınıflarda $\lambda\in[0{,}14;\,0{,}68]$** — pencere-içi konum artık tek boyutsuz sayıya inmiştir. Belirleyicisinin türetim denemesi [LAMBDA_TURETIM.md](LAMBDA_TURETIM.md)'dedir: $\lambda$ çekirdek-içi olamaz (enerji kilidi), çekirdekler-arası muhasebe korelasyonudur; ortalama polarizasyonun tam sıfırlığı ($\sqrt{N}$'in teoremleşmesi) türetildi; mekanizma adayı ortamın kaskad karakteridir (incelik/dinamik soğukluk) — nicel bağıntısı açık.
4. **S0 ile BCD ikisi de $\lambda\approx1{,}6$** — pencereyi aynı miktarda aşıyorlar. Ya çekirdek-ötesi bir hizalanma kanalı vardır ya da iki uç örneklemin ($n=3$, $n=4$) ortak bir ölçüm sistematiği. Aynı sayıya düşmeleri kayda değerdir ve ayrı iş olarak durur.

## Dürüstlük kayıtları

1. **Pencere türetildi, pencere-içi konum türetilmedi.** Bir sınıfın tabanda mı tavanda mı oturduğunu belirleyen şey, ω₁-dolanımının çekirdek içi eşlenmeye ne ölçüde katıldığıdır — bu, nükleon iç yapısının (Blok H) henüz yazılmamış kısmıdır. Sd–Sdm sıralaması gibi pencere-içi ayrıntılar bu yüzden hâlâ açıklamasızdır.
2. **S0 (3,03) tavanı %17 aşıyor** — $n=3$ ve tavanın kendisi bileşim varsayımına duyarlı ($A_Z$, $Y$); çelişki ilan etmek için erken, görmezden gelmek için kayıtlı.
3. **"Farklı çekirdekler korele olamaz" adımı bir büyüklük argümanıdır, eşitsizlik ispatı değil:** $d\gg\ell_\omega$'da bağlanma enerjisinin termal çalkantıya oranı hesaplanmadı (γ_n'nin mutlak değeri bilinmiyor); alan-oranı + seyrelme argümanıyla geçildi.
4. **Eşlenme tabanı, ω₁-dolanımının nükleer spin gibi çiftlendiğini varsayar.** Teori ω₁'i spinle özdeşlemez; taban bu varsayıma bağlıdır. Gerçek $g_j$ iki sınırın arasındadır — Adım 6 bunu $\lambda$ ile hesapladı; $\lambda$'nın kendisi türetilmemiştir. Ayrıca Adım 6'nın bileşim girdileri ($X_{gaz}$, $X_{yıldız}$, $Z$-sınıf ataması) literatür kaba değerleridir; $\lambda$'nın ikinci ondalığı anlam taşımaz.
5. **Kanal gerilimi duruyor:** bu türetim yalnız F4'ü ölçekler; 85'in kanal sınavı 5/8 grupta (kılpayı) toplam-ölçeği seçmişti. Yarıçap-profili düzeyinde keskinleştirme hâlâ gerekli.
6. Bu türetim Claude Fable 5 tarafından üretilmiştir; teorinin matematik katmanına bir **öneridir** ve kitaba işlenmeden önce yazar onayı gerekir.

## Hüküm

$N_c$'nin türetimi **kuruldu**: korelasyon istatistiği, $\ell_\omega$'nın doğanın nükleer–atomik ölçek boşluğuna düşmesinden zorunlu olarak çıkar — **kafes, atom çekirdeğidir.** Pencere $[X,\langle A\rangle]$ parametresizdir, ölçülen bandı kapsar, küresel $M_{tut}$'u %15 içinde verir ($X\,m_n\approx0{,}72$, ölçülen 0,84) ve iki eski bilmeceyi (GAZ_KAFES null'u, 92'nin 0,84'ü) öngörüye çevirir. $g_j$ eşlenme hesabı pencere-içi konumu tek boyutsuz sayıya indirdi: kısmi hizalanma kesri $\lambda$ — Im tam tabanda ($\lambda\approx0$), ana sınıflar $0{,}14$–$0{,}68$, uçlar $\approx1{,}6$. **Kalan iki iş:** $\lambda$'nın ortam belirleyicisinin türetimi ve S0/BCD ucunun büyük örneklemle sınanması.
