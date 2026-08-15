# ÇALIŞMA DOSYASI — Atom Spektrumları ve Kesikli Yapı (Rydberg/Bohr)

> # ✅ DOSYA TAMAMLANDI — 10 Ağustos 2026 · **§12 ile revize edildi**
> **Bütün kalemler kapandı; açık iş yoktur.** Bu dosya bundan sonra **gerekçe arşivi** olarak durur: elenmiş yolların sayısal kayıtları, denetim sonuçları, dört yasak ve hükümlerin gerekçeleri burada; yayın metni yalnız sonuçları taşıyor. Yeni bir kalem açılmadıkça bu dosyaya iş listesi olarak bakılmamalıdır.
>
> ⚠️ **ÖNCE §12'Yİ OKU.** 9.11 denetimden `CIDDI_SORUN` ile döndü ve iki mekanizma **değişti** (yarıçap: kuvvet dengesi → çevre paylaşımı; ritim: Kepler dolanma → duvar frekansı). Aşağıdaki §4–§10'un bazı hükümleri **yürürlükten kalkmıştır**; hangileri olduğu §12.5'te listelidir. Bu bölümler kayıt olarak duruyor, hüküm olarak değil.
>
> **Ne kapandı:** kabuk sayıları · dışlama mekanizması · yarıçap oranları · $1/n^2$ biçimi · Rydberg–Ritz · harmoniğin yokluğu (+ *harmonik ⟺ iki merkez* öngörüsü) · karşılıklılık ikilemi (§11) · mutlak ölçek (parite kararı)
> **Ne havale edildi:** bileşik yapıların tayfı ve yönlü kimyasal bağ → *Kimyasal Bağ* / *Atomların İşleyişi* (7.4 md. 6-d)
> **Ne borç olarak kayda geçti:** ışıma şiddetleri — altı kalem (7.4 md. 6-c)
>
> **Taşınan yerler:**
> | Yer | İçerik |
> |---|---|
> | `Kisim_2/01_Mikro_Evren.md` (2.1) | "Kabuk Sayıları" notu: $2k^2$ geometrisi, tek yörünge + yük itmesiyle dışlama, $r\propto N$ ile $1:4:9:16$, ve **parite hükmü** |
> | `Kisim_1/03_Evrenaki_Postulasi.md` | Parametre çizelgesi **satır 1-b**: $a_0$, rozet **S**, sabitleyen gözlem Rydberg sabiti |
> | `Kisim_8/08_Sembol_Sozlugu.md` | $a_0$ satırı |
> | `Kisim_7/04_Tartisma_ve_Sonuc.md` | **madde 6-b**: ne kapandı, ne açık kaldı; parite ilanı; on elenmiş yol kaydı |
> | `Kisim_2/99_Kaynakca.md` | Güler, *Atom Geometrisi* |
| `Kisim_2/01_Mikro_Evren.md` (2.1) | **Harmonik bölümü:** neden harmonik değil + *harmonik ⟺ iki merkez* öngörüsü (CO/Landau/Zeeman tablosu, $l$-yozlaşması kanıtı) |
| `Kisim_9/02_Planck_Sabiti_ve_Kuantum_Eylemi.md` | **"Soğurma ile Yayma Birbirinin Tersi Değildir"** — §11'in hükmü (asimetri kurucudur; konumlar ortak merdivenden, hızlar yönden) |
| `Kisim_7/04_Tartisma_ve_Sonuc.md` | **md. 6-c** ışıma şiddetleri programı (altı borç) · **md. 6-d** seri içi havaleler |
>
> **Açık kalem yoktur.** Mutlak ölçek borç olmaktan çıkmış, **ilan edilmiş ölçülen girdi** olmuştur ($a_0$, Ek C satır 1-b). Yönlü kimyasal bağ ve bileşik tayfları serinin sonraki kitaplarına havale edilmiştir (7.4 md. 6-d).

> **Durum:** GEREKÇE ARŞİVİ · **Son güncelleme:** 10 Ağustos 2026
> **Kaynak Eksik Envanteri:** Madde 1.1 (Atomun kesikli yapısı: spektrum + Pauli + orbital)
> ⚠️ Bu dosya yayın metni değildir; `app.js`'e kayıtlı değildir.

## 1. Problem Tanımı
Evrenakı teorisine göre ışık bir dalga değil, ardışık Zerre'lerin katarıdır ve **ışığın frekansı, kaynağın (atomun) ardışık Zerre fırlatma (ateşleme) ritmidir** (Bölüm 2.3.1).
Standart fizikte hidrojen atomu (ve diğer elementler) ısıtıldığında her frekansta değil, yalnızca çok spesifik ve **kesikli** frekanslarda (Balmer, Lyman, Paschen serileri) ışıma yapar.

Eğer ışığın frekansı doğrudan kaynağın mekanik bir ritmi ise, **"Atom neden yalnızca belirli ritimlerde ateşleme yapar?"** sorusu teorinin kendi akışkanlar dinamiği sınırları içinde yanıtlanmak zorundadır.

---

## 2. RAKİBİN GERÇEK GÜCÜ — bu bölüm hafife alınmamalı

> ⚠️ **Kayıt (10 Ağu 2026):** Bu dosyanın ilk hâli standart fiziğin kesikliliği *postüla ettiğini* ima ediyordu. **Bu yanlıştır ve düzeltilmelidir**, aksi hâlde ilk hakem itirazı buradan gelir.

**Kesiklilik standart fizikte türetilmiştir, varsayılmamıştır.**
- **Bohr (1913)** kesikliliği gerçekten *postüla etti* — açıklamadı.
- **Schrödinger (1926)** onu **türetti**: Coulomb potansiyelinde bağlı durum için dalga denklemi çözülür, $\psi$'nin sonsuzda sıfıra gitmesi (normalize edilebilirlik) koşulu konur ve özdeğerler kendiliğinden kesikli çıkar ($E_n=-13{,}6/n^2$ eV). Kesiklilik, **sınırlı bölgeye hapsedilmiş dalga probleminin teoremidir** — telin belirli notaları vermesiyle aynı matematik.

**Standart fiziğin gerçekten açıklamadığı şey bir katman aşağıdadır:** dalga denklemi neden geçerlidir, $\hbar$ neden vardır. **Evrenakı'nın iddiası bu düzeyde kurulmalıdır** — "kesikliliği biz açıklıyoruz, onlar açıklamıyor" değil, *"kesikliliğin altındaki mekanik tabanı biz veriyoruz."*

### 2.1 Hangi barı aşmamız gerekiyor — ve hangisini aşmamız gerekmiyor

| Sistem | Standart fiziğin durumu |
|---|---|
| **Hidrojen** (ve H-benzeri iyonlar) | **Tam analitik çözüm.** 1S–2S geçişi $\sim10^{-15}$ bağıl hassasiyette ölçülü; Rydberg sabiti $\sim10^{-12}$ |
| Helyum (2 elektron) | Analitik çözüm **yok**; yüksek hassasiyetli varyasyonel hesap $\sim10^{-9}$ uyum |
| H₂⁺ (tek elektron, iki çekirdek) | Born-Oppenheimer içinde **analitik** (uzatılmış küresel koordinatlar) |
| Hafif çok-elektronlu atomlar | Sayısal (Hartree-Fock, CI, coupled-cluster) — türetim değil, hesaplama |
| Ağır atomlar (lantanit/aktinit) | Tipik %0,1–1; karmaşık konfigürasyonlarda daha kötü |
| Moleküller (H₂ dâhil) | Kapalı form yok |
| **Tüm elementler** | NIST ASD'de **ölçülü** — ölçüm, türetim değil |

**Kapalı form yalnız tek elektronlu sistemlerde vardır.** Ama bu bir "standart fizik bilmiyor" değildir ve öyle sunulmamalıdır: helyum 40 anlamlı basamağa çözülmüştür; eksik olan analitik izlenebilirliktir, fiziksel anlayış değil. Çok-cisim probleminin çözülemezliği kuantum mekaniğine özgü de değildir (klasik üç-cisim problemi de çözülemez). Çerçeve türetilmiştir: kabuk yapısı, seçim kuralları, ince/hiperince yapı, Lamb kayması, izotop kaymaları, Zeeman/Stark.

**İki elektrondan sonra analitik çözüm yoktur.** Dolayısıyla:
- **Aşmamız gereken bar "her element" DEĞİL** — o bar standart fizikte de aşılmamıştır. Bunu iddia etmek de zorunda değiliz.
- **Aşmamız gereken bar HİDROJEN.** Ve orada hassasiyet acımasız ($10^{-12}$). Hedef dar ama sert.

---

## 3. Standart Modelin Yanıtı ve Evrenakı'nın İtirazı
*   **Standart Fiziğin Yanıtı:** Elektron, çekirdeğin Coulomb potansiyelinde bağlı bir dalga fonksiyonudur; normalize edilebilirlik koşulu enerji özdeğerlerini kesikli kılar. Üst seviyeden alt seviyeye geçişte enerji farkı ($E=h\nu$) ışıma olarak salınır.
*   **Evrenakı'nın İtirazı:** Nokta parçacık ("foton") yoktur; elektron fiziksel bir girdaptır, olasılık dalgası değildir. "Sıçrama" bir teleportasyon olamaz; enerji fırlatımı mekanik bir deşarjdır ve Zerre katarının ritmi bu boşalmanın fiziksel ritmidir.
*   **İtirazın dürüst sınırı:** İtiraz, kesikliliğin *matematiğine* değil **ontolojisine**dir. Aynı kesikli sonucu vermek zorundayız; farkımız mekanizmada olacak.

---

## 4. ÇÖZÜM ÖNERİSİ — SPEKTRUM ÇİZGİLERİ **VURU (BEAT) NOTASIDIR**

> 🔴 **BU BÖLÜM BAĞIMSIZ DENETİMDEN GEÇEMEDİ (10 Ağu 2026).** Aşağıdaki türetim, göründüğü gibi bir türetim **değildir** — ayrıntılı gerekçe ve sayılar için **§9'a bakmadan bu bölüme dayanılmamalıdır.** Bölüm, ne yapılmaması gerektiğinin kaydı olarak korunmuştur.

### 4.1 Mekanizma
E1 kararından sonra teorinin elinde şu yasa var (M-3, duvar hızı yasası): her vakum-cepli girdap zarfı duvarını **boyutundan bağımsız olarak** $\sqrt2\,c$ ile döndürür. Dolayısıyla açısal hız yalnız yarıçaptan okunur:

$$\Omega(r) = \frac{\sqrt2\,c}{r}$$

Bir elektron girdabı $r_2$'den $r_1$'e düştüğünde ortada **iki mekanik ritim** vardır. Yayılan katarın ritmi bu iki ritmin **farkıdır**:

$$\boxed{\;\nu = \frac{\sqrt2\,c}{2\pi}\left(\frac{1}{r_1}-\frac{1}{r_2}\right)\;}$$

$r_n \propto n^2$ olduğunda bu **doğrudan Rydberg yapısını** verir:

$$\nu \;\propto\; \frac{1}{n_1^2}-\frac{1}{n_2^2}$$

Yön de doğru: küçük $r$'de $\Omega$ büyük olduğundan düşüşte $\Omega_1>\Omega_2$ ve vuru pozitiftir — emisyon. ✔

### 4.2 Kavramsal kazanç (formülden büyük)
"Frekans = kaynağın ateşleme ritmi" tanımının altında rahatsız edici bir soru vardı: **mekanik bir ritim neden iki terimin farkı olsun?** Standart fizikte cevap kolaydır ("enerji farkı"), ama teoride ritim fiziksel bir dönüştür ve farkın mekanik karşılığı yoktu.

**Vuru okuması bunu çözer:** iki dönüş ritmi üst üste bindiğinde ortaya çıkan şey zaten bir fark frekansıdır. **Spektrum çizgisi bir vuru notasıdır.** Rydberg formülünün "iki terimin farkı" biçimi, teoride bir tesadüf değil, mekanizmanın zorunlu imzası olur.

### 4.3 Ölçek denetimi — dürüst kayıt
$r=a_0=5{,}29\times10^{-11}$ m konduğunda:

$$\nu(a_0)=\frac{\sqrt2\,c}{2\pi a_0}=1{,}276\times10^{18}\ \text{Hz}, \qquad \nu_{Rydberg}=3{,}290\times10^{15}\ \text{Hz}$$

**Oran 387,9.** Ve bu sayı rastgele değil, cebirsel olarak tam:

$$\frac{\nu(a_0)}{\nu_{Rydberg}} = \frac{2\sqrt2}{\alpha} = 387{,}6$$

*(Türetim: $a_0=\hbar/m_ec\alpha$ ve $\nu_{Ryd}=\alpha^2m_ec^2/2h$ konduğunda $\alpha$'lar sadeleşir.)*

**Yapı doğru, ölçek $2\sqrt2/\alpha$ kadar yüksek.** İki okuma mümkün:
- **(a) İlgili yarıçap $a_0$ değildir** — 388 katı, yani $\approx2{,}05\times10^{-8}$ m ($\approx20{,}5$ nm). Elektronun *süpürdüğü disk* yarıçapının kavitasyon yarıçapından çok büyük olması teoride zaten kabul (2.1) — bu okuma o çizgide.
- **(b) Ateşleme ritmi dönüş ritminin bir kesridir** — kavitasyon kapakçığı her turda değil, $\alpha/2\sqrt2 = 1/388$ oranında açılıyordur (görev çevrimi).

> ⚠️ **YASAK: $\alpha$ elle konulmayacak.** $2\sqrt2/\alpha$ çarpanı, uyum sağlamak için yazılırsa Anayasa Madde 21'in yasakladığı **yama parametre** olur. ($\tau$ ve $R_{disk}$ kalemlerinde verilen kararla aynı ilke.) $\alpha$ bu zincire girecekse **9.6'nın kendi mekanik türetiminden** gelmek zorundadır — o bölüm yazılmıştır, bağlanacak yer orasıdır.

### 4.4 Aday (a) ile Aday (b) arasındaki ayırt edici sınav
İki okuma aynı çizgileri verir ama **farklı şey söyler**: (a) elektronun disk yarıçapını 20,5 nm'ye çıkarır — atomdan ~400 kat büyük, ki bu komşu atomlarla örtüşme demektir ve katı hâl/kırılma mekaniğinde iz bırakmak zorundadır. (b) ise geometriyi bozmaz, yalnız bir görev çevrimi ekler. **Bu ayrım, kalemin sınanabilir tarafıdır ve önce buradan gidilmelidir.**

---

## 5. GERİYE KALAN GERÇEK İŞ: NEDEN $r_n \propto n^2$?

§4'ün türetimi bunu **varsayıyor**. Standart fizik bunu $L=n\hbar$'dan alır; teori kendi mekaniğinden almak zorundadır. Bu, dosyanın en ağır kalemidir.

### Aday 4 ⭐ — Kapalı-iz (wake) koşulu
Teori girişimi zaten Zerre'lerin birbirinin **wake tünelüne** kapılmasıyla açıklıyor (2.7–2.8). Aynı mekanizmayı bağlı elektrona uygula:

> Yörüngede dolanan elektron Evrenakı'da bir iz bırakır ve **bir turdan sonra kendi izine fazı bozulmadan girmek zorundadır.** Bu kapanma koşulu, yörünge çevresinin iz-uzunluğunun tam katı olmasını gerektirir → kararlı yarıçaplar **kesikli** çıkar.

Bu, duran-dalga koşulunun mekanik karşılığıdır — ama **ödünç değil**: teorinin kendi wake mekaniğinden geliyor ve 2.7–2.8 ile kenetleniyor. Başarılırsa $1/n^2$ yapısı §4'ün vuru formülüne oturur ve zincir tamamlanır.

**Türetilmesi gereken:** iz-uzunluğunun ($\lambda_{iz}$) elektronun hızı ve ortamın yerel özellikleriyle ilişkisi. $\lambda_{iz} \propto 1/v$ çıkarsa Bohr koşulu mekanik olarak yeniden kurulmuş olur.

---

## 6. Aday 1–3 (ilk sürümden korunan, düzeltilmiş hâlleriyle)

### Aday 1: Girdap çaplarının ve rampa kilitlenmelerinin rezonansı
Çekirdek ile elektron girdabı arasında hidrodinamik kararlılık zonları. **§4 bu adayın mekanizmasını verdi** (duvar hızı yasası + vuru); Aday 1 artık ayrı bir aday değil, §4'ün niteliksel öncüsüdür.

### Aday 2: Kelvin-Helmholtz kararsızlığı ve deşarj eşiği
İki akışkan tabakası arasındaki hız farkı eşiği aştığında girdap kopar. Yalnız kesikli hız/enerji eşiklerinde Zerre kopması hidrodinamik olarak mümkündür. **Durum:** ayakta; §4'ün *kapakçık ritmini* (görev çevrimi, §4.3b) verebilecek aday budur.

### Aday 3: Pauli dışlamasının akışkan karşılığı — **düzeltildi**
İlk sürüm "eş yönlü girdapların itişmesi" diyordu. Akışkanlar mekaniğinde daha güçlü ve daha doğru olgu şudur:

> **Eş-dolanımlı iki girdap çekirdeği çakışırsa itişmez — birleşir** (vortex merger).

Dolayısıyla dışlama bir *itme kuvveti* olarak değil, **"iki eş girdap aynı çekirdeği paylaşamaz; paylaşırsa iki olmaktan çıkar"** biçiminde kurulmalıdır. Bu, Pauli'nin ifadesine hem daha yakın hem de literatürde yerleşiktir (Kelvin–Helmholtz girdap birleşmesi).

---

## 9. 🔴 ELENMİŞ YOLLAR — BAĞIMSIZ DENETİM SONUÇLARI *(10 Ağustos 2026, üç hakem)*

> Bu bölüm bilinçli olarak tutulur: **hangi kapıların kapalı olduğu ve NEDEN kapalı olduğu**, hangi kapıların açık olduğu kadar değerlidir. Aşağıdaki hiçbir yola tekrar girilmemelidir.

### 9.1 ⛔ Örgünün taşıyıcısı **ÇEKİRDEK OLAMAZ** — en kesin kapı
Na-23 için $R=1{,}2A^{1/3}=3{,}413$ fm, $M=3{,}819\times10^{-26}$ kg:
$$I=\tfrac25 MR^2 = 1{,}779\times10^{-55}\ \text{kg·m}^2$$
$L=\hbar$ olduğunda $\omega = 5{,}927\times10^{20}$ rad/s → $\nu = 9{,}43\times10^{19}$ Hz $= 390$ **keV**.
Optik frekansa ($5{,}09\times10^{14}$ Hz) inmek için gereken açısal momentum:
$$L = 5{,}69\times10^{-40}\ \text{J·s} = 5{,}4\times10^{-6}\,\hbar$$
**Eylem kuantumunun 200.000 katı altında — fiziksel değil.** Çekirdeğin dönüşü de yalpalaması da optik frekans üretemez. "Proton örgüyü yazar, nötron yük olarak biner" önerisi bu duvara çarpar; öneri izotop verisiyle uyumlu olsa bile **bu hesapla elenir.**

**Yön işareti (yapıcı):** örgünün taşıyıcısı çekirdek değil, **elektron kabuğunun ritmik Evrenakı basınç zarfı** olmalıdır — ki bu 2.6'nın mevcut ifadesiyle zaten tutarlıdır.

### 9.2 ⛔ §4'ün vuru formülü bir türetim değil, **geri-mühendisliktir**
1. **$\sqrt2$ tamamen sadeleşiyor:** $\dfrac{\alpha}{2\sqrt2}\cdot\dfrac{\sqrt2 c}{2\pi} = \dfrac{\alpha c}{4\pi}$. Duvar hızı $kc$ ve çevrim $\alpha/2k$ alındığında sonuç **her $k$ için aynıdır** ($k=1;\sqrt2;2;7{,}3$ denendi). Yani bu hesap $\sqrt2c$ duvar hızı için **sıfır kanıt** sağlar; $\sqrt2$ kozmetiktir.
2. **Formül birebir Rydberg'dir:** $a_0=\hbar/\alpha m_ec$ konduğunda $\alpha c/4\pi a_0 = \alpha^2m_ec^2/2h = R_\infty c$ — **özdeşlik**. Yeni bir şey türetilmiyor, Rydberg yeniden parametrelendiriliyor.
3. **$r_n=n^2a_0$ Bohr'dan ithal edildi.** $1/n^2$ giden herhangi bir nicelik farklanıp serbest bir katsayıyla ölçeklenirse Rydberg otomatik çıkar.
4. **Ölçek çelişkisi:** varsayılan $\Omega\propto1/n^2$ (1275,1 / 318,8 / 141,7 PHz), gerçek yörünge frekansının $\propto1/n^3$ ölçeğiyle (6,58 / 0,82 / 0,244 PHz) uyuşmuyor.
5. **Karşılaştırma hatası:** 656,279 nm **hava** dalga boyudur; vakum karşılığı **656,461 nm**. Ölçülen çizgiye karşı sapma $5{,}32\times10^{-4}$ ($m_e/m_p$'nin 0,976 katı); kalan $\sim1{,}3\times10^{-5}$ ince yapı + Lamb kaymasıdır ve formülde **hiç yok**.

**Hüküm:** bu hesap kitapta "$\sqrt2c$'nin kanıtı" olarak **sunulamaz**; en fazla "model Rydberg ile tutarlıdır, ama çekirdek geri tepmesini ve ince yapıyı içermez" düzeyinde bir tutarlılık kontrolüdür.

### 9.3 ⛔ "TARAK FİLTRESİ" metaforu **yanlış öngörü** veriyor
Tarak, fizikte **eşit aralıklı** diş demektir. Balmer frekanslarının ardışık farkları ($\times10^{14}$ Hz): **1,599 · 0,740 · 0,402 · 0,242 · 0,157** — eşit değil, $8{,}225\times10^{14}$ Hz'lik seri limitine **sıkışıyor**.

Mekanik bir dönüş+yalpalama deseni doğal olarak **harmonik** üstses verir (tam katlar, eşit aralık). Atom tayfı harmonik değildir; **Rydberg–Ritz birleşme ilkesine** uyar ($\nu_{13}=\nu_{12}+\nu_{23}$ — *terimler* toplanır, frekanslar katlanmaz).

> ✅ **DÜZELTME (10 Ağu 2026) — bu madde artık "kapalı kapı" değil.** İtirazın ilk hâli fazla geniş kurulmuştu. İtiraz gerçektir ama **dar bir hedefi** vardır; teori onu yalnız aşmıyor, kendi lehine çeviriyor. Aşağıya bakılmadan bu maddeye dayanılmamalıdır.

**İtirazın gerçek hedefi:** harmonik teoremi **zamansaldır** — $f(t+T)=f(t)$ ise spektrum $\{n/T\}$ içinde kalmak zorundadır. Dolayısıyla itiraz, *"ışıma kaynağın kendi dönüş frekansında ve harmoniklerinde olur"* diyen modelleri vurur. **Durağan bir uzamsal düzen içindeki geçişleri vurmaz** — durağan düzen zamanda tekrar etmez, frekansı yoktur.

**Teorinin cevabı — güncel tam tablo** *(Atom Geometrisi katkısıyla güncellendi, 10 Ağu 2026):*

| Gözlem | Nereden | Durum |
|---|---|---|
| Kabuk sayıları **2, 8, 18, 32** | Kare katman geometrisi: $k$'ıncı katman $(2k)^2$ konumlu, $2k^2$ protonlu | ✅ *Atom Geometrisi* |
| $2n^2$'nin içindeki **"2"** | Kare ızgaranın yarısı proton — **spin eşleşmesi gerekmez** | ✅ *Atom Geometrisi* |
| **Dışlama / eşit aralık** | Bir kabuk = **tek yörünge**; karşılıklı yük itmesi mesafeyi eşit tutar. Düzlem seçilmez, katman dayatır | ✅ *Atom Geometrisi* |
| **Yarıçap oranları ($1:4:9:16$)** | Çapı **elektron sayısı** belirler; $N=2k^2 \Rightarrow r\propto k^2$ | ✅ *Atom Geometrisi* |
| $1/n^2$ **biçimi** (enerji) | Düzenin şekli $1/r$: $P(r)=P_0-\alpha M/r$ | ✅ Evrenakı |
| **Rydberg–Ritz toplanabilirliği** | Geçiş = iki hâlin **vurusu**: $(\Omega_1-\Omega_2)+(\Omega_2-\Omega_3)=\Omega_1-\Omega_3$ | ✅ Evrenakı |
| **Harmoniğin olmaması** | Işıma bir dönüş frekansı değil, durağan düzen içinde **geçiş** | ✅ Evrenakı |
| **Mutlak ölçek** ($a_0$, dolayısıyla $\hbar$) | **Ölçülen girdi** — türetilmesi beklenmez | ✅ **parite kararı** (§10.6.4), Ek C satır 1-b |

> ### 🔑 İKİ ÖNEMLİ GÜNCELLEME
> **1. "Basamakların varlığı" kalemi kapandı — ve aradığımız kural hiç gerekmedi.** §10.1–10.2'de "kapanma/uyum kuralı" arıyorduk ($\lambda_{iz}\propto1/v$, kapalı-iz koşulu vb.). *Atom Geometrisi*'nin yolu bu kuralı **atlıyor**: sayı geometriden ($2k^2$), çap sayıdan ($r\propto N$) geliyor. Açısal momentum kuantumlaması gerekmiyor. §10.2–10.3'ün programı bu nedenle **artık zorunlu değil** — yalnız alternatif bir yol olarak kalır.
>
> **2. Mutlak ölçek boşluğu bağımsız olarak teyit edildi.** *Atom Geometrisi* de mutlak ölçeği vermiyor, ve **vermemesi yapısaldır**: hem merkez çekimi hem karşılıklı itme $1/r^2$ gittiğinden salt yük mekaniği ölçekten bağımsızdır — oran verir, mutlak değer vermez. Bu, §10.6.2'nin sonucuyla (teoride eylem boyutunda bağımsız nicelik yok, $\hbar$ üretilemez) **iki ayrı yoldan aynı duvara çarpmak** demektir. Boşluk gerçektir; bir eksiklik değil, teorinin sınırının konumudur.

#### 9.3.1 İtiraz bir öngörüye dönüşüyor: **harmonik ⟺ iki merkez**
Harmoniğin nerede *görüldüğüne* bakınca kural tek: **gerçekten dönen bir gövde varsa** tayf eşit aralıklı çıkıyor.

| Yapı | Dönme ekseni | Tayf | Ölçüm (4 çizgide aralık oynaması) |
|---|---|---|---|
| Tek atom (küresel $1/r$ düzeni) | **yok** | terim farkı | Balmer: **6,6 kat** |
| Molekül (iki merkez) | **var** | **harmonik** | CO: **%0,02** (115,27 GHz) |
| Landau / Zeeman | siklotron / Larmor | **harmonik** | 28,0 GHz/T · 13,996 GHz/T |
| Deforme çekirdek | eksenel simetri kırık | $J(J+1)$ bandı | MeV |

Dört mertebe fark. **Dönecek bir eksen ancak en az iki merkez varken doğar** — tek atomda küresel düzen vardır, dönecek gövde yoktur.

> **Teori harmoniği yasaklamaz; nerede beklendiğini söyler.** İki rejimi önceden ayırt edebilen bir öngörü, ikisini aynı kefeye koyan modelden güçlüdür.

#### 9.3.2 Bunu doğrulayan keskin gözlem: hidrojende $l$-yozlaşması
Kaba yapıda $n=2$'nin **2s ve 2p durumları aynı enerjidedir**; enerji yalnız $n$'ye bağlıdır, $l$'ye hiç bağlı değildir.

Atomda rijit bir dönme enerjisi olsaydı $E_{dönme}\propto l(l+1)$ gereği 2p, 2s'nin belirgin biçimde üstünde olurdu. Değil. **"Atomun içinde rijit dönen bir gövde yok" ölçülmüş durumdadır** — ve bu tam olarak $1/r$ düzeninin simetri imzasıdır. Molekülde bu yozlaşma yoktur, çünkü orada gerçekten dönen bir gövde vardır.

#### 9.3.3 Terim düzeltmesi
"Tarak filtresi" **kullanılmayacak** — tarak fizikte eşit aralıklı diş demektir, atom tayfı eşit aralıklı değildir. Yerine **"seçici rezonans zarfı"** veya **"uyum kilidi"**; Rydberg–Ritz'e açık atıf yapılacak.

#### 9.3.4 Kapsam beyanı ✅ *(2.1'e yazıldı — "harmonik ⟺ iki merkez" tablosuyla birlikte; bileşik tayfları 7.4 md. 6-d'ye havale edildi)*
> Bu bölüm **tek atomun** düzenini konu alır. Bileşikler (moleküller) iki ritmin birleşmesinden doğar; birleşmiş yapının davranışı ayrı bir katmandır ve bu kitapta hesaplanmaz. Ayrım keyfî değildir ve sınanabilir bir sonucu vardır: dönecek bir eksen ancak iki merkez varken doğar, dolayısıyla **harmonik (eşit aralıklı) tayf yalnız bileşik yapılarda beklenir** — tek atomun elektronik tayfında beklenmez, ve gözlenmez.

*(Madde 19 karşılanır: mekanizma adlandırılmıştır — "iki ritmin birleşmesi" — yalnız hesabı üst katmana bırakılmıştır. 7.4'e kalem: **bileşik yapıların molekül dönme/titreşim tayflarının teori-içi hesabı.**)*

### 9.4 ⛔ Kirchhoff kazancı **aşırı iddiaydı**
Önce ayrım: **(K1)** Kirchhoff ışıma yasası ($\varepsilon_\nu=\alpha_\nu$, termodinamik dengede) bir teoremdir ve çizgi konumu hakkında hiçbir şey söylemez. **(K2)** Kirchhoff–Bunsen kuralı (soğurma ve yayma çizgileri aynı dalga boyunda) ampirik bir gözlemdir. İddia (K2)'yi açıklayıp (K1)'i kazandığını sanıyordu — kazanmıyor.

Kural **mutlak değil**:
- **Soğurma listesi yayma listesinden dar.** Hα'nın alt seviyesi $n=2$ (10,199 eV); 300 K'de $n_2/n_1=1{,}9\times10^{-171}$ → soğuk hidrojen Hα **soğurmaz**, ama H II bölgeleri onu en parlak optik çizgi olarak yayar. (Na 818,33 nm: $n(3p)/n(3s)=1{,}3\times10^{-35}$.) "Aynı örgü ters yön" bu $10^{35}$–$10^{171}$ asimetrisini üretemez.
- **Çizginin işareti atomun değil ORTAMIN özelliği:** Güneş fotosferinde soğurmadaki Na D çizgileri kromosferde aynı atomla yaymaya döner. Karar veren $dT/d\tau$ (Eddington–Barbier).
- **Örtüşmenin bozulduğu haller:** Stokes kayması (floresein 490→514 nm, 953 cm⁻¹), Raman (532 nm uyarma → Stokes 545,3 / anti-Stokes 519,3 nm; madde ikisinde de saydam), Auger ($\omega_K$(C)$=0{,}0026$ — karbon K-soğurmasının %99,7'si hiç ışıma vermez), ön-ayrışma, ters çevrilmiş popülasyon (HeNe 632,8 nm'de $T_{uyarılma}=-2{,}4\times10^5$ K), kendini soğurma/self-reversal, P Cygni.

**Ayakta kalan çekirdek:** *doğrusal, karşılıklı, kayıpsız bir rezonatör soğurmada ve yaymada aynı rezonans frekansını gösterir.* Bu meşrudur — ama içeriği **Lorentz osilatör modelidir** (1896) ve yalnız çizgi **konumları** için sezgi verir. Şiddetler, çizginin işareti ve kendiliğinden yayma hızı bundan çıkmaz.

### 9.5 ⛔ İzotop argümanımın **gerekçesi geçersizdi** (sonucu doğru olsa bile)
"Döteronun kuadrupolü var, protonun yok; girseydi fark büyük olurdu" akıl yürütmesi bir **non-sequitur**'dür: H/D karşılaştırması kuadrupol kanalını sınırlayacak duyarlıkta değildir. Gerçek gerekçe **ölçektir**: $Q_d/a_0^2 \approx 1{,}0\times10^{-10}$; kuadrupol etkisi izotop kaymasından $\sim4\times10^{-7}$ kat küçüktür. Ayrıca kuadrupol operatörü **izsizdir (traceless)** — çizgi ağırlık merkezini birinci mertebede hiç kaydırmaz, yalnız hiperince alt seviyeleri ayırır.
Ek düzeltme: izotop kayması "tam olarak indirgenmiş kütle" değildir — 1S–2S kaymasında **18,95 MHz** artık kalır ($2{,}8\times10^{-5}$); bunun bir kısmı çekirdek hacmi (alan kayması, $-5{,}23$ MHz), kalanı geri tepme QED'idir.

### 9.5b ⚠️ §9.3'ün ilk hâline dayanan kayıtlar geçersizdir
§9.3 düzeltildiği için, ona dayanarak "mekanik model imkânsız" diye kurulmuş her ara sonuç düşer. Geçerli olan §9.3.1–9.3.4'tür.

### 9.6 Yeni açık borç listesi (7.4'e yazılacak)
Teori bunları **henüz türetmemiştir** ve bir spektrum bölümü bunlar olmadan tamamlanamaz:
| # | Borç | Sayısal hedef (Na D2) |
|---|---|---|
| a | $A_{21}/B_{21} = 8\pi h\nu^3/c^3$ | $8\pi\nu^2/c^3=2{,}415\times10^{5}$ kip m⁻³Hz⁻¹; $A_{21}=6{,}16\times10^7$ s⁻¹ ($\tau=16{,}23$ ns) → $B_{21}=7{,}56\times10^{20}$ |
| b | $g_1B_{12}=g_2B_{21}$ | $g_2/g_1=2$; ölçüm $f(D_2)/f(D_1)=2{,}0025$. Örgü modelinde "$g$"nin karşılığı tanımlanmalı |
| c | $\nu^3$ ölçeklemesi | $(\nu_{opt}/\nu_{21cm})^3=4{,}60\times10^{16}$ — ritim-uyumu tüm ritimlere aynı davrandığı için bu asimetriyi üretemez |
| d | Kennard–Stepanov / McCumber | yayma/soğurma oranı $\propto\nu^3e^{-h\nu/kT}$; teori "aynı çizgiler" yerine bu **oranı** vermeli |
| e | Kendiliğinden yayma kaynak terimi | tam karşılıklı bir filtre yalnız eşevreli esnek saçılma verir; rastgele fazlı $e^{-At}$ bozunumu için ayrı dalgalanma kaynağı gerekir |
| f | **Fırsat:** $A\propto n$ sınavı | $A/B\propto1/c^3$ olduğundan değişken-$c$ teorisi ortam indisiyle ışıma ömrünün kısalmasını (Eu³⁺ ölçümü) öngörmek zorundadır — 9.1 (Fizeau) ile doğal köprü |

### 9.7 Yapısal ikilem *(kayda geçmeli)*
Model **tam karşılıklı/zamanda tersinir** ise yalnız eşevreli esnek saçılma verir — kendiliğinden yayma, Stokes kayması, Raman ve kazanç imkânsız olur. **Karşılıklı değilse** "ters yönde aynı çizgiler" garantisi düşer. **İkisi bir arada olmaz;** teori bu ikilemde bir taraf seçip bedelini ödemek zorundadır.

---

## 10. KESİKLEŞME KURALI — **TEK KALAN EKSİK**

### 10.1 Biçim ile varlığın ayrımı
İki ayrı soru vardır ve karıştırılmamalıdır:
- **Biçim:** basamaklar $n=1,2,3\dots$ diye var kabul edildiğinde enerjileri ne olur?
- **Varlık:** basamaklar neden var, neden süreklilik değil?

**Klasik mekanikte $1/r$ kuyusu süreklilik verir** — yasak yarıçap yoktur (uydu her yükseklikte dolaşır). Yani $1/r$ tek başına merdiven yapmaz.

Ama merdiven bir kez varsayıldığında **biçimi $1/r$ dayatır.** Dairesel yörünge için $mv^2/r=k/r^2 \Rightarrow v=\sqrt{k/mr} \Rightarrow L=mvr=\sqrt{kmr}$. Herhangi bir eylem kuantumlama kuralı ($L=n\hbar$) konduğunda:

$$\sqrt{kmr}=n\hbar \;\Longrightarrow\; r\propto n^2 \;\Longrightarrow\; E=-\frac{k}{2r}\propto-\frac{1}{n^2}$$

**Karşılaştırma — aynı kural, parabolik kuyu** ($V=\tfrac12m\omega^2r^2$): $L=m\omega r^2=n\hbar \Rightarrow r\propto\sqrt n \Rightarrow E=n\hbar\omega$ — **eşit aralıklı.**

> **Merdivenin biçimini kuyunun şekli, varlığını kapanma kuralı belirler.** Teorinin kuyusu $1/r$'dir ($P(r)=P_0-\alpha M/r$, kütle-itim), dolayısıyla **$1/n^2$ bedavadır.** Eksik olan yalnız kapanma kuralıdır. Bu ayrım, §9.3'ün tablosundaki "bedava üç, eksik bir" dağılımının gerekçesidir.

### 10.2 Eksik kural tek bir soruya indi
Kapalı-iz koşulu (§5 Aday 4): çevreye tam sayıda iz sığmalı.
$$2\pi r = n\,\lambda_{iz}$$
$\lambda_{iz}\propto 1/v$ ise $mvr\propto n$ çıkar — **bu tam olarak Bohr kuralıdır**, ve arkasından $1/n^2$ gelir.

**Bütün problem şudur: iz uzunluğu neden hıza TERS orantılı olsun?**
Sıradan bir iz $\lambda=v/f$ verir, yani $\lambda\propto v$ — **ters işaret.** $1/v$ elde etmek için iç frekansın $v^2$ ile büyümesi gerekir.

### 10.3 ⭐ En umut verici iz: faz dalgası ve **ikinci kanal**
de Broglie'nin **özgün** türetimi tam bu yapıdadır: iç salınımın *faz dalgası*, hızı $c^2/v$ olan bir dalgadır ve $\lambda=(c^2/v)/f$ hesabı $\lambda=h/mv$ verir. Faz hızı $c^2/v$ **her zaman $c$'den büyüktür.**

> ⚠️ **DÜZELTME (10 Ağu 2026):** Bu maddenin ilk hâli $c^2/v$'yi Madde 8'in kohezyon kanalına ($v_m\gg c$) bağlıyordu. **Gereksiz ve zararlıydı.** $c^2/v$ bir **sinyal hızı değil, desen hızıdır** — hareket eden bir salınıcının sabit-faz yüzeylerinin, laboratuvar eşzamanlılık düzlemiyle kesişme noktasının süpürme hızı. Hiçbir şey o hızda *taşınmaz*. Dolayısıyla üst-ışık bir kanal **çağırmaya gerek yok**; saf geometri yetiyor. Bu teori için hem daha ucuz hem daha güvenlidir: Madde 8'i bu kaleme borçlandırmıyoruz.

**Zincirin yapısı:**
$$\lambda = \frac{v_{faz}}{f_0} = \frac{c^2/v}{f_0}$$
$1/v$'nin **tamamı** $v_{faz}$'dan gelir (geometri). Geriye tek gereksinim kalır: **iç ritim $f_0$** — ve bunun $h$'sız bir kaynaktan gelmesi zorunludur (§10.3 yasağı). Teorinin böyle bir kaynağı vardır: $\Omega=\sqrt2c/r$ ile, yarıçap $m/\rho_n$'den. Sayısal sınav §10.4'te.

> ⚠️ **YASAK:** $h$ bu türetimin **girdisi olamaz.** $\lambda=h/mv$ sonucuna varmak için $h$ konursa döngüsellik doğar (aynı hata $\tau$ ve $R_{disk}$ kalemlerinde reddedildi). Kapanma kuralı ortamın kendi mekaniğinden çıkmalıdır — Madde 21.

### 10.4 SAYISAL SINAV — *(bağımsız denetimle düzeltildi 10 Ağu 2026; bkz. §10.5)*

> 🔴 **Bu bölümün ilk hâlinde iki hata vardı ve düzeltilmiştir.** (1) $\sqrt2c$ için $\sqrt2\times3{,}000\times10^8$ kullanılmıştı (yani $c=3\times10^8$); doğrusu $4{,}2397\times10^8$ m/s. (2) Daha önemlisi: "5876 / 5878 / 5880" üç bağımsız teyit gibi sunulmuştu — **cebirsel olarak aynı sayıdır** ve doğru değeri **5870**'tir. Ayrıntı ve totoloji kanıtı §10.5'te. Aşağıdaki sayılar düzeltilmiş hâlleridir.

Teorinin $h$'sız iç ritmi: elektronun kavitasyon çekirdeği yarıçapı, kütle ve öz yoğunluktan (Postülat 4 yöntemi, Zerre için kullanılanın aynısı):

$$V_e = \frac{m_e}{\rho_n} = \frac{9{,}109\times10^{-31}}{2{,}7\times10^{17}} = 3{,}374\times10^{-48}\ \text{m}^3 \;\Longrightarrow\; r_e^{çek} = 9{,}30\times10^{-17}\ \text{m}$$

$$\Omega = \frac{\sqrt2\,c}{r_e^{çek}} = 4{,}563\times10^{24}\ \text{rad/s} \;\Longrightarrow\; f_0 = \frac{\Omega}{2\pi} = 7{,}263\times10^{23}\ \text{Hz}$$

$n=1$ elektronu için $v=\alpha c = 2{,}188\times10^6$ m/s, dolayısıyla $v_{faz}=c^2/v = 4{,}108\times10^{10}$ m/s:

$$\lambda = \frac{4{,}108\times10^{10}}{7{,}263\times10^{23}} = 5{,}656\times10^{-14}\ \text{m} \;\Longrightarrow\; r_1 = \frac{\lambda}{2\pi} = 9{,}00\times10^{-15}\ \text{m}$$

| | Değer |
|---|---|
| Teorinin verdiği $r_1$ | $9{,}00\times10^{-15}$ m |
| Gerçek $a_0$ | $5{,}292\times10^{-11}$ m |
| **Sapma** | **5880 kat küçük** |

**Sebebi tek ve net:** teorinin $h$'sız iç frekansı ($7{,}263\times10^{23}$ Hz), elektronun Compton frekansından ($1{,}236\times10^{20}$ Hz) **5878 kat yüksektir.** Zincirin geri kalanı — $1/v$'nin geometriden gelmesi, $h$'nin girmemesi, kapanma koşulunun Bohr kuralını vermesi — çalışıyor.

#### 10.4.1 Kırılan şey bir **oran**
$f_0$'ın Compton frekansına eşit olması için gereken yarıçap:
$$r = \frac{\sqrt2\,c}{2\pi\nu_C} = 5{,}465\times10^{-13}\ \text{m} \;\Longrightarrow\; \frac{r}{r_e^{çek}} = 5876$$

Yani dönen şey kavitasyon çekirdeği değil, **süpürülen disk** ise ve disk/çekirdek oranı $\approx5900$ ise zincir kapanır. Teori elektron için bu ayrımı zaten yapıyor (2.1: *"kavitasyonu çok küçük ama süpürdüğü Disk yarıçapı EN GENİŞ"*) — eksik olan **oranın türetimi.**

#### 10.4.2 🔗 K-8 ile çapraz bağ — iki kalem tek soruya bağlandı
`Zerre_Spini_ve_Optik_Acisal_Momentum.md` (K-8) da bir disk/çekirdek oranı istiyordu: **$3{,}7\times10^6$** (Zerre için, optik açısal momentum açığını kapatmak üzere).

| Kalem | Parçacık | Gereken disk/çekirdek oranı |
|---|---|---|
| K-8 (açısal momentum) | Zerre | $3{,}7\times10^{6}$ |
| §10.4 (Bohr yarıçapı) | elektron | $5{,}9\times10^{3}$ |

İki bağımsız gereksinim, iki farklı parçacık, iki farklı oran. **Bu bir çelişki değil ama bir kilit:** teori "süpürülen disk / kavitasyon çekirdeği" oranını kendi mekaniğinden türetebilirse **iki kalem birden ya kapanır ya çöker.** Oran serbest bırakılırsa ikisi de yama parametreye döner (Madde 21).

> **Sonuç: $\lambda_{iz}\propto1/v$ problemi, "iz uzunluğu neden $1/v$" sorusundan çıkıp bir *disk/çekirdek oranı türetimi* sorusuna indi.** Bu, teorinin kendi diline çok daha yakın ve iki ayrı kalemi aynı hedefe bağlayan bir sorudur.

⚠️ **Yasak (yine):** 5870 ve $3{,}7\times10^6$ değerleri **atanmayacak.** Bunlar açığı kapatmak için *gereken* sayılardır; bağımsız gerekçeden gelmedikçe yazılırlarsa yama parametre olurlar.

---

## 10.5 🔴 BAĞIMSIZ DENETİM — §10.4'ÜN DÜZELTİLMESİ ve ELENEN MEKANİZMALAR *(10 Ağustos 2026, iki hakem)*

### 10.5.1 "Üç doğrulama" bir totolojiymiş
§10.4'te 5876 / 5878 / 5880 sayıları üç ayrı teyit gibi sunulmuştu. **Cebirsel olarak aynı sayıdır:**

$$\frac{a_0/r_1}{f_0/\nu_C} = \frac{2\pi\alpha\,a_0\,m_e c}{h} = \frac{a_0}{\hbar/(m_ec\alpha)} = \frac{a_0}{a_0} = 1$$

çünkü $a_0 = \hbar/(m_ec\alpha)$ **tanımdır.** Denetçi sayısal olarak da doğruladı: $f_0$ yerine 1 Hz, $10^{10}$, $7{,}25\times10^{23}$ ve $5\times10^{30}$ Hz konduğunda oran **her seferinde 1** çıkıyor.

> **Sonuç:** bu eşitlik $\rho_n$, $r_e$ ve $\sqrt2$ hakkında **sıfır bilgi** taşır. Aynı şekilde $r^*/r_e = f_0/\nu_C$ de özdeşliktir ($\sqrt2$ ve $c$ sadeleşir). Geriye **tek bir olgu** kalır:
> **Teorinin $\hbar$'sız elektron yarıçapı, $\sqrt2\times$ indirgenmiş Compton boyundan 5870 kat küçüktür.** Bir cümle — "üç yerden doğrulanan kilit" değil.

### 10.5.2 Aritmetik düzeltmeler
İlk hesapta $\sqrt2c$ için $\sqrt2\times3{,}000\times10^8$ kullanılmıştı (yani $c=3\times10^8$); %0,069 hata zincire yayılmıştı.

| Nicelik | İlk hâli | **Doğru** |
|---|---|---|
| $\sqrt2\,c$ | $4{,}2426\times10^8$ | $\mathbf{4{,}2397\times10^8}$ m/s |
| $r_e^{çek}$ | $9{,}30\times10^{-17}$ | $9{,}304\times10^{-17}$ m ✔ |
| $f_0$ | $7{,}263\times10^{23}$ | $\mathbf{7{,}252\times10^{23}}$ Hz |
| $\nu_C$ | — | $1{,}236\times10^{20}$ Hz |
| $\lambda$ | $5{,}656\times10^{-14}$ | $\mathbf{5{,}665\times10^{-14}}$ m |
| $r_1$ | $9{,}00\times10^{-15}$ | $\mathbf{9{,}016\times10^{-15}}$ m |
| Üç oran | 5876/5878/5880 | **hepsi 5870** ($5869{,}5$) |

Sayıların birbirinden farklı çıkması bağımsız teyit değil, **yuvarlama hatasının kanıtıydı.**

### 10.5.3 Özteşkil çözümde sapma **kare** oluyor
§10.4'te $v=\alpha c$ cevaptan ithal edilmişti. Kapanma koşulu ile kuvvet dengesi birlikte çözülürse:

$$r=\frac{c^2}{2\pi v f_0} \;\wedge\; v^2=\frac{k}{m_e r} \;\Longrightarrow\; v=\frac{2\pi k f_0}{m_ec^2}$$

Teorinin $f_0$'ı ile: $v = 1{,}28\times10^{10}$ m/s $=\mathbf{42{,}8\,c}$ ve $r_1 = 1{,}5\times10^{-18}$ m.
$r\propto1/f_0^2$ olduğundan **sapma $5870^2 = 3{,}4\times10^{7}$ kat.**

*(Zincirin cebiri sağlam: $f_0=\nu_C$ konduğunda aynı çözüm $v=\alpha c$ ve $r=a_0$ veriyor. Bozuk olan tek girdi $f_0$'dır.)*

### 10.5.4 Yapıcı olan: $c^2/v$ değerlendirmesi **doğrulandı**
§10.3'ün düzeltmesi hakem onayı aldı: $c^2/v$ bir **desen hızıdır**, eşzamanlılığın göreliliğinden doğar ($\varphi=\gamma\omega_0 t-(\gamma\omega_0v/c^2)x$), hiçbir şey o hızda taşınmaz. **Madde 8'in üst-ışık kanalı bu kaleme borçlandırılmamalı** — doğru karar.

### 10.5.5 ⛔ Elenen mekanizmalar (disk yarıçapını üretmek için denenenler)

| # | Mekanizma | Verdiği | Gereken | Sonuç |
|---|---|---|---|---|
| 1 | **Viskoz sınır tabakası** (Navier–Stokes). $\mathrm{Re}=\rho_n v_{cev}r_e/\eta_E \approx 4{,}6\times10^{20}$; $\delta/r\sim1/\sqrt{\mathrm{Re}}$ | $5\times10^{-11}$ | $5870$ | ⛔ **ters yön.** $\delta/r=5870$ için $\eta_E\approx3{,}7\times10^{17}$ Pa·s gerekir; teorinin kaydı $\lesssim2{,}3\times10^{-11}$ — **28 mertebe** |
| 2 | **Girdap dolanımı, kenar $v=c$'de.** $\Gamma=2\pi r_e v_{cev}=2{,}48\times10^{-7}$ m²/s, $r=\Gamma/2\pi c$ | $1{,}4\times r_e$ | $5870\times$ | ⛔ |
| 3 | **Dinamik basınç dengesi.** $\tfrac12\rho_n v^2=P_0=\tfrac14\rho_nc^2 \Rightarrow v=c/\sqrt2$, $r=\Gamma/2\pi v$ | **tam $2\times r_e$** | $5870\times$ | ⛔ |
| 4 | Prof. önerisi: **sürüklenme zarfı / entrainment** | (=1 ile aynı) | | ⛔ 1 ile aynı gerekçe |

### 10.5.6 🔴 YAPISAL TEŞHİS — sorun eksik hesap değil, eksik **uzunluk ölçeği**
Yukarıdaki üç mekanizma **2, 1,4 ve $5\times10^{-11}$** veriyor; hiçbiri 5870'e yakın bile değil. Nedeni tesadüf değil:

> **Teorinin basınç yasaları ölçekten bağımsızdır — hız verirler, uzunluk vermezler.** $c=\sqrt{P/\rho}$, $v_{denge}=\sqrt2c$, $v_{kav}=\sqrt2c\sqrt{1+\Sigma/P_0}$: hepsi hız. Teorinin elindeki tek uzunluk girdisi $r=(3m/4\pi\rho_n)^{1/3}$'tür ve o da 5870 kat küçük çıkıyor.

Yani açık, "doğru hesabı bulamadık" türünden değil: **teori 5870 mertebesinde bir boyutsuz büyüklük üretecek bir mekanizma içermiyor.** Kapanması için ya yeni bir uzunluk ölçeği postüla edilecek (yeni serbest parametre — Madde 21'e karşı ağır bedel) ya da henüz teoride olmayan bir mekanizmadan türetilecek.

### 10.5.7 ⚠️ ÖNLEYİCİ YASAK — bir sayı benzerliği fark edilecek
Biri şunu fark edecek: $\sqrt{m_p/m_e}\,/\,\alpha = 42{,}850\times137{,}036 = \mathbf{5873{,}5}$, ve hedef $5869{,}5$.

**Kullanılmayacak.** Gerekçe:
1. Sapma %0,07 — bu mertebede bir "uyum" hiçbir şey kanıtlamaz; teorinin başka yerlerinde %18'lik farklar $O(1)$ bütçesine yazılıyor.
2. Hedef sayı $\sqrt2(\hbar/m_ec)/(3m_e/4\pi\rho_n)^{1/3}$'tür, yani **$\hbar$ ve $\rho_n$'den** kuruludur. Aday ise $m_p,m_e,\alpha$'dan. İkisinin eşit olması için $\rho_n$ ile $\alpha$ arasında bir bağ gerekir — **teoride böyle bir bağ yok.**
3. $\rho_n$ nükleer doygunluk yoğunluğundan gelen **ampirik** bir girdidir; $\alpha$ ile ilişkilendirilmesi için ayrı bir türetim şart.
Yazılırsa bu, $\tau$, $R_{disk}$ ve $2\sqrt2/\alpha$ kalemlerinde reddedilen yama parametrenin dördüncü örneği olur.

### 10.5.7b 🔴 DAHA TEMEL BİR HATA — elektrona $\rho_n$ uygulanmış
§10.4'ün tamamı $r_e^{çek}=(3m_e/4\pi\rho_n)^{1/3}=9{,}304\times10^{-17}$ m üzerine kuruluydu. **Bu, teorinin kendi ifadesine aykırıdır.**

[2.1 karşılaştırma tablosu](../../Metin/Akademik/Kisim_2_Mikro_Evren/01_Mikro_Evren.md) öz yoğunlukları şöyle veriyor: nükleon **aşırı yüksek** ($\sim10^{17}$), Zerre **aşırı yüksek**, **elektron: "Aşırı Seyrek (Disk)"**. Yani elektron $\rho_n$'de **değildir**; $9{,}304\times10^{-17}$ m, elektron nükleon yoğunluğunda *olsaydı* sahip olacağı yarıçaptır — fiziksel bir büyüklük değil, bir varsayım artığıdır.

**Doğru çerçeve.** Gereken $r_{disk}=\sqrt2\hbar/m_ec = 5{,}461\times10^{-13}$ m ise, o yarıçaptaki ortalama yoğunluk:

$$\rho_e = \frac{m_e}{\tfrac43\pi r_{disk}^3} = \frac{9{,}109\times10^{-31}}{6{,}822\times10^{-37}} = 1{,}34\times10^{6}\ \text{kg/m}^3 \qquad \frac{\rho_n}{\rho_e} = \mathbf{2{,}0\times10^{11}}$$

> **Yani "5870 katlık gizemli uzunluk oranı" diye bir şey yok.** Olan şey **elektronun seyreklik çarpanıdır: $2{,}0\times10^{11}$.** Ve teori bunu niteliksel olarak zaten söylüyor ("aşırı seyrek"), yalnızca hiç sayısallaştırmamıştır.

**Kalemin doğru ifadesi:**
> Elektronun ortalama yoğunluğunu (eşdeğer olarak seyreklik çarpanını) teoriden türet. 2.1 mekanizma taslağını da veriyor: *"bu düşük yoğunluk elektronun sıkı ve yoğun bir küre şeklinde çökmesini engeller; bu yüzden elektron merkezkaç dinamiğiyle açılarak ortası boşluklu, geniş bir girdap rüzgarı (Disk) formunu alır."*

**Mertebe uyumu (ilk kez):** $2{,}0\times10^{11}$, teorinin $\Sigma/P_0>10^8$ sınırının **içindedir** ve ana plandaki $\Sigma/P_0\approx8\times10^{11}$ kestirimiyle aynı mertebededir. Bu, kohezyon kanalının bu kaleme bağlanabileceğine dair ilk somut işarettir — ama henüz bir mekanizma değil, yalnız mertebe uyumu.

**Ek elenmiş yollar (bu çerçevede denendi):**
| Mekanizma | Sonuç |
|---|---|
| Merkezkaç ↔ $P_0$: $R^2t = 4m_e/\pi\rho_n$ | ⛔ yine $m/\rho_n$'e düşüyor — ölçekten bağımsızlığın kanıtı |
| Merkezkaç ↔ $\Sigma$ | ⛔ $\Sigma>P_0$ olduğundan disk **küçülür**, ters yön |
| Merkezkaç ↔ viskoz gerilme $\eta_E\omega$ | ⛔ $R=6{,}3$ Å (**aşırı büyük**); doğru değer $\eta_E=0{,}035$ Pa·s ister, sınır $\le2{,}3\times10^{-11}$ |

**Daralan hedef:** kırılmak için $\rho_n c^2$ **olmayan** bir gerilme gerekiyor. Viskoz gerilme aşırı zayıf (disk çok büyüyor), kohezyon aşırı güçlü (disk küçülüyor). **Aradaki mertebede bir gerilme kaynağı aranıyor.**

### 10.5.8 Açığı gerçekten kapatacak şey
Kapanma için gereken tek şey **$h$ kullanmadan** bir uzunluk: $r_{disk}=5870\times r_e^{çek}$. Başarılırsa ödül büyüktür — $r_C=r_{disk}/\sqrt2$ ve $\hbar=m_ecr_C$, yani **$\hbar$'ın kendisi türetilmiş olur.** Bu, ana plandaki §19.15 ($\tau$ üzerinden $h$) ile birlikte **$h$'a iki bağımsız yol** demektir; ikisi aynı değeri verirse teorinin en güçlü sonucu olur.

**Ama §10.5.6'nın teşhisi ciddiye alınmalı:** bugünkü hâliyle teori bu uzunluğu üretemiyor. Bu kalem, "biraz daha hesap" değil, **yeni bir mekanizma** gerektiriyor. → §10.6'da altı mercekle arandı.

---

## 10.6 MEKANİZMA ARAMASI — ALTI MERCEK, ALTI ELEME *(10 Ağustos 2026)*

| Mercek | Verdi | Hüküm |
|---|---|---|
| Girdap halkası (log oranları) | 9,9 kat | ⛔ |
| Dönen akışkan dengesi (sabit duvar hızı) | $dE/dR\equiv0$ | ⛔ |
| Kavitasyon balonu / Young–Laplace | 0,46 µm ya da 24 mertebe eksik | ⛔ |
| Süperakışkan şifa uzunluğu | 1,65 kat | ⛔ |
| Tüketici boyut analizi | 1 kat (gerekçeli) | ⛔ |
| Elektron-özgül (kaynak/kuyu ayrımı) | $\hbar$ kalibre edilirse tam — döngüsel | ⛔ |

### 10.6.1 ✅ Yapıcı sonuç: **M-3 artık postülat değil, teorem**
İçi boş (hollow) girdabın serbest yüzey Bernoulli koşulu $P_0=\tfrac12\rho_0q^2$'dir. Teorinin kendi değerleri konduğunda:

$$q^2=\frac{2P_0}{\rho_0}=\frac{2\cdot\tfrac14\rho_nc^2}{\tfrac14\rho_n}=2c^2 \;\Longrightarrow\; \boxed{q=\sqrt2\,c}$$

**Tam olarak.** Yani *"her vakum-cepli girdap zarfı duvarını $\sqrt2c$ ile, boyutundan bağımsız döndürür"* ifadesi **klasik akışkanlar mekaniğinin bir teoremidir** — postülat olarak taşınmasına gerek yoktur. E1 kararının bağımsız doğrulanması.
→ **Bu bulgu yayın metnine taşınmalı** (Ek A / M-3): postülat listesinden çıkıp türetim listesine geçer.

### 10.6.2 🔴 KESİN SINIR — teori $\hbar$'ı üretemez (üretemedi değil, **üretemez**)
Bağımsız nicelik kümesi $\{\rho_n, c, m_e, \eta_E\}$. **Eylem** boyutunda kurulabilen kombinasyonlar tek parametreli bir aile oluşturur ve iki ucu vardır:

$$m_ec\left(\frac{m_e}{\rho_n}\right)^{1/3}=2{,}54\times10^{-38}\ \text{J·s} \qquad\text{ve}\qquad \frac{m_e\eta_E}{\rho_n}\le7{,}8\times10^{-59}\ \text{J·s}$$

$\hbar=1{,}055\times10^{-34}$ J·s, büyük olanın **4152 katıdır** ($\times\sqrt2=5871$ — aradığımız 5870).

**Uzunluk tarafında da aynı kapanış:** türetilebilir yalnız iki uzunluk var — $(m_e/\rho_n)^{1/3}=9{,}30\times10^{-17}$ m ve $\eta_E/\rho_nc=2{,}84\times10^{-37}$ m. Oranları $\mathrm{Re}=4{,}6\times10^{20}$'dir ve **$\eta_E$ yalnız üst sınır olduğundan $\mathrm{Re}$ yalnız alt sınırdır** → her $\mathrm{Re}$ yolu bir *değer* değil bir *sınır* verir. 5870 için $\mathrm{Re}^{0{,}182}$ gerekiyor; doğal bir sınır-tabaka üsteli değil ($1/4\to1{,}5\times10^5$, $1/5\to1{,}4\times10^4$, $1/6\to2781$).

> **İroni ve teşhisin kökü:** $\sqrt2c$'yi evrensel yapan şey (boyuttan bağımsızlık) tam olarak onun bir uzunluk üretmesini engelleyen şeydir. Postülatın gücü, boşluğun kaynağıdır.

### 10.6.3 Eleme gerekçeleri yapısaldır *(tekrar denenmesin)*
- **Girdap halkası:** bu mercekteki her yasa $m=\rho\,a^\alpha R^\beta[\log]$ biçimindedir, $\alpha+\beta=3$. İki yasanın oranı $m/\rho$'yu **daima** yok eder ve $\Lambda^{\Delta\alpha}=[\log$ oranı$]\approx15$ verir → $\Lambda\le15$. Kütle ($\alpha{=}2$), enerji ($\alpha{=}2$), gerilim ($\alpha{=}2$), impuls ($\alpha{=}1$) — hepsi buraya düşer. **Logaritmanın katkısı yalnız $14^{1/3}=2{,}41$ kat**; "log büyük oran üretir" umudu ölmüştür.
- **Dönen gövde:** sabit duvar hızı altında $E_{dön}=\tfrac12k_am_ev_w^2$ ve $R$'ye hiç bağlı değil → $dE/dR\equiv0$, hiçbir yarıçap seçilmiyor. Klasik dönen-damla problemlerinden (sabit $\omega$ ya da sabit $L$) yapısal olarak farklı ve **yozlaşmış**.
- **Elektron-özgül:** $\max(r_{çek},r_L)$ ayrımı $2{,}0226\times10^{11}$'i **tam** veriyor — ama yalnız $L=\hbar$ kalibre edildikten sonra. Döngüsel.

### 10.6.4 ⭐ KARAR ÖNERİSİ: bunu yenilgi değil **parite** olarak yaz
Standart fizik de $\hbar$'ı türetmez — **ölçer.** Teori de bir uzunluk girdisi alsın:

> **Elektronun disk yarıçapı** (eşdeğer olarak seyreklik çarpanı $\rho_n/\rho_e=2{,}0\times10^{11}$), **teorinin ölçülen girdi parametresidir** — $m_z$ için verilen kararla aynı statü (§17.4 / Anayasa Madde 21).

Karşılığında teori **türetir**: $\hbar=m_ec\,r_{disk}/\sqrt2$ · $a_0$ · Rydberg'in $1/n^2$ biçimi · Rydberg–Ritz toplanabilirliği · harmoniğin yokluğu · *harmonik ⟺ iki merkez* ayrıştırıcı öngörüsü · $\sqrt2c$ duvar hızı (§10.6.1, artık teorem).

**Girdi sayısında parite, mekanizmada kazanç.** Standart fizik $\hbar$'ı alır ve $1/n^2$'yi verir; teori bir uzunluk alır, aynı şeyi *artı mekanizmayı* verir. Uydurma değil — ilan edilmiş parametre.

**Ve bu, $\tau$ kalemiyle aynı desendir** (ana plan §19.15): $h$'a iki bağımsız yol da aynı duvara çarpıyor, çünkü teoride **eylem boyutunda bağımsız bir nicelik yok.** Bunu bir kez açıkça ilan etmek, altı ayrı yerde savunmaya çalışmaktan iyidir.

---

## 7. Görev Listesi (güncellendi)

**Öncelik sırası denetimden sonra yeniden dizildi (10 Ağu 2026):**

- [x] ~~**1. Harmonik-olmama itirazına cevap**~~ ✅ **KAPANDI (§9.3).** Cevap: ışıma bir dönüş frekansı değil, durağan düzen içinde bir geçiştir; harmonik teoremi zamansaldır ve durağan düzeni bağlamaz. Üstelik ayrıştırıcı öngörüye dönüştü: **harmonik ⟺ iki merkez.**
- [x] ~~**1'. $\lambda_{iz}\propto1/v$ türetimi**~~ ✅ **ÇÖZÜLDÜ (§10.3).** $1/v$'nin tamamı $v_{faz}=c^2/v$ desen hızından geliyor — eşzamanlılığın göreliliği, hakem onaylı. Üst-ışık kanal gerekmiyor.
- [x] ~~**Basamakların varlığı / kapanma kuralı**~~ ✅ **KAPANDI** — *Atom Geometrisi* yolu kuralı atlıyor: sayı geometriden ($2k^2$), çap sayıdan ($r\propto N$). §9.3 tablosuna bak. §10.2–10.3 programı artık **zorunlu değil**, alternatif yol olarak kalır.
- [x] ~~**Mutlak ölçek**~~ ✅ **KAPANDI — parite kararı uygulandı ve yayına taşındı.** Ek C satır 1-b ($a_0$, rozet **S**, sabitleyen gözlem: Rydberg sabiti) · 2.1 parite hükmü · 8.8 sembol satırı · 7.4 md. 6-b. *(Yasak yerinde: $\sqrt{m_p/m_e}/\alpha=5873$ benzerliği kullanılmayacak — §10.5.7.)*
- [x] ~~**Yönlü kimyasal bağ**~~ ✅ **KAPANDI — havale edildi.** 2.1'e dürüst kayıt, 7.4 md. 6-d'ye seri içi havale (*Kimyasal Bağ* kitabı). Bu kitabın borcu değil.
- [x] ~~**§9.3.4 kapsam beyanı + "bileşik yapıların tayfı"**~~ ✅ **KAPANDI.** Kapsam beyanı ve **"harmonik ⟺ iki merkez"** ayrıştırıcı öngörüsü (CO/Landau/Zeeman karşılaştırma tablosu ve $l$-yozlaşması kanıtıyla) 2.1'e yazıldı; bileşik tayfları 7.4 md. 6-d'ye havale edildi.
- [x] ~~**§9.6'nın altı borcu**~~ ✅ **KAPANDI — 7.4 md. 6-c olarak yazıldı.** Altısı da "açıklandı" sayılmıyor; (f) maddesi fırsat kalemi olarak işaretlendi ($A\propto n$ sınavı, değişken-$c$ ile Eu³⁺ ölçümü).
- [x] ~~**Aday 3'ün merger diliyle nicelleştirilmesi**~~ ✅ **KONUSUZ KALDI.** Dışlama, *Atom Geometrisi*'nin mekanizmasıyla kapandı: bir kabuk = tek yörünge, karşılıklı yük itmesi mesafeyi eşit tutar. Vortex-merger yoluna gerek yok.
- [x] ~~**Hedef bar: hidrojen**~~ ✅ **KAPANDI.** 7.4 md. 6-b "her element" iddia etmiyor; 2.1'in notu da yalnız oran ve biçim iddia ediyor. §2.1'in kaydı (kapalı form yalnız tek elektronlu sistemlerde) arşivde duruyor.
- [x] ~~**Örgünün taşıyıcısını elektron kabuğuna taşı**~~ ⚠️ **KALEM GEÇERSİZ — yanlış soruyu soruyordu.** Örgünün *saat* rolü §10.6'da geri alındı (frekans ölçeği örgüden gelmiyor), ve *Atom Geometrisi*'nde çekirdek kabukları **geometrik** olarak belirliyor — **ritmik** olarak değil. Yani "taşıyıcı kim?" sorusu ortadan kalktı: örgü bir ritim kaynağı değil, **durağan bir düzendir**; kabuk sayılarını ve yarıçap oranlarını o düzenin geometrisi verir. Elektron kabuğuna taşıma gereği yoktur.

- [x] ~~**§9.7 karşılıklılık ikilemi**~~ ✅ **KAPANDI (yazar onayı, 10 Ağu 2026): teori KARŞILIKLI DEĞİLDİR.** Gerekçe ve hüküm: **§11**.

---

## 11. §9.7'NİN HÜKMÜ — TEORİ KARŞILIKLI DEĞİLDİR ✅ *(10 Ağustos 2026, yazar onayı)*

### 11.1 İkilem yanlış kurulmuştu
Denetçi ikilemi şöyle koymuştu: *karşılıklıysa yalnız eşevreli esnek saçılma verir (kendiliğinden yayma, Stokes, Raman, kazanç imkânsız); karşılıklı değilse çizgi örtüşmesinin garantisi düşer.* İkinci kanat **geçersizdir**: çizgi örtüşmesi karşılıklılıktan değil, **paylaşılan merdivenden** gelir.

### 11.2 Hüküm: asimetri kurucudur
Teoride soğurma ve yayma birbirinin zaman-tersi **değildir**:

| | Mekanizma |
|---|---|
| **Soğurma** | $N$ vuruşun $\tau$ penceresi içinde **birikmesi** — kademeli, gelen akı gerektirir |
| **Yayma** | Zarfın **tek seferde boşalması** — gelen akı gerektirmez |

Biriktirme ile boşaltma simetrik süreçler değildir. **Karşılıklılığın kırılması sonradan eklenmiş bir düzeltme değil, pencere mekaniğinin kendisidir.**

### 11.3 Denetçinin saydığı "istisnalar" bu asimetriden çıkıyor
| Olgu | Teoride nereden |
|---|---|
| Soğurma listesinin yayma listesinden **dar** olması (soğuk H, Hα'yı soğurmaz; $n_2/n_1=1{,}9\times10^{-171}$) | Soğurma $\tau$ içinde $N$ vuruş ister; akı yetmezse soğurma olmaz |
| Yaymanın akısız olabilmesi (H II bölgeleri Hα'yı en parlak çizgi olarak yayar) | Boşalma tek olaydır, gelen katar gerekmez |
| **Stokes kayması** (floresein 490→514 nm) | Biriken enerjinin bir kısmı boşalmadan önce girdabın iç gevşemesine gider → çıkan ritim düşer |
| **Lazer kazancı** | Önceden yüklü zarflar, geçen katarla eşzamanlı boşalmaya tetiklenir |
| Çizginin işaretinin ortama bağlı olması (Na D: fotosferde soğurma, kromosferde yayma) | Soğurma akıya, yayma yüke bağlı; oran ortamın $dT/d\tau$'suna göre değişir |

### 11.4 Örtüşme nereden geliyor
Soğurma $r_i\to r_j$, yayma $r_j\to r_i$. **İkisi de aynı izinli yarıçap kümesi** arasındaki geçiştir; dolayısıyla vuru frekansları **aynı kümedir**. Yönle değişen şey **hız ve şiddet**, frekans değil.

> **Konumlar ortak merdivenden, hızlar yönden.** Örtüşme için karşılıklılık gerekmez; **ortak seviye yapısı** yeterlidir — daha zayıf ve sağlanabilir bir koşul.

### 11.5 Bedeli — ve bedelin zaten ödenmiş olduğu
Karşılıklılık bırakıldığında **hızlar** borçlanılır: $A/B$, $g$-faktörleri, $\nu^3$ ölçeklemesi, Kennard–Stepanov. **Ama bu borç zaten listededir** (7.4, md. 6-c). Yani seçim yeni borç yaratmıyor; mevcut borcun **yerini doğru gösteriyor.** Karşılıklı seçenek ise borç yaratmak yerine olguları (kendiliğinden yayma, Stokes, Raman, kazanç) **imkânsız** kılardı — çok daha pahalı.

### 11.6 Yayına taşındı
Asimetri hükmü `Kisim_9/02_Planck_Sabiti_ve_Kuantum_Eylemi.md`'ye eklendi (pencere mekaniğinin doğal devamı olarak) ve 7.4 md. 6-c ile bağlandı.

**İptal edilen kalemler:**
- ~~§4.4 ayırt edici sınav (a/b)~~ — §4 denetimden geçemedi (§9.2), soru konusuz kaldı.
- ~~$2\sqrt2/\alpha$ çarpanının 9.6'dan çıkarılması~~ — $\sqrt2$ sadeleştiği için çarpan zaten $\alpha$'ya indi; bu bir kazanç değil, Rydberg'in yeniden yazımı.

> **Sonuç Hedefi:** Bu belge olgunlaştığında "Kısım 9: Mikro Doğrulamalar" içine yeni bir bölüm olarak entegre edilecektir (*9.X Atom Spektrumları ve Kesikli Yörüngelerin Hidrodinamiği*). — **Yapıldı:** 9.11 olarak yazıldı ve `app.js`'e kaydedildi (10 Ağu 2026).

---

# §12 DENETİM SONRASI REVİZYON — "virüs" teşhisi ve iki mekanizma değişikliği
*(10 Ağustos 2026)*

## 12.1 Ne oldu
9.11 yazıldıktan sonra dört cepheli denetime verildi. **Dördü de `CIDDI_SORUN` döndü; 75 bulgu, 16'sı kritik.** Merkezî bulgular:

1. **Yarıçap türetimi diye sunulan şey türetim değildi.** "$r\propto N$" bir kuraldı: hem merkez çekimi hem karşılıklı itme $1/r^2$ gittiği için $r$ sadeleşir — salt yük mekaniğinde denge yarıçapı **hiç yoktur** (Earnshaw). Ne mutlak değer, ne oran.
2. **Mekanizma hidrojende boştu.** Her seviyede $N=1$; "elektron sayısı çapı belirler" tek elektronla merdiven vermez.
3. **Vuru yanlış seri veriyordu.** Kepler dolanma frekansıyla ($\Omega\propto n^{-3}$) vuru $(1/n_1^3-1/n_2^3)$ verir: Ly-α 52,07 nm (gözlem 121,50), Balmer-α 517,98 nm (656,11).
4. **Ölçülmüş karşı-örnek.** Rydberg atomlarında ışıma klasik dolanma frekansına yakınsıyor: $\nu(51\!\to\!50)=51{,}07$ GHz vs $f_{dolanma}(n{\approx}50{,}5)=51{,}09$ GHz.
5. **Gizli üçüncü girdi.** Dalga boyu sütunu $\lambda=hc/\Delta E$ ile kuruluydu; parite iddiası ikiye iki değil üçe üçtü.
6. **Döngüsellik.** $E_1=k_e/2a_0 \equiv hcR_\infty$; $a_0$'ı sabitleyen gözlem Rydberg sabiti olduğuna göre $-13{,}606$ eV bir sınav değil, girdinin geri okunması.
7. **Sayısal hatalar.** Paschen-α teori değeri **1875,28 → 1874,607 nm**; "Ölçülen" sütunu aslında $R_H$'den hesaplanmıştı; trityum 656,229 → 656,232 nm.

Kullanıcının teşhisi şu oldu: *"üzerine gidelim türetecek mekanizmamız var. sanırım standart bilimin metotlarından virüs bulaşmış olabilir."* — **Teşhis doğruydu.** Çürütmelerin ikisi teorinin kendi mekanizmasını değil, **standart fiziğin çatısını** varsayıyordu.

## 12.2 Virüs 1 — elektronu nokta yük saymak
Earnshaw itirazı **nokta yüklerden kurulu bir kuvvet dengesini** çürütür. Teoride elektron nokta değil, süpürdüğü diski olan bir girdaptır (2.1) ve girdaplar üst üste binemez. Kısıt bu yüzden kuvvet değil **yer kaplamadır** — ve geometrik kısıtları Earnshaw bağlamaz.

$$2\pi r_k = N_k\,s \;\Longrightarrow\; r_k = \frac{k^2 s}{\pi} \;\Longrightarrow\; 1:4:9:16$$

Kazançlar:
- **Oran yaklaşık değil tam** — çevre tam bölünür. "Eşit yay mı kiriş mi" tartışması konusuz: elektron halka *boyunca* gider, engelleyen şey bir yaydır.
- **Earnshaw çürütme değil dayanak** — yarıçapın yükten gelemeyeceğinin kanıtı, geometriden gelmesi gerektiğinin kanıtıdır.
- **Hidrojen kapanır:** kural katmanın **kapasitesini** kullanır, doluluğunu değil. İzler üzerlerinde elektron olmasa da vardır (kullanıcının "örgünün izleri" fikri). Bu bir **posit**tir ve öyle yazıldı — karşılığında açısal momentum kuantumlaması varsayımı düştü.
- Ölçek: $s=\pi a_0 = 1{,}6625\times10^{-10}$ m. Atomlarda tipik elektron-elektron mesafesinin mertebesi.
- Elektron neden tam sınırda durur: **kuyu çeker, geometri durdurur** — izin verilen en derin yarıçap.

## 12.3 Virüs 2 — Kepler dolanma frekansını ritim saymak
Denetçi $v=\sqrt{k_e/mr}$ aldı. Teorinin ritmi bu değil: Postülat 5'in duvar hızı yasası (M-3) duvarı **boyuttan bağımsız** $\sqrt2c$'de döndürür.

$$\Omega_k = \frac{\sqrt2 c}{r_k} \propto \frac{1}{k^2} \;\Longrightarrow\; \text{vuru} \propto \left(\frac{1}{k_1^2}-\frac{1}{k_2^2}\right)$$

**Rydberg biçimi doğrudan çıkar** — ve bu, teoriyi sınanabilir kılar: ödünç alınmış kinematik yanlış seri verir, teorinin kendi yasası doğru seriyi verir. $1/n^2$ yapısı $\sqrt2c$ yasasının imzası oldu.

## 12.4 Karşı-örnek teyide döndü
$n^{-2}$ giden niceliklerin komşu vurusu zorunlu olarak $n^{-3}$ ile gider:
$$\frac{1}{(n-j)^2}-\frac{1}{n^2} = \frac{j(2n-j)}{n^2(n-j)^2} \approx \frac{2j}{n^3}$$
- $j=1$: klasik dolanma frekansına yakınsama → uyum ilkesi **teori-içi sonuç**, çelişki değil. ($\nu(51\!\to\!50)=51{,}072$ vs $f_{dolanma}(50{,}5)=51{,}062$ GHz; $2\times10^{-4}$.)
- $j$'de doğrusal → yüksek $n$'de **harmonik** tayf. H110α/β/γ: 4,874 · 9,618 · 14,237 GHz = $1:1{,}97:2{,}92$ (%3). Radyo astronomisi H110α'yı 4,874 GHz'de ölçüyor.

**Hüküm düzeltildi:** *"harmonik ⟺ iki merkez"* → **"harmonik ⟺ terim farkları doğrusallaşır"** (rijit dönme *veya* yüksek $n$). Daha genel, daha güçlü, ve iki rejimi de öngörüyor.

## 12.5 🔴 Yürürlükten kalkan hükümler
Aşağıdakiler bu dosyada duruyor ama artık **hüküm değil, kayıttır**:
- **§4.1–4.4 bütünüyle** — "ateşleme ritmi = dönüş ritmi, ilgili yarıçap $a_0$ mı 20,5 nm mi" ikilemi. §12.3 ile konusuz kaldı: ritim duvar frekansı, ölçek çarpanı görev çevrimi.
- **§9.3'ün *harmonik ⟺ iki merkez* tablosu** — §12.4 ile genelleştirildi.
- **§10.2–10.4'ün $c^2/v$ zinciri** — Rydberg biçimi artık duvar hızı yasasından geliyor, faz hızından değil.
- **§10.4'ün 5870 hedefi** — o hedef elektronun kavitasyon yarıçapına dayanıyordu (§10.5.7b'de zaten reddedildi); çevre paylaşımı bambaşka bir uzunluk kullanıyor ($s$, ölçülen girdi).

**Yürürlükte kalanlar:** dört yasak (§4.3, §10.3, §10.5.7, §10.5.7b), §9.1–9.2'nin eleme kayıtları, §10.5'in totoloji kanıtı, §11'in tamamı (karşılıklılık hükmü).

## 12.6 ⚠️ §4.3'ün yasağı ihlal edildi ve geri alındı
İlk yazımda görev çevrimi şöyle yazıldı: *"$\eta_d$ serbest değildir, kesin olarak $\alpha/2\sqrt2$'dir; bir yama değildir."*

**Bu, §4.3'ün açıkça yasakladığı hamledir.** Gerekçe: $a_0R_\infty=\alpha/4\pi$ **standart sabitlerin bir özdeşliğidir.** $a_0$ girdi, Rydberg sabiti de onu sabitleyen gözlem olduğuna göre $\eta_d=\alpha/2\sqrt2$ bir türetim değil, o özdeşliğin yeniden yazımıdır — teori $\alpha$'yı üretmiş olmaz. Yazım geri alındı; $\eta_d$ **türetilmemiş ikinci girdi** olarak envantere geçti ve $\alpha$ benzerliği açık bir uyarı kutusuyla reddedildi.

**Ders:** virüsü temizlerken karşı yöne sapma riski var. Bir çürütmenin standart-fizik varsayımına dayandığını göstermek, o boşluğa serbestçe sayı yazma izni vermiyor.

## 12.7 Karşılığında doğan yapısal kazanç
$\eta_d$ girdi olarak alındığında, enerji ($1/r$ topografyası) ve frekans (duvar hızı) iki **ayrı** yoldan geldiği için oranları $h$'ı ödünç almadan kurar:

$$h = \frac{\Delta E}{\nu} = \frac{\pi k_e}{\eta_d\sqrt2\,c} = 6{,}626\times10^{-34}\ \text{J·s}$$

Statüsü 9.2'nin $h=\delta\tau$ kaydıyla **birebir aynı**: $\eta_d$ tayfla sabitlendiği için sayısal öngörü değil, **mekanik ayrıştırma**. Söylediği: $h$ temel sabit değil; bir yük katsayısı, bir hız ve bir görev çevrimine ayrılıyor. Ve iki borç ($\eta_d$, $\tau$) aynı mekanizmaya bakıyor — biri kapanırsa öteki de kapanabilir.

## 12.8 Girdisiz sınav — teorinin gerçek kanıtı
Oranlarda ne $s$, ne $\eta_d$, ne $k_e$, ne $h$ var. $\eta_d$ sadeleşir, indirgenmiş kütle düzeltmesi sadeleşir. Teori sütunu **kesin kesir**:

| Çizgi | Teori $\nu/\nu_{Ly\alpha}$ | Ölçülenden | Sapma |
|---|---|---|---|
| Balmer-α | $5/27$ | 0,1851857 | $+2{,}7\times10^{-6}$ |
| Balmer-β | $1/4$ | 0,2500000 | $<10^{-7}$ |
| Balmer-γ | $7/25$ | 0,2799999 | $-3{,}3\times10^{-7}$ |
| Paschen-α | $7/108$ | 0,0648146 | $-2{,}6\times10^{-6}$ |

Dört bağımsız oran, $10^{-5}$ içinde — ve sapma alıntılanan çizgi merkezlerinin basamak sayısıyla sınırlı. **Bu tablo bölümün asıl kanıtıdır**; mutlak konumlar tablosu (9.11.9-ii) kalibrasyondur ve öyle yazıldı.

## 12.9 Açılan üç yeni kalem (7.4 md. 6-g)
| Kalem | Neden açık | Kapsam |
|---|---|---|
| **① $\eta_d$** | görev çevriminin mekanizması pencere mekaniğinden türetilmeli | bu kitabın borcu |
| **② $Z$ ölçeklemesi** | çevre paylaşımı yarıçapı elektron sayısından kurar, çekirdek yükünden değil; He⁺ Ly-α 30,378 nm ($r=a_0/Z$) paketlemeden çıkmaz — kuyu derinliğinden gelmeli | bu kitabın borcu, bar'ın hemen yanı |
| **③ Katman yinelenmesi** | periyot uzunlukları yinelenir (2,8,8,18,18,32,32); aynı kapasite aynı yarıçap verir, gerçekte vermez | çok elektronlu; bar'ın dışında |

## 12.10 Yayına taşınanlar
| Dosya | Ne değişti |
|---|---|
| `Kisim_9/11_Atom_Spektrumlari...md` | **bütünüyle yeniden yazıldı** — §9.11.4 çevre paylaşımı, §9.11.6 duvar frekansı + $h$ ayrıştırması, §9.11.7 harmonik hükmü genelleştirildi, §9.11.9 iki katmanlı (girdisiz oranlar + kalibrasyon), §9.11.10 üçe üç parite, §9.11.11 dört kalem |
| `Kisim_2/01_Mikro_Evren.md` | Kabuk Sayıları notu aynı iki mekanizmayla düzeltildi; harmonik tablosuna yüksek-$n$ satırı |
| `Kisim_7/04_Tartisma_ve_Sonuc.md` | md. 6-b yeniden yazıldı; **md. 6-g eklendi** (üç yeni kalem) |
| `Kisim_8/08_Sembol_Sozlugu.md` | $s$ ve $\eta_d$ satırları eklendi; $a_0$ satırı çevre paylaşımına bağlandı |
| `Kisim_1/06_Evrenaki_Terminolojisi.md` | **Çevre Paylaşımı** maddesi eklendi |

---

# §13 ÖRGÜ TURU — $Z$ ÖLÇEKLEMESİ VE $\Omega\propto1/r$ DENETİMİ
*(10 Ağustos 2026 · 13 ajanlı workflow: 5 türetim yolu + sayısal sınavlar + düşmanca çürütmeler + bağımsız $\Omega$ denetimi)*

> ## 🔴 İKİ MANŞET
> **1.** $Z$ ölçeklemesi **KAPANMADI.** Beş bağımsız yol denendi, beşi de başarısız. İki kalıcı teorem çıktı (§13.2).
> **2.** Daha ağırı: **$\Omega\propto1/r$ yasası ayakta kalmadı** ve 9.11.6'nın tamamı ona asılıydı (§13.3).
> Bu tur bir kazanç turu değil, bir **temizlik** turudur. Kazanç, beş sokağın sayılarıyla kapatılmasıdır.

## 13.1 Yazarın üç düzeltmesi (bu turun girdisi)
1. **Örgü birincildir.** "Bir kabuk tek yörünge" doğru, ama o yörüngenin desenini/örgüsünü **çekirdeğin devinimi** belirler. Elektron yörüngeleri böylece her yerde küresel bir örgüye kavuşur; örgü yörüngenin kahramanıdır.
2. **Elektron kuyuya inmez.** "Yörüngeler hep aynı örgüyü işler" — yarıçap bir *derinlik* değildir; elektron iz arar, derinlik aramaz. **C yolunun çatısı bu hükümle düşmüştür** (bulgudan önce, yazar kararıyla).
3. **Kapı kuralı.** Örgü kapısından ne giriyorsa yalnız o çıkabilir, çünkü örgü deseni hep aynıdır.

**Nedensellik tersine çevrildi** ve bu bir kazançtır: artık $N$ yarıçapı belirlemiyor, yarıçap $N$'i belirliyor ($N_k=2\pi r_k/s$). Bu, denetimin **M4** bulgusunu (minimizasyon ile "kapasite" positinin birbirini iptal etmesi) kaldırır ve hidrojen positini gereksiz kılar. Bedeli: $2k^2$ artık girdi değil **sınav** — kare katman geometrisi ile örgünün yuva sayımı bağımsız olarak aynı sayıyı vermek zorunda (denetimin **K-8**'i tam buraya bakıyor).

## 13.2 İKİ KALICI TEOREM — bu turun asıl ürünü

### T-A · Seçici Lemması: kuyu derinliği yarıçapı **hiçbir zaman** seçemez
İzinli küme $\mathcal{A}=\{Ns/2\pi\}$ $Z$'den bağımsız ve kuyu $U_Z=-Z\,f(r)$ ile $f$ monoton azalan ise:
$$\arg\min_{\mathcal{A}} U_Z \;\text{her } Z \text{ için aynıdır}$$
çünkü **pozitif bir çarpan argmin'i kaydırmaz.** $f=k_e/2r$'ye özel değil — her $f\propto1/r^p$, $p>0$ için geçerli. Yani kuyunun *biçimini* değiştirmek de kurtarmaz.
**Sonuç:** C yolu kalıcı olarak kapalıdır. $p=0$ tam. He⁺'de dalga boyunda 4,00 kat ($Z$ enerjiye elle sokulursa 2,00 kat).

### T-B · Örgünün mesh adımı bir **uzunluk** olmak zorunda, **açı olamaz**
Mesh adımını açısal alırsak $s=r\,\Delta\varphi$ ve çevre paylaşımına koyarsak:
$$2\pi r = N\,r\,\Delta\varphi \;\Longrightarrow\; 1 = \frac{N\,\Delta\varphi}{2\pi}$$
**$r$ özdeş olarak düşer.** $\Delta\varphi=2\pi/(Zm)$ gibi her seçim yalnız $N$ üzerinde kısıt verir ve **her yarıçap çözümdür** — merdiven ölür. ($Z\in\{1,2,3\}$, $m\in\{2,8\}$ için altı durumda da $r$ belirsiz kaldı.)
**Sonuç:** Örgü dönüşlerden dokunuyorsa doğal ürünü bir **açıdır**. Uzunluk ya (i) bir çekirdek uzunluğundan ya (ii) bir hız/frekans oranından **ithal** edilmek zorundadır. **Beş yolun neden düştüğünü tek başına bu teorem açıklıyor.**

## 13.3 🔴 $\Omega\propto1/r$ ÇÖKTÜ — $Z$'den daha temel bulgu

**(a) M-3 bir nesne yasasıdır, alan yasası değildir.** Ek A.2/M-3′'ün türetimi: akış alanı potansiyel girdap ($v_\theta=\Gamma/2\pi r$), ayırt edici yarıçapta hız $\sqrt2c$, ve $r_e=\Gamma/2\pi\sqrt2c$. Yasanın ifadesi: *her zarf **kendi** e-katlanma yarıçapında $\sqrt2c$'ye sahiptir.* Evrensellik = **$\Gamma$'dan bağımsızlık**, yani nesneden nesneye. Alan yasası olabilmesi için $|v(r)|=\sqrt2c$'nin $r_1\dots r_4$'ün **hepsinde** doğru olması gerekir — bu M-3'ün kendi akış alanı ($v\propto1/r$) değildir ve dönüsüzlük/Crocco tabanını ihlal eder ($v=$sabit için vortisite $\ne0$).

**Üçüncü nesne itirazı sayıyla doğrulandı:** proton $\Omega_p=5{,}047\times10^{23}$ rad/s ($r=0{,}84$ fm) · elektron gözlenen $\sim1{,}236\times10^{20}$ Hz $\Rightarrow r_{zarf}=5{,}461\times10^{-13}$ m $=a_0/96{,}9$ · 9.11.6'nın $f_1=1{,}2751\times10^{18}$ Hz $\Rightarrow r=a_0$, **elektronun 96,9 katı, protonun 63.000 katı.** $a_0$ yarıçaplı bir zarf envanterde **yok**.

**(b) $r^{-3/2}$ çıkarımı doğrulandı — ve zaten kitapta yazılı.**
- Bernoulli: $\tfrac12\rho v^2 = P_0-P(r)=\alpha_g M/r \Rightarrow v\propto r^{-1/2}\Rightarrow \Omega\propto r^{-3/2}$
- Siklostrofik (Ek B.4'ün kendi denklemi): $v_\theta^2 = r(dP/dr)/\rho_0 \Rightarrow$ aynı üs. *(Kontrol: $v(4a_0)/v(a_0)=0{,}5000=4^{-1/2}$.)*
- **Ek A.4 (M-9/DY-1/M-22) bunu açıkça yazıyor:** $v_\theta=\sqrt{\rho_n/\rho_0}\,v_{yör}=2v_{yör}$, $v_{yör}=\sqrt{\mathcal{G}M/R}\propto R^{-1/2}$. **Teorinin bir kütle merkezi çevresindeki kendi dolaşım yasası Kepler ölçeklemesidir.**

Teori **iki** açısal hız yasası taşıyor ve 9.11.6 alan yasası gereken yerde nesne yasasını kullanıyor:

| Yasa | Kaynak | $\Omega(r)$ | $r\propto k^2$ üzerinde seri |
|---|---|---|---|
| Nesne yasası M-3 | Ek A.2 / M-3′ | $\sqrt2c/R_{kendi}$ (nesne başına tek sayı) | seri vermez |
| **Alan yasası** DY-1/M-22 | Ek A.4, Ek B.4 | $\propto r^{-3/2}$ | $(1/n_1^3-1/n_2^3)$ ✗ |
| Potansiyel girdap (M-3'ün kendi alanı) | M-3 varsayım 2 | $\propto r^{-2}$ | $(1/n_1^4-1/n_2^4)$ ✗ |

**(c) Genlik de ölü — 22 mertebe.** Protonun deplasman kuyusu $a_0$'da $\Delta P=5{,}696\times10^{-10}$ Pa ($\Delta P/P_0=9{,}39\times10^{-44}$) $\Rightarrow v_{siklo}=9{,}19\times10^{-14}$ m/s, $f=2{,}76\times10^{-4}$ Hz. Gereken $f_1$'in **$2{,}2\times10^{-22}$ katı.**

**(d) 🔴 $\sqrt2c$ her mutlak öngörüden TAM olarak sadeleşiyor.** $\eta_d\equiv cR_\infty/f_1$ olduğundan, herhangi bir duvar hızı $\kappa c$ için $\eta_d f_1\equiv cR_\infty$:

| varsayılan duvar hızı | $f_1$ (Hz) | $\eta_d$ | $\eta_d f_1$ |
|---|---|---|---|
| $1{,}000\,c$ | $9{,}017\times10^{17}$ | $3{,}649\times10^{-3}$ | $3{,}289842\times10^{15}$ |
| $\mathbf{1{,}414\,c}$ | $1{,}2751\times10^{18}$ | $2{,}580\times10^{-3}$ | $3{,}289842\times10^{15}$ |
| $2{,}000\,c$ | $1{,}8033\times10^{18}$ | $1{,}824\times10^{-3}$ | $3{,}289842\times10^{15}$ |
| $100\,c$ | $9{,}017\times10^{19}$ | $3{,}649\times10^{-5}$ | $3{,}289842\times10^{15}$ |

Dolayısıyla §12.3'ün *"$1/n^2$ yapısı teorinin kendi $\sqrt2c$ yasasının imzasıdır"* cümlesi **sayısal olarak boştur.** İmza atan şey $\sqrt2$ değil, "hız $r$'den bağımsızdır" **varsayımıdır** — ve M-3 tam onu lisanslamıyor.
Dahası $\Omega_k=C/k^2+D$'nin $D$'si her vuruda sadeleşir, $C$ ise $\eta_d$'ye gömülür: **tayf ne yasanın biçimini ne mutlak ölçeğini sınıyor.**

### 13.3.1 ⚠️ KENDİ KAYDIMDA ÇELİŞKİ — düzeltilmesi zorunlu
Çalışma dosyası **§9.2 md.1** zaten şunu yazıyor: *"$\sqrt2$ tamamen sadeleşiyor… bu hesap $\sqrt2c$ duvar hızı için **sıfır kanıt** sağlar; $\sqrt2$ kozmetiktir."* Ve **§12.5** onu "yürürlükte kalanlar" listesine koydu. Ama **§12.3** ("Virüs 2") bunun tersini hüküm yaptı. **Aynı dosyada iki çelişik hüküm vardı.** §9.2 md.1 geçerlidir; §12.3'ün imza iddiası **yürürlükten kalkmıştır.**

### 13.3.2 Kurtarma adayları — hepsi kesici sayılarla elendi
| Aday | Nasıl öldü |
|---|---|
| **(a)** Her kabuk bir kavitasyon sınırı ($P\to0$) | $\sqrt2c$ için tam %100 basınç açığı gerekir ($=P_0$). Protonun bütçesi $9{,}39\times10^{-44}$ → **boşluk $10^{43}$**. Enerji bütçesi: $a_0$ küresinde $3{,}77\times10^3$ J $=1{,}73\times10^{21}\times13{,}6$ eV. İnce halka kaçışı da kapalı: $\delta\le5{,}86\times10^{-22}$ m (bütçe 13,6 eV), $m_ec^2$ bütçesiyle bile $1{,}14\times10^{-19}$ m — Zerre yarıçapından 9, elektron zarfından 4800 kat küçük. Ayrıca **M-3′ keskin duvarı zaten kaldırdı**; 9.11.6'nın "zarfın duvar frekansı" dili **yürürlükten kalkmış M-3 okumasına** yazılmış |
| **(a′)** Elektron halka boyunca $\sqrt2c$ ile gidiyor | $v_{yör}(a_0)=\alpha c=2{,}188\times10^6$ m/s; $\sqrt2c/v_{yör}=193{,}8$. **İnce yapı doğrudan $(v/c)^2$ ölçer:** gözlenen $\alpha^2=5{,}33\times10^{-5}$, $v=\sqrt2c$ olsa 2 → **37.558 kat** büyük yarılma. 9.11.9'un "ince yapı düzeyinde $10^{-5}$" kaydı, **atomda hiçbir şeyin $\sqrt2c$ ile hareket etmediğinin ölçülmüş kanıtıdır** |
| **(b)** Örgünün desen dönme hızı | **Rijit desen → tek $\omega$ → $\Omega_1=\Omega_2$ → vuru = 0.** Devinen çekirdek tek gövdedir; frekans kümesi $\{\Omega_p, \omega_{dev}, \text{kombinasyonlar}\}$ — ayrık ama $1/k^2$ merdiveni değil. Çalışma dosyası **§9.1** bunu zaten elemiş (gereken $L=5{,}4\times10^{-6}\hbar$) |
| **(c)** Elektronun kendi zarfı kabukla büyüyor | Deplasman $\propto r_e^3$; $n{=}1\to4$'te $r_e\times16 \Rightarrow m\times4096$. Gözlenen 12,75 eV $\Rightarrow \Delta m/m_e=2{,}50\times10^{-5} \Rightarrow$ izin verilen kesirli yarıçap değişimi $8{,}32\times10^{-6}$; gereken 15. **Aşım $1{,}80\times10^6$** |
| **(d1)** Kabuğun kendisi bir halka-girdabı | Minör yarıçap $10^{-13}$ m alınsa bile deplasman kütlesi $7{,}8\times10^{11}\,m_e$ — üstelik "izler elektron olmasa da vardır" positi gereği **her $k$ için aynı anda** |
| **(d2)** Yay/dolanma türevleri | $v_{yör}/s \propto k^{-1}$ · $N_k f_{dol}\propto k^{-1}$ · kuantumlanmış $\Gamma\propto n$ → $n^{-3}$ (ayrıca $h$ ithal eder, **§10.3 ihlali**) — hepsi yanlış üs |
| **(d3)** Faz/desen kanalı | Tek hayatta kalan, ama **YENİ POSİT** ($\sqrt2c$ hızlı bir desen/faz kanalı) ve Ek A.1'in şok argümanıyla çarpışıyor |

## 13.4 BEŞ YOLUN ELEME KAYDI — bu sokaklara bir daha girilmesin

### A-mesh — $s$'nin örgü mesh adımı olarak yeniden atfı *(üs türetildi, mekanizma öldü)*
**Kurulum (damga saati):** Protonlar kaynaktır, nötronlar örgüye damga atmaz (2.1 yük notu). M-3 gereği tek-proton damga saati her çekirdekte özdeştir: $f_p=\sqrt2c/2\pi r_p=8{,}0330\times10^{22}$ Hz. $Z$ proton aynı örgüye eşit fazla iç içe damga vurursa $s=2\pi r_p/Z$, ve çevre paylaşımıyla
$$r_k(Z)=\frac{k^2 s_1}{\pi Z}=\frac{k^2 a_0}{Z} \quad\Longrightarrow\quad p=-1 \text{ TAM (yaklaşık değil)}$$
$E=-Zk_e/2r$ ile birlikte doğrudan $E\propto Z^2$. $A$ bağımlılığı yok → izotop saflığı **öngörü** olur ($|d\ln s/d\ln A|\lesssim2{,}7\times10^{-4}$ koşulunu kendiliğinden sağlar).
**🔴 ÖLDÜREN SINAV — MÜONİK HİDROJEN, 185,8 KAT.** Mekanizmanın kurucu iddiası: *örgü ortamın malıdır, işgalcinin değil* — yani **yarıçap yörüngedeki parçacığın kütlesini görmez.** Müonik hidrojenin yarıçapı 186 kat küçüktür. Kendi kurucu iddiası mekanizmayı öldürüyor.
**Ek bedeller:** (i) yeni boyutsuz parametre $\Lambda=3{,}1499\times10^4$ (mesh büyütmesi) — Ek C'de satır gerektirir ve §10.6.2'nin uzunluk kümesi bu oranı vermez; (ii) "bir tur = bir iplik" damga varsayımı teoride yok, ilan ediliyor — $\eta_d$ ile aynı türden sayılamamış oran; (iii) **faz varsayımı tek taşıyıcı halka**: $Z$ damganın düzgün iç içe geçmesi ($\phi_j=2\pi j/Z$). Fazlar **kilitliyse** damgalar çakışır, $s$ $Z$'den bağımsız olur, He⁺ yine 121,5 nm (4,00 kat yanlış) — ve kilitlilik 2.1'in kendi çekirdek tasviriyle ("Zerrelerin birbiri etrafında kilitlenmesi") **desteklenir**; (iv) hakemin **152 kat** itirazı ortadan kalkmıyor, bir **doluluk postülatına** dönüşüyor (mesh hücresi başına bir elektron); (v) $\sqrt2c$ burada da tamamen sadeleşiyor ($s=2\pi r_p/Z$) — M-3 senkronizasyon argümanı verir, **sayı vermez**.
**Devinim alt-yolu ayrıca elendi:** $s=r_{nuc}/\varepsilon$; He'nin L2 katmanı ince disk ($\varepsilon=1/2$) → $s=1{,}68\times10^{-15}$ m, gereken $1{,}66\times10^{-10}$ → **98.956 kat**. İzotop: $s\propto A^{1/3}$ ile Balmer-α 656,460 → 521,03 nm (ölçüm 656,280) → **753 kat**, kısıt ihlali **1217 kat**.
> ⚠️ **YENİ ÖNLEYİCİ YASAK.** Yazarın "küresellik için $\varepsilon\gtrsim1{,}6\times10^{-5}$" eşiği ile $r_1=a_0$ koşulunun gerektirdiği $\varepsilon$ **ÖZDEŞTİR** ($1{,}587370\times10^{-5}=1{,}587370\times10^{-5}$, bağımsız doğrulandı). Yani o eşik bir teyit **değil**, kalibrasyonun geri okunmasıdır. **§10.5.7'nin beşinci örneği olarak kayda geçer.** Ayrıca hükmün 2π konvansiyonuyla **işaret değiştirmesi** ($5{,}05\times10^{-6}$ tabanın altında, $3{,}17\times10^{-5}$ iki katı üstünde) tek başına o hükmün kanıt olamayacağını gösterir.

### B-rezonans — halka frekansı $\leftrightarrow$ çekirdek devinim frekansı kilidi
$r(Z)=r_{nuc}(A)/(m\,\varepsilon)$. $\varepsilon$ sabit alınırsa $r\propto A^{1/3}\approx(2Z)^{1/3}$ → **$p=+1/3$, İŞARET TERS.** He⁺ için $r_1=2{,}268\,a_0$ (gözlem $0{,}5\,a_0$), Ly-α 137,8 nm (gözlem 30,378). $p=-1$ için $\varepsilon\propto Z A^{1/3}$ elle konmak zorunda ve dört gözlem reddediyor: ölçülen $\beta_2$ ($Z{:}62\to82$'de gereken 1,46 kat **artış**, gözlenen $\ge$68 kat **düşüş**) · $\varepsilon\equiv0$ olan spin-0 çekirdeklerde ($^4$He, $^{12}$C, $^{16}$O) tanımsız ve $r=\infty$ verir — **oysa en temiz $Z$ ölçeklemesi tam bu sistemlerde ölçülüyor** · izotop kaymasını **948 kat** aşırı öngörüyor.
**İtiraf edilmemiş üç varsayım:** (G1) **teorinin kendi devinimi konik değil DOĞRUSALDIR** (Postülat 5: *"eksen — koni değil, doğrusal — salınır"*); yol rijit gövde konik presesyonunu ithal etti, yani teorinin kendi metniyle çelişik. (G2) M-3 çekirdeğin **bütününe** uygulandı; çekirdek tek zarf değil, alt alta kare katman yığınıdır ve Ek C satır 8 tek proton için bile $\sqrt2c$ ile ~%18 açık bırakıyor. (G3) Tüm $Z$ bağımlılığı $\varepsilon$'a yüklendi; $m$'ye de yüklenebilirdi (tamsayılık duvarına çarpar) — tercih mekanizmadan değil, hangi kanalın daha az açık çökeceğine bakılarak yapıldı.
**Beşinci ihlal sınıfı (Madde 21):** $\varepsilon\propto ZA^{1/3}$ tek parametre değil **iki değişkenli fonksiyondur** ve iki bağımsız işi birden yapmak zorundadır. Madde 21 tek sayılar için yazılmıştır; **bir fonksiyon ilan edilemez, o bir arama tablosudur.**

### C-kuyu — Seçici Lemması ile kalıcı kapalı (§13.2 T-A). $p=0$ tam.
> ⚠️ İki önleyici kayıt: (i) **İzinli kümeyi inceltmek yasaklanmalıdır** — $\mathcal{A}=\{Ns/2\pi\},\,N\in\mathbb{N}$ kümesini serbestleştirmek Lemmayı atlatmaz, yalnız gizler. (ii) $P_{amb}(Z)=Z^2P_{amb}(1)$ hipotezindeki **2 üssü türetilmemiş, hedeften geri hesaplanmıştır** ($r\propto1/Z$ isteniyor → $v_w\propto Z$ → $P\propto Z^2$). Üs serbest bırakıldığında yalnız $m=2$ gözlemi verir ve gerekçesi "gözlem böyle istiyor"dur. Reddedildi; **bir daha "kapatıcı hipotez" diye diriltilmesin.**
> 🟢 **Doğru davranış kaydı:** bu yol $L=\hbar$ kolunun $r=5{,}29195\times10^{-11}$ m (yani $a_0$'ı 1,000034 doğrulukla) verdiğini **fark etti, kaydetti ve §10.3 gereği açıkça reddetti**, hiçbir sonucun dayanağı yapmadı. Örnek alınacak davranış.

### D-lambda — M-42'nin $\Lambda$ kanalı
$r_k(Z)=k^2a_0(1-Z\alpha^2)$, yani potansiyelde **doğrusal, hiperbolik değil**. $p_{etkin}=-Z\alpha^2/(1-Z\alpha^2)$: $Z{=}2$'de $-1{,}065\times10^{-4}$ (gereken $-1$ → **9.389 kat**), $Z{=}92$'de $-4{,}95\times10^{-3}$ (202 kat) — ve sabit bile değil. Kütle-itim kanalıyla $p_{etkin}=-2{,}35\times10^{-44}$ (**44 mertebe**); $\Phi/c^2=2{,}347\times10^{-44}$ iki yoldan doğrulandı.
**İki yapısal ihlal:** (1) $m_e$ girdi kümesine giriyor → 9.11.10'un üçe-üç paritesi **dörde-üçe** bozuluyor; tek başına reddetmeye yeter. (2) **M-42 Kısıt 3 ihlali (yeni bulgu):** $\Lambda$'yı $m_e$ ile yazmak onu **prob-bağımlı** yapar — aynı noktada elektron-probu $\varepsilon=5{,}3251\times10^{-5}$, proton-probu $2{,}9002\times10^{-8}$. $\Lambda$ "yerin" ölçeğidir; probun ölçeği olursa $c_{loc}/(\ell_{loc}f_{loc})=1$ kontrolü çöker → optik saat sınırını **$5{,}3\times10^{13}$ kat** ihlal. İkilem kapalıdır: $\Lambda$ prob-bağımsız kalırsa $m_e$ giremez; prob-bağımlı olursa artık M-42'nin $\Lambda$'sı değildir ve üç üssün kalibrasyonu (bükülme 1,751″, kızıla kayma, Lorentz null) düşer.
> ⚠️ $\varepsilon=k_e/(a_0m_ec^2)=\alpha^2$ **tam özdeşliktir** ($1{,}9\times10^{-13}$'te doğrulandı) — yani $a_0=\hbar/m_ec\alpha$'nın geri okunması, **§12.6'daki $\eta_d=\alpha/2\sqrt2$ hatasının birebir aynısı.** Bu yol bağlaşım ayarlanarak kurtarılmaya çalışılırsa **§4.3 doğrudan ihlal edilir.**

### E-kaynak — $Z$ proton $=Z$ kaynak
Türetilen: $s(Z)=s_0/\sqrt Z \Rightarrow p=1/2$ (3B hacim→yüzey→çizgi okumasıyla $1/3$; kaynak şiddeti okumasıyla **işaret bile ters**, $+1/2$).
**🔴 KIRILMANIN GERÇEK YERİ — ve bu, "1/2'yi 1'e yükseltelim" denemesini de kapatır:** $Z$ nokta kaynak $R$ yarıçaplı bölgede kümelenmişse, $r\gg R$'de separatriks yüzeyleri asimptotik olarak **kümeden geçen KONİLERDİR**; hücre sınırları **sabit açıdadır**. Yani bu yol hiçbir yarıçap üretmiyor — T-B teoreminin somut örneği. *(Aday "$p=1/2$ verdim, $1$ gerekiyor" dedi; bu teşhis eksik ve tehlikeliydi — birinin "aradaki farkı kapatan mekanizma bulalım" diye aynı sokağa girmesine davetiyeydi.)*
> Kayıt: $p=1$ **elle** konulursa cebir sekiz H-benzeri iyonda $10^{-4}$ içinde kapanıyor (He⁺ 30,377 vs 30,378 nm; C⁵⁺ 3,3752 vs 3,3746; Fe²⁵⁺ 0,17974 vs 0,17845). **Bu uyum kanıt değildir** (§10.5.7) — üs türetilmemiştir. Ve $Z_{eff}=Z-N_{iç}$ "türetilmiş, sıfır serbest parametre" ibaresi düzeltilmelidir: tablo 7/13 girdide tutarsız, salınım yalnız türetilmemiş gerçek periyot uzunluklarıyla çıkıyor, ve diverjans teoreminin sadeleşmesi $|q_{elektron}|=q_n$ eşitliğini şart koşuyor — teorinin tek kaynak-şiddeti formülü kütleye bağlı olduğu için bunu **vermiyor** (naif karşılık $9{,}83\times10^3$ kat sapıyor). Nötr atomlarda tam perdeleme Li→Cs iyonlaşmasını 9,00 kat düşürüyor, gözlem 1,385 kat.

## 13.5 Örgünün net kapsamı — ne yapar, ne yapamaz
| Örgünün işi | Durum | Gerekçe |
|---|---|---|
| $l$ alt-durumları, 2s=2p yozlaşması | ✅ **ayakta** | aynı yarıçapta farklı modlar; frekans yasası gerektirmiyor. **Denetimin en sert bulgusunu (C-12) kapatır** |
| Küresel simetri (dinamik sonuç) | ✅ **ayakta** | rijit halka + devinen yönelim küreyi süpürür |
| Katmanların eşdüzlemsizliği → iç içe küreler | ✅ **ayakta** | — |
| Kapı → seçim kuralları + Kirchhoff mekanizması | ✅ **ayakta** | konumlar kapıdan, hızlar yönden (9.11.8 ile uyumlu) |
| **Yarıçapı belirlemek** | ❌ | **T-B**: açı üretir, uzunluk üretmez |
| **Frekansı belirlemek** | ❌ | rijit desen → tek $\omega$ → **vuru = 0**; ayrıca §9.1 zaten elemiş |

**Yapısal okuma:** Örgü bir **açısal/topolojik** yapıdır, metrik bir yapı değil. *Kabuğun neresinde* ve *hangi geçişler* sorularını yanıtlar; *kabuk ne kadar büyük* ve *hangi frekansta* sorularını yanıtlamaz. Standart çatının açısal kısmına (küresel harmonikler, seçim kuralları) karşılık gelir; **radyal kısım teorinin açık borcudur.**

## 13.6 Yayına ne yazılacak
| Dosya | Değişiklik |
|---|---|
| **9.11.6** | "Rydberg biçimi türetilmiştir" iddiası **geri çekilecek.** Dürüst hâli: biçim **$\Omega\propto1/r$ posit edilirse** çıkar; posit M-3'ten lisanslanmıyor ve teorinin kendi alan yasasıyla (Kepler, Ek A.4) **gerilim hâlinde.** $\sqrt2c$'nin sadeleştiği (§13.3-d) açıkça yazılacak |
| **9.11.7** | "2s=2p bağımsız teyit" kutusu **örgü moduna** çevrilecek (yoksunluk değil) |
| **9.11.4** | Nedensellik ters çevrilecek (örgü birincil); minimizasyon argümanı ve "kapasite positi" kalkacak; **T-B teoremi** kaydedilecek |
| **9.11.11** | **Beşinci kalem:** ince yapı · Lamb · aşırı ince · seçim kuralları — kapı mekanizması adlandırıldı, bastırma çarpanları türetilmedi (nicel hedefler: 2s→1s $10^{-8}$, [O III] $10^{-10}$, 21 cm $10^{-24}$). **Kalem ② randevudan çıkarılacak** |
| **7.4 / 7.5** | Kalem ② → **7.5 yanlışlanma koşulu** (beş yol + bir teorem; "hesabı yapılmadı" savunulamaz). $\Omega\propto1/r$ için **yeni kalem** açılacak |
| **§12.3 / §12.5** | §12.3'ün imza iddiası **yürürlükten kalktı** (§13.3.1) |
| **Ek C** | $\eta_d$ satırı hâlâ yok (denetim K-1) — açılacak |

## 13.7 ÖRGÜ ANLATISI — mekanizma zinciri (yayına 9.11.3-b olarak taşındı)

Bu, örgünün **ayakta kalan** içeriğinin tam zinciri. Yazarın üç düzeltmesi (§13.1) bu biçimde birleşti.

**(1) Çekirdek tek zarf değil, kaynak yığınıdır.** Kare katmanlar alt alta, her biri kendi düzleminde (radon: L2·L8·L18·L32·L18·L8). Her proton Kaynak: içinde vakum cebi, çeperinde Evrenakı Rampası, akışkanı dışa pompalıyor (Madde 25). ⟹ akış alanı **doğuştan küresel-simetrik değil.**

**(2) Döner + yalpalar; yalpalama DOĞRUSAL.** Devinim zorunlu (Ö-5: kuark yapılı proton ideal küre olamaz). **Düzeltme kaydı:** Postülat 5 *"eksen — koni değil, doğrusal — salınır"* diyor. B yolu klasik konik presesyonu ithal etmişti ve bu teorinin kendi metniyle çelişikti (workflow bulgusu G1). Örgüyü dokuyan hareket **iki dik düzlemde bileşik salınım**, koni taraması değil.

**(3) Belirlenimli hareket → duran desen.** Sırt-ve-oluk yapısının yönelimi kapalı bir figür boyunca çevrim yapar; figürün basınç alanına yazılmış hâli örgü. Elektron Kuyu olduğu için oluğa oturur, sırta oturamaz. İzler işgalciden bağımsız var.

**(4) Kesiklilik = KAPANMA.** Desen ancak çekirdek başlangıç duruşuna dönerse durur ⟹ tamsayı koşulu. **Teorinin kuantumlaması budur** ve $L=n\hbar$'ın yerini alır. *Ve tam bu yüzden T-B kaçınılmazdır: açısal kapanma kesiklilik üretir, uzunluk üretmez. Yarıçap borcu bir hesap eksiği değil, kapanma mekanizmasının yapısal bedelidir.*

**(5) Küresellik = rijit halka + devinen yönelim.** Halka bütün olarak korunur (bozulursa $r\propto\sqrt N$, merdiven ölür). $\Omega_p=5{,}05\times10^{23}$ rad/s, ilk kabuğun dolanımı 15 mertebe altı ⟹ elektron bir tur atmadan yönelim taranmış. Katmanların eşdüzlemsizliği → **iç içe küreler**; yığılmış diskler resmi terk edildi.

**(6) Kapı.** Desen sabit ⟹ geçitler sabit ⟹ giren çıkabilen. Kirchhoff'un mekaniği. **Süzgeç, veto değil** (2s→1s $10^{-8}$, [O III] $10^{-10}$, 21 cm $10^{-24}$ — bastırılmış ama sıfır değil). 9.11.8 ile uyumlu: konumlar kapıdan, hızlar yönden.

### 13.7.1 SIRADAKİ İŞ — kapanma sayımı, açıkça kurulmuş problem
| | |
|---|---|
| **Girdi** | kaynak dizilimi ($k$'ıncı katmanda $(2k)^2$ konumun yarısı proton) · dönüş fazı · doğrusal salınım fazı |
| **Koşul** | iz deseni kapanır |
| **Çıktı** | duran açısal desenlerin ayrık kümesi + **katlılıkları** |
| **Hedef** | gnomon dizisi $1,3,5,\dots,2k-1$; toplam $2k^2$ (k=1..4 → 2,8,18,32) |

> ⚠️ **GNOMON YASAĞI — beşinci önleyici yasak.** $k^2=\sum_l(2l+1)$ bir **aritmetik özdeşliktir**; "bizim $k^2$ onların $n^2$ gibi ayrışıyor" demek iki tarafın aynı sayıyı yazması demektir ve **kanıt değildir** (§10.5.7 ailesi). Tablo bir **hedef**tir, sonuç değil. Kanıt olacak olan: kapanma koşulu bağımsız çözüldüğünde mod ailelerinin gerçekten gnomon çıkması **ve sıralamanın** (neden s→p→d) türetilmesi. Hedefin yazılı olması hesabın yapıldığı anlamına gelmez.

### 13.7.2 Kapanma sayımına bağlı borçlar (9.11.11 md. ④–⑤ olarak yayına geçti)
- Mod sayımı ve katlılıklar — çözülmedi
- Alt kabuk **sıralaması** (s, sonra p) — türetilmedi
- **Seçim kuralları** $\Delta l=\pm1$ — kapı adlandırıldı, geometrisi kurulmadı
- **İnce yapı · Lamb · aşırı ince** — hiçbiri açıklanmış sayılmaz
- **"2" çarpanı:** bu resimde ızgaranın yarılanmasından, spinden değil. Ama **Stern–Gerlach spini doğrudan ölçüyor** (gümüş demeti ikiye ayrılıyor). Manyetizma havaleli (1.1.3) ama **havale bu borcu kapatmaz** — demetin ikiye ayrılmasının geometrik karşılığı gösterilmeli.

### 13.7.3 Yayına taşındı
| Dosya | Ne |
|---|---|
| `Kisim_9/11_Atom_Spektrumlari...md` | **§9.11.3-b "Örgü: yörünge deseni nasıl doğar"** eklendi (9.11.3 ile 9.11.4 arasına); T-B teoremi kutuya alındı; kapsam tablosu; gnomon hedefi uyarı kutusuyla; iki borç adlandırıldı |
| aynı dosya | 9.11.11'e **md. ④ (mod sayımı)** ve **md. ⑤ ("2" çarpanı / Stern–Gerlach)** eklendi; eski ④ → ⑥ |
| `Kisim_1/06_Evrenaki_Terminolojisi.md` | **Örgü** maddesi eklendi (kapsam sınırı teoremiyle birlikte) |

> **Kalan iş — yazar kararı bekliyor:** §13.6'nın listesi henüz uygulanmadı. Özellikle **9.11.6'nın "Rydberg biçimi türetilmiştir" iddiası** hâlâ metinde duruyor ve §13.3 onu çürüttü; 9.11.3-b'nin kapsam tablosu ("örgü frekansı vermez") bu iddiayla **görünür gerilim** hâlinde. Bu, bilinçli olarak görünür bırakılmıştır — gizlenmesi daha kötü olurdu.
