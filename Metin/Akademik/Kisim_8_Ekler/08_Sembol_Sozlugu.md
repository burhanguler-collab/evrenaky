# Ek D — Sembol Sözlüğü ve Notasyon Kuralları

Bu ek, kitabın tamamında geçerli sembol standardını tanımlar. Her sembol kitap genelinde tek bir fiziksel büyüklüğü gösterir; standart fizikten aktarılan semboller çakışma durumunda indislenir. Kompakt özet için bkz. Bölüm 1.6.1.

## D.1 Notasyon Kuralları

Kitap boyunca **R-1 … R-11** rozetleriyle anılan notasyon kuralları aşağıdakilerdir; metinde "(R-6)" gibi bir atıf gördüğünüzde karşılığı bu listedeki aynı rozetli maddedir. Sembol çakışmalarının nasıl çözüldüğü ise **D.7**'deki **S-1 … S-27** kararlarındadır.

1. **`R-1` · Tek sembol, tek anlam.** Bir sembol kitabın her yerinde aynı fiziksel büyüklüğü gösterir; standart fizikten gelen bir sembolle çakışma varsa indislenir ve gerekçesi tanımlandığı yerde belirtilir.
2. **`R-2` · Frekans daima $\nu$** ile gösterilir. $f$ sembolü yalnızca Fizeau sürükleme katsayısı ($f = 1 - 1/n^2$) için ayrılmıştır.
3. **`R-3` · Kavrama Yasası eşitliktir ve aynı zamanda hâl denklemidir:** $c_0=\sqrt{P/\rho}$, yani $P=c_0^2\rho$. Bu, **stiff (Zel'dovich) akışkan** hâl denklemidir ve dalga kanalında geçerlidir (deplasman alanı sabit): $(\partial P/\partial\rho)_\chi=c_0^2$, dolayısıyla **akustik dalga hızı tam $c_0$**'dir. Ortamın $c_0$'yi aşan tepkisi sıkışmada değil **kohezyon kanalındadır** ($v_m$, M-5). *(Ek B.3'ün $k$'sı bu kanala ait değildir; o, sabit yoğunlukta işleyen **deplasman** sürecinin katsayısıdır ve $k=0$'dır — Ek M-44. Akustik hızı $c_0/\sqrt k$ biçiminde yazmak kategori hatasıdır.)*
4. **`R-4` · İşaret (kuyu) konvansiyonu:** Kütle çevresinde $dP/dr > 0$; itim ivmesi $\vec a = -\tfrac{1}{\rho_n}\nabla P$. $\nabla P$ tek başına "kuvvet" değildir; kuvvet $-\nabla P$ yönündedir. Skaler basınç farkı $\Delta P$ ile yazılır.
5. **`R-5` · Arka plan basıncı:** $P_0 = \tfrac14\rho_n c_0^2 = 6{,}07\times10^{33}$ Pa. Türetim zincirinde genel biçim $\tfrac{1-k}{4}\rho_nc^2$ yazılabilir, ama **$k=0$ artık türetilmiştir** (deplasman süreci yoğunluğu korur — Ek M-44), dolayısıyla sonuç kesindir; "$k$'ya duyarlı" kaydı geçersizdir. (Katsayı $\tfrac14$'tür çünkü ölçek yapısı $\delta c/c_0 = 2\,\delta f/f$ verir — bkz. Ek M-42.)
6. **`R-9` · Ondalık:** metin gövdesinde virgül; LaTeX bloklarında nokta kabul edilir.
7. **`R-10` · Ölçek ayrımı ($\Lambda$ ↔ $c_{loc}$):** "Yerel ışık hızı" tek büyüklük değildir. **Saat, cetvel ve atomik frekans** bağlamında daima madde ölçeği $\Lambda = 1-\Phi/c_0^2$ yazılır; **yayılım, bükülme, Shapiro ve $n_{eff}$** bağlamında daima yayılma hızı $c_{loc} = c_0\Lambda^2$ yazılır. İkisini tek büyüklüğe indirmek kategori hatasıdır — bkz. Ek M-42.

8. **İki eşik, iki kanal.** Ortamın $c_0$'yi aşan tepkileri **tek** bir eşiğe bağlanamaz; hangi olgunun hangi eşiğe ait olduğu karıştırılmamalıdır:

   | Kanal | Eşik | Yönettiği büyüklükler | Katalog |
   |---|---|---|---|
   | **Kavrama / patinaj** | $c_0=\sqrt{P/\rho}$ | dönme sürüklenme kesri $\xi$ | Ek M-40 (+M-42) |
   | **Kavitasyon / yırtılma** | $v_{kav}=\sqrt2c\sqrt{1+\Sigma/P_0}$ | öteleme artık sürüklemesi, $\tau_{ret}$, $\eta_E^{etkin}$ | Ek M-43 (+M-4) |

   Sürükleme kohezyon kanalının, $\xi$ ise kavrama kanalının büyüklüğüdür — adı da bunu söyler ("patinaj"). $\xi$'yi $v_{kav}$'a bağlama girişimi bu yüzden sayısal olarak tutmaz ve Bell alt sınırıyla çelişir. **Sıkışma kanalı** ise $c_0$'yi aşmaz: hâl denklemi stiff olduğundan akustik hız tam $c_0$'dir (kural 3). Deplasman ise bir hız değil, sabit yoğunlukta işleyen statik tepkidir ($k=0$) ve bu ikisinden ayrıdır.

9. **Kut'un sembolü yoktur — kasıtlı olarak.** Teorinin **varlık tabanı Kut, açıklama tabanı Zerre'dir** (1.1.3, 1.6): Kut hiçbir denkleme girmez, hiçbir gözlemsel sonuç ona dayandırılmaz. Bu yüzden Kut'a bu sözlükte kütle, yarıçap, yoğunluk veya açısal hız sembolü **tahsis edilmemiştir**. Gerekçe Anayasa Madde 21'dir: adlandırılmış her parametre, onu sabitleyecek bir gözlemle birlikte envantere girmek zorundadır; hiçbir gözleme bağlanmayan bir sembol "yama parametre" kapısı açardı. Sembolün yokluğu, açıklama tabanı kuralını kendiliğinden uygulatır — olmayan sembol yanlışlıkla bir denkleme sokulamaz.

10. **`R-6` · Sayısal sabitler tek değerden.** Aşağıdaki referans değerler kitap genelinde bağlayıcıdır; bir bölümde farklı hassasiyet gerekiyorsa yuvarlama "$\approx$" ile açıkça işaretlenir. Aynı büyüklüğün iki bölümde iki değerle geçmesi hatadır.

    | Büyüklük | Bağlayıcı değer |
    |---|---|
    | $\rho_n$ — nükleon öz yoğunluğu | $2{,}7\times10^{17}$ kg/m³ |
    | $m_z$ — Zerre kütlesi | $1{,}47\times10^{-35}$ kg |
    | $V_z$ ; $r_z$ — Zerre hacmi ve yarıçapı | $5{,}44\times10^{-53}$ m³ ; $2{,}35\times10^{-18}$ m |
    | $R_p$ — proton yarıçapı | $0{,}84$ fm |
    | $\rho_0$ — arka plan yoğunluğu ($k=0$) | $\approx6{,}8\times10^{16}$ kg/m³ |
    | $P_0$ — arka plan basıncı ($k=0$) | $\approx6{,}1\times10^{33}$ Pa |
    | $\sqrt2\,c_0$ — Zerre çevre hızı | $4{,}24\times10^{8}$ m/s |
    | $v_{ekvator}$ (proton) | $\approx5\times10^{8}$ m/s $\approx1{,}67\,c_0$ |
    | Dünya ekvator dönüş hızı | $465$ m/s |
    | Merkür yörünge hızı | $47{,}4$ km/s |
    | Kilit modu eşiği | $e\approx0{,}125$ |
    | $N$ — fotoelektrik vuruş sayısı | $\approx1{,}5\times10^{4}$ |

11. **`R-11` · Matematikte çıplak $c$ kullanılmaz.** Teori ışık hızının evrensel bir sabit olduğunu reddeder (Postülat 4); dolayısıyla denklemlerde iki büyüklük **ayrı** yazılır: taban sabiti $c_0\equiv\sqrt{P_0/\rho_0}$ — kalibrasyon değeri, sayısal çapa — ve yerel yayılma hızı $c_{loc}=c_0\Lambda^2$ — konuma göre **değişen** gerçek hız (kural `R-10`). Çıplak $c$ yazmak bu ikisini tek sembolde birleştirir ve reddedilen sabitliği sessizce geri sokar. **Tek istisna:** standart fiziğin bir sonucu aktarılırken (örneğin $E=mc^2$, Lorentz çarpanı, PPN dili) $c$ o bilimin sembolü olarak korunur ve bağlamı belirtilir. Yerellik izni: $c_{loc}$ ve $\mathcal{G}$ evren ölçeğinde değişkendir, ama Güneş sistemi içinde sapma en fazla $4{,}2$ ppm'dir (Güneş yüzeyi; Dünya yüzeyinde $1{,}4\times10^{-9}$) — bu yüzden yerel hesaplarda standart sayısal değerlerin kullanılması sakıncalı görülmemiştir.

## D.2 Ortam (Evrenakı) Büyüklükleri

| Sembol | Anlamı | Birim / Değer | Tanımlandığı yer |
|---|---|---|---|
| $P$ | Yerel Evrenakı basıncı | Pa | Postülat 1, 6 |
| $P_0$ | Arka plan (derin uzay) basıncı; $\nabla P_0 = 0$ | $\tfrac14\rho_n c_0^2 = 6{,}07\times10^{33}$ Pa ($k=0$, Ek M-44) | Ek B.3 |
| $P_{ref}$ | Galaktik log-profilde $r_0$'daki referans basınç *(4.2.9.2)* | Pa | 4.2.9.2 |
| $\bar P_m$ | Madde içinde hacimce ortalanmış basınç $= P_0(1-\phi)$ | Pa | 3.4.6.3 |
| $\Delta P$ | Basınç açığı/farkı; Dünya merkezi için $\approx 0{,}83\times10^{25}$ Pa | Pa | Ek B.2 |
| $\nabla P$ | Basınç gradyanı; $\nabla P_r$ radyal, $\nabla P_{spin}$ dönme kaynaklı bileşen | Pa/m | Postülat 6, Ek B.1 |
| $\rho$ | Yerel Evrenakı yoğunluğu | kg/m³ | Postülat 1 |
| $\rho_0$ | Arka plan yoğunluğu $= P_0/c_0^2 = \tfrac14\rho_n$ | $6{,}8\times10^{16}$ kg/m³ | Ek B.3 |
| $\rho_n$ | Nükleon/Zerre öz yoğunluğu (evrensel sabit) | $\approx 2{,}7\times10^{17}$ kg/m³ | Postülat 4 |
| $\bar\rho_m$ | Madde içinde hacimce ortalanmış yoğunluk ($=\rho_0$, korunum) | kg/m³ | 3.4.6.3 |
| $\rho(r)$ | Galaktik vorteks yoğunluk profili (serbest profil fonksiyonu, Ek C P1) | — | 4.2.9 |
| $\Sigma$ | Kohezyon (çekme) dayanımı | $\Sigma/P_0 > 10^8$ | Ek A.3 |
| $\eta_E$ | Artık kuplaj katsayısı, Stokes biçiminde parametrize *($\mu$ yalnız standart Navier-Stokes alıntısında kullanılır)*. **Evrensel akışkan sabiti değildir:** $\eta_E^{etkin} = C_D\rho_0 a_b v^{1+n}/12v_{kav}^{n}$ ile cisme ve bağıl hıza bağlıdır; Phoebe için $3{,}3\times10^{-5}$ Pa·s. **En sıkı sınır Satürn halkasından gelir: $\lesssim2{,}3\times10^{-11}$ Pa·s** (11.4.8) | türetilmiş (T), M-43 | Postülat 7, Ek M-37, **Ek M-43** |
| $n$ | **Altkritik bastırma üssü:** $F_{artık} = \tfrac12 C_D\rho_0 v^2 A\,(v/v_{kav})^{n}$. Süper-akışkanda kritik hız altındaki kuplaj bastırmasının üssü; $\eta_E$'nin yerini alan boyutsuz serbest kalem | $n\simeq3$ (S — Phoebe'den) | **Ek M-43** |
| $C$ | Ortamın deplasman→basınç direnç katsayısı; gözleme yalnız $Cq_n$ çarpımı bağlanır | kg·m⁻³·s⁻¹, serbest (F). **[T-aday]** değer: $2{,}35$ (M-45, $\sqrt2c$ çapasıyla) | Ek M-35, **M-45** |
| $q_n$ | **Nükleon başına pulsasyon hacim debisi** ($\omega_2$ pompasının kaynak şiddeti). $\alpha = Cq_n/4\pi m_n$ ile gradyan bağlaşım sabitini, dolayısıyla $G$'yi üretir | m³·s⁻¹, serbest (F) — gözleme yalnız $Cq_n$ çarpımı ($G$) ve $q_n/2\gamma_n=\ell_\omega^{mikro}$ oranı bağlanır. **[T-aday]** değer: $1{,}62\times10^{-19}$ (M-45) | **Ek M-35**, 6.5.4.3, **M-45** |
| $\gamma_n$ | **Nükleon başına dolanım (sirkülasyon) debisi** ($\omega_1$ kolunun kaynak şiddeti); galaktik F4'ün genliğini besler. $\gamma_N=NV_n$ (etkileşim hacmi) ile karıştırılmamalıdır | m²·s⁻¹, serbest (F) — gözleme yalnız $q_n/2\gamma_n$ oranı bağlanır. **[T-aday]** değer: $2\pi r_n\sqrt2c=2{,}24\times10^{-6}$ (M-45) | **6.5.4.3**, **M-45** |
| $\ell_\omega^{mikro}$ | **Vortisite uzunluğu** $= q_n/2\gamma_n$: nükleonun pulsasyon debisinin dolanım debisine oranı — **mikro sabittir.** Fiziksel anlamı: komşuda dolanım alanının pulsasyon alanını geçtiği yarıçap ($v_t/v_r=d/\ell_\omega$); nükleer–atomik ölçek boşluğunda oturur. $a_0=\mathcal{G}m_n/\ell_\omega^2$ bileşkesinin girdisi. **[T-aday] özdeşlik:** $\ell_\omega=r_n\sqrt{m_p/m_e}=36{,}05$ fm (eşbölüşüm M-45'te türetildi; %1 örtüşme ölçüm hatası içinde — oran tam olmalı; G-9) | **S** — ölçümü $35{,}7$ fm (133 galaksi; kütleyle korelasyon $+0{,}03$; saçılma 0,17 dex) | 6.5.4.3 Adım 6–7, 6.5.4.5 |
| $N_c$ | **Tutarlılık kümesi büyüklüğü:** rastgele yürüyüşün bağımsız birimi başına etkin dolanım sayısı; $\Gamma_{etkin}=\gamma_n\sqrt{N_cN}$, $M_{tut}=N_cm_n$. Küme **atom çekirdeğidir** (fazdan bağımsız); pencere $[X,\langle A\rangle]$ — taban: eşlenme sönmesi (hidrojen kütle kesri), tavan: tam iç uyum | **T** (pencere) — $\approx[0{,}71;\,2{,}2]$; sınıf ölçümleri 0,65–1,55 (uçlar 2,5–3,0) | **6.5.4.3 Adım 7** |
| $\lambda$ (tutarlılık) | Pencere-içi konum: ortamın çekirdekler-arası dolanım muhasebesi ($N_c=X+\lambda(\langle A\rangle-X)$). Çekirdek-içi olamaz (enerji kilidi); ortalama polarizasyon tam sıfırdır ($\varepsilon<3\times10^{-35}$ — $\sqrt{N}$ dolanım korunumunun teoremi). Aday belirleyici: ortamın kaskad karakteri (incelik/dinamik soğukluk); $\lambda\leq1$ | ölçülen: Im $\approx0$ · ana sınıflar 0,14–0,68 · S0/BCD $\approx1{,}6$ (temiz örneklemde $<1$'e inmeli — G-8); ilk $v/\sigma$ sınavı (18 gal.) $+0{,}49$, $p=0{,}019$ — öngörülen yönde ilk işaret; nicel bağıntı **açık** (7.4) | 6.5.4.3 Adım 7 |
| $\ell_\omega^{etkin}(R)$ | Galaktik ölçekte kurulan **net** dolanımın etkin uzunluğu $= \ell_\omega^{mikro}\sqrt{N(R)} = \sqrt{\mathcal{G}M_{kaps}(R)/a_0}$. **$\equiv r_0$** — F1↔F4 rejim geçiş yarıçapının ta kendisidir (Ek M-38, 3 Ağu 2026): iki nicelik aynı sayıdır, bu yüzden $r_0$ serbest kalem değildir ve bu satırın [T] rozeti onu da kapsar. Galaksiden galaksiye beş mertebe yayılır — yayılım $\sqrt{N}$ çarpanıdır, serbestlik değildir | türetilmiş (T) | 6.5.4.3–6.5.4.5 |
| $\kappa_d$ | İçsel deşarj sabiti (fonksiyon ailesi) | serbest (F) | 3.1.8 |
| $S(x,t)$ | Süreklilik denklemi kaynak/kuyu terimi | kg/(m³·s) | 4.2.2 |
| $S_{kozmik}$ | Evrensel deşarj kaynak terimi $= 3\rho_0 H_0$ | — | 4.2.11 |
| $k$ | **Deplasman** sürecinde $\rho$'nun $P$'ye eşlik oranı — maddenin ortamı dışlaması yoğunluğu değil basıncı değiştirir. **Dalga kanalının adiyabatik katsayısıyla karıştırılmamalıdır** (o, $(\partial P/\partial\rho)_\chi=c_0^2$'dir). | **$k=0$**, türetilmiş (T): M-15 G2 + M-30 Varsayım 1 | Ek B.3, **Ek M-44** |
| $\chi$ | **Deplasman alanı** — maddenin doğurduğu, kütle-itim kuyusunu taşıyan ikinci durum değişkeni. Hâl denklemi $P=P(\rho,\chi)$; nükleonlar $\chi$'nin kaynağıdır ve $\chi$ kütlenin dışında da sıfır değildir | — | **Ek M-44** |
| $\phi$ | **Deplasman hacim kesri** — maddenin Evrenakı'yı deplase ettiği hacim oranı. **Tanımı geometrik, ölçümü optiktir:** $\phi$ daima hacim kesridir, $\phi=1-1/n^2$ (M-15) yalnız saydam ortamdaki ters okumasıdır. **Doğrudan hesaplanır:** $\phi(\rho)=\min(\rho/\rho_*,\phi_{doy})$ — 11.4.1-(4)–(5). **İki rolü vardır:** (i) Fizeau sürükleme katsayısı $f=\phi$ (M-16), (ii) **kavrama kesri** $\mathcal{R}=\phi$ (M-39, M-40) — *genliğe girer, hıza değil: $v_e=\phi\,\omega R$ yazımı M-39'da terk edildi, $p=1$ türetildi.* Kütleyle değil **hacimle** ölçeklenir: su için $\phi\approx0{,}42$ iken $\rho_{su}/\rho_n=3{,}7\times10^{-15}$; deplasman kafesi bare nükleon değil **atomun tamamıdır** | su: 0,42 · kristal katı (kayaç): **0,70** · yoğun akışkan (gaz devi zarfı): **0,45** · **metal / iyonize plazma: $1-\delta$, $\delta\lesssim10^{-13}$** · nötron maddesi: ~0,7–0,9 *(elektron gazı yok ⟹ paketlenme-sınırlı)* | M-15, M-16, **M-39**, **M-40**, **11.4.1-(4)–(5)** |
| $\mathcal{R}$ | İç kavrama kesri $=\phi$ (kafesin içindeki ortamı yönetir). Gövdenin *dışındaki* dipolar alanı yöneten $\xi$'den **ayrı büyüklüktür**; sınırda eşleşmeleri gerekmez — sınır kafesin bittiği yerdir | $=\phi$ | **Ek M-40** ("İki kavrama kanalı") |
| $\Xi$ | Kuyu iskeleti gücü / baryonik öz-kuyu (öz-itim) oranı | $\approx 5$ | 3.7.4 |
| $\Psi_{Evrenakı}$ | Toplam Evrenakı alanı $= \Psi_0 + \sum_i \psi_i$ (kuantum dalga fonksiyonu $\psi$ ile ilgisizdir) | — | 1.3.1 |

## D.3 Hız Merdiveni

| Sembol | Anlamı | Değer |
|---|---|---|
| $c_0$ | Yerel ışık hızı = Kavrama (patinaj/sonik) sınırı: $c_0 = \sqrt{P/\rho}$; mutlak üst sınır **değildir** | arka planda $2{,}998\times10^8$ m/s |
| $\Lambda$ | **Madde ölçeği:** $\Lambda \equiv 1 - \Phi/c_0^2$. Cetvelleri ($\ell_{loc}\propto\Lambda$), saatleri ve **atomik geçiş frekanslarını** ($\nu_{tik}\propto\Lambda$) yöneten ortak çarpan. Kızıla kayma ve Zerre-Saati bağıntılarında geçen büyüklük budur (Ek M-21, M-42). *(Standart kozmolojinin kozmolojik sabiti gerektiğinde **$\Lambda_{kozm}$** yazılır; indissiz $\Lambda$ daima madde ölçeğidir. "$\Lambda\text{CDM}$" birleşik model adı olarak dokunulmaz. Ek D · S-11/R-10.)* | $1-\Phi/c_0^2$; Dünya yüzeyi için $1 - 7\times10^{-10}$ |
| $c_{loc} = c_0\Lambda^2$ | Zerre'nin arka plan (düz) uzayda ölçülen **yayılma hızı**. Işık bükülmesi, Shapiro gecikmesi ve etkin kırılma indisinde ($n_{eff} = 1/\Lambda^2$) geçen büyüklük budur (Ek M-42). Saat/frekans bağlamında $c_{loc}$ **kullanılmaz** — orada $\Lambda$ geçer. | — |
| $c_{loc,kaynak}$, $c_{loc,alıcı}$ | Konuma bağlı yayılma hızı değerleri (Doppler'in uzaysal/Zerre Aralığı çarpanı)  | — |
| $\Lambda_{kaynak}$, $\Lambda_{alıcı}$, $\Lambda_{ref}$ | Konuma bağlı madde ölçeği değerleri (kızıla kayma zinciri)  | — |
| $c_f$ | Fiber içi ışık hızı *(5.2.9.2)* | $\approx 1{,}794\times10^8$ m/s |
| $\sqrt{2}\,c_0$ | Girdap zarfının denge yüzey hızı ($v_{denge}$); boyuttan bağımsızdır (M-3 duvar hızı yasası) ve Zerre'nin evrensel çevresel hızı $v_{cev}$ ile aynı büyüklüktür (D.4) | $4{,}24\times10^8$ m/s |
| $v_{ekvator}$ | Protonun Compton frekansından okunan kompozit ekvator hızı ($2\pi\nu_c R_p$) — teorinin girdisi değil, $v_{cev}=\sqrt2\,c_0$'nin **gözlemsel sağlamasıdır**; ~%18'lik fark $O(1)$ bütçesindedir (7.4) | $\approx 5\times10^8$ m/s $\approx 1{,}67c$ |
| $v_m$ | Kohezyon kanalı sinyal hızı $= \sqrt{\Sigma/\rho_0} = c_0\sqrt{\Sigma/P_0}$ | $> 10^4\,c_0$ |
| $v_{kav}$ | Kavitasyon eşiği $= \sqrt{2}\,c_0\,\sqrt{1+\Sigma/P_0} \approx \sqrt{2}\,v_m$ — **hız merdiveninin son basamağı.** Maddeyi doğuran dönüş bu eşiğin üzerindedir; ama taşıyıcısı Kut düzeyinde olduğu için ona sembol tahsis edilmez ve merdivende basamak açılmaz (D.1 kural 9). Teorinin niceliği yırtılmanın *eşiğidir*, eşiği aşan gövdenin hızı değil | $\gg c_0$ |
| $v_{bağıl}$ | Cisim–Evrenakı bağıl hızı (sürüklenme zarfı içinde $\approx 0$) | — |
| $v_\theta(r)$ | Girdabın teğetsel hızı; ideal girdapta $\Gamma/2\pi r$ | — |
| $v_0$, $r_0$ | Bileşik girdapta düz-hız değeri ve **rejim geçiş yarıçapı**. **Türetilmiştir** (Ek M-38): $r_0=\sqrt{\mathcal{G}M/a_0}=\ell_\omega^{etkin}$, $v_0^2=\sqrt{\mathcal{G}Ma_0}$ — serbest kalem değil (Ek C satır 21 [T]). $r_0$, küresel akı geometrisinin ($1/R^2$) silindirik geometriye ($1/R$) döndüğü yarıçaptır — Güneş Sistemi'nin Kepler'de kalmasını ve galaktik düz dönüş eğrisini aynı sayı belirler (türetilmemiş; serbest F, Ek C P1) | — |
| $u_{ort}$ | Momentum-ağırlıklı ortalama sürüklenme hızı $= \phi u$ *(3.4.6.3)* | — |
| $u$ | Akan ortamın (ör. suyun) hızı — Fizeau bağlamı; Doppler'de alıcı hızı | — |
| $\beta$ | $v/c_0$ | — |

## D.4 Mikro Evren ve Işık

| Sembol | Anlamı | Değer |
|---|---|---|
| $m_z$ | Zerre kütlesi — teorinin **ölçülen girdi parametresi** (Standart Model'de $m_e$ nasılsa öyle); Zerre, Kutlardan kurulu **en küçük kararlı yapılanmadır** | $\approx 1{,}47\times10^{-35}$ kg |
| $r_{L2}$ | **Atomik uzunluk ölçeği:** ilk kabuğun (L2 katmanının) yörünge yarıçapı. Bu kitapta **hesaba girmez**: atom tayfının nicel işlenişi serinin *Atomların İşleyişi* kitabına bırakılmıştır (9.11.8–9.11.9). Kaydı, teorinin bu ailede kendi uzunluk ölçeğini **henüz kurmadığının** ilanıdır ve bir **borçtur**, kalıcı girdi ilanı değil (Ek C satır 1-b; Madde 21). *Standart fiziğin bu niceliğe verdiği $a_0$ adı burada **kullanılmaz** — çıplak $a_0$ bu kitapta galaktik ivme ölçeğidir (D.3; Ek C satır 20)* | $5{,}29177\times10^{-11}$ m; ölçülen değer, teori-içi kaynağı kurulmamış |
| $V_z$, $r_z$ | Zerre hacmi ve **eşdeğer küre (ortalama)** yarıçapı. Hacim $V_z=m_z/\rho_n$'den gelir, dolayısıyla geometriden bağımsızdır; yarıçap ise basık gövdenin eşdeğer küre okumasıdır | $5{,}44\times10^{-53}$ m³; $2{,}35\times10^{-18}$ m |
| $\lambda$ | **Zerre Aralığı:** ardışık iki Zerre arası fiziksel mesafe ("dalga boyu" yalnız standart fizik aktarımında tırnak içinde kullanılır) | — |
| $\nu$ | Frekans: **tek katarın içindeki** ardışık Zerrelerin birim zamanda hedefe çarpma ritmi; rengi belirler *(Fizeau katsayısı $f$ ile çakışmaması için; 2.2.3)* | — |
| şiddet ($S_ş$) | Işık şiddeti (parlaklık): **birim alana düşen Zerre katarı sayısı** — frekans katarın içini, şiddet katarların sayısını sayar (Bölüm 2.2.3, 2.3.5) | — |
| $\nu_c$ | Compton frekansı — **teorinin girdisi değildir.** Teorik frekans duvar hızı yasasından türetilir ($\nu=\Omega/2\pi=\sqrt2\,c_0/2\pi r$, M-3); $\nu_c$ bu türetimin **gözlemsel sağlama noktasıdır** (mertebe + $O(1)$ uyumu) | $\approx 10^{23}$ Hz (gözlem) |
| $h$ | Planck sabiti; mekanik özdeşliği $h = \delta\tau$ *(S-4: çıplak $h$ yalnız budur)* | — |
| $a_0$ | **Galaktik F4 ivme ölçeği** *(çıplak $a_0$ yalnız budur — atomik uzunluk için $r_{L2}$ kullanılır, D.4)* | Ek C satır 20 |
| $h_d$ | **Galaktik akı-tabakası (disk) kalınlığı** (M-38); $h_d(R)=h_{inj}$ türetilmiştir. *(Eski çıplak-$h$ yazımı 9 Ağu 2026'da taşındı. Gözlemsel ölçek yükseklikleri ayrıdır: $h_z$ [yıldız/gaz], $h_{inj}$ [enjeksiyon]; halka kalınlığı $h_{halka}\simeq a_b$ — 11.4.5.)* | ~$10^{19}$ m (Samanyolu) |
| $\hbar$ | İndirgenmiş Planck sabiti $= h/2\pi$ | — |
| $\delta$ | Tek vuruşta aktarılan enerji $= \eta\cdot\tfrac12 m_z(c_0^2 + k_a v_{cev}^2) = \eta\,m_z c_0^2$ *(çünkü $k_a=1/2$ ve $v_{cev}=\sqrt2\,c_0$ ile $c_0^2+k_av_{cev}^2=2c^2$)* | $5{,}4\times10^{-4}$ eV/vuruş; türetilmiş (T) |
| $\tau$ | **Kopma penceresi** $=h/\delta$; ölçülen $h$ ile sabitlenir. **Dürüstlük kaydı:** M-10'un birikim yolu bağımsız bir sağlama vermez — $N=h\nu/\delta$ olduğundan $N/\nu\equiv h/\delta$ çıkar, iki yol cebirsel olarak tek bağıntıdır. Dolayısıyla $h=\delta\tau$ bir **ayrıştırmadır**, $h$'ın sayısal üretimi değil (9.2.2). $h$'ı kullanmayan bağımsız bir $\tau$ tayini açık kalemdir; elde edilirse $h$ gerçekten öngörülebilir hâle gelir | $\approx7{,}7$ ps; gözlemle sabitlenmiş (S) |
| $N$ | Kopma penceresindeki vuruş sayısı $= \nu\tau$ | $\approx 7{,}5\times10^3$ (morötesi eşiği) |
| $\eta$ | Tek-vuruş elastik aktarım verimi $\approx 4m_z/m_e$ | $\approx 6{,}5\times10^{-5}$ |
| $k_a$ | Zerre atalet (kütle dağılımı) katsayısı; Zerre kendi dönüşüyle basık olduğu için disk gövde değeri benimsenir. **Kesin türetim değil, ince-disk limitidir:** gövde basık ama sonsuz ince değilse değer $2/5$ ile $1/2$ arasında kalır ($\delta$'da ~%11 bant). Serbest kalem sayılmaz — geometri onu bu aralığa kapatır *(Ek B.3'ün eşlik oranı $k$ ile çakışmaması için indislenir; 2.2.2)* | $1/2$ benimsenen limit; aralıkla sınırlı (A): $2/5 < k_a \le 1/2$ |
| $v_{cev}$ | Zerre'nin evrensel çevresel dönüş hızı; D.3'teki $\sqrt2\,c_0$ (girdap zarfının denge yüzey hızı) ile aynı büyüklüktür ve boyuttan bağımsızdır | $\sqrt{2}\,c_0 = 4{,}24\times10^8$ m/s; türetilmiş (T) — M-3 duvar hızı yasası |
| $\varphi$ | Katar ritmi ile rampa çevrimi arasındaki göreli faz | — |
| $n$ | Kırılma indisi; $1/n^2 = 1-\phi$ *(soğurma olayı / paket sayısı için $N_p$ kullanılır)* | — |
| $\phi$ | Moleküllerin hacim kesri = Fizeau katsayısı $f = 1 - 1/n^2$ — **tam kayıt ve ikinci rolü (kavrama kesri) için bkz. D.2** | su: $0{,}437$ |
| $I$ | Atalet momenti *(ışık şiddeti için ayrı sembol: metinde "şiddet" veya $S_ş$)* | — |
| $A$ | Dalga genliği ($I_ş \propto A^2$) *(enerji $E$ ile çakışmaması için; 2.7.1)* | — |
| $E$ | Enerji (yalnız enerji) | — |
| $\Phi$ | **İki ayrı büyüklük; bağlam ayırır (S-28):** (1) **Potansiyel bağlamında — kuyu derinliği.** Teoride ödünç alınmaz, **tanımlanır:** $\Phi \equiv (P_0-P)/\rho_n \ge 0$; dış alanda $\Phi = +\mathcal{G}M/r$, Dünya yüzeyinde $\Phi/c_0^2 \approx 7\times10^{-10}$. $\Lambda = 1-\Phi/c_0^2$'de (M-8, M-20, M-21, M-42) geçen $\Phi$ budur. Dinamik daima M-2 ile yazılır ($\vec a = -\nabla P/\rho_n$); Kuvvet-1'in dinamik potansiyeli ayrı sembol taşır: $\Phi_{it} \equiv (P-P_0)/\rho_n = -\Phi$ (11.1; $\vec a_1 = -\nabla\Phi_{it}$). Standart fizik köprüsü: $\Phi_{std} = \Phi_{it} = -\Phi$. (2) **Fotoelektrik bağlamında:** iş fonksiyonu (eV boyutlu; M-10/M-11, 2.2.3, 9.2) — potansiyelle ilgisiz, bağlam-yerel. *(Düzeltme kaydı, 17 Ağustos 2026: eski ek kayıt potansiyel-$\Phi$'yi $(P-P_0)/\rho_n = -\mathcal{G}M/r$ işaretiyle tanımlıyordu; o işaret $\Lambda$ satırıyla ve M-8/M-42'nin tüm kullanım yerleriyle çelişiyor, kızıla kayma/Shapiro yönlerini ters çeviriyordu. Negatif-işaretli dinamik büyüklük $\Phi_{it}$ adıyla ayrıldı.)* | — |
| $D_{toplam}=D_{zarf}+D_{yol}$ | SN 1987A gecikme bütçesi bileşenleri | ~3 saat |
| $\chi$ | Evrenakı dispersiyon katsayısı (fenomenolojik) | $5\times10^{-4}$ |
| $g^{(2)}(0)$, $S$ | Standart kuantum optik ölçütleri (anti-demetlenme; CHSH istatistiği) | — |

## D.5 Dönüş ve Makro Evren

**Kayıt:** $\omega_1$ ve $\omega_2$ yalnız Bölüm 1.4'ün dört boyutlu çift dönüşünün iki bileşenini adlandırır — biri üç boyut içindeki düzlemde, diğeri W eksenini içeren düzlemde. İkisi arasında hız hiyerarşisi yoktur (nükleonda $\omega_2=\omega_1$) ve hiçbiri Compton frekansının adı değildir; temel nicelik duvar hızı yasasıdır ($\Omega=\sqrt2\,c_0/r$, M-3), frekans ondan türetilir.

| Sembol | Anlamı |
|---|---|
| $w$, W | Dördüncü uzay ekseni; uzayımız $w=0$ kesiti *(karanlık enerji hâl denklemi $w$ yalnız 7.7.9'da, açık etiketle)* |
| $\omega_1$ | Çift dönüşün 3B içi düzlemdeki bileşeni; açısal hızı duvar hızı yasasından okunur, $\omega_1=\sqrt2\,c_0/r$ (M-3). Nükleonda $5{,}0389\times10^{23}$ rad/s. İki bileşen arasında hız hiyerarşisi varsayılmaz; oran gövdenin kendi kütle dağılımınca kilitlenir ($\omega_2/\omega_1=\varepsilon\cos\theta$, 1.4.8 md.3) |
| $\omega_2$ | Çift dönüşün W eksenli düzlemdeki bileşeni; bileşiklerde devinimin kaynağı |
| $\omega_Z$ | Zitterbewegung frekansı $\approx 2mc^2/\hbar$ |
| $\Omega_{yör}$ | Yerel yörünge (girdap) açısal frekansı |
| $\Omega_{dön}$ | Gök cisminin dönüş açısal hızı *(3.6.3)* |
| $\Omega_z$ | Halka parçacığının dikey salınım frekansı $= \sqrt{GM/r^3}$ *(3.10.3)* |
| $\vec\omega_v$ | Vortisite $= \nabla\times\vec v$; rotasyon vektörü $= \tfrac12\nabla\times\vec v$ |
| $\Gamma$ | Girdap sirkülasyonu *(3.4.4'teki termal tutamaç şiddeti $\Gamma$ bağlamla ayrılır)* |
| $r_{cep}$ | Vakum cebi yarıçapı $= \Gamma/2\pi\sqrt{2}c_0$ *(Ek A.2)* |
| $r_t$ | Tanecik yarıçapı (Stokes sönümü $\gamma_{ortam} \sim 6\pi\eta_E r_t/m$) *(3.10.4.2)* |
| $g$, $g(R)$, $R_c$, $p$, $q$, $q_{peri}(e)$ | Kavrama/kilitlenme parametreleri (Bölüm 3.4.4) |
| $e$ | Yörünge basıklığı; kilit modu eşiği $e \approx 0{,}125$ |
| $\gamma$ | Lorentz / çapraz-yol uzama çarpanı $= 1/\sqrt{1-v^2/c_0^2}$ |
| $\gamma_{ortam}$, $\gamma_{standart}$, $\gamma_{toplam}$ | Sönüm oranları (Bölüm 3.10.4) |
| $\gamma_N$ | Cismin etkileşim hacmi $= NV_n$ *(Lorentz çarpanı $\gamma$ ile çakışmaması için indislenir; 4.2.4)* |
| $G$, $\mathcal{G}$ | Yerleşik adıyla "kütleçekim sabiti"; teoride türetilmiş ve **yerel** (Postülat 4): $\mathcal{G} = \alpha/\rho_n$ (M-28). Teori kendi denklemlerinde $\mathcal{G}$ yazar; düz $G$ yalnız standart-fizik aktarımında, Newton-kalibrasyon bağlamında (M-27) ve ölçülen yerel değer/$GM$ çarpımı bağlamında kalır *(kesme modülü için $G_s$)* |
| $\alpha$ | Gradyan bağlaşım sabiti [s⁻²]; $P(r) = P_0 - \alpha M/r$ *(ince yapı sabiti: $\alpha_{is}$ veya açık yazım)* |
| $H_0$ | Hubble sabiti $= S_{kozmik}/3\rho$ |
| $\xi$ | **Dönme sürüklenme kesri:** ortamın gövde dönüşüne tutunma oranı, $\vec\Omega_{ortam} = \xi\,\vec\omega_{gövde}$. Türetilmiştir — ortam bir cismi ancak kavrama hızının bozulduğu ölçüde tutar: $\xi = \dfrac{I}{MR^2}\left\lvert\dfrac{\delta c_{loc}}{c}\right\rvert = \dfrac{I}{MR^2}\dfrac{2\Phi}{c^2}$. Dünya: $4{,}605\times10^{-10}$; nötron yıldızı: $\sim0{,}1$. Ötelemedeki *tam* sürüklenmeden (Postülat 7) ayrıdır — bu neredeyse tam **patinajdır** *(**Ek M-40**; girdisi Ek M-42)* |
| $\kappa_5$ | **Yanal itim deplasman kapanış katsayısı:** $f_{yanal}(\theta) = -\dfrac{\kappa_5\,\rho\,v_e^2}{r}\sin2\theta$ [N/m³]. Ekvatordan kutba deplasman muhasebesini kapatan boyutsuz çarpan *(boyutsuz, serbest (F), **$\lesssim2{,}1\times10^{-3}$** (Ay'ın düğüm gerilemesi, LLR — **11.4.3**); figür sınırı $\lesssim0{,}0114$–$0{,}0131$ (Sınav 1: Dünya basıklığı + $k=0$ + $p=1$ + $\phi_\oplus=0{,}70$ — Ek M-39); $\tfrac12$ çalışma değeri **kırk kattan fazla**. Gözlemin sabitlediği nicelik çarpımdır: $\kappa_5\phi\lesssim1{,}5\times10^{-3}$ · **Ek M-39**, 11.4)* |
| $\phi_{doy}$ | **Deplasman doygunluk kesri:** kafesler temas ettikten sonra $\phi$'nin kilitlendiği değer; yoğunluktan değil **fazdan** gelir — kristal katı $0{,}68\pm0{,}06$ (bcc $0{,}680$, fcc/hcp $0{,}7405$), yoğun akışkan $0{,}47\pm0{,}03$ (sert-küre donma sınırı $\eta_f=0{,}494$), açık yapılı sıvı $0{,}36$–$0{,}42$, **metal/plazma $1-\delta$, $\delta\lesssim10^{-13}$** (delokalize elektron gazı; kalan pay 30 protonluk boşluk gerektirir — 11.4.1-(5)) *(boyutsuz, **T** — 11.4.1-(4)–(5); türetilmiş değerler $\phi_\oplus=0{,}70$, $\phi_{Satürn}=0{,}45\pm0{,}03$)* |
| $R_\phi$ | **Deplasman yüzeyi:** gövdede $\rho=\phi_{doy}\rho_*$ koşulunun sağlandığı derinlik; F5'in dış alanının sınır koşulu burada kurulur ve Rankine tepesi buradadır. Karasal cisimlerde $R_\phi=R_e$; gaz devlerinde $0{,}93$–$0{,}97\,R_e$ (Satürn $0{,}935$, Jüpiter $0{,}966$, Uranüs $0{,}959$, Neptün $0{,}968$) *(m, **T** — 11.4.1-(4))* |
| $n_e^{eşik}$ | **Deplasman kafesi sınır yoğunluğu:** $\phi$'nin kafes hacmini tanımlayan elektron yoğunluğu eş-yüzeyi, $\simeq0{,}001$ a.u. $=6{,}75\times10^{27}$ e/m³ (deneysel vdW hacimlerini üreten standart değer). İki ayrı sonucu birden yönetir: (i) $\rho_*$'ların değerleri, (ii) metalik/plazma fazında ara bölgenin dolu olması. **Tek noktadan sınanabilirlik:** bu sabit şişerse ikisi birlikte bozulur *(a.u., kalibre — 11.4.1-(4)–(5))* |
| $\rho_*$ | **Tam dolgu yoğunluğu:** kafeslerin uzayı tümüyle doldurduğu yoğunluk, $\rho_*=m/v$ ile $v=b_{vdW}/4N_A$ (ya da iyonik hacimler). H₂ 303 · He 675 · H₂O 2363 · silikat (forsterit) 4732 kg/m³ *(kg/m³, **T** — 11.4.1-(4))* |
| $\tau_{ret}(r,e,i)$ | Retrograd sönüm zaman ölçeği *(kopma penceresi $\tau$ ile çakışmaması için indislenir; 3.6.1)*. Stokes yazımında $2\rho_c a_b^2/9\eta_E$ (hızdan bağımsız); altkritik yazımda $\propto \rho_c a_b v_{bağıl}^{-4}$ — **iki yazımı ayıran sınav budur** (Ek M-43) |
| $f(\theta_e)$ | Hizalanma verimi ($\theta_e$: eksen eğikliği; türetilmemiş) |
| $J_2$ | Dünya basıklık (kuadrupol) katsayısı |
| $\mathsf{T}$, $T_{ij}$ | **Gelgit tensörü:** $T_{ij} \equiv \partial a_i/\partial x_j = -\dfrac{1}{\rho_n}\partial_i\partial_j P$ — kütle-itim alanının ikinci türevi. Kaynaksız bölgede özdeğerleri $\dfrac{\mathcal{G}M}{r^3}(+2,-1,-1)$ ve **izi sıfırdır** (türetilmiş sonuç, varsayım değil); gövde içinde $\mathrm{tr}\,\mathsf{T} = -4\pi\mathcal{G}\rho_{madde}$ *(Bölüm 11.1, Ek M-36)* |
| $\vec\xi$ | **Gövde içi konum vektörü:** gelgit açılımında gövde merkezinden ölçülen yer değiştirme, $\lvert\xi\rvert \le b$. *(Bağlam ayrımı: indissiz skaler $\xi$ dönme sürüklenme kesridir — yukarıya bkz. İkisi hiçbir denklemde birlikte geçmez; gelgit bağlamında daima vektörel $\vec\xi$, sürüklenme bağlamında daima skaler $\xi$ yazılır.)* *(Bölüm 11.1, Ek M-36)* |
| $\psi$ | Gelgit açısı: $\vec\xi$ ile gövde–kaynak ekseni arasındaki açı *(kuantum dalga fonksiyonu $\psi$ ile ilgisizdir — bkz. D.2 $\Psi_{Evrenakı}$)* *(Bölüm 11.1)* |
| $\Psi_T$ | **Gelgit potansiyeli:** taşınan gövde çerçevesinde, ortak taşınma terimi çıkarıldıktan sonra kalan artık potansiyel. $\Psi_T(\xi,\psi) = -\dfrac{\mathcal{G}M\xi^2}{2r^3}(3\cos^2\psi-1)$. Artık **basınç** alanı $P_T = \rho_n\Psi_T$'dir: eksende açık, yanaklarda fazla, oran $2{:}1$ *(Bölüm 11.1, Ek M-36)* |
| $\zeta$ | **Serbest yüzey yükseltisi** (denge gelgiti). Gelgit **genliği** (tepe–çukur) $\Delta\zeta = \tfrac32\dfrac{M}{M_\oplus}\left(\dfrac{b}{r}\right)^3 b$ — bir *yükseklik değil*, tam genliktir: tepe $+A$, çukur $-A/2$. *(Eski yazım $\Delta h$ **geçersizdir** — S-4 gereği $h$ yalnız Planck sabitidir. $\Delta\eta$ kullanılmaz, $\eta_E$ ile çakışır.)* Ek D · **S-27** *(Bölüm 11.1, Ek M-36)* |
| $R_p$, $R_\oplus$, $R_s$ | Proton yarıçapı ($0{,}84$ fm); Dünya yarıçapı; yüzey yarıçapı |
| $\lambda_s$ | Bending-wave sönüm mesafesi $= v_{grup}/\gamma_{toplam}$ *(Zerre aralığı $\lambda_z$ ile çakışmaması için indislenir)* |
| $\lambda_z$ | Dispersiyon türetimindeki Zerre aralığı *($\Lambda$ madde ölçeğine ayrılmıştır; bkz. D.3 ve Ek M-42)* |

## D.6 Statü Kodları (Ek C ile ortak)

**T** türetilmiş · **S** gözlemle sabitlenmiş · **A** aralıkla sınırlanmış · **F** serbest · **G** gözlemsel girdi

Serbest parametre bilançosu (Ek C.1): **3 skaler** ($\Sigma$, $n$, $\kappa_d$) + 2 profil fonksiyonu ($\rho(r)$, rampa profili). Kut'a sembol tahsis edilmediği için bu sayıma girecek bir Kut büyüklüğü de yoktur (D.1 kural 9). *(10 Ağu 2026: $v_{cev}=\sqrt2\,c_0$ türetilip $k_a$ geometriyle aralığa kapanınca $\delta=\eta m_zc^2$ tamamen hesaplanır oldu ve listeden **[F]**'den çıktı; $\tau$ ise ölçülen $h$ ile sabitlendiği için **[S]**'ye geçti — serbest skaler sayısı 5 → 3. **Dürüstlük notu:** $\tau$'nun $h$'tan bağımsız bir tayini yoktur; bu yüzden $h=\delta\tau$ bir ayrıştırmadır, $h$'ın sayısal öngörüsü değildir — bkz. 9.2.2.)* *(3 Ağu 2026: $r_0$ ve $A_4$ Ek M-38'de türetildi — $r_0=\sqrt{\mathcal{G}M/a_0}=\ell_\omega^{etkin}$; Ek C'ye satır 21 [T] olarak girdi. Blok H'nin kendi sayımı üçten **ikiye** ($(Cq_n)$, $\kappa_5$) indi; Ek C'nin başlık sayımı bu türetimden etkilenmez çünkü $r_0$ orada zaten ayrı kalem değildi, P1'e bağlanmıştı — o bağ da koptu.)* *(29 Tem 2026: $\eta_E\to n$ — Ek M-43; $k$ listeden çıktı, $k=0$ türetildi — Ek M-44.)*

## D.7 Sembol Çakışma Kararları (S-1 … S-27)

Kitap standart fizikten çok sayıda sembol devralır ve kendi büyüklüklerini de adlandırmak zorundadır; ikisi kaçınılmaz olarak çakışır. Aşağıdaki kararlar her çakışmayı **tek** bir kural lehine çözer. Metinde "(S-14)" gibi bir atıf gördüğünüzde karşılığı bu tablodaki satırdır. Kararların bağlı olduğu genel ilke `R-1`'dir: bir sembol kitabın her yerinde aynı büyüklüğü gösterir.

| # | Sembol | Karar |
|---|---|---|
| **S-1** | $k$ | Yalnız $\rho$–$P$ eşlik oranı (Ek B.3). Fotoelektrik atalet katsayısı → $k_a$. Güç spektrumu $P(k)$ standart bırakılır |
| **S-2** | $\alpha$ | Yalnız gradyan bağlaşım sabiti $[\text{s}^{-2}]$ ($\mathcal{G}=\alpha/\rho_n$). İnce yapı sabiti → $\alpha_{is}$ veya açık yazım |
| **S-3** | $E$ | Yalnız enerji. Dalga genliği → $A$ (2.7.1'deki $I\propto E^2$ → $I\propto A^2$) |
| **S-4** | $h$ | Yalnız Planck sabiti ($h=\delta\tau$). Su derinliği (3.9.2.1) → $d$; disk/akı tabakası kalınlığı → $h_d$ |
| **S-5** | $I$ | Yalnız atalet momenti. Işık şiddeti → $S_{ş}$ veya açık yazım "şiddet" |
| **S-6** | $n$ | Yalnız kırılma indisi (ve M-43'ün bastırma üssü). Paket tam sayısı ($n h\nu$) → $N_p$ |
| **S-7** | $\Omega$ | $\Omega_{yör}$ = yörünge frekansı; gövde dönüşü → $\Omega_{dön}$; dikey salınım (3.10.3) → $\Omega_z$; vortisite → $\vec\omega_v=\nabla\times\vec v$ (tam rotasyonel; yarılı büyüklük "rotasyon vektörü" adıyla $\tfrac12\nabla\times\vec v$ olarak ayrıca tanımlanır) |
| **S-8** | $\gamma$ | $\gamma$ (indissiz) = Lorentz çarpanı; $\gamma_{ortam}$ = sönüm; $\gamma_N=NV_n$ = etkileşim hacmi (4.2.4'teki $\gamma$ yeniden adlandırıldı) |
| **S-9** | $\tau$ | $\tau$ = kopma penceresi (Ek C). Retrograd sönüm ölçeği → $\tau_{ret}(r,e,i)$ |
| **S-10** | $\delta$ | $\delta$ = tek-vuruş aktarımı (Ek C). Varyasyon operatörü $\delta c$, $\delta L$ standarttır (bağlam ayırır); flyby açıları $\delta_i$, $\delta_o$ indisli kalır |
| **S-11** | $\Lambda$ | $\Lambda$ = **madde ölçeği** ($1-\Phi/c_0^2$, Ek M-42; resmî tanım). Dispersiyon türetimindeki Zerre aralığı → $\lambda_z$. Kozmolojik sabit → $\Lambda_{kozm}$ (yalnız standart fizik aktarımında; "$\Lambda$CDM" birleşik model adı olarak dokunulmaz) — bkz. `R-10` |
| **S-12** | $w$ | $w$ = dördüncü eksen koordinatı. Momentum-ağırlıklı hız ($=\phi u$) → $u_{ort}$. Karanlık enerji hâl denklemi $w$ standart bırakılır (yalnız 7.7.9, açık etiketle) |
| **S-13** | $a$ | $\vec a$ = ivme. Cep yarıçapı → $r_{cep}$; Stokes tanecik yarıçapı → $r_t$; yörünge yarı-büyük ekseni $a$ standart (Kepler bağlamı) |
| **S-14** | $R$ | İndis zorunlu: $R_p$ (proton), $R_\oplus$ (Dünya), $R_s$ (yüzey). Silindirik bağlamda $R=r\cos\theta$ **eksene dik uzaklık**, $r$ ise **küresel yarıçap** |
| **S-15** | $\nu$ / $f$ | Frekans daima $\nu$. $f$ yalnız Fizeau katsayısı (`R-2` ile aynı karar) |
| **S-16** | $c$ / $C$ | Fiber içi hız $C$ → $c_f$; osilatör frekansı → $\nu_{osc}$ |
| **S-17** | $P_0$ / $P_\infty$ | Tek sembol $P_0$ = arka plan basıncı; $P_\infty$ kaldırıldı. 4.2.9.2 log profil referansı → $P_{ref}$ |
| **S-18** | $\rho$ ailesi | $\rho$ (yerel), $\rho_0$ (arka plan), $\rho_n$ (nükleon öz). $\rho_E$ ve $\rho_{zerre}$ kaldırıldı; Zerre öz yoğunluğu için tercih edilen sembol $\rho_n$'dir |
| **S-19** | $\mu$ / $\eta_E$ | Resmî sembol $\eta_E$; $\eta_z$ metinden kaldırıldı. $\mu$ yalnız standart Navier–Stokes alıntısında. **Birim kararı: $\eta_E$ dinamik viskozitedir (Pa·s)** — Stokes biçimi $6\pi\eta_E r_t/m$ bunu gerektirir; kinematik biçim gerekirse $\nu_E=\eta_E/\rho_0$ türetilir |
| **S-20** | $G$ | $G$ = kütleçekim sabiti, yalnız **standart fizik atfında**. Teorinin kendi denklemlerinde $\mathcal{G}M$ yazılır. Kesme modülü → $G_s$ |
| **S-21** | $\phi$ | $\phi$ = hacim kesri (Fizeau). Enlem → açık yazım veya $\phi_c$ (coğrafi); interferometre/rampa fazı → $\varphi$ |
| **S-22** | $\beta$ | $\beta=v/c_0$. Ekliptik enlem → açık yazım |
| **S-23** | $z$ | Bağlamsal (kızıla kayma / dikey koordinat); ilk kullanımda etiketlenir |
| **S-24** | $\theta$ | $\theta_{sap}$ (ışık sapma açısı), $\theta_e$ (eksen eğikliği), $\theta$ (geometrik açı) |
| **S-25** | $\lambda$ | $\lambda$ = **Zerre Aralığı** (resmî tanım; "dalga boyu" yalnız standart fizik aktarımında tırnak içinde). Sönüm mesafesi (3.10.5) → $\lambda_s$ |
| **S-26** | $\Psi$ | $\Psi_{Evrenakı}$ korunur; kuantum dalga fonksiyonu $\psi$ ile **ilgisizdir** |
| **S-27** | $\zeta$ | $\zeta$ = **serbest yüzey yükseltisi** (denge gelgiti, 11.1). Gelgit genliği $\Delta\zeta$ ile yazılır; eski yazım $\Delta h$ **geçersizdir** (S-4: $h$ yalnız Planck sabitidir). $\Delta\eta$ kullanılmaz — $\eta_E$ ile çakışır |
| **S-28** | $\Phi$ | Potansiyel bağlamında $\Phi$ = **kuyu derinliği** $(P_0-P)/\rho_n \ge 0$ ($\Lambda = 1-\Phi/c_0^2$; M-42). Kuvvet-1 dinamik potansiyeli → $\Phi_{it} = -\Phi$ (11.1; $\vec a_1=-\nabla\Phi_{it}$). Newton'un öz-kütleçekim potansiyeli (yalnız standart-fizik aktarımında) → $\Phi_N$. İş fonksiyonu (fotoelektrik, eV) → bağlam-yerel $\Phi$ (M-10/M-11) *(karar, 17 Ağu 2026)* |
