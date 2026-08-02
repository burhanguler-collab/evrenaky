# 10.7 Türetim Zincirinin Denetimi (Galaksi İçi)

Doğrulama programının amacı yalnız uyum ölçmek değildir: **kalibre edilmiş her sayıyı teorinin kendi yapısından türetmeye** çalışmak ve türetilemeyenin yerini tam olarak söylemektir. Bu bölüm o zincirin dört halkasıdır.

## 10.7.1 $\ell_\omega$ yerel kütleden kurulur — ve galaksi içinde sınanır

F4 teriminin vortisite uzunluğu $\ell_\omega=q_n/2\gamma_n$ bir **akı oranıdır** ve galaktik etkin uzunluk, kapsanan kütleden kurulur — akı teoremi gereği: $R$ yüzeyinden geçen dolanım, $R$ içindeki maddeden doğar:

$$\ell_\omega^{etkin}(R)=\sqrt{\frac{\mathcal{G}M_{kaps}(R)}{a_0}}\;\Longrightarrow\;v_{F4}^2=\sqrt{\mathcal{G}M_{kaps}(R)\,a_0}$$

Bu biçim üç bağımsız ölçümle sınanmıştır (141 galaksi, fit yok, yeni parametre yok):

| Ölçüm | Sonuç | Teorinin dediği |
|---|---|---|
| Kütle üssü: $\ell_\omega\propto M^p$ | $p=\mathbf{0{,}506}$ | 0,500 ✓ |
| Yarıçap izi: $d\log(\ell_\omega^{ölç}/\ell_\omega^{yasa})/d\log R$ | $\mathbf{-0{,}025}$ | 0 ✓ |
| Dönüş eğrisi RMS'ine etkisi | **−19 %** (102/141 galakside iyileşme) | — |

![Yerel ℓ_ω sınavı](Gorseller/k10_yerel_lomega.png)

**Yarıçap izi sonucun kalbidir:** yasa doğru kütleyle kurulduğunda, ölçülen $\ell_\omega$'nın yasaya oranı galaksinin içinde yarıçap boyunca hiçbir sistematik iz bırakmaz ($-0{,}025$, saçılma 0,091 dex). Sıfır serbest parametreli bir yapısal öngörü, 125 galakside 0,025 hassasiyetle doğrulanmıştır.

## 10.7.2 Tutarlılık kütlesi türetilir: $M_{tut}=m_n$

Kısım 6'nın türetiminde (6.5.4.3) Stokes toplamı, nükleon dolanımlarının nasıl hizalandığına bağlıdır. En genel hâl: dolanım vektörleri hizalı değilse halkadan geçen net dolanım bir **rastgele yürüyüştür**, $\Gamma_{etkin}=\gamma_n\sqrt{N}$. Bu, zincire konduğunda iki kapalı sonuç verir:

$$\boxed{\;a_0=\frac{\mathcal{G}\,m_n}{\ell_\omega^{2}}\;}\qquad\text{ve}\qquad\boxed{\;M_{tut}=m_n\;}$$

**Ortam, mikro dolanımları tek bir nükleondan öteye hizalı toplayamaz.** $M_{tut}$ apriori $10^{-30}$–$10^{60}$ kg arasında herhangi bir değer olabilirdi; sıfır parametreli türetim onu nükleon kütlesine sabitler.

**Ölçümü** ($a_0$ hiç kullanılmadan, 133 galakside): $\ell_\omega^{etkin}$ dönüş eğrisinden doğrudan çözülüp $\sqrt{N}$'e bölündüğünde

| Ölçüt | Değer |
|---|---|
| $\ell_\omega^{mikro}$ medyanı | **35,7 fm** — nükleer ölçek; proton yük yarıçapının ~42 katı |
| Kütleyle korelasyonu (3,8 decade) | Spearman $\mathbf{+0{,}029}$ — **gerçekten sabit** |
| Galaksi içi saçılma | 0,090 dex |
| Köprü üssü: $d\log\ell_\omega^{etkin}/d\log N$ | **0,503** (türetim: 0,500) |
| $M_{tut}=a_0\ell_\omega^2/\mathcal{G}$ | **0,84 $m_n$** — sıfır parametreli öngörünün beşte biri içinde |

![M_tut sınavı](Gorseller/k10_m_tut.png)

Galaktik $\ell_\omega^{etkin}$'in galaksiden galaksiye **beş mertebe** yayılmasının tamamı $\sqrt{N}$ çarpanıdır; mikro oran sabittir. Kalan %16'lık fark türetim katsayılarının ($2\pi$, $4\pi$, hizalanma dağılımı) defterindedir ve kapatılmamıştır — bu bir *mertebe ve yapı* doğrulamasıdır, hassas doğrulama değil.

## 10.7.3 $a_0$'ın biçimi ve son serbestlik

Türetimle birlikte $a_0$'ın statüsü kesinleşir: **biçimi türetilmiştir** ($\mathcal{G}m_n/\ell_\omega^2$ — üç mikro sabitin bileşkesi), sayısal değeri gözlemle sabitlenir, ve **kozmik zamanla değişmez** (sınavı 10.9'dadır). Türetim $a_0$'ın $\rho_n$ bağımlılığını da verir — birinci kuvvet: $a_0=C\gamma_n^2/(\pi\rho_n q_n)\propto\rho_n^{-1}$; $cH_0$ mertebesiyle bugünkü sayısal örtüşme rastlantı olarak kaydedilir.

Teorinin kalan tek galaktik serbestliği artık adresiyle bellidir: **nükleonun iki kolunun debi oranı** $q_n/\gamma_n=2\ell_\omega^{mikro}\approx7\times10^{-14}$ m. Kürsel kaynak geometrisinde bu, radyal pulsasyon hızının teğetsel dolanım hızına oranına çevrilir: $u_r/v_t\approx42$.

**Bu oran için aday kapanış kayıtlıdır** (Blok H türetimi **M-45**): kafes-atomu kaydından (deplasman kafesi atomun tamamıdır) pulsasyon kolunu $m_e$, dolanım kolunu $m_p$ taşır; eş-güç **türetilmiştir** — izoklinik kilit Ek A.2'nin $\sqrt2$'sinden çıkar (iki düzlem ayrı ayrı kavrama sınırında doyar), medyan-H kilidi ($X>0{,}5$ → medyan hidrojen değerine kilitlenir) bileşim-kararlılığını açıklar, ve eşbölüşümün termalleşme koşulu **36 mertebe marjla** hesaplanıp kapanmıştır (kanal enerjisi $m_pc^2$; sızıntı ~0,8 milyon yıl; banyo teması $10^{-23}$ s). Sonuç: $u_r/v_t=\sqrt{m_p/m_e}=42{,}85$ — ölçülenle %1,1 (fark medyan hatasının içinde; **oran tam olmalı**); $\ell_\omega=36{,}05$ fm ve $a_0=\mathcal{G}m_nm_e/(m_pr_n^2)=8{,}6\times10^{-11}$ m/s², **sıfır kalibrasyonla** beş-ölçüm bandının içinde. $\sqrt2c$ çapasıyla mutlak debiler de sayısallaşır: $\gamma_n=2{,}24\times10^{-6}$ m²/s, $q_n=1{,}62\times10^{-19}$ m³/s, $C=2{,}35$ kg·m⁻³·s⁻¹ — Blok H'nin "tek serbest çift"i çözülür. Statüsü **[T-aday]**: başka-yere-bakma dar uzayda ~$2\sigma$, geniş uzayda %40 — [S] rozeti, kalan **iki dış koşula** kadar korunur: bağımsız $\ell_\omega$ ölçümü (medyan 36,0 fm + tür-ayrımlı ikinci mod ~51 fm) ve hakem denetimi (G-9).

![a₀ köprüsü — mikro ve kozmik okuma](Gorseller/k10_a0_kopru.png)

## 10.7.4 $\mathcal{G}$ yerel mi? — işaret doğru, dejenerasyon yapısal

Teoride $\mathcal{G}=\alpha/\rho_n$ ve $\rho_n$ ortamın yerel yoğunluğudur; sabit $c$'nin olmadığı bir kuramda (Postülat 4) $\mathcal{G}$ de evrensel sabit olamaz. Öngörü: yoğun bölgede $\mathcal{G}$ düşmelidir. Ölçüm (737 nokta, 110 galaksi, fit yok):

| Ölçüt | Değer |
|---|---|
| $\mathcal{G}_{yerel}/G$ medyanı | **0,930** — genel ölçek doğru |
| Yüzey yoğunluğuyla eğim | $\mathbf{-0{,}093}$ dex/dex (Spearman $-0{,}305$; dört kesitte kararlı) |

![G yerel sınavı](Gorseller/k10_g_yerel.png)

**İşaret teorinin öngördüğü işarettir** — ama iki kayıt hükmü sınırlar: (1) $\mathcal{G}$ ile $\Upsilon_*$ bu yöntemle **ayrılamaz** ve ayrılamama yapısaldır (F4'ün ihmal edilebilir olduğu bölge zaten yıldız-baskındır; gaz kaldıracı doğmaz). (2) Yine de iki açıklamadan biri fizikle uyumsuzdur: sapmayı $\Upsilon_*$ ile açıklamak, 3,6 μm'de yoğun bölgelerin daha yaşlı (daha yüksek $\Upsilon_*$'lı) olması gerçeğiyle **ters işaret** ister; $\mathcal{G}=\alpha/\rho_n$ istemez. Teorinin $\rho_n(\Sigma_{bar})$ bağıntısını nicel vermesi, bu sınavı işaret kontrolünden ölçüme çevirecek açık iştir.

## 10.7.5 Tutarlılık yasasının atom çekirdeği yapısı

Rastgele yürüyüşün bağımsız birimi nedir? Cevap $\ell_\omega$'nın fiziksel anlamından çıkar: komşunun hissettiği dolanım/pulsasyon alan oranı $v_t/v_r=d/\ell_\omega$'dir — $\ell_\omega$, yönsüz pulsasyon bölgesinden yönlü dolanım bölgesine **geçiş yarıçapıdır.** Ve ölçülen 35,7 fm, doğanın bir ölçek boşluğuna düşer: en büyük çekirdek 7,4 fm, çekirdekler arası mesafe her fazda (beyaz cüce dahil) $\geq2{,}7\times10^3$ fm. Dolayısıyla **aynı çekirdeğin nükleonları daima korele, farklı çekirdekler daima bağımsızdır: tutarlılık kümesi atom çekirdeğidir** — maddenin fazından bağımsız olarak (gaz-kafes sınavının null'unun öngörüye dönüşmesi; 10.6.1).

Rastgele yürüyüş çekirdekler üzerinden işleyince $\Gamma_{etkin}=\gamma_n\sqrt{N_c N}$, $M_{tut}=N_c m_n$ ve pencere parametresiz çıkar:

$$N_c\in[\,X,\;\langle A\rangle\,]\approx[\,0{,}71\,;\;2{,}2\,]$$

(taban: eşlenme sönmesi — çift-çift çekirdekler sıfırlanır, kalan hidrojen kütle kesri $X$; tavan: tam iç uyum, $\langle A\rangle=\sum X_jA_j$.)

![Sınıf bandının mekanizma taraması — hedefler, kanal ayrımı, yasa denemesi](Gorseller/k10_tutarlilik.png)

**Sınav — üç isabet:** (a) morfolojik sınıf bandının tamamı (Im 0,65 … Sd 1,55) pencerenin içindedir — 10.2.4'ün "açıklanmamış bandı" çekirdek istatistiğinin izin verdiği aralık çıkar; (b) tabanın keskin öngörüsü $M_{tut}=X\,m_n\approx0{,}72\,m_n$, ölçülen 0,84 ile **%15 içinde** — 10.7.2'nin kapanmayan farkının ana kalemi; (c) en çalkantılı sınıf (Im) tam tabanda oturur ($\lambda\approx0$), ana sınıflar kısmi hizalanma kesri $\lambda=0{,}14$–$0{,}68$ ile pencere içindedir.

**$\lambda$'nın yeri de türetilmiştir**: enerji kilidi ($\sim$MeV'e karşı $\sim$500 eV) $\lambda$'yı çekirdek-içi olmaktan çıkarır — o, ortamın **çekirdekler-arası dolanım muhasebesidir.** Ortalama polarizasyonun ölçümden gelen sınırı ($\varepsilon<3\times10^{-35}$; $\ell_\omega^{mikro}$'nun 3,8 mertebelik kütle-değişmezliği) $\sqrt{N}$ yasasını dolanım korunumunun **teoremi** yapar. Belirleyici aday, ortamın kaskad karakteridir: kalın/3B çalkantı söndürür ($\lambda\to0$ — Im tam tabanda), ince/soğuk yarı-2B disk korur ve disk ekseni boyunca örgütler ($\lambda>0$ — tavan Sd, literatürün "süper-ince" sınıfı). Bu çerçevede $\lambda\leq1$ zorunludur. **HI-$\sigma$ eşleştirme sınavının ilk turu koşulmuştur** (THINGS + VLA-ANGST + LITTLE THINGS, 18 galaksi): Spearman $+0{,}49$ (tek yönlü $p=0{,}019$), kaldıraç tam öngörülen yerde — en çalkantılı sistemler en küçük çarpanları taşıyor. Ardışık-analiz çekincesiyle bu bir **ilk anlamlı işarettir**, doğrulama değil. **Açık kalanlar:** nicel $\lambda$(incelik) bağıntısı, $n\gtrsim40$'lık kayıt-öncesi doğrulama ve uçların (S0/BCD, $\lambda\approx1{,}6$; $n=3$–4) temiz örneklemde 1'in altına inip inmediği.

![σ sınavı — k, diskin dinamik soğukluğunu izliyor (18 galaksi)](Gorseller/k10_vsigma.png)

## 10.7.6 Zincirin özeti

| Halka | Önce | Sonra |
|---|---|---|
| $\ell_\omega$'nın kuruluşu | toplam $M_{bar}$ | **yerel $M_{kaps}(R)$** — akı teoremi + galaksi-içi sınav (yarıçap artığı $-0{,}025$) |
| $\ell_\omega$'nın doğası | "sabit değil, yayılıyor" | **mikro sabit** (35,7 fm) × $\sqrt{N}$; fiziksel anlamı: alan geçiş yarıçapı |
| $M_{tut}$ | tanımsız | **$=N_c m_n$, türetilmiş**; taban $X\,m_n\approx0{,}72$ — ölçülen 0,84 (%15) |
| Tutarlılık kümesi | varsayım (saf rastgele) | **atom çekirdeği** — pencere $[X,\langle A\rangle]$, sınıf bandı içinde |
| $a_0$ | kalibre ivme, mikro karşılıksız | **biçimi türetilmiş**: $\mathcal{G}m_n/\ell_\omega^2$; değişmez |
| Kalan serbestlik | $a_0$ (1 sayı) | $q_n/\gamma_n$ (1 sayı) + pencere-içi konum $\lambda$ — **ikisinin de adresi teorinin kendi yapısında** |
