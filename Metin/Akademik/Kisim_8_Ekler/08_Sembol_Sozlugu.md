# Ek D — Sembol Sözlüğü ve Notasyon Kuralları

Bu ek, kitabın tamamında geçerli sembol standardını tanımlar. Her sembol kitap genelinde tek bir fiziksel büyüklüğü gösterir; standart fizikten aktarılan semboller çakışma durumunda indislenir. Kompakt özet için bkz. Bölüm 1.6.1.

## D.1 Notasyon Kuralları

1. **Tek sembol, tek anlam.** Çakışan tarihsel kullanımlar aşağıdaki tabloda "eski yazım" sütununda kayıtlıdır.
2. **Frekans daima $\nu$** ile gösterilir. $f$ sembolü yalnızca Fizeau sürükleme katsayısı ($f = 1 - 1/n^2$) için ayrılmıştır.
3. **Kavrama Yasası eşitliktir ve aynı zamanda hâl denklemidir:** $c=\sqrt{P/\rho}$, yani $P=c^2\rho$. Bu, **stiff (Zel'dovich) akışkan** hâl denklemidir ve dalga kanalında geçerlidir (deplasman alanı sabit): $(\partial P/\partial\rho)_\chi=c^2$, dolayısıyla **akustik dalga hızı tam $c$**'dir. Ortamın $c$'yi aşan tepkisi sıkışmada değil **kohezyon kanalındadır** ($v_m$, M-5). *(Ek B.3'ün $k$'sı bu kanala ait değildir; o, sabit yoğunlukta işleyen **deplasman** sürecinin katsayısıdır ve $k=0$'dır — Ek M-44. Bir ara kayıt akustik hızı $c/\sqrt k$ yazıyordu; kategori hatasıydı, düzeltildi.)*
4. **İşaret (kuyu) konvansiyonu:** Kütle çevresinde $dP/dr > 0$; itim ivmesi $\vec a = -\tfrac{1}{\rho_n}\nabla P$. $\nabla P$ tek başına "kuvvet" değildir; kuvvet $-\nabla P$ yönündedir. Skaler basınç farkı $\Delta P$ ile yazılır.
5. **Arka plan basıncı:** $P_0 = \tfrac14\rho_n c^2 = 6{,}07\times10^{33}$ Pa. Türetim zincirinde genel biçim $\tfrac{1-k}{4}\rho_nc^2$ yazılabilir, ama **$k=0$ artık türetilmiştir** (deplasman süreci yoğunluğu korur — Ek M-44), dolayısıyla sonuç kesindir; "$k$'ya duyarlı" kaydı geçersizdir. (Formülün $\tfrac{1-k}{2}$'li eski hâli, $\delta c/c=\delta f/f$ varsayımına dayanıyordu; ölçek yapısı $\delta c/c = 2\,\delta f/f$ verdiği için 1/4'e indi — bkz. Ek M-42.)
6. **Ondalık:** metin gövdesinde virgül; LaTeX bloklarında nokta kabul edilir.
7. **Ölçek ayrımı ($\Lambda$ ↔ $c_{loc}$):** "Yerel ışık hızı" tek büyüklük değildir. **Saat, cetvel ve atomik frekans** bağlamında daima madde ölçeği $\Lambda = 1-\Phi/c^2$ yazılır; **yayılım, bükülme, Shapiro ve $n_{eff}$** bağlamında daima yayılma hızı $c_{loc} = c\Lambda^2$ yazılır. Tek büyüklüğe indiren eski yazım ($c_{yerel}$) terk edilmiştir — bkz. Ek M-42.

8. **İki eşik, iki kanal.** Ortamın $c$'yi aşan tepkileri **tek** bir eşiğe bağlanamaz; hangi olgunun hangi eşiğe ait olduğu karıştırılmamalıdır:

   | Kanal | Eşik | Yönettiği büyüklükler | Katalog |
   |---|---|---|---|
   | **Kavrama / patinaj** | $c=\sqrt{P/\rho}$ | dönme sürüklenme kesri $\xi$ | Ek M-40 (+M-42) |
   | **Kavitasyon / yırtılma** | $v_{kav}=\sqrt2c\sqrt{1+\Sigma/P_0}$ | öteleme artık sürüklemesi, $\tau_{ret}$, $\eta_E^{etkin}$ | Ek M-43 (+M-4) |

   Sürükleme kohezyon kanalının, $\xi$ ise kavrama kanalının büyüklüğüdür — adı da bunu söyler ("patinaj"). $\xi$'yi $v_{kav}$'a bağlama girişimi bu yüzden sayısal olarak tutmaz ve Bell alt sınırıyla çelişir. **Sıkışma kanalı** ise $c$'yi aşmaz: hâl denklemi stiff olduğundan akustik hız tam $c$'dir (kural 3). Deplasman ise bir hız değil, sabit yoğunlukta işleyen statik tepkidir ($k=0$) ve bu ikisinden ayrıdır.

## D.2 Ortam (Evrenakı) Büyüklükleri

| Sembol | Anlamı | Birim / Değer | Tanımlandığı yer |
|---|---|---|---|
| $P$ | Yerel Evrenakı basıncı | Pa | Postülat 1, 6 |
| $P_0$ | Arka plan (derin uzay) basıncı; $\nabla P_0 = 0$ | $\tfrac14\rho_n c^2 = 6{,}07\times10^{33}$ Pa ($k=0$, Ek M-44) | Ek B.3 |
| $P_{ref}$ | Galaktik log-profilde $r_0$'daki referans basınç *(eski yazım: $P_0$ — 4.2.9.2)* | Pa | 4.2.9.2 |
| $\bar P_m$ | Madde içinde hacimce ortalanmış basınç $= P_0(1-\phi)$ | Pa | 3.4.6.3 |
| $\Delta P$ | Basınç açığı/farkı; Dünya merkezi için $\approx 0{,}83\times10^{25}$ Pa | Pa | Ek B.2 |
| $\nabla P$ | Basınç gradyanı; $\nabla P_r$ radyal, $\nabla P_{spin}$ dönme kaynaklı bileşen | Pa/m | Postülat 6, Ek B.1 |
| $\rho$ | Yerel Evrenakı yoğunluğu *(eski yazım: $\rho_E$)* | kg/m³ | Postülat 1 |
| $\rho_0$ | Arka plan yoğunluğu $= P_0/c^2 = \tfrac14\rho_n$ | $6{,}8\times10^{16}$ kg/m³ | Ek B.3 |
| $\rho_n$ | Nükleon/Zerre öz yoğunluğu (evrensel sabit) *(eski yazım: $\rho_z$, $\rho_{zerre}$)* | $\approx 2{,}7\times10^{17}$ kg/m³ | Postülat 4 |
| $\bar\rho_m$ | Madde içinde hacimce ortalanmış yoğunluk ($=\rho_0$, korunum) | kg/m³ | 3.4.6.3 |
| $\rho(r)$ | Galaktik vorteks yoğunluk profili (serbest profil fonksiyonu, Ek C P1) | — | 4.2.9 |
| $\Sigma$ | Kohezyon (çekme) dayanımı | $\Sigma/P_0 > 10^8$ | Ek A.3 |
| $\eta_E$ | Artık kuplaj katsayısı, Stokes biçiminde parametrize *(eski yazım: $\eta_z$ — Bölüm 3.10; $\mu$ yalnız standart Navier-Stokes alıntısında)*. **Evrensel akışkan sabiti değildir:** $\eta_E^{etkin} = C_D\rho_0 a_b v^{1+n}/12v_{kav}^{n}$ ile cisme ve bağıl hıza bağlıdır; Phoebe için $3{,}3\times10^{-5}$ Pa·s | türetilmiş (T), M-43 | Postülat 7, Ek M-37, **Ek M-43** |
| $n$ | **Altkritik bastırma üssü:** $F_{artık} = \tfrac12 C_D\rho_0 v^2 A\,(v/v_{kav})^{n}$. Süper-akışkanda kritik hız altındaki kuplaj bastırmasının üssü; $\eta_E$'nin yerini alan boyutsuz serbest kalem | $n\simeq3$ (S — Phoebe'den) | **Ek M-43** |
| $C$ | Ortamın deplasman→basınç direnç katsayısı; gözleme yalnız $Cq_n$ çarpımı bağlanır | kg·m⁻³·s⁻¹, serbest (F). **[T-aday]** değer: $2{,}35$ (M-45, $\sqrt2c$ çapasıyla) | Ek M-35, **M-45** |
| $q_n$ | **Nükleon başına pulsasyon hacim debisi** ($\omega_2$ pompasının kaynak şiddeti). $\alpha = Cq_n/4\pi m_n$ ile gradyan bağlaşım sabitini, dolayısıyla $G$'yi üretir | m³·s⁻¹, serbest (F) — gözleme yalnız $Cq_n$ çarpımı ($G$) ve $q_n/2\gamma_n=\ell_\omega^{mikro}$ oranı bağlanır. **[T-aday]** değer: $1{,}62\times10^{-19}$ (M-45) | **Ek M-35**, 6.5.4.3, **M-45** |
| $\gamma_n$ | **Nükleon başına dolanım (sirkülasyon) debisi** ($\omega_1$ kolunun kaynak şiddeti); galaktik F4'ün genliğini besler. $\gamma_N=NV_n$ (etkileşim hacmi) ile karıştırılmamalıdır | m²·s⁻¹, serbest (F) — gözleme yalnız $q_n/2\gamma_n$ oranı bağlanır. **[T-aday]** değer: $2\pi r_n\sqrt2c=2{,}24\times10^{-6}$ (M-45) | **6.5.4.3**, **M-45** |
| $\ell_\omega^{mikro}$ | **Vortisite uzunluğu** $= q_n/2\gamma_n$: nükleonun pulsasyon debisinin dolanım debisine oranı — **mikro sabittir.** Fiziksel anlamı: komşuda dolanım alanının pulsasyon alanını geçtiği yarıçap ($v_t/v_r=d/\ell_\omega$); nükleer–atomik ölçek boşluğunda oturur. $a_0=\mathcal{G}m_n/\ell_\omega^2$ bileşkesinin girdisi. **[T-aday] özdeşlik:** $\ell_\omega=r_n\sqrt{m_p/m_e}=36{,}05$ fm (eşbölüşüm M-45'te türetildi; %1 örtüşme ölçüm hatası içinde — oran tam olmalı; G-9) | **S** — ölçümü $35{,}7$ fm (133 galaksi; kütleyle korelasyon $+0{,}03$; saçılma 0,17 dex) | 6.5.4.3 Adım 6–7, 6.5.4.5 |
| $N_c$ | **Tutarlılık kümesi büyüklüğü:** rastgele yürüyüşün bağımsız birimi başına etkin dolanım sayısı; $\Gamma_{etkin}=\gamma_n\sqrt{N_cN}$, $M_{tut}=N_cm_n$. Küme **atom çekirdeğidir** (fazdan bağımsız); pencere $[X,\langle A\rangle]$ — taban: eşlenme sönmesi (hidrojen kütle kesri), tavan: tam iç uyum | **T** (pencere) — $\approx[0{,}71;\,2{,}2]$; sınıf ölçümleri 0,65–1,55 (uçlar 2,5–3,0) | **6.5.4.3 Adım 7** |
| $\lambda$ (tutarlılık) | Pencere-içi konum: ortamın çekirdekler-arası dolanım muhasebesi ($N_c=X+\lambda(\langle A\rangle-X)$). Çekirdek-içi olamaz (enerji kilidi); ortalama polarizasyon tam sıfırdır ($\varepsilon<3\times10^{-35}$ — $\sqrt{N}$ dolanım korunumunun teoremi). Aday belirleyici: ortamın kaskad karakteri (incelik/dinamik soğukluk); $\lambda\leq1$ | ölçülen: Im $\approx0$ · ana sınıflar 0,14–0,68 · S0/BCD $\approx1{,}6$ (temiz örneklemde $<1$'e inmeli — G-8); ilk $v/\sigma$ sınavı (18 gal.) $+0{,}49$, $p=0{,}019$ — öngörülen yönde ilk işaret; nicel bağıntı **açık** (7.4) | 6.5.4.3 Adım 7 |
| $\ell_\omega^{etkin}(R)$ | Galaktik ölçekte kurulan **net** dolanımın etkin uzunluğu $= \ell_\omega^{mikro}\sqrt{N(R)} = \sqrt{\mathcal{G}M_{kaps}(R)/a_0}$. Galaksiden galaksiye beş mertebe yayılır — yayılım $\sqrt{N}$ çarpanıdır, serbestlik değildir | türetilmiş (T) | 6.5.4.3–6.5.4.5 |
| $\kappa_d$ | İçsel deşarj sabiti (fonksiyon ailesi) | serbest (F) | 3.1.8 |
| $S(x,t)$ | Süreklilik denklemi kaynak/kuyu terimi | kg/(m³·s) | 4.2.2 |
| $S_{kozmik}$ | Evrensel deşarj kaynak terimi $= 3\rho_0 H_0$ | — | 4.2.11 |
| $k$ | **Deplasman** sürecinde $\rho$'nun $P$'ye eşlik oranı — maddenin ortamı dışlaması yoğunluğu değil basıncı değiştirir. **Dalga kanalının adiyabatik katsayısıyla karıştırılmamalıdır** (o, $(\partial P/\partial\rho)_\chi=c^2$'dir). | **$k=0$**, türetilmiş (T): M-15 G2 + M-30 Varsayım 1 | Ek B.3, **Ek M-44** |
| $\chi$ | **Deplasman alanı** — maddenin doğurduğu, kütle-itim kuyusunu taşıyan ikinci durum değişkeni. Hâl denklemi $P=P(\rho,\chi)$; nükleonlar $\chi$'nin kaynağıdır ve $\chi$ kütlenin dışında da sıfır değildir | — | **Ek M-44** |
| $\phi$ | **Deplasman hacim kesri** — maddenin Evrenakı'yı deplase ettiği hacim oranı; $\phi=1-1/n^2$ (M-15). **İki rolü vardır:** (i) Fizeau sürükleme katsayısı $f=\phi$ (M-16), (ii) **kavrama kesri** $\mathcal{R}=\phi$ — cismin ortamını ne kadar döndürdüğü, $v_e=\phi\,\omega R$ (M-39, M-40). Kütleyle değil **hacimle** ölçeklenir: su için $\phi=0{,}437$ iken $\rho_{su}/\rho_n=3{,}7\times10^{-15}$; deplasman kafesi bare nükleon değil **atomun tamamıdır** | su: 0,437 · kayaç: ~0,6 · iyonize plazma: $\sim10^{-15}$ · nötron maddesi: ~0,7–0,9 | M-15, M-16, **M-39**, **M-40** |
| $\mathcal{R}$ | İç kavrama kesri $=\phi$ (kafesin içindeki ortamı yönetir). Gövdenin *dışındaki* dipolar alanı yöneten $\xi$'den **ayrı büyüklüktür**; sınırda eşleşmeleri gerekmez — sınır kafesin bittiği yerdir | $=\phi$ | **Ek M-40** ("İki kavrama kanalı") |
| $\Xi$ | Kuyu iskeleti gücü / baryonik öz-çekim oranı | $\approx 5$ | 3.7.4 |
| $\Psi_{Evrenakı}$ | Toplam Evrenakı alanı $= \Psi_0 + \sum_i \psi_i$ (kuantum dalga fonksiyonu $\psi$ ile ilgisizdir) | — | 1.3.1 |

## D.3 Hız Merdiveni

| Sembol | Anlamı | Değer |
|---|---|---|
| $c$ | Yerel ışık hızı = Kavrama (patinaj/sonik) sınırı: $c = \sqrt{P/\rho}$; mutlak üst sınır **değildir** | arka planda $2{,}998\times10^8$ m/s |
| $\Lambda$ | **Madde ölçeği:** $\Lambda \equiv 1 - \Phi/c^2$. Cetvelleri ($\ell_{loc}\propto\Lambda$), saatleri ve **atomik geçiş frekanslarını** ($\nu_{tik}\propto\Lambda$) yöneten ortak çarpan. Kızıla kayma ve Zerre-Saati bağıntılarında geçen büyüklük budur (Ek M-21, M-42). *(Standart kozmolojinin kozmolojik sabiti gerektiğinde **$\Lambda_{kozm}$** yazılır; indissiz $\Lambda$ daima madde ölçeğidir. "$\Lambda\text{CDM}$" birleşik model adı olarak dokunulmaz. Anayasa S-11/R-10.)* | $1-\Phi/c^2$; Dünya yüzeyi için $1 - 7\times10^{-10}$ |
| $c_{loc} = c\Lambda^2$ | Zerre'nin arka plan (düz) uzayda ölçülen **yayılma hızı**. Işık bükülmesi, Shapiro gecikmesi ve etkin kırılma indisinde ($n_{eff} = 1/\Lambda^2$) geçen büyüklük budur (Ek M-42). Saat/frekans bağlamında $c_{loc}$ **kullanılmaz** — orada $\Lambda$ geçer. | — |
| $c_{loc,kaynak}$, $c_{loc,alıcı}$ | Konuma bağlı yayılma hızı değerleri (Doppler'in uzaysal/Zerre Aralığı çarpanı) *(eski yazım: $c_{kaynak}$, $c_{alıcı}$)* | — |
| $\Lambda_{kaynak}$, $\Lambda_{alıcı}$, $\Lambda_{ref}$ | Konuma bağlı madde ölçeği değerleri (kızıla kayma zinciri) *(eski yazım: $c_{yerel}$, $c_{kaynak}$, $c_{alıcı}$, $c_{ref}$ — M-42 öncesi tek büyüklük sayılıyordu)* | — |
| $c_f$ | Fiber içi ışık hızı *(eski yazım: $C$ — 5.2.9.2)* | $\approx 1{,}794\times10^8$ m/s |
| $\sqrt{2}\,c$ | Girdap zarfının denge yüzey hızı ($v_{denge}$) | $4{,}24\times10^8$ m/s |
| $v_{ekvator}$ | Protonun kompozit ekvator hızı $= 2\pi\nu_c R_p$ | $\approx 5\times10^8$ m/s $\approx 1{,}67c$ |
| $v_m$ | Kohezyon kanalı sinyal hızı $= \sqrt{\Sigma/\rho_0} = c\sqrt{\Sigma/P_0}$ | $> 10^4\,c$ |
| $v_{kav}$ | Kavitasyon eşiği $= \sqrt{2}\,c\,\sqrt{1+\Sigma/P_0} \approx \sqrt{2}\,v_m$ | $\gg c$ |
| $v_{saf}$ | Alt-bileşenlerin saf dönüş hızları | $> v_{kav}$ |
| $v_{bağıl}$ | Cisim–Evrenakı bağıl hızı (sürüklenme zarfı içinde $\approx 0$) | — |
| $v_\theta(r)$ | Girdabın teğetsel hızı; ideal girdapta $\Gamma/2\pi r$ | — |
| $v_0$, $r_0$ | Bileşik (Rankine) girdapta düz-hız değeri ve **rejim geçiş yarıçapı**: $r_0$, küresel akı geometrisinin ($1/R^2$) silindirik geometriye ($1/R$) döndüğü yarıçaptır — Güneş Sistemi'nin Kepler'de kalmasını ve galaktik düz dönüş eğrisini aynı sayı belirler (türetilmemiş; serbest F, Ek C P1) | — |
| $u_{ort}$ | Momentum-ağırlıklı ortalama sürüklenme hızı $= \phi u$ *(eski yazım: $w$ — 3.4.6.3)* | — |
| $u$ | Akan ortamın (ör. suyun) hızı — Fizeau bağlamı; Doppler'de alıcı hızı | — |
| $\beta$ | $v/c$ | — |

## D.4 Mikro Evren ve Işık

| Sembol | Anlamı | Değer |
|---|---|---|
| $m_z$ | Zerre kütlesi (evrensel sabit) | $\approx 1{,}47\times10^{-35}$ kg |
| $V_z$, $r_z$ | Zerre hacmi ve yarıçapı | $5{,}44\times10^{-53}$ m³; $2{,}35\times10^{-18}$ m |
| $\lambda$ | **Zerre Aralığı:** ardışık iki Zerre arası fiziksel mesafe ("dalga boyu" yalnız standart fizik aktarımında tırnak içinde kullanılır) | — |
| $\nu$ | Frekans: **tek katarın içindeki** ardışık Zerrelerin birim zamanda hedefe çarpma ritmi; rengi belirler *(eski yazım: $f$ — 2.2.3)* | — |
| şiddet ($S_ş$) | Işık şiddeti (parlaklık): **birim alana düşen Zerre katarı sayısı** — frekans katarın içini, şiddet katarların sayısını sayar (Bölüm 2.2.3, 2.3.5) | — |
| $\nu_c$ | Compton frekansı | $\approx 10^{23}$ Hz |
| $h$ | Planck sabiti; mekanik özdeşliği $h = \delta\tau$ | — |
| $\hbar$ | İndirgenmiş Planck sabiti $= h/2\pi$ | — |
| $\delta$ | Tek vuruşta aktarılan enerji $= \eta\cdot\tfrac12 m_z(c^2 + k_a v_{cev}^2)$ | $\approx 2{,}8\times10^{-4}$ eV; serbest (F) |
| $\tau$ | Kopma penceresi | serbest (F) |
| $N$ | Kopma penceresindeki vuruş sayısı $= \nu\tau$ | $\approx 1{,}5\times10^4$ |
| $\eta$ | Tek-vuruş elastik aktarım verimi $\approx 4m_z/m_e$ | $\approx 6{,}5\times10^{-5}$ |
| $k_a$ | Zerre atalet (kütle dağılımı) katsayısı *(eski yazım: $k$ — 2.2.2)* | $2/5$ (homojen küre) |
| $v_{cev}$ | Zerre'nin evrensel çevresel dönüş hızı | belirlenmemiş (açık iş) |
| $\varphi$ | Katar ritmi ile rampa çevrimi arasındaki göreli faz | — |
| $n$ | Kırılma indisi; $1/n^2 = 1-\phi$ *(paket tam sayısı için $N_p$ kullanılır)* | — |
| $\phi$ | Moleküllerin hacim kesri = Fizeau katsayısı $f = 1 - 1/n^2$ — **tam kayıt ve ikinci rolü (kavrama kesri) için bkz. D.2** | su: $0{,}437$ |
| $I$ | Atalet momenti *(ışık şiddeti için ayrı sembol: metinde "şiddet" veya $S_ş$)* | — |
| $A$ | Dalga genliği ($I_ş \propto A^2$) *(eski yazım: $E$ — 2.7.1)* | — |
| $E$ | Enerji (yalnız enerji) | — |
| $\Phi$ | İş fonksiyonu (fotoelektrik) / standart fiziğin "kütleçekim potansiyeli" — yalnız ölçülen genlik girdisi olarak (Ek B bağlamında, $\Phi/c^2 \approx 7\times10^{-10}$) | — |
| $D_{toplam}=D_{zarf}+D_{yol}$ | SN 1987A gecikme bütçesi bileşenleri | ~3 saat |
| $\chi$ | Evrenakı dispersiyon katsayısı (fenomenolojik) | $5\times10^{-4}$ |
| $g^{(2)}(0)$, $S$ | Standart kuantum optik ölçütleri (anti-demetlenme; CHSH istatistiği) | — |

## D.5 Dönüş ve Makro Evren

| Sembol | Anlamı |
|---|---|
| $w$, W | Dördüncü uzay ekseni; uzayımız $w=0$ kesiti *(karanlık enerji hâl denklemi $w$ yalnız 7.7.9'da, açık etiketle)* |
| $\omega_1$ | Çift dönüşün hızlı bileşeni (3B içi düzlemde, Compton düzeyi) |
| $\omega_2$ | Çift dönüşün yavaş bileşeni (W eksenli düzlemde; devinim kaynağı) |
| $\omega_Z$ | Zitterbewegung frekansı $\approx 2mc^2/\hbar$ |
| $\Omega_{yör}$ | Yerel yörünge (girdap) açısal frekansı |
| $\Omega_{dön}$ | Gök cisminin dönüş açısal hızı *(eski yazım: $\Omega$ — 3.6.3)* |
| $\Omega_z$ | Halka parçacığının dikey salınım frekansı $= \sqrt{GM/r^3}$ *(eski yazım: $\Omega$ — 3.10.3)* |
| $\vec\omega_v$ | Vortisite $= \nabla\times\vec v$; rotasyon vektörü $= \tfrac12\nabla\times\vec v$ *(eski yazım: $\vec\Omega$)* |
| $\Gamma$ | Girdap sirkülasyonu *(3.4.4'teki termal tutamaç şiddeti $\Gamma$ bağlamla ayrılır)* |
| $r_{cep}$ | Vakum cebi yarıçapı $= \Gamma/2\pi\sqrt{2}c$ *(eski yazım: $a$ — Ek A.2)* |
| $r_t$ | Tanecik yarıçapı (Stokes sönümü $\gamma_{ortam} \sim 6\pi\eta_E r_t/m$) *(eski yazım: $a$ — 3.10.4.2)* |
| $g$, $g(R)$, $R_c$, $p$, $q$, $q_{peri}(e)$ | Kavrama/kilitlenme parametreleri (Bölüm 3.4.4) |
| $e$ | Yörünge basıklığı; kilit modu eşiği $e \approx 0{,}125$ |
| $\gamma$ | Lorentz / çapraz-yol uzama çarpanı $= 1/\sqrt{1-v^2/c^2}$ |
| $\gamma_{ortam}$, $\gamma_{standart}$, $\gamma_{toplam}$ | Sönüm oranları (Bölüm 3.10.4) |
| $\gamma_N$ | Cismin etkileşim hacmi $= NV_n$ *(eski yazım: $\gamma$ — 4.2.4)* |
| $G$, $\mathcal{G}$ | Yerleşik adıyla "kütleçekim sabiti"; teoride türetilmiş ve **yerel** (Postülat 4): $\mathcal{G} = \alpha/\rho_n$ (M-28). Teori kendi denklemlerinde $\mathcal{G}$ yazar; düz $G$ yalnız standart-fizik aktarımında, Newton-kalibrasyon bağlamında (M-27) ve ölçülen yerel değer/$GM$ çarpımı bağlamında kalır *(kesme modülü için $G_s$)* |
| $\alpha$ | Gradyan bağlaşım sabiti [s⁻²]; $P(r) = P_0 - \alpha M/r$ *(ince yapı sabiti: $\alpha_{is}$ veya açık yazım)* |
| $H_0$ | Hubble sabiti $= S_{kozmik}/3\rho$ |
| $\xi$ | **Dönme sürüklenme kesri:** ortamın gövde dönüşüne tutunma oranı, $\vec\Omega_{ortam} = \xi\,\vec\omega_{gövde}$. Türetilmiştir — ortam bir cismi ancak kavrama hızının bozulduğu ölçüde tutar: $\xi = \dfrac{I}{MR^2}\left\lvert\dfrac{\delta c_{loc}}{c}\right\rvert = \dfrac{I}{MR^2}\dfrac{2\Phi}{c^2}$. Dünya: $4{,}605\times10^{-10}$; nötron yıldızı: $\sim0{,}1$. Ötelemedeki *tam* sürüklenmeden (Postülat 7) ayrıdır — bu neredeyse tam **patinajdır** | **Ek M-40**; girdisi Ek M-42 |
| $\kappa_5$ | **Yanal itim deplasman kapanış katsayısı:** $f_{yanal}(\theta) = -\dfrac{\kappa_5\,\rho\,v_e^2}{r}\sin2\theta$ [N/m³]. Ekvatordan kutba deplasman muhasebesini kapatan boyutsuz çarpan | boyutsuz, serbest (F); $\tfrac12$ çalışma değeri | **Ek M-39** |
| $\tau_{ret}(r,e,i)$ | Retrograd sönüm zaman ölçeği *(eski yazım: $\tau$ — 3.6.1)*. Stokes yazımında $2\rho_c a_b^2/9\eta_E$ (hızdan bağımsız); altkritik yazımda $\propto \rho_c a_b v_{bağıl}^{-4}$ — **iki yazımı ayıran sınav budur** (Ek M-43) |
| $f(\theta_e)$ | Hizalanma verimi ($\theta_e$: eksen eğikliği; türetilmemiş) |
| $J_2$ | Dünya basıklık (kuadrupol) katsayısı |
| $R_p$, $R_\oplus$, $R_s$ | Proton yarıçapı ($0{,}84$ fm); Dünya yarıçapı; yüzey yarıçapı |
| $\lambda_s$ | Bending-wave sönüm mesafesi $= v_{grup}/\gamma_{toplam}$ *(eski yazım: $\lambda$ — 3.10.5)* |
| $\lambda_z$ | Dispersiyon türetimindeki Zerre aralığı *(eski yazım: $\Lambda$ — bu sembol artık madde ölçeğine ayrılmıştır; bkz. D.3 ve Ek M-42)* |

## D.6 Statü Kodları (Ek C ile ortak)

**T** türetilmiş · **S** gözlemle sabitlenmiş · **A** aralıkla sınırlanmış · **F** serbest · **G** gözlemsel girdi

Serbest parametre bilançosu (Ek C.1): **5 skaler** ($\Sigma$, $n$, $\kappa_d$, $\tau$, $\delta$) + 2 profil fonksiyonu ($\rho(r)$, rampa profili). *(29 Tem 2026: $\eta_E\to n$ — Ek M-43; $k$ listeden çıktı, $k=0$ türetildi — Ek M-44. Toplam 6 → 5.)*
