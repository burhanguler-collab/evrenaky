# 11.2 Küresel Basıklık ve Jeoit Formu

Dönen bir gök cismi neden küre değildir? Standart hidrostatik model bunu iki terimli bir dengeye bağlar: kütleçekimi içe çeker, merkezkaç ekvatorda dışa iter, yüzey bu ikisinin ortak eşpotansiyeline oturur. Evrenakı'da denge aynı sayıda terimden oluşmaz ve terimlerin hiçbiri "çekim" değildir. Bu bölüm, basıklığın teorideki mekanik zeminini kurar ve teorinin kendi formülasyonunun — **izobar okumasının** — gözlemi hangi hassasiyetle yeniden ürettiğini gövde gövde sınar.

> **Gözlemsel Hedef.** Standart fiziğin "sanal" merkezkaç kuvvetiyle modellediği gezegen ve yıldız basıklığını, Evrenakı'nın gerçek ortam ataleti (M-22) ile yeniden üretmek; figürü iç yapı modeline (λ) muhtaç yaklaşım formülleriyle değil, **ölçülen basınç alanının izobarından** okumak. Ulaşılan hassasiyet: Dünya **+%0,014**, Jüpiter **+%0,08**, Satürn **−%0,09** — ve Satürn'de bağıntının tersine çevrilmesiyle, gövdenin bulutlar altında saklı dönme döneminin **10ˢ 33ᵈ 13ˢⁿ** olarak öngörülmesi (Cassini halka sismolojisi: 10ˢ 33ᵈ 38ˢⁿ).

---

## 11.2.1 Gözlem Tabanı

Açıklanacak sayılar şunlardır (Dünya referans gövdedir; çok-gövdeli tablo 11.2.6'dadır):

| Nicelik | Dünya | Not |
|---|---|---|
| Basıklık $f=(a-b)/a$ | $3{,}3528\times10^{-3}$ ($1/298{,}257$) | WGS-84 |
| $J_2$ | $1{,}08263\times10^{-3}$ | alanın ölçülen dört-kutup katsayısı |
| $J_4$ | $-1{,}6199\times10^{-6}$ | ayrık kanal (11.2.7) |
| Merkezkaç oranı $q=\omega^2R^3/\mathcal{G}M$ | $3{,}4614\times10^{-3}$ | boyutsuz sürücü |
| Hidrostatik denge fazlası | $\approx\%0{,}42$ | gözlenen $f$, iç-yapı modellerinin üzerinde |

Son satır dikkatle okunmalıdır, çünkü iki ayrı soruyu birbirine karıştırmak bu bölümün tarihsel hatasıydı:

1. **Kaynak sorusu** — gövdenin içi $J_2$'yi hangi değerde üretir? Bu, iç yoğunluk dağılımının işidir; Dünya'nın manto anomalileri ölçülen $J_2$'yi hidrostatik iç-yapı modellerinin ~%1 üzerine çıkarır. %0,42'lik "fazla" burada, **kaynak yanında** yaşar.
2. **Denge sorusu** — yüzey, *fiilen ölçülen* alanın izobarına oturuyor mu? Bu, teorinin denge yasasının (M-22) işidir ve iç yapıdan bağımsız sınanabilir.

Bu bölümün ana sınavı ikinci sorudur. Ölçülen $J_2$ kaynak anomalilerini zaten içinde taşıdığından, izobar sınavı %0,42'lik kalemi otomatik soğurur: Dünya'da denge yasası **+%0,014** hassasiyetle tutar (11.2.6). Kaynak sorusunun teoriye düşen payı ise ayrık $J_4$ kanalındadır (11.2.7).

---

## 11.2.2 Terim Envanteri

Basıklık masasında dört Evrenakı öğesi vardır. Karıştırılmamaları için kaynakları ve nesneleri ayrı yazılır:

| Öğe | Katalog | Nesnesi | Yönü |
|---|---|---|---|
| **F1** — radyal kütle-itim | M-2 | gövde maddesi ($\rho_n$) | içe, küresel |
| **Merkezkaç gereksinimi** | — | gövde maddesi ($\rho_n$) | dışa, $\propto\omega^2R$ |
| **F4** — eksenel itim | M-38 | gövde maddesi | dönme eksenine doğru, $\propto1/R$ |
| **F5** — yanal itim | M-39 | gövde maddesi | ekvator düzlemine doğru, $\propto\sin2\theta$ |
| **M-22** — ortamın siklostrofik dengesi | M-22 / DY-1 | **ortam** ($\rho_0$) | denge yasası — kuvvet değil |

Son satır ayrı bir türdendir ve toplanmaz. **M-22 bir kuvvet değildir**; F1'in kurduğu $\nabla P$'nin ortamın dolaşımıyla dengede olduğunu söyleyen bir koşuldur (DY-1). Basıklık hesabına girişi **iki** ayrı yoldandır ve karıştırılmamalıdır: figüre **U2 uygulaması** ile girer (kafese bağlı gövde maddesinin dönme ataleti — 11.2.6), disk/halka toplanmasına ise **U1 + R2** ile (ortamın kendi dolaşımı — 11.2.5).

**F4 ve F5 aynı olaydan doğar.** İkisi de gövdenin dönüşünden, tek bir mekanizmayla çıkar: ekvator kuşağının Evrenakı'yı düzlem boyunca dışa **deplase etmesi** (M-38, Varsayım 1). Deplasman **yerel bir öteleme** olayıdır: kafes, bulunduğu noktadaki ortamın $\phi=1-1/n^2$ kesrini kendi malzemesinin hızıyla taşır (M-16'nın Fizeau kanalı). Ortamın **küresel** bir açısal hıza girmesini gerektirmez — bu yüzden dönme patinajıyla ($\xi$, ayrı kanal) çelişmez. Akı silindir yanağından geçtiğinde **F4**, yüzey basıncının enleme bağlı profilinden **F5** doğar.

---

## 11.2.3 Geometri ve Ortak Tanımlar

1. **Koordinatlar.** Küresel koordinatlarda $R=r\cos\theta$ (dönme eksenine uzaklık) ve $z=r\sin\theta$ (ekvator düzlemine uzaklık); $\theta$ ekvatordan ölçülen enlemdir. Ekvator $\theta=0$, kutup $\theta=90°$.
2. **İki yoğunluk.** Aynı $\nabla P$ ortama $\rho_0$, maddeye $\rho_n$ ile etki eder; M-8'in $k=0$ hâliyle $\rho_n=4\rho_0$ (M-2 ↔ M-22 ayrımı). Figür hesabı **madde** hesabıdır; dolayısıyla $\rho_n$ ile yürür.
3. **Deplasman kapanışı.** Akışın bıraktığı basınç açığı kinetik ölçeklemeyle yazılır: $\Delta P(\theta)=-\kappa_5\,(\phi\rho_0)\,v(\theta)^2$ — yalnız deplase edilen $\phi$ kesri taşındığı için genlik $\phi$ ile **doğrusaldır** ($p=1$; M-39 Varsayım 4'ün iki-fazlı türetimi). İdeal akış $\kappa_5=\tfrac12$ verir, fakat Dünya basıklığı $\kappa_5\lesssim0{,}014$–$0{,}017$ dayatır (bant, $\phi$'nin ~%10'luk hacim-kesri sistematiğinden).
4. **$\phi$ hacim kesridir, optik nicelik değil.** Blok D'nin tanımı bağlayıcıdır: $\phi$, bağlı yapının kapladığı **hacim kesri**; $1/n^2=1-\phi$ ise onun şeffaf ortamdaki **ölçüm yolu** (M-15'te $\phi$ girdi, $n$ çıktıdır). Metallerde ($n$ karmaşık) ve iyonize plazmada ($n<1$ ya da sanal) ters okuma çöker; hacim kesri tanımlı kalır.

---

## 11.2.4 F5'in Yapısı: $\sin2\theta$ Yasası

Bu türetim **hızdan bağımsızdır**: yüzeydeki teğetsel akış hızının ekvatoral değeri $v_{eq}$ ne olursa olsun, enlem profili $v(\theta)=v_{eq}\cos\theta$ olduğu sürece yapı aynı çıkar. (Hangi $v_{eq}$'nun doğru olduğu ayrı bir sorudur — 11.2.5.)

Yüzey basınç profili:
$$P(\theta) = P_{kutup} - \kappa_5\,\rho\,v_{eq}^2\cos^2\theta$$

Açısal gradyan ($\nabla_\theta P=\tfrac1r\,dP/d\theta$) alınır; $\tfrac{d}{d\theta}(\cos^2\theta)=-\sin2\theta$ olduğundan:

$$\frac{dP}{d\theta} = \kappa_5\rho v_{eq}^2\sin2\theta$$

Birim hacme düşen kuvvet $f=-\nabla P$ ile:

$$\boxed{\;f_{yanal}(\theta) = -\frac{\kappa_5\,\rho\,v_{eq}^{2}}{r}\,\sin 2\theta\qquad [\mathrm{N/m^3}]\;}$$

Eksi işareti ($-\hat\theta$), kuvvetin her iki yarımküreden de **ekvatora doğru** olduğunu gösterir.

**Kararlılık deseni.** $|f|\propto\sin2\theta$ olduğundan:

| Enlem | Kuvvet | Denge |
|---|---|---|
| Ekvator ($\theta=0°$) | sıfır | **kararlı** — sapan madde geri itilir |
| Orta enlem ($\theta=45°$) | maksimum | ezme zirvesi |
| Kutup ($\theta=90°$) | sıfır | **kararsız** — madde barınamaz, ekvatora savrulur |

Ekvator, yanal itim alanının tek kararlı çekim noktasıdır. Halka sistemlerinin ve galaktik disklerin jilet inceliğinde ekvator düzleminde toplanması bu desene bağlanır (11.4, M-27); yörünge eş-düzlemliliği de aynı kaynaktan gelir.

> **Dikkat — düzlemde tutmak ile şişirmek aynı şey değildir.** F5 meridyenel bir **geri çağırıcı** kuvvettir ve tam da basıklığın kurulacağı yerde, ekvatorda, **sıfırdır**. Yörüngeleri ve halkaları düzlemde tutması bu yüzden güçlüdür; gövdeyi şişirmeye katkısı ise ayrı ve çok daha zayıf bir sorudur (11.2.7).

---

## 11.2.5 Hız Kaynağı: Üç Aday, Bir Doğru Cevap

11.2.4 yapıyı verir ama $v_{eq}$'yu vermez. Basıklığın niceliği tamamen bu tek sayıya bağlıdır ($f_{yanal}\propto v_{eq}^2$) ve teoride **üç aday** vardır. Üçü de farklı nesnelerdir, farklı kanallara aittir ve mertebeleri arasında uçurumlar bulunur:

| Aday | Kaynak | $v_{eq}$ (Dünya yüzeyi) |
|---|---|---|
| **(A) Madde ekvator kuşağı** — $v_{eq}=\omega_{gövde}R$ | gövdenin kendi malzemesinin katı-cisim dönüşü (M-38/M-39 **R1**) | $465$ m/s |
| **(B) Ortam ekvator düzlemi** — $v_{eq}=v_\theta=2\sqrt{\mathcal{G}M/R}$ | ortamın kendi dolaşımı (M-22 / M-38-M-39 **R2**) | $1{,}58\times10^{4}$ m/s |
| *(C) Dönme entrainment'ı* — $v_{eq}=\xi\,\omega R$ | dıştaki alan kuplajı (M-40) | $2{,}1\times10^{-7}$ m/s |

**Aday (A) figürün doğru kaynağıdır.** Gövdenin malzemesi katı cisim olarak döner, dolayısıyla $v(\theta)=\omega_{gövde}R\cos\theta$ **tam** geçerlidir — 11.2.4'ün istediği profil hiçbir varsayım gerektirmeden buradan gelir. Atama zorunludur: gözlenen $J_2$/$J_4$ **dönme eksenine** kilitlidir, oysa ortamın dolaşım ekseni Dünya'da $23{,}44°$ eğiklikle ondan ayrılır — kaynak (B) olsaydı imza yanlış eksende çıkardı.

**Aday (B) gövde figürüne değil, disk toplanmasına aittir** (R2): galaktik disklerin ve halka sistemlerinin ekvator düzleminde jilet inceliğinde toplanması bu rejimin işidir ve hiçbir kavrama kesri içermez. Yüzeyde $15{,}8$ km/s'lik dolaşım gerçektir, ama figürün simetri eksenini o belirlemez.

**Aday (C) elenmiştir** — ve zaten hiçbir zaman aday değildi: $\xi$ **dıştaki alan** kanalıdır, yüzey deplasmanı değil.


> **Korunan sonuç — cisimden bağımsızlık.** Aday (A) ile $v_{eq}\propto\omega R$ olduğundan, ivmeye geçildiğinde ($a=-\rho_n^{-1}\nabla P$) $\omega^2R^2$ ile merkezkaçın $\omega^2R$'si sadeleşir:
> $$\frac{a_{yanal}}{a_{merkezkaç}} = \kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi\cdot 2\sin\theta \qquad (p=1)$$
> Oran gövdenin boyutundan ve dönüş hızından **bağımsızdır**; yalnız kompozisyon çarpanına ($\phi$, hacim kesri) bağlıdır. Buradan çıkan kazanç korunur: klasik mekanikte $\omega$ arttıkça merkezkaç/itim oranı büyür ve bir yerde 1'i aşar — sert bir kopma tavanı vardır. Burada oran $\omega$ ile büyümediği için **bir hızda kararlı olan cisim her hızda kararlıdır**; tavan kalkmaz ama kompozisyona bağlı sabit bir çarpanla yükselir. Sadeleşme yalnızca $v_{eq}\propto\omega R$ olmasından geldiği için $\phi$'nin üssünden **etkilenmez.**

---

## 11.2.6 Figür Denklemi — M-22'nin İki Uygulaması ve İzobar Okuması

M-22 tek bir denge yasasıdır ($dP/dr=\rho v_\theta^2/r$) ama **iki ayrı nesneye** uygulanır. Karıştırılırlarsa figür hesabına yanlış bir 2 çarpanı girer.

### (U1) Serbest madde — DY-1 rejimi

Yalnız $\nabla P$ ile tutulan madde. Tek gradyan, iki yoğunluk:

$$\frac{dP}{dr}=\rho_0\frac{v_\theta^2}{r}\ \ \text{(ortam)}\,,\qquad\qquad \frac{dP}{dr}=\rho_n\frac{v_{madde}^2}{r}\ \ \text{(madde)}$$

Sol taraflar aynı olduğundan $\rho_0v_\theta^2=\rho_nv_{madde}^2$; M-8'in $\rho_n=4\rho_0$ ($k=0$) sonucuyla

$$v_\theta=\sqrt{\rho_n/\rho_0}\;v_{madde}=2\,v_{madde}$$

2 çarpanı **serbest düşme dengesinden** gelir.

### (U2) Kafese bağlı gövde maddesi — figür rejimi

Gövdenin malzemesi $\nabla P$ ile değil **kafes rijitliğiyle** tutulur. Testi doğrudandır: serbest düşme dengesindeki madde yüzey hızı yörünge hızına eşit olurdu.

| | $\omega R$ | $\sqrt{\mathcal{G}M/R}$ | oran |
|---|---|---|---|
| Dünya | 465 m/s | 7.905 m/s | **0,059** |
| Jüpiter | 12.572 m/s | 42.096 m/s | **0,299** |
| Satürn | 9.871 m/s | 25.087 m/s | **0,394** |
| Güneş | 1.993 m/s | 436.762 m/s | **0,005** |

Hiçbiri 1'e yakın değil: **hiçbir gövdenin yüzey maddesi DY-1 rejiminde değildir.** Figür hesabında $v_\theta=2\,\omega R$ yazmak bu nedenle hatadır — U1'in 2 çarpanı U2'ye **taşınmaz.**

U2'de M-22 hızı kapatan bir bağıntı değil, dışarıdan verilen $\omega$ karşısında basınç alanının uymak zorunda olduğu **koşuldur.** Figür, bu koşulun eşpotansiyel yüzeyidir:

$$U(r,\theta)\;=\;-\frac{\mathcal{G}M}{r}\;-\;\tfrac12\,\omega^2r^2\cos^2\theta\;+\;U_4(r,\theta)+U_5(r,\theta)\;=\;\text{sabit}$$

İlk terim F1'in itim potansiyeli; ikincisi kafese bağlı maddenin **gerçek** dönme ataletidir (M-22'nin *"merkezkaç sanal değildir"* kaydı); son ikisi F4 ve F5'in paylarıdır (F5 merkezkaça soğurulur, F4'ün ayrık payı $J_4$ kanalındadır — 11.2.7).

Bu koşulu sayıya dökmenin **iki yolu** vardır ve ikisi aynı statüde değildir.

### Yol 1 — İç yapı yolu (Darwin–Radau): ithal yaklaşım, denetim görevlisi

Alan bilinmiyorsa, $J_2$'yi iç yoğunluk dağılımından tahmin etmek gerekir. Klasik araç, eylemsizlik çarpanı $\lambda=I/MR^2$ üzerinden Darwin–Radau interpolasyonudur:

$$\frac{f}{q}=\frac{5}{2\left[1+\tfrac{25}{4}\left(1-\tfrac32\lambda\right)^{2}\right]}$$

Dünya için ($q=3{,}4614\times10^{-3}$, $\lambda=0{,}3307$) $f=3{,}3446\times10^{-3}$ verir — gözlemin %0,2 altı. İyi bir ilk adımdır, fakat üç yapısal kusuru vardır:

1. **Yaklaşımdır** ve nokta-kütle limitini tutmaz: $\lambda\to0$'da $f/q\to0{,}3448$ verir, kesin değer $0{,}5000$'dir — **−%31**. Geçerlilik penceresi $\lambda\gtrsim0{,}2$'dir; yıldızlarda ($\lambda\lesssim0{,}1$) kullanılamaz.
2. **λ'yı girdi ister** — ve λ yalnız Dünya, Mars, Ay gibi gövdelerde bağımsız ölçülür (presesyon). Gaz devlerinde λ, kütle-itim alanı verisine ayarlanmış iç modellerden gelir: DR'yi orada "öngörü" saymak **dolaşık akıl yürütmedir.**
3. Teorinin diline yabancıdır: figürü kaynak modeline bağlar, oysa teoride figür **alanın** izobarıdır.

Bu üç kusur nedeniyle DR bu bölümde ana yöntemlikten alınmış, çapraz-denetim görevine çekilmiştir.

### Yol 2 — Alan yolu (izobar okuması): teorinin kendi formülasyonu

Teorinin tezi şudur: yüzey, **fiilen ölçülen** basınç alanının izobarıdır. Ve alan gerçekten ölçülmüştür — uydu ve uzay aracı yörüngeleri, teoride tam olarak bu alanın içinde uçar; $J_2$ ve $J_4$, F1 alanının ölçülmüş çok-kutup katsayılarından başka bir şey değildir. İç yapıya dair **hiçbir model varsayımına gerek yoktur**: λ'nın taşıdığı bütün bilgi, ölçülen $J_2$'nin içinde zaten durur.

Alanın dış potansiyeli çok-kutup açılımıyla $V=-\frac{\mathcal{G}M}{r}\bigl[1-J_2(\tfrac ar)^2P_2-J_4(\tfrac ar)^4P_4\bigr]$ yazılır; izobar koşulu $V-\tfrac12\omega^2r^2\cos^2\theta=$ sabit, **kutupta ve ekvatorda** değerlendirilir ($P_2$: ekvator $-\tfrac12$, kutup $1$; $P_4$: ekvator $\tfrac38$, kutup $1$; kutup yarıçapı $b=a(1-f)$, açılım ikinci mertebeye kadar). Sonuç kapalı bir bağıntıdır:

$$\boxed{\;f=\tfrac32 J_2+\tfrac12 q+\underbrace{3J_2\,f-f^2+\tfrac58 J_4}_{\text{ikinci mertebe}}\;}$$

Birinci mertebede $f=\tfrac32J_2+\tfrac12q$; ikinci mertebe terimleri gaz devlerinde %2–6 düzeltme getirir ve $f$'te örtük olduğundan iki-üç yinelemeyle çözülür. Kesme hatası $O(f^3)$'tür: Dünya'da $10^{-8}$ (ihmal), Jüpiter'de ~%0,4, Satürn'de ~%1 tavanındadır — ölçülen $J_4$'ün kullanılması bu payın bir bölümünü de soğurur.

**Bağıntı iki kesin limiti kendiliğinden içerir** — DR'nin tutamadığı sınav budur:

| Limit | $J_2$ değeri | Bağıntının verdiği | Kesin değer |
|---|---|---|---|
| Nokta kütle (yıldız) | $J_2\to0$ | $f=q/2$ | $q/2$ ✓ |
| Homojen gövde (Maclaurin) | $J_2=q/2$ | $f=\tfrac54q$ | $\tfrac54q$ ✓ |

Arada hiçbir interpolasyon varsayımı yoktur; gövdenin nerede durduğunu ölçülen $J_2$ söyler.

### Sekiz gövdede izobar sınavı

Girdilerin tamamı ölçümdür: $a$, $\mathcal{G}M$, $\omega$, $J_2$, $J_4$. Serbest parametre yoktur.

| Gövde | $q$ | $J_2$ | $f_{izobar}$ | $f_{gözlenen}$ | Sapma |
|---|---|---|---|---|---|
| **Dünya** | $3{,}4614\times10^{-3}$ | $1{,}0826\times10^{-3}$ | $3{,}35327\times10^{-3}$ | $3{,}35281\times10^{-3}$ | **+%0,014** |
| **Jüpiter** (Juno) | $8{,}9196\times10^{-2}$ | $1{,}46966\times10^{-2}$ | $6{,}4923\times10^{-2}$ | $6{,}4874\times10^{-2}$ | **+%0,08** |
| **Satürn** (Cassini, sismoloji dönemi) | $1{,}5763\times10^{-1}$ | $1{,}62906\times10^{-2}$ | $9{,}7872\times10^{-2}$ | $9{,}7963\times10^{-2}$ | **−%0,09** |
| **Güneş** (Carrington dönemi) | $2{,}0831\times10^{-5}$ | $2{,}2\times10^{-7}$ | $1{,}0745\times10^{-5}$ | $1{,}100\times10^{-5}$ | **−%2,3** (ölçüm ±%5) |
| Neptün (Voyager) | $2{,}6078\times10^{-2}$ | $3{,}4084\times10^{-3}$ | $1{,}7991\times10^{-2}$ | $1{,}7081\times10^{-2}$ | +%5,3 (gözlem ±%7) |
| Mars | $4{,}5953\times10^{-3}$ | $1{,}9566\times10^{-3}$ | $5{,}2263\times10^{-3}$ | $5{,}888\times10^{-3}$ (yüzey) | −%11,2 → **Tharsis** |
| Uranüs (17,24 sa ile) | $2{,}9535\times10^{-2}$ | $3{,}5107\times10^{-3}$ | $1{,}9828\times10^{-2}$ | $2{,}2927\times10^{-2}$ | −%13,5 → **açık kalem** |
| *(Merkür, Venüs)* | — | — | — | — | figür ekseni devretmiştir (11.2.8) |

Satırlar üç sınıfa ayrılır ve üçü de ayrı bir şey öğretir:

**(a) Denge yasası tutan gövdeler — Dünya, Jüpiter, Satürn, Güneş, Neptün.** İlk üçünde uyum ölçüm hassasiyeti düzeyindedir (binde 1'in altı). Dünya'nın meşhur %0,42'lik "hidrostatik fazlası" tabloda görünmez, çünkü o kalem alanın **kaynağında** yaşar (manto anomalileri ölçülen $J_2$'nin içindedir) ve izobar okuması ölçülen alanı kullandığı için onu otomatik taşır: yüzeyin izobara oturma hassasiyeti +%0,014'tür. Neptün'ün +%5,3'ü gözlem hatasının ($b$ yarıçapında ±30 km → $f$'te ±%7) içindedir; ayrıca 1-bar seviyesini ±400 m/s'lik bölgesel rüzgârlar da biçimlendirir.

**(b) Yüzeyi izobarda olmayan gövde — Mars.** Yüzey figürü öngörünün %12,7 üzerindedir ve bu fark bir teori hatası değil, **ölçülmüş topografyadır**: Tharsis platosu. Mars'ın kabuğu, izobardan bu kadar sapmayı taşıyabilecek kadar rijittir — teorinin diliyle, kafes rijitliği (U2) maddeyi izobara oturmak zorunda bırakmaz; izobar yalnız *akışkan* davranan gövdelerde figürü dikte eder. Mars bu yüzden denge yasasının değil, **kabuk mukavemetinin** sınavıdır ve her iki teoride de aynı kaleme yazılır. (Jeoit — areoid — düzeyinde bağıntı sağlanır; fakat areoid alandan türetildiği için bu bağımsız bir sınav sayılmaz ve tabloya konmaz.)

**(c) Girdisi kusurlu gövde — Uranüs.** −%13,5'lik sapma $f$'e değil, girdiye aittir: 17,24 saatlik dönem Voyager'ın **manyetosfer** ölçümüdür ve manyetosfer dönemlerinin iç dönmeyi temsil etmediği Satürn'de kanıtlanmıştır (aşağıda). Bağıntı tersine çevrilirse Uranüs'ün iç dönme dönemi **15,6–16,0 saat** çıkar ($f$'in ±1σ bandıyla); şekil+rüzgâr modellemeleri de bağımsız olarak ~16,6 saate işaret eder. Sorun her figür teorisinde aynıdır — standart hidrostatik model de 17,24 saat ile aynı %13'ü ıskalar. Uranüs bu bölümün **teoriden bağımsız açık kalemidir**: çözümü yeni bir görevin dönem ölçümündedir, teoride değil.

### Satürn: bağıntının tersine çevrilmesi — saklı dönemin öngörüsü

Satürn'ün iç dönme dönemi doğrudan ölçülemez: gövde bulutlarla kaplıdır, manyetik ekseni dönme eksenine neredeyse tam oturduğu için manyetosfer sinyali de güvenilmez (Voyager 10ˢ 39ᵈ 22ˢⁿ vermişti; Cassini boyunca bu "dönem" %1 kaydı — bir iç dönme ölçüsü olamaz). O hâlde izobar bağıntısındaki üç gözlenirden ($f$, $J_2$, $q$) ikisi ölçülüp üçüncüsü **öngörülebilir**:

$$q=2\Bigl(f-\tfrac32J_2-3J_2f+f^2-\tfrac58J_4\Bigr)\;\Rightarrow\;q=0{,}15784\;\Rightarrow\;P=\frac{2\pi}{\sqrt{q\,\mathcal{G}M/a^3}}=\textbf{10ˢ 33ᵈ 13ˢⁿ}\;(\pm\sim2\text{ dk kesme payı})$$

Bağımsız ölçüm: Cassini, C halkasındaki dalgaların gövdenin iç titreşimlerince sürüldüğünü kullanarak — **halka sismolojisi** — iç dönemi $10ˢ\,33ᵈ\,38ˢⁿ\;(+1ᵈ52ˢⁿ/-1ᵈ19ˢⁿ)$ ölçtü. İki değer **25 saniye** içinde örtüşür; her ikisinin de hata bandı ~2 dakikadır. Eski Voyager dönemi kullanılsaydı $f$ öngörüsü −%1,35 sapardı — tablodaki −%0,09, doğru dönemin doğrulanmasıyla birlikte gelir. Bu, izobar okumasının yalnız figürü *açıklamadığını*, ölçülemeyen bir niceliği *öngörüp bağımsız yöntemle doğrulatabildiğini* gösteren, bölümün en güçlü tek sonucudur.

### Güneş: nokta-kütle ucunun sınavı

Güneş'te $\tfrac32J_2=3{,}3\times10^{-7}$, $f$'in yalnız %3'üdür — kütle merkezde o kadar yoğunlaşmıştır ki gövde, figür açısından nokta-kütle limitine ($f=q/2$) oturur. İzobar okuması, ölçülen $J_2=2{,}2\times10^{-7}$ (helyosismoloji + gezegen efemerisleri) ile $f=1{,}0745\times10^{-5}$ verir; gözlem $1{,}10\times10^{-5}\pm\%5$'tir → sapma **−%2,3, ölçüm hatasının içinde.** Kalan işaretli pay da anlaşılırdır: Güneş diferansiyel döner ve $q$ hangi dönemle kurulacaksa bir bant oluşur — Carrington dönemi (25,38 gün) −%2,3, ekvatoral yüzey dönemi (24,47 gün) +%4,9 verir; **gözlenen değer bandın içindedir.** Güneş bu bölümde açık kalem değildir; tersine, DR'nin giremediği $\lambda=0{,}070$ bölgesinde izobar okumasının çalıştığını gösteren uç sınavdır.

> **Düzeltme kaydı — Güneş'in "%21 sapması" (3 Ağustos 2026).** Bu bölümün bir ara sürümü Güneş'i Darwin–Radau ile hesaplayıp $f=8{,}67\times10^{-6}$ buluyor ve gözlenen $1{,}10\times10^{-5}$'e göre **−%21,2** sapma kaydediyordu; bu, bölümün en büyük uyumsuzluğu olarak yazılmıştı. **Sapma fiziksel değildi:** Güneş'in $\lambda=0{,}070$'i Darwin–Radau'nun geçerlilik penceresinin dışındadır. Nokta-kütle limitiyle ($f=q/2$) sapma −%5,3'e inmişti; ölçülen $J_2$'yi de taşıyan tam izobar okumasıyla **−%2,3**'e iner ve ölçüm hatasının içine girer.

> **Düzeltme kaydı — yöntem değişikliği (3 Ağustos 2026).** Bu bölümün önceki sürümü figürü **Darwin–Radau** ile hesaplıyor, izobar yazımını yalnız nokta-kütle limiti ($f=q/2$) için kullanıyordu. Bu sürümde izobar okuması ikinci mertebeye taşındı ($f=\tfrac32J_2+\tfrac12q+3J_2f-f^2+\tfrac58J_4$) ve ana yöntem yapıldı; DR denetim görevine çekildi. Kazanç tablosu (sapma, önce → sonra): Dünya $-\%0{,}2\to+\%0{,}014$ · Jüpiter $+\%1{,}3\to+\%0{,}08$ · Satürn $+\%0{,}5\to-\%0{,}09$ (ayrıca dönem öngörüsü kazanıldı) · Güneş $-\%21{,}2\to-\%2{,}3$ · Neptün $+\%3{,}5\to+\%5{,}3$ (ikisi de gözlem hatası içinde; DR'nin oradaki λ'sı zaten ölçüm değil, alan verisine ayarlı model çıktısıydı — dolaşıklık giderildi) · Uranüs, DR tablosunda sessizce eksikti — şimdi açık kalem olarak kayıtlıdır. İkinci kazanç kavramsaldır: figür artık iç yapı modelinden değil, teorinin kendi tezine uygun biçimde **ölçülen alanın izobarından** okunur.

---

## 11.2.7 Multipol Muhasebesi: Kim Ayrıştırılabilir?

İzobar sınavı (11.2.6) **kaynağa kördür**: ölçülen $J_2$/$J_4$'ü kim üretmiş olursa olsun — iç yoğunluk, manto anomalisi, F4 — denge yasasını sınar. Kaynakları birbirinden ayırmak ayrı bir muhasebedir ve bir kuvvetin figüre katkı vermesi ile o katkının **ölçüde ayırt edilebilmesi** farklı şeylerdir. Sınav 1'in (6.6.2) multipol ayrıştırması bu ayrımı keskin biçimde koyar:

| Öğe | Ürettiği harmonikler | Ayrık imza? |
|---|---|---|
| Merkezkaç | saf $P_2$ | — (referans) |
| **F5** | **saf $P_2$** | **Yok** — merkezkaçla dejenere |
| **F4** | $P_2,\,P_4,\,P_6$ | **Var** — $J_4$ kanalı |

**F5'in basıklıktaki etkisi ölçüde sıfıra düşer** — ve sebebi genliğinin küçüklüğünden önce **dejenerasyondur**: F5, merkezkaç potansiyelinin sabit bir çarpanla yeniden ölçeklenmesine denktir. Gezegeni farklı bir şekle sokmaz; yalnızca *biraz daha hızlı dönüyormuş gibi* görünmesine yol açar. Dolayısıyla $J_4$ veya $J_6$'da aranacak ayrı bir F5 imzası **yoktur**; katkısı ne olursa olsun fite soğurulur. (İlk tasarım imzayı $J_4$'te arıyordu; gerekçesi "kuvvet profilleri farklı görünüyor" idi ve yanlıştı — farklı kuvvet profili, farklı multipol içeriği demek değildir.)

**Ayrıştırılabilir imzayı taşıyan kuvvet F4'tür.** Merkezkaç $J_4$'e birinci mertebede hiç katkı vermez, F4 verir — boş kanalda zayıf kuvvet görünür hâle gelir. Dünya için indüklenen $J_4$ payı **%4–8** mertebesindedir ve **işareti doğrudur**: gözlenen $J_4$, hidrostatik modellerin verdiğinden daha derindir ve F4 tam o yönde çalışır. Bu, sınav programının olumsuz olmayan ilk sonucudur — "geçilmiş sınav" değil, "teorinin öngörüsü önemli olacak büyüklükte" durumu. Dürüst sınırları (hidrostatik referansın $\sim\%10$ belirsizliği, hidrostatik-olmayan manto katkısı) 6.6.2'dedir. İzobar sınavıyla çatışma yoktur: $J_4$'ün $f$'e girişi $\tfrac58J_4$ terimiyledir ve F4'ün %4–8'lik payı $f$'i ancak $\sim\%0{,}005$ oynatır — 11.2.6'nın tablosu bu ayrıştırmaya duyarsızdır.

> **Bu bölümün başlığı için sonuç.** Basıklığın gözlemsel imzasını taşıyan kuvvet **F5 değil F4'tür.** F5'in rolü figürü şişirmek değil, **düzlemi tanımlamaktır** (11.2.4).

### $J_4$ Öngörüsü — çok-cisimli sınav

F4'ün beslendiği hız, deplasmanı yaratan **bağıl** dönüştür (M-38 R1): $\omega_{gövde}-\Omega_{ortam}$. $\Omega_{ortam}=\xi\,\omega$ ve $\xi\le3\times10^{-7}$ olduğundan

$$F_4\;\propto\;\omega^2(1-\xi)^2=\omega^2\bigl[1-O(10^{-7})\bigr]$$

yani F4, M-22 ile **aynı $\omega$'yı** yedi hane hassasiyetle izler — kafes bu orana ancak $10^{-7}$ düzeyinde girer. F5'te $\omega$ ve $R$'yi sadeleştiren mekanizma burada da işlediğinden (11.2.5'in korunan sonucu) F4'ün merkezkaça oranı **gövdeden bağımsız** bir sabittir. Öngörü bu nedenle $J_4$'ün kendisinde değil, **$J_4/J_2$'de** yazılmalıdır:

$$\boxed{\;\left(\frac{\Delta J_4}{J_2}\right)_{F4}=\text{gövdeden bağımsız sabit}\;}$$

Ayrım önemlidir, çünkü $J_4/J_2$ gövdeden gövdeye **27 kat** değişir:

| | $J_2$ | $J_4$ | $J_4/J_2$ |
|---|---|---|---|
| Dünya | $1{,}083\times10^{-3}$ | $-1{,}620\times10^{-6}$ | $-1{,}50\times10^{-3}$ |
| Jüpiter | $1{,}470\times10^{-2}$ | $-5{,}870\times10^{-4}$ | $-3{,}99\times10^{-2}$ |
| Satürn | $1{,}629\times10^{-2}$ | $-9{,}358\times10^{-4}$ | $-5{,}74\times10^{-2}$ |

Dünya'nın ölçülen payı (%4–8; Kısım 6 §6.6.2) sabiti verir: $\Delta J_4/J_2=6{,}0\times10^{-5}$–$1{,}2\times10^{-4}$. Diğer gövdelere taşındığında:

| Gövde | Öngörülen $\Delta J_4$ | Kendi $J_4$'ünün yüzdesi |
|---|---|---|
| **Jüpiter** (Juno) | $8{,}8\times10^{-7}$–$1{,}8\times10^{-6}$ | **%0,15–0,30** |
| **Satürn** (Cassini) | $9{,}8\times10^{-7}$–$2{,}0\times10^{-6}$ | **%0,10–0,21** |

Yani gaz devlerinde beklenen sapma Dünya'nınkinden **mertebelerce küçüktür**; "her gövdede %4–8" beklentisi yanlış olurdu ve öngörünün doğru biçimi ancak $J_4/J_2$ üzerinden yazıldığında görünür. Ölçüm hassasiyeti buna fazlasıyla yeter (Juno $J_4$'ü $\sim10^{-8}$ düzeyinde verir, yani %0,002) — **sınavın sınırlayıcı belirsizliği ölçüm değil, hidrostatik referans modelidir.**

**Ay tutarlılık kontrolü.** M-38'in gövde rejimi (R1) Ay verisiyle sınırlıdır: $\varepsilon(r_{Ay})<2\times10^{-5}$ ve $\varepsilon\propto r$ ile yüzeyde $\varepsilon(R_\oplus)<3{,}3\times10^{-7}$. $J_4=1{,}62\times10^{-6}$ ve $c_4/c_2=27/50$ ile: F4'ün $P_2$ payı merkezkaça oranla $2{,}5\,\varepsilon/q<2{,}40\times10^{-4}$, buradan $\Delta J_2<2{,}59\times10^{-7}$ ve $\Delta J_4<1{,}40\times10^{-7}$ — yani F4'e $J_4$'ün en çok **%8,65'i** kadar yer vardır; iddia %4–8'dir. **Geçiyor, fakat marj alt uçta 2,2 kat, üst uçta yalnız 1,08 kattır** — sınırın %92'si tüketilir. Ayrıca bu hesap $n=2$ ile $n=4$ için tepki (Love) çarpanlarını **eşit** alır; gerçekçi gövdelerde $k_4<k_2$ olduğundan gerçek marj daha da incedir. Bu, iki bağımsız verinin (Ay apsidal presesyonu ↔ Dünya $J_4$'ü) aynı katsayıyı kıstırdığı gerçek bir sınavdır ve üç sonuçtan biri doğru olmak zorundadır: **(i)** F4'ün payı iddianın alt ucundadır, **(ii)** Ay sınırı fazla muhafazakârdır, ya da **(iii)** ikisi çatışır ve M-38'in genlik ataması ($A_4$, rozet `[A]`) yeniden hesaplanmalıdır.

---

## 11.2.8 Merkür ve Venüs: Figür Ekseninin Devri

Bu iki gövde yukarıdaki tablolardan çıkarılmıştır ve sebebi *"$q$ çok küçük"* değil — **üç katmanlıdır** ve üçü de teorinin kendi mekanizmasından çıkar.

### (i) Kavrama dönüşü yutmuştur

İkisi de M-24'ün **bastırılmış** sınıfındadır: $g_{Merkür}=0{,}98$, $g_{Venüs}=1{,}00$ (Kısım 3 §3.4.4). Girdap rekabeti serbest dönüş ifadesinin neredeyse tamamını soğurmuştur. Zincir buradan zorunlu olarak akar:

$$\text{kavrama}\;\Rightarrow\;\omega\!\downarrow\;\Rightarrow\;q\!\downarrow\;\Rightarrow\;\underbrace{F_4,\,F_5}_{\propto\,\omega^2}\!\downarrow$$

$q_{Merkür}=1{,}01\times10^{-6}$ ve $q_{Venüs}=6{,}1\times10^{-8}$ — Dünya'nın sırasıyla $1/3400$'ü ve $1/57.000$'i. Dönme kaynaklı figür pratikte yoktur, ve onunla birlikte F4/F5 de yoktur.

### (ii) Figürü belirleyen alan gelgit eksenine devreder

Dönme terimi çöktüğünde geriye Güneş'in **diferansiyel sıkıştırması** kalır (§11.1; teoride gelgit bir çekim değil, basınç alanının ikinci türevidir). Boyutsuz gelgit sürücüsü $t=(M_\odot/M)(R/a)^3$:

| | $q$ (dönme ekseni) | $t$ (gelgit ekseni) | $t/q$ |
|---|---|---|---|
| Merkür | $1{,}01\times10^{-6}$ | $4{,}51\times10^{-7}$ | **0,445** |
| Venüs | $6{,}11\times10^{-8}$ | $7{,}16\times10^{-8}$ | **1,17** |
| *(Dünya, karşılaştırma)* | $3{,}46\times10^{-3}$ | $2{,}58\times10^{-8}$ | $7{,}5\times10^{-6}$ |

**Ama bu iki sayı skaler gibi toplanamaz** — §11.1'in uyarısı burada bağlayıcıdır: *"gelgit ekseni ≠ dönme ekseni."* F4 ve F5 **dönme eksenine** kilitlidir (M-38/M-39, R1); gelgit ise **Güneş–gövde doğrultusundadır.** İki farklı doğrultuda iki $P_2$ yapısı vardır ve toplamları tensörel olarak alınmak zorundadır. Üstelik teorinin gelgit tensörü Newton'unkiyle özdeş değildir: F4 dejenerasyonu kırar (yanal özdeğer çifti $-(1{+}\beta)$ ↔ $-1$), F5 ise izi ihlal eder ($\nabla\!\cdot\!\vec a_5=-2a_5/r$) — §11.1'in ayırt edici imzası tam buradadır.

### (iii) Kalıcı mı gezici mi — spin-yörünge durumu belirler

Gelgit ekseni **Güneş günü başına bir tur döner**; hızla dönen bir gövdede bu yüzden *kalıcı* figüre girmez, gezici bir deformasyon olarak kalır.

| Gövde | Güneş günü | Spin-yörünge | Kalıcı gelgit bileşeni |
|---|---|---|---|
| Altı serbest gezegen | 0,4–1,0 gün | serbest | **yok** ($t/q\le10^{-6}$, ayrıca gezici) |
| Venüs | 116,8 gün | asenkron, retrograd | **yok** — ömrü boyunca $\sim1{,}4\times10^{10}$ çevrim, gezici |
| **Merkür** | 175,9 gün | **3:2 rezonans** | **VAR** — ardışık günberilerde aynı yüz Güneş'e döner |

Merkür'ün kalıcı gelgit bileşeni teoride **türetilmiş** bir sonuçtur: M-24'ün günberi ritmi $q_{peri}(e)=\sqrt{1+e}/(1-e)^{3/2}$, $e=0{,}206$ ile $1{,}55\to3{:}2$ verir. Yani kilidin kendisi de, kalıcı bileşenin varlığı da aynı mekanizmadan gelir.

**Sonuç.** Merkür'ün ölçülen $J_2$'si hidrostatik değerin ~200 katıdır; Venüs'ün $f$'i $10^{-5}$'in altındadır ve ölçülemez. Bu iki gövde **hiçbir figür teorisini sınayamaz** — ama teorinin şunu söylemesi gerekir ve söyler: *bastırılmış gövdelerde figür ekseni dönmeden gelgite devreder.* Bu, kavrama mekanizmasının bedava getirdiği nitel bir sonuçtur.

> **Düzeltme kaydı — dört hata (3 Ağustos 2026).** Bu alt bölümün hazırlığında dört hata yapıldı ve kaydı korunur, çünkü üçü kolayca yeniden yapılabilir hatalardır.
> 1. **M-43'e yanlış hız verildi.** Altkritik bastırma $F\propto(v/v_{kav})^n$ hesaplanırken $v=\omega R$ (spin yüzey hızı) kullanıldı. M-43'ün argümanı $v_{bağıl}$'dır — cismin **ortama göre öteleme** hızı; Phoebe kalibrasyonu yörünge hızıyla yapılmıştır. Düzeltme, yavaş dönenlerde $10^{12}$ kata varan fark yaratır (Merkür/Venüs spinde en yavaş, yörüngede sistemin en hızlısıdır) ve sıralamayı tersine çevirir. Nicel hüküm değişmez, ama **iki yasanın aynı niceliği paylaşmadığı** böylece kanıtlanır: deplasman kapanışı spin yüzey hızını, M-43 yörünge bağıl hızını alır. Rakip yasa olarak karşılaştırılmaları kategori hatasıydı.
> 2. **Güneş gradyanı hiç hesaba katılmamıştı.** Merkür ve Venüs için $f$ yalnız dönmeden hesaplanmış, gelgit terimi atlanmıştı — oysa $t/q$ sırasıyla 0,445 ve 1,17'dir.
> 3. **Kalıcı/gezici ayrımı yapılmamıştı.** $t/q=1{,}17$ ile "Venüs'te gelgit baskın" denmişti; oysa $q$ kalıcı bir figür sürücüsü, $t$ ise Güneş günü başına bir tur atan gezici bir deformasyondur. İkisi aynı türden nesne değildir.
> 4. **Darwin–Radau Güneş'e uygulanmıştı.** Güneş için bildirilen $-\%21$'lik "sapma" fiziksel bir uyumsuzluk değil, DR'nin $\lambda=0{,}070$'te bilinen çöküşüdür. Referans model yanlış seçilmişti; doğru okuma 11.2.6'dadır.

---

## 11.2.9 Sekiz Gövdede Sınav: "Kim Kazandı?"

Bu bölümün en kritik sonucu şudur: Evrenakı (M-22 U2 uygulaması + izobar okuması) ile standart akışkan figür teorisi, gövdelerin basıklığı ($f$) konusunda rekabet içinde değildir; Evrenakı birinci ve ikinci mertebede **gözlenen basıklığı ölçüm hassasiyetinde üretir** ve aynı izobar cebiri standart teoride de kurulabilir. Ayrım üç yerde çıkar: yöntem disiplini, kavramsal zemin ve $J_4$ kanalı.

1. **Denge yasası: ÖLÇÜM HASSASİYETİNDE DOĞRULANDI.**
   İzobar okuması (11.2.6) serbest parametresiz olarak Dünya'da **+%0,014**, Jüpiter'de **+%0,08**, Satürn'de **−%0,09** verir; Güneş **−%2,3** ve Neptün **+%5,3** ile kendi ölçüm hatalarının içindedir. Sapan iki gövdenin ikisi de nedenini kendisi söyler: Mars'ın +%12,7'si ölçülmüş topografyadır (Tharsis — kabuk rijitliği izobara oturmayı zorunlu kılmaz), Uranüs'ün −%13,5'i girdideki manyetosfer-dönemi kusurudur ve her figür teorisinde aynıdır. Evrenakı'nın akışkan terimlerini (F5) bu kalemleri "düzeltmek" için kullanmak yapısal hata olurdu; F5'in genliği ($\kappa_5\lesssim0{,}017$) zaten dejenere ve fite soğurulmuş durumdadır (11.2.7).

2. **Yöntem: İZOBAR OKUMASI, DARWIN–RADAU'YU EMEKLİYE AYIRDI.**
   Kazanç iki katmanlıdır. *Pratik katman:* DR, λ'sı bağımsız ölçülen gövdelerde ±%1 bandında kalır ama λ'sı model çıktısı olan gaz devlerinde dolaşık, $\lambda\lesssim0{,}2$'de (yıldızlar) geçersizdir; izobar okuması bu üç kusurun üçünü de taşımaz ve üstüne Satürn'ün saklı dönme dönemini öngörür (**10ˢ 33ᵈ 13ˢⁿ**; halka sismolojisi 10ˢ 33ᵈ 38ˢⁿ — 25 saniye içinde). *Dürüstlük katmanı:* bu cebir potansiyel teorisinin malıdır ve standart fizikçi de aynı hesabı yapabilir — burada yenilen "standart fizik" değil, **iç-yapı-modeline-bağımlı yaklaşım alışkanlığıdır.** Teori bu yöntemi seçmek zorundaydı, çünkü kendi tezi budur: figür, kaynak modelinin değil, **fiilen ölçülen alanın** izobarıdır. Bu ayrım yapılmazsa karşılaştırma standart fiziğe haksızlık eder ve hakem denetiminde ilk düşecek kalem olur.

3. **Kavramsal zemin: EVRENAKI KAZANDI.**
   Standart model, gözlemi doğru hesaplasa da bunu "sanal kuvvet (fictitious force)" dediği merkezkaç üzerinden yapar. Evrenakı aynı dengeyi, uydurma çerçeve etkileriyle değil, uzay akışkanının **gerçek ataletiyle (M-22)** kurar; $J_2$ de onun için soyut bir katsayı değil, F1 basınç alanının ölçülmüş dört-kutup biçimidir — uydu yörüngeleri bu alanın içinde uçtuğu için izobar okuması teoride bir *tanım gereği* değil, bir *mekanizma sonucudur.*

> **Sonuç:** Gezegen basıklıkları ($f$ ve $J_2$) iki teoriyi ayırt etmez; her ikisi de aynı izobarı üretir ve Evrenakı bunu ölçüm hassasiyetinde yapar. Evrenakı'nın ayırt edici imzası $J_2$ basıklığında değil, F4'ün birinci mertebede yarattığı $J_4$ anomalilerindedir (11.2.7) — ve teoriden bağımsız tek açık kalem, Uranüs'ün iç dönme dönemidir (öngörü: 15,6–16,0 saat; sınayacak olan gelecek görev ölçümüdür).
