# Ek M — Yeni Girdiler: Ortamın Hız Alanı (M-51 … M-54) · ✅ TAŞINDI

> **DURUM: 17 Ağustos 2026'da yayın metnine TAŞINDI** (Enes onayı: *"yayın metnine taşı"*).
> Dört girdi `Kisim_8_Ekler/10_Ek_M_Blok_B_Arka_Plan_Basinci.md`'nin sonuna eklendi (satır 131, 186, 248, 321).
> Bağlı düzeltmelerin tamamı uygulandı — **taşıma kaydı bu dosyanın en sonundadır.**
> Bu dosya artık tarihsel kayıt/karşılaştırma amacıyla saklanmaktadır.
> **Kaynak çalışmalar:** `ortam_hiz_alani_cozumu.md` · `ortam_donusu_kilit_teoremi.md` · `es_duzlemlilik_cozumu.md` · `formasyon_gerekcesi.md`
> **Sınav betikleri:** `ortam_hiz_alani_sinavi.py` · `ortam_dolasimi_mp.py` · `saturn_ortami_sinavi.py` · `es_duzlemlilik_sinavi.py` · `formasyon_gerekcesi_sinavi.py`
>
> **⚠️ Numara kararı gerekiyor.** Kitapta en yüksek katalog numarası M-50'dir (Blok I). Bu taslak M-51…M-54'ü kullanıyor. Ancak üstel ölçek yapısı girdisi de (ayrı çalışma, `DEVIR_KAYDI_ustel_olcek.md`) numara bekliyor. Öneri: **üstel yapı M-55**, aşağıdaki dördü M-51…M-54 — çünkü bu dördü üstel yapıdan **bağımsızdır** ve ondan önce yerleşebilir.
>
> **Blok yerleşimi önerisi:** Dördü de **Blok B'nin devamı** (Arka Plan Basıncı ve Ağırlıksızlık, M-7…M-9). Gerekçe: hepsi M-9'un Geçerlilik Sınırı'nın eksenindedir ve M-4/M-5'in kohezyon kanalını kullanır. Blok B'nin kapsam cümlesi buna göre genişletilmelidir.
>
> **Λ-bağımsızlık kaydı:** Aşağıdaki dört girdinin hiçbiri madde ölçeği $\Lambda$'nın *biçimine* bağlı değildir; yalnız $\nabla P$, $\rho_n\Phi$, $\Sigma$ ve yörünge kinematiği kullanılır. Üstel geçiş yapılsa da yapılmasa da geçerlidirler.

---

## M-51 · Ortamın Statik Dengesi: Kuyu Kesmeyle Tutulur · **[T]**

**Kullanıldığı bölümler:** M-9 (Geçerlilik Sınırı — bu girdi onu düzeltir), M-4/M-5 (kohezyon kanalı), M-2 (kütle-itim), M-22/M-37 (ortam profili), 3.4.x. Bağlı katalog: **M-52** (dönüş kilidi), **M-53** (dolaşımın yokluğu).

### Varsayımlar
1. Kütle çevresinde basınç kuyusu vardır: $dP/dr>0$, dış alanda $P(r)=P_0-\rho_n\Phi(r)$ ile $\Phi=\mathcal{G}M/r\ge0$ (M-2'nin kuyu konvansiyonu; M-46'nın $\chi$ Poisson'u).
2. Ortam yalnız izotropik basınç taşımaz: **kohezyon dayanımı $\Sigma$ vardır** (M-4) ve $\Sigma$, kesme/gerilme kanalının modülü rolündedir — $v_m=\sqrt{\Sigma/\rho_0}$ (M-5). Gözlemsel taban: $\Sigma/P_0>10^8$ (Bell tipi deneyler; Salart ve ark., 2008).
3. Durağan hâl incelenir ($\partial\vec v/\partial t=0$) ve küresel simetri varsayılır.

### Adımlar
1. **Euler denklemi kohezyonsuz limittir.** Gerilme tensörü yalnız izotropik alınırsa ($\sigma_{ij}=-P\delta_{ij}$), statik denge imkânsızdır: $\nabla\!\cdot\!\sigma=-\nabla P\neq0$. Bu durumda ortamın tek çıkışı dolaşmaktır — M-9'un Geçerlilik Sınırı'ndaki siklostrofik sonuç bu limitin ürünüdür.
2. **Ortam kohezyonlu olduğundan gerilme tensörü izsiz bir pay taşır:** $\sigma_{ij}=-P\delta_{ij}+\tau_{ij}$, $\operatorname{tr}\tau=0$. Statik denge $\nabla\!\cdot\!\sigma=0$; küresel simetride radyal bileşen
$$\frac{d\sigma_{rr}}{dr}+\frac{2\sigma_{rr}-\sigma_{\theta\theta}-\sigma_{\varphi\varphi}}{r}=0$$
3. İzsizlik ($\tau_{rr}+2\tau_{\theta\theta}=0\Rightarrow\tau_{rr}-\tau_{\theta\theta}=\tfrac32\tau_{rr}$) konularak:
$$\frac{d\tau_{rr}}{dr}+\frac{3\tau_{rr}}{r}=\frac{dP}{dr}=\frac{\rho_n\mathcal{G}M}{r^2} \;\Longleftrightarrow\; \frac{1}{r^3}\frac{d\left(r^3\tau_{rr}\right)}{dr}=\frac{\rho_n\mathcal{G}M}{r^2}$$
4. Sonsuzda sönen çözüm (homojen kol $C/r^3$ için $C=0$):

### Sonuç
$$\boxed{\;\tau_{rr}=\frac{\rho_n\mathcal{G}M}{2r}=\frac{\rho_n\Phi}{2}=\frac{\Delta P}{2}\;,\qquad \tau_{\theta\theta}=\tau_{\varphi\varphi}=-\frac{\tau_{rr}}{2}\;}$$

**Kuyuyu tutmak için gereken kesme gerilmesi, basınç açığının tam yarısıdır** ve ortam bunu **dolaşmadan** sağlar. Genel denge, dolaşım ile kohezyonun bölüşümüdür:
$$\frac{1}{\rho_0}\frac{dP}{dr}=\underbrace{\frac{v_\theta^2}{r}}_{\text{dolaşım payı}}+\underbrace{\frac{1}{\rho_0}\left(\frac{d\tau_{rr}}{dr}+\frac{3\tau_{rr}}{r}\right)}_{\text{kohezyon payı}}$$
$v_\theta=2v_{yör}$ (M-37), kohezyon payının sıfır olduğu **kohezyonsuz üst sınırdır**; $v_\theta=0$ izinlidir ve kohezyon tüm yükü taşır.

### Madde kesmeyi görmez — bağlayıcı kayıt
M-2'nin Varsayım 2'si itimin **deplase edilen hacimle** orantılı olduğunu söyler. Deplase hacim bir **skalerdir**; dolayısıyla deplasman cebi gerilme tensörünün **izine** (yani basınca) bağlanır. $\tau$ **izsizdir** ve saf hacim dışlamasıyla çiftlenmez. Sonuç:
- Ortam kendini **kesmeyle** ayakta tutar (madde bunu hissetmez),
- Madde yalnız **basınç gradyanını** hisseder: $\vec a=-\nabla P/\rho_n$ — **M-2 aynen geçerlidir.**

### $\Sigma$'nın yapısal görevi — bu girdinin en önemli sonucu
$\Sigma$, bu girdiden önce yalnız Bell tipi deneylerden **alttan sınırlı** ve teorinin başka hiçbir yerine yük taşımayan bir kalemdi. **M-52 ile birlikte statüsü değişir:** ortam dolaşmak *zorunda kalırsa* kapalı elips yörüngeler var olamaz (M-52); kuyuyu dolaşmadan tutan tek mekanizma kohezyondur. Dolayısıyla
> **kohezyon kanalı, Kepler yörüngelerinin var olabilmesinin yapısal koşuludur.**

Bu, $\Sigma$ için Bell deneylerinden **tamamen bağımsız ikinci bir gerekçedir.** *(Nicel olarak yeni bir alt sınır vermez — gereken $\tau$ zaten $\Sigma$'nın çok altındadır; kazanç yapısaldır.)*

### Sayısal Çapraz Kontroller
$\Sigma$'nın yalnız **alt sınırıyla** ($\Sigma\ge10^8P_0=6{,}07\times10^{41}$ Pa) gereken kesme:

| Konum | $\Phi/c_0^2$ | $\tau_{rr}$ (Pa) | $\tau_{rr}/\Sigma$ |
|---|---|---|---|
| Merkür yörüngesi | $2{,}55\times10^{-8}$ | $3{,}10\times10^{26}$ | $5{,}1\times10^{-16}$ |
| Dünya yörüngesi | $9{,}87\times10^{-9}$ | $1{,}20\times10^{26}$ | $2{,}0\times10^{-16}$ |
| Güneş yüzeyi | $2{,}12\times10^{-6}$ | $2{,}58\times10^{28}$ | $4{,}2\times10^{-14}$ |
| Dünya yüzeyi | $6{,}96\times10^{-10}$ | $8{,}45\times10^{24}$ | $1{,}4\times10^{-17}$ |
| Samanyolu (Güneş yarıçapı) | $4{,}45\times10^{-7}$ | $5{,}40\times10^{27}$ | $8{,}9\times10^{-15}$ |
| Nötron yıldızı yüzeyi | $0{,}172$ | $2{,}09\times10^{33}$ | $3{,}4\times10^{-9}$ |

**On dört–on beş mertebe marj**; nötron yıldızı yüzeyinde dahi dokuz mertebe. Elastik zorlanma $\varepsilon\sim\tau/\Sigma\sim10^{-16}$.

### Geçerlilik Sınırı
- Küresel simetri ve durağan hâl varsayılmıştır; dönen/basık kaynaklarda $\tau$'nun açısal yapısı devreye girer.
- Homojen kolun ($C/r^3$) katsayısı sonsuzda sönme koşuluyla sıfırlanmıştır; **kaynak içinde** (madde gövdesinin içinde) eşleme yapılmamıştır.
- Tüm marjlar $\Sigma$'nın **alt sınırıyla** hesaplanmıştır. Gerçek $\Sigma$ daha büyükse marj yalnız büyür — bu yönde duyarsızdır.
- Kesme gerilmesinin ortamın **akış** kanalıyla (viskozite) ilişkisi kurulmamıştır; burada yalnız elastik (modül) rol kullanılır.

### Açık Uçlar
- Zarf sınırındaki **kayma tabakası** (Dünya zarfı $\sim30$ km/s, Güneş zarfı $\sim220$ km/s) statik resimde gerçek bir kesme tabakasıdır; gereken gerilme $\sim\rho_0v^2=3{,}3\times10^{27}$ Pa ile $\Sigma$'nın altındadır, ama **yitim ve tork hesabı** hâlâ açıktır (7.4'ün mevcut kalemi).
- Kaynak içi eşleme ve $\tau$'nun madde gövdesi sınırındaki sürekliliği.
- $\Sigma$'nın kesme **modülü** mü **dayanımı** mı olduğunun ayrımı (M-4/M-5 ikisini tek sembolle taşıyor); elastik zorlanma hesabı modül okumasını gerektirir.

### Düzeltme Kaydı (17 Ağustos 2026)
**M-9'un Geçerlilik Sınırı'ndaki *"cevabı düşmek değil dolaşmaktır… siklostrofik dengede"* hükmü, Euler denkleminin (kohezyonsuz akışkanın) sonucudur ve teorinin kendi ortamı için eksiktir.** Kohezyonlu ortamda statik elastik denge açıktır ve gözlem onu seçer (M-52). M-9'un ifadesi *"Madde düşer, ortam dolaşır"* → **"Madde düşer, ortam gerilir"** olarak okunmalıdır. M-9'un çekirdek sonucu (homojen arka planın kuvvetsiz, kararlı ve doğurgan-olmadığı) **etkilenmez**.

---

## M-52 · Ortam Dönüşü Kilit Teoremi: $\Omega_m=2n$ · **[T]**

**Kullanıldığı bölümler:** M-9, M-22, M-37 (profil teoreminin statüsü), M-51, 6.3, 11.3, 11.4, 11.5. Bağlı katalog: **M-53**.

### Varsayımlar
1. Siklostrofik dolaşım hipotezi (M-22/M-37'nin ortam kolonu): $w(r)=v_\theta(r)=2v_{yör}(r)=2\sqrt{\mathcal{G}M/r}$. *(Oran $\sqrt{\rho_n/\rho_0}=2$ tamdır; $\rho_0=\rho_n/4$, M-8.)*
2. Cismin dinamiği **yerel ortama göre** tanımlıdır (11.4.8.1'in açık ifadesi: *"$V$, maddenin yerel ortama göre hızıdır"*).
3. Yörünge dairesele yakındır; dolaşım yörünge düzlemindedir.

### Adımlar
1. **Dolaşan ortamın açısal hızı:**
$$\Omega_m=\frac{w(r)}{r}=\frac{2\sqrt{\mathcal{G}M/r}}{r}=2\sqrt{\frac{\mathcal{G}M}{r^3}}=\boxed{2n}$$
$n$ yörüngenin ortalama hareketidir. **Oran kütleden ve yarıçaptan bağımsızdır.**
2. **Dinamiği ortama referanslı bir cismin apsisleri, ortamla birlikte sürüklenir.** Katı dolaşım limitinde bu, eş-dönen çerçeveye geçmenin doğrudan sonucudur: eş-dönen çerçevede yörünge kapalı elipstir, laboratuvar çerçevesinde $\Omega_m$ hızıyla devinir. Diferansiyel dolaşımda da sürüklenme hızı mertebe olarak $\Omega_m$'dir (sayısal doğrulama aşağıda).
3. **Kategorik sonuç:** $\Omega_m=2n$ ise apsis çizgisi **her radyal periyotta tam iki tur** atar. Yörünge kapalı elips değil, hızla dönen bir rozettir.

### Sonuç
$$\boxed{\;\text{Siklostrofik dolaşım}\;\Longrightarrow\;\Omega_{apsis}=2n\;\Longrightarrow\;\textbf{kapalı elips yörünge var olamaz}\;}$$

> **Gözlenen kapalı elipslerin varlığı, tek başına, ortamın dolaşmadığının kanıtıdır.** Bu bir hassasiyet sınavı değildir: siklostrofik hipotez altında Kepler yörüngeleri hiç oluşmaz. Ölçüm hassasiyeti yalnız **kalan** dönüşün üst sınırını belirler.

### Sayısal Çapraz Kontroller
**(a) Teoremin denetimi** — $\Omega_m/n$ oranı dört sistemde: Merkür, Ay, Titan, Mimas → **2,0000000000**.

**(b) Satürn sistemi** ($J_2$-hâkim apsidal presesyonla kıyas, $\dot\omega=\tfrac32nJ_2(R_S/a)^2(1-e^2)^{-2}$):

| Uydu | $a$ (km) | Gözlenen apsis periyodu | Dolaşımın vereceği | **Dışlama** |
|---|---|---|---|---|
| Mimas | 185.539 | 1,0 yıl | 11,3 saat | $7{,}8\times10^2$ |
| Enceladus | 237.948 | 2,4 yıl | 16,5 saat | $1{,}3\times10^3$ |
| Dione | 377.396 | 12,0 yıl | 1,4 gün | $3{,}2\times10^3$ |
| Rhea | 527.108 | 38,7 yıl | 2,3 gün | $6{,}3\times10^3$ |
| **Titan** | 1.221.870 | **733 yıl** | **8,0 gün** | $\mathbf{3{,}4\times10^4}$ |

*(Iapetus'ta Güneş pertürbasyonu $J_2$'yi aşar; sağlam sınır Titan'dır. Phoebe için dolaşan ortam 4 Gyr'de $5{,}3\times10^9$ tur verirdi.)*

**(c) Dört bağımsız ortam:**

| Ortam | Sınayan gözlem | Dışlama | Kalan dönüş üst sınırı |
|---|---|---|---|
| **Güneş** | Merkür günberi $575{,}3100\pm0{,}0015''$/yy (Park ve ark., 2017) | $1{,}9\times10^6$ | $\lvert\Omega\rvert\le2{,}3\times10^{-18}$ s⁻¹ |
| **Dünya** | Ay perigee presesyonu 8,85 yıl (LLR) | $2{,}4\times10^2$ | $\lesssim2\times10^{-16}$ s⁻¹ |
| Dünya | LAGEOS-2 ($J_2$-hâkim) | $4{,}5\times10^3$ | — |
| **Satürn** | Titan apsisi | $3{,}4\times10^4$ | $\lesssim2{,}7\times10^{-15}$ s⁻¹ |
| **Jüpiter** | Io apsisi ($J_2$-hâkim) | $3{,}2\times10^3$ | — |

**(d) Merkür'ün yeni rolü.** $\lvert\Omega_{ortam}\rvert\le1{,}4\times10^{-18}$ s⁻¹ (1σ), yani Merkür yörüngesinde teğetsel hız $\le81$ nm/s; bir tam tur $1{,}4\times10^{11}$ yıl = evren yaşının **on katı**. Güneş sisteminin ortamı, evren yaşı ölçeğinde fiilen dönmemektedir. **Standart görelilikte bu okumanın karşılığı yoktur** — orada ortam yoktur.

### Geçerlilik Sınırı
- Kilit, **yörünge apsisleri** üzerinden çalışır; apsis ölçümü olmayan ölçeklerde (galaktik) doğrudan uygulanamaz — orada hüküm M-53'ün Ayak 1'inden gelir.
- 2. adımın diferansiyel dolaşım hâli mertebe argümanıdır; kesin katsayı sayısal olarak doğrulanmıştır (`ortam_dolasimi_mp.py`), analitik genel çözüm verilmemiştir.
- Satürn/Jüpiter dışlamaları $J_2$-hâkim apsidal hızla kıyaslanmıştır; gerçek efemerid artıklarıyla çalışılırsa sınırlar bir–iki mertebe sıkışabilir.
- Sonuç, madde ölçeği $\Lambda$'nın **biçiminden bağımsızdır** (yalnız yörünge kinematiği ve ortama-referanslılık kullanılır).

### Açık Uçlar
- Iapetus kanalının gerçek efemerid artıklarıyla işlenmesi (Satürn sınırı $\sim10^{-17}$ s⁻¹'e inebilir).
- Galaktik ortamın dönüş durumunun bağımsız gözlemsel kilidi (apsis kanalı yok).
- **Statü değişimi kaydı:** M-37'nin $v_\theta=2v_{yör}$ profil teoremi **kohezyonsuz üst sınır** statüsüne iner; türetimi doğrudur ($\sqrt{\rho_n/\rho_0}=2$ tam) ama zorunluluk değildir ve gezegen ölçeğinde **gözlemle dışlanmıştır**. M-22'nin *"dönen ortam merkezkaç gereksinimini basınç gradyanıyla karşılar"* varsayımı **opsiyonel dinamik durum** olarak etiketlenmelidir. M-37'nin **madde kolonu** (gözlenen dönüş eğrisi: $v_{yör}=\sqrt{R\lvert a_{madde}\rvert}$) bundan **etkilenmez** — o yalnız M-2 ve akı geometrisini kullanır.
- **Bedel kaydı (dürüst):** Dolaşıma dayanan retrograd/prograd sürükleme asimetrisi ($\Delta v=v$ ↔ $3v$, sürükleme $\propto\Delta v^4$ ⟹ **81 katı**; Triton, DY-2) statik ortamda **oran 1**'e iner. Prograd hesaplar değişmez ($\lvert v-2v\rvert=\lvert v-0\rvert=v$); yalnız retrograd kalemler 81 kat zayıflar ve Phoebe'nin $\eta_E$ sınırı **gevşer**. 7.4 md.15 bu ayrımı zaten sınav olarak kaydetmiştir; statik çözüm *"fark sıfır"* öngörür. Kaybedilen bir öngörü değil, **karara bağlanmış** bir öngörüdür.

---

## M-53 · Dolaşımın Yokluğunun Türetimi: Üç Ayak · **[T]**

**Kullanıldığı bölümler:** M-4, M-5 (kohezyon), M-7 (yırtılmama), M-9 (taban durumu), M-43 (altkritik bastırma), M-51, M-52.

> **Neden gerekli:** M-51 dolaşımın yokluğunu **izinli** kılar, M-52 onu **gözlemsel olarak** doğrular. Ama açısal momentum serbest bir başlangıç koşuludur; teorinin *neden* sıfır olduğunu söylemesi gerekir — yoksa sonuç "şanslı başlangıç koşulu" olarak kalır. Aşağıdaki üç ayak bu itirazı kapatır.

### AYAK 3 (yük taşıyıcı) — Madde ortamı döndüremez
Kesmeyi yaratacak tek kaynak maddedir. İki bağımsız kanal, ikisi de kapalı:

**(a) Enerji kanalı.** Maddenin dönme enerji yoğunluğu ile $\Sigma$ kıyası:

| Sistem | $E_{dönme}/V$ (Pa) | $/\Sigma$ |
|---|---|---|
| Güneş (dönme) | $1{,}7\times10^{14}$ | $2{,}8\times10^{-28}$ |
| Jüpiter | $1{,}5\times10^{11}$ | $2{,}4\times10^{-31}$ |
| Güneş sistemi yörünge KE | $5{,}0\times10^{4}$ | $8{,}3\times10^{-38}$ |
| Galaksi (dönme) | $2{,}4\times10^{-10}$ | $4{,}0\times10^{-52}$ |

**(b) Sürüklenme kanalı.** M-43'ün altkritik bastırması $\sim10^{28}$ ⇒ tork kanalı kapalı.

**M-9'un teoremiyle birleşince** (*"homojen durum yalnızca izinli değil, ortamın tek doğal taban durumudur"*): **kesme hiç doğmadı.** Açısal momentum maddede kalır — yıldızın spini ve gezegenlerin yörüngelerinde; gözlenen de budur.

### AYAK 1 — Diferansiyel dönüş bir denge durumu değildir
M-5 kohezyon kanalını **kesme modülü** rolünde kurar ($\Sigma\leftrightarrow G_s$, $v_m=\sqrt{\Sigma/\rho_0}>10^4c_0$). Kesme modülü olan ortam **kararlı kesme akışı taşımaz**: diferansiyel dönüş zorlanma biriktirir, elastik geri-çağırma devreye girer ve sistem sıfır-kesme durumu etrafında **salınır**. Siklostrofik profil ($\Omega\propto r^{-3/2}$, şiddetle kesmeli) bu yüzden bir **denge çözümü değildir**.

Salınım periyodu $L/v_m$:

| Ölçek | $L/v_m$ | Yörünge / salınım |
|---|---|---|
| Ay yörüngesi | $1{,}3\times10^{-4}$ s | $1{,}8\times10^{10}$ |
| **Merkür yörüngesi** | **0,019 s** | $\mathbf{3{,}9\times10^{8}}$ |
| 1 AU | 0,050 s | $6{,}3\times10^{8}$ |
| Galaksi (10 kpc) | 3,3 yıl | $6{,}7\times10^{7}$ |
| Hubble yarıçapı | **$1{,}37\times10^{6}$ yıl** | $1{,}0\times10^{4}$ |

İki sonuç: **(i)** M-52'nin ölçtüğü sekülér apsis hızı, tanım gereği $\langle w\rangle/r=0$'dır (Merkür yörüngesi başına $3{,}9\times10^8$ çevrim). **(ii)** Hubble ölçeğinde elastik denkleşme 1,37 Myr = evren yaşının $10^{-4}$'ü; ilksel diferansiyel dönüş, hangi başlangıç koşulundan başlanırsa başlansın **$10^4$ denkleşme süresi önce silinmiş** olurdu.

### AYAK 2 — Katı dönüş, sınırsız kohezyonlu ortamda yasaktır
Kesme içermeyen tek dönüş katı dönüştür ($\Omega=$ sabit); Ayak 1 onu dışlamaz. Ama merkezcil gereksinim gerilme ister:
$$\frac{dP}{dr}=\rho_0\Omega^2r \;\Longrightarrow\; \tau_{gerekli}=\frac{\rho_0\Omega^2r^2}{2}$$
$r$ ile **sınırsız büyür** ve $\Sigma$'yı aşar:
$$r_{max}=\frac{\sqrt{2\Sigma/\rho_0}}{\Omega}=\frac{\sqrt2\,v_m}{\Omega}$$
$r>r_{max}$'ta **M-7'nin yırtılmama koşulu ihlal edilir.** Yırtılma gözlenebilir evrenin içinde olmasın koşuluyla **yapısal sınır: $\lvert\Omega\rvert<3{,}3\times10^{-14}$ s⁻¹** (gözlem bundan $1{,}4\times10^4$ kat sıkı). **Ortam sınırsızsa** (monizm — okyanus gözlenebilir evrenin ötesine uzanır) her $\Omega\neq0$ sonlu bir yarıçapta yırtar:
$$\boxed{\;\text{sınırsız kohezyonlu ortam}\;\Longrightarrow\;\Omega=0\ \text{tam}\;}$$

### Sonuç
$$\boxed{\;\text{Diferansiyel dönüş: denge değil (Ayak 1)}\;\cdot\;\text{Katı dönüş: M-7 ihlali (Ayak 2)}\;\cdot\;\text{Madde onu kuramaz (Ayak 3)}\;}$$
Dolaşımın yokluğu artık izin verilen bir seçenek değil, **üç bağımsız yapısal nedenin sonucudur.**

### Sayısal Çapraz Kontroller ve iş bölümü kaydı
**⚠ Ayak 1 tek başına yetmez ve bu açıkça kaydedilmelidir.** Viskozite sıfıra yakın olduğundan salınım **sönmez**: Kelvin–Voigt sönüm süresi ($\eta\le2{,}3\times10^{-11}$ Pa·s ile) 1 AU ölçeğinde $5{,}3\times10^{40}$ yıl. Ve $\langle w\rangle=0$ olsa da $\langle w^2\rangle\neq0$; $\Lambda_{kin}$ $\lvert v-w\rvert$'ye bağlı olduğundan bu bir ek saat terimi verir, $\langle w^2\rangle/2c_0^2$. Merkür yörüngesinde $w_{genlik}=f\,v_{yör}$ için terim/$(\Phi/c_0^2)=f^2/4$:

| $f$ | $w_{genlik}$ | terim/$(\Phi/c_0^2)$ |
|---|---|---|
| 1,0 | 47,9 km/s | **0,25** |
| 0,1 | 4,8 km/s | $2{,}5\times10^{-3}$ |
| **0,02** | **957 m/s** | $\mathbf{10^{-4}}$ |

Tam genlikte terim, kızıla kayma genliğinin **kendisi mertebesindedir** ve kalibrasyonu çökertir. Kızıla kaymanın $\sim10^{-4}$ bağıl doğrulanması (GPS; Pound–Rebka) **$w_{genlik}\le0{,}02\,v_{yör}$** dayatır.
**Çözüm: salınım hiç uyarılmadı** — Ayak 3 + M-9. **İş bölümü bağlayıcıdır:** Ayak 3 + M-9 kesmenin *hiç doğmadığını*, Ayak 1 *doğsa bile kararlı kalamayacağını*, Ayak 2 katı dönüşün de yasak olduğunu gösterir.

### Geçerlilik Sınırı
- Ayak 2'nin en güçlü kolu ($\Omega=0$ tam) ortamın **uzaysal sınırsızlığına** dayanır; teorinin monizmi bunu ima eder ama kozmolojik erimle (Büyük Patlama, $S_{kozmik}$) ilişkisi yazılmamıştır. Hubble-kesikli kolda sonuç $3{,}3\times10^{-14}$ s⁻¹'de kalır.
- Tüm sayılar $\Sigma$'nın alt sınırıyladır. **Duyarlılık ters yönlüdür:** büyük $\Sigma$ Ayak 1 ve 3'ü güçlendirir, Ayak 2'nin yapısal sınırını ($\propto v_m$) **gevşetir**.
- Ayak 1'in salınım genliği ilksel koşula bağlıdır ve teori onu türetmez; kısıt gözlemseldir ($\le0{,}02v_{yör}$).
- Kelvin–Voigt sönüm hesabı $\eta_E$'yi ortamın kesme viskozitesi olarak okur; bu özdeşleştirme kurulmamıştır (M-43'ün $\eta_E$'si artık kuplaj katsayısıdır).

### Açık Uçlar
- Ortamın uzaysal eriminin kozmolojik çatıyla eşlenmesi (Ayak 2'nin tam kolunun koşulu).
- Salınım genliğinin ilksel değerinin teori-içi türetimi (şu an yalnız gözlemsel üst sınır).
- Galaktik ölçekte hükmün açıkça yazılması: denkleşme süresi 3,3 yıl olduğundan galaktik ortam da diferansiyel dönemez — M-37'nin galaktik **ortam kolonunu** da dışlar (madde kolonu etkilenmez).

---

## M-54 · Mach Sonucu: Yerel Eylemsizlik Çerçevesinin Küresel Kilidi · **[T]**

**Kullanıldığı bölümler:** M-5 (kohezyon kanalı), M-51, M-53; 7.7 (modern fiziğin açık krizleri), 11.3/11.4.8.1 (tercihli çerçeve tartışması).

### Sorun
Klasik bulmaca: **yerel eylemsizlik çerçevesi neden uzak maddeye göre dönmez?** Newton'da bu bir tanımdır (mutlak uzay); genel görelilikte kozmolojik madde dağılımından gelen bir uyum sorunudur (Mach ilkesi; çerçeve sürüklenmesinin kozmolojik toplamı). Hiçbir çatıda mekanik bir taşıyıcısı yoktur.

### Varsayımlar
1. Ortam **tek sürekli** gövdedir (monizm; Postülat 1).
2. Kesme rijitliği vardır ve sinyal hızı $v_m=\sqrt{\Sigma/\rho_0}>10^4c_0$'dır (M-5).
3. Ortam dolaşmaz (M-51, M-52, M-53).

### Adımlar
1. Bir ortam yaması, komşularına göre dönmek isterse kesme zorlanması doğar; elastik geri-çağırma bunu $v_m$ hızıyla iletir (M-5).
2. Ölçek $L$ üzerinde dönüş durumunun denkleşme süresi $L/v_m$'dir.
3. Dolayısıyla her yerel yama, **küresel ortam durumuna elastik olarak kilitlidir**; ve küresel durum dönmeyendir (M-53).

### Sonuç
$$\boxed{\;\text{Yerel eylemsizlik çerçevesi, kesme rijitliği yoluyla küresel ortam durumuna kilitlidir}\;}$$
Yerel eylemsizlik çerçevesinin uzak maddeye göre dönmemesi, bu teoride bir postülat ya da kozmolojik uyum değil, **kohezyon kanalının bedava sonucudur.**

**Tercihli çerçevenin yeni okuması:** Teoride tercihli çerçeve **vardır** — ama küresel olarak **tek ve dönmeyendir**. 11.4.8.1'in *"tercihli çerçeve ortadan kalkmaz, yalnız doğrusal rejimde gözlenemez hâle gelir"* kaydı böylece dönme sektöründe tamamlanır: dönme sektöründe tercihli çerçeve yalnız gözlenemez değil, **küresel olarak biriciktir**.

### Sayısal Çapraz Kontroller
Kesme denkleşme süresi $L/v_m$:

| Ölçek | Denkleşme süresi |
|---|---|
| Güneş sistemi (100 AU) | **5,0 saniye** |
| Galaksi (10 kpc) | **3,3 yıl** |
| Gözlenebilir evren ($1{,}3\times10^{26}$ m) | **$1{,}37\times10^{6}$ yıl** |

Evren yaşının ($1{,}38\times10^{10}$ yıl) $10^{-4}$'ü ⇒ kilitlenme kozmolojik ölçekte **anlıktır**.

### Geçerlilik Sınırı
- Sonuç, dönme (kesme) sektörüne ilişkindir; **öteleme** sektöründe tercihli çerçeve zarf hiyerarşisiyle yerelleşir (Postülat 7; 11.4.8.1). İkisi karıştırılmamalıdır.
- $v_m$ alt sınırıyla hesaplanmıştır; büyük $\Sigma$ denkleşmeyi yalnız hızlandırır.
- Nicel bir Mach-tipi öngörü (ör. kozmolojik dönüşün yerel çerçeveye kalan sızıntısı) türetilmemiştir; sonuç şimdilik **mekanizma düzeyindedir**.

### Açık Uçlar
- Kalan sızıntının nicelenmesi: sonlu $v_m$ ile yerel çerçevenin küresel duruma kilitlenmesi tam değil, $\sim(L/v_m)$ gecikmelidir; bunun gözlemsel imzası (ör. yıllık/kozmolojik ölçekte çerçeve kayması) hesaplanmalıdır.
- CMB dipolüyle (öteleme sektörü) ve galaktik dönüşle (kesme sektörü) çapraz denetim.
- Standart fizikteki Mach tartışmasıyla (Brans–Dicke, Lense–Thirring toplamı) karşılaştırmalı bir kutu — Kısım 7.7'ye adaydır.

---

## Taşıma partisi için kontrol listesi

**Yeni girdiler:** M-51, M-52, M-53, M-54 (Blok B'nin devamı) · `07_Matematiksel_Ekler.md`'nin Blok B kapsam cümlesi genişletilir · Ek M girişindeki "M-1..M-50" sayımı güncellenir.

**Düzeltilecek mevcut satırlar:**
| Yer | İşlem |
|---|---|
| `10_Ek_M_Blok_B:116–118` (M-9 Geçerlilik Sınırı) | *"cevabı düşmek değil dolaşmaktır… siklostrofik dengede"* → M-51'in düzeltme kaydı; *"Madde düşer, ortam dolaşır"* → **"Madde düşer, ortam gerilir"** |
| `10_Ek_M_Blok_B:124` (M-9 Açık Uçlar) | *"siklostrofik denge profilinin nicel eşlenmesi"* → kalem yeniden tanımlanır: **kohezyon/dolaşım bölüşümü**; gözlem bölüşümü ~%100 kohezyona veriyor |
| `09_Ek_M_Blok_A` (M-4/M-5) | $\Sigma$'ya **ikinci yapısal görev** notu (M-51): Kepler yörüngelerinin varlık koşulu; Bell'den bağımsız gerekçe |
| `10_Ek_M_Blok_B` (M-7) | Yırtılmama koşulunun **katı dönüşü de yasakladığı** kaydı (M-53 Ayak 2) |
| `18_5:265–286` (M-37) | Profil teoreminin ortam kolonu → **kohezyonsuz üst sınır**; madde kolonunun etkilenmediği vurgulanır |
| `14_Ek_M_Blok_F:15` (M-22 Varsayım 2) | *"makro girdap kararlı ve eksenel simetriktir"* → **opsiyonel dinamik durum** etiketi |
| `18_5` (M-2) | **İz/izsiz çiftlenme notu**: cisim gerilme tensörünün izine bağlanır; izsiz kesme payı deplasman cebine kuvvet uygulamaz |
| `Kisim_11\04_Saturn:922` (11.4.8.1 kapsam kuralı) | *"yerel ortam"* → **cismin kendi zarfının dışındaki ambiyans ortam**, merkezî cismin çerçevesinde durgun (Hill hiyerarşisi: Güneş 1,225 pc; Dünya 234,9 R_⊕ — kitabın kendi 235 değeriyle birebir) |
| `18_5:376` | *"F5 **dolaşımı** gövdenin dönme düzlemine kilitler"* → dolaşımdan bağımsız yazım |
| `18_5:565` (M-39 R2) | *"M-22 (R2'de hız kaynağı)"* atfı yeniden gerekçelendirilir |
| `05_Oturma_Yaricapi:136–138`, `KARNE:765`, `11.4:782,786,811`, `98_Ne_Ogrendik:63` | **81 çarpanı** kalemleri koşullu yazılır (dolaşan-ortam senaryosu) veya geri çekilir; statik senaryonun öngörüsü **oran 1** eklenir |
| `Kisim_7\04` md.15 | Sınavın öngörüsü netleşir: statik ortam ⇒ **fark sıfır** |
| KARNE | Yeni sınav satırları: Merkür (Güneş ortamı) · Ay + LAGEOS-2 (Dünya) · Titan (Satürn) · Io (Jüpiter) — statü **Sınandı ✓** · Mach sonucu satırı |

**Dokunulmayacaklar (doğrulandı):** `18_5:313` (eş-düzlemlilik zaten F5'te, prograd tercih zaten açık kalem) · KARNE s.35 (*"eş-düzlemlilik için mekanizma borcu yoktur"*) · M-37'nin madde kolonu · galaktik zincir (a₀, W penceresi, 163 galaksi fiti) · Kısım 5 ve Kısım 10 (Λ ve ortam hız alanı geçmiyor).

---

# ✅ TAŞIMA KAYDI — 17 Ağustos 2026

**Yeni girdiler:** `Kisim_8_Ekler/10_Ek_M_Blok_B_Arka_Plan_Basinci.md` sonuna eklendi — **M-51** (satır 131), **M-52** (186), **M-53** (248), **M-54** (321). Dördü de tam şablonla.

**Uygulanan bağlı düzeltmeler (16 nokta, 10 dosya):**

| # | Dosya | Ne yapıldı |
|---|---|---|
| 1 | `10_Ek_M_Blok_B` M-9 Geçerlilik Sınırı | İki kollu yazım (kohezyonsuz Euler ↔ kohezyonlu statik); M-51/52/53 atıfları; **"ortam gerilir"** + düzeltme kaydı |
| 2 | `10_Ek_M_Blok_B` M-9 Açık Uçlar | Kalem yeniden tanımlandı: kohezyon/dolaşım **bölüşümü** |
| 3 | `10_Ek_M_Blok_B` M-7 Geçerlilik Sınırı | Yırtılmama koşulunun **katı dönüşü de yasakladığı** kaydı (M-53 Ayak 2) |
| 4 | `09_Ek_M_Blok_A` M-5 | **Σ'nın ikinci yapısal görevi** bölümü (Kepler yörüngelerinin varlık koşulu; Bell'den bağımsız gerekçe) + modül/dayanım açık ucu |
| 5 | `09_Ek_M_Blok_A` M-2 İşaret Konvansiyonu | **İz/izsiz çiftlenme kaydı** (deplase hacim skaler ⇒ ize bağlanır; izsiz τ kuvvet uygulamaz) |
| 6 | `14_Ek_M_Blok_F` M-22 Varsayım 2 | **Opsiyonel dinamik durum** statü kutusu |
| 7 | `18_5` M-37 sağ kolon | Statü düştü: "ölçülmemiş" → **"dolaylı olarak ölçülmüş ve dışlanmış"**; madde kolonunun etkilenmediği vurgulandı |
| 8 | `18_5:270` M-37 oran cümlesi | 2 katının kohezyonsuz kol olduğu kaydı |
| 9 | `18_5:376` F5 | *"dolaşımı kilitler"* → dolaşımdan bağımsız yazım |
| 10 | `18_5:249` sıfırıncı mertebe (zarf) | Ortam teğetsel alanı koşullu yazıldı |
| 11 | `18_5:904` DY bölümü "Ne söyler" | **"ortam gerilir"** |
| 12 | `Kisim_11/04_Saturn` 11.4.8.1 | **Kapsam kuralı (3) eklendi:** "yerel ortam" = zarf dışı ambiyans, merkezî cismin çerçevesinde durgun; Hill hiyerarşisi tablosu (Güneş 1,225 pc; Dünya 234,9 R⊕); Merkür ↔ GPS'in birlikte doğru çıkması |
| 13 | `Kisim_11/04_Saturn:786` | Tork işaretinin dolaşıma bağlı olduğu **senaryo kaydı** |
| 14 | `Kisim_11/05_Oturma_Yaricapi` | **81 çarpanı** iki senaryolu tabloya çevrildi (81 ↔ 1); prograd kolun değişmediği, Phoebe sınırının gevşediği kaydı |
| 15 | `Kisim_11/98_Ne_Ogrendik:25` | Triton sorusu iki senaryolu yazıldı |
| 16 | `Kisim_7/04` md.15 | Sınavın öngörüsü **karara bağlandı**: statik ⇒ fark sıfır |

**Slogan hizalaması (kitap-içi tutarlılık, 8 yayın dosyası):** *"madde düşer, ortam dolaşır"* → **"ortam gerilir"** / **"ortam düşmez"**, her birinde M-51/52 atfıyla: `Kisim_1/03_Evrenaki_Postulasi` (Postülat 1 metni) · `Kisim_3/08_Makro_Girdabin_Motoru` · `Kisim_7/04` · `Kisim_8_Ekler/14_Blok_F` (2 yer) · `16_Ek_A` (Ek A.4 başlığı + statü kutusu) · `17_Ek_B` · `18_5` (2 yer). Yayın metninde eski ifade **kalmadı**; tek kalan yer `Kisim_7/00_CALISMA_Acik_Konular.md` (çalışma dosyası, tarihsel yazar kararı kaydı — kasıtlı bırakıldı).

**Katalog/karne:** `07_Matematiksel_Ekler` — Blok B kapsam cümlesi genişletildi, "M-1..M-50" → **"M-1..M-54"** · `00_KARNE` — **S-12** (kilit teoremi, Sınandı ✓), **S-13** (Merkür = ortam dönüşü ölçümü, Sınandı ✓), **S-14** (Mach sonucu, mekanizma kuruldu) satırları eklendi; **S-7** yeniden okunmalı işaretlendi; 9 Ağustos DY-2 kutusuna güncelleme notu düşüldü.

**Numara durumu:** M-51…M-54 kullanıldı. **Üstel ölçek yapısı girdisi hâlâ numara bekliyor — sıradaki boş numara M-55.**
