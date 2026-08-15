# 11.4 Yanal İtim Alanının Matematiği: Satürn Halkaları, Düzlem Seçimi ve Dikey Salınım

> [!NOTE]
> **Bölümün konumu ve tezi.** 11.2 F5'in **yapısını** ($\sin2\theta$) gövde içinde kurdu; bu bölüm aynı kuvvetin **gövde dışındaki** alanını kurar ve teorinin halka tezini eksiksiz verir. Tez üç cümledir: **(i)** **Halkayı F5 kurar.** Düzlemi seçen ve maddeyi o düzleme bastıran kuvvet F5'tir — doğrudan payı ortamda hâlâ canlı olan deplasman alanından, dolaylı payı aynı dönüşün maddeye çökelmiş fosili olan figürden ($J_2$, 11.2.6) gelir; iki kanal tek köktendir ve ikisi de teorinindir. **(ii)** **Salınımı halkanın kendi Evrenakı rampası sönümler.** Her kütle, nükleonlarının pulsasyonuyla çevresinde bir deplasman rampası taşır; tanecikler birbirine değmeden önce rampaları buluşur ve dikey hareketin enerjisi alan aracılığıyla halkanın ortak dolaşımına boşalır. Temaslı çarpışma bu zincirin son adımıdır — etkendir, ama ana etken değildir (11.4.5). **(iii)** **Aynı F5, levha geometrisinde $(R/h_z)^2$ ile mertebelerce güçlenir: galaksilerin yassılığı da aynı kuvvetin eseridir** (11.4.9). Bölümün teknik kazançları: F5'in radyal profili bir **Rankine tepesidir** ve maksimumu **deplasman yüzeyindedir** (11.4.2); $\phi$ serbest girdi değildir, iç yoğunluk profilinden türetilir (11.4.1-(4)); dış alanın sönüm üssü **Ay'ın düğüm gerilemesiyle** sabitlenir ($s=2$, 11.4.3); F5 dikey salınıma **çift olmayan radyal üsle** ($\propto(R_e/r)^3$) girer — hiçbir kütle çokkutbunun üretemeyeceği, **taklit edilemez** imza (11.4.4); ve rampanın erimi türetilir: kesit çarpanı $(r_H/a_b)^2=1{,}1$–$3{,}2$, kalınlık kilidi parametresiz $h\simeq a_b$ (11.4.5).

---

## 11.4.0 Bölümün Soruları

Dört soru sorulur ve dördü de nicel cevaplanır:

| # | Soru | Cevabın yeri |
|---|---|---|
| **S1** | F5'in büyüklüğünü ne belirler? Dönüş hızı ve basıklık nasıl girer? | 11.4.1 |
| **S2** | Kütleden uzaklaşınca F5 nasıl değişir? Kutupta gerçekten sıfır mı? | 11.4.2–11.4.3 |
| **S3** | Halka düzlemini ne kurar, salınımı ne sönümler, kalınlığı ne kilitler? | 11.4.4–11.4.5 |
| **S4** | Halkalar neden Satürn'de bu kadar belirgin, diğer gaz devlerinde değil? | 11.4.6 |

Ek olarak, aynı matematikten galaktik disklerin ve yörünge sistemlerinin **düzlüğü** çıkar (11.4.9) — ve orada geometri F5'i mertebelerce yükseltir: bir levhada gradyan ölçeği $R$ değil $h_z$'dir. Genliğin ikinci çarpanı F4'ün radyal payıdır, yani **F5 ancak F4'ün güçlü olduğu yerde güçlüdür.**

**Notasyon.** $\theta$ ekvatordan ölçülen enlem (M-39 konvansiyonu), $r$ küresel yarıçap, $R=r\cos\theta$ eksene dik uzaklık (S-14). Gövdenin ekvator yarıçapı $R_e$, kutup yarıçapı $R_p=R_e(1-f)$. Kuvvet $-\nabla P$, $dP/dr>0$ (R-4). $\rho_0=\rho_n/4$ ($k=0$, M-8), $\rho_n=2{,}7\times10^{17}$ kg/m³ (R-6). Teorinin kendi denklemlerinde $\mathcal{G}M$ yazılır (R-1/S-20).

---

## 11.4.1 F5'in Genlik Denklemi: Üç Çarpan ve İkisinin Zıt Yönde Çalışması · **[T]**

M-39'un sonucu, sabit $r$ üzerinde teğetsel kuvvet yoğunluğudur:

$$f_{yanal}(r,\theta) = -\frac{\kappa_5\,\phi\,\rho_0\,V(r)^{2}}{r}\,\sin 2\theta$$

Burada $V(r)$ *deplase eden akışın* o yarıçaptaki genliğidir ve $\phi$ deplasman hacim kesridir ($p=1$; M-39 Varsayım 4'ün iki-fazlı türetimi). Maddeye etki eden ivme $a=f/\rho_n$'dir (M-2), dolayısıyla $\rho_0/\rho_n=\tfrac14$ çarpanı her yerde görünür.

Genliği belirleyen üç çarpan vardır ve ikisi zıt yönde çalışır.

### (1) Merkezî makro kütlenin dönüş hızı — doğrudan ve güçlü ✓

Gövde rejiminde (R1) $V(R_e)=\omega R_e=v_e$'dir. Kuvvet $v_e^2$ ile gider, yani **dönüş hızının karesiyle**. Bu, aynı $\omega$'nın F4'ü de büyütmesiyle tutarlıdır (M-38): iki kuvvet de $\omega_1$ kökündendir (M-39 köken haritası), dolayısıyla **F4 ve F5 asla ayrı ayrı ayarlanamaz** — birini büyüten şey ötekini de büyütür.

Boyutsuzlaştırılmış hâli, gözlemle karşılaştırılabilir tek biçimdir. **Dönüş (deplasman) parametresi** tanımlanır:

$$\boxed{\;\mathcal{Q} \equiv \frac{\omega^2 R_e^{3}}{\mathcal{G}M} = \frac{v_e^2 R_e}{\mathcal{G}M} \;}$$

$\mathcal{Q}$, gövdenin dönme atalet ivmesinin yüzeydeki kütle-itim ivmesine oranıdır ve F5'in bütün gözlemsel yükünü taşır.

### (2) Basıklık — meridyen kısalması gradyanı gerçekten sertleştirir ✓ (ama zayıf)

Mekanizma şudur: gradyan kutuptan ekvatora doğrudur; basıklık arttıkça kutup ile ekvator birbirine yaklaşır, aynı basınç farkı daha kısa bir yola sığar, gradyan sertleşir. Türetimi aşağıdadır.

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
| *(limit $f\to1$: cisim levhaya iner)* | $\to1$ | **1,5708** |

**Dürüst kayıt.** Mekanizma gerçektir ve Satürn'de en büyüktür — ama etkisi **%5**'tir: yön olarak doğru, mertebe olarak ikincil bir düzeltme. Basıklığın F5'e asıl katkısı bu değildir; aşağıdaki üçüncü kalemdir.

> **Ve bu kanal doygundur.** $f\to1$ limitinde $e\to1$, $E(1)=1$ ve $\mathcal{S}\to\pi/2=1{,}5708$. Meridyen kısalmasından elde edilebilecek **azami** kazanç %57'dir — bir gövdeyi tam levhaya kadar bassanız bile. Dolayısıyla *"basıklık arttıkça F5 sınırsız artar"* okuması bu kanalda **yanlıştır.** Sınırsız olan başka bir kanal vardır ve bu bölümün en büyük sayısal çarpanını o üretir: gradyanın **dikey** ölçeği, $(R/h_z)^2$ olarak 11.4.9'da devreye girer. İkisini ayırmak gerekir — biri yüzeyin eğriliği, öteki yapının kalınlığıdır.

### (3) Basıklığın ikinci ve zıt yönlü kanalı — figür soğurması ⚠

Basıklık bağımsız bir girdi değildir: $f$ ile $\mathcal{Q}$ aynı fiziğin iki yüzüdür (hidrostatik figür, 11.2.6). Dolayısıyla *"basıklık arttıkça F5 artar"* ifadesi **mutlak büyüklükte doğrudur** — ama sebebi basıklığın kendisi değil, onu doğuran $\mathcal{Q}$'dur. Ve burada zıt yönlü bir kanal devreye girer:

> **Figür, dönüşü soğurur.** Gövde dönüşünün bir kısmı kütle dağılımına *fosilleşir* ve $J_2$ olarak dışarıya kütle çokkutbu şeklinde yansır. Bu pay artık ortamda değil, maddededir. Dolayısıyla **ortamda kalan** (yani F5'i besleyen) pay $\mathcal{Q}$ ile artar, $J_2/\mathcal{Q}$ ile azalır.

Bu, S4'ün (Satürn sorusunun) cevabının anahtarıdır ve 11.4.6'da kullanılacaktır. Şimdilik kaydedilecek nicelik:

$$\boxed{\;\frac{\mathcal{Q}}{J_2} \;=\; \text{gövde dönüşünün figüre soğurulmayan payının ölçüsü}\;}$$

### (4) $\phi$'nin kendisi: iç yoğunluk profilinden türetim ve **deplasman yüzeyi** · **[T + kalibre]**

> $\phi$ serbest bir girdi değildir: gövdenin iç yoğunluk profilinden hesaplanır. Yöntem önce, bağımsızca bilinen iki değer üzerinde (sıvı su ve üst manto) kalibre edilir.

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

**Kalibrasyon — yöntem bağımsız olarak bilinen iki değeri üretiyor mu?**

| Sınama | Bu yöntem | Bağımsız değer | Sapma |
|---|---|---|---|
| Sıvı su ($\rho=1000$) | $\rho_*=2363 \Rightarrow \phi=\mathbf{0{,}423}$ | optik ters okuma $0{,}437$; moleküler paketlenme $0{,}36$–$0{,}40$ | ikisinin **arasında**, $\pm$%10 |
| Üst manto forsterit ($\rho=3320$) | iyonik hacimlerle $\rho_*=4732 \Rightarrow \phi=\mathbf{0{,}70}$ | optik ters okuma $0{,}61$ ($n=1{,}6$); bcc Fe $0{,}68$ | **+%13** |

İki bağımsız sınamada $\pm$%13 içinde tutar — ve sapmanın **yönü** M-15'in kendi kaydıyla uyumludur (ters okuma su için ~%10 yüksek sarkıyordu; burada ters okuma manto için %13 *düşük* çıkıyor, yani iki yöntem farklı yönlerde sapıyor ve gerçek değer aralarındadır).

**Satürn'ün iç modeli.** H/He zarfı Mbar basınçlarında $P\simeq K\rho^2$'ye çok yakındır; bu $n=1$ politropudur ve analitik çözümü $\rho(r)=\rho_c\,\sin x/x$, $x=\pi r/R$, $\rho_c=\pi M/4R^3$'tür. Satürn ($M=5{,}683\times10^{26}$ kg, $R_{ort}=5{,}823\times10^{7}$ m): $\rho_c=2261$ kg/m³, $\langle\rho\rangle=687$ kg/m³. Bileşim, dış zarf için $X=0{,}86$, $Y=0{,}13$, $Z=0{,}01$:

$$\rho_*^{Satürn} = \left(\frac{0{,}86}{303}+\frac{0{,}13}{675}+\frac{0{,}01}{1968}\right)^{-1} = \mathbf{329\ kg/m^3} \qquad\Longrightarrow\qquad \rho_{kafes}=0{,}47\times329=\mathbf{155\ kg/m^3}$$

Profil bu yoğunluğu $r=0{,}9356\,R_{ort}$'ta geçer. **Buradaki yarıçap seçimi keyfî değildir ve bir sonraki alt başlıkta türetilir.** Ve kritik sonuç şudur:

| Nicelik | Satürn | Jüpiter | Uranüs | Neptün |
|---|---|---|---|---|
| $\rho_*$ (kg/m³) | 329 | 329 | 379 | 379 |
| $\rho_{kafes}$ (kg/m³) | 155 | 155 | 178 | 178 |
| **Deplasman yüzeyi $R_\phi/R_{ort}$** (ideal küre) | **0,9356** | **0,9657** | **0,9590** | **0,9679** |
| Hacim eşdeğerlik çarpanı $(1-f)^{1/3}$ | 0,9662 | 0,9779 | 0,9923 | 0,9943 |
| **$R_\phi/R_e$** (gözlem birimine geçiş) | **0,9040** | **0,9444** | **0,9516** | **0,9624** |
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
> Değer artık bir kabul değil, iç yoğunluk profilinin ve faz kuralının çıktısıdır.

**Deplasman yüzeyi $R_\phi$.** Ortam gövdede 1 bar seviyesinde durmaz; onu *taşıyan* şey bağlı kafestir ve kafes ancak temas ettiğinde ($\rho>\rho_{kafes}$) ortamı sürükler. Üstündeki seyreltik gaz, ortamı sürüklemek için fazla incedir; oradaki ortam pratik olarak dıştaki ortamla süreklidir. Dolayısıyla **F5'in dış alanının sınır koşulu $R_e$'de değil $R_\phi$'de kurulur.** Sonuçları:

1. **Rankine tepesi $R_\phi$'ye kayar** (11.4.2): Satürn'de $0{,}904\,R_e$, yani ekvatorda 1 bar seviyesinin ~5.800 km altına.
2. **Dış alan genliği $(R_\phi/R_e)^{2s+2}$ ile azalır.** $s=2$ (11.4.3) ile bu $(R_\phi/R_e)^6$'dır: Satürn $0{,}546$ · Jüpiter $0{,}709$ · Uranüs $0{,}743$ · Neptün $0{,}795$. *(Ring yarıçapları $R_e$ biriminde ölçüldüğü için ön çarpan bu birime taşınır; fizik $R_\phi$'nin mutlak değerindedir.)*
3. **Kavram karasal cisimlerde görünmezdir.** Dünya'nın yüzeyi katı silikattır ($\rho=2700\gg\rho_{kafes}^{silikat}=0{,}68\times4732=3218$… sınırda, kabuk altında hemen aşılır), dolayısıyla deplasman yüzeyi gövdenin kendi yüzeyidir: $R_\phi/R_{ort}=1$ ve çarpan $(1-f)^2$'ye iner — Dünya'da $0{,}9933$, yani birden %0,7 ayrı. **Ayrım yalnız gaz ve buz devlerinde belirleyicidir**; karasal cisimlerde ihmal edilebilir kalır.

**Faz kuralının ikinci sonucu: Satürn ↔ Dünya oranı öngörülür.** Dünya'nın yüzeyi kristal katıdır ($\phi_{doy}=0{,}68$), Satürn'ünki yoğun akışkandır ($\phi_{doy}=0{,}47$); faz kuralı oranı doğrudan verir:

$$\frac{\phi_{doy}^{\text{akışkan}}}{\phi_{doy}^{\text{kristal}}} = \frac{0{,}47}{0{,}68} = 0{,}69$$

Benimsenen değerlerle ($\phi_{Satürn}=0{,}45$, $\phi_\oplus=0{,}70$) oran $0{,}64$'tür; ikisi de faz belirsizliklerinin bandı içindedir. **Oran bir seçim değil, faz kuralının sonucudur.** Dünya'da yüzey yoğunluğu doygunluk eşiğini az miktarda aştığı için $\phi$ doygunluk değerinin biraz üstüne çıkar; F5'in kullandığı nicelik gövde ortalaması değil deplasman yüzeyindeki değer olduğundan (gerekçesi (5)'in sonundadır) benimsenen değer $\phi_\oplus=\mathbf{0{,}70}$'tir.

**Bant ve duyarlılık.**

| Varyant | $\langle\phi\rangle_V$ | $\langle\phi\rangle_M$ |
|---|---|---|
| $\phi_{doy}=0{,}44$ (düşük akışkan) | 0,401 | 0,437 |
| **$\phi_{doy}=0{,}47$ (ana)** | **0,426** | **0,467** |
| $\phi_{doy}=0{,}50$ (yüksek akışkan) | 0,450 | 0,496 |
| metalik H'de $\phi=0{,}64$ (RCP) | 0,495 | 0,593 |
| metalik H'de $\phi=1{,}00$ (elektron denizi) | 0,643 | 0,861 |

> **Dürüst kayıt — metalik hidrojen tek gerçek belirsizlik.** Satürn'ün iç zarfında H₂ ayrışıp basınçla iyonlaşır; orada "atom" yoktur, protonlar ve dejenere bir elektron denizi vardır. M-39 iki şey söyler ve ikisi bu noktada gerilir: *(i)* kavrama nükleon düzeyindedir ve iyonizasyonla çökmez; *(ii)* kafes nükleon değil **atomdur** — elektron kabuğu kütlesel olarak boş, Evrenakı açısından doludur. Metalik fazda elektronlar hâlâ oradadır (bağlı değil, ama var), dolayısıyla hacim yine deplase edilir; fakat *ne kadarı* türetilmemiştir. Tablo bandı bunu ölçer: metalik faz da akışkan gibi paketlenme-sınırlıysa $\langle\phi\rangle_M=0{,}467$; elektron denizi hacmi tümüyle doldurursa $0{,}861$. **Ana değer alt uçtur** — çünkü Blok D'nin geçerlilik sınırı ($\phi\to1$ fiziksel değil, geometrik paketlenme bağlar) ve M-39'un nötron maddesi kaydı ($\phi\approx0{,}7$–$0{,}9$, *asimptotik*) ikisi de üst ucu dışlar: hidrojen plazması nötron maddesinden **daha** dolu olamaz. Kalan iş, elektron yoğunluğu eşiğinin ilk-ilkelerden konulmasıdır → §7.4 kalem **11.4-iv′**.

> **Referans yarıçap türetilir, seçilmez — ve seçim ideal küredir.** Bu, hesabın en kolay yanlış kurulan adımıdır ve gerekçesi metodolojiktir: **basıklığın nedenini arayan bir hesap, basılmış gövdenin kendi ekvator yarıçapını girdi olarak kullanamaz.** Kullanırsa aradığı sonucu varsaymış olur. Deplasman yüzeyi, gövdenin henüz basılmamış — yani hacmi eşdeğer **ideal küre** — hâlinde nerede duruyorsa oradadır; politrop da zaten o küre üzerinde çözülür. İdeal kürenin yarıçapı hacim eşitliğinden tektir:
> $$R_{ort}=R_e\,(1-f)^{1/3}$$
> Satürn için $6{,}0268\times10^{7}\times0{,}96622=5{,}8232\times10^{7}$ m — tabloda kullanılan değerin ta kendisi. Zincir bu yüzden iki adımlıdır ve ikisi de türetilmiştir:
> $$\boxed{\;\frac{R_\phi}{R_e}=\underbrace{\frac{R_\phi}{R_{ort}}}_{\text{politrop, ideal küre}}\times\underbrace{(1-f)^{1/3}}_{\text{hacim eşdeğerliği}}\;}$$
> Satürn: $0{,}9356\times0{,}9662=0{,}9040$. **Serbest parametre yoktur**; $f$ ölçülmüş, politrop çözümü analitiktir. Doygun yüzeyli (karasal) bir gövdede $R_\phi/R_{ort}=1$ olduğundan çarpan $(1-f)^2$'ye iner — kural her iki sınıfta da aynıdır, yalnız birinci çarpan farklıdır.
>
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

> **Kapsam düzeltmesi — Blok D'nin $\phi\to1$ yasağı tikel kafeslere aittir.** Blok D şöyle der: *"$\phi\to1$ limiti fiziksel **değildir**; moleküler paketlenmenin geometrik üst sınırları $\phi$'yi 1'in belirgin altında tutar"* — ve özdeş kürelerin $\pi/\sqrt{18}=0{,}7405$ sınırını gösterir. **Bu argümanın kapsamı tikel, geçilmez birimlerdir.** Delokalize bir elektron gazı bir küre kümesi değildir; paketlenme sınırı ona uygulanamaz. Aynı biçimde M-39'un nötron maddesi kaydı ($\phi\approx0{,}7$–$0{,}9$, asimptotik) da tikel nükleonlar hakkındadır ve geçerlidir. *(Aynı kapsam kuralı (4)'ün su sistematiği için de geçerlidir: her iki genelleme de yalnız türetildikleri rejimde bağlayıcıdır.)*

> **Dürüst tuhaflık — kaydedilmeli.** Bu sonuç metalleri nötron maddesinden **daha** doygun yapar ($\to1$ ↔ $0{,}7$–$0{,}9$). Sezgiye aykırıdır ama tutarlıdır: deplasman kütleyle değil **yer** ile ölçeklenir (Fizeau'nun doğrudan ölçtüğü şey), ve bir elektron gazı tüm hacme yayılmış bir yapıdır; bir nötron yığınında ise geometrik boşluklar kalır. Teori burada yanlış olabilir — ve yanlışsa, aşağıdaki laboratuvar sınavı bunu gösterir.

> **Ayırt edici laboratuvar sınavı.** Kriter niceldir: ara bölge serbest-taşıyıcı yoğunluğu $n_c$ eşiği ($6{,}75\times10^{27}$ m⁻³) geçtiğinde $\phi$ paketlenme değerinden $1$'e doğru sıçramalıdır. Bu, **saydam bir iletkende Fizeau sürüklenme katsayısının $1-1/n^2$ değerini aşması** demektir. En iyi şeffaf iletken oksitler (ITO, ağır katkılı ZnO) $n_c\sim10^{27}$ m⁻³'e ulaşır — eşiğin **7 kat altında**, yani onlarda etki beklenmez ✓ (bu bir öngörü, sonradan uydurma değil). Eşiği aşan ve kızılötesinde saydam kalan bir dejenere yarıiletkende $f>1-1/n^2$ ölçülmelidir. **Yanlışlanma:** $n_c\gg10^{28}$ m⁻³'de bile $f=1-1/n^2$ çıkarsa, delokalizasyonun ara hacmi doldurduğu tezi düşer ve metalik $\phi$ paketlenme değerine geri iner.

#### Ve F5 bu belirsizlikten etkilenmez — bant çöküyor

Kalemin F5 üzerindeki asıl sonucu olumsuzlama değil, **karantinadır.** F5'in dış alanının sınır koşulu deplasman yüzeyinde kurulur (madde (4)) ve o yüzey **moleküler zarfın içindedir**:

| | Satürn'de yer | Basınç |
|---|---|---|
| **Deplasman yüzeyi $R_\phi$** | $0{,}935\,R_e$ | $\approx$ **0,035 Mbar** |
| Moleküler → metalik geçiş | $\approx0{,}55$–$0{,}65\,R_e$ | $\approx$ **1–2 Mbar** |

Aradaki basınç farkı **30–60 kattır.** $R_\phi$'de madde tartışmasız moleküler H₂/He akışkanıdır ve orada $\phi_{doy}=0{,}47$ sağlamdır. Metalik fazın $\phi$'si F5'in genliğine **hiç girmez.**

$$\boxed{\;\hat{\mathcal{Q}}_{et}^{Satürn} = 4{,}46\times10^{-5}\quad\text{— bant yok}\;}$$

Sınav 11.4-A'nın öngörüsü bu yüzden **tek değerlidir:** metalik fazın $\phi$ belirsizliği (11.4.1-(5)'in geniş bandı) genliğe hiç girmez, çünkü sınır koşulu $R_\phi$'de kurulur ve orası moleküler akışkandır. Kalan belirsizlik yalnız $\phi_{doy}$'un akışkan değerindedir ($0{,}47\pm0{,}03$, $\pm$%6).

> **Aynı karantina Dünya için de geçerlidir.** Dünya'nın Fe çekirdeği bir metaldir, dolayısıyla $\phi_{çekirdek}\to1$'dir (tabloda 166×). Bu, gövde-ortalamalı $\phi$'yi $0{,}68$'den $0{,}75$'e çıkarır. **Ama F5 gövde ortalamasını kullanmaz**; kullandığı nicelik $R_\phi$'deki değerdir ve Dünya'da $R_\phi=R_e$'dir (yüzey katı silikat). Dolayısıyla doğru değer **yüzey silikatınınkidir:**
> $$\phi_\oplus = \mathbf{0{,}70}\qquad(\text{kristal silikat; bant }0{,}64\text{–}0{,}74)$$
> Gövde ortalaması ($0{,}75$) F5 için yanlış niceliktir; kaynak okuması $R_\phi$'de yapılır. Bu değerle figür sınırı $\kappa_5\lesssim1{,}14$–$1{,}31\times10^{-2}$ (merkezî $1{,}20\times10^{-2}$), LLR düğüm sınırı $\kappa_5\lesssim2{,}1\times10^{-3}$, ve gözlemin sabitlediği çarpım $\kappa_5\phi\lesssim1{,}5\times10^{-3}$'tür. **Sınırın kendisi çarpım üzerinedir**, dolayısıyla $\phi_\oplus$'nin bandı ($0{,}64$–$0{,}74$) sınıra değil yalnız bölüşmeye taşınır.

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

**Denetim (11.2.5 ile).** 11.2.5'in korunan sonucu $a_{yanal}/a_{merkezkaç}=\kappa_5(\rho_0/\rho_n)\phi\cdot2\sin\theta$'dır. $a_{merkezkaç}=\omega^2R\cos\theta$ ve $a_r=\mathcal{G}M/R^2$ konularak iki ifade birebir örtüşür ($\mathcal{Q}=\omega^2R^3/\mathcal{G}M$ tanımıyla) ✓ Satürn için ($\kappa_5=2{,}1\times10^{-3}$, $\phi=0{,}47$, $\mathcal{S}=1{,}0508$, $\theta=45°$): oran $4{,}1\times10^{-5}$, yani $a_{yanal}=4{,}3\times10^{-4}$ m/s² — yüzey itiminin ($10{,}44$ m/s²) yüz binde dördü.

---

## 11.4.2 Radyal Yapı: F5 Bir Rankine Tepesidir · **[T]**

F5'in uzaysal yapısı iki ayrı ifadede özetlenir: **kutuplarda kuvvet yok olur**, ve **kütleden uzaklaşıldıkça önce artar sonra azalır.** İkisi de doğrudur, fakat farklı sebeplerden — ayrıştırılmaları gerekir, çünkü birincisi geometrik bir özdeşlik, ikincisi radyal profilin yapısıdır. Maksimumun yeri de tam olarak hesaplanabilir.

### (a) Kutupta sıfır — bu geometrik ve *tamdır*

$\sin2\theta$, $\theta=90°$'de tam sıfırdır. Bu bir yaklaşım veya küçüklük ifadesi değil, **özdeşliktir**: dönme ekseni üzerinde deplasman akışının enlemsel gradyanı yoktur, çünkü $v(\theta)=V\cos\theta$ profili orada durağan noktasına ulaşır. Aynı sıfır ekvatorda da ($\theta=0$) vardır — ama nitelikleri zıttır (M-39 kararlılık analizi):

- **Ekvator:** $f_{yanal}$ sıfır, türev **geri çağırıcı** ⟹ **kararlı denge**
- **Kutup:** $f_{yanal}$ sıfır, türev **iteleyici** ⟹ **kararsız denge**
- **45°:** $|\sin2\theta|=1$ ⟹ **maksimum ezme**

*"Kutupta yok"* ifadesi bu yüzden çift anlamlıdır ve ikisi de gereklidir: kuvvet orada sıfırdır **ve** madde orada barınamaz. Kutup, F5'in tek "temiz" noktasıdır (M-35 Varsayım 4 bu yüzden kutbu yalıtma noktası olarak kullanır).

### (b) Radyal profil — Rankine yapısı

Radyal davranış tümüyle $V(r)$'ye bağlıdır ve iki rejim vardır. Kritik nokta şudur: **gövdenin içinde ve dışında $V(r)$ zıt yönlü davranır.**

**İç kol — gövde maddesi (katı-cisim, $r\le R_\phi$).** Gövde katı cisim olarak döner; bu bir varsayım değil, katı cismin tanımıdır (M-39 Varsayım 2, R1):
$$V(r) = \omega r \quad\Longrightarrow\quad |f_{yanal}| = \kappa_5\phi_{doy}\rho_0\,\omega^2 r\,|\sin2\theta| \;\propto\; r$$
**Merkezden dışa doğru doğrusal olarak artar.** Merkezde tam sıfırdır ($V=0$).

**Dış kol — serbest alan ($r>R_\phi$).** Deplasman yüzeyinin dışında deplase edilen akış korunum yasasıyla seyrelir; $V(r)=\omega R_\phi(R_\phi/r)^{s}$ biçiminde yazılır ($s>0$, sönüm üssü):
$$|f_{yanal}| = \kappa_5\phi_{doy}\rho_0\,\frac{\omega^2R_\phi^2}{r}\left(\frac{R_\phi}{r}\right)^{2s}|\sin2\theta| \;\propto\; r^{-(2s+1)}$$
**Dışa doğru hızla azalır.**

$$\boxed{\;|f_{yanal}|\propto r \;\;(r<R_\phi) \qquad\qquad |f_{yanal}|\propto r^{-(2s+1)} \;\;(r>R_\phi) \qquad\Longrightarrow\qquad \text{maksimum } r=R_\phi \text{'de}\;}$$

**Sonuç.** F5 kuvvet yoğunluğu **deplasman yüzeyinde maksimumdur**; içeride $+1$ eğimle yükselir, dışarıda $-(2s+1)$ eğimle düşer. "Önce artar sonra azalır" davranışı böylece türetilmiş olur ve tepe noktası **serbest parametre içermez** — 11.4.1-(4)'te iç yoğunluk profilinden türetilir: karasal cisimlerde $R_\phi\simeq R_e$, Satürn'de $0{,}904\,R_e$, Jüpiter'de $0{,}944\,R_e$.

### (c) Maksimumun geometrisi: bir tepe *noktası* değil, iki **halka sırtı**

$|f_{yanal}|$ hem $r$'de hem $\theta$'da maksimumlanır. İki koşul birlikte alındığında maksimum kümesi:

$$r=R_\phi,\qquad \theta=\pm45°$$

yani gövdenin çevresinde, kuzey ve güney orta enlemlerde **iki eş merkezli halka**. F5 alanının en şiddetli olduğu yer ne kutup, ne ekvator, ne merkez — **45° enlem çemberidir.** Satürn için bu sırttaki değer ($R_\phi=0{,}904R_e$, $\omega R_\phi=9\,004$ m/s, $\phi_{doy}=0{,}47$, referans $\kappa_5=2{,}1\times10^{-3}$):

$$|f_{yanal}|_{max} = \kappa_5\phi_{doy}\rho_0\,\omega^2R_\phi = 9{,}91\times10^{13}\ \mathrm{N/m^3} \qquad(a_{yanal}=3{,}67\times10^{-4}\ \mathrm{m/s^2})$$

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

*Şekil 11.4.1: F5'in radyal profili bir Rankine yapısıdır. İç kolda kaynağın katı-cisim dönüşü ($V=\omega r$), dış kolda korunumlu seyrelme ($V\propto r^{-s}$). Tepe, deplasman yüzeyi $R_\phi$'de — serbest parametresiz, iç yoğunluk profilinden türetilir (11.4.1-(4)). Satürn için $R_\phi=0{,}904\,R_e$; karasal cisimlerde $R_\phi\simeq R_e$.*

> **Bu M-30'un Rankine profilinin F5 karşılığıdır.** M-30 vorteks *hızı* için aynı yapıyı verir (iç çekirdek $v\propto R$, dış kol $v\propto1/R$). Buradaki ek adım, aynı yapının **enlemsel kuvvet yoğunluğuna** taşınmasıdır: F5, kaynağın Rankine profilini karesiyle ve bir ek $1/r$ metrik çarpanıyla miras alır.

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

Ay için $r=60{,}27\,R_\oplus$, $n=4813°$/yıl, $\mathcal{Q}_\oplus=3{,}461\times10^{-3}$, $\mathcal{S}=1{,}0017$, $R_\phi=R_e$, $\phi_\oplus=0{,}70$ (11.4.1-(4)–(5)'ten türetildi — yüzey kristal silikatı). Üç aday $\kappa_5$'te doğrusaldır, dolayısıyla eleme **$\kappa_5$'ten bağımsız** yapılabilir: her aday, LLR'nin düğüm artığını ($\lesssim0{,}1$ mas/yıl) aşmamak için bir $\kappa_5$ tavanı dayatır.

| Aday | $\mathcal{F}_5(\text{Ay})/\kappa_5$ | Öngörü$/\kappa_5$ | LLR artığının izin verdiği $\kappa_5$ | Hüküm |
|---|---|---|---|---|
| **(B)** R2 | $2{,}0$ | $4{,}8\times10^{3}$ °/yıl | $\lesssim6\times10^{-12}$ | ✗ **DIŞLANDI** |
| **(A1)** $s=1$ | $1{,}95\times10^{-5}$ | $1{,}7\times10^{2}$ ″/yıl | $\lesssim6\times10^{-7}$ | ✗ **DIŞLANDI** |
| **(A2)** $s=2$ | $5{,}5\times10^{-9}$ | $48$ mas/yıl | $\lesssim\mathbf{2{,}1\times10^{-3}}$ | ✓ **AYAKTA** |

**Eleme mantığı.** (B) ve (A1) doğru olsaydı $\kappa_5$ sırasıyla $10^{-12}$ ve $10^{-7}$ mertebesinde olmak zorunda kalırdı — figür sınırının ($\lesssim1{,}3\times10^{-2}$) dokuz ve dört mertebe altında. O büyüklükte bir kuplaj F5'i kitabın **her** kanalında görünmez kılar: halka frekansında, Laplace yüzeyinde, galaktik levhada, hiçbir yerde ölçülebilir bir iz bırakmaz. **$s=2$, F5'in fiziksel olarak sonuç doğuran bir kuvvet kalabildiği tek üstür.** *(Bu bir çürütme değil, bir tutarlılık argümanıdır ve öyle etiketlenmiştir; bağımsız desteği aşağıdaki Laplace yarıçapları verir.)*

$$\boxed{\;s=2\;:\quad V(r)=\omega R_\phi\left(\frac{R_\phi}{r}\right)^{2},\qquad |f_{yanal}|\propto r^{-5},\qquad \mathcal{F}_5\propto\left(\frac{R_e}{r}\right)^{3}\;}$$

> **Bu, M-38'in Ay sınavının ikizidir — ve simetrisi kayda değer.** M-38'de Ay'ın **apsidal** presesyonu F4'ün $1/R$ rejimini yalıtılmış gezegenlerde iptal etmiş ve *disk koşulunu* zorunlu kılmıştı. Burada Ay'ın **düğüm** gerilemesi F5'in dış alan sönüm üssünü sabitliyor. **F4 apsisle, F5 düğümle kısıtlanır** — ikisi de aynı gövde tarafından, ikisi de aynı veri kümesiyle (LLR). Bu tesadüf değildir: F4 yörünge düzlemi *içinde*, F5 düzleme *dik* çalışır; Ay yörüngesinin iki bağımsız açısal elementi bu yüzden iki kuvvetin doğal ölçüm kanallarıdır.

**Ve seçilen üs teorinin kendi geometrisidir.** $s=2$, ortamın açısal hızının $\Omega_{ortam}\propto r^{-3}$ ile düşmesi demektir — bu **tam olarak M-40'ın dipolar çerçeve-sürüklenme alanıdır** (GP-B kanalı). Yani F5'in dış alanı, M-40'ın alanıyla aynı radyal biçimi paylaşır; ikisi bağımsız kanallar olmakla birlikte ($\phi$ ↔ $\xi$, M-39'un kanal kaydı) aynı dış geometriye oturur. Sönüm üssü artık **[T]** statüsündedir, seçim gözlemseldir.

> **Bağımsız destek — Laplace yarıçapları.** $s=1$ olsaydı F5, $J_2$'nin çokkutbundan **daha yavaş** ($r^{-4}$ ↔ $r^{-5}$) düşerdi ve dış bölgede $J_2$'yi geçerdi. Sonucu hesaplanabilir: bütün Laplace yarıçapları büyürdü — Dünya $8{,}41\to8{,}54$ ($+1{,}6\%$), Jüpiter $28{,}3\to30{,}6$ ($+8{,}2\%$), Satürn $36{,}3\to41{,}8$ ($+15{,}4\%$), Uranüs $46{,}1\to54{,}0$ ($+17{,}1\%$), Neptün $63{,}8\to76{,}4$ ($+19{,}9\%$) $R_e$. Düzenli/düzensiz uydu sınırı bu yarıçaplarla belirlenir ve gözlenen sınırlar $J_2$-tabanlı değerlerle uyumludur; %8–20'lik kaymalar için yer yoktur. $s=2$'de F5 $r^{-6}$ ile düşer ve Laplace yüzeyinde **hiçbir** iz bırakmaz (Satürn'ün $r_L$'sinde F5/güneş-gelgiti $=7\times10^{-4}$) ✓ İki bağımsız gözlem — Ay'ın düğümü ve uydu sınırları — aynı üssü seçer.

**$\kappa_5$ üzerine yeni sınır.** Ay'ın düğüm artığı $0{,}1$ mas/yıl düzeyinde sınırlanırsa:

$$\boxed{\;\kappa_5 \lesssim 2{,}1\times10^{-3}\;}\qquad\text{(LLR düğümü, } s=2,\ \phi_\oplus=0{,}70)$$

Bu, Sınav 1'in figür sınırından ($\lesssim1{,}14$–$1{,}31\times10^{-2}$) **5–6 kat sıkıdır** ve kitaptaki en güçlü $\kappa_5$ kısıtıdır; galaktik kanal (11.4.9) daha gevşek kalır, yani **bağlayıcı sınır budur.** $1$ mas/yıl toleransla $2{,}1\times10^{-2}$'ye gevşer.

> **Bölümün referans değeri.** Bundan sonraki bütün genlikler $\kappa_5=2{,}1\times10^{-3}$ ile verilmiştir — gözlemin izin verdiği **en büyük** değer. Dolayısıyla her sayı bir **üst sınırdır**: teori "en fazla bunu görürsünüz" der. Bütün büyüklükler $\kappa_5$'te doğrusal olduğu için sınır ileride sıkışırsa aynı oranda ölçeklenirler.

> **Gözlemin sabitlediği nicelik $\kappa_5$ değil, $\kappa_5\phi$ çarpımıdır.** 11.4.1-(4) $\phi$'yi bağımsızca türettiği için bölüşme artık yapılabilir; ama sınırın kendisi çarpım üzerinedir: $\kappa_5\phi \lesssim 1{,}5\times10^{-3}$. $\phi$'nin metalik-faz belirsizliği (11.4.1-(4)'ün bandı) doğrudan buraya taşınır — üst uçtaki ($\phi\to0{,}86$) bir metalik hidrojen okuması Satürn tarafındaki bütün genlikleri 1,8 kat büyütür, Dünya tarafını (dolayısıyla sınırı) değiştirmez.

---

## 11.4.4 Halka Dikey Salınımı ve F5'in Taklit Edilemez İmzası · **[T]**

### Dikey salınım denklemi

Ekvatoral kararlı denge çevresinde ($z\ll r$) $\sin2\theta\simeq2z/r$ konulur. Toplam dikey geri çağırma, Kepler'in kendi payı + $J_2$ çokkutbu + F5'tir:

$$\ddot z = -\nu^2 z,\qquad \boxed{\;\frac{\nu^2}{\Omega^2} = 1 \;+\; \underbrace{3J_2\!\left(\frac{R_e}{r}\right)^{\!2}}_{\text{figür (madde kanalı)}} \;+\; \underbrace{\hat{\mathcal{Q}}_{et}\!\left(\frac{R_e}{r}\right)^{\!3}}_{\text{F5 (ortam kanalı)}} \;+\;\cdots\;}$$

$$\hat{\mathcal{Q}}_{et}\;=\;\frac{\kappa_5\,\phi_{doy}\,\mathcal{S}}{2}\,\mathcal{Q}\left(\frac{R_\phi}{R_e}\right)^{\!6}\;=\;4{,}46\times10^{-5}\quad(\text{Satürn})$$

$\nu$ dikey (bending) frekansı, $\Omega$ yörünge frekansıdır. **Halka tanecikleri bu frekansta yukarı-aşağı harmonik salınım yapar** ve kararlı düzlem $z=0$'dır.

### İmza: radyal üs **tek** sayıdır — ve bu imkânsızdır

Kuzey-güney simetrik bir gövdenin kütle çokkutbu alanında $\nu^2/\Omega^2$ açılımı **yalnız çift** $(R_e/r)^{2n}$ üsleri içerir: $J_2\to(R_e/r)^2$, $J_4\to(R_e/r)^4$, $J_6\to(R_e/r)^6$. Tek üsler yasaktır — çünkü tek dereceli zonal harmonikler ($J_3$, $J_5$) ekvatora göre asimetri gerektirir ve dönel simetrik hidrostatik gövdede sıfırdır.

$$\boxed{\;\text{F5, } \nu^2/\Omega^2\text{'ye } (R_e/r)^{3}\text{ ile girer — TEK bir üsle.}\;}$$

> [!IMPORTANT]
> **Bu, F5'in kitapta bulunmuş ilk taklit edilemez imzasıdır.** Sınav 1 (6.6.2) F5'in figürde saf $P_2$ olduğunu ve merkezkaçla **dejenere** olduğunu göstermişti — ölçülemez. Dış alanda dejenerasyon **kırılır**: F5'in radyal üssü hiçbir kütle çokkutbunun üretemeyeceği bir paritededir. Bir kuvvetin *çürütülmesi* ile *gözlemsel içeriğinin olmaması* farklı şeylerdir (M-39'un kaydı); burada üçüncü bir durum doğar: **F5 ölçülebilir hâle gelir.**

Halka sismolojisi (kronosismoloji) $\nu(r)$'yi Satürn halkalarındaki bükülme dalgalarından (bending waves) ve düğüm rezonanslarından okur; $J_2$, $J_4$, $J_6$ bu yolla bağımsızca çıkarılır ve Cassini Grand Finale çekim verisiyle karşılaştırılır. Yalnız çift üslerle yapılan bir uyumlama, F5 varsa **sistematik ve radyal olarak yapılandırılmış** bir artık bırakmak zorundadır.

### Nicel öngörü: Satürn halka kuşağı

$\kappa_5=2{,}1\times10^{-3}$, $\phi_{doy}=0{,}47$, $\mathcal{S}=1{,}0508$, $\mathcal{Q}_S=0{,}1576$, $(R_\phi/R_e)^6=0{,}546$ ile:

| Bölge | $r/R_e$ | $\mathcal{F}_5$ | $\delta\nu/\nu$ | $J_2$ terimi | **F5 payı** |
|---|---|---|---|---|---|
| D halkası (iç) | 1,110 | $3{,}26\times10^{-5}$ | $1{,}63\times10^{-5}$ | $3{,}97\times10^{-2}$ | **%0,082** |
| C halkası (iç) | 1,239 | $2{,}34\times10^{-5}$ | $1{,}17\times10^{-5}$ | $3{,}18\times10^{-2}$ | **%0,074** |
| B halkası (iç) | 1,527 | $1{,}25\times10^{-5}$ | $6{,}26\times10^{-6}$ | $2{,}10\times10^{-2}$ | **%0,060** |
| B/A orta | 1,750 | $8{,}32\times10^{-6}$ | $4{,}16\times10^{-6}$ | $1{,}60\times10^{-2}$ | **%0,052** |
| A halkası (dış) | 2,269 | $3{,}82\times10^{-6}$ | $1{,}91\times10^{-6}$ | $9{,}49\times10^{-3}$ | **%0,040** |
| F halkası | 2,326 | $3{,}54\times10^{-6}$ | $1{,}77\times10^{-6}$ | $9{,}03\times10^{-3}$ | **%0,039** |

**Üç okuma:**

1. **Düzlem-kilitleme bütçesinin tamamı tek köktendir — ve o kök teorinindir.** Dikey geri çağırmanın figür payı ($J_2$) ile F5 payı iki ayrı fizik değildir: $J_2$, gövde dönüşünün kütle dağılımına **çökelmiş fosilidir** (11.2.6), F5 aynı dönüşün ortamda **hâlâ canlı** olan kalanıdır. Standart fizik fosili veri olarak alır ve canlı alanı tanımaz; teori ikisini tek kökten türetir ve oranlarını öngörür ($\mathcal{Q}/J_2$, 11.4.6). Halkayı düzleme bastıran bütçe bu iki kanalın toplamıdır — **yani bütünüyle dönüş-deplasman fiziğinindir.**
2. **Canlı payın fosile oranı halka kuşağında %0,04–0,08'dir ve radyal olarak yapılandırılmıştır:** pay $(R_e/r)$ ile **içe doğru artar** — D halkasında A halkasının iki katı. En güçlü sinyal en iç halkalarda beklenir.
3. **Mutlak büyüklük $\delta\nu/\nu = 1{,}8\times10^{-6}$–$1{,}6\times10^{-5}$**'tür. Bükülme dalgası rezonans konumları Satürn halkalarında km mertebesinde ölçülür ($\delta r/r\sim10^{-5}$); iç halkalardaki kayma bu hassasiyetin üstündedir — sınav yürütülebilir durumdadır ve ölçüm C–D halkalarına ağırlık vermelidir.

### Sınav protokolü (yürütülmeyi bekliyor)

> **Sınav 11.4-A · Halka bükülme dalgalarında tek-parite artığı.**
> **Yöntem:** Satürn'ün ölçülü bükülme-dalgası ve düğüm-rezonans yarıçapları, (i) yalnız çift üsler ($J_2,J_4,J_6,J_8$) ve (ii) çift üsler + tek bir $(R_e/r)^3$ terimi ile uyumlanır. İkinci uyumlamanın $\chi^2$ kazancı ve $(R_e/r)^3$ katsayısının işareti okunur.
> **Öngörü:** Katsayı **pozitif** olmalıdır (F5 dikey geri çağırmayı *artırır*, düzlemi sıkılaştırır) ve değeri $\hat{\mathcal{Q}}_{et} = \mathbf{4{,}5\times10^{-5}}$ (referans üst sınır $\kappa_5=2{,}1\times10^{-3}$ ile; bant yok — metalik-faz belirsizliği 11.4.1-(5)'te karantinaya alındı) civarında çıkmalıdır.
> **Yanlışlanma:** Negatif katsayı veya $\lesssim10^{-5}$ üst sınır. İkinci durumda $\kappa_5\lesssim4\times10^{-4}$ olur ve F5 gözlemsel olarak tamamen susar.
> **Neden sadece Satürn:** Bükülme dalgalarını çözecek optik derinlikte ve genişlikte halka yalnız Satürn'de vardır (11.4.6).

---

## 11.4.5 Halkanın İnceliği ve Dikey Sönüm: Düzlemi F5 Kurar, Salınımı Halkanın Kendi Rampası Söndürür · **[T]**

11.4.4 dikey salınımın **frekansını** verdi: düzlemden saptırılan tanecik $\nu$ frekansıyla geri çağrılır ve kararlı düzlem $z=0$'dır. Bu bölüm kalan iki soruyu cevaplar: salınımın **genliğini ne söndürür**, ve halkanın **kalınlığını ne kilitler?** Teorinin cevabı iki kalemdir; ikisi de teorinin kendi denklemlerinden çıkar ve halkayı ikisi birlikte **kurar:**

1. **Düzlemi ve geri çağırmayı F5 kurar.** Doğrudan payı, ortamda hâlâ canlı olan deplasman alanıdır; dolaylı payı, aynı dönüşün maddeye çökelmiş fosili olan figürdür ($J_2$, 11.2.6). İki kanal tek köktendir ve bölüşümleri bu bölümün sonunda verilir.
2. **Salınımı halkanın kendi Evrenakı rampası sönümler.** Her kütle, nükleonlarının $\omega_2$ pulsasyonuyla çevresinde bir deplasman rampası taşır. Halka taneciği çıplak küre değildir: iki tanecik birbirine **değmeden önce rampaları buluşur**, ve dikey hareketin momentumu alan aracılığıyla halkanın ortak dolaşımına aktarılır. Temaslı çarpışma bu zincirin yalnız **son adımıdır** — artığı ısıya çevirir. Etkendir; ama ana etken değildir, çünkü karşılaşmanın **kapısı, kesiti ve seçiciliği rampanındır.** Bu hiyerarşi aşağıda sayıyla kurulur.

### Önce iki rampayı ayırmak gerekir — karıştırılırlarsa hesap bozulur

Kitapta "rampa" adı iki farklı yapıya verilir; kaynakları, ölçekleri ve işleri ayrıdır:

| | **Elektron rampası** | **Pulsasyon rampası** |
|---|---|---|
| Kaynak | Yüzeydeki elektronların dolanımı | Nükleonların $\omega_2$ nefes alması |
| Konum | Madde **yüzeyine yapışık** | Gövdeyi **kuşatan** hacim |
| Kalınlık | $\lesssim0{,}1$ mm — **maddeye bağlı** | $r=\sqrt{\mathcal{G}m/a_{d\imath\c{s}}}$ — **dış gradyana bağlı** |
| İşi | **Optik**: yansıma (2.6), Malus soğurması (2.9), "hidrodinamik kalkan" (1.6) | **Dinamik**: kütle-itim yakın alanı, karşılaşma kesiti |

**Ve hangisinin büyük olduğu ortama göre değişir** — çünkü elektron rampası sabit, pulsasyon rampası dış gradyanla ölçeklenir:

| Ortam | Elektron rampası | Pulsasyon rampası | Baskın |
|---|---|---|---|
| Yeryüzünde 1 kg cisim | $10^{-4}$ m | $2{,}6\ \mu$m | elektron |
| Yeryüzünde 1 ton cisim | $10^{-4}$ m | $82\ \mu$m | elektron |
| Satürn halka taneciği ($a_b=10$ m) | $10^{-4}$ m | **$17$ m** | **pulsasyon** |

Yeryüzünde pulsasyon rampası mikron mertebesindedir ve iki cisim daima **elektron rampalarından** değer — sıradan temas mekaniğinin bozulmamasının sebebi budur. Halka taneciğinde sıralama tersine döner: pulsasyon rampası elektron rampasının **beş mertebe** üstündedir. **Halka, pulsasyon rampasının hâkim olduğu rejimdedir.** Aşağıdaki bütün hesap pulsasyon rampasınadır; elektron rampasının payı $10^{-4}/10=10^{-5}$'tir ve tümüyle ihmal edilir.

### Pulsasyon rampasının erimi serbest değildir — türetilir

Rampa, cismin kendi pulsasyon akışının ortamı belirlediği bölgedir; sınırı, kendi kütle-itim ivmesinin dış ivmeye yenildiği yerdir:

$$\boxed{\;\frac{\mathcal{G}m}{r^2}=a_{d\imath\c{s}} \qquad\Longrightarrow\qquad r_{puls}=\sqrt{\frac{\mathcal{G}m}{a_{d\imath\c{s}}}}\;}$$

Bu, **11.4.8.1'in zarf erimi için kullandığı ölçütün aynısıdır** (gradyan hâkimiyeti) — tek ölçüt, her ölçekte. Yörünge ortamında $a_{d\imath\c{s}}$ gelgit gradyanıdır ($3\mathcal{G}M r/R_{y\ddot{o}r}^3$) ve bağıntı Hill biçimine iner:

$$r_H = R_{y\ddot{o}r}\left(\frac{m}{3M}\right)^{1/3},\qquad m=\tfrac43\pi a_b^3\rho_c \quad\Longrightarrow\quad \boxed{\;\frac{r_H}{a_b}=R_{y\ddot{o}r}\left(\frac{4\pi\rho_c}{9M}\right)^{1/3}\;}$$

**$a_b$ sadeleşir: oran tanecik boyundan bağımsızdır.** Yalnız yörünge yarıçapına ve tanecik yoğunluğuna bağlıdır — ikisi de ölçülü. Satürn halkasında buz için ($\rho_c=900$ kg/m³):

| Bölge | $r$ (km) | $r_H/a_b$ | Kesit çarpanı $(r_H/a_b)^2$ |
|---|---|---|---|
| C halkası | 80 000 | 1,04 | **1,09** |
| B halkası (iç) | 92 000 | 1,20 | **1,44** |
| Mimas 5:3 (A) | 131 900 | 1,72 | **2,96** |
| A halkası dışı | 137 000 | 1,79 | **3,19** |

> **Kesit çarpanı iki rampanın toplamıdır.** Etkileşim, iki rampa değdiğinde başlar: ayrılık $2r_H$, çıplak temasta $2a_b$. Oran $(2r_H/2a_b)^2=(r_H/a_b)^2$ — yani tablodaki çarpan zaten **iki rampalıdır**, ayrıca ikiye katlanmaz.

**Ve pulsasyon rampası izotropiktir.** Nefes alan bir pompanın yönü yoktur, akış radyaldir; rampanın düşey ve düzlem-içi kesiti **aynıdır.** *(1.5'te elektron rampası için söylenen "birlikte döner" ifadesi o rampaya özgüdür ve pulsasyon rampasına taşınmaz.)*

> **Nicel dejenerasyon, kavramsal ayrım.** $r_{puls}$'un yörünge ortamındaki değeri, standart fiziğin **Hill yarıçapıyla** sayı sayıya aynıdır — o rejimde M-35 Newton'a kalibreli olduğu için bu zorunluluktur, tesadüf değil. Teoriye ait olan üç şeydir: **kaynak** (rampa $\omega_2$ pulsasyonundan doğar), **izotropi** (yönsüzdür — aşağıdaki seçicilik hesabı ve Sınav 11.4-H buna bağlıdır), ve **tek ölçüt, her ölçek** (gradyan hâkimiyeti: tanecikte $1{,}0$–$1{,}8\,a_b$, gezegen zarfında $10^3\,R$; 11.4.8.1).

### Tek tanecikte rampa, tabakada kuyu: halkanın ortak rampası

Düzlemde toplanan taneciklerin rampaları tek tek son bulmaz; tabaka ölçeğinde **üst üste biner** ve ortamda düzlem boyunca ortak bir seyrelme kurar. Seyrelme bir kuyudur; kuyu dikey geri çağırma verir. Bu, halkanın kendi maddesinin pulsasyon deplasmanından doğan **ortak Evrenakı rampasıdır** — salınan taneciği düzleme geri çağıran ve sönümün içinde çalıştığı yapı budur.

Yüzey yoğunluğu $\Sigma$, kalınlığı $h$ olan tabakada hacim yoğunluğu $\rho=\Sigma/h$'tir ve düzlemde deplase edilen ortam kesri:

$$\frac{\Delta\rho_0}{\rho_0}\;=\;\frac{\rho}{\rho_c}\,\phi_{buz} \qquad(\phi_{buz}\approx0{,}5\text{–}0{,}7;\ \rho_c\approx900\ \mathrm{kg/m^3})$$

Bu seyrelmenin kurduğu dikey frekans, tabakanın kendi kütle-itim kuyusudur:

$$\boxed{\;\nu_{kol}=\sqrt{4\pi\mathcal{G}\rho}\;=\;\sqrt{4\pi\mathcal{G}\,\Sigma/h}\;}$$

**Sayılar — terim birinci mertebedir:**

| Halka | $\Sigma$ (kg/m², yoğunluk dalgalarından) | $\rho$ ($h=10$ m) | deplase ortam | $\nu_{kol}$ (s⁻¹) | $\Omega$ (s⁻¹) | **$\nu_{kol}/\Omega$** |
|---|---|---|---|---|---|---|
| **A** (Mimas 5:3, $r=2{,}19R_e$) | $\approx370$ | 37 | %2,5 | $1{,}76\times10^{-4}$ | $1{,}286\times10^{-4}$ | **1,37** |
| **B** (iç, $r=1{,}53R_e$) | $\approx400$ *(bant 400–1400)* | 40 | %2,7 | $1{,}83\times10^{-4}$ | $2{,}207\times10^{-4}$ | **0,83** *(bant 0,83–1,55)* |

**Ortak rampanın kuyusu, A halkasında gezegenin dikey zorlamasını aşar (1,37 katı); B'de en az %83'ü kadardır.** Frekanslar dikey yönde toplandığında ($\nu^2=\Omega^2+\nu_{kol}^2$): A'da $\nu/\Omega=1{,}70$ ($h$ düzeltmesi $-\%41$), B'de $1{,}30$ ($-\%23$). Halkanın dikey dinamiği, kendi rampasının kuyusu hesaba katılmadan yazılamaz.

> [!WARNING]
> **Süreklilik sınırı — düzgün-levha değeri tavandır.** $\nu_{kol}$ halkayı düzgün bir levha sayar; gerçek yapı metre ölçeğinde 1–3 tanecik katmanı kalınlığında ve **öbeklidir** (Cassini'nin ölçtüğü öz-çekim izleri). Terim **vardır ve birinci mertebedir**, ama tablodaki düzeltmeler öbeklenme hesaba katıldığında bir miktar küçülür.

**Kuyu derinleştikçe genlik sıkışır.** $\rho=\Sigma/h$ olduğu için kuyu, tabaka inceldikçe **derinleşir**; adyabatik değişmezle ($E/\nu=$ sabit) salınım genliği $z_{maks}\propto\nu^{-1/2}$: oturma → daha derin kuyu → daha küçük genlik → daha çok oturma. Ortak rampa, sönümün sonucunu geri besleyerek hızlandırır.

> **Kapsam — bileşim öngörüsü kurulamaz · [T].** Akla gelen ek adım — *"deplasman hacimle ölçeklendiğine göre pay $\propto\phi/\rho_c$ olmalı ve eşit $\Sigma$'da buzlu halka kayaçtan ince çıkmalı"* — **kurulamaz, ve gerekçesi teorinin temelindedir.** $\phi$ bir **kaynak** terimidir, tepki terimi değil: kuvvet M-2 ile nükleon başına işler, $a=-\nabla P/\rho_n$. Tepki $\phi/\rho_c$ üzerinden kurulsaydı serbest düşüş bileşime bağlı olurdu — MICROSCOPE'un test çifti için $\eta_{E\ddot{o}tv\ddot{o}s}\approx1{,}3$ çıkardı; ölçülen $|\eta|<1{,}5\times10^{-15}$, **on beş mertebe farkla dışlanır.** M-2'nin $\rho_n$'si bir tercih değil, teorinin Eötvös sınavını geçme şartıdır. Bileşime bağlı halka kalınlığı öngörüsü teoriye ait değildir ve ileri sürülmez. *(Kalınlığın $\Sigma$'ya bağlılığı bundan etkilenmez: o, kütle-itim kuyusunun kendisidir ve evrenseldir.)*

### Sönümün mekanizması: rampa kanalı · **[T]** · ⭐ ana kanal

Zincir dört halkadır ve her halkası sayıyla kuruludur.

**(i) Karşılaşmanın kapısı istisnasız rampadır.** Salınan tanecik düzlemi her periyotta iki kez keser; her geçiş, komşularının rampalarıyla **alan aracılı** bir karşılaşmadır. Kesit çıplak kesitin $(r_H/a_b)^2=1{,}1$–$3{,}2$ katıdır ve yarıçapla büyür. İki yüzeyin fiilen değmesi, ancak rampalar momentumu zaten aktarmışken gerçekleşen ender kuyruktur: standart fiziğin "çarpışma" diye tek kalemde saydığı olay, teoride **rampa karşılaşması + seyrek temas artığıdır.**

**(ii) Rampa karşılaşması dikey modu boşaltır.** Karşılaşma esnektir — enerji yutmaz; ama **pay değiştirir**: momentum ve açısal momentum taşır, dikey (düzensiz) hareketi düzlem içi ortak dolaşıma dağıtır. Koheran bir dikey mod — saptırılmış bir tanecik, bir bükülme dalgası — bu aktarımla halkaya yayılır ve söner. Kitabın adlandırmasıyla bu, **kütle-itimsel (temassız) karşılaşma** kanalıdır.

**(iii) Gözlem bu kanalı doğrudan görüyor.** Bükülme dalgalarının sönüm viskozitesi, aynı bölgenin yoğunluk dalgalarınınkinden **2,22 kat büyüktür** (Mimas 5:3: $\nu=576$ ↔ $260$ cm²/s). Çıplak-küre çarpışma resmi bu fazlalığı öngörmez; rampa kesitinin yarıçapla büyümesi ve dengenin anizotropisi öngörür (aşağıda, Sınav 11.4-H). **Dikey sönümdeki fazlalık, rampa kanalının gözlemdeki imzasıdır.**

**(iv) Temas kanalı artığı yakar.** Buz esnek değildir ($\varepsilon\approx0{,}1$–$0{,}6$; her temasta bağıl kinetik enerjinin $1-\varepsilon^2\simeq0{,}64$'ü ısıya gider). Rampaların dağıttığı hareketin artığı bu temaslarda ısıya döner ve uzaya atılır. **İş bölümü nettir: rampa dağıtır ve boşaltır; temas yakar.**

**Bilanço iki işaretlidir ve bir termostat kurar.** Rampa kanalı yalnız boşaltmaz; Kepler kaymasının düzenli deposundan da beslenir — komşu yörüngeler arasındaki kayma, rampa aracılığıyla rastgele harekete sızar ve bir **taban** koyar: bir taneciğin dikey hızı, kendi rampa yarıçapı boyunca kaymanın altına inemez —

$$\boxed{\;\sigma_z \simeq \Omega\,r_H\;}$$

— inseydi kayma onu hemen o değere geri getirirdi. Temas kanalı fazlayı yakar; denge $h$'ı belirler. Halka kalınlığı bir sönüm *sonu* değil, **termostattır**: salınım ölmez ($\sigma_z$ asla sıfırlanmaz, kayma deposu tükenmez), ama şiddetlenmez de — dengeye oturur. Sayılar: $\sigma_z\simeq1{,}7$ mm/s, dikey periyot $2\pi/\nu\simeq8$ saat (A halkası), genlik $\sigma_z/\nu\simeq8$ m; karşılaşma sıklığı yörünge başına birkaç olaydır ($\sim1{,}2$ saat). Bu, Güneş Sistemi'nin en uysal salınımlarından biridir — ve uysallığını rampa termostatına borçludur.

| # | Kanal | Mekanizma | Enerji hanesi | Rolü |
|---|---|---|---|---|
| **1** | **Rampa** *(kütle-itimsel, temassız)* | alan aracılı momentum/açısal momentum aktarımı; kesit $(r_H/a_b)^2$ | esnek — dağıtır: dikey modu boşaltır, kaymadan tabanı besler | **ana kanal** — sönümün kapısı, kesiti ve seçiciliği |
| **2** | Temas *(kütlesel çarpışma)* | $\varepsilon<1$, inelastik | soğutucu — tek yönlü | ikincil — rampanın bıraktığı artığı ısıya çevirir |
| **3** | Ortam artık kuplajı $\gamma_{ortam}$ | M-43, $\Delta v^4$ | soğutucu | dikey payı $5\times10^{-10}$ — hiç (aşağıda) |

### Kuvvet ile yitimin iş bölümü — teorinin tezi iki bacağıyla tamdır

$$h \simeq \frac{\sigma_z}{\nu}\qquad\Longrightarrow\qquad \underbrace{\nu}_{\text{kuvvetlerin işi}}\ \text{ile}\ \underbrace{\sigma_z}_{\text{yitim zincirinin işi}}\ \text{ayrı hanelerdir.}$$

F5'in bir **potansiyeli** vardır — teorinin kendi denklemlerinden çıkar: $\Psi_5=(\kappa_5\phi/4)V^2\sin^2\theta$. Potansiyeli olan kuvvet **korunumludur** ve tek başına genlik söndürmez; aynı şey Kepler'in dikey geri çağırması, $J_2$ ve ortak rampanın kuyusu için de geçerlidir. Bu bir zayıflık değil, iş bölümüdür: **kuvvetler "hangi düzlem" ve "hangi frekans" sorularını cevaplar; genliği söndürmek yitimin işidir — ve teorinin yitim zinciri yukarıda kuruldu: kapı rampa, ocak temas.** Düzlemi F5 seçer, salınımı rampa kanalı boşaltır; halkayı bu ikili kurar. Standart fizik bu tabloda yalnız temas kanalını ve figür fosilini görür; kapıyı ve dümeni görmez.

### Parametresiz kalınlık: halka bir tanecik çapındadır · **[T]** · ⭐

Taban ile kuyu birleştirilirse kalınlık serbest parametresiz çözülür. Önce çıplak-küre biçimi yazılır ($\sigma_z\simeq\Omega a_b$); $h=\sigma_z/\nu$ ve $\nu^2=\Omega^2+\nu_{kol}^2$ ile:

$$h^2\Omega^2+4\pi\mathcal{G}\Sigma\,h=\Omega^2a_b^2 \qquad\Longrightarrow\qquad \boxed{\;\frac{h}{a_b}=\sqrt{1+\Lambda^2}-\Lambda,\qquad \Lambda\equiv\frac{2\pi\mathcal{G}\Sigma}{\Omega^2a_b}\;}$$

**Sağ tarafta yalnız gözlenen büyüklükler vardır:** yüzey yoğunluğu $\Sigma$ (yoğunluk dalgalarından), yörünge frekansı $\Omega$ (yarıçaptan), tanecik boyu $a_b$ (örtülme boyut dağılımından). **Serbest parametre yoktur; $\kappa_5$ girmez, ayarlanacak hiçbir kol kalmaz.**

| Halka | $\Sigma$ (kg/m²) | $a_b=1$ m | $a_b=5$ m | $a_b=10$ m |
|---|---|---|---|---|
| **C** | $\approx50$ | $h/a_b=0{,}76$ | $0{,}94$ | $0{,}97$ |
| **A** (Mimas 5:3) | $\approx370$ | $\mathbf{0{,}05}$ | $\mathbf{0{,}25}$ | $\mathbf{0{,}43}$ |
| **B** (iç) | $\approx400$ | $0{,}14$ | $0{,}53$ | $0{,}71$ |

**Üç ayırt edici içerik:**

1. **Halka bir *tek katmandır*, ve bu türetilmiştir.** $\Lambda>0$ olduğu sürece $h/a_b<1$ özdeş olarak sağlanır. Gözlem özeti değil, denklemin zorunlu sonucu.
2. **Sıralama tersine döner.** Kepler tek başına alınsaydı iç halka (büyük $\Omega$) ince, dış halka kalın olurdu. Halkanın kendi kuyusu katılınca belirleyici $\Lambda\propto\Sigma/\Omega^2$ olur: **yoğun ve yavaş halka incedir** ($\Lambda(10\text{ m})$: A $0{,}94$ · B $0{,}34$ · C $0{,}03$) — eşit $a_b$'de A halkası C'den iki kat ince çıkar, üstelik $\Omega$ farkı bunun tersine çalışırken.
3. **Bugünkü veriyle sınanabilir** (Sınav 11.4-G): üç niceliğin üçü de bağımsızca ölçülüyor — $\Sigma$ (yoğunluk dalgaları, Cassini), $a_b$ (örtülme boyut dağılımı), $h$ (yıldız örtülmesi, halka kenarı difraksiyonu). **Kalınlık $\Sigma/\Omega^2$ ile antikorele olmalıdır.**

#### Rampa hesabı keskinleştirir: halka **tam bir tanecik çapı** kalınlığındadır

Kayma tabanı çıplak yarıçapa değil, **etkileşim yarıçapına** kurulur ($\sigma_z\simeq\Omega\,r_H$); denklem biçimini korur, $a_b\to r_H$ olur:

$$h^2\Omega^2+4\pi\mathcal{G}\Sigma\,h=\Omega^2 r_H^2 \qquad\Longrightarrow\qquad \frac{h}{r_H}=\sqrt{1+\Lambda^2}-\Lambda,\quad \Lambda=\frac{2\pi\mathcal{G}\Sigma}{\Omega^2 r_H}$$

Sonuç dikkat çekicidir — dört bölgede de aynı:

| Bölge | $h/a_b$ | $h=10$ m için $a_b$ |
|---|---|---|
| C halkası | 1,01 | 9,9 m |
| B halkası (iç) | 0,90 | 11,1 m |
| Mimas 5:3 | 1,02 | 9,8 m |
| A halkası dışı | 1,09 | 9,2 m |

$$\boxed{\;h \simeq a_b\;}$$

**Halka, bir tanecik çapı kalınlığındadır** — ve bu, $\Sigma$ sekiz kat, $\Omega$ iki kat değişirken sabit kalıyor. **Rampanın göz ardı edilemezliği burada sayıya döner:** rampasız hesap aynı $h=10$ m için bölgeye göre $a_b=10$–$23$ m ister — hem tekdüzeliği kaybeder hem gözlenen en iri blok boyunun üstüne çıkar. Rampalı hesap dört bölgede birden **9–11 m** verir, ve Satürn halkasında gözlenen en iri blokların boyu tam bu banttadır. *(Hesabın bir parçası — $\nu_{kol}$ terimi — o rejimde Newton'a kalibreli olduğu için standart öz-çekimle sayısal olarak çakışır; teorinin katkısı, kaynağın kimliği — pulsasyon deplasmanı — ile tabanın rampadan türetilmesi ve bilançonun parametresiz kapanmasıdır.)*

### Rampalar birbirine ne kadar yakın: perkolasyon eşiği

Rampalar sürekli temasa geçerse halka ayrık taneler değil, **bağlı bir ortam** olur. Eşik, tanecik aralığının $2r_H$'ye inmesidir; hacim doldurma kesriyle $D\ge\dfrac{4\pi}{3}\left(\dfrac{a_b}{2r_H}\right)^{3}$:

| Bölge | $D$ | $2r_H/$aralık | durum |
|---|---|---|---|
| C halkası | 0,006 | **0,23** | ayrık |
| B halkası (iç) | 0,044 | **0,53** | ayrık |
| Mimas 5:3 (A) | 0,041 | **0,74** | ayrık, eşiğe yakın |
| A halkası dışı | 0,033 | **0,71** | ayrık, eşiğe yakın |

**Halka hiçbir yerde perkole değildir, ama A halkasında eşiğe en çok yaklaşır** — çünkü $r_H/a_b$ yarıçapla büyür. Ayırt edici öngörü: rampa kaynaklı her etki **dışa doğru güçlenmelidir.**

### Kanal seçiciliği rampadan değil, dengeden gelir

İzotropik bir rampa bükülme ve yoğunluk dalgasını aynı çarpanla büyütür; tek başına ikisinin **oranını** açıklayamaz. Ama halkanın **dengesi** izotropik değildir:

| Bağıl hız (Mimas 5:3) | m/s |
|---|---|
| Dikey denge, $\sigma_z$ | 0,0022 |
| Radyal denge, komşu Kepler kayması $\tfrac32\Omega\,\Delta$ | **0,0089** |
| Bükülme dalgasının dikey hızı, $A_V\Omega$ | 0,0368 |

Radyal kanalda rampalar **sürekli kaymadadır** — doymuş, kalıcı bir rejimde. Dikey kanal ise durgundur. Aynı mutlak bozulma dikey kanalda **17 kat**, radyal kanalda **4 kat** göreli sıçrama demektir: $v_r^{denge}/\sigma_z=4{,}09$. Gözlenen fazlalık — bükülme dalgası viskozitesinin yoğunluk dalgalarına oranı **2,22** — aynı mertebededir.

> **Yapısal kazanç: yeni parametre eklenmedi.** Seçiciliği rampaya yüklemek yeni bir serbest kol açardı. Gerek kalmadı: **rampa izotropik** (pulsasyondan, erimi gradyan hâkimiyetinden), **seçicilik dengeden** — ve denge ölçülmüştür ($\sigma_z$, Kepler kayması). Teori bu haneyi kendi kurduğu iki büyüklükle kapatıyor.

**Ve bu bir sınav doğuruyor.** Fazlalık, dalganın **yerel denge dispersiyonuna oranıyla** ölçeklenmelidir:

$$\frac{\nu_{fazla}}{\nu_0}\;\sim\;f\!\left(\frac{A_V\Omega}{\sigma_z}\right)$$

Bilinen üç bükülme dalgası — Mimas 5:3 (A), Iapetus $-1{:}0$ (A iç), Titan $-1{:}0$ (C) — çok farklı $\Omega$ ve $\Sigma$ bölgelerindedir. Standart açıklama (öz-çekim izleri) böyle bir ölçekleme öngörmez. **Sınav 11.4-H.**

### Ortam kanalının yeri: $10^{28}$'lik iş bölümü · **[T]**

Halkanın kendi rampası ile **dış ortamın** artık kuplajı ($\gamma_{ortam}$, M-27/M-37) ayrı kanallardır; ikincisinin dikey sönümde payı var mıdır? Cevap teorinin kendi iki yasasından, serbest parametresiz çıkar. M-43 artık kuplajı hıza dördüncü kuvvetle bağlar ($\eta_E^{etkin}\propto a_b v^4/v_{kav}^3$); aynı tanecik için iki bağıl hız vardır:

| Kanal | Ortamın o yöndeki hızı | Bağıl hız $\Delta v$ |
|---|---|---|
| **Dikey** | ortam ekvator düzleminde dolaşır, dikey bileşeni $\approx0$ | $\Delta v=\sigma_z\approx1{,}7\times10^{-3}$ m/s |
| **Yörünge** | **DY-2:** ortam maddenin iki katı hızla dolaşır | $\Delta v=v_{madde}=1{,}90\times10^{4}$ m/s |

Oran $1{,}12\times10^{7}$'dir ve $v^4$ ile:

$$\boxed{\;\frac{\gamma_{ortam}^{yörünge}}{\gamma_{ortam}^{dikey}} = \left(\frac{v_{madde}}{\sigma_z}\right)^{4} = 1{,}5\times10^{28}\;}$$

**Tanecik yarıçapı $a_b$ sadeleştiği için bu oran parametresizdir.** Sonucu tektir: ortam kuplajının dikey kanaldaki payı pratik olarak sıfırdır (rampa+temas zinciri $\sim10^{31}$ kat öndedir; $1$ m'lik tanecik için $\tau=2\rho_ca_b^2/9\eta_E=2{,}8\times10^{5}$ yıl ↔ $1{,}2$ saat); yörünge kanalında ise maksimumdur ve **yalnız sınırlanır** — DY-2 gereği tork daima dışadır, halka yağmuru ise içedir (11.4.8). İki mekanizma yarışmaz; alanları $10^{28}$ çarpanıyla ayrılmıştır. **Dikey sönümün sahibi halkanın kendi rampasıdır; dış ortamın bu hanede işi yoktur.**

> **Neden kalınlık değil frekans.** $h$ ölçümü $\sigma_z$'yi bilmeyi gerektirir ve $\sigma_z$ karşılaşma fiziğinden gelir — %50 belirsizdir. $\nu$ ise rezonans yarıçaplarından **doğrudan** ve $10^{-5}$ hassasiyetle okunur, $\sigma_z$'den bağımsızdır. F5 aranırken bakılacak yer kalınlık değil, **rezonans konumudur.** Bu, bölümün yöntemsel kazancıdır.

### F5'in işlevi: düzlemin kimliği — ve bütçenin tek kökü

> [!IMPORTANT]
> **Küresel kütle-itim (F1) düzlem tercih etmez.** Nokta kütle çevresinde eğik bir yörünge, ekvatoral bir yörünge kadar kararlıdır — hiçbir geri çağırma yoktur, hiçbir düzlem ayrıcalıklı değildir. Düzlem *seçimi* tümüyle $\omega_1$ kökenli kuvvetlerin işidir. Ve bunun **iki kanalı** vardır:
>
> | Kanal | Taşıyıcı | Radyal üs | Satürn halkasındaki pay |
> |---|---|---|---|
> | **Dolaylı** — figür ($J_2$) | **madde** (fosilleşmiş dönüş) | $(R_e/r)^2$ | %99 |
> | **Doğrudan** — F5 | **ortam** (canlı deplasman alanı) | $(R_e/r)^3$ | %1 |
>
> İkisi **aynı fiziktir**: $J_2$, gövdenin dönüşünün kütle dağılımına çökelmiş kalıntısıdır (11.2.6); F5 ise aynı dönüşün ortamda hâlâ canlı olan kalanıdır. Standart fizik birincisini veri olarak alır, ikincisini tanımaz; Evrenakı ikisini tek kökten türetir ve **oranını öngörür** ($\mathcal{P}_5$, 11.4.6). **Halkayı düzleme bastıran bütçenin tamamı, dönüş-deplasman fiziğinindir.**

Bu okumayla F5'in kuvvet kuyusu da anlamlanır. Potansiyeli integralle alınır:

$$\Psi_5(r,\theta) = \frac{\kappa_5\phi}{4}\,V(r)^2\sin^2\theta \qquad\Longrightarrow\qquad \Delta\Psi_5 = \frac{\kappa_5\phi}{4}V(r)^2 \;\;(\text{ekvator}\to\text{kutup})$$

Satürn'de $r=1{,}75R_e$'de ($V=\omega R_\phi(R_\phi/r)^2=2\,403$ m/s): $\Delta\Psi_5=1{,}43\times10^3$ J/kg, yani düzlemden kaçış hızı **53 m/s** ($J_2$'nin kuyusu: 2 396 m/s). Halka taneciklerinin gerçek dikey hızı $1{,}7$ mm/s'dir — **kuyunun içinde $10^{-5}$ mertebesinde bir derinlikte gömülüdürler.** F5 hangi düzlemin dip olduğunu söyler; taneciği o dibe indiren ve orada uysal tutan ise rampa kanalıdır. Halka, bu iki işin bitmiş hâlidir.


---

## 11.4.6 Neden Satürn? Beş Gezegenin Nicel Karşılaştırması · **[T + gözlem]**

Soru S4: *halkalar neden Satürn'de belirgin, diğer gaz devlerinde değil?* Cevap iki ayrı büyüklükte aranır: Satürn **mutlak ezmede** birincidir, **payda** ise Uranüs ve Neptün'le başa baştır — ve ölçülebilirlikte tek adaydır.

**Ölçüt 1 — mutlak ezme, $\hat{\mathcal{Q}}_{et}\equiv\dfrac{\kappa_5\phi_{doy}\mathcal{S}\mathcal{Q}}{2}\left(\dfrac{R_\phi}{R_e}\right)^{6}$.** F5'in Kepler geri çağırmasına oranının genliği; "F5 hiç önemli mi?" sorusunun cevabı.

**Ölçüt 2 — pay, $\mathcal{P}_5\equiv\mathcal{F}_5/[3J_2(R_e/r)^2] = \mathcal{K}(R_e/r)$, $\mathcal{K}=\hat{\mathcal{Q}}_{et}/3J_2$.** F5'in düzlem-kilitleme bütçesindeki payı; "F5 ölçülebilir mi?" sorusunun cevabı.

| Cisim | $v_e$ (m/s) | $\mathcal{Q}$ | $\mathcal{S}$ | $\phi_{doy}$ | $(R_\phi/R_e)^6$ | $J_2$ | $\mathcal{Q}/J_2$ | $\hat{\mathcal{Q}}_{et}$ | $\mathcal{F}_5(1{,}6R_e)$ | $\mathcal{P}_5(1{,}6R_e)$ |
|---|---|---|---|---|---|---|---|---|---|---|
| **Satürn** | 9 962 | **0,1576** | **1,0508** | 0,47 | 0,546 | 0,016291 | **9,68** ① | **$4{,}46\times10^{-5}$** ① | **$1{,}09\times10^{-5}$** ① | %0,0570 ③ |
| Jüpiter | 12 572 | 0,0892 | 1,0332 | 0,47 | 0,709 | 0,014697 | 6,07 ④ | $3{,}23\times10^{-5}$ ② | $7{,}88\times10^{-6}$ ② | %0,0457 ⑤ |
| Uranüs | 2 588 | 0,0295 | 1,0116 | 0,47 | 0,743 | 0,003343 | 8,82 ② | $1{,}09\times10^{-5}$ ③ | $2{,}67\times10^{-6}$ ③ | **%0,0682** ① |
| Neptün | 2 683 | 0,0261 | 1,0086 | 0,47 | 0,795 | 0,003411 | 7,65 ③ | $1{,}03\times10^{-5}$ ④ | $2{,}52\times10^{-6}$ ④ | %0,0630 ② |
| Dünya | 465 | 0,00346 | 1,0017 | **0,70** | 0,993 | 0,001083 | 3,20 ⑤ | $2{,}53\times10^{-6}$ ⑤ | $6{,}18\times10^{-7}$ ⑤ | %0,0487 ④ |

*(① = sıralamada birinci. $\phi_{doy}$ ve $R_\phi$ **11.4.1-(4)'te iç yoğunluk profilinden türetilmiştir**; $\kappa_5=2{,}1\times10^{-3}$ (11.4.3'ün referans üst sınırı). Satürn dönüş periyodu, 11.2 ve 11.3 ile uyumlu olarak Cassini halka sismolojisinin değeridir (10 sa 33 dk 38 sn).)*

> **İki sıralamanın başı farklı — ve bu tesadüf değil.** Mutlak ezmede ($\hat{\mathcal{Q}}_{et}$) Satürn birincidir; **payda ($\mathcal{P}_5$) ise Uranüs** (%0,0682 ↔ Satürn %0,0570). Sebep deplasman yüzeyinin derinliğidir: Satürn'ün $R_\phi$'si ideal küre içinde en derinde, üstelik gövdesi en basık olduğu için $(R_\phi/R_e)^6$ cezasını iki koldan da en çok o öder ($0{,}904\,R_e$). İki sıralamanın ayrışması bir zayıflık değil, **ilk gerçek ayırt edici öngörüdür** — aşağıya bakınız.

### Üç ayrı ifade, tek sonuç

**(i) Mutlak ezme sıralaması, halka sahibi gezegenleri seçer.** $\hat{\mathcal{Q}}$: Satürn $>$ Jüpiter $>$ Uranüs $>$ Neptün $\gg$ Dünya. Halka sistemi olan **dört gezegen listenin ilk dördüdür**; Dünya beşinciye 6 kat aşağıda düşer ve Mars, Venüs ($\mathcal{Q}\sim10^{-5}$–$10^{-8}$) tabloya girmez bile. Bu, F5'in halka için **gerekli koşulu** kurduğunun kaydıdır.

**(ii) Pay sıralamasında Satürn birinci değildir — ve sebebi deplasman yüzeyinin türetiminden çıkar.** $\mathcal{P}_5$ iki zıt çarpanın ürünüdür:

$$\mathcal{P}_5 \;\propto\; \underbrace{\frac{\mathcal{Q}}{J_2}}_{\text{dönüşün figüre soğurulmayan payı}}\;\times\;\underbrace{\left(\frac{R_\phi}{R_e}\right)^{6}}_{\text{deplasman yüzeyinin derinlik cezası}}$$

Birinci çarpanda Satürn açık birincidir:

> **Satürn, dönüşünü kendi figürüne en az soğuran gezegendir.** $J_2/\mathcal{Q}$ hidrostatik figür tepki fonksiyonudur ve merkezî yoğunlaşmayla azalır: Dünya 0,313 · Jüpiter 0,165 · Neptün 0,131 · Uranüs 0,113 · **Satürn 0,103**. Satürn en yoğunlaşmış devdir (en düşük ortalama yoğunluk, en kalın H/He zarfı), dolayısıyla dönüş sinyalinin en büyük kesri **maddede değil ortamda** kalır.

İkinci çarpanda ise Satürn **son**dur, hem de iki kez: en düşük ortalama yoğunluğa sahip olduğu için deplasman doygunluğuna ideal küre içinde **en derinde** ulaşır ($R_\phi/R_{ort}=0{,}9356$; Neptün'de $0{,}9679$), **ve** en basık dev olduğu için hacim eşdeğerlik çarpanı da onu en çok aşağı çeker ($(1-f)^{1/3}=0{,}9662$ ↔ Neptün $0{,}9943$). İki etki birleşince $(R_\phi/R_e)^6$ cezası belirgin biçimde en büyüktür ($0{,}546$ ↔ $0{,}795$) ve Satürn'ün $\mathcal{Q}/J_2$ üstünlüğünü fazlasıyla yer:

| | Satürn | Uranüs | Neptün | Jüpiter | Dünya |
|---|---|---|---|---|---|
| $\mathcal{P}_5(1{,}6R_e)$ | %0,0570 | **%0,0682** | %0,0630 | %0,0457 | %0,0487 |

> **Dürüst kayıt — sıralama sağlam, mutlak değerler değil.** Payda **Uranüs birincidir** (%0,0682), Neptün ikinci (%0,0630), Satürn üçüncü (%0,0570); Jüpiter ve Dünya altta kalır. Sıralamanın kendisi $\phi_{doy}$'un ortak çarpan olması sayesinde sağlamdır — beş gövdede de aynı değer kullanıldığı için oranlarda sadeleşir. **Mutlak değerler ise sağlam değildir**: $\phi$'nin faz bandı ($\pm$%6) ve $\mathcal{A}$–$\kappa_5$ belirsizliği hepsini birlikte kaydırır. Satürn'ün payda üçüncü, mutlak ezmede ($\hat{\mathcal{Q}}$) birinci olması bir çelişki değil, iki farklı sorunun iki farklı cevabıdır.
>
> **Ve bu bir kayıp değil — kitabın ilk gerçek *ayırt edici* F5 öngörüsüdür.** İki çarpanın birbirini götürmesi tesadüf değil: yoğunluk hem $\mathcal{Q}/J_2$'yi yükseltir hem $R_\phi$'yi derinleştirir. Sonuç, F5'in payının **gezegenden gezegene 1,5 kat içinde kalması**dır (%0,046–0,068). Standart fizikte $J_2$ payı böyle bir evrensellik göstermez. Yani F5 varsa, dört devin bükülme dalgalarında **birbirine yakın** bir $(R_e/r)^3$ katsayısı çıkmalıdır; farklı çıkarsa $\phi$'nin faz kuralı yanlıştır.

**(iii) Ve yalnız Satürn'de okunabilir.** F5'in imzası (11.4.4) bükülme dalgası rezonans konumlarından okunur; bu, optik olarak kalın, radyal olarak geniş ve dalga taşıyan bir disk gerektirir. Jüpiter'in ana halkası ($\tau\sim10^{-6}$, toz), Uranüs'ün dar halkaları ve Neptün'ün yaylar hâlindeki halkaları bu ölçümü kaldırmaz. Ölçülebilirlik farkı $\hat{\mathcal{Q}}$'nun 1,4 katı değil, **$10^3$–$10^5$ katıdır** ve F5'ten değil, halkanın kendi optik derinliğinden gelir.

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

F5 halka bandının genişliğini belirleyen unsur mudur? Soru artık nicel olarak yanıtlanabilir; cevap iki parçalıdır ve biri olumlu, biri olumsuzdur.

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

> **"İşaret değiştirmez" ifadesinin kapsamı — ve 3.9 ile çelişmediği.** Bu satır **yalnız ortamın artık kuplajı** hakkındadır ve bir **tespit kanalı değil, tek yönlü koşuldur**: sınır, etkinin *gözlenmemesinden* okunur. Kısım 3.9'un ("Gradyan Lobu ve Senkron Yarıçap") beş cisimde sınadığı **dönümlü** işaret tablosu ise **başka bir kanalın** tablosudur — gelgit şişkinliğinin gradyan lobu, ve gözlenen bütün yönleri (Ay dışa · Deimos dışa · Phobos içe · Triton içe) o verir. Uydu ölçeğinde ortam kanalı $\Delta v^4$ bastırması nedeniyle ölçülemez küçüktür; nitekim Ay bu kanalda kısıt vermez (yukarıdaki çapraz denetim). **Üç kanal — lob torku · ortam artık kuplajı · kozmolojik seyrelme tabanı — ayrı ayrı okunur; işaret kuralları birbirinin yerine konulamaz.**

### Kitaptaki en sıkı $\eta_E$ sınırı

Halka genişliği $\sim7\times10^{7}$ m, ömrü $\sim10^{7}$ yıl; $\dot a=2\gamma a$ ile:

$$\dot a < 2{,}2\times10^{-7}\ \mathrm{m/s} \;\Longrightarrow\; \gamma_{ortam}<1{,}0\times10^{-15}\ \mathrm{s^{-1}} \;\Longrightarrow\; \boxed{\;\eta_E \lesssim 2{,}3\times10^{-11}\ \mathrm{Pa\cdot s}\ \text{(Phoebe eşdeğeri)} - \mathbf{1{,}4\times10^{6}}\ \text{kat sıkı}\;}$$

**Bağımsız çapraz denetim.** Aynı prograd tork Güneş çevresindeki her cisme etki eder; astronomik birimin kararlılığı ($\lesssim0{,}01$–$0{,}1$ m/yıl) $\eta_E\lesssim1{,}5\times10^{-10}$–$1{,}5\times10^{-9}$ Pa·s verir — aynı yönde, 6–60 kat gevşek ✓ *(Ay bu kanalda kısıt vermez: $\Delta v^4$ çarpanı 1 km/s'de çöker; Ay'ın gücü **düğüm** kanalındadır, 11.4.3.)*

> **Hangi cisim en güçlü sınırı verir.** *"Sınır $a_b^2$ ile ölçeklendiğinden en küçük kalıcı retrograd cisim en güçlü sınırı verir"* okuması, M-43'ün altkritik bastırmasını hesaba katmaz. Sınırı yöneten kombinasyon $\eta_E/(r_t\Delta v^4)$'tür ve $\Delta v^4$ yarıçap çarpanını ezer: **en güçlü sınırı en küçük cisim değil, en hızlı ve en dar yapı verir — Satürn halkası.**

---

## 11.4.8.1 Sürüklenme Zarfı: Erim, Kavrama ve Dördüncü Kanal · **[T-aday]**

Yukarıdaki hesaplar zarfın iki ayrı özelliğini kritik hâle getirir: **erimi** (nereye kadar uzanır) ve **kavraması** (ne kadar tam sürükler). İkisi ayrı sorulardır ve ayrı cevapları vardır.

### Zorunlu ilk adım: Fizeau muhasebesi

Işık yolundaki ortamın **ortalama hızı**, iki fazın ağırlıklı toplamıdır (M-16):

$$\langle v_{ortam}\rangle_{yol} = \phi\,v_{madde} + (1-\phi)\,v_{ambiyans}$$

**Fizeau ile denetim.** Su $u$ ile akar, ambiyans ortam laboratuvarda durgundur: $\langle v\rangle=\phi u$, ışık hızı $c_0/n+\phi u$, ölçülen sürüklenme katsayısı $\phi=1-1/n^2$ ✓

**Rezonatör geometrisi.** Düzenek laboratuvarda durgun, **ambiyans ortam $V$ ile akar**:

$$\langle v_{ortam}\rangle_{yol} = (1-\phi)\,V$$

Anizotropiyi yöneten çarpan $\phi$ değil **$(1-\phi)$**'dir:

| Yol | $n$ | $\phi$ | $(1-\phi)V$ | $\big((1-\phi)V/c_0\big)^2$ | Deney sınırı |
|---|---|---|---|---|---|
| **Serbest Evrenakı kovuk** | 1,000000 | **0** | **29 785 m/s** | $\mathbf{9{,}9\times10^{-9}}$ | $10^{-17}$ |
| Hava | 1,000293 | $5{,}9\times10^{-4}$ | 29 768 m/s | $9{,}9\times10^{-9}$ | 1887'de $4\times10^{-9}$ |
| Su | 1,333 | 0,437 | 16 762 m/s | $3{,}1\times10^{-9}$ | $10^{-16}$ |
| Safir | 1,77 | 0,681 | 9 507 m/s | $1{,}0\times10^{-9}$ | $10^{-16}$ |

**Kavrama ile bastırılmadıkça serbest-Evrenakı yolu en kısıtlayıcıdır** ($\phi=0$, rüzgârın tamamını görür); katı yol $1/n^4$ ile zayıflar. *(Bu tablo, izotropinin **kavrama** yoluyla sağlanması varsayımı altındadır. Aşağıda türetilen kinematik ölçek terimi anizotropiyi her yol için tam olarak sıfırlar ve tablo yalnız kavrama yolunun neden gerekmediğini göstermek üzere burada durur.)*

### Kavrama yoluyla çözüm neden tükeniyor

Anizotropi kavrama ile bastırılacaksa, zarf kaymayı çok yüksek bir tamlıkla söndürmek zorundadır. Ölçülen sınır ($\delta c/c_0<10^{-17}$, artık kayma $<0{,}95$ m/s) şunu ister:

$$\text{zarf tamlığı} > 1-3{,}2\times10^{-5}$$

Teorinin üç kuplaj kanalı da bunun çok altındadır:

| Aday kanal | Verdiği | Yetersizlik |
|---|---|---|
| Viskoz sınır tabakası $\sqrt{\nu_E t}$ | Güneş Sistemi yaşında $6{,}9\ \mu$m | $9\times10^{11}$ |
| Öteleme deplasmanı $\phi$ | yalnız madde içinde; serbest Evrenakı'nda $0$ | tam |
| Dönme kavraması $\xi$ | $4{,}6\times10^{-10}$ | $10^{5}$ |

> **Viskoz yolu kapatan şey bu bölümün kendi sonucudur.** Zarfı viskoz bir sınır tabakası olarak kurmak büyük bir $\eta_E$ ister; 11.4.8'in sınırı ($\lesssim2{,}3\times10^{-11}$ Pa·s) bu yolu altı mertebe kapatır.

**Kavrama yolu tükenmiştir.** Ama izotropinin ikinci bir mekanik çıkışı vardır ve aşağıda türetilir; o çıkışta zarfın tam sürüklemesine hiç gerek kalmaz ve yukarıdaki tamlık koşulu da ortadan kalkar.

### Erim: gradyan hâkimiyeti — **[T]**

Erim tarafı türetilebilir. Ortam hangi cismin $\nabla P$'sine cevap veriyorsa onun çevresinde dolaşır (DY-1); gövdenin gradyanı Güneş'inkini **Hill yarıçapına** kadar bastırır:

$$R_{zarf}\simeq a\left(\frac{M}{3M_\odot}\right)^{1/3}\qquad \text{Dünya: } 235\,R_\oplus \qquad \text{Satürn: } 1\,086\,R_S$$

Halkaları, düzenli uyduları ve laboratuvarları rahatça kapsar. **Erim açık kalem değildir.**

### Kinematik ölçek terimi: türetim · **[T]**

Üç kavrama kanalının da yetersiz kalması, sorunun yanlış yerde arandığının işaretidir. Bir esir kuramında ışık hızı izotropisinin **iki** mekanik çıkışı vardır: ortamı gövdeyle birlikte taşımak (Stokes) ya da gövdeyi kısaltmak (Lorentz–FitzGerald). Birincisi yukarıda tükendi. İkincisi teoride hazır durur ve kullanılmamıştır: **M-42'nin ölçek yapısı.**

M-42, madde ölçeği $\Lambda$ ile cetvelin ve saatin birlikte ölçeklendiğini kurar ($\ell,f\propto\Lambda$) ve potansiyel terimini verir, $\Lambda_{grav}=1-\Phi/c_0^2$. Eksik olan **kinematik** terimdir ve teorinin kendi malzemesinden türetilir.

#### Kurulum

Üç girdi, hepsi mevcut:

1. **Ortam sıkıştırılabilirdir** ve içindeki bozunum hızı $c_0=\sqrt{P/\rho}$'dur (Postülat 1, Kavrama Yasası M-1).
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

Frekans aynı çarpanı bağımsız bir yoldan alır. Zerre balistiktir ve sürati **ortama göre** $c_0$'dir (M-1). Enine ayrılmış iki nokta arasında gidip gelen bir Zerre'yi saat sayalım: gövde $V$ ile giderken Zerre'nin yolu zikzaklaşır ve bir çevrim başına $2L/\beta$ olur (enine uzunluk kısalmaz). Dolayısıyla

$$f = \frac{c\beta}{2L} \;\Longrightarrow\; f \propto \beta$$

Bütün saatler birbiriyle uyumlu kalmak zorunda olduğundan bu, her bağlı salınıcıya taşınır. **Cetvel ve saat aynı çarpanla ölçeklenir — tam olarak M-42'nin kuralı:**

$$\boxed{\;\Lambda=\Lambda_{grav}\cdot\Lambda_{kin},\qquad \Lambda_{grav}=1-\frac{\Phi}{c^2},\qquad \Lambda_{kin}=\sqrt{1-\frac{V^2}{c^2}}\;}$$

$V$, maddenin **yerel ortama göre** hızıdır. **Yeni parametre yoktur:** $\Lambda$ envanterde zaten [T] statüsündedir; eklenen tek şey, mevcut ölçek yapısının hız bağımlılığıdır.

#### Gözlemin dayattığı biçim sağlanıyor

11.4.8.1'in başındaki muhasebe, kinematik terimin **tam** Lorentz çarpanı olmasını dayatıyordu: ikinci mertebede kesilmiş bir biçim $\beta^4/8=1{,}2\times10^{-17}$ artık bırakır ve modern sınır $10^{-17}$'dir. Prandtl–Glauert dönüşümü $\beta$'yı **kapalı biçimde** verir; kesme yoktur, dolayısıyla artık da yoktur. Türetim, gözlemin istediği tam biçimi kendiliğinden üretir.

#### İki kapsam kuralı

**(1) $\Lambda_{kin}$ maddeye etki eder, ortamın yayılma hızına etmez.** $c_{loc}\propto\Lambda_{grav}^2$ bir *yer* niceliğidir — ortamın o noktadaki hâli. $\Lambda_{kin}$ ise *hareket eden gövdenin* niceliğidir. İkisini karıştırmak, $\phi$ ile $\xi$'yi karıştırmakla aynı türden bir kategori hatasıdır.

**(2) Tekillik yereldir, evrensel bir tavan değildir.** $M=V/c_{loc}$ olduğundan $\beta\to0$ koşulu yerel bozunum hızına bağlıdır. Postülat 4 ile uyum tamdır: $c_0$ sabit olmadığı için bariyer de sabit değildir; $P/\rho$'nun yüksek olduğu bölgede aynı $V$ daha küçük $M$ verir ve kısalma azalır.

### Sonuç: Postülat 7 zorunlu işini kaybediyor

| Zarfın klasik işi | Kim yapıyor |
|---|---|
| Yörünge sürüklemesinin bastırılması | **M-43** — altkritik rejim, $10^{28}$ bastırma, zarftan bağımsız |
| Işık hızı izotropisi | **$\Lambda_{kin}$** — kısalma yoluyla, kavramadan bağımsız |

İkisi de zarf gerektirmiyor. Zarf böylece bir **postülat** olmaktan çıkıp bölgesel bir tanıma iner: gövdenin gradyanının hâkim olduğu bölge, erimi Hill yarıçapı ($235R_\oplus$, $1086R_S$). **Teori bir postülat eksilir.**

> **Ve bedeli açıkça kaydedilmelidir: bir sınav düşüyor.** $\Lambda_{kin}$ tam Lorentz kısalması ürettiğine göre, ışık hızı anizotropisi **her yol için** tam olarak sıfırlanır — serbest Evrenakı'nda, havada, katı dielektrikte. Dolayısıyla 11.4.8.1'in $(1-\phi)V$ tablosu ve ondan çıkan **$1/n^4$ ölçekleme sınavı geçersizdir**; teori de standart fizik gibi sıfır öngörür. Zarfın kavrama tamlığı üzerine konulan $>1-3{,}2\times10^{-5}$ koşulu da düşer, çünkü koşulun kaynağı bastırılmamış bir anizotropiydi.
>
> Muhasebe nettir: **bir açık kalem ve bir postülat kazanıldı, bir ayırt edici sınav kaybedildi.** Bu arenada teori artık Lorentz fenomenolojisini birebir üretir ve ondan ayrılmaz.

> **Geriye ne kalıyor.** Ayrım, doğrusallaştırmanın bozulduğu yerde aranmalıdır: **(i)** $M\to1$ civarı, yani maddenin yerel bozunum hızına yaklaştığı rejim — orada Prandtl–Glauert doğrusal biçimi geçersizleşir ve teori Lorentz'den ayrılır; **(ii)** $\Lambda_{grav}$ ile $\Lambda_{kin}$'in birlikte büyük olduğu durumlar (derin kuyuda hızlı hareket), çünkü çarpım yapısı iki terimin ayrı ayrı ölçülmesinden farklı bir öngörü verir; **(iii)** teorinin tercihli çerçevesi ortadan kalkmaz — yalnız doğrusal rejimde gözlenemez hâle gelir. Üçü de hesaplanmamıştır.

**11.4.6 ile bağ.** S4'ün cevaplanmayan yarısı (optik derinlik farkı) §7.4'te **kalem 11.4-i** olarak kalır: tedarik ↔ kayıp dengesi standart mekanizmaların işidir ve teorinin kapsamı dışındadır.

---

## 11.4.9 Neden Her Şey Düz: Levha Geometrisi ve F5'in Kilidi · **[T]**

Aynı matematik, halkanın çok ötesine geçer. Galaksiler ve yörünge sistemleri neden düzdür? Cevap burada verilir — ve F5'in en güçlü olduğu yer tam olarak orasıdır.

### Genelleştirilmiş F5 yasası ve **kabuksallık üssü**

M-39'un $v(\theta)=V\cos\theta$ profili özel bir hâldir. Genel olarak dolaşımın enlemsel yapısı $v(r,\theta)=V(r)\cos^{\lambda}\theta$ yazılırsa:

$$P = P_{kutup} - \kappa_5\rho_0 V^2\cos^{2\lambda}\theta \quad\Longrightarrow\quad \boxed{\;f_\theta = -\frac{2\lambda\,\kappa_5\rho_0V^2}{r}\cos^{2\lambda-1}\theta\,\sin\theta\;}$$

$\lambda$, dolaşımın **kabuksallık üssüdür**: dönüşün küreler üzerinde mi ($\lambda=1$, katı/kabuksal) yoksa silindirler üzerinde mi ($\lambda\le0$) organize olduğunu ölçer.

| $\lambda$ | Dolaşımın organizasyonu | $f_\theta$ | Sonuç |
|---|---|---|---|
| **$\lambda=1$** | küreler üzerinde (kabuksal / katı-cisim) | $-\dfrac{\kappa_5\rho_0V^2}{r}\sin2\theta$ | **ekvatora doğru — M-39'un yasası** |
| $\lambda=0$ | silindirler üzerinde, **$z$-yapısı olmayan** dolaşım | **0** | kuvvet yok — *ama bu hâl bir levhada gerçekleşmez, aşağıya bkz.* |
| $\lambda<0$ | silindirler üzerinde, $v_\theta$ içe doğru artan | $+$ | eksene doğru — **bu F4'tür, F5 değil** (M-38) |

> **Kategori kaydı — F4 ile F5, aynı deplasman basıncının iki izdüşümüdür.** Silindirik bileşen (dönüş silindirler üzerinde sabitse) **F4**'ü doğurur ve eksene bakar; kabuksal artık bileşen **F5**'i doğurur ve ekvatora bakar. Bu ayrım, DY-1'in *"denge yasaları kuvvetlerle toplanmaz"* uyarısını F5 için de kapatır: ortamın siklostrofik dolaşımı (M-22, silindirik) F4/DY-1 hanesine yazılır; F5 yalnız **enlemsel artığı** okur. Aynı gradyanı iki kez saymak bu ayrımla imkânsızlaşır.

### $\lambda$ serbest değildir — teorinin kendi içgirdilerinden türetilir · **[T]**

Yukarıdaki tablo $\lambda$'yı bir *seçenek* gibi sunar. Değildir: bir levhada $\lambda$, M-38 ile DY-2 tarafından belirlenir ve **hesaplanır.**

**Zincir üç halkalıdır.** *(i)* M-38'in iç içe tabaka sonucu, eksenel itimin yükseklik bağımlılığını yerel deplasman yoğunluğuna bağlar: $a_{F4}(R,z)\propto\rho_*(z)$. *(ii)* F4 radyal desteğe katkı verdiği için maddenin dairesel hızı bu yüzden $z$'ye bağlı olur. $\mathcal{A}(R)$, orta düzlemde radyal ivmenin **F4'ten gelen payı** olsun:

$$v_{madde}^2(R,z) \;=\; v_c^2(R)\Big[\big(1-\mathcal{A}\big) \;+\; \mathcal{A}\,g(z)\Big],\qquad g(z)\equiv\frac{\rho_*(z)}{\rho_*(0)}$$

*(iii)* DY-2'nin kayma yasası $v_{ortam}=2v_{madde}$'dir ve çarpan $z$'den bağımsızdır — ortam maddenin $z$-profilini olduğu gibi taşır.

Şimdi küre üzerinde açalım. Sabit $r$'de $R=r\cos\theta$, $z=r\sin\theta$; $g(z)\simeq1-z^2/2h_z^2$ ile ikinci mertebeye kadar:

$$\frac{v(r,\theta)}{v(r,0)} \simeq 1-\frac{\theta^2}{2}\left[\frac{d\ln v_c}{d\ln R}+\frac{\mathcal{A}}{2}\frac{r^2}{h_z^2}\right]$$

$\cos^{\lambda}\theta\simeq1-\lambda\theta^2/2$ ile eşleştirilir:

$$\boxed{\;\lambda_{etkin} \;=\; \underbrace{\frac{d\ln v_c}{d\ln R}}_{\text{dönüş eğrisinin eğimi}} \;+\; \underbrace{\frac{\mathcal{A}}{2}\left(\frac{R}{h_z}\right)^{\!2}}_{\textbf{iç içe tabaka terimi (M-38)}}\;}$$

**İkinci terim birinciyi üç mertebe ezer.** $R=8{,}2$ kpc, $h_z=300$ pc, $\mathcal{A}=0{,}25$ için $\lambda_{etkin}=93{,}3$; eğim teriminin payı **%0,06**. Sonuç kesindir ve iki yanlış okumayı birlikte kapatır:

> **Düz dönüş eğrisi F5'i kapatmaz.** *"$v_c$ sabit ⟹ dolaşım silindirler üzerinde ⟹ $\lambda=0$ ⟹ kuvvet yok"* okuması, ortamın $z$-yapısını yok sayar. M-38'in iç içe tabakaları diski **zorla kabuksal** kılar: her yükseklik kendi yoğunluğunun belirlediği hızla döner, ve $h_z\ll R$ olduğu için bu kabuksallık şiddetlidir. Tablonun $\lambda=0$ satırı yalnız **$z$-yapısı olmayan** bir dolaşım için geçerlidir; gerçek bir levha için değil.
>
> **Ve bu, standart akışkan teoremlerinin buraya taşınamayacağının kaydıdır.** Barotropik bir akışkanda dönüşün silindirler üzerinde sabitlenmesini veren teoremler (Poincaré–Wavre, Taylor–Proudman) Evrenakı'da **uygulanamaz**, çünkü deplasman basıncı $\phi$ ile *ve* dolaşım hızı $V$ ile ayrı ayrı değişir: $\Delta P=\kappa_5\phi\rho_0V^2$. Ortam özünde **barotropik değildir.** Bir teoremi varsayımı sağlanmadan ithal etmek, burada işaretini değil **mertebesini** kaybettirir.

### Disk, F5'in **geometrik** sabit noktasıdır

$$\boxed{\;\sin2\theta\to0\ \ (\theta\to0)\;}$$

Dönen bir ortam konfigürasyonu kabuksaldır ve F5 maddeyi ekvatora bastırır. Düzleşme ilerledikçe madde $\theta\to0$'a gider ve $\sin2\theta$ sıfırlanır: **orta düzlem kararlı bir dengedir.** Ama bu bir *söndürme* değildir — düzlemden en küçük sapma kuvveti geri çağırır, ve $\lambda_{etkin}$ hesabının gösterdiği gibi geri çağırma bir levhada zayıf da değildir. Disk, F5'in **dengesi**dir; kaynağını kaybettiği yer değil.

> **Ayrım neden önemli.** Bir kuvvet kaynağını kaybederse sistem serbest kalır ve dış tork onu istediği yere taşır. Bir kuvvet dengede *susup sapmada konuşursa* sistem kilitlenir. Diskin ikinci türden olması, "neden diskler bu kadar yaygın ve bu kadar kararlı" sorusunun mekanik cevabıdır: geri itme yoktur, salınım yoktur, aşırı düzeltme yoktur — ama kilit vardır.

### Galaktik ölçek — ve levha geometrisinin $(R/h_z)^2$ yükseltmesi

Galaktik yarıçapta $J_2$ kanalı yoktur: $(R_e/r)^2$ ile ölçeklenen bir figür çokkutbu 10 kpc'de $10^{-30}$ mertebesindedir. Merkezî gövdenin basıklığı galaktik diski düzleştiremez. F1 ise düzlem tercih etmez (11.4.5). **Geriye tek kaynak kalır** — ve orada gradyanın ölçeğini doğru seçmek her şeyi belirler.

#### Küresel okuma yanlış geometriyi kullanır

Kabuksal rejimde ($\lambda=1$, R2 — kavrama kesri içermez, M-39) ve gradyan ölçeği $r$ alınırsa:

$$a_\theta = -\frac{\kappa_5}{4}\,\frac{v_0^2}{r}\sin2\theta \qquad\Longrightarrow\qquad \mathcal{F}_5^{k\ddot{u}re} = \frac{\Omega_5^2}{\Omega^2} = \frac{\kappa_5}{2}$$

Yarıçaptan bağımsız — çünkü hem $a_\theta$ hem $\Omega^2$ düz dönüş eğrisi rejiminde $v_0^2/r$ ile gider. Ama bu okuma **kürenin** geometrisini varsayar. M-38'in kendi sonucu bunu yasaklar: eksenel itim iç içe tabakalarda üretilir ve yükseklik bağımlılığı yerel deplasman yoğunluğunu izler, $a_{F4}(R,z)\propto\rho_*(z)$. Bir galakside deplasmanı taşıyan madde bir küre değil, kalınlığı $h_z\ll R$ olan bir **levhadır.** Basınç açığının tamamı $R$ boyunca değil, $h_z$ boyunca kurulur.

Genlik denklemine $\lambda_{etkin}$ konulur ($\Omega_5^2=2\lambda_{etkin}\kappa_5\phi(\rho_0/\rho_n)V^2/r^2$, 11.4.4'ün türetimi) ve tabaka terimi baskın olduğu için:

$$\boxed{\;\Omega_5^2 \;=\; \frac{\mathcal{A}\,\kappa_5}{4}\,\frac{v_c^2}{h_z^2} \qquad\Longrightarrow\qquad \mathcal{F}_5^{levha} \;=\; \frac{\mathcal{A}\,\kappa_5}{4}\left(\frac{R}{h_z}\right)^{\!2}\;}$$

İki çarpan var ve **ikisi de teorinin kendi büyüklüğü:** geometrik yükseltme $(R/h_z)^2$ ve **F4'ün radyal payı $\mathcal{A}$.** Yeni parametre yok. $R=8{,}2$ kpc'de, §6.5.4.2'nin kaynak tablosunun ölçek yükseklikleriyle ve $\kappa_5=2{,}1\times10^{-3}$ ile:

| Bileşen | $h_z$ | $(R/h_z)^2$ | $\mathcal{F}_5$ ($\mathcal{A}=0{,}25$) | $\mathcal{F}_5$ ($\mathcal{A}=0{,}70$) |
|---|---|---|---|---|
| Yıldız diski | 0,30 kpc | **747** | 0,098 | 0,27 |
| HI gaz diski | 0,50 kpc | **269** | 0,035 | 0,099 |
| Soğuk HI (Güneş komşuluğu) | 0,15 kpc | **2988** | 0,39 | 1,10 |

Küresel okumanın verdiği $10^{-3}$ yerine **$10^{-2}$–$1$**. Fark iki-üç mertebedir, tamamen geometriktir, ve tek bir serbest parametre eklenmemiştir.

> **$\mathcal{A}$ varsayılmaz, okunur.** Kısım 6, dönüş eğrisini sayılan baryonlar üzerinde F1 integrali + F4'ün $1/R$ terimiyle kurar (§6.5.4.2). $\mathcal{A}(R)$ tam olarak o ayrışımın F4 payıdır — standart fizikte "karanlık madde kesri" denilen niceliğin teorideki karşılığı. Samanyolu iç diskte baryon-baskındır, yani $\mathcal{A}$ orada en küçüktür; dış diskte 1'e yaklaşır. **Sayısal değeri Kısım 6'nın kendi eğrisinden alınmalıdır** (kalem 11.4-vi).

> **Basıklığın hangi kanalı sınırsızdır.** 11.4.1-(2)'de basıklık F5'i meridyen kısalmasıyla artırıyordu ve o kanal $\mathcal{S}\to\pi/2=1{,}571$'de **doyar**: bir gövdeyi levhaya kadar bassanız kazanç %57'yi geçmez. *"Disk hâline geldiği için F5 çok çok güçlü olmalı"* sezgisi doğrudur — ama kanalı $\mathcal{S}$ değil, $R/h_z$'dir ve karesiyle girer. Satürn'de geçerli oran gövdenin kendisinindir ($R_e/h_z\sim1$, $\mathcal{S}=1{,}05$); galakside $16$–$55$'tir. **F5'in halka ile galaksi arasındaki mertebe farkı buradan doğar, $\kappa_5$'ten değil.**

#### Yasanın alt sınırı: ortamın **dolaşım tutarlılık ölçeği** · **[T]** + **[A]**

$(R/h_z)^2$ sınırsız büyüyemez, ve sınırı teorinin kendi yapısı koyar. Denetimi Satürn halkası verir: orada $R/h=9{,}0\times10^{6}$'dır, karesi $8{,}2\times10^{13}$. Yasa oraya olduğu gibi uygulansaydı — halkanın kendi radyal payı $\mathcal{A}\lesssim9\times10^{-8}$ olmasına rağmen —

$$\Omega_5/\Omega_{y\ddot{o}r} \simeq 6\text{–}65$$

çıkardı. **Dışlanmıştır:** gözlenen dikey frekans $\nu\simeq\Omega$'dır (11.4.4). Yasanın tabanı yoktur diye alınamayacağı buradan bellidir.

**Ayrım, iki kuplajın farklı doğasındadır.** F1 **statik** bir deplasman tepkisidir: ortam, yerel yoğunluğa her ölçekte cevap verir — bu yüzden on metre arayla duran iki halka taneciği arasında kütle-itim normal işler ve 11.4.5'in $\nu_{kol}$ terimi geçerlidir. F5 ise bir **dolaşım** gradyanı okur; dolaşım kolektif bir akış desenidir ve bir akış deseninin **asgari tutarlılık ölçeği** vardır. Ortam, maddenin yoğunluk yapısını her ölçekte izler; **dönme yapısını izlemez.**

$$\boxed{\;\mathcal{F}_5^{levha}=\frac{\mathcal{A}\,\kappa_5}{4}\left(\frac{R}{\max(h_z,\;\ell_{min})}\right)^{\!2}\;}$$

Halkanın $\Omega_5\lesssim10^{-2}\,\Omega$ koşulu bu ölçeği alttan sınırlar:

$$\ell_{min}\;\gtrsim\;7\text{–}65\ \mathrm{km}\qquad(\mathcal{A}=10^{-9}\text{–}10^{-7})$$

| Sistem | İlgili kalınlık | $\ell_{min}$'e göre | $(R/h_z)^2$ devrede mi |
|---|---|---|---|
| Satürn halkası | $10$ m | **çok altında** | **hayır** — yasa tabanlanır |
| $\ell_{min}$ | $\gtrsim7$ km | — | — |
| Satürn gövdesi | $6\times10^{7}$ m | çok üstünde | evet |
| Galaktik levha | $9\times10^{18}$ m | çok üstünde | evet |

**Üç kazanç.** *(i)* Yasa halkada patlamaz ve galakside geçerli kalır — arada on üç mertebe boşluk var, sınır rahat. *(ii)* Küçük ölçekte Newton davranışı korunur, çünkü sınırlanan F1 değil F5'tir. *(iii)* $\ell_{min}$ **teorinin ölçülmüş yeni bir büyüklüğüdür** ve halkalar onu alttan sınırlıyor; üstten sınırı henüz yoktur (kalem 11.4-vii).

#### İki rejim — ve yassılaşmanın mimarı

Yükseltme levhanın *içinde* geçerlidir. Düzlemden çok uzaktaki ($|z|\gg h_z$) izole bir yörünge levhayı görmez; onun için gradyan ölçeği yine $R$'dir. İki rejim aynı $\kappa_5$ ile üç mertebe ayrılır:

| Rejim | Gradyan ölçeği | $\mathcal{F}_5$ | Sonuç |
|---|---|---|---|
| $\lvert z\rvert\gg h_z$ — izole eğik yörünge | $R$ | $\sim10^{-4}$ | tek başına eğik yıldız yörüngesini taşımaz — taşıması da gerekmez (aşağıda) |
| $\lvert z\rvert\lesssim h_z$ — levha içi | $h_z$ | $0{,}03$–$1{,}1$ | dikey geri çağırmanın **kayda değer payı** — kilit |

Birinci satır teorinin aleyhine okunamaz, çünkü yassılaşma sürecinde o satırın taşıyacağı bir iş yoktur. Yıldızlar yitimsizdir; ama galaksiyi kuran madde **gazdır ve gaz yitimlidir**: bulut–bulut çarpışmaları ve ışınım dikey enerjiyi boşaltır, açısal momentum korunur. Enerjisini kaybeden dönen bir sistemin **hangi biçime çökeceğini** söyleyen tek düzlem-seçici kuvvet F5'tir — F1 düzleme kayıtsızdır (11.4.5), figür çokkutbu galaktik yarıçapta $10^{-30}$'dur (yukarıda). F5'in potansiyeli vardır ($\Psi_5=\tfrac{\kappa_5\phi}{4}V^2\sin^2\theta$), dolayısıyla enerji hanesini kendisi kapatmaz — kapatması da gerekmez: **yitim motordur, F5 dümendir.** Enerjiyi yitim boşaltır; nereye çökeceğini F5 yazar. Halkadaki iş bölümünün (11.4.5: düzlemi F5 seçer, boşaltmayı rampa+temas zinciri yapar) galaktik ölçekteki karşılığı budur.

İkinci satır kilidin kendisidir: levha inceldikçe F5'in kavrayışı $(R/h_z)^2$ ile mertebelenir — $\mathcal{F}_5$ küresel rejimin $10^{-4}$'ünden levha içinde $0{,}03$–$1{,}1$'e atlar. **Galaksilerin yassılığı F5'in eseridir:** çöküşün düzlemini o seçer, incelen levhayı yayılmaya, kalınlaşmaya ve kepçelenmeye karşı o tutar.

> **Ve payı $\mathcal{A}$ ile yarıçapa göre yeniden dağılır — istenen yönde.** İç diskte $\mathcal{A}$ küçüktür ($\mathcal{F}_5\simeq0{,}1$), dış diskte 1'e yaklaşır ($\mathcal{F}_5\simeq0{,}9$, $R=25$ kpc, $h_z=0{,}5$ kpc). F4'ün $1/R$ akı tüpü rejimi zaten **dış disktedir**; §6.5.4.1'in *"$h_d=$ sabit"* koşuluna en çok ihtiyaç duyduğu yer orasıdır. F5 tam orada güçlü çıkıyor — ve iç diskte zayıf çıkması aşağıdaki Oort kısıtını da kurtarıyor. **Tek katsayı, iki zıt ihtiyaç, ayarlama yok:** ikisi de $\mathcal{A}(R)$'nin aynı profilinden geliyor, çünkü F4 ile F5 aynı alanın iki izdüşümüdür.

> **Bu, pozitif geri beslemeli bir çekerdir.** İnceldikçe kavrayış güçlenir ($\Omega_5\propto1/h_z$). F5 geç devreye girer ama girdiğinde tutar; bu yüzden galaktik disk $z$ yönünde *keskin kenarlıdır.* Ve bu, §6.5.4.1'in ihtiyaç duyduğu mekanik dayanaktır: M-38'in akı tüpü yayılırsa $1/R$ yasası $1/R^2$'ye döner ve galaktik ayak çöker; levhayı yayılmaya karşı destekleyen ikinci mekanizma F5'tir. *(Koşulun kendisi M-38 içinde bağımsızca da kurulur — viskoz difüzyonun ihmal edilebilirliği $10^{22}$ marj bırakır. F5 o marjı destekler, tek başına taşımaz.)*

#### F5'in payı doğrudan ölçülür — ve $h_z$ sadeleşir

$\Omega_5\propto1/h_z$ ile $h_z=\sigma_z/\nu$ birleştirilirse ($\nu^2=\nu_{\ddot{o}z}^2+\Omega_5^2$, toplam dikey frekans) F5'in paydaki oranı $h_z$'den **ve** özçekimin büyüklüğünden bağımsız çıkar:

$$\boxed{\;x \;\equiv\; \frac{\Omega_5^2}{\nu^2} \;=\; \frac{\mathcal{A}\,\kappa_5}{4}\left(\frac{v_c}{\sigma_z}\right)^{2}\;}$$

İçinde yalnız gözlenen büyüklükler var: dönüş hızı, tabakanın dikey dispersiyonu, ve F4'ün radyal payı. Üç sonucu vardır.

**(i) Teori diski aşırı belirlemiyor.** $h_z$ sadeleştiği için kalınlık serbest gözlem girdisi kalır; §6.5.4.2'nin kaynak tablosu ve F1 integrali bozulmaz.

**(ii) Bir dispersiyon ölçeği.** $x=1$ hâli, F5'in tabakayı tek başına taşımasına karşılık gelir ve $\kappa_5$'i doğrudan bir hıza çevirir:

$$\sigma_z^{(F5)} = \frac{\sqrt{\mathcal{A}\,\kappa_5}}{2}\;v_c \;=\; 2{,}5\ \mathrm{km/s} \qquad (\kappa_5=2{,}1\times10^{-3},\;\mathcal{A}=0{,}25,\; v_c=220\ \mathrm{km/s})$$

Gözlenen soğuk HI dispersiyonu **6–8 km/s** olduğuna göre $x\simeq0{,}1$: F5 tabakayı taşımıyor, ona **onda bir mertebesinde** katkı veriyor. Bu, teorinin kendi lehine bir sonuçtur — çünkü $x\to1$ olsaydı gözlenen dikey kuvvetten çıkarılan yerel yoğunluk tümüyle hayalî olurdu, ve o yoğunluk bağımsızca sayılmıştır.

**(iii) Bedel: Oort limiti $\kappa_5$'e kitaptaki en sıkı üst sınırı koyar.**

Yerel dikey kuvvet yasasından çıkarılan **dinamik** yoğunluk ile teleskopla **sayılan** yıldız+gaz yoğunluğu %10–20 içinde uyuşur (Oort limiti). F5 modellenmemişse fazlalık doğrudan $x$ kadardır, dolayısıyla:

$$x\le x_{maks}\qquad\Longleftrightarrow\qquad \boxed{\;\kappa_5 \;\le\; \frac{4\,x_{maks}}{\mathcal{A}}\left(\frac{\sigma_z}{v_c}\right)^{2}\;}$$

Ve burada belirleyici bir olgu devreye girer: **Oort limiti Güneş komşuluğunda ölçülür, ve Samanyolu orada baryon-baskındır** — yani $\mathcal{A}$ tam olarak sınırın en gevşek olduğu yerde en küçüktür. $x_{maks}=0{,}20$, $\sigma_z=7$ km/s, $v_c=220$ km/s ile:

| $\mathcal{A}$ (Güneş çemberi) | $\kappa_5\le$ | LLR'ye ($2{,}1\times10^{-3}$) göre |
|---|---|---|
| 0,20 | $4{,}1\times10^{-3}$ | gevşek — **LLR bağlayıcı** |
| **0,25** | $\mathbf{3{,}2\times10^{-3}}$ | gevşek — **LLR bağlayıcı** |
| 0,30 | $2{,}7\times10^{-3}$ | gevşek — **LLR bağlayıcı** |
| 0,50 | $1{,}6\times10^{-3}$ | 1,3 kat sıkı |
| 0,70 | $1{,}2\times10^{-3}$ | 1,8 kat sıkı |

**Sonuç: Oort limiti bağlayıcı sınır değildir.** Güneş çemberinde $\mathcal{A}\lesssim0{,}3$ olduğu sürece Ay'ın düğüm gerilemesi ($\kappa_5\lesssim2{,}1\times10^{-3}$) kitaptaki en sıkı kısıt olarak kalır ve galaktik kanal **hiçbir öngörüyü küçültmez.** Sınav 11.4-A $\hat{\mathcal{Q}}_{et}=4{,}5\times10^{-5}$, $\delta\nu/\nu=1{,}6\times10^{-5}$ ile ayaktadır; 11.4-B 0,10 mas/yıl ile LLR eşiğindedir.

> **$\mathcal{A}$ neden bu işi yapıyor.** Tesadüf değil, yapısal: $\mathcal{F}_5\propto\mathcal{A}$, yani **F5 ancak F4'ün güçlü olduğu yerde güçlüdür** — ikisi aynı deplasman basıncının iki izdüşümü olduğu için zorunlu. Oort limiti baryon-baskın iç diskte ölçülür (F4 zayıf ⟹ F5 zayıf ⟹ kısıt gevşek); §6.5.4.1'in $h_d=$ sabit koşuluna ihtiyacı ise F4'ün $1/R$ rejiminin işlediği dış diskte doğar (F4 güçlü ⟹ F5 güçlü ⟹ mekanizma var). **Aynı $\mathcal{A}(R)$ profili iki zıt ihtiyacı birlikte karşılıyor ve arada tek bir ayar yok.**

**Ve dejenerasyonu kıran şey burada.** Galaktik dikey kuvvette bir fazlalık, F5 ile de açıklanır fazladan kütleyle de. Ama F5'in fazlalığı **radyal eksik kütle payına orantılıdır** ($\propto\mathcal{A}$) ve **tabaka kalınlığının karesiyle ters** gider ($\propto h_z^{-2}$). Bir kütle dağılımının dikey/radyal oranı ise kendi **şekliyle** belirlenir; baryon kesrine ya da tabaka kalınlığına duyarlı değildir. İki bağımsız ölçeklendirme:

$$\text{F5:}\quad \nu_{fazla}^2 \propto \frac{\mathcal{A}\,v_c^2}{h_z^2} \qquad\qquad \text{kütle:}\quad \nu_{fazla}^2 \propto \frac{v_c^2}{R^2}\,q(\text{şekil})$$

**Sınav 11.4-F bu ayrımın üzerine kurulur** ve galaksi içi olduğu için uzaklık, eğim ve $M/L$ sistematikleri sadeleşir.

> **Dürüst kayıt — kalan iki belirsizlik.** *(i)* $g(z)\simeq1-z^2/2h_z^2$ açılımı profil biçimine bağlıdır; $\mathrm{sech}^2$ için katsayı iki kat değişir ve $\mathcal{A}_{etkin}$ aynı oranda kayar. $\mathcal{A}\gtrsim0{,}5$ bölgesinde Oort yeniden bağlayıcı olur. *(ii)* $\mathcal{A}(R)$ burada varsayılmıştır; Kısım 6'nın kendi F1/F4 ayrışımından okunmalıdır. **İkisi birlikte kalem 11.4-vi'nin tanımıdır** ve F5'in galaktik hanesinin tek açık hesabıdır.

#### Warp: F5 onu açıklamaz — **sınırlar**

Galaktik diskler düz değildir: yaklaşık $R_{25}$'ten sonra orta düzlem bükülür ve Samanyolu'nda dış HI diski $|z|\sim1$–3 kpc'ye çıkar. F5'in bu gözlemle ilişkisi doğrudandır, ama yönü *ters*: **F5 warp üretmez, ona direnir.** Yanal itim düzleme doğru geri çağırıcıdır; warp ise düzlemden sapmadır. Dolayısıyla warp teorinin açıklayacağı bir olgu değil, **geçmesi gereken bir denetimdir** — ve denetim niceldir.

**Zorlanmış bükülme kipinin genliği.** Warp, dış bir tork tarafından (halo torku, uydu geçişi, kozmolojik akış — kaynağı ne olursa olsun) sürülen bir $m=1$ bükülme kipidir. Rezonansın altındaki bir zorlanmış salınıcının genliği geri çağırma ile ters gider, $z\simeq\mathcal{T}/\nu^2$. F5 devreye girerse $\nu^2=\nu_{\ddot{o}z}^2+\Omega_5^2$ olur ve genlik tam olarak $x$ kadar bastırılır:

$$\boxed{\;\frac{z_{warp}}{z_{warp}^{(F5\,yok)}} \;=\; \frac{\nu_{\ddot{o}z}^2}{\nu_{\ddot{o}z}^2+\Omega_5^2} \;=\; 1-x\;}$$

Torkun büyüklüğünü bilmemize gerek yoktur — o, oranda sadeleşir. Gereken tek şey $x$'tir. Dış diskte ($v_c=200$, $\sigma_z=7$ km/s, $\kappa_5=2{,}1\times10^{-3}$):

| $\mathcal{A}$ | $x$ | warp genliği | Hüküm |
|---|---|---|---|
| 0,25 | 0,11 | %89'a iner | ✓ model belirsizliğinin içinde |
| 0,50 | 0,21 | %79'a iner | ✓ sınırda |
| **0,70** | **0,30** | **%70'e iner** | ⚠ **ölçülebilir bastırma — bu bir öngörü** |

**Warp $\kappa_5$'e bağlayıcı bir sınır koymaz.** Mutlak koşul $x\le1$'dir ve $\kappa_5\le4(\sigma_z/v_c)^2/\mathcal{A}=7$–$20\times10^{-3}$ verir — LLR'nin $2{,}1\times10^{-3}$'ünden bir mertebe gevşek. Warp bir kısıt kaynağı değil, **bir öngörü adresidir.**

$$\boxed{\;\text{Dış diskte warp genlikleri, saf özçekim + tork modellerinin verdiğinin } \%70\text{'i olmalıdır}\;}$$

Bu, hiçbir serbest parametre içermeyen nicel bir sapma öngörüsüdür ($\mathcal{A}$ Kısım 6'dan, $\kappa_5$ LLR'den, $\sigma_z$ ve $v_c$ gözlemden). Standart fizik sapma öngörmez.

**Ne açıklanmıyor: warpın başlangıç yarıçapı.** Burada teorinin sınırını açıkça çizmek gerekir. $\mathcal{A}$ dışa doğru büyüdüğü için $x$ de büyür:

| $R$ (kpc) | 8 | 12 | 16 | 20 | 25 | 30 |
|---|---|---|---|---|---|---|
| $\mathcal{A}$ (temsilî) | 0,25 | 0,35 | 0,45 | 0,55 | 0,65 | 0,72 |
| $x$ | 0,10 | 0,15 | 0,20 | 0,26 | 0,33 | 0,40 |

F5'in kavrayışı dışa doğru **güçlenir** — warpların büyüdüğü yönde. Dolayısıyla F5 **karakteristik bir warp başlangıç yarıçapı öngörmez** ve warpların neden optik kenarda başladığını açıklamaz; tersine, dışa doğru artan bir direnç getirir. Warpın kaynağı dış torkun kendi radyal profilindedir ve teorinin kapsamı dışındadır. *(Bu, gözlemle bir gerilim değildir — bastırma en dışta %40'a çıksa da warp yine var olur; ama teorinin dış diskte sistematik olarak **daha zayıf** warp beklemesi gerektiğini kaydeder.)*

**F5'in warpta bıraktığı doğrudan iz.** Düğüm çizgisinin presesyonuna katkı: $R=25$ kpc, $h_z=1{,}5$ kpc'de $|\dot\Omega_{d\ddot{u}\breve{g}\ddot{u}m}|=\tfrac12\Omega_5^2/\Omega$ = 0,15 ($\mathcal{A}=0{,}25$) … 0,41 km/s/kpc ($\mathcal{A}=0{,}70$).

> **Gözlem tabanı ve F5'in payı.** Warp presesyonunun ölçümü tartışmalıdır: Poggio ve ark. (2020) $10{,}86$ km/s/kpc verdi, Chrobáková & López-Corredoira (2021) buna itiraz edip $\beta=4^{+6}_{-4}$ buldu (presesyonsuz warpı bile dışlamaz), Zhou ve ark. (2024) 13 kpc'de $4{,}9\pm1{,}6$, ve Sefeid analizi **$4{,}86\pm0{,}88\pm2{,}14$ km/s/kpc**'de oturur. Bu taban üzerinden:
>
> | $\mathcal{A}$ | F5'in katkısı | F5'in payı |
> |---|---|---|
> | $0{,}25$ | $0{,}15$ km/s/kpc | **%3,1** |
> | $0{,}70$ | $0{,}41$ km/s/kpc | **%8,4** |
>
> ⟹ **F5'in warp payı %3–8**'dir — mevcut belirsizliklerin içinde, ama işareti sabittir (daima gerileme yönünde) ve dönüş yönüne kilitlidir.
>
> **Ve ikinci, yapısal kayıt: devinim RİJİTTİR.** Aynı analiz presesyonu 12,5 kpc'nin ötesinde *"nearly uniform"* bulur — kapalı biçimin zaman terimi $R$ içermez. Bu, 3.8.7'nin *"sarılma problemi hiç doğmaz"* iddiasının arkasına **ölçüm** koyar: standart çerçevede rijitliği ayakta tutmak özel bir hale geometrisi ister (Ideta ve ark. 2000 — **prolat** hale), akışkan yaprak okumasında ise varsayılandır. *(Warpın kaynağı bu bölümün değil 3.8.7'nin konusudur; buradaki kayıt yalnız F5'in payını ve rijitlik denetimini verir.)*

> **Bölümün warp hükmü.** *F5 galaktik warpı açıklamaz, açıklaması da beklenmez — warp bir sapmadır, F5 sapmaya karşı çalışan kuvvettir.* Warpın **var olması** bir denetimdir ve teori onu rahatça geçer: bastırma %11–30 mertebesindedir, mutlak sınır ise LLR'den bir mertebe gevşektir. Kazanılan şey bir sınır değil, **bir sapma öngörüsüdür.** Warpın başlangıç yarıçapı, genliği ve asimetrisi teorinin kapsamı dışındadır ve öyle kaydedilmiştir.

### Yörünge eş-düzlemliliği

F5 **düzlemi seçer**, açısını **sönümlemez** — sönüm için yitim gerekir. Eş-düzlemliliğin tam zinciri üç halkalıdır:

$$\underbrace{\text{F5} \Rightarrow \text{çekici düzlem = dönme düzlemi}}_{\text{11.4.4}} \;\;+\;\; \underbrace{\text{M-37}\ \gamma_{sür} \Rightarrow \Delta v\text{ sönümü}}_{\tau_{ret}=2\rho_ca_b^2/9\eta_E} \;\;\Longrightarrow\;\; \text{eğik yörüngeler düzleme oturur}$$

Koşul, F5'in presesyon hızının sönüm hızını aşmasıdır:

$$\tfrac12\mathcal{F}_5(r)\,\Omega(r) \;\gtrsim\; \gamma_{sür} = \frac{9\eta_E}{2\rho_c a_b^2}$$

Sağlanırsa yörünge **zorlanmış düzleme** (F5'in düzlemi) sönümlenir; sağlanmazsa rastgele kalır.

> [!WARNING]
> **Bu zincir $\gamma_{sür}$ üzerinden taşınamaz.** $\gamma_{sür}=9\eta_E/2\rho_ca_b^2$ ifadesi $\eta_E$'yi sabit alır; M-43 ile $\eta_E^{etkin}\propto\Delta v^4$'tür ve kitaptaki $\eta_E$ sınırı, tanım gereği *en hızlı sönmesi gereken cismin bile sönmediği* yerden okunur (Phoebe, $215R_e$'de kalıcı retrograd — Ek M-37). Uzak yörünge ölçeğinde bu kanaldan bir düzleme-oturtma beklenemez.
>
> **Ayakta duran şey F5'in düzlem seçimidir** ($\S$11.4.2–11.4.4) — korunumludur, sönüm gerektirmez. Eğik uzak yörüngelerin kaderi düzlemin **kimliği** üzerinden okunur (aşağıda); prograd tercihin ve daireselliğin mekanizması ayrı bir hesap kalemidir → §7.4 kalem **11.4-viii**.

#### Sönüm halkası kopunca kalan soru: düzlemin **kimliği**

Yukarıdaki geri alma, *"eğik yörünge düzleme oturur"* zincirini koparır. Ama **hangi düzlem** sorusu ayakta kalır ve cevabı vardır — sönüm gerektirmeden. Aşağıdaki dört kalem o cevabı verir; hiçbiri yitimli bir kanala dayanmaz.

##### (a) Geçiş yarıçapı: iki düzlem adayının eşitlendiği yer · **[T (türetim) / gözlemle 10/10]**

Yakında gezegenin $J_2$+F5'i düzlemi seçer; uzakta Güneş'in torku. **F1 her iki uçta da kayıtsızdır** — yörüngeyi kurar, düzlemi kurmaz (11.4.5). İki düğüm-presesyon hızının eşitlenmesinden:

$$\tfrac32 J_2\!\left(\frac{R_e}{r}\right)^{2}\!n \;=\; \tfrac34\frac{n_\odot^2}{n}
\qquad\Longrightarrow\qquad
\boxed{\;r_{geçiş}^{5}=2\,J_2\,R_e^2\,a_p^3\,\frac{M_p}{M_\odot}\;}$$

Beş sistem, on cisim, **sıfır serbest parametre**:

| Sistem | $r_{geçiş}$ | İçeride ($r/r_g$) | Dışarıda ($r/r_g$) |
|---|---|---|---|
| **Dünya** | $9{,}7\,R_\oplus$ | — | Ay **6,25** ✓ ekliptikte ($5{,}14°$), Dünya ekvatorunda **değil** |
| **Jüpiter** | $32{,}5\,R_e$ | Callisto **0,81** ✓ ($0{,}19°$) | Himalia **4,9** ✓ ($27{,}5°$) |
| **Satürn** | $41{,}6\,R_e$ | Titan **0,49** ✓ ($0{,}35°$) | Iapetus **1,42** ✓ ($\sim\!15{,}5°$) |
| **Uranüs** | $52{,}9\,R_e$ | Oberon **0,43** ✓ ekvatorda | Caliban **5,3** ✓ eğik/retrograd |
| **Neptün** | $73{,}2\,R_e$ | Triton **0,20** ✓ ekvator etrafında preses | Nereid **3,0** ✓ |

**Uranüs ayırt edicidir.** Eğikliği $97{,}77°$ olduğu için iki aday düzlem neredeyse **diktir** — belirsizlik yok. Ve beş büyük uydu $r_g$ içinde, ekliptiğe dik denecek bir düzlemde, **Uranüs ekvatorunda** duruyor. Hiçbir "ortalama düzlem" okuması bunu veremez. **Iapetus tam sınırdadır** ($1{,}42\,r_g$): eğikliğinin neden ara değerde olduğu buradan çıkar.

> [!IMPORTANT]
> **Dürüst kayıt: geçiş yarıçapı bir F5 sınavı DEĞİLDİR.** $r_g$'de F5'in payının $J_2$'ye oranı
> $$\frac{\hat{\mathcal{Q}}_{et}(R_\phi/r)^3}{J_2(R_e/r)^2}\bigg|_{41{,}6R_e}=\frac{4{,}58\times10^{-10}}{9{,}41\times10^{-6}}=4{,}9\times10^{-5}$$
> ve $r_g\propto(\text{toplam})^{1/5}$ olduğundan yarıçaptaki kayma $\sim\!10^{-5}$ — **ölçülemez.** Teorinin payı **dolaylıdır**: $J_2$'yi kendisi türetir (11.2), dolayısıyla $r_g$ de türetilmiş olur; ama **ayrışan imza yoktur.** Bu, F5'in figürde görünmezliğiyle (Sınav 1) ve saf-$P_2$ dejenerasyonuyla tutarlıdır — sürpriz değil. **"Kazanılmış sınav" diye sunulamaz:** 10/10 tutan şey standart **Laplace yarıçapıdır** ve teori onu ancak $J_2$ üzerinden sahiplenir.

##### (b) "Serbestlik" nicelleşir · **[T]**

Düzlem seçen payın Kepler geri-çağırmasına oranı $\tfrac32J_2(R_e/r)^2$ (Satürn):

| Konum | Düzlem seçen pay |
|---|---|
| Halka ($1{,}75R_e$) | $8{,}0\times10^{-3}$ |
| Titan | $5{,}9\times10^{-5}$ |
| $r_{geçiş}$ | $1{,}4\times10^{-5}$ |
| Iapetus | $7{,}0\times10^{-6}$ |

**Halkadan Iapetus'a bin kat düşer.** Halka gezegene yakın olduğu için $J_2$+F5 payı orada hâlâ iş görür; Iapetus'ta görmez.

##### (c) Serbestliğin kökeni: baskın kuvvetin düzleme kayıtsızlığı · **[T]** · yapısal

Bu bölümün başında galaktik disk için kurulan zincirin karşıtı, gezegen sistemlerinde geçerlidir:

| | Baskın kuvvet | Düzleme karşı tutumu | Sonuç |
|---|---|---|---|
| **Galakside** | **F4** ($\lambda_{etkin}=+93$, levha) | içkin olarak **düzlemsel** | yörünge diskte hapis |
| **Gezegen çevresinde** | **F1** (küresel) | **kayıtsız** — düzlem tercih etmez | düzlem seçen pay yalnız $J_2$+F5 ⟹ **serbestlik** |

$$\boxed{\;\text{Serbestlik, F5'in zayıflığından değil; BASKIN kuvvetin düzleme kayıtsız olmasından gelir.}\;}$$

Kitap *"küresel kütle-itim düzlem tercih etmez"* tespitini 11.4.5'te zaten yapar; buradaki kayıt onun sonucunu çıkarır. **Geçiş yarıçapının fiziksel anlamı budur:** aranan yer, $J_2$+F5 payının F1'in kayıtsızlığına yenildiği yarıçaptır.

##### (d) Kolektif düzlemin kimliği — **muhasebe ifadesi** · **[T]** · *kuvvet iddiası değildir*

$r_g$'nin dışında düzlemi kolektif dolaşım kurar. Hareket eden her cisim ortamı kendi hareket doğrultusunda şekillendirir; payı deplase ettiği hacim ve dolanım momentiyle ölçülür:

$$w_i=\phi_i\rho_0V_i\,v_ir_i=L_i\frac{\phi_i\rho_0}{\rho_{c,i}}
\qquad\Longrightarrow\qquad
\hat n_{ortam}=\frac{\sum_i w_i\hat n_i}{\left|\sum_i w_i\hat n_i\right|}$$

Spin ile yörünge **aynı toplama** girer. $\phi$ burada **kaynak/pay** terimidir — 11.4.5'in yasakladığı **tepki** kullanımı değildir ($1/\rho_n$ evrenseldir, eşdeğerlik ilkesi gereği); iki kullanım karıştırılmamalıdır.

| Sistem | Çıplak $L$ oranı | $\phi$-düzeltmeli | Kazanan | Gözlem |
|---|---|---|---|---|
| **Uranüs** | $94:1$ | $\mathbf{115:1}$ | **spin** | beş büyük uydu $97{,}77°$ eğik **ekvator** düzleminde ✓ |
| **Satürn** | $79:1$ | $\mathbf{199:1}$ | **spin** | halkalar + Titan ekvatorda ✓ |
| **Güneş Sistemi** | $165:1$ | $\mathbf{99:1}$ | **yörüngeler** | değişmez düzlem; Güneş ekvatoru $6{,}0°$ **dışarıda** ✓ |

Aynı kural, aynı katsayı, **zıt verdikt** — ve üç sistemde de gözlemle uyumlu. $\phi$ düzeltmesi yönü iki taraflıdır (Güneş spini plazma olduğu için $\phi\to1$ ile kazanır; Satürn düşük yoğunluklu olduğu için spini kazanır) ama **hiçbir verdikti çevirmez**: en büyük sapma 2,5 kattır.

> [!WARNING]
> **Bu bir muhasebe ifadesidir, kuvvet ifadesi değildir — ve totolojik yanı beyan edilmelidir.** $w_i\propto L_i$ alındığında $\hat n_{ortam}\equiv\vec L_{top}/|\vec L_{top}|$ olur, yani **tanım gereği** değişmez düzlem. Kural değişmez düzlemi *öngörmez*; ortam düzlemini onunla **özdeşleştirir.**
>
> **Ve arkasında onu tutan bir geri-çağırma yoktur.** Dış alanda ortamın kendi dolaşımını kaynak sayan okuma (aday B) 11.4.3'te elenmiştir; kalan tek kanal R1/$s\!=\!2$'dir ve 1 AU'da merkezcile oranı $1{,}1\times10^{-15}$'tir. Dolayısıyla kural düzlemin **kimliğini** verir, **tutulmasını** vermez. *"Değişmez düzleme doğru bir kuvvet vardır"* biçiminde okunamaz.

##### (e) Ve muhasebe boş değil: $\theta\propto1/L$ · **[T]** · sınanabilir desen

Totoloji kaydı kuralı boşaltmaz, çünkü kimliğin kendisi **kimin dar kimin serbest olduğunu** söyler. $\sum_iL_i\mathbf{i}_i=0$ (eğiklik vektörleri $L$ ağırlıklı olarak birbirini götürür) ⟹ $L_i\theta_i$ çarpımları karşılaştırılabilir olmak zorundadır.

**Jüpiter–Satürn kaldıracı** ($L$'nin %85'i; $L_J\theta_J=L_S\theta_S$, $\theta_J+\theta_S=i_{JS}\approx1{,}25°$):

| | Kimlikten | Gözlenen |
|---|---|---|
| $\theta_J$ | $1{,}25°\times7{,}84/27{,}1=\mathbf{0{,}36°}$ | $0{,}32°$ |
| $\theta_S$ | $1{,}25°\times19{,}3/27{,}1=\mathbf{0{,}89°}$ | $0{,}93°$ |

**%4–13 içinde, sıfır parametreyle.** Kalan sapma Uranüs+Neptün'ün %13'ünden. ⟹ *Jüpiter değişmez düzleme yakındır çünkü değişmez düzlem büyük ölçüde Jüpiter'dir.*

**Ayırt edici kısım — kimlik hafif cisme hiçbir şey dayatmaz, ve gözlem de dayatmıyor:**

| Cisim | $L$ payı | Değişmez düzleme $\theta$ | $L\theta$ |
|---|---|---|---|
| Jüpiter | %60,7 | $0{,}32°$ | $6{,}2\times10^{42}$ |
| Satürn | %24,7 | $0{,}93°$ | $7{,}3\times10^{42}$ |
| Neptün | %7,9 | $0{,}72°$ | $1{,}8\times10^{42}$ |
| Uranüs | %5,4 | $1{,}02°$ | $1{,}7\times10^{42}$ |
| Dünya | %0,084 | $1{,}57°$ | $4{,}2\times10^{40}$ |
| **Merkür** | **%0,0029** | $\mathbf{6{,}34°}$ | $5{,}8\times10^{39}$ |

Merkür, Jüpiter'in **20 katı** eğiktir. Ağırlığı olan dört cisim $0{,}3$–$1{,}0°$ bandında; ağırlığı olmayanlar dağınık — ve aynı serinin devamı düzensiz uydular, Oort bulutunun izotropisi ve yüksek-$i$ Kuiper cisimleridir. **Yanlışlanabilir:** ağır bir cisim değişmez düzlemden uzak bulunsaydı kimlik çökerdi.

> [!NOTE]
> **Kapsam kaydı — burada bir mekanizma borcu YOKTUR.** *"Gezegenleri değişmez düzlemde tutan kuvvet nedir?"* sorusu malformdur: eğiklik korunumlu bir niceliktir, **donmuş niceliği tutmak için kuvvet gerekmez.** Gereken tek şey onu dağıtacak bir kanalın olmamasıdır — ve teori böyle bir kanal getirmez (F5'in 1 AU payı $1{,}1\times10^{-15}$). **F5'in oradaki zayıflığı bir eksiklik değil, tam olarak aranan şeydir.** Bir kanal getirseydi Ay'ın düğüm gerilemesi onu $\kappa_5\lesssim4\times10^{-12}$'ye kilitlerdi — F5'i kitabın **her** kanalında görünmez kılan bir değer (Ek M-22'nin $z$-türetimi; 11.4.3'ün (B) satırı).
>
> Kimlik $\theta_i$ **oranlarını** sabitler, yayılımın **toplam ölçeğini** ($\sim1°$) sabitlemez. O, *"hangi düzlemde oluştular"* sorusudur; cevabı yukarıdaki (a)–(d) zinciridir ve **duran bir yapıya** aittir — geçmişte kalmış bir faza atıf gerekmez. Yayılımın mutlak ölçeği bu bölümün kapsamı dışındadır ve öyle kaydedilmiştir.

---

## 11.4.10 Bölümün Bilançosu

### Kurulan sonuçlar

| # | Sonuç | Statü |
|---|---|---|
| 1 | F5 genlik denklemi: $\hat{\mathcal{Q}}_{et}=\dfrac{\kappa_5\phi_{doy}\mathcal{S}}{2}\mathcal{Q}\left(\dfrac{R_\phi}{R_e}\right)^{6}$; çarpanlar ayrıştırıldı | **[T]** |
| 2 | Basıklığın gradyan sertleştirmesi $\mathcal{S}=\dfrac{\pi/2}{E(e)}=1+\dfrac f2+\cdots$, ve **doyması**: $f\to1$'de $\mathcal{S}\to\pi/2=1{,}571$ — bu kanaldan azami kazanç %57 | **[T]** |
| 3 | Radyal profil **Rankine**: içeride $\propto r$, dışarıda $\propto r^{-(2s+1)}$; tepe $r=R_\phi$'de | **[T]** |
| 4 | Maksimum kümesi: **45° enlem halkaları** — nokta değil, sırt | **[T]** |
| 5 | Dış alan sönüm üssü $s=2$ (dipolar); rakip adaylar Ay'ın düğümüyle elendi | **[T]** |
| 6 | $\nu^2/\Omega^2$'de **tek paritede** $(R_e/r)^3$ terimi — hiçbir kütle çokkutbuyla taklit edilemez | **[T]** · F5'in ilk ayırt edici imzası |
| 7 | $\kappa_5\lesssim2{,}1\times10^{-3}$ (LLR düğümü) — **bölümün referans üst sınırı**, bütün genlikler onunla verilir; gözlemin sabitlediği çarpım $\kappa_5\phi\lesssim1{,}5\times10^{-3}$. Aday üsler $\kappa_5$'ten bağımsız elendi | **[A]** |
| 8 | **Kuvvet–yitim iş bölümü:** $h=\sigma_z/\nu$ — kuvvetler $\nu$'yü ve düzlemi, yitim zinciri $\sigma_z$'yi belirler. Düzlemi F5 seçer; genliği boşaltan kanal teorinin kendi rampa kanalıdır (kapı rampa, ocak temas) | **[T]** |
| 9 | **Dikey sönümün ana kanalı halkanın kendi Evrenakı rampasıdır:** alan aracılı karşılaşmalar (kesit $(r_H/a_b)^2$) dikey modu ortak dolaşıma boşaltır; temaslı çarpışma artığı ısıya çeviren ikincil kalemdir. Bükülme dalgalarının 2,22 katlık sönüm fazlalığı bu kanalın gözlemdeki izidir | **[T]** |
| 9b | **Sönüm bilançosu iki işaretlidir ve termostat kurar:** rampa kanalı kaymanın deposundan beslenip tabanı koyar ($\sigma_z\simeq\Omega r_H$) ve dikey modu boşaltır; temas kanalı artığı ısıya çevirir; ortam kuplajının dikey payı $5\times10^{-10}$. Halka kalınlığı bir sönüm sonu değil **termostattır** — salınım ölmez, dengeye oturur | **[T]** |
| 9d | **Evrenakı rampasının erimi türetildi — serbest kalem kapandı.** $r_H/a_b=R_{y\ddot{o}r}(4\pi\rho_c/9M)^{1/3}$, **tanecik boyundan bağımsız**; ölçüt 11.4.8.1'in zarf erimiyle **aynıdır** (gradyan hâkimiyeti). Tek ölçüt iki ölçek: tanecikte $1{,}0$–$1{,}8\,a_b$, Dünya çevresinde $235R_\oplus$ | **[T]** · ⭐ |
| 9e | **Rampa izotropiktir** ($\omega_2$ pulsasyonundan; nefes alan pompanın yönü yoktur). İki rampa değdiğinde etkileşim başlar ⟹ kesit çarpanı $(r_H/a_b)^2$ = 1,09 (C) … 3,19 (A dışı), **yarıçapla büyür** | **[T]** |
| 9f | **Halka tam bir tanecik çapı kalınlığındadır:** $h\simeq a_b$ ($\Sigma$ sekiz kat, $\Omega$ iki kat değişirken 0,90–1,09 sabit); $h=10$ m ⟹ $a_b=9$–11 m — gözlenen en iri blok boyu. Rampasız hesap aynı $h$ için bölgeye göre $a_b=10$–23 m isterdi ⟹ **rampa göz ardı edilemez** | **[T]** · 11.4.5'in kalınlık kilidinin keskin hâli |
| 9g | **Perkolasyon eşiği:** halka hiçbir yerde rampa-bağlı değil, ama A halkasında eşiğin **%74**'üne çıkar (C'de %23) ⟹ rampa kaynaklı her etki dışa doğru güçlenmeli | **[T]** · ayırt edici |
| 9h | **Kanal seçiciliği rampadan değil dengeden gelir.** İzotropik rampa + anizotropik denge: $v_r^{denge}/\sigma_z=4{,}09$, gözlenen $\nu_{bük}/\nu_{yoğ}=2{,}22$ — aynı mertebe. **Yeni parametre yok** ⟹ Sınav 11.4-H | **[T]** · ⭐ yapısal |
| 9c | **Parametresiz kalınlık öngörüsü:** $\sigma_z\simeq\Omega a_b$ tabanı ve halkanın kendi kuyusuyla $\;h/a_b=\sqrt{1+\Lambda^2}-\Lambda$, $\Lambda=2\pi\mathcal{G}\Sigma/\Omega^2a_b$. Halka **bir tanecik çapından ince olmak zorundadır** ve inceliği $\Lambda\propto\Sigma/\Omega^2$ belirler — sıralama Kepler'inkinin tersine döner. Üç girdi de bağımsızca ölçülü ⟹ **Sınav 11.4-G** | **[T]** · ⭐ ayırt edici |
| 10 | $\mathcal{Q}/J_2$ = dönüşün figüre soğurulmayan payı; Satürn birinci (9,68) | **[T]** |
| 11 | $\mathcal{P}_5$ gezegenden gezegene 1,5 kat içinde (%0,046–0,068): $\mathcal{Q}/J_2$ ile $(R_\phi/R_e)^6$ büyük ölçüde birbirini götürür — $J_2$ kanalının göstermediği bir evrensellik. Payda birinci **Uranüs**, mutlak ezmede **Satürn** | **[T]** · ayırt edici öngörü |
| 12 | **$\phi$ iç yoğunluk profilinden türetildi:** $\phi(\rho)=\min(\rho/\rho_*,\phi_{doy})$; $\rho_*$ dışlanan hacimden, $\phi_{doy}$ **fazdan**. Su ve manto üzerinde $\pm$%13 kalibre. $\phi_\oplus=0{,}70$, $\phi_{Satürn}=0{,}45\pm0{,}03$ | **[T]** |
| 13 | **Deplasman yüzeyi $R_\phi$ ve referans yarıçapın türetimi.** Basıklığın *nedenini* arayan hesap basılmış gövdenin $R_e$'sini kullanamaz; başlangıç hacmi eşdeğer **ideal küredir** ($R_{ort}=R_e(1-f)^{1/3}$). Zincir: $R_\phi/R_e=(R_\phi/R_{ort})\cdot(1-f)^{1/3}$ — Satürn $0{,}9040$, Jüpiter $0{,}9444$, Uranüs $0{,}9516$, Neptün $0{,}9624$; doygun yüzeyli gövdede çarpan $(1-f)^2$ | **[T]** · serbest parametre yok |
| 14 | Metalik/plazma fazda $\phi=1-\delta$, $\delta\lesssim10^{-13}$; iyonizasyon $\phi$'yi **artırır** ve geçiş süreklidir | **[T]** |
| 15 | **$10^{28}$'lik kanal ayrımı:** M-43'ün $v^4$ bastırması + DY-2'nin kayma yasası ⟹ ortam kuplajı yörünge kanalında dikey kanaldan $1{,}5\times10^{28}$ kat etkin ($r_t$ sadeleşir, parametresiz) | **[T]** |
| 16 | Ortamın orbital torku **daima dışa**dır ⟹ halka yağmuru bu kanalın işi değildir; standart mekanizmalardan ayrışma yönden ve profilden gelir, tanecik boyundan değil | **[T]** |
| 17 | **$\eta_E\lesssim2{,}3\times10^{-11}$ Pa·s** — Phoebe'den $1{,}4\times10^{6}$ kat sıkı; kitaptaki en sıkı $\eta_E$ kısıtı. Dünya yörüngesi bağımsız çapraz denetim verir | **[A]** |
| 18 | **Fizeau muhasebesi:** yoldaki ortalama ortam hızı $\phi v_{madde}+(1-\phi)v_{ambiyans}$; rezonatörde $(1-\phi)V$ ⟹ serbest-Evrenakı yolu en kısıtlayıcı, katı yol $1/n^4$ ile zayıf | **[T]** |
| 19 | **Kavrama yoluyla izotropi tükenmiştir:** üç kanal, gereken $>1-3{,}2\times10^{-5}$ tamlığın en az $10^4$ kat altındadır. İzotropi bu yüzden ortam taşınarak değil, **madde kısalarak** sağlanır (kalem 21) | **[T]** |
| 20 | **Zarfın erimi türetildi:** gradyan hâkimiyeti (Hill), $235R_\oplus$ · $1086R_S$ | **[T]** |
| 21 | **Kinematik ölçek terimi $\Lambda_{kin}=\sqrt{1-V^2/c_0^2}$ türetildi** — sıkıştırılabilir ortamda hareketli deplasman kaynağının alanından (Prandtl–Glauert). Cetvel ve saat aynı çarpanla ölçeklenir; ışık hızı izotropisi **kavramadan bağımsız** çıkar, yeni parametre eklenmez. Kapalı biçim, gözlemin istediği tam Lorentz çarpanıdır | **[T]** |
| 22 | Disk F5'in **geometrik** dengesidir ($\sin2\theta\to0$): kuvvet düzlemde susar, sapmada konuşur — söndürme değil **kilit**. *(Kinematik bir sabit nokta yoktur: 11.4.9'un $\lambda_{etkin}$ türetimi diskin F5'i kinematik olarak kapatmadığını gösterir.)* | **[T]** |
| 22b | **$\lambda$ serbest değildir, türetilir:** $\lambda_{etkin}=\dfrac{d\ln v_c}{d\ln R}+\dfrac{\mathcal{A}}{2}\left(\dfrac{R}{h_z}\right)^2$ — M-38'in iç içe tabakası + DY-2'nin kayma yasasından. İkinci terim birinciyi üç mertebe ezer ($93$ ↔ $0{,}06$). Barotropik akışkan teoremleri (Poincaré–Wavre) **uygulanamaz**: ortam barotropik değildir | **[T]** · yöntem kaydı |
| 22c | **$(R/h_z)^2$ yasasının tabanı var:** ortamın **dolaşım tutarlılık ölçeği** $\ell_{min}$. F1 statik tepkidir, her ölçekte çalışır (Newton korunur); F5 dolaşım gradyanı okur ve altında desen kuramayacağı bir ölçek vardır. Satürn halkası alttan sınırlıyor: $\ell_{min}\gtrsim7$–65 km. Halka ($10$ m) yasanın dışında, gövde ve galaktik levha ($10^{7}$–$10^{19}$ m) içinde kalır | **[T]** + **[A]** · yeni büyüklük |
| 23 | **Levha yükseltmesi:** $\mathcal{F}_5^{levha}=\dfrac{\mathcal{A}\,\kappa_5}{4}\left(\dfrac{R}{h_z}\right)^2$ — küresel okumanın 2–3 mertebe üstünde. **İki çarpan da teorinin kendi büyüklüğü:** geometri $(R/h_z)^2$, F4'ün radyal payı $\mathcal{A}$. Yeni parametre yok | **[T]** |
| 24 | **Galaktik yassılığın mimarı F5'tir:** enerji hanesini yitim (bulut çarpışmaları, ışınım) kapatır, çöküşün düzlemini ve kilidini F5 yazar — F1 kayıtsız, figür çokkutbu $10^{-30}$; levha içinde $\mathcal{F}_5$ O(0,1–1) ve kilit pozitif geri beslemelidir | **[T]** |
| 25 | **F5'in dikey paydaki oranı $h_z$'den ve özçekimden bağımsızdır:** $x=\dfrac{\mathcal{A}\,\kappa_5}{4}\left(\dfrac{v_c}{\sigma_z}\right)^2$. Teori diski aşırı belirlemez; Güneş komşuluğunda $x\simeq0{,}1$ — F5 tabakayı taşımaz, onda bir mertebesinde katkı verir | **[T]** |
| 26 | **Oort limiti bağlayıcı sınır DEĞİLDİR.** $\kappa_5\le\dfrac{4x_{maks}}{\mathcal{A}}\left(\dfrac{\sigma_z}{v_c}\right)^2$; ölçüm baryon-baskın iç diskte yapıldığı için $\mathcal{A}\lesssim0{,}3$ ve sınır $\gtrsim2{,}7\times10^{-3}$ — LLR'nin $2{,}1\times10^{-3}$'ünden gevşek. **Galaktik kanal hiçbir öngörüyü küçültmez** | **[A]** |
| 26b | **$\mathcal{F}_5\propto\mathcal{A}$ iki zıt ihtiyacı birlikte karşılar:** iç diskte zayıf (Oort'u kurtarır, $\mathcal{F}_5\simeq0{,}10$), dış diskte güçlü (§6.5.4.1'in $h_d=$ sabit koşulunu taşır, $\mathcal{F}_5\simeq0{,}92$). Ayarlama yok — F4 ile F5 aynı alanın iki izdüşümü olduğu için zorunlu | **[T]** · yapısal |
| 27 | **Dejenerasyonu kıran ölçeklendirme:** F5'in dikey fazlalığı $\propto\mathcal{A}v_c^2/h_z^2$; bir kütle dağılımının ise $\propto v_c^2q(\text{şekil})/R^2$. F5 baryon kesrine **ve** tabaka kalınlığına duyarlı, kütle ikisine de değil ⟹ Sınav 11.4-F | **[T]** · ayırt edici |
| 28 | **Warp F5'i açıklamaz — F5 warpı bastırır.** Zorlanmış bükülme genliği tam olarak $1-x$ ile küçülür (tork oranda sadeleşir): dış diskte **%70'e iner.** Bu bir sınır değil, **parametresiz bir sapma öngörüsüdür.** Mutlak koşul $x\le1$ LLR'den bir mertebe gevşektir. Warpın **başlangıç yarıçapı** açıklanmaz | **[T]** · kapsam sınırı açık |
| 28b | **F5'in warp presesyonundaki payı %3–8** (katkı $0{,}15$–$0{,}41$ km/s/kpc; gözlem tabanı $4{,}86\pm0{,}88\pm2{,}14$ km/s/kpc). Devinimin **rijit** (yarıçaptan bağımsız) ölçülmesi, 3.8.7'nin *"sarılma problemi doğmaz"* kaydının arkasına ölçüm koyar — standart çerçeve rijitlik için **prolat hale** ister | **[A]** + **[T]** |
| 29 | **Geçiş yarıçapı türetildi:** $r_{geçiş}^5=2J_2R_e^2a_p^3M_p/M_\odot$ — $J_2$+F5 payının Güneş torkuna yenildiği yer. **5 sistem, 10 cisim, sıfır serbest parametre; 10/10.** Uranüs ayırt edici ($97{,}77°$ eğiklikte beş uydu $r_g$ içinde ve ekvatorda), Iapetus tam sınırda ($1{,}42\,r_g$) | **[T]** · ⚠ **F5 sınavı DEĞİL** (kalem 30) |
| 30 | **Dürüst kayıt:** $r_g$'de F5'in $J_2$'ye oranı $4{,}9\times10^{-5}$, yarıçapa etkisi $\sim10^{-5}$ ⟹ ölçülemez. Teori $r_g$'yi ancak **$J_2$'yi türetmesi** üzerinden sahiplenir; tutan şey standart **Laplace yarıçapıdır.** Saf-$P_2$ dejenerasyonuyla tutarlı | kapsam kaydı |
| 31 | **"Serbestlik" nicelleşti:** düzlem seçen pay halkada $8{,}0\times10^{-3}$, Titan'da $5{,}9\times10^{-5}$, Iapetus'ta $7{,}0\times10^{-6}$ — **bin kat düşüş** | **[T]** |
| 32 | **Serbestliğin kökeni yapısaldır:** F5'in zayıflığından değil, **baskın kuvvetin düzleme kayıtsızlığından** gelir. Galakside baskın F4 içkin düzlemsel ($\lambda_{etkin}=+93$) ⟹ hapis; gezegen çevresinde baskın F1 kayıtsız ⟹ serbestlik. $r_g$'nin fiziksel anlamı budur | **[T]** · yapısal |
| 33 | **Kolektif düzlemin kimliği — muhasebe ifadesi:** $w_i=L_i\phi_i\rho_0/\rho_{c,i}$, $\hat n_{ortam}=\widehat{\sum w_i\hat n_i}$. Aynı kural zıt verdikt verir ve üçü de tutar: Uranüs $115{:}1$ **spin** ✓ · Satürn $199{:}1$ **spin** ✓ · Güneş Sistemi $99{:}1$ **yörüngeler** ✓ ($\phi$ düzeltmesi hiçbir verdikti çevirmiyor, en büyük sapma 2,5 kat) | **[T]** · ⚠ **totolojik; kuvvet iddiası değil** |
| 34 | **Ve muhasebe boş değil:** $\sum_iL_i\mathbf{i}_i=0$ ⟹ $\theta\propto1/L$. J–S kaldıracı $0{,}36°/0{,}89°$ ↔ gözlenen $0{,}32°/0{,}93°$ (%4–13, sıfır parametre); **hafif cisim serbest** — Merkür $6{,}34°$, Jüpiter'in 20 katı. Ağır bir cisim düzlemden uzak bulunsaydı kimlik çökerdi | **[T]** · sınanabilir desen |
| 35 | **Eş-düzlemlilik için mekanizma borcu yoktur.** Eğiklik korunumludur; donmuş niceliği tutmak için kuvvet gerekmez, gereken tek şey dağıtacak kanalın olmamasıdır. **F5'in 1 AU'daki zayıflığı ($1{,}1\times10^{-15}$) eksiklik değil, aranan şeydir** — kanal getirseydi Ay'ın düğümü $\kappa_5\lesssim4\times10^{-12}$'ye kilitlerdi (11.4.3'ün (B) satırı). Yayılımın mutlak ölçeği ($\sim1°$) kapsam dışı | **[T]** · kapsam kaydı |
| 36 | **$v_\theta^2(R,z)=4\mathcal{G}MR^2/r^3$ türetildi** (Ek M-22): silindirik/küresel çatalı teorinin kendi denklemlerinden kesilir, $z$ bağımlılığı **çıktıdır** (Poincaré–Wavre uygulanamaz). Dikey gradyanı aday (B)'yi **bağımsız olarak ikinci kez eler** — $\dot\Omega=-\tfrac32\kappa_5n$ ⟹ $\kappa_5\lesssim3{,}9\times10^{-12}$, yani 11.4.3'ün (B) satırının ($6\times10^{-12}$) tam $\tfrac32$ katı sıkı | **[T]** · 11.4.3'ün elemesini yeniden üretir |
| 37 | **$\sin2\theta$ yasası R1'e özgüdür** (Ek M-39): genel yasa $\propto\lambda\cos^{2\lambda-1}\theta\sin\theta$, katı cisim $\lambda=1$. Ayrım *"R2 geçerli mi"* değil **"ortam nasıl örgütlü"**: levhada $\lambda_{etkin}=+93$ (R2 geçerli, kaynağı F4'ün tabakaları), gezegen çevresinde $-0{,}375$ (**zayıf ve ters işaretli**) | **[T]** · kapsam |

### Bölümün üç yapısal tespiti

| Tespit | Nicel karşılığı |
|---|---|
| **Dönüş hızı F5'i (ve F4'ü) birlikte büyütür** | $f_{yanal}\propto v_e^2$; ikisi de $\omega_1$ kökünden gelir ve ayrı ayarlanamaz. Boyutsuz taşıyıcı $\mathcal{Q}=\omega^2R_e^3/\mathcal{G}M$. |
| **Basıklık gradyanı sertleştirir — ama iki zıt kanaldan, ve doyarak** | Meridyen kısalması $\mathcal{S}=1+f/2$ genliği **artırır** (Satürn'de %5) ama $\pi/2=1{,}571$'de **doyar**; figür soğurması ise ölçülebilir payı ($\propto\mathcal{Q}/J_2$) **azaltır.** Mutlak büyüklüğün taşıyıcısı $\mathcal{Q}$, ölçülebilir payınki $\mathcal{Q}/J_2$'dir. Sınırsız olan tek geometrik kanal $R/h_z$'dir ve yalnız levhalarda devreye girer (11.4.9). |
| **Kutupta sıfır; uzaklaşınca önce artar sonra azalır** | Kutupta $\sin2\theta=0$ — geometrik özdeşlik, yaklaşım değil. Radyal profil Rankine'dir ve tepe **deplasman yüzeyindedir** ($R_\phi$): Satürn'de $0{,}935R_e$, karasal cisimlerde ekvator yarıçapının kendisi. Enlemsel tepe 45°'dedir. |

### Sınavlar

| # | Sınav | Durum |
|---|---|---|
| **11.4-A** | Satürn bükülme dalgalarında tek-parite $(R_e/r)^3$ artığı; öngörülen katsayı $\hat{\mathcal{Q}}_{et}=4{,}5\times10^{-5}$ | Veri hazır (Cassini); analiz yapılmadı. **F5'in ilk yürütülebilir doğrudan sınavı** |
| **11.4-B** | Ay'ın düğüm artığında **0,10 mas/yıl** bileşeni (LLR, 50+ yıllık seri) | Öngörü eşikte |
| **11.4-C** | 45° enlem sırtı: gaz devi atmosferlerinde orta enlem akış deseni, Dünya mantosunda gerilme imzası | Aranmadı |
| **11.4-D** | Saydam iletkende Fizeau: ara bölge taşıyıcı yoğunluğu $n_c\gtrsim6{,}8\times10^{27}$ m⁻³'yi geçince $f>1-1/n^2$. En iyi şeffaf iletken oksitler eşiğin 7 kat altında ⟹ onlarda etki beklenmez | Metal/plazma $\phi\to1$ tezinin tek laboratuvar sınavı |
| **11.4-H** | **Bükülme dalgası viskozite fazlalığının $(A_V\Omega)/\sigma_z$ ile ölçeklenmesi.** Rampa izotropiktir; seçicilik dengenin anizotropisinden gelir ⟹ fazlalık, dalganın yerel dikey denge dispersiyonuna oranıyla büyümelidir. Ayrıca rampa kesiti $(r_H/a_b)^2$ yarıçapla büyüdüğü için etki **dışa doğru güçlenmelidir** (C 1,09 → A 3,19) | Üç bükülme dalgası biliniyor (Mimas 5:3, Iapetus $-1{:}0$, Titan $-1{:}0$); yalnız birinde $\nu$ ölçülü. Öz-çekim izi açıklaması bu ölçeklemeyi öngörmez |
| **11.4-G** | **Halka kalınlığı ↔ yüzey yoğunluğu ↔ tanecik boyu.** $h/a_b=\sqrt{1+\Lambda^2}-\Lambda$, $\Lambda=2\pi\mathcal{G}\Sigma/\Omega^2a_b$ — serbest parametresiz. İki keskin ifade: **(a)** $h<a_b$ her zaman; **(b)** eşit $a_b$'de kalınlık $\Lambda\propto\Sigma/\Omega^2$ ile düşer — bu ölçünün en büyüğü A halkasındadır ve A, C'den iki kat ince çıkar (Kepler tek başına tersini, iç halkanın ince olmasını verirdi) | Üç girdi de Cassini verisinde mevcut: yoğunluk dalgaları ($\Sigma$), örtülme boyut dağılımı ($a_b$), yıldız örtülmesi/kenar difraksiyonu ($h$). **Analiz yapılmadı** |
| **11.4-F** | **Dikey fazlalığın $\mathcal{A}$ ve $h_z$ ile ölçeklenmesi.** F5 varsa dinamik/sayılan dikey kuvvet oranı $1+x$, $x=\tfrac{\mathcal{A}\kappa_5}{4}(v_c/\sigma_z)^2$ ile değişmeli: **radyal eksik kütle payıyla orantılı, tabaka kalınlığının karesiyle ters.** Bir kütle dağılımının dikey/radyal oranı ise yalnız şekline bağlıdır — ikisine de duyarsız. Galaksi içi test olduğu için uzaklık, eğim ve $M/L$ sadeleşir | Dış galaksilerde dikey dinamik veri var; tarama yapılmadı |

> **Bu listede olmayan bir madde.** Işık hızı anizotropisi bir sınav değildir: kinematik ölçek terimi anizotropiyi **her yol için tam olarak** sıfırlar — serbest Evrenakı, sıvı, katı dielektrik ayrımı yapmaz (11.4.8.1). Teori bu kanalda standart fizikle aynı öngörüde bulunur; ayrım aranacak yer $M\to1$ rejimidir (kalem 11.4-iv).

### Açık kalemler

- **11.4-i** — Halka optik derinliği bütçesi: Roche kuşağı ↔ buz çizgisi ↔ kütle kaybı ömrü. *S4'ün cevaplanmayan yarısı; teorinin kapsamı dışında ama cevaplanması gereken soru.*
- **11.4-ii** — Galaktik levhanın dikey denge hesabı: F5 ↔ ortamın basınç desteği ↔ baryonik özçekim, üçü birlikte. *(Düzleşmenin **kendisi** artık açık kalem değildir: 11.4.9 onun yitimli olduğunu ve F5'in kapsamı dışında kaldığını gösterir.)*
- **11.4-iii** — Ortamın prograd torkunun sistematik taraması. Halka ve Dünya yörüngesi ilk iki sınavdır; en duyarlı adaylar $\Delta v^4/r_t$ oranı büyük olanlardır (halka tanecikleri, iç uydular, sıcak Jüpiterler, ikili pulsarlar).
- **11.4-iv** — **$\Lambda_{kin}$'in doğrusal-olmayan rejimi.** Türetim doğrusallaştırılmış ortam tepkisinde kapalıdır (11.4.8.1) ve tam Lorentz çarpanını verir. Açık kalan üç kalem: **(i)** $M\to1$ civarında Prandtl–Glauert biçiminin bozulması — teorinin Lorentz fenomenolojisinden ayrıldığı tek yer; **(ii)** $\Lambda_{grav}\cdot\Lambda_{kin}$ çarpım yapısının derin kuyuda hızlı hareket için öngörüsü; **(iii)** boyuna salınıcının frekans kısalmasının alan dönüşümünden doğrudan gösterimi (enine ışık-saati yolu kapalıdır).
- **11.4-vii** — **$\ell_{min}$'in üst sınırı ve ilk-ilkelerden değeri.** Halkalar alttan sınırladı ($\gtrsim7$–65 km); ortamın dolaşım deseninin tutarlılık ölçeğini neyin belirlediği türetilmemiştir. $\ell_\omega$ ailesiyle ilişkisi (M-38/M-45) ilk bakılacak yerdir.
- **11.4-vi** — **$\mathcal{A}(R)$ ve $g(z)$: F5'in galaktik hanesinin tek açık hesabı.** İki kalem: **(i)** $\mathcal{A}(R)$, Kısım 6'nın kendi F1/F4 ayrışımından okunmalıdır — burada temsilî değerlerle çalışıldı; **(ii)** $g(z)=\rho_*(z)/\rho_*(0)$ profilinin biçimi $\lambda_{etkin}$'in katsayısını iki kat kaydırır ($\mathrm{sech}^2$ ↔ Gauss), ve $\mathcal{A}_{etkin}\gtrsim0{,}5$ bölgesinde Oort limiti yeniden bağlayıcı olur. İkisi birlikte hem Oort kısıtının hem warp bastırmasının kesin değerini verir.
- **11.4-v** — **Sürüklenme zarfının kavraması: dördüncü kanal.** Üç mevcut kanal, izotropinin gerektirdiği tamlığın en az $10^4$ kat altındadır; dördüncü bir kanal gerekiyor (11.4.8.1, ve DY-2'nin kalan kalemler notu). **Teorinin en ciddi açık kalemi.**
- **11.4-v′** — Metalik hidrojenin yoğunluk modülasyonundan $\delta$'nın tam hesabı. F5 için gereksiz (karantina), 11.4-D'nin öngörüsünü keskinleştirir.
- **11.4-viii** — **Prograd tercih ve dairesellik için gerçek mekanizma.** Bu iki kalem M-37'nin $\tau_{ret}=2\rho_ca_b^2/9\eta_E$ kanalına bağlanıyordu; geri alındı (Ek M-37, "Sonuç geri alındı"; 11.4.9'un uyarı kutusu). Gerekçe: kitaptaki $\eta_E$ sınırının kendisi, M-43'ün $\Delta v^4$ yasasıyla, tanım gereği *en hızlı sönen durumun bile sönmediği* yerden (Phoebe, yörünge kanalı) okunuyor; retrograd/prograd farkı ($3^4=81$) bu sınırı aşamıyor, dikey kanalda fark daha da büyük ($10^{31}$, 11.4.5).
  > **Eş-düzlemlilik bu kalemde YER ALMAZ** — kapalıdır (11.4.9-(e)). Sebebi bir mekanizma bulunması değil, **sorunun malform olmasıdır:** eğiklik korunumlu bir niceliktir, tutulması için kuvvet gerekmez; ve dar bant diye tarif edilen şey $\sum_iL_i\mathbf{i}_i=0$ kimliği yüzünden $L$ payı büyük cisimlerin dar olmak **zorunda** olmasıdır ($\theta\propto1/L$; hafif cisimler dar değil — Merkür $6{,}34°$). Teorinin bu kalemde borcu yok; tersine, F5'in dış alandaki zayıflığı gerekli koşulu sağlıyor. **Kalan iki kalem açıktır, ama artık farklı statüde:**
  > - **Dairesellik — yitimli kanal BULUNDU, menzili yetmiyor.** Yitimli olma şartı Ek M-44'ün korunumluluk ölçütüyle karşılanır: gelgit lobu küresel simetriyi kırar, $\nabla\rho$ ile $\nabla\chi$ hizasızlaşır, dolayısıyla lob kanalı gerçekten enerji söndürür. Ve 11.5.5 kanalın menzilini gözlenen çembersellik kesim periyodundan kalibre ederek dokuz cisimde ölçer: WASP-12b $7{,}4\times10^{3}$ · Io $1{,}6$ · Ay $5{,}1\times10^{-4}$ · **Dünya $1{,}2\times10^{-11}$.** ⟹ Kanal yakın çift ve düzenli uydu rejiminde çalışır, **gezegen rejiminde $9$–$13$ mertebe ölüdür.** Kalemin eksiği artık nitel değil **nicel**: aranan şey $(R_b/a)^5$ ile ölmeyen bir kanaldır, ve ölçeklemesi doğru yönde olan tek aday ortam kuplajıdır (11.5-iv).
  > - **Prograd tercih — dokunulmamıştır.** Lob kanalının işareti senkron yarıçapta döner, dolayısıyla küresel bir prograd seçiciliği yoktur. *"Retrogradlar daha hızlı içe göçer ⟹ hayatta kalanlar prograddır"* argümanı ise M-37'nin kendi geri alma gerekçesine çarpar: kitaptaki $\eta_E$ sınırı **Phoebe'den** okunur, yani $4$ Gyr hayatta kalmış bir retrograd cisimden, ve $3^4=81$ çarpanı o sınırı aşamaz.

> **Bölümün tek cümlelik sonucu.** Halka, F5'in eseridir: düzlemi F5 seçer ve bastırır — doğrudan payı ortamdaki canlı deplasman alanı, dolaylı payı aynı dönüşün maddeye çökelmiş fosili olan figürdür —; dikey salınımı halkanın kendi **Evrenakı rampası** sönümler ve kalınlığı parametresiz $h\simeq a_b$'ye kilitler; temaslı çarpışma bu zincirde artığı yakan ikincil kalemdir. Aynı kuvvet levha geometrisinde $(R/h_z)^2$ ile mertebelenir ve galaksilerin yassılığını yazar. Ve F5, hiçbir kütle dağılımının üretemeyeceği tek-parite $(R_e/r)^3$ imzasıyla, halka frekanslarında **ölçülebilirdir.**

---

## 11.4.11 Halka Bandının Radyal Sınırları Teoriden Çıkar mı?

Bölümü kapatmadan önce, 11.4.7'nin bıraktığı soru doğrudan sorulmalıdır: **F5 halkanın nerede başlayıp nerede bittiğini belirler mi?** Cevap hayırdır, ve gerekçesi üç kalemde niceldir. Kalem, 11.4.10'un açık kalemler listesinde **11.4-i** olarak zaten kayıtlıdır; burada yalnız sınırın nereden geldiği gösterilir.

**1. Dış sınır Roche kuşağıdır ve F1'in hanesindedir.** A halkasının dış kenarı ($2{,}269\,R_e$), kütle-itim gradyanının bir gövdeyi kendi bağından hızlı ayırdığı yarıçaptır — 11.4.7'de hesaplandı: $r_{Roche}=2{,}23\,R_e$, gözlenenle **%2 içinde**. Bu sınır tümüyle F1'in ve taneciklerin kendi bağının işidir. F5'in oradaki katkısı $\mathcal{F}_5=3{,}8\times10^{-6}$'dır, yani Kepler geri çağırmasının milyonda dördü; radyal bir bağ kurma ya da koparma kapasitesi yoktur.

**2. İç sınırı da teori koymaz — ve bunu 11.4.8 zaten kapatmıştır.** D halkasının iç kenarında ($1{,}110\,R_e$) madde gezegenin üst atmosferine dökülür (*halka yağmuru*). Ortamın artık kuplajının torku ise **daima dışadır** (DY-2: ortam her yarıçapta maddeyi önden geçer), yani işareti gözlenen akışın tersidir. Dolayısıyla iç sınır Evrenakı kanallarının ürünü olamaz; standart mekanizmalara aittir — manyetosfer–iyonosfer kuplajı, plazma sürüklemesi, mikrometeorit bombardımanı.

**3. F5'in belirlediği şey genişlik değil, frekanstır.** $s=2$ ile F5 $r^{-5}$ düşer ve bandın tamamı yakın alanın içinde kalır (11.4.7). Bu, halkanın *nerede* duracağını değil, orada duran bir halkanın dikey salınım frekansında hangi imzayı taşıyacağını belirler: tek paritede $(R_e/r)^3$ terimi (11.4.4).

**Sonuç.** Halka bandının genişliği bir denge değil, bir **bütçedir** — Roche kuşağı, buz çizgisine göre konum ve kütle kaybı ömrü arasında sıkışmış tarihsel bir sonuç. Teorinin iddiası bu bütçeyi hesaplamak değildir; iddiası, o bütçe ne olursa olsun, bandın içindeki halkanın düğüm frekanslarında hiçbir kütle çokkutbunun taklit edemeyeceği bir artık bırakacağıdır (Sınav 11.4-A).
