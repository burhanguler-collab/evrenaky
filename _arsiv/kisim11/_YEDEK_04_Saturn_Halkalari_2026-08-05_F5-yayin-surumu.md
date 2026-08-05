# 11.4 Yanal İtim Alanının Matematiği: Satürn Halkaları, Düzlem Seçimi ve Dikey Salınım

> [!NOTE]
> **Bölümün konumu.** 11.2 F5'in **yapısını** ($\sin2\theta$) ve gövde figüründeki payını verdi; sonucu olumsuzdu — F5 figürde görünmez (11.2.7, Sınav 1). Bu bölüm aynı kuvvetin **gövde dışındaki** alanını kurar. Sonuç tersine döner: F5'in radyal yapısı, genliği ve **sönüm üssü** dışarıda ölçülebilir bir imza bırakır, ve bu imzayı taşıyan tek laboratuvar Satürn halkalarıdır. Bölümün dört kazancı: **(i)** F5 kuvvet yoğunluğunun radyal profili bir **Rankine tepesidir** ve maksimumu **deplasman yüzeyindedir** (11.4.2); **(ii)** $\phi$ artık çalışma değeri değil — gövdenin **iç yoğunluk profilinden türetilir** ve bu, deplasman yüzeyi $R_\phi$ kavramını doğurur (11.4.1-(4)); **(iii)** dış alanın sönüm üssü teoride serbest değildir — **Ay'ın düğüm gerilemesi** üç adaydan ikisini eler (11.4.3); **(iv)** kalan aday, halka dikey salınımına **çift olmayan radyal üsle** ($\propto(R_e/r)^3$) girer; bu üs hiçbir kütle çokkutbuyla üretilemez, dolayısıyla F5'in **taklit edilemez** imzasıdır (11.4.4).

---

## 11.4.0 Bölümün Soruları

Dört soru sorulur ve dördü de nicel cevaplanır:

| # | Soru | Cevabın yeri |
|---|---|---|
| **S1** | F5'in büyüklüğünü ne belirler? Dönüş hızı ve basıklık nasıl girer? | 11.4.1 |
| **S2** | Kütleden uzaklaşınca F5 nasıl değişir? Kutupta gerçekten sıfır mı? | 11.4.2–11.4.3 |
| **S3** | Halka yapısını ne kadarıyla korur? İnceliğin kaynağı F5 mi? | 11.4.4–11.4.5 |
| **S4** | Halkalar neden Satürn'de bu kadar belirgin, diğer gaz devlerinde değil? | 11.4.6 |

Ek olarak, aynı matematikten galaktik disklerin ve yörünge sistemlerinin **düzlüğü** çıkar (11.4.9) — ve orada F5 kesirli değil, **tek** düzlem seçicidir.

**Notasyon.** $\theta$ ekvatordan ölçülen enlem (M-39 konvansiyonu), $r$ küresel yarıçap, $R=r\cos\theta$ eksene dik uzaklık (S-14). Gövdenin ekvator yarıçapı $R_e$, kutup yarıçapı $R_p=R_e(1-f)$. Kuvvet $-\nabla P$, $dP/dr>0$ (R-4). $\rho_0=\rho_n/4$ ($k=0$, M-8), $\rho_n=2{,}7\times10^{17}$ kg/m³ (R-6). Teorinin kendi denklemlerinde $\mathcal{G}M$ yazılır (R-1/S-20).

---

## 11.4.1 F5'in Genlik Denklemi: Üç Çarpan ve İkisinin Zıt Yönde Çalışması · **[T]**

M-39'un sonucu, sabit $r$ üzerinde teğetsel kuvvet yoğunluğudur:

$$f_{yanal}(r,\theta) = -\frac{\kappa_5\,\phi\,\rho_0\,V(r)^{2}}{r}\,\sin 2\theta$$

Burada $V(r)$ *deplase eden akışın* o yarıçaptaki genliğidir ve $\phi$ deplasman hacim kesridir ($p=1$; M-39 Varsayım 4'ün iki-fazlı türetimi). Maddeye etki eden ivme $a=f/\rho_n$'dir (M-2), dolayısıyla $\rho_0/\rho_n=\tfrac14$ çarpanı her yerde görünür.

Genliği belirleyen üç çarpan vardır. **Yazarın iki tespiti burada sınanır ve biri sağlam, biri düzeltilerek doğrulanır.**

### (1) Merkezî makro kütlenin dönüş hızı — doğrudan ve güçlü ✓

Gövde rejiminde (R1) $V(R_e)=\omega R_e=v_e$'dir. Kuvvet $v_e^2$ ile gider, yani **dönüş hızının karesiyle**. Bu, aynı $\omega$'nın F4'ü de büyütmesiyle tutarlıdır (M-38): iki kuvvet de $\omega_1$ kökündendir (M-39 köken haritası), dolayısıyla **F4 ve F5 asla ayrı ayrı ayarlanamaz** — birini büyüten şey ötekini de büyütür. Yazarın tespiti birebir doğrudur.

Boyutsuzlaştırılmış hâli, gözlemle karşılaştırılabilir tek biçimdir. **Dönüş (deplasman) parametresi** tanımlanır:

$$\boxed{\;\mathcal{Q} \equiv \frac{\omega^2 R_e^{3}}{\mathcal{G}M} = \frac{v_e^2 R_e}{\mathcal{G}M} \;}$$

$\mathcal{Q}$, gövdenin dönme atalet ivmesinin yüzeydeki kütle-itim ivmesine oranıdır ve F5'in bütün gözlemsel yükünü taşır.

### (2) Basıklık — meridyen kısalması gradyanı gerçekten sertleştirir ✓ (ama zayıf)

Yazarın mekanizması şudur: *gradyan kutuptan ekvatora doğrudur; basıklık arttıkça kutup ile ekvator birbirine yaklaşır, aynı basınç farkı daha kısa bir yola sığar, gradyan sertleşir.* **Bu doğrudur ve şimdi türetiliyor.**

Basınç açığı $\Delta P=\kappa_5\phi\rho_0v_e^2$ enlemle *yol boyunca* dağılır. Küre üzerinde ekvatordan kutba meridyen çeyrek yayı $\tfrac{\pi}{2}R_e$'dir. Basık dönel elipsoidde ($R_p=R_e(1-f)$) aynı yay:

$$L_m = \int_0^{\pi/2}\!\!\sqrt{R_e^2\sin^2 t + R_p^2\cos^2 t}\;dt \;=\; R_e\,E(e),\qquad e^2 = 1-(1-f)^2 = 2f-f^2$$

$E$ ikinci tür tam eliptik integraldir. Gradyan sertleşme çarpanı, kürenin yayının gerçek yaya oranıdır:

$$\boxed{\;\mathcal{S}(f) \;\equiv\; \frac{\pi R_e/2}{L_m} \;=\; \frac{\pi/2}{E(e)} \;=\; 1+\frac{f}{2}+\frac{3f^2}{16}+\mathcal{O}(f^3)\;}$$

| Cisim | $f$ | $\mathcal{S}$ |
|---|---|---|
| Dünya | 0,00335 | **1,0017** |
| Neptün | 0,01708 | **1,0086** |
| Uranüs | 0,02293 | **1,0116** |
| Jüpiter | 0,06487 | **1,0332** |
| **Satürn** | **0,09796** | **1,0508** |

**Dürüst kayıt.** Mekanizma gerçektir ve Satürn'de en büyüktür — ama etkisi **%5**'tir. Yazarın sezgisi yön olarak doğru, mertebe olarak ikincil bir düzeltmedir. Basıklığın F5'e asıl katkısı bu değildir; aşağıdaki üçüncü kalemdir.

### (3) Basıklığın ikinci ve zıt yönlü kanalı — figür soğurması ⚠

Basıklık bağımsız bir girdi değildir: $f$ ile $\mathcal{Q}$ aynı fiziğin iki yüzüdür (hidrostatik figür, 11.2.6). Dolayısıyla *"basıklık arttıkça F5 artar"* ifadesi **mutlak büyüklükte doğrudur** — ama sebebi basıklığın kendisi değil, onu doğuran $\mathcal{Q}$'dur. Ve burada zıt yönlü bir kanal devreye girer:

> **Figür, dönüşü soğurur.** Gövde dönüşünün bir kısmı kütle dağılımına *fosilleşir* ve $J_2$ olarak dışarıya kütle çokkutbu şeklinde yansır. Bu pay artık ortamda değil, maddededir. Dolayısıyla **ortamda kalan** (yani F5'i besleyen) pay $\mathcal{Q}$ ile artar, $J_2/\mathcal{Q}$ ile azalır.

Bu, S4'ün (Satürn sorusunun) cevabının anahtarıdır ve 11.4.6'da kullanılacaktır. Şimdilik kaydedilecek nicelik:

$$\boxed{\;\frac{\mathcal{Q}}{J_2} \;=\; \text{gövde dönüşünün figüre soğurulmayan payının ölçüsü}\;}$$

### (4) $\phi$'nin kendisi: iç yoğunluk profilinden türetim ve **deplasman yüzeyi** · **[T + kalibre]**

> $\phi$ bir çalışma değeri değildir: gövdenin iç yoğunluk profilinden hesaplanır. Yöntem önce, bağımsızca bilinen iki değer üzerinde (sıvı su ve üst manto) kalibre edilir.

**Yöntem.** $\phi$ bir **hacim kesridir** (Blok D'nin bağlayıcı notasyon uyarısı) ve $\phi=1-1/n^2$ bunun yalnız saydam ortamlardaki *ters okumasıdır* (M-15). Doğrudan hesap iki girdi ister: bileşenin kafes hacmi ve fazın paketlenme yapısı.

$$\boxed{\;\phi(\rho) = \min\!\left(\frac{\rho}{\rho_*},\;\phi_{doy}\right),\qquad \frac{1}{\rho_*} = \sum_i \frac{X_i}{\rho_{*,i}},\qquad \rho_{*,i}=\frac{m_i}{v_i},\quad v_i=\frac{b_i}{4N_A}\;}$$

$b_i$ van der Waals dışlanan hacmidir ($b=4N_Av$, molekülün sert-küre hacminin dört katı); $\rho_*$ kafeslerin uzayı **tam** doldurduğu yoğunluktur. İki rejim vardır ve ayrımı fizikseldir:

- **Seyreltik dal ($\rho<\rho_{kafes}$):** kafesler temas etmez, $\phi=\rho/\rho_*$ — **yoğunlukla doğrusal.**
- **Doygun dal ($\rho\ge\rho_{kafes}$):** kafesler temas hâlindedir; daha fazla sıkıştırma kafesi de küçültür, dolayısıyla $\phi$ artık yoğunluğa değil **fazın paketlenme yapısına** kilitlenir. $\rho_{kafes}\equiv\phi_{doy}\rho_*$.

**Faz kuralı — $\phi_{doy}$ yoğunluktan değil, fazdan gelir.** Bu, bölümün yapısal kazancıdır:

| Faz | $\phi_{doy}$ | Gerekçe |
|---|---|---|
| **Kristal katı** | **0,68 ± 0,06** | bcc 0,680 · fcc/hcp 0,7405 · yapı seçer |
| **Yoğun akışkan** | **0,47 ± 0,03** | sert-küre **donma** sınırı $\eta_f=0{,}494$; denge akışkanı bunu aşamaz |
| Açık yapılı sıvı | 0,36–0,42 | H-bağı ağı (su) paketlenmeyi seyreltir |

**Kalibrasyon — yöntem kitabın bildiği iki değeri üretiyor mu?**

| Sınama | Bu yöntem | Bağımsız değer | Sapma |
|---|---|---|---|
| Sıvı su ($\rho=1000$) | $\rho_*=2363 \Rightarrow \phi=\mathbf{0{,}423}$ | optik ters okuma $0{,}437$; moleküler paketlenme $0{,}36$–$0{,}40$ | ikisinin **arasında**, $\pm$%10 |
| Üst manto forsterit ($\rho=3320$) | iyonik hacimlerle $\rho_*=4732 \Rightarrow \phi=\mathbf{0{,}70}$ | kitap $0{,}61$ ($n=1{,}6$); bcc Fe $0{,}68$ | **+%13** |

İki bağımsız sınamada $\pm$%13 içinde tutar — ve sapmanın **yönü** M-15'in kendi kaydıyla uyumludur (ters okuma su için ~%10 yüksek sarkıyordu; burada ters okuma manto için %13 *düşük* çıkıyor, yani iki yöntem farklı yönlerde sapıyor ve gerçek değer aralarındadır).

**Satürn'ün iç modeli.** H/He zarfı Mbar basınçlarında $P\simeq K\rho^2$'ye çok yakındır; bu $n=1$ politropudur ve analitik çözümü $\rho(r)=\rho_c\,\sin x/x$, $x=\pi r/R$, $\rho_c=\pi M/4R^3$'tür. Satürn ($M=5{,}683\times10^{26}$ kg, $R_{ort}=5{,}823\times10^{7}$ m): $\rho_c=2261$ kg/m³, $\langle\rho\rangle=687$ kg/m³. Bileşim, dış zarf için $X=0{,}86$, $Y=0{,}13$, $Z=0{,}01$:

$$\rho_*^{Satürn} = \left(\frac{0{,}86}{303}+\frac{0{,}13}{675}+\frac{0{,}01}{1968}\right)^{-1} = \mathbf{329\ kg/m^3} \qquad\Longrightarrow\qquad \rho_{kafes}=0{,}47\times329=\mathbf{155\ kg/m^3}$$

Profil bu yoğunluğu $r=0{,}935\,R_e$'de geçer. Ve kritik sonuç şudur:

| Nicelik | Satürn | Jüpiter | Uranüs | Neptün |
|---|---|---|---|---|
| $\rho_*$ (kg/m³) | 329 | 329 | 379 | 379 |
| $\rho_{kafes}$ (kg/m³) | 155 | 155 | 178 | 178 |
| **Deplasman yüzeyi $R_\phi/R_e$** | **0,935** | **0,966** | **0,959** | **0,968** |
| Doygun **olmayan** hacim | %18,1 | %9,9 | %11,8 | %9,3 |
| Doygun **olmayan** kütle | **%1,96** | **%0,57** | **%0,81** | **%0,50** |
| $\langle\phi\rangle_V$ (hacim ağırlıklı) | **0,426** | 0,446 | 0,442 | 0,448 |
| $\langle\phi\rangle_M$ (kütle ağırlıklı) | **0,467** | 0,469 | 0,469 | 0,469 |
| $\phi(R_\phi)$ (kaynak okuması) | **0,47** | 0,47 | 0,47 | 0,47 |

> [!IMPORTANT]
> **Ağırlıklandırma belirsizliği çöktü — ve bu hesabın asıl kazancı budur.** F5'in $\phi$'si bir *yüzey* mi *hacim* niceliği mi? Gaz devi için bu soru $10^{-4}$ ile $0{,}5$ arasında, **dört mertebelik** bir belirsizlik gibi görünüyordu: 1 bar seviyesinde $\rho\approx0{,}2$ kg/m³ ile $\phi\approx6\times10^{-4}$'tür.
>
> Hesap gösterdi ki soru **anlamsızdır**, çünkü Satürn kütlesinin **%98'inde deplasman doygundur.** Üç fiziksel okuma — hacim ortalaması ($0{,}426$), kütle ortalaması ($0{,}467$), kaynak yüzeyi ($0{,}47$) — **%10 bandında buluşur.** Dört mertebelik belirsizlik, %10'luk bir banda iner.
>
> $$\boxed{\;\phi_{Satürn} = 0{,}45 \pm 0{,}03\;}$$
>
> Çalışma değeri $0{,}5$ **%7 yüksekti** — yani türetim, kullanılan sayıyı doğruluyor.

**Deplasman yüzeyi $R_\phi$ — yeni ve gerekli bir kavram.** Ortam gövdede 1 bar seviyesinde durmaz; onu *taşıyan* şey bağlı kafestir ve kafes ancak temas ettiğinde ($\rho>\rho_{kafes}$) ortamı sürükler. Üstündeki seyreltik gaz, ortamı sürüklemek için fazla incedir; oradaki ortam pratik olarak dıştaki ortamla süreklidir. Dolayısıyla **F5'in dış alanının sınır koşulu $R_e$'de değil $R_\phi$'de kurulur.** Sonuçları:

1. **Rankine tepesi $R_\phi$'ye kayar** (11.4.2): Satürn'de $0{,}935\,R_e$, yani 1 bar seviyesinin ~3.900 km altına.
2. **Dış alan genliği $(R_\phi/R_e)^{2s+2}$ ile azalır.** $s=2$ (11.4.3) ile bu $(R_\phi/R_e)^6$'dır: Satürn $0{,}668$ · Jüpiter $0{,}813$ · Uranüs $0{,}778$ · Neptün $0{,}823$.
3. **Kavram karasal cisimlerde görünmezdir.** Dünya'nın yüzeyi katı silikattır ($\rho=2700\gg\rho_{kafes}^{silikat}=0{,}68\times4732=3218$… sınırda, kabuk altında hemen aşılır), dolayısıyla $R_\phi\simeq R_e$ ve çarpan 1'dir. **Kavramın kitapta şimdiye kadar gerekmemiş olmasının sebebi budur** — yalnız gaz/buz devlerinde devreye girer.

**Faz kuralının ikinci sonucu: Dünya ↔ Satürn oranı öngörülür.** Dünya katı ve kristaldir ($\phi_{doy}=0{,}68$), Satürn akışkandır ($\phi_{doy}=0{,}47$):

$$\frac{\phi_{Satürn}}{\phi_{Dünya}} = \frac{0{,}47}{0{,}68} = 0{,}69$$

Kitabın örtük olarak kullandığı oran $0{,}5/0{,}6=0{,}83$'tü — %20 içinde. **Ve şimdi bu bir seçim değil, faz kuralının sonucudur.** Dünya için türetilen değer $\phi_\oplus=\mathbf{0{,}68}$'dir (manto hacimce %84, $\phi=0{,}70$; Fe çekirdek %16, $\phi=0{,}68$) — kitabın $0{,}60$'ından %13 yüksek.

**Bant ve duyarlılık.**

| Varyant | $\langle\phi\rangle_V$ | $\langle\phi\rangle_M$ |
|---|---|---|
| $\phi_{doy}=0{,}44$ (düşük akışkan) | 0,401 | 0,437 |
| **$\phi_{doy}=0{,}47$ (ana)** | **0,426** | **0,467** |
| $\phi_{doy}=0{,}50$ (yüksek akışkan) | 0,450 | 0,496 |
| metalik H'de $\phi=0{,}64$ (RCP) | 0,495 | 0,593 |
| metalik H'de $\phi=1{,}00$ (elektron denizi) | 0,643 | 0,861 |

> **Dürüst kayıt — metalik hidrojen tek gerçek belirsizlik.** Satürn'ün iç zarfında H₂ ayrışıp basınçla iyonlaşır; orada "atom" yoktur, protonlar ve dejenere bir elektron denizi vardır. M-39 iki şey söyler ve ikisi bu noktada gerilir: *(i)* kavrama nükleon düzeyindedir ve iyonizasyonla çökmez; *(ii)* kafes nükleon değil **atomdur** — elektron kabuğu kütlesel olarak boş, Evrenakı açısından doludur. Metalik fazda elektronlar hâlâ oradadır (bağlı değil, ama var), dolayısıyla hacim yine deplase edilir; fakat *ne kadarı* türetilmemiştir. Tablo bandı bunu ölçer: metalik faz da akışkan gibi paketlenme-sınırlıysa $\langle\phi\rangle_M=0{,}467$; elektron denizi hacmi tümüyle doldurursa $0{,}861$. **Ana değer alt uçtur** — çünkü Blok D'nin geçerlilik sınırı ($\phi\to1$ fiziksel değil, geometrik paketlenme bağlar) ve M-39'un nötron maddesi kaydı ($\phi\approx0{,}7$–$0{,}9$, *asimptotik*) ikisi de üst ucu dışlar: hidrojen plazması nötron maddesinden **daha** dolu olamaz. Kalan iş, elektron yoğunluğu eşiğinin ilk-ilkelerden konulmasıdır → §7.4 kalem **11.4-iv′**.

> **İki ek dürüst kayıt.** *(a)* $n=1$ politropu Satürn'ün ağır element çekirdeğini hafife alır ($C/MR^2$ politropta $0{,}261$, gözlem $\approx0{,}21$); ama çekirdek $\rho\sim10^4$ kg/m³ ile $\rho_{kafes}$'in **60 katındadır**, yani zaten doygun daldadır ve $\langle\phi\rangle$'a $\phi_{doy}$ değerinden başka bir şey katmaz. Model duyarlılığı bu yüzden zayıftır. *(b)* $R_\phi$'de rijit dönüş varsayılmıştır; Satürn'ün ekvatoral zonal rüzgârı $+450$ m/s ile $\omega R_e$'nin %4,6'sıdır ve genliği $\pm$%9 oynatır — banda dahildir.

### (5) İyonize ve Metalik Fazlar · **[T + kalibre]**

> Bağlı kafes yokken deplase edilen hacmi ne belirler? İki uç düşünülebilir: $\phi=0{,}47$ (paketlenme-sınırlı, kafesler hâlâ tikelmiş gibi) ya da $\phi=1$ (elektron denizi hacmi doldurur). **Cevap üst uçtur, ve gerekçesi kalibre edilebilir.**

**Kriter: kafes sınırı bir elektron yoğunluğu eş-yüzeyidir.** (4)'ün $\rho_*$'ları van der Waals ve iyonik hacimlerden geldi; bu hacimlerin fiziksel tanımı standarttır — molekülün sınırı, elektron yoğunluğunun $n_e\simeq0{,}001$ a.u. değerine düştüğü eş-yüzeydir (Bader ve ark., 1987; bu eş-yüzey deneysel vdW hacimlerini birebir üretir). Atomik birimde $1$ a.u. $=a_0^{-3}=6{,}748\times10^{30}$ e/m³, dolayısıyla:

$$\boxed{\;n_e^{eşik} \simeq 0{,}001\ \mathrm{a.u.} = 6{,}75\times10^{27}\ \mathrm{e/m^3}\;}$$

Kafesin *içi* bu eşiğin üstünde, *arası* altındadır. Yalıtkan moleküler maddede ara bölge eksponansiyel kuyruklardan ibarettir ve eşiğin altına iner — bu yüzden $\phi<1$'dir ve Fizeau kısmi sürüklenme ölçer. **Soru şu hâle gelir: metalik fazda ara bölge eşiğin altına iniyor mu?**

**Hayır — iki mertebe farkla.** Delokalize elektron gazının yoğunluğu her yerde eşiğin çok üstündedir:

| Ortam | $\rho$ (kg/m³) | $n_e$ (a.u.) | $r_s/a_0$ | $T/T_F$ | **$n_e/n_e^{eşik}$** |
|---|---|---|---|---|---|
| **Metalik H** (Satürn iç zarfı) | 700 | 0,062 | 1,57 | 0,025 | **62×** |
| **Metalik H** | 1 000 | 0,089 | 1,39 | 0,027 | **89×** |
| **Metalik H** | 2 000 | 0,177 | 1,10 | 0,021 | **177×** |
| **Güneş plazması** ($0{,}5R_\odot$) | 1 300 | 0,098 | — | 10,6 (klasik) | **98×** |
| **Güneş plazması** ($0{,}1R_\odot$) | 90 000 | 5,42 | — | 2,4 | **5 422×** |
| **Dünya Fe çekirdeği** (itinerant, ~8 e⁻/atom) | 13 000 | 0,166 | — | — | **166×** |

Metalik hidrojen $r_s=1{,}1$–$1{,}6\,a_0$ ve $T/T_F\approx0{,}02$ ile **kuvvetli dejenere, zayıf korelasyonlu** — yani jellium'a yakın; yoğunluk modülasyonu birkaç on yüzdedir. **%50'lik bir çukur bile ara bölgeyi eşiğin 40 katı üstünde bırakır.** Güneş plazması dejenere değildir ama Debye uzunluğu parçacık aralığını aşar ($\lambda_D/r_s=2{,}0$–$2{,}2$), yani elektron gazı orada da delokalizedir.

$$\boxed{\;\phi_{metalik\ H} \;=\; 1 - \delta,\qquad \delta \lesssim 10^{-13}\;}$$

*(Kalan pay $\delta$ aşağıda hesaplanmıştır.)*

**Ve hidrojen bu ailenin uç üyesidir.** Her elementte elektronların bir kısmı **çekirdek (core) elektronu** olarak yerel kalır; yalnız hidrojende kalmaz — tek elektronu vardır ve metalik fazda o elektron iletim elektronudur. **Metalik hidrojen, elektronlarının %100'ü delokalize olan tek maddedir.** Dolayısıyla $\phi$'si paketlenme değerinden en çok sapan maddedir.

> [!IMPORTANT]
> **İyonizasyonun yönü, sezgiye aykırıdır.** Yaygın beklenti *"atom çözülünce kafes kalmaz ve $\phi$ çöker"* biçimindedir. M-39 bu beklentiyi üç gerekçeyle reddeder ama yerine bir sayı koymaz. Sayı şudur ve işaret tersidir:
>
> $$\phi_{\text{moleküler yalıtkan}}\;\approx0{,}42\text{–}0{,}47 \;\;<\;\; \phi_{\text{kristal katı}}\;\approx0{,}68\text{–}0{,}70 \;\;<\;\; \phi_{\text{metal / plazma}}\;\to1$$
>
> **İyonizasyon $\phi$'yi yok etmez, artırır.** Sebebi tek cümlede: bağlı moleküllerin *boş bıraktığı* ara hacim, delokalize elektron gazı tarafından **doldurulur.** Geçiş süreklidir — kısmen iyonize rejimde ara bölge yoğunluğu düzgün biçimde yükselir; eşikli bir atlama yoktur. M-39'un *"sürekli mi eşikli mi"* sorusunun cevabı: **sürekli.**

> **Kapsam düzeltmesi — Blok D'nin $\phi\to1$ yasağı tikel kafeslere aittir.** Blok D şöyle der: *"$\phi\to1$ limiti fiziksel **değildir**; moleküler paketlenmenin geometrik üst sınırları $\phi$'yi 1'in belirgin altında tutar"* — ve özdeş kürelerin $\pi/\sqrt{18}=0{,}7405$ sınırını gösterir. **Bu argümanın kapsamı tikel, geçilmez birimlerdir.** Delokalize bir elektron gazı bir küre kümesi değildir; paketlenme sınırı ona uygulanamaz. Aynı biçimde M-39'un nötron maddesi kaydı ($\phi\approx0{,}7$–$0{,}9$, asimptotik) da tikel nükleonlar hakkındadır ve geçerlidir. *(Bu, (4)'teki su-sistematiği kapsam düzeltmesinin ikizidir: iki genelleme de doğru oldukları rejimin dışına taşınmıştı.)*

> **Dürüst tuhaflık — kaydedilmeli.** Bu sonuç metalleri nötron maddesinden **daha** doygun yapar ($\to1$ ↔ $0{,}7$–$0{,}9$). Sezgiye aykırıdır ama tutarlıdır: deplasman kütleyle değil **yer** ile ölçeklenir (Fizeau'nun doğrudan ölçtüğü şey), ve bir elektron gazı tüm hacme yayılmış bir yapıdır; bir nötron yığınında ise geometrik boşluklar kalır. Teori burada yanlış olabilir — ve yanlışsa, aşağıdaki laboratuvar sınavı bunu gösterir.

> **Ayırt edici laboratuvar sınavı (yeni).** Kriter niceldir: ara bölge serbest-taşıyıcı yoğunluğu $n_c$ eşiği ($6{,}75\times10^{27}$ m⁻³) geçtiğinde $\phi$ paketlenme değerinden $1$'e doğru sıçramalıdır. Bu, **saydam bir iletkende Fizeau sürüklenme katsayısının $1-1/n^2$ değerini aşması** demektir. En iyi şeffaf iletken oksitler (ITO, ağır katkılı ZnO) $n_c\sim10^{27}$ m⁻³'e ulaşır — eşiğin **7 kat altında**, yani onlarda etki beklenmez ✓ (bu bir öngörü, sonradan uydurma değil). Eşiği aşan ve kızılötesinde saydam kalan bir dejenere yarıiletkende $f>1-1/n^2$ ölçülmelidir. **Yanlışlanma:** $n_c\gg10^{28}$ m⁻³'de bile $f=1-1/n^2$ çıkarsa, delokalizasyonun ara hacmi doldurduğu tezi düşer ve metalik $\phi$ paketlenme değerine geri iner.

#### Ve F5 bu belirsizlikten etkilenmez — bant çöküyor

Kalemin F5 üzerindeki asıl sonucu olumsuzlama değil, **karantinadır.** F5'in dış alanının sınır koşulu deplasman yüzeyinde kurulur (madde (4)) ve o yüzey **moleküler zarfın içindedir**:

| | Satürn'de yer | Basınç |
|---|---|---|
| **Deplasman yüzeyi $R_\phi$** | $0{,}935\,R_e$ | $\approx$ **0,035 Mbar** |
| Moleküler → metalik geçiş | $\approx0{,}55$–$0{,}65\,R_e$ | $\approx$ **1–2 Mbar** |

Aradaki basınç farkı **30–60 kattır.** $R_\phi$'de madde tartışmasız moleküler H₂/He akışkanıdır ve orada $\phi_{doy}=0{,}47$ sağlamdır. Metalik fazın $\phi$'si F5'in genliğine **hiç girmez.**

$$\boxed{\;\hat{\mathcal{Q}}_{et}^{Satürn} = 3{,}83\times10^{-4}\quad\text{— bant yok}\;}$$

Yani 11.4.4'ün Sınav 11.4-A öngörüsünde daha önce kaydedilen $2{,}6$–$7{,}0\times10^{-4}$ bandı **kapanmıştır**; bandın tek kaynağı metalik-faz belirsizliğiydi ve o belirsizlik yanlış yerde aranıyordu. Kalan belirsizlik yalnız $\phi_{doy}$'un akışkan değerindedir ($0{,}47\pm0{,}03$, $\pm$%6).

> **Aynı karantina Dünya için de geçerli — ve $\phi_\oplus$'yi %3 düzeltir.** Dünya'nın Fe çekirdeği bir metaldir, dolayısıyla $\phi_{çekirdek}\to1$'dir (tabloda 166×). Bu, gövde-ortalamalı $\phi$'yi $0{,}68$'den $0{,}75$'e çıkarır. **Ama F5 gövde ortalamasını kullanmaz**; kullandığı nicelik $R_\phi$'deki değerdir ve Dünya'da $R_\phi=R_e$'dir (yüzey katı silikat). Dolayısıyla doğru değer **yüzey silikatınınkidir:**
> $$\phi_\oplus = \mathbf{0{,}70}\qquad(\text{kristal silikat; bant }0{,}64\text{–}0{,}74)$$
> Madde (4)'te $0{,}68$ yazılmıştı (hacim ortalaması, çekirdek $0{,}68$ alınarak). Kaynak okuması tutarlı biçimde uygulandığında $0{,}70$ olur. **Etkisi küçüktür ve yön belirtilerek kaydedilir:** figür sınırı $\kappa_5\lesssim0{,}0114$–$0{,}0131$ (merkezî $0{,}0120$), Ay'ın düğüm öngörüsü $0{,}70\to\mathbf{0{,}72}$ mas/yıl. **LLR sınırı ve $\kappa_5\phi$ çarpımı değişmez** ($2{,}1\times10^{-3}$ ve $1{,}5\times10^{-3}$) — çarpım zaten gözlemin sabitlediği değişmez niceliktir.

#### Kalan payın hesabı · **[T]**

> Kalan pay, ihtiyatlı $\mathcal{O}(10^{-2})$ tahmininden on bir mertebe küçüktür.

İhtiyatlı okuma $\mathcal{O}(10^{-2})$ verirdi: elektron yoğunluğu ortalamada eşiğin çok üstünde olsa da, proton konumları arası **modülasyon** yerel çukurlar açabilir. Modülasyon lineer tepkiden hesaplanır. Her proton bir Thomas–Fermi ekranlama bulutu taşır ve bulutlar bindirilir:

$$\delta n_e(r) = \frac{1}{4\pi\lambda_{TF}^2\,r}\,e^{-r/\lambda_{TF}},\qquad \int\delta n_e\,d^3r = 1\ \text{(tam bir elektron)},\qquad n_e(\mathbf r)=\sum_i \delta n_e(|\mathbf r-\mathbf R_i|)$$

Bu kurgu ortalamayı birebir $n_i$ verir; modülasyonu $\lambda_{TF}/r_s$ oranı yönetir.

| $\rho$ (kg/m³) | $\lambda_{TF}/r_s$ | $k_{TF}/2k_F$ | **en düşük** $n_e$ / ortalama | en düşük $n_e$ / **eşik** | eşik altı hacim |
|---|---|---|---|---|---|
| 700 (metalik geçiş) | 0,511 | 0,51 | 0,658 (örgü) · **0,311 (sıvı)** | 40,6 · **13,8** | **0** |
| 1 000 | 0,542 | 0,48 | 0,688 · 0,345 | 60,7 · 21,8 | **0** |
| 2 000 | 0,609 | 0,43 | 0,741 · 0,412 | 130,7 · 52,0 | **0** |
| 5 000 | 0,709 | 0,37 | 0,801 | 353,2 | **0** |

*(Satürn'ün iç zarfı **sıvı** metaldir; sıvı satırı esas alınmalıdır — örgüden daha derin çukurlar açar. Örgü duyarlılığı zayıftır: bcc 0,688 · fcc 0,636 · sc 0,588, hepsinde eşik altı hacim sıfır.)*

**Modülasyon sığdır ve minimum eşiğin çok üstünde kalır: eşik altı hacim kesri özdeş olarak sıfırdır.** Ama "sıfır" bir Monte Carlo ifadesi olarak zayıftır; asıl sonuç analitiktir. **Eşik altı bir cebin doğması için ne gerekir?** Yarıçapı $R$ olan küresel bir boşluğun merkezinde:

$$n_e(0) = \bar n_e\,e^{-x}(1+x),\qquad x\equiv\frac{R}{\lambda_{TF}}$$

Eşik koşulu $e^{-x}(1+x)=n_e^{eşik}/\bar n_e$ çözülür ve boşluğun içerdiği proton sayısı $N_{boş}=(R/r_s)^3$ olarak okunur:

| $\rho$ (kg/m³) | $R_{boş}$ | $R_{boş}/r_s$ | **$N_{boş}$ (proton)** | $P\sim e^{-N}$ |
|---|---|---|---|---|
| **700** (en kırılgan) | 2,58 Å | 3,11 | **30** | $9\times10^{-14}$ |
| 1 000 | 2,60 Å | 3,52 | 44 | $10^{-19}$ |
| 2 000 | 2,59 Å | 4,44 | 88 | $10^{-38}$ |
| 5 000 | 2,54 Å | 5,90 | 206 | $10^{-90}$ |

$$\boxed{\;\phi_{metalik\ H} = 1-\delta,\qquad \delta \lesssim 10^{-13}\;}$$

**Yani eşik altı bir cep için 30 protonluk bir boşluk gerekir.** Yoğun bir sıvı metalde ısıl dalgalanmalar 30 parçacıklı bir kovuk üretmez; $e^{-N}$ Poisson kestirimi bile $10^{-13}$ verir ve gerçek korelasyonlu sıvı bunu mertebelerce daha bastırır. Pay **en fazla $10^{-13}$**'tür.

> **Yan gözlem — $R_{boş}$ neredeyse yoğunluktan bağımsız (2,54–2,60 Å).** Sıkıştırma $\lambda_{TF}$'yi küçültürken $x$'i tam telafi edecek kadar büyütür. Gereken boşluğun *proton sayısı* ise hızla artar ($30\to206$), çünkü $r_s$ küçülür. Yani **sıkıştırma $\phi=1$ sonucunu yalnız güçlendirir.**

**Güneş için aynı hesap:** klasik plazmada ekranlama Debye uzunluğudur ve sonuç daha da uçtur — eşik altı cep için $0{,}5R_\odot$'da **3 072**, $0{,}1R_\odot$'da **11 326** protonluk boşluk gerekir. $\phi_\odot=1$ ifadesi bu yüzden bir yaklaşım değil, kesindir.

> **Eşik duyarlılığı — dürüst kayıt.** Sonuç $n_e^{eşik}$'in değerine bağlıdır ve standart bant içinde sağlamdır: $0{,}0005$ a.u. $\Rightarrow N=44$ · **$0{,}001$ (standart, Bader) $\Rightarrow N=30$** · $0{,}002$ (bandın üstü) $\Rightarrow N=20$; üçünde de $P<10^{-8}$. **Sonucu zayıflatan tek senaryo eşiğin 5–10 kat şişmiş olmasıdır** ($0{,}005$ a.u. $\Rightarrow N=10$, $0{,}01$ a.u. $\Rightarrow N=5$, $P\sim10^{-2}$) — ve $0{,}001$ a.u. değeri deneysel vdW hacimlerinden kalibre olduğu için böyle bir şişme, (4)'ün bütün $\rho_*$ değerlerini de birlikte bozardı. İki sonuç aynı sabite bağlıdır; bu bir zayıflık değil, **tek noktadan sınanabilirlik**tir.

> **Modelin sınırları.** *(i)* Lineer tepki (TF) kullanıldı; $k_{TF}/2k_F=0{,}37$–$0{,}51$ ile TF sınırdadır. Friedel salınımları ihmal edildi — onlar ortalama etrafında **salınır**, derin kovuk açmaz. *(ii)* Ekranlama bulutlarının bindirilmesi sıvı-metal kuramının standart ilk yaklaşımıdır; değiş-tokuş-korelasyon düzeltmesi girmedi. *(iii)* Her iki eksik de en fazla on yüzdelik düzeltmedir, oysa sonucun marjı **13–130 kat**tır. Hiçbir makul düzeltme hükmü çevirmez.

**Bilanço.** $\phi$ zinciri kapalıdır: metalik/plazma değeri ($1-\delta$, $\delta\lesssim10^{-13}$), iyonizasyon geçişinin yönü ve sürekliliği, Blok D yasağının kapsamı, F5'in bu belirsizlikten karantinası ve kalan payın niceliği. Kalan tek iş gözlemseldir: Sınav 11.4-D (saydam iletkende Fizeau).

### Genlik denkleminin kapalı biçimi

Dördünü birleştirerek, deplasman yüzeyinde F5 ivmesinin merkezî kütle-itime oranı:

$$\boxed{\;\left|\frac{a_{yanal}}{a_r}\right|_{r=R_\phi} = \frac{\kappa_5\,\phi_{doy}\,\mathcal{S}}{4}\,\mathcal{Q}\,\sin2\theta\;,\qquad \text{dış alan ek çarpanı } \left(\frac{R_\phi}{R_e}\right)^{2s+2}\;}$$

**Denetim (11.2.5 ile).** 11.2.5'in korunan sonucu $a_{yanal}/a_{merkezkaç}=\kappa_5(\rho_0/\rho_n)\phi\cdot2\sin\theta$'dır. $a_{merkezkaç}=\omega^2R\cos\theta$ ve $a_r=\mathcal{G}M/R^2$ konularak iki ifade birebir örtüşür ($\mathcal{Q}=\omega^2R^3/\mathcal{G}M$ tanımıyla) ✓ Satürn için ($\kappa_5=0{,}015$, $\phi=0{,}47$, $\theta=45°$): oran $2{,}7\times10^{-4}$, yani $a_{yanal}=2{,}85\times10^{-3}$ m/s² — yüzey itiminin ($10{,}44$ m/s²) on binde üçü.

---

## 11.4.2 Radyal Yapı: F5 Bir Rankine Tepesidir · **[T]**

> **Yazarın sorusu:** *"Kütlenin kendi kutuplarında F5 çok azalıyor, hatta yok. Kütleden uzaklaştıkça kutup ve ekvator düzlemindeki gradyan yapısına bağlı olarak önce artar sonra azalır. Sen teyit et."*
>
> **Teyit edildi — ve maksimumun yeri tam olarak hesaplanabiliyor.** İki ifadenin ikisi de doğrudur, fakat farklı sebeplerden; ayrıştırılmaları gerekir.

### (a) Kutupta sıfır — bu geometrik ve *tamdır*

$\sin2\theta$, $\theta=90°$'de tam sıfırdır. Bu bir yaklaşım veya küçüklük ifadesi değil, **özdeşliktir**: dönme ekseni üzerinde deplasman akışının enlemsel gradyanı yoktur, çünkü $v(\theta)=V\cos\theta$ profili orada durağan noktasına ulaşır. Aynı sıfır ekvatorda da ($\theta=0$) vardır — ama nitelikleri zıttır (M-39 kararlılık analizi):

- **Ekvator:** $f_{yanal}$ sıfır, türev **geri çağırıcı** ⟹ **kararlı denge**
- **Kutup:** $f_{yanal}$ sıfır, türev **iteleyici** ⟹ **kararsız denge**
- **45°:** $|\sin2\theta|=1$ ⟹ **maksimum ezme**

Yazarın *"kutupta yok"* tespiti bu yüzden çift anlamlıdır ve ikisi de gereklidir: kuvvet orada sıfırdır **ve** madde orada barınamaz. Kutup, F5'in tek "temiz" noktasıdır (M-35 Varsayım 4 bu yüzden kutbu yalıtma noktası olarak kullanır).

### (b) Radyal profil — Rankine yapısı

Radyal davranış tümüyle $V(r)$'ye bağlıdır ve iki rejim vardır. Kritik nokta şudur: **gövdenin içinde ve dışında $V(r)$ zıt yönlü davranır.**

**İç kol — gövde maddesi (katı-cisim, $r\le R_\phi$).** Gövde katı cisim olarak döner; bu bir varsayım değil, katı cismin tanımıdır (M-39 Varsayım 2, R1):
$$V(r) = \omega r \quad\Longrightarrow\quad |f_{yanal}| = \kappa_5\phi_{doy}\rho_0\,\omega^2 r\,|\sin2\theta| \;\propto\; r$$
**Merkezden dışa doğru doğrusal olarak artar.** Merkezde tam sıfırdır ($V=0$).

**Dış kol — serbest alan ($r>R_\phi$).** Deplasman yüzeyinin dışında deplase edilen akış korunum yasasıyla seyrelir; $V(r)=\omega R_\phi(R_\phi/r)^{s}$ biçiminde yazılır ($s>0$, sönüm üssü):
$$|f_{yanal}| = \kappa_5\phi_{doy}\rho_0\,\frac{\omega^2R_\phi^2}{r}\left(\frac{R_\phi}{r}\right)^{2s}|\sin2\theta| \;\propto\; r^{-(2s+1)}$$
**Dışa doğru hızla azalır.**

$$\boxed{\;|f_{yanal}|\propto r \;\;(r<R_\phi) \qquad\qquad |f_{yanal}|\propto r^{-(2s+1)} \;\;(r>R_\phi) \qquad\Longrightarrow\qquad \text{maksimum } r=R_\phi \text{'de}\;}$$

**Sonuç.** F5 kuvvet yoğunluğu **deplasman yüzeyinde maksimumdur**; içeride $+1$ eğimle yükselir, dışarıda $-(2s+1)$ eğimle düşer. Yazarın "önce artar sonra azalır" tespiti doğrudur ve tepe noktası **serbest parametre içermez** — 11.4.1-(4)'te iç yoğunluk profilinden türetilir: karasal cisimlerde $R_\phi=R_e$ (ekvator yarıçapı), Satürn'de $0{,}935\,R_e$, Jüpiter'de $0{,}966\,R_e$.

### (c) Maksimumun geometrisi: bir tepe *noktası* değil, iki **halka sırtı**

$|f_{yanal}|$ hem $r$'de hem $\theta$'da maksimumlanır. İki koşul birlikte alındığında maksimum kümesi:

$$r=R_\phi,\qquad \theta=\pm45°$$

yani gövdenin çevresinde, kuzey ve güney orta enlemlerde **iki eş merkezli halka**. F5 alanının en şiddetli olduğu yer ne kutup, ne ekvator, ne merkez — **45° enlem çemberidir.** Satürn için bu sırttaki değer ($R_\phi=0{,}935R_e$, $\omega R_\phi=9\,230$ m/s, $\phi_{doy}=0{,}47$):

$$|f_{yanal}|_{max} = \kappa_5\phi_{doy}\rho_0\,\omega^2R_\phi = 7{,}19\times10^{14}\ \mathrm{N/m^3} \qquad(a_{yanal}=2{,}66\times10^{-3}\ \mathrm{m/s^2})$$

Bu, M-39'un 2. Açık Ucu olan **45° imzasının** geometrik adresidir: F5'in ölçülebilir doğrudan izi, gövdenin 45° enlem kuşağında beklenmelidir — atmosferik akış deseni veya manto gerilmesi olarak.

<div style="text-align:center; margin:22px 0;">
<svg width="100%" viewBox="0 0 700 330" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, -apple-system, Segoe UI, sans-serif">
  <rect x="0" y="0" width="700" height="330" rx="12" fill="#0d1117"/>
  <text x="350" y="28" fill="#c9d1d9" font-size="14" text-anchor="middle">F5 kuvvet yoğunluğunun radyal profili (θ = 45° boyunca)</text>
  <line x1="80" y1="250" x2="650" y2="250" stroke="#8b949e" stroke-width="1.5"/>
  <line x1="80" y1="250" x2="80" y2="58" stroke="#8b949e" stroke-width="1.5"/>
  <text x="68" y="64" fill="#8b949e" font-size="11" text-anchor="end">|f₅|</text>
  <text x="68" y="254" fill="#8b949e" font-size="11" text-anchor="end">0</text>
  <!-- rising branch: r linear 0..Re at x=80..250 -->
  <polyline fill="none" stroke="#7ee787" stroke-width="3" points="80,250 250,70"/>
  <!-- falling branch r^-5 from Re -->
  <polyline fill="none" stroke="#7ee787" stroke-width="3"
    points="250,70 265,90 282,113 302,138 325,160 352,181 385,199 425,214 470,227 520,235 575,242 640,246"/>
  <circle cx="250" cy="70" r="6" fill="#7ee787"/>
  <line x1="250" y1="250" x2="250" y2="70" stroke="#58a6ff" stroke-width="1.2" stroke-dasharray="4,4" opacity="0.7"/>
  <text x="250" y="268" fill="#58a6ff" font-size="12" text-anchor="middle">r = R_φ</text>
  <text x="258" y="60" fill="#7ee787" font-size="12">maksimum</text>
  <text x="150" y="150" fill="#7ee787" font-size="12" transform="rotate(-46 150 150)">∝ r  (katı cisim)</text>
  <text x="400" y="185" fill="#7ee787" font-size="12">∝ r⁻⁽²ˢ⁺¹⁾  (serbest alan)</text>
  <!-- ring zone -->
  <rect x="278" y="58" width="90" height="192" fill="#ffa657" fill-opacity="0.12"/>
  <text x="323" y="290" fill="#ffa657" font-size="11" text-anchor="middle">halka kuşağı</text>
  <text x="323" y="304" fill="#ffa657" font-size="11" text-anchor="middle">1,11 – 2,27 Rₑ</text>
  <text x="80" y="268" fill="#8b949e" font-size="12" text-anchor="middle">0</text>
  <text x="360" y="322" fill="#6e7681" font-size="11" text-anchor="middle">Kuvvet gövde merkezinde ve her iki kutupta sıfır; deplasman yüzeyinde tepe yapar.</text>
</svg>
</div>

*Şekil 11.4.1: F5'in radyal profili bir Rankine yapısıdır. İç kolda kaynağın katı-cisim dönüşü ($V=\omega r$), dış kolda korunumlu seyrelme ($V\propto r^{-s}$). Tepe, deplasman yüzeyi $R_\phi$'de — serbest parametresiz, iç yoğunluk profilinden türetilir (11.4.1-(4)). Satürn için $R_\phi=0{,}935\,R_e$; karasal cisimlerde $R_\phi=R_e$.*

> **Bu M-30'un Rankine profilinin F5 karşılığıdır.** M-30 vorteks *hızı* için aynı yapıyı verir (iç çekirdek $v\propto R$, dış kol $v\propto1/R$). Yeni olan, aynı yapının **enlemsel kuvvet yoğunluğuna** taşınmasıdır: F5, kaynağın Rankine profilini karesiyle ve bir ek $1/r$ metrik çarpanıyla miras alır.

---

## 11.4.3 Sönüm Üssünü Gözlem Seçer: Ay'ın Düğümü · **[T (yapı) / gözlemle sabitlenmiş ($s$)]**

11.4.2 profilin **biçimini** verdi ama $s$'i vermedi. Genliğin bütünü buna bağlıdır ve teoride üç aday vardır — 11.2.5'in üç adayının dış-alan karşılıkları:

| Aday | $V(r)$ | Fiziksel gerekçe | $|f_{yanal}|$ | $\mathcal{F}_5\equiv\Omega_5^2/\Omega^2$ |
|---|---|---|---|---|
| **(B)** Ortamın kendi dolaşımı (R2) | $v_\theta=2\sqrt{\mathcal{G}M/r}$ | M-22 / DY-2 | $\propto r^{-2}$ | $2\kappa_5$ — **$r$'den bağımsız** |
| **(A1)** Serbest vorteks, $s=1$ | $v_e(R_e/r)$ | açısal momentum korunumu | $\propto r^{-3}$ | $\propto (R_e/r)^1$ |
| **(A2)** Dipolar alan, $s=2$ | $v_e(R_e/r)^2$ | M-40'ın dış alan geometrisi ($\Omega_{ortam}\propto r^{-3}$) | $\propto r^{-5}$ | $\propto (R_e/r)^3$ |

Genel biçim ($s\ge1$ için; kaynak yüzeyi 11.4.1-(4)'ün deplasman yüzeyi $R_\phi$'dir):

$$\boxed{\;\mathcal{F}_5(r)\;\equiv\;\frac{\Omega_5^2}{\Omega_{yör}^2}\;=\;\underbrace{\frac{\kappa_5\,\phi_{doy}\,\mathcal{S}}{2}\;\mathcal{Q}\left(\frac{R_\phi}{R_e}\right)^{2s+2}}_{\textstyle \hat{\mathcal{Q}}_{et}}\left(\frac{R_e}{r}\right)^{2s-1}\;}$$

*Türetim:* ekvator çevresinde $\sin2\theta\simeq2z/r$ ile $a_z=-\Omega_5^2z$, $\Omega_5^2=2\kappa_5\phi(\rho_0/\rho_n)V(r)^2/r^2$ ve $V(r)=\omega R_\phi(R_\phi/r)^s$; $\Omega_{yör}^2=\mathcal{G}M/r^3$ ile bölünüp $\mathcal{Q}$ tanımı konulur. $\rho_0/\rho_n=\tfrac14$ çarpanı $2/4=1/2$ olarak görünür. Karasal cisimlerde $R_\phi=R_e$ olduğundan çarpan 1'dir.

### Sınav: Ay'ın düğüm gerilemesi (LLR)

F5, gövdenin dönme düzlemine doğru **dikey geri çağırıcı** bir kuvvettir; eğik bir yörüngede bu, düğüm boylamında (nodal) ek bir gerileme üretir:

$$\dot\Omega_{düğüm}\big|_{F5} \simeq -\tfrac12\,\mathcal{F}_5(r)\,n$$

Ay için $r=60{,}27\,R_\oplus$, $n=4813°$/yıl, $\mathcal{Q}_\oplus=3{,}461\times10^{-3}$, $\mathcal{S}=1{,}0017$, $R_\phi=R_e$, $\phi_\oplus=0{,}70$ (11.4.1-(4)–(5)'ten türetildi — yüzey kristal silikatı), $\kappa_5=0{,}015$ (çalışma değeri):

| Aday | $\mathcal{F}_5$(Ay) | Öngörülen ek düğüm gerilemesi | Kıyas | Hüküm |
|---|---|---|---|---|
| **(B)** R2 | $3{,}0\times10^{-2}$ | **72,2 °/yıl** | gözlenen **toplam** gerileme 19,34 °/yıl | ✗ **MUTLAK DIŞLANDI** (bütçenin 3,7 katı) |
| **(A1)** $s=1$ | $2{,}93\times10^{-7}$ | **2,54 yay-saniyesi/yıl** | Dünya $J_2$'sinin payı 7,75 ″/yıl | ✗ **DIŞLANDI** ($J_2$ payının %33'ü; LLR mas mertebesinde modellenmiş) |
| **(A2)** $s=2$ | $8{,}32\times10^{-11}$ | **0,72 mas/yıl** | $J_2$ payının $9{,}3\times10^{-5}$'i | ✓ **AYAKTA — eşiğin tam üstünde** |

$$\boxed{\;s=2\;:\quad V(r)=\omega R_\phi\left(\frac{R_\phi}{r}\right)^{2},\qquad |f_{yanal}|\propto r^{-5},\qquad \mathcal{F}_5\propto\left(\frac{R_e}{r}\right)^{3}\;}$$

> **Bu, M-38'in Ay sınavının ikizidir — ve simetrisi kayda değer.** M-38'de Ay'ın **apsidal** presesyonu F4'ün $1/R$ rejimini yalıtılmış gezegenlerde iptal etmiş ve *disk koşulunu* zorunlu kılmıştı. Burada Ay'ın **düğüm** gerilemesi F5'in dış alan sönüm üssünü sabitliyor. **F4 apsisle, F5 düğümle kısıtlanır** — ikisi de aynı gövde tarafından, ikisi de aynı veri kümesiyle (LLR). Bu tesadüf değildir: F4 yörünge düzlemi *içinde*, F5 düzleme *dik* çalışır; Ay yörüngesinin iki bağımsız açısal elementi bu yüzden iki kuvvetin doğal ölçüm kanallarıdır.

**Ve seçilen üs teorinin kendi geometrisidir.** $s=2$, ortamın açısal hızının $\Omega_{ortam}\propto r^{-3}$ ile düşmesi demektir — bu **tam olarak M-40'ın dipolar çerçeve-sürüklenme alanıdır** (GP-B kanalı). Yani F5'in dış alanı, M-40'ın alanıyla aynı radyal biçimi paylaşır; ikisi bağımsız kanallar olmakla birlikte ($\phi$ ↔ $\xi$, M-39'un kanal kaydı) aynı dış geometriye oturur. Sönüm üssü artık **[T]** statüsündedir, seçim gözlemseldir.

> **Bağımsız destek — Laplace yarıçapları.** $s=1$ olsaydı F5, $J_2$'nin çokkutbundan **daha yavaş** ($r^{-4}$ ↔ $r^{-5}$) düşerdi ve dış bölgede $J_2$'yi geçerdi. Sonucu hesaplanabilir: bütün Laplace yarıçapları büyürdü — Dünya $8{,}41\to8{,}54$ ($+1{,}6\%$), Jüpiter $28{,}3\to30{,}6$ ($+8{,}2\%$), Satürn $36{,}3\to41{,}8$ ($+15{,}4\%$), Uranüs $46{,}1\to54{,}0$ ($+17{,}1\%$), Neptün $63{,}8\to76{,}4$ ($+19{,}9\%$) $R_e$. Düzenli/düzensiz uydu sınırı bu yarıçaplarla belirlenir ve gözlenen sınırlar $J_2$-tabanlı değerlerle uyumludur; %8–20'lik kaymalar için yer yoktur. $s=2$'de F5 $r^{-6}$ ile düşer ve Laplace yüzeyinde **hiçbir** iz bırakmaz (Satürn'ün $r_L$'sinde F5/güneş-gelgiti $=7\times10^{-4}$) ✓ İki bağımsız gözlem — Ay'ın düğümü ve uydu sınırları — aynı üssü seçer.

**$\kappa_5$ üzerine yeni sınır.** Ay'ın düğüm artığı $0{,}1$ mas/yıl düzeyinde sınırlanırsa:

$$\boxed{\;\kappa_5 \lesssim 2{,}1\times10^{-3}\;}\qquad\text{(LLR düğümü, } s=2,\ \phi_\oplus=0{,}70)$$

Bu, Sınav 1'in figür sınırından ($0{,}014$–$0{,}017$) **7 kat sıkıdır** ve kitaptaki en güçlü $\kappa_5$ kısıtıdır. $1$ mas/yıl toleransla sınır $0{,}021$'e gevşer — yani F5'in çalışma değeri **tam LLR eşiğinde oturuyor**. Aşağıdaki bütün sayılar $\kappa_5=0{,}015$ ile verilmiştir; sınır sıkışırsa doğrusal olarak ölçeklenirler.

> **Gözlemin sabitlediği nicelik $\kappa_5$ değil, $\kappa_5\phi$ çarpımıdır.** 11.4.1-(4) $\phi$'yi bağımsızca türettiği için bölüşme artık yapılabilir; ama sınırın kendisi çarpım üzerinedir: $\kappa_5\phi \lesssim 1{,}5\times10^{-3}$. $\phi$'nin metalik-faz belirsizliği (11.4.1-(4)'ün bandı) doğrudan buraya taşınır — üst uçtaki ($\phi\to0{,}86$) bir metalik hidrojen okuması Satürn tarafındaki bütün genlikleri 1,8 kat büyütür, Dünya tarafını (dolayısıyla sınırı) değiştirmez.

---

## 11.4.4 Halka Dikey Salınımı ve F5'in Taklit Edilemez İmzası · **[T]**

### Dikey salınım denklemi

Ekvatoral kararlı denge çevresinde ($z\ll r$) $\sin2\theta\simeq2z/r$ konulur. Toplam dikey geri çağırma, Kepler'in kendi payı + $J_2$ çokkutbu + F5'tir:

$$\ddot z = -\nu^2 z,\qquad \boxed{\;\frac{\nu^2}{\Omega^2} = 1 \;+\; \underbrace{3J_2\!\left(\frac{R_e}{r}\right)^{\!2}}_{\text{figür (madde kanalı)}} \;+\; \underbrace{\hat{\mathcal{Q}}_{et}\!\left(\frac{R_e}{r}\right)^{\!3}}_{\text{F5 (ortam kanalı)}} \;+\;\cdots\;}$$

$$\hat{\mathcal{Q}}_{et}\;=\;\frac{\kappa_5\,\phi_{doy}\,\mathcal{S}}{2}\,\mathcal{Q}\left(\frac{R_\phi}{R_e}\right)^{\!6}\;=\;3{,}83\times10^{-4}\quad(\text{Satürn})$$

$\nu$ dikey (bending) frekansı, $\Omega$ yörünge frekansıdır. **Halka tanecikleri bu frekansta yukarı-aşağı harmonik salınım yapar** ve kararlı düzlem $z=0$'dır.

### İmza: radyal üs **tek** sayıdır — ve bu imkânsızdır

Kuzey-güney simetrik bir gövdenin kütle çokkutbu alanında $\nu^2/\Omega^2$ açılımı **yalnız çift** $(R_e/r)^{2n}$ üsleri içerir: $J_2\to(R_e/r)^2$, $J_4\to(R_e/r)^4$, $J_6\to(R_e/r)^6$. Tek üsler yasaktır — çünkü tek dereceli zonal harmonikler ($J_3$, $J_5$) ekvatora göre asimetri gerektirir ve dönel simetrik hidrostatik gövdede sıfırdır.

$$\boxed{\;\text{F5, } \nu^2/\Omega^2\text{'ye } (R_e/r)^{3}\text{ ile girer — TEK bir üsle.}\;}$$

> [!IMPORTANT]
> **Bu, F5'in kitapta bulunmuş ilk taklit edilemez imzasıdır.** Sınav 1 (6.6.2) F5'in figürde saf $P_2$ olduğunu ve merkezkaçla **dejenere** olduğunu göstermişti — ölçülemez. Dış alanda dejenerasyon **kırılır**: F5'in radyal üssü hiçbir kütle çokkutbunun üretemeyeceği bir paritededir. Bir kuvvetin *çürütülmesi* ile *gözlemsel içeriğinin olmaması* farklı şeylerdir (M-39'un kaydı); burada üçüncü bir durum doğar: **F5 ölçülebilir hâle gelir.**

Halka sismolojisi (kronosismoloji) $\nu(r)$'yi Satürn halkalarındaki bükülme dalgalarından (bending waves) ve düğüm rezonanslarından okur; $J_2$, $J_4$, $J_6$ bu yolla bağımsızca çıkarılır ve Cassini Grand Finale çekim verisiyle karşılaştırılır. Yalnız çift üslerle yapılan bir uyumlama, F5 varsa **sistematik ve radyal olarak yapılandırılmış** bir artık bırakmak zorundadır.

### Nicel öngörü: Satürn halka kuşağı

$\kappa_5=0{,}015$, $\phi_{doy}=0{,}47$, $\mathcal{S}=1{,}0508$, $\mathcal{Q}_S=0{,}1548$, $(R_\phi/R_e)^6=0{,}668$ ile:

| Bölge | $r/R_e$ | $\mathcal{F}_5$ | $\delta\nu/\nu$ | $J_2$ terimi | **F5 payı** |
|---|---|---|---|---|---|
| D halkası (iç) | 1,110 | $2{,}80\times10^{-4}$ | $1{,}40\times10^{-4}$ | $3{,}97\times10^{-2}$ | **%0,71** |
| C halkası (iç) | 1,239 | $2{,}01\times10^{-4}$ | $1{,}01\times10^{-4}$ | $3{,}18\times10^{-2}$ | **%0,63** |
| B halkası (iç) | 1,527 | $1{,}08\times10^{-4}$ | $5{,}38\times10^{-5}$ | $2{,}10\times10^{-2}$ | **%0,51** |
| B/A orta | 1,750 | $7{,}15\times10^{-5}$ | $3{,}57\times10^{-5}$ | $1{,}60\times10^{-2}$ | **%0,45** |
| A halkası (dış) | 2,269 | $3{,}28\times10^{-5}$ | $1{,}64\times10^{-5}$ | $9{,}49\times10^{-3}$ | **%0,35** |
| F halkası | 2,326 | $3{,}05\times10^{-5}$ | $1{,}52\times10^{-5}$ | $9{,}03\times10^{-3}$ | **%0,34** |

**İki okuma:**

1. **F5, halka kuşağı boyunca $J_2$ kanalının %0,34–0,71'idir.** Küçük ama sıfır değil, ve *radyal olarak yapılandırılmış*: pay $(R_e/r)$ ile **içe doğru artar** — D halkasında A halkasının iki katı. En güçlü sinyal en iç halkalarda beklenir.
2. **Mutlak büyüklük $\delta\nu/\nu = 1{,}5\times10^{-5}$–$1{,}4\times10^{-4}$**'tür. Bükülme dalgası rezonans konumları Satürn halkalarında km mertebesinde ölçülür ($\delta r/r\sim10^{-5}$); iç halkalardaki $10^{-4}$'lük frekans kayması bu hassasiyetin **on katı üstündedir**. Yani sınav yürütülebilir durumdadır — ve ya F5 görülür, ya $\kappa_5$ bir mertebe daha aşağı iner. *(Dış halkalarda sinyal hassasiyetle aynı mertebeye iniyor; sınav bu yüzden C ve D halkalarına ağırlık vermelidir.)*

### Sınav protokolü (yürütülmeyi bekliyor)

> **Sınav 11.4-A · Halka bükülme dalgalarında tek-parite artığı.**
> **Yöntem:** Satürn'ün ölçülü bükülme-dalgası ve düğüm-rezonans yarıçapları, (i) yalnız çift üsler ($J_2,J_4,J_6,J_8$) ve (ii) çift üsler + tek bir $(R_e/r)^3$ terimi ile uyumlanır. İkinci uyumlamanın $\chi^2$ kazancı ve $(R_e/r)^3$ katsayısının işareti okunur.
> **Öngörü:** Katsayı **pozitif** olmalıdır (F5 dikey geri çağırmayı *artırır*, düzlemi sıkılaştırır) ve değeri $\hat{\mathcal{Q}}_{et} = \mathbf{3{,}8\times10^{-4}}$ (çalışma değeri; bant yok — metalik-faz belirsizliği 11.4.1-(5)'te karantinaya alındı) civarında çıkmalıdır.
> **Yanlışlanma:** Negatif katsayı veya $\lesssim10^{-5}$ üst sınır. İkinci durumda $\kappa_5\lesssim4\times10^{-4}$ olur ve F5 gözlemsel olarak tamamen susar.
> **Neden sadece Satürn:** Bükülme dalgalarını çözecek optik derinlikte ve genişlikte halka yalnız Satürn'de vardır (11.4.6).

---

## 11.4.5 Halkaların İnceliği Nereden Gelir · **[T]**

> [!IMPORTANT]
> **Halkaların inceliği F5'ten gelmez.** $\kappa_5$ üzerine konulan sınırlar (figür $\lesssim0{,}0114$–$0{,}0131$, LLR düğümü $\lesssim2{,}1\times10^{-3}$) F5'in dikey ezmesini Kepler'in kendi dikey geri çağırmasının $10^{-4}$'ü mertebesine indirir. Aşağıdaki hesap bunun sonuçlarını açar ve inceliğin gerçek kaynağını gösterir.

Hesap açıkça yapılır. Halka kalınlığı denge ilişkisi $h\simeq\sigma_z/\nu$'dur ($\sigma_z$ dikey hız dağılımı, çarpışmalı sönümle ~mm/s mertebesinde tutulur):

| Geri çağırma kaynağı | $\nu$ ($r=1{,}75R_e$) | Öngörülen $h$ ($\sigma_z=1{,}7$ mm/s) |
|---|---|---|
| **Kepler tek başına** ($\nu=\Omega$) | $1{,}798\times10^{-4}$ s⁻¹ | **9,45 m** ✓ gözlenen ~10 m |
| **F5 tek başına** | $1{,}52\times10^{-6}$ s⁻¹ | **1 118 m** ✗ 118 kat kalın |

**F5'in gerçek payı hesaplanabilir ve kaydedilmelidir:** $h\to h(1+\mathcal{F}_5)^{-1/2}$ ile F5, Satürn halkasını **0,2 mm (A halkası) – 0,7 mm (D halkası)** inceltir (10 metrede). Sıfır değildir; ölçülemez de değildir — ama halka kalınlığı üzerinden değil, **frekans** üzerinden (11.4.4).

### Neden hiçbir kuvvet halkayı inceltemez — teorinin kendi potansiyelinden

> [!IMPORTANT]
> **Kalınlığı belirleyen kuvvet değil, enerjidir** — ve bu, yukarıda türetilen $\Psi_5$'in doğrudan sonucudur.
>
> $$h \simeq \frac{\sigma_z}{\nu}\qquad\Longrightarrow\qquad \underbrace{\nu}_{\text{kuvvetlerin işi}}\ \text{ile}\ \underbrace{\sigma_z}_{\text{enerji bütçesinin işi}}\ \text{ayrı hanelerdir.}$$
>
> F5'in bir **potansiyeli** vardır — 11.4.5'te teorinin kendi denklemlerinden çıkarıldı: $\Psi_5=(\kappa_5\phi/4)V^2\sin^2\theta$. Potansiyeli olan kuvvet **korunumludur**, ve korunumlu bir geri çağırma alanında düzlem dışına salınan bir tanecik **sonsuza kadar aynı genlikle salınır** — asla oturmaz. Kuvveti on kat büyütmek $\nu$'yü $\sqrt{10}$ kat büyütür, genliği ($\sigma_z/\nu$) yalnız $\sqrt{10}$ kat küçültür; yüz kat, bin kat büyütmek de aynı yavaş kökle gider. Genliği **sıfıra** götüren tek şey enerji kaybıdır.
>
> Bu, F5'e özgü bir zayıflık **değildir**: aynı şey Kepler'in dikey geri çağırması ve $J_2$ için de geçerlidir. **Üçü de korunumludur, üçü de tek başına inceltemez.** Halka 10 metre değil 10 kilometre kalınlığında olsaydı, F5 yine tam aynı $\nu$'yü verirdi.
>
> **Doğru iş bölümü:** kuvvetler **hangi düzlem** ve **hangi frekans** sorularını cevaplar; **ne kadar ince** sorusunu enerji bütçesi cevaplar. Teori birinci soruda söz sahibidir (F5 → düzlem kimliği, $(R_e/r)^3$ imzası); ikinci soruda hakem enerjidir.

### Çarpışmalar neden inceltir: yön değil, **enerji**

> Sık karşılaşılan bir itiraz şudur: *"halka çarpışmaları rastgeledir ve her yönedir; incelmenin sebebi olamaz."* İtiraz yönle enerjiyi bir tutar; ayrıldıklarında cevap çıkar.
>
> Çarpışma iki şey yapar ve ikisi bağımsızdır: **(i)** hız *yönünü* rastgeleleştirir, **(ii)** hız *büyüklüğünü* küçültür — çünkü buz taneciklerinin çarpışması **esnek değildir** (geri tepme katsayısı $\varepsilon<1$; buz için $\varepsilon\approx0{,}1$–$0{,}6$). Yalnız (i) olsaydı itiraz haklıydı: yön karıştırmak inceltmez. İnceltme (ii)'dendir ve tek yönlüdür — **enerji her çarpışmada azalır, hiç artmaz.**
>
> Peki neden *yörünge* hareketi de sönmüyor? Çünkü o **rastgele değil**: komşu dairesel yörüngelerdeki iki tanecik birbirine göre neredeyse durgundur ($\Delta v\sim\Omega\times$ ayrılık $\sim$ mm/s), oysa eğik bir tanecik düzlemi her geçişte $\sigma_z$ ile keser. Çarpışmalar bu yüzden **seçicidir**: ortak dolanımı (açısal momentumu) korurken rastgele bileşeni boşaltır.
>
> **Sonuç bir korunum yasasıdır, tesadüf değil:** açısal momentum $L$ sabitken enerji minimumu, $L$'ye dik **düz bir diskтir**. Sistem enerjisini kaybettikçe o duruma akmak *zorundadır*. "Rastgelelikten düzen" değil, **korunum yasası altında gevşeme.**
>
> Ve sayı da bunu söyler: $\sigma_z$ dışarıdan alınan bir girdi değildir. Karıştırma (Kepler kayması + özçekim) ile esnek olmayan çarpışmaların dengesi $\sigma_z\sim\Omega\,a_t$ verir ($a_t$ tanecik yarıçapı), yani $h\sim$ **birkaç tanecik çapı**. Satürn halkalarında en iri taneciklerin boyu metre mertebesindedir; $h\approx10$ m bundan çıkar. Kalınlık ölçüsü tanecik boyunu ölçer.

> **Zincirin yönü önemlidir.** $\sigma_z$ gözlenen $h$'dan geri çözülürse açıklama döngüsel olur. Döngüsel olmayan zincir yukarıdadır: **tanecik boyu → $\sigma_z$ → $h$.** Ve "çarpışmalar" cevabı eksiktir: teorinin **kendi** sönüm kanalı da vardır (ortam sönümü $\gamma_{ortam}$, 11.4.8). Aşağıdaki bölüm onu hesaba katar ve nerede çalıştığını öngörür.

### Teorinin kendi sönüm kanalı nerede çalışır: $10^{28}$'lik iş bölümü · **[T]**

Evrenakı'nın standart fizikte karşılığı olmayan bir sönüm kanalı vardır: ortamın artık kuplajı $\gamma_{ortam}$ (M-27/M-37). Öyleyse doğru soru şudur: **bu kanal halkanın kalınlığına mı, yoksa yarıçapına mı iş yapar?** Cevap teorinin kendi iki yasasından, serbest parametresiz çıkar.

M-43 artık kuplajı hıza dördüncü kuvvetle bağlar ($\eta_E^{etkin}\propto a_b v^4/v_{kav}^3$). Aynı tanecik için iki ayrı bağıl hız vardır:

| Kanal | Ortamın o yöndeki hızı | Bağıl hız $\Delta v$ |
|---|---|---|
| **Dikey** | ortam ekvator düzleminde dolaşır, dikey bileşeni $\approx0$ | $\Delta v=\sigma_z\approx1{,}7\times10^{-3}$ m/s |
| **Yörünge** | **DY-2:** ortam maddenin iki katı hızla dolaşır | $\Delta v=v_{madde}=1{,}90\times10^{4}$ m/s |

Oran $1{,}12\times10^{7}$'dir ve $v^4$ ile:

$$\boxed{\;\frac{\gamma_{ortam}^{yörünge}}{\gamma_{ortam}^{dikey}} = \left(\frac{v_{madde}}{\sigma_z}\right)^{4} = 1{,}5\times10^{28}\;}$$

**Tanecik yarıçapı $a_b$ sadeleştiği için bu oran parametresizdir** — Phoebe kalibrasyonuna, tanecik boyuna, $v_{kav}$'a bağlı değildir. Sonucu tektir:

| Kanal | Ortamın kuplajı | Yönü | Rolü |
|---|---|---|---|
| **Dikey** (kalınlık) | pratik olarak sıfır — çarpışmalar $\sim10^{31}$ kat önde | — | **hiç** |
| **Yörünge** (yarıçap) | maksimum | **dışa** (DY-2: ortam maddeyi önden geçer) | yalnız **sınırlanır** |

> **Teorinin kendi kanalı vardır ve yeri kalınlık değil, yarıçaptır — ama halka yağmuru da değildir.** İşaret denetimi 11.4.8'dedir: ortam her yarıçapta maddeyi önden geçtiği için (DY-2) tork **daima dışa**dır, halka yağmuru ise içedir. Eş-dönüş kolu M-40'ın $\xi$'siyle dışlanmıştır. Dolayısıyla ortam kanalının rolü **sınırlanmaktır** — ve o rol verimsiz değildir: kitaptaki en sıkı $\eta_E$ kısıtını verir ($\lesssim2{,}3\times10^{-11}$ Pa·s, Phoebe'den $1{,}4\times10^{6}$ kat sıkı).
>
> $10^{28}$'lik iş bölümü bu yüzden hâlâ önemlidir: ortamın **niçin** kalınlığa dokunamadığını söyler. M-43'ün $v^4$ bastırması ile DY-2'nin kayma yasası birlikte, ortamın dikey harekete pratik olarak hiç iş yapmadığını **türetir** — varsaymaz. İki mekanizma yarışmaz; alanları $10^{28}$ çarpanıyla ayrılmıştır.

> **Neden kalınlık değil frekans.** $h$ ölçümü $\sigma_z$'yi bilmeyi gerektirir ve $\sigma_z$ çarpışma fiziğinden gelir — %50 belirsizdir. $\nu$ ise rezonans yarıçaplarından **doğrudan** ve $10^{-5}$ hassasiyetle okunur, $\sigma_z$'den bağımsızdır. F5 aranırken bakılacak yer kalınlık değil, **rezonans konumudur.** Bu, bölümün yöntemsel kazancıdır.

### F5'in gerçek işlevi: kuyu değil, **düzlem**

O hâlde F5 halkalarda ne yapıyor? Cevap, kuyunun *derinliğinde* değil **varlığındadır**:

> [!IMPORTANT]
> **Küresel kütle-itim (F1) düzlem tercih etmez.** Nokta kütle çevresinde eğik bir yörünge, ekvatoral bir yörünge kadar kararlıdır — hiçbir geri çağırma yoktur, hiçbir düzlem ayrıcalıklı değildir. Düzlem *seçimi* tümüyle $\omega_1$ kökenli kuvvetlerin işidir. Ve bunun **iki kanalı** vardır:
>
> | Kanal | Taşıyıcı | Radyal üs | Satürn halkasındaki pay |
> |---|---|---|---|
> | **Dolaylı** — figür ($J_2$) | **madde** (fosilleşmiş dönüş) | $(R_e/r)^2$ | %99 |
> | **Doğrudan** — F5 | **ortam** (canlı deplasman alanı) | $(R_e/r)^3$ | %1 |
>
> İkisi **aynı fiziktir**: $J_2$, gövdenin dönüşünün kütle dağılımına çökelmiş kalıntısıdır (11.2.6); F5 ise aynı dönüşün ortamda hâlâ canlı olan kalanıdır. Standart fizikte birincisi vardır, ikincisi yoktur. Evrenakı ikisini tek kökten türetir ve **oranını öngörür** ($\mathcal{P}_5$, 11.4.6).

Bu okumayla F5'in kuvvet kuyusu da anlamlanır. Potansiyeli integralle alınır:

$$\Psi_5(r,\theta) = \frac{\kappa_5\phi}{4}\,V(r)^2\sin^2\theta \qquad\Longrightarrow\qquad \Delta\Psi_5 = \frac{\kappa_5\phi}{4}V(r)^2 \;\;(\text{ekvator}\to\text{kutup})$$

$J_2$'nin aksine F5'in kuyusu **sonlu derinliktedir** — kuvvet 45°'de tepe yapıp kutupta sıfırlandığı için. Satürn'de $r=1{,}75R_e$'de ($V=2\,635$ m/s): $\Delta\Psi_5=1{,}22\times10^4$ J/kg, yani düzlemden kaçış hızı **156 m/s** ($J_2$'nin kuyusu: 2 396 m/s). Halka taneciklerinin gerçek dikey hızı $1{,}7$ mm/s'dir — **F5 kuyusunun içinde $10^{-5}$ derinlikte gömülüdürler.** Kuyu sığdır ama halka onun dibinde durur; F5 halkayı ezmiyor, **hangi düzlemin dip olduğunu söylüyor.**

---

## 11.4.6 Neden Satürn? Beş Gezegenin Nicel Karşılaştırması · **[T + gözlem]**

Soru S4: *halkalar neden Satürn'de belirgin, diğer gaz devlerinde değil?* Cevap iki ayrı büyüklükte aranır: Satürn **mutlak ezmede** birincidir, **payda** ise Uranüs ve Neptün'le başa baştır — ve ölçülebilirlikte tek adaydır.

**Ölçüt 1 — mutlak ezme, $\hat{\mathcal{Q}}_{et}\equiv\dfrac{\kappa_5\phi_{doy}\mathcal{S}\mathcal{Q}}{2}\left(\dfrac{R_\phi}{R_e}\right)^{6}$.** F5'in Kepler geri çağırmasına oranının genliği; "F5 hiç önemli mi?" sorusunun cevabı.

**Ölçüt 2 — pay, $\mathcal{P}_5\equiv\mathcal{F}_5/[3J_2(R_e/r)^2] = \mathcal{K}(R_e/r)$, $\mathcal{K}=\hat{\mathcal{Q}}_{et}/3J_2$.** F5'in düzlem-kilitleme bütçesindeki payı; "F5 ölçülebilir mi?" sorusunun cevabı.

| Cisim | $v_e$ (m/s) | $\mathcal{Q}$ | $\mathcal{S}$ | $\phi_{doy}$ | $(R_\phi/R_e)^6$ | $J_2$ | $\mathcal{Q}/J_2$ | $\hat{\mathcal{Q}}_{et}$ | $\mathcal{F}_5(1{,}6R_e)$ | $\mathcal{P}_5(1{,}6R_e)$ |
|---|---|---|---|---|---|---|---|---|---|---|
| **Satürn** | 9 871 | **0,1548** | **1,0508** | 0,47 | 0,668 | 0,016291 | **9,50** ① | **$3{,}83\times10^{-4}$** ① | **$9{,}35\times10^{-5}$** ① | **%0,490** ② |
| Jüpiter | 12 572 | 0,0892 | 1,0332 | 0,47 | 0,813 | 0,014697 | 6,07 ④ | $2{,}64\times10^{-4}$ ② | $6{,}44\times10^{-5}$ ② | %0,374 ④ |
| Uranüs | 2 588 | 0,0295 | 1,0116 | 0,47 | 0,778 | 0,003343 | 8,83 ② | $8{,}19\times10^{-5}$ ③ | $2{,}00\times10^{-5}$ ③ | **%0,511** ① |
| Neptün | 2 683 | 0,0261 | 1,0086 | 0,47 | 0,823 | 0,003411 | 7,64 ③ | $7{,}63\times10^{-5}$ ④ | $1{,}86\times10^{-5}$ ④ | %0,466 ③ |
| Dünya | 465 | 0,00346 | 1,0017 | **0,70** | 1,000 | 0,001083 | 3,20 ⑤ | $1{,}82\times10^{-5}$ ⑤ | $4{,}45\times10^{-6}$ ⑤ | %0,350 ⑤ |

*(① = sıralamada birinci. $\phi_{doy}$ ve $R_\phi$ **11.4.1-(4)'te iç yoğunluk profilinden türetildi** — artık çalışma değeri değil; $\kappa_5=0{,}015$. Satürn dönüş periyodu 10s39d22s alınmıştır — 11.2'nin tablosuyla uyum için; Cassini kronosismolojisinin 10s33d38s değeri $\mathcal{Q}$'yu %2 büyütür.)*

> **$\phi$ türetildikten sonra tabloda ne değişti.** Eski tablo $\phi=0{,}5$ ve kaynağı $R_e$ almıştı. İki düzeltme birlikte genlikleri şu çarpanlarla küçültür: Satürn $0{,}63$ · Uranüs $0{,}73$ · Jüpiter $0{,}76$ · Neptün $0{,}77$; Dünya ise $\phi_\oplus$ $0{,}60\to0{,}70$ olduğu için $1{,}17$ ile **büyür**. **Mutlak ezme ($\hat{\mathcal{Q}}_{et}$) sıralaması değişmez** — Satürn birinci kalır. Ama **pay ($\mathcal{P}_5$) sıralamasının başı Uranüs'e geçer** (%0,511 ↔ Satürn %0,490): Satürn'ün deplasman yüzeyi daha derinde ($0{,}935\,R_e$) olduğu için $(R_\phi/R_e)^6$ cezası en büyüktür. **Bu bir kayıp değil, ilk gerçek ayırt edici öngörüdür** — aşağıya bakınız.

### Üç ayrı ifade, tek sonuç

**(i) Mutlak ezme sıralaması, halka sahibi gezegenleri seçer.** $\hat{\mathcal{Q}}$: Satürn $>$ Jüpiter $>$ Uranüs $>$ Neptün $\gg$ Dünya. Halka sistemi olan **dört gezegen listenin ilk dördüdür**; Dünya beşinciye 6 kat aşağıda düşer ve Mars, Venüs ($\mathcal{Q}\sim10^{-5}$–$10^{-8}$) tabloya girmez bile. Bu, F5'in halka için **gerekli koşulu** kurduğunun kaydıdır.

**(ii) Pay sıralaması: Satürn ile Uranüs başa baş — ve bunun sebebi $\phi$ türetiminden çıktı.** $\mathcal{P}_5$ iki zıt çarpanın ürünüdür:

$$\mathcal{P}_5 \;\propto\; \underbrace{\frac{\mathcal{Q}}{J_2}}_{\text{dönüşün figüre soğurulmayan payı}}\;\times\;\underbrace{\left(\frac{R_\phi}{R_e}\right)^{6}}_{\text{deplasman yüzeyinin derinlik cezası}}$$

Birinci çarpanda Satürn açık birincidir:

> **Satürn, dönüşünü kendi figürüne en az soğuran gezegendir.** $J_2/\mathcal{Q}$ hidrostatik figür tepki fonksiyonudur ve merkezî yoğunlaşmayla azalır: Dünya 0,313 · Jüpiter 0,165 · Neptün 0,131 · Uranüs 0,113 · **Satürn 0,105**. Satürn en yoğunlaşmış devdir (en düşük ortalama yoğunluk, en kalın H/He zarfı), dolayısıyla dönüş sinyalinin en büyük kesri **maddede değil ortamda** kalır.

İkinci çarpanda ise Satürn **son**dur: en düşük ortalama yoğunluğa sahip olduğu için deplasman doygunluğuna en derinde ulaşır ($R_\phi=0{,}935\,R_e$; Neptün'de $0{,}968$) ve $(R_\phi/R_e)^6$ cezası en büyüktür ($0{,}668$ ↔ $0{,}823$). İki çarpan neredeyse tam olarak birbirini götürür:

| | Satürn | Uranüs | Neptün | Jüpiter | Dünya |
|---|---|---|---|---|---|
| $\mathcal{P}_5(1{,}6R_e)$ | %0,490 | **%0,511** | %0,466 | %0,374 | %0,340 |

> **Dürüst kayıt — bu sıralama sağlam değildir.** Satürn ile Uranüs arasındaki fark **%4**'tür ve $\phi$'nin metalik/iyonik faz belirsizliği (11.4.1-(4)'ün bandı, $\pm$%40) bunun on katıdır. Doğru ifade: **Satürn, Uranüs ve Neptün pay bakımından başa baştır; Jüpiter ve Dünya belirgin biçimde altta.** Eski sürüm "pay sıralamasının birincisi de Satürn" diyordu; $\phi$ türetimi bu ifadeyi geçersiz kıldı ve düzeltilmiştir.
>
> **Ve bu bir kayıp değil — kitabın ilk gerçek *ayırt edici* F5 öngörüsüdür.** İki çarpanın birbirini götürmesi tesadüf değil: yoğunluk hem $\mathcal{Q}/J_2$'yi yükseltir hem $R_\phi$'yi derinleştirir. Sonuç, F5'in payının **gezegenden gezegene neredeyse sabit** (%0,34–0,51) olmasıdır. Standart fizikte $J_2$ payı böyle bir evrensellik göstermez. Yani F5 varsa, dört devin bükülme dalgalarında **birbirine yakın** bir $(R_e/r)^3$ katsayısı çıkmalıdır; farklı çıkarsa $\phi$'nin faz kuralı yanlıştır.

**(iii) Ve yalnız Satürn'de okunabilir.** F5'in imzası (11.4.4) bükülme dalgası rezonans konumlarından okunur; bu, optik olarak kalın, radyal olarak geniş ve dalga taşıyan bir disk gerektirir. Jüpiter'in ana halkası ($\tau\sim10^{-6}$, toz), Uranüs'ün dar halkaları ve Neptün'ün yaylar hâlindeki halkaları bu ölçümü kaldırmaz. Ölçülebilirlik farkı $\hat{\mathcal{Q}}$'nun 1,8 katı değil, **$10^3$–$10^5$ katıdır** ve F5'ten değil, halkanın kendi optik derinliğinden gelir.

### Dürüst sınır — F5 halkaların *parlaklığını* açıklamaz

> [!WARNING]
> **Bu bölüm S4'ün yarısını cevaplar, yarısını cevaplamaz — ve ayrım net yazılmalıdır.**
>
> **Cevaplanan:** *Neden halka sahibi gezegenler bunlar ve neden Satürn dinamik olarak en elverişli olanı.* F5 sıralaması ($\hat{\mathcal{Q}}$, $\mathcal{P}_5$, $\mathcal{Q}/J_2$ — üçünde de Satürn birinci) bunu verir.
>
> **Cevaplanmayan:** *Satürn halkalarının optik derinliğinin diğer üçünden $10^3$–$10^5$ kat büyük olması.* Bu bir **düzlem-kilitleme** sorusu değil, **madde tedariki** sorusudur: buzul bir kaynak gövdenin Roche kuşağı içinde parçalanması, buz çizgisine göre konum, ve halka-yağmuru ömrü (11.4.8). F5'in $1{,}8$ katlık üstünlüğü $10^4$'lük bir farkı açıklayamaz ve açıklamaya kalkışmak teorinin kendi $\kappa_5$ sınırını ihlal eder.
>
> **Bu bir eksiklik değil, kapsam kaydıdır.** Teori düzlem seçimini üstlenir; kütle bütçesini üstlenmez. Nicel hâle getirilmesi gereken kalem (Roche kuşağı ↔ buz çizgisi ↔ ömür üçlüsü) **§7.4'e hesap kalemi olarak yazılmıştır** (kalem 11.4-i).

---

## 11.4.7 Halka Bandının Genişliği: F5 Yakın Alan Kuvvetidir · **[T]**

Yazarın sorusu — *"bu halka yapısının genişliğini belirleyen unsur olabilir"* — şimdi nicel olarak yanıtlanabilir. Cevap iki parçalıdır ve biri olumlu, biri olumsuzdur.

**Olumsuz kısım: bandın *kenarlarını* F5 koymuyor.** Halkaların iç kenarı (D halkası, $1{,}11R_e$) atmosfer/manyetosfer sürüklemesiyle, dış kenarı (A halkası, $2{,}27R_e$) **Roche sınırıyla** belirlenir — Roche ötesinde madde yığışıp uydu olur. Buz tanecikleri için ($\rho_s=920$ kg/m³, $\rho_S=687$ kg/m³):
$$r_{Roche} = 2{,}456\left(\frac{\rho_S}{\rho_s}\right)^{1/3}R_e = 2{,}23\,R_e$$
Gözlenen A halkası dış kenarı $2{,}269R_e$ ✓ **%2 içinde.** F5 bu sayıya girmez.

**Olumlu kısım: bandın *tamamının* F5 yakın alanında olması bir öngörüdür.** $s=2$ ile F5 $r^{-5}$ ile düşer; $\mathcal{F}_5$ ekvator yarıçapından itibaren $(R_e/r)^3$ ile seyrelir:

$$\frac{\mathcal{F}_5(r)}{\mathcal{F}_5(R_e)} = \left(\frac{R_e}{r}\right)^{3}$$

| $r/R_e$ | 1,11 | 1,53 | 2,27 | 5 | 10 | 60 |
|---|---|---|---|---|---|---|
| $\mathcal{F}_5/\mathcal{F}_5(R_e)$ | 0,73 | 0,28 | 0,086 | 0,008 | $10^{-3}$ | $5\times10^{-6}$ |

$$\boxed{\;\text{F5, } r\lesssim2{,}5R_e\text{'de ekvator yarıçapındaki değerinin }\gtrsim\%8\text{'ini korur; } r\gtrsim10R_e\text{'de biner mertebe içinde susar.}\;}$$

Ve bu, gözlenen **iki keskin mimari sınırla** üst üste düşer:

1. **Halka + düzenli uydu kuşağı** ($r\lesssim20$–$25R_e$): ekvatoral, prograd, dairesel — F5 yakın alanının içi.
2. **Düzensiz uydu kuşağı** ($r\gtrsim100R_e$; Phoebe $215R_e$): eğik, retrograd, basık — F5'in tamamen sustuğu bölge.

Yani F5'in radyal menzili, Güneş Sistemi'nin *düzenli/düzensiz uydu dikotomisiyle* aynı ölçekte biter. Bu **bir sınav değil, mertebe uyumudur** (Laplace yarıçapı da aynı bölgeye düşer ve $J_2$ ile açıklanabilir); ama iki mekanizmanın ayrıştırılabileceği yer bellidir: **F5 dönme düzlemine, güneş gelgiti yörünge düzlemine kilitler.** Satürn'ün 26,73° eğikliği bu ikisini ayırır ve ara bölgede (İapetus, $59R_e$) fark ölçülebilir — fakat $s=2$ ile F5'in oradaki payı $7\times10^{-4}$ olduğundan **öngörü sıfırdır.** Bu, $s=2$ seçiminin bir başka olumlu sonucudur: teori İapetus'un Laplace düzlemine dokunmaz ve dolayısıyla Ward (1981) çözümünü bozmaz.

---

## 11.4.8 Ortam Sönümü: Torkun İşareti ve $\eta_E$ Sınırı

Halka tanecikleri mutlak vakumda dönmez; sürüklenen Evrenakı akışkanı içinde hareket ederler (Postülat 7). Stokes biçimli artık kuplaj katsayısı:

$$\gamma_{ortam} = \frac{6\pi\eta_E r_t}{m} = \frac{9\eta_E}{2\rho_c r_t^2},\qquad \eta_E^{etkin}\propto \frac{r_t\,\Delta v^4}{v_{kav}^3}\ \ (\text{M-43})$$

M-37'nin $\gamma_{sür}$ ifadesiyle birebir aynı kuplaj — biri halka taneciğinde, biri gezegen uydusunda.

### Torkun işareti: dışa

Ortamın Satürn çevresindeki teğetsel alanı tek bir şeydir — kendi siklostrofik dolaşımı (M-22/DY-2), her yarıçapta prograd ve maddeden hızlı:

$$v_{ortam}=2v_{Kepler} \;\Longrightarrow\; \Delta v = +v_{Kepler}\ \ (\text{her yarıçapta}) \;\Longrightarrow\; \boxed{\;\text{tork } \textbf{DIŞA}\;}$$

Artık kuplaj cismi ortamla eş-dönüşe gevşetmeye çalışır (M-37); ortam önden geçtiğine göre kuvvet prograddır ve açısal momentumu **artırır**.

> **Halka yağmuru bu kanalın işi değildir.** Halka yağmuru **içe**dir, ortamın torku **dışa**. Teorinin bu olguda ayrışan bir sözü yoktur; içe akış standart mekanizmalara aittir (plazma sürüklemesi, mikrometeorit bombardımanı, viskoz yayılma, elektromanyetik güdüm). Kısım 6'nın kanıt matrisinde de kalem bu gerekçeyle taşınmaz.

**Eş-dönüş kolu neden yok.** "Zarf içinde ortam gövdeyle eş-döner" okuması bir **dönme** sürüklenmesi iddiasıdır ve onu $\xi$ yönetir, $\phi$ değil: $\xi_\oplus=4{,}6\times10^{-10}$ (M-40, GP-B ile sınandı). M-39 bu kolu adıyla eler — *"ortam gövdeyle eş-dönseydi presesyon ölçülenin $10^{10}$ katı çıkardı."* $\phi$ öteleme, $\xi$ dönme kanalıdır; ikisi birbirinin yerine konulamaz.

### Standart mekanizmalardan ayrışma

| Mekanizma | Yönü | $r_{syn}=1{,}862R_e$'de dönüm? | Profili ne belirler |
|---|---|---|---|
| **Ortam artık kuplajı** | **daima dışa** | **yok** | $\Delta v^4=(\mathcal{G}M/r)^2$ — saf kinematik |
| Plazma sürüklemesi | plazma eş-döner | **var** (içeride içe, dışarıda dışa) | manyetosfer modeli $n_p(r)$ |
| Mikrometeorit / balistik | net içe | yok | akı ve püskürtme verimi |
| Viskoz yayılma | net içe | yok | optik derinlik, $\sigma$ gradyanı |

Üçü de tanecik boyuyla $\propto1/r_t$ ölçeklenir; **ayrışma boyuttan değil, yönden ve profilden gelir.** Ve ortam kanalı gözlenen içe akışla zıt yönlü olduğu için standart bütçenin içine girip pay bölüşmek gerekmez: koşul tek yönlü ve çerçeveden bağımsızdır — *ortamın dışa sürüklemesi halkayı dağıtmamış olmalıdır.*

### Kitaptaki en sıkı $\eta_E$ sınırı

Halka genişliği $\sim7\times10^{7}$ m, ömrü $\sim10^{7}$ yıl; $\dot a=2\gamma a$ ile:

$$\dot a < 2{,}2\times10^{-7}\ \mathrm{m/s} \;\Longrightarrow\; \gamma_{ortam}<1{,}0\times10^{-15}\ \mathrm{s^{-1}} \;\Longrightarrow\; \boxed{\;\eta_E \lesssim 2{,}3\times10^{-11}\ \mathrm{Pa\cdot s}\ \text{(Phoebe eşdeğeri)} - \mathbf{1{,}4\times10^{6}}\ \text{kat sıkı}\;}$$

**Bağımsız çapraz denetim.** Aynı prograd tork Güneş çevresindeki her cisme etki eder; astronomik birimin kararlılığı ($\lesssim0{,}01$–$0{,}1$ m/yıl) $\eta_E\lesssim1{,}5\times10^{-10}$–$1{,}5\times10^{-9}$ Pa·s verir — aynı yönde, 6–60 kat gevşek ✓ *(Ay bu kanalda kısıt vermez: $\Delta v^4$ çarpanı 1 km/s'de çöker; Ay'ın gücü **düğüm** kanalındadır, 11.4.3.)*

> **M-37'nin ölçekleme kaydı aşılmıştır.** *"Sınır $a_b^2$ ile ölçeklendiğinden en küçük kalıcı retrograd cisim en güçlü sınırı verir"* çıkarımı M-43'ten önce yazılmıştı. Sınırı yöneten kombinasyon $\eta_E/(r_t\Delta v^4)$'tür ve $\Delta v^4$ yarıçap çarpanını ezer: **en güçlü sınırı en küçük cisim değil, en hızlı ve en dar yapı verir — Satürn halkası.**

---

## 11.4.8.1 Sürüklenme Zarfı: Erim, Kavrama ve Dördüncü Kanal · **[T-aday]**

Yukarıdaki hesaplar zarfın iki ayrı özelliğini kritik hâle getirir: **erimi** (nereye kadar uzanır) ve **kavraması** (ne kadar tam sürükler). İkisi ayrı sorulardır ve ayrı cevapları vardır.

### Zorunlu ilk adım: Fizeau muhasebesi

Işık yolundaki ortamın **ortalama hızı**, iki fazın ağırlıklı toplamıdır (M-16):

$$\langle v_{ortam}\rangle_{yol} = \phi\,v_{madde} + (1-\phi)\,v_{ambiyans}$$

**Fizeau ile denetim.** Su $u$ ile akar, ambiyans ortam laboratuvarda durgundur: $\langle v\rangle=\phi u$, ışık hızı $c/n+\phi u$, ölçülen sürüklenme katsayısı $\phi=1-1/n^2$ ✓

**Rezonatör geometrisi.** Düzenek laboratuvarda durgun, **ambiyans ortam $V$ ile akar**:

$$\langle v_{ortam}\rangle_{yol} = (1-\phi)\,V$$

Anizotropiyi yöneten çarpan $\phi$ değil **$(1-\phi)$**'dir:

| Yol | $n$ | $\phi$ | $(1-\phi)V$ | $\big((1-\phi)V/c\big)^2$ | Deney sınırı |
|---|---|---|---|---|---|
| **Vakum kovuk** | 1,000000 | **0** | **29 785 m/s** | $\mathbf{9{,}9\times10^{-9}}$ | $10^{-17}$ |
| Hava | 1,000293 | $5{,}9\times10^{-4}$ | 29 768 m/s | $9{,}9\times10^{-9}$ | 1887'de $4\times10^{-9}$ |
| Su | 1,333 | 0,437 | 16 762 m/s | $3{,}1\times10^{-9}$ | $10^{-16}$ |
| Safir | 1,77 | 0,681 | 9 507 m/s | $1{,}0\times10^{-9}$ | $10^{-16}$ |

**Kavrama ile bastırılmadıkça vakum yolu en kısıtlayıcıdır** ($\phi=0$, rüzgârın tamamını görür); katı yol $1/n^4$ ile zayıflar. *(Bu tablo, izotropinin **kavrama** yoluyla sağlanması varsayımı altındadır. Aşağıda türetilen kinematik ölçek terimi anizotropiyi her yol için tam olarak sıfırlar ve tablo yalnız kavrama yolunun neden gerekmediğini göstermek üzere burada durur.)*

### Kavrama yoluyla çözüm neden tükeniyor

Anizotropi kavrama ile bastırılacaksa, zarf kaymayı çok yüksek bir tamlıkla söndürmek zorundadır. Ölçülen sınır ($\delta c/c<10^{-17}$, artık kayma $<0{,}95$ m/s) şunu ister:

$$\text{zarf tamlığı} > 1-3{,}2\times10^{-5}$$

Teorinin üç kuplaj kanalı da bunun çok altındadır:

| Aday kanal | Verdiği | Yetersizlik |
|---|---|---|
| Viskoz sınır tabakası $\sqrt{\nu_E t}$ | Güneş Sistemi yaşında $6{,}9\ \mu$m | $9\times10^{11}$ |
| Öteleme deplasmanı $\phi$ | yalnız madde içinde; vakumda $0$ | tam |
| Dönme kavraması $\xi$ | $4{,}6\times10^{-10}$ | $10^{5}$ |

> **Viskoz yolu kapatan şey bu bölümün kendi sonucudur.** Zarfı viskoz bir sınır tabakası olarak kurmak büyük bir $\eta_E$ ister; 11.4.8'in sınırı ($\lesssim2{,}3\times10^{-11}$ Pa·s) bu yolu altı mertebe kapatır.

**Kavrama yolu tükenmiştir.** Ama izotropinin ikinci bir mekanik çıkışı vardır ve aşağıda türetilir; o çıkışta zarfın tam sürüklemesine hiç gerek kalmaz ve yukarıdaki tamlık koşulu da ortadan kalkar.

### Erim: gradyan hâkimiyeti — **[T]**

Erim tarafı türetilebilir. Ortam hangi cismin $\nabla P$'sine cevap veriyorsa onun çevresinde dolaşır (DY-1); gövdenin gradyanı Güneş'inkini **Hill yarıçapına** kadar bastırır:

$$R_{zarf}\simeq a\left(\frac{M}{3M_\odot}\right)^{1/3}\qquad \text{Dünya: } 235\,R_\oplus \qquad \text{Satürn: } 1\,086\,R_S$$

Halkaları, düzenli uyduları ve laboratuvarları rahatça kapsar. **Erim açık kalem değildir.**

### Kinematik ölçek terimi: türetim · **[T]**

Üç kavrama kanalının da yetersiz kalması, sorunun yanlış yerde arandığının işaretidir. Bir esir kuramında ışık hızı izotropisinin **iki** mekanik çıkışı vardır: ortamı gövdeyle birlikte taşımak (Stokes) ya da gövdeyi kısaltmak (Lorentz–FitzGerald). Birincisi yukarıda tükendi. İkincisi teoride hazır durur ve kullanılmamıştır: **M-42'nin ölçek yapısı.**

M-42, madde ölçeği $\Lambda$ ile cetvelin ve saatin birlikte ölçeklendiğini kurar ($\ell,f\propto\Lambda$) ve potansiyel terimini verir, $\Lambda_{grav}=1-\Phi/c^2$. Eksik olan **kinematik** terimdir ve teorinin kendi malzemesinden türetilir.

#### Kurulum

Üç girdi, hepsi mevcut:

1. **Ortam sıkıştırılabilirdir** ve içindeki bozunum hızı $c=\sqrt{P/\rho}$'dur (Postülat 1, Kavrama Yasası M-1).
2. **Nükleon bir deplasman kaynağıdır**; çevresinde durgun hâlde küresel simetrik bir basınç alanı kurar (M-35, debi $q_n$).
3. **Bağlı maddenin denge aralığı** bu alanların karşılıklı dengesiyle belirlenir (M-15'in kafes resmi; molekül, komşusunun alanında oturur).

Ortama göre $V$ hızıyla giden bir gövdede alan artık küresel değildir. Kararlı hâlde, küçük bozunum yaklaşımında (teorinin her yerde kullandığı doğrusal ortam tepkisi — M-35 Varsayım 2, M-37 Varsayım 3) basınç potansiyeli şu denklemi sağlar:

$$(1-M^2)\,\frac{\partial^2\varphi}{\partial x^2}+\frac{\partial^2\varphi}{\partial y^2}+\frac{\partial^2\varphi}{\partial z^2}=0,\qquad M\equiv\frac{V}{c}$$

$x$ hareket doğrultusudur. Bu, sıkıştırılabilir akışkanın standart kararlı-hâl denklemidir; teoriye yeni hiçbir şey eklemez.

#### Türetim

$X=x/\beta$ dönüşümü, $\beta\equiv\sqrt{1-M^2}$ ile denklemi Laplace denklemine indirger:

$$(1-M^2)\frac{1}{\beta^2}\varphi_{XX}+\varphi_{yy}+\varphi_{zz}=\varphi_{XX}+\varphi_{yy}+\varphi_{zz}=0$$

Yani **hareketli kaynağın alanı, durgun alanın hareket doğrultusunda $1/\beta$ ile gerilmiş hâlidir.** Tersi de doğrudur ve aradığımız ifade odur: *bir kafes dizilimi, hareket hâlinde durgun hâldeki alan yapısını koruyabilmek için hareket doğrultusunda $\beta$ ile kısalmak zorundadır.* Denge aralığı alan yapısıyla belirlendiğine göre (girdi 3), kısalma fiziksel olarak gerçekleşir:

$$\boxed{\;\frac{\ell_\parallel}{\ell_\parallel^{(0)}}=\beta=\sqrt{1-\frac{V^2}{c^2}}\;,\qquad \ell_\perp\ \text{değişmez}\;}$$

**Bu, Lorentz çarpanının kendisidir — ve seri açılımı değil, kapalı biçimi.** Sıkıştırılabilir akışkan mekaniğinde aynı çarpan Prandtl–Glauert dönüşümü olarak bilinir; burada bir benzetme değil, teorinin ortamının doğrudan sonucudur.

#### Saat tarafı

Frekans aynı çarpanı bağımsız bir yoldan alır. Zerre balistiktir ve sürati **ortama göre** $c$'dir (M-1). Enine ayrılmış iki nokta arasında gidip gelen bir Zerre'yi saat sayalım: gövde $V$ ile giderken Zerre'nin yolu zikzaklaşır ve bir çevrim başına $2L/\beta$ olur (enine uzunluk kısalmaz). Dolayısıyla

$$f = \frac{c\beta}{2L} \;\Longrightarrow\; f \propto \beta$$

Bütün saatler birbiriyle uyumlu kalmak zorunda olduğundan bu, her bağlı salınıcıya taşınır. **Cetvel ve saat aynı çarpanla ölçeklenir — tam olarak M-42'nin kuralı:**

$$\boxed{\;\Lambda=\Lambda_{grav}\cdot\Lambda_{kin},\qquad \Lambda_{grav}=1-\frac{\Phi}{c^2},\qquad \Lambda_{kin}=\sqrt{1-\frac{V^2}{c^2}}\;}$$

$V$, maddenin **yerel ortama göre** hızıdır. **Yeni parametre yoktur:** $\Lambda$ envanterde zaten [T] statüsündedir; eklenen tek şey, mevcut ölçek yapısının hız bağımlılığıdır.

#### Gözlemin dayattığı biçim sağlanıyor

11.4.8.1'in başındaki muhasebe, kinematik terimin **tam** Lorentz çarpanı olmasını dayatıyordu: ikinci mertebede kesilmiş bir biçim $\beta^4/8=1{,}2\times10^{-17}$ artık bırakır ve modern sınır $10^{-17}$'dir. Prandtl–Glauert dönüşümü $\beta$'yı **kapalı biçimde** verir; kesme yoktur, dolayısıyla artık da yoktur. Türetim, gözlemin istediği tam biçimi kendiliğinden üretir.

#### İki kapsam kuralı

**(1) $\Lambda_{kin}$ maddeye etki eder, ortamın yayılma hızına etmez.** $c_{loc}\propto\Lambda_{grav}^2$ bir *yer* niceliğidir — ortamın o noktadaki hâli. $\Lambda_{kin}$ ise *hareket eden gövdenin* niceliğidir. İkisini karıştırmak, $\phi$ ile $\xi$'yi karıştırmakla aynı türden bir kategori hatasıdır.

**(2) Tekillik yereldir, evrensel bir tavan değildir.** $M=V/c_{loc}$ olduğundan $\beta\to0$ koşulu yerel bozunum hızına bağlıdır. Postülat 4 ile uyum tamdır: $c$ sabit olmadığı için bariyer de sabit değildir; $P/\rho$'nun yüksek olduğu bölgede aynı $V$ daha küçük $M$ verir ve kısalma azalır.

### Sonuç: Postülat 7 zorunlu işini kaybediyor

| Zarfın klasik işi | Kim yapıyor |
|---|---|
| Yörünge sürüklemesinin bastırılması | **M-43** — altkritik rejim, $10^{28}$ bastırma, zarftan bağımsız |
| Işık hızı izotropisi | **$\Lambda_{kin}$** — kısalma yoluyla, kavramadan bağımsız |

İkisi de zarf gerektirmiyor. Zarf böylece bir **postülat** olmaktan çıkıp bölgesel bir tanıma iner: gövdenin gradyanının hâkim olduğu bölge, erimi Hill yarıçapı ($235R_\oplus$, $1086R_S$). **Teori bir postülat eksilir.**

> **Ve bedeli açıkça kaydedilmelidir: bir sınav düşüyor.** $\Lambda_{kin}$ tam Lorentz kısalması ürettiğine göre, ışık hızı anizotropisi **her yol için** tam olarak sıfırlanır — vakumda, havada, katı dielektrikte. Dolayısıyla 11.4.8.1'in $(1-\phi)V$ tablosu ve ondan çıkan **$1/n^4$ ölçekleme sınavı geçersizdir**; teori de standart fizik gibi sıfır öngörür. Zarfın kavrama tamlığı üzerine konulan $>1-3{,}2\times10^{-5}$ koşulu da düşer, çünkü koşulun kaynağı bastırılmamış bir anizotropiydi.
>
> Muhasebe nettir: **bir açık kalem ve bir postülat kazanıldı, bir ayırt edici sınav kaybedildi.** Bu arenada teori artık Lorentz fenomenolojisini birebir üretir ve ondan ayrılmaz.

> **Geriye ne kalıyor.** Ayrım, doğrusallaştırmanın bozulduğu yerde aranmalıdır: **(i)** $M\to1$ civarı, yani maddenin yerel bozunum hızına yaklaştığı rejim — orada Prandtl–Glauert doğrusal biçimi geçersizleşir ve teori Lorentz'den ayrılır; **(ii)** $\Lambda_{grav}$ ile $\Lambda_{kin}$'in birlikte büyük olduğu durumlar (derin kuyuda hızlı hareket), çünkü çarpım yapısı iki terimin ayrı ayrı ölçülmesinden farklı bir öngörü verir; **(iii)** teorinin tercihli çerçevesi ortadan kalkmaz — yalnız doğrusal rejimde gözlenemez hâle gelir. Üçü de hesaplanmamıştır.

**11.4.6 ile bağ.** S4'ün cevaplanmayan yarısı (optik derinlik farkı) §7.4'te **kalem 11.4-i** olarak kalır: tedarik ↔ kayıp dengesi standart mekanizmaların işidir ve teorinin kapsamı dışındadır.

---

## 11.4.9 Neden Her Şey Düz: F5'in Kendini Söndüren Yapısı · **[T]**

Aynı matematik, halkanın çok ötesine geçer. Yazarın son sorusu — *galaksiler ve yörünge sistemleri neden düz?* — burada cevaplanır, ve cevap F5'in en güçlü olduğu yerdir.

### Genelleştirilmiş F5 yasası ve **kabuksallık üssü**

M-39'un $v(\theta)=V\cos\theta$ profili özel bir hâldir. Genel olarak dolaşımın enlemsel yapısı $v(r,\theta)=V(r)\cos^{\lambda}\theta$ yazılırsa:

$$P = P_{kutup} - \kappa_5\rho_0 V^2\cos^{2\lambda}\theta \quad\Longrightarrow\quad \boxed{\;f_\theta = -\frac{2\lambda\,\kappa_5\rho_0V^2}{r}\cos^{2\lambda-1}\theta\,\sin\theta\;}$$

$\lambda$, dolaşımın **kabuksallık üssüdür**: dönüşün küreler üzerinde mi ($\lambda=1$, katı/kabuksal) yoksa silindirler üzerinde mi ($\lambda\le0$) organize olduğunu ölçer.

| $\lambda$ | Dolaşımın organizasyonu | $f_\theta$ | Sonuç |
|---|---|---|---|
| **$\lambda=1$** | küreler üzerinde (kabuksal / katı-cisim) | $-\dfrac{\kappa_5\rho_0V^2}{r}\sin2\theta$ | **ekvatora doğru — M-39'un yasası** |
| $\lambda=0$ | silindirler üzerinde, $v_\theta=$ sabit (düz dönüş eğrisi) | **0** | **kuvvet yok** |
| $\lambda<0$ | silindirler üzerinde, $v_\theta$ içe doğru artan | $+$ | eksene doğru — **bu F4'tür, F5 değil** (M-38) |

> **Kategori kaydı — F4 ile F5, aynı deplasman basıncının iki izdüşümüdür.** Silindirik bileşen (dönüş silindirler üzerinde sabitse) **F4**'ü doğurur ve eksene bakar; kabuksal artık bileşen **F5**'i doğurur ve ekvatora bakar. Bu ayrım, DY-1'in *"denge yasaları kuvvetlerle toplanmaz"* uyarısını F5 için de kapatır: ortamın siklostrofik dolaşımı (M-22, silindirik) F4/DY-1 hanesine yazılır; F5 yalnız **enlemsel artığı** okur. Aynı gradyanı iki kez saymak bu ayrımla imkânsızlaşır.

### Disk, F5'in sabit noktasıdır — **iki bağımsız anlamda**

$$\boxed{\;\textbf{(1) } \sin2\theta\to0 \text{ (geometrik)} \qquad\qquad \textbf{(2) } \lambda\to0 \text{ (kinematik)}\;}$$

Dönen bir ortam konfigürasyonu başlangıçta kabuksaldır ($\lambda\simeq1$: yeni çöken bir bulut, yeni doğmuş bir gövde çevresi). F5 devrededir ve maddeyi ekvatora bastırır. **Düzleşme ilerledikçe iki şey birlikte olur:** madde $\theta\to0$'a gider ve $\sin2\theta$ sıfırlanır; **ve** dönüş barotropik hâle gelip silindirler üzerinde sabitlenir (Poincaré–Wavre / Taylor–Proudman), yani $\lambda\to0$ ve F5 **kaynağını da kaybeder.**

> **F5 kendini söndüren bir kuvvettir.** Düzlemi kurar, düzlem kurulunca susar. Disk onun *dengesi* değil, **sabit noktasıdır.** Bu, "neden diskler bu kadar yaygın ve bu kadar kararlı" sorusunun mekanik cevabıdır: sistem bir kuvvetin sıfırına doğru akar ve varınca kuvvet ortadan kalkar — geri itme yoktur, salınım yoktur, aşırı düzeltme yoktur.

### Galaktik ölçek — burada F5 kesirli değil, **tek** düzlem seçicidir

Galaktik yarıçapta $J_2$ kanalı yoktur: $(R_e/r)^2$ ile ölçeklenen bir figür çokkutbu 10 kpc'de $10^{-30}$ mertebesindedir. Merkezî gövdenin basıklığı galaktik diski düzleştiremez. F1 ise düzlem tercih etmez (11.4.5). **Geriye tek kaynak kalır.**

Kabuksal rejimde ($\lambda=1$, R2 — kavrama kesri içermez, M-39):

$$a_\theta = -\frac{\kappa_5}{4}\,\frac{v_0^2}{r}\sin2\theta \qquad\Longrightarrow\qquad \boxed{\;\mathcal{F}_5^{gal} = \frac{\Omega_5^2}{\Omega^2} = \frac{\kappa_5}{2} \;=\; 7{,}5\times10^{-3}\;}$$

**Yarıçaptan bağımsız** — çünkü hem $a_\theta$ hem $\Omega^2$ düz dönüş eğrisi rejiminde $v_0^2/r$ ile gider. F5, galaktik diskin her yerinde dikey geri çağırmanın aynı kesrini sağlar. Samanyolu için düzleşme zaman ölçeği ($v_0=220$ km/s, $r=8{,}2$ kpc, 45°):

$$a_\theta = 7{,}2\times10^{-13}\ \mathrm{m/s^2} \qquad\Longrightarrow\qquad t_{düz}\simeq\sqrt{2r/a_\theta} = 2{,}7\times10^{16}\ \mathrm{s} \approx \mathbf{840\ Myr}$$

Galaktik dinamik zaman ölçeğiyle ($2\pi r/v_0=230$ Myr) aynı mertebede — yani F5, bir galaksiyi **birkaç dönüşte** diske indirir. Gözlenen disk oluşum zaman ölçeği (~1 Gyr) bu değerle uyumludur.

> **Dürüst kayıt.** Bu bir mertebe hesabıdır: gerçek düzleşme, ortamın kendi dikey basınç desteğine ve baryonik özçekime karşı yürür; ikisi de girmemiştir. Sayının söylediği tek şey şudur: **F5'in düzleştirme kapasitesi galaktik ölçekte doğru mertebede.** Nicel hesap §7.4'e yazılmıştır (kalem 11.4-ii).

### Yörünge eş-düzlemliliği

F5 **düzlemi seçer**, açısını **sönümlemez** — sönüm için yitim gerekir. Eş-düzlemliliğin tam zinciri üç halkalıdır:

$$\underbrace{\text{F5} \Rightarrow \text{çekici düzlem = dönme düzlemi}}_{\text{11.4.4}} \;\;+\;\; \underbrace{\text{M-37}\ \gamma_{sür} \Rightarrow \Delta v\text{ sönümü}}_{\tau_{ret}=2\rho_ca_b^2/9\eta_E} \;\;\Longrightarrow\;\; \text{eğik yörüngeler düzleme oturur}$$

Koşul, F5'in presesyon hızının sönüm hızını aşmasıdır:

$$\tfrac12\mathcal{F}_5(r)\,\Omega(r) \;\gtrsim\; \gamma_{sür} = \frac{9\eta_E}{2\rho_c a_b^2}$$

Sağlanırsa yörünge **zorlanmış düzleme** (F5'in düzlemi) sönümlenir; sağlanmazsa rastgele kalır. M-37'nin üç sonucu — ekliptik eş-düzlemlilik, prograd tercih, dairesellik — bu koşulun sağlandığı bölgenin (yakın alan) sonuçlarıdır; Phoebe gibi $215R_e$'deki retrograd cisimler ise koşulun sağlanmadığı bölgenin. **İki bölgenin sınırı, 11.4.7'nin F5 yakın alan yarıçapıdır.**

---

## 11.4.10 Bölümün Bilançosu

### Kurulan sonuçlar

| # | Sonuç | Statü |
|---|---|---|
| 1 | F5 genlik denklemi: $\hat{\mathcal{Q}}_{et}=\dfrac{\kappa_5\phi_{doy}\mathcal{S}}{2}\mathcal{Q}\left(\dfrac{R_\phi}{R_e}\right)^{6}$; çarpanlar ayrıştırıldı | **[T]** |
| 2 | Basıklığın gradyan sertleştirmesi $\mathcal{S}=\dfrac{\pi/2}{E(e)}=1+\dfrac f2+\cdots$ | **[T]** |
| 3 | Radyal profil **Rankine**: içeride $\propto r$, dışarıda $\propto r^{-(2s+1)}$; tepe $r=R_\phi$'de | **[T]** |
| 4 | Maksimum kümesi: **45° enlem halkaları** — nokta değil, sırt | **[T]** |
| 5 | Dış alan sönüm üssü $s=2$ (dipolar); rakip adaylar Ay'ın düğümüyle elendi | **[T]** |
| 6 | $\nu^2/\Omega^2$'de **tek paritede** $(R_e/r)^3$ terimi — hiçbir kütle çokkutbuyla taklit edilemez | **[T]** · F5'in ilk ayırt edici imzası |
| 7 | $\kappa_5\lesssim2{,}1\times10^{-3}$ (LLR düğümü); gözlemin sabitlediği çarpım $\kappa_5\phi\lesssim1{,}5\times10^{-3}$ | **[A]** |
| 8 | **Korunumlu kuvvet teoremi:** $h=\sigma_z/\nu$ — kuvvetler $\nu$'yü, enerji bütçesi $\sigma_z$'yi belirler. $\Psi_5$ potansiyeli olduğu için F5 tek başına inceltemez; aynısı Kepler ve $J_2$ için de geçerli | **[T]** |
| 9 | Halka inceliği çarpışmalı sönümdendir; F5'in payı 10 metrede 0,2–0,7 mm | **[T]** |
| 10 | $\mathcal{Q}/J_2$ = dönüşün figüre soğurulmayan payı; Satürn birinci (9,50) | **[T]** |
| 11 | $\mathcal{P}_5$ gezegenden gezegene yakın-sabit (%0,34–0,51): $\mathcal{Q}/J_2$ ile $(R_\phi/R_e)^6$ birbirini götürür — $J_2$ kanalının göstermediği bir evrensellik | **[T]** · ayırt edici öngörü |
| 12 | **$\phi$ iç yoğunluk profilinden türetildi:** $\phi(\rho)=\min(\rho/\rho_*,\phi_{doy})$; $\rho_*$ dışlanan hacimden, $\phi_{doy}$ **fazdan**. Su ve manto üzerinde $\pm$%13 kalibre. $\phi_\oplus=0{,}70$, $\phi_{Satürn}=0{,}45\pm0{,}03$ | **[T]** |
| 13 | **Deplasman yüzeyi $R_\phi$** — F5'in dış alan sınır koşulunun kurulduğu derinlik; Satürn $0{,}935R_e$, Jüpiter $0{,}966$, Uranüs $0{,}959$, Neptün $0{,}968$; karasal cisimlerde $R_e$ | **[T]** · yeni kavram |
| 14 | Metalik/plazma fazda $\phi=1-\delta$, $\delta\lesssim10^{-13}$; iyonizasyon $\phi$'yi **artırır** ve geçiş süreklidir | **[T]** |
| 15 | **$10^{28}$'lik kanal ayrımı:** M-43'ün $v^4$ bastırması + DY-2'nin kayma yasası ⟹ ortam kuplajı yörünge kanalında dikey kanaldan $1{,}5\times10^{28}$ kat etkin ($r_t$ sadeleşir, parametresiz) | **[T]** |
| 16 | Ortamın orbital torku **daima dışa**dır ⟹ halka yağmuru bu kanalın işi değildir; standart mekanizmalardan ayrışma yönden ve profilden gelir, tanecik boyundan değil | **[T]** |
| 17 | **$\eta_E\lesssim2{,}3\times10^{-11}$ Pa·s** — Phoebe'den $1{,}4\times10^{6}$ kat sıkı; kitaptaki en sıkı $\eta_E$ kısıtı. Dünya yörüngesi bağımsız çapraz denetim verir | **[A]** |
| 18 | **Fizeau muhasebesi:** yoldaki ortalama ortam hızı $\phi v_{madde}+(1-\phi)v_{ambiyans}$; rezonatörde $(1-\phi)V$ ⟹ vakum yolu en kısıtlayıcı, katı yol $1/n^4$ ile zayıf | **[T]** |
| 19 | **Kavrama yoluyla izotropi tükenmiştir:** üç kanal, gereken $>1-3{,}2\times10^{-5}$ tamlığın en az $10^4$ kat altındadır. İzotropi bu yüzden ortam taşınarak değil, **madde kısalarak** sağlanır (kalem 21) | **[T]** |
| 20 | **Zarfın erimi türetildi:** gradyan hâkimiyeti (Hill), $235R_\oplus$ · $1086R_S$ | **[T]** |
| 21 | **Kinematik ölçek terimi $\Lambda_{kin}=\sqrt{1-V^2/c^2}$ türetildi** — sıkıştırılabilir ortamda hareketli deplasman kaynağının alanından (Prandtl–Glauert). Cetvel ve saat aynı çarpanla ölçeklenir; ışık hızı izotropisi **kavramadan bağımsız** çıkar, yeni parametre eklenmez. Kapalı biçim, gözlemin istediği tam Lorentz çarpanıdır | **[T]** |
| 22 | F5 **kendini söndüren** kuvvettir: disk hem geometrik hem kinematik sabit noktasıdır | **[T]** |
| 23 | Galaktik ölçekte $\mathcal{F}_5=\kappa_5/2$, yarıçaptan bağımsız; düzleşme ölçeği $t\approx840$ Myr | **[T/A]** |

### Bölümün üç yapısal tespiti

| Tespit | Nicel karşılığı |
|---|---|
| **Dönüş hızı F5'i (ve F4'ü) birlikte büyütür** | $f_{yanal}\propto v_e^2$; ikisi de $\omega_1$ kökünden gelir ve ayrı ayarlanamaz. Boyutsuz taşıyıcı $\mathcal{Q}=\omega^2R_e^3/\mathcal{G}M$. |
| **Basıklık gradyanı sertleştirir — ama iki zıt kanaldan** | Meridyen kısalması $\mathcal{S}=1+f/2$ genliği **artırır** (Satürn'de %5); figür soğurması ise ölçülebilir payı ($\propto\mathcal{Q}/J_2$) **azaltır.** Mutlak büyüklüğün taşıyıcısı $\mathcal{Q}$, ölçülebilir payınki $\mathcal{Q}/J_2$'dir. |
| **Kutupta sıfır; uzaklaşınca önce artar sonra azalır** | Kutupta $\sin2\theta=0$ — geometrik özdeşlik, yaklaşım değil. Radyal profil Rankine'dir ve tepe **deplasman yüzeyindedir** ($R_\phi$): Satürn'de $0{,}935R_e$, karasal cisimlerde ekvator yarıçapının kendisi. Enlemsel tepe 45°'dedir. |

### Sınavlar

| # | Sınav | Durum |
|---|---|---|
| **11.4-A** | Satürn bükülme dalgalarında tek-parite $(R_e/r)^3$ artığı; öngörülen katsayı $\hat{\mathcal{Q}}_{et}=3{,}8\times10^{-4}$ | Veri hazır (Cassini); analiz yapılmadı. **F5'in ilk yürütülebilir doğrudan sınavı** |
| **11.4-B** | Ay'ın düğüm artığında **0,72 mas/yıl** bileşeni (LLR, 50+ yıllık seri) | Öngörü eşikte |
| **11.4-C** | 45° enlem sırtı: gaz devi atmosferlerinde orta enlem akış deseni, Dünya mantosunda gerilme imzası | Aranmadı |
| **11.4-D** | Saydam iletkende Fizeau: ara bölge taşıyıcı yoğunluğu $n_c\gtrsim6{,}8\times10^{27}$ m⁻³'yi geçince $f>1-1/n^2$. En iyi şeffaf iletken oksitler eşiğin 7 kat altında ⟹ onlarda etki beklenmez | Metal/plazma $\phi\to1$ tezinin tek laboratuvar sınavı |
| ~~11.4-E~~ | *(Geçersiz)* Anizotropinin yol indisine bağlı olması, izotropinin kavrama yoluyla sağlandığı varsayımına dayanıyordu. $\Lambda_{kin}$ anizotropiyi her yol için tam sıfırlar; teori de standart fizik gibi sıfır öngörür (11.4.8.1) |

### Açık kalemler

- **11.4-i** — Halka optik derinliği bütçesi: Roche kuşağı ↔ buz çizgisi ↔ kütle kaybı ömrü. *S4'ün cevaplanmayan yarısı; teorinin kapsamı dışında ama cevaplanması gereken soru.*
- **11.4-ii** — Galaktik düzleşmenin tam hesabı: F5 ↔ ortamın dikey basınç desteği ↔ baryonik özçekim.
- **11.4-iii** — Ortamın prograd torkunun sistematik taraması. Halka ve Dünya yörüngesi ilk iki sınavdır; en duyarlı adaylar $\Delta v^4/r_t$ oranı büyük olanlardır (halka tanecikleri, iç uydular, sıcak Jüpiterler, ikili pulsarlar).
- **11.4-iv** — **$\Lambda_{kin}$'in doğrusal-olmayan rejimi.** Türetim doğrusallaştırılmış ortam tepkisinde kapalıdır (11.4.8.1) ve tam Lorentz çarpanını verir. Açık kalan üç kalem: **(i)** $M\to1$ civarında Prandtl–Glauert biçiminin bozulması — teorinin Lorentz fenomenolojisinden ayrıldığı tek yer; **(ii)** $\Lambda_{grav}\cdot\Lambda_{kin}$ çarpım yapısının derin kuyuda hızlı hareket için öngörüsü; **(iii)** boyuna salınıcının frekans kısalmasının alan dönüşümünden doğrudan gösterimi (enine ışık-saati yolu kapalıdır).
- **11.4-v** — Metalik hidrojenin yoğunluk modülasyonundan $\delta$'nın tam hesabı. F5 için gereksiz (karantina), 11.4-D'nin öngörüsünü keskinleştirir.

> **Bölümün tek cümlelik sonucu.** F5 halkaları ezmez — **halkalara hangi düzlemin dip olduğunu söyler.** Ezme işini Kepler'in kendi dikey geri çağırması, inceltme işini çarpışmalı sönüm yapar. F5'in payı yüzde bir mertebesindedir; ama o pay, hiçbir kütle dağılımının üretemeyeceği bir radyal paritede geldiği için, kuvvetin gözlemsel varlığını **ölçülebilir** kılan tek şeydir.
