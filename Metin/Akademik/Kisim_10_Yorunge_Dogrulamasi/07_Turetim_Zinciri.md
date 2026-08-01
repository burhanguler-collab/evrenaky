# 10.7 Türetim Zinciri — $M_{tut}=m_n$, Mikro $\ell_\omega$, $a_0$'ın Biçimi, $\mathcal{G}$'nin Yerelliği

*(Hesaplar: `CALISMA/yerel_lomega_sinavi.py`, `CALISMA/m_tut_sinavi.py`, `CALISMA/a0_kopru_sinavi.py`, `CALISMA/g_yerel_sinavi.py` · kayıtlar: `94_YEREL_LOMEGA/` (+`TURETIM.md`), `92_M_TUT/`, `91_A0_KOPRU/`, `93_G_YEREL/`)*

Doğrulama programının amacı yalnız uyum ölçmek değildir: **kalibre edilmiş her sayıyı teorinin kendi yapısından türetmeye** çalışmak ve türetilemeyenin yerini tam olarak söylemektir. Bu bölüm o zincirin dört halkasıdır.

## 10.7.1 $\ell_\omega$ yerel kütleden kurulur — ve galaksi içinde sınanır

F4 teriminin vortisite uzunluğu $\ell_\omega=q_n/2\gamma_n$ bir **akı oranıdır**; $R$ yüzeyinden geçen akı, akı teoremi gereği $R$ **içindeki** maddeden doğar. Dolayısıyla galaktik etkin uzunluk kapsanan kütleyle kurulur:

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

Teorinin kalan tek galaktik serbestliği artık adresiyle bellidir: **nükleonun iki kolunun debi oranı** $q_n/\gamma_n=2\ell_\omega^{mikro}\approx7\times10^{-14}$ m. Kürsel kaynak geometrisinde bu, radyal pulsasyon hızının teğetsel dolanım hızına oranına çevrilir: $u_r/v_t\approx42$. Bu oranı üretecek ikinci denklem teoride henüz yoktur — onu yazmak, nükleonun ortamdaki kaynak modelini kurmak demektir ve açık iştir (10.10). Serbestliğin *sayısı* değişmemiştir (bir); *yeri* değişmiştir: makroskopik, teoride karşılıksız bir ivmeden, teorinin kendi yapısının ($\omega_1/\omega_2$ kolları) üretmesi gereken bir mikro orana.

![a₀ köprüsü — mikro ve kozmik okuma](Gorseller/k10_a0_kopru.png)

## 10.7.4 $\mathcal{G}$ yerel mi? — işaret doğru, dejenerasyon yapısal

Teoride $\mathcal{G}=\alpha/\rho_n$ ve $\rho_n$ ortamın yerel yoğunluğudur; sabit $c$'nin olmadığı bir kuramda (Postülat 4) $\mathcal{G}$ de evrensel sabit olamaz. Öngörü: yoğun bölgede $\mathcal{G}$ düşmelidir. Ölçüm (737 nokta, 110 galaksi, fit yok):

| Ölçüt | Değer |
|---|---|
| $\mathcal{G}_{yerel}/G$ medyanı | **0,930** — genel ölçek doğru |
| Yüzey yoğunluğuyla eğim | $\mathbf{-0{,}093}$ dex/dex (Spearman $-0{,}305$; dört kesitte kararlı) |

![G yerel sınavı](Gorseller/k10_g_yerel.png)

**İşaret teorinin öngördüğü işarettir** — ama iki kayıt hükmü sınırlar: (1) $\mathcal{G}$ ile $\Upsilon_*$ bu yöntemle **ayrılamaz** ve ayrılamama yapısaldır (F4'ün ihmal edilebilir olduğu bölge zaten yıldız-baskındır; gaz kaldıracı doğmaz). (2) Yine de iki açıklamadan biri fizikle uyumsuzdur: sapmayı $\Upsilon_*$ ile açıklamak, 3,6 μm'de yoğun bölgelerin daha yaşlı (daha yüksek $\Upsilon_*$'lı) olması gerçeğiyle **ters işaret** ister; $\mathcal{G}=\alpha/\rho_n$ istemez. Teorinin $\rho_n(\Sigma_{bar})$ bağıntısını nicel vermesi, bu sınavı işaret kontrolünden ölçüme çevirecek açık iştir.

## 10.7.5 Zincirin özeti

| Halka | Önce | Sonra |
|---|---|---|
| $\ell_\omega$'nın kuruluşu | toplam kütle (tutarsız) | **yerel $M_{kaps}(R)$** — yarıçap izi sıfır |
| $\ell_\omega$'nın doğası | "sabit değil, yayılıyor" | **mikro sabit** (35,7 fm) × $\sqrt{N}$ |
| $M_{tut}$ | tanımsız | **$=m_n$, türetilmiş**; ölçülen 0,84 $m_n$ |
| $a_0$ | kalibre ivme, mikro karşılıksız | **biçimi türetilmiş**: $\mathcal{G}m_n/\ell_\omega^2$; değişmez |
| Kalan serbestlik | $a_0$ (1 sayı) | $q_n/\gamma_n$ (1 sayı) — **adresi teorinin kendi yapısında** |
