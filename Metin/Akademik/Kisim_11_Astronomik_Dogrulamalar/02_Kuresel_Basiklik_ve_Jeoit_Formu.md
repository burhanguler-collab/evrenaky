# 11.2 Küresel Basıklık ve Jeoit Formu

Dönen bir gök cismi neden küre değildir? Standart hidrostatik model bunu iki terimli bir dengeye bağlar: kütleçekimi içe çeker, merkezkaç ekvatorda dışa iter, yüzey bu ikisinin ortak eşpotansiyeline oturur. Evrenakı'da denge aynı sayıda terimden oluşmaz ve terimlerin hiçbiri "çekim" değildir. Bu bölüm, basıklığın teorideki mekanik zeminini kurar.

> **Bu dosyanın statüsü.** Bölüm yeniden kuruluyor. Aşağıda gözlem tabanı, terim envanteri ve F5'in yapısal türetimi yerleşiktir; basıklığın nicel kaynağı 11.2.5–11.2.6'da kurulmuş, $\phi$'nin üssü türetilmiştir ($p=1$). Sızma kesri $\varepsilon$ önerisi sınanıp **geri çekilmiştir** (11.2.7). **Kalan açık kalem**, F4'ün $J_4$ payı ile Ay üst sınırı arasındaki dar marjdır (11.2.8). Önceki sürümün kapanan/çürüyen kalemleri 11.2.10'da kayıtlıdır.

---

## 11.2.1 Gözlem Tabanı

Açıklanacak sayılar şunlardır:

| Nicelik | Dünya | Not |
|---|---|---|
| Basıklık $f=(a-b)/a$ | $3{,}3528\times10^{-3}$ ($1/298{,}257$) | WGS-84 |
| $J_2$ | $1{,}08263\times10^{-3}$ | baş figür terimi |
| $J_4$ | $-1{,}6199\times10^{-6}$ | ayrık kanal (11.2.8) |
| Merkezkaç oranı $q=\omega^2R^3/GM$ | $3{,}4614\times10^{-3}$ | boyutsuz sürücü |
| Hidrostatik denge fazlası | $\approx\%0{,}42$ | gözlenen $f$, katı hidrostatik modelin üzerinde |

Son satır bu bölümün çalışma alanıdır: standart model basıklığın **%99,6'sını** zaten verir. Teorinin ek terimleri bu payın içine sığmak zorundadır — daha fazlası gözlemle çelişir, sıfır olması ise teorinin figüre hiç katkı vermediği anlamına gelir.

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
3. **Deplasman kapanışı.** Akışın bıraktığı basınç açığı kinetik ölçeklemeyle yazılır: $\Delta P(\theta)=-\kappa_5\,\rho\,v(\theta)^2$. İdeal akış için $\kappa_5=\tfrac12$.

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

> **Dikkat — düzlemde tutmak ile şişirmek aynı şey değildir.** F5 meridyenel bir **geri çağırıcı** kuvvettir ve tam da basıklığın kurulacağı yerde, ekvatorda, **sıfırdır**. Yörüngeleri ve halkaları düzlemde tutması bu yüzden güçlüdür; gövdeyi şişirmeye katkısı ise ayrı ve çok daha zayıf bir sorudur (11.2.8).

---

## 11.2.5 Hız Kaynağı: Üç Aday, Bir Doğru Cevap

11.2.4 yapıyı verir ama $v_{eq}$'yu vermez. Basıklığın niceliği tamamen bu tek sayıya bağlıdır ($f_{yanal}\propto v_{eq}^2$) ve teoride **üç aday** vardır. Üçü de farklı nesnelerdir, farklı kanallara aittir ve mertebeleri arasında uçurumlar bulunur:

| Aday | Kaynak | $v_{eq}$ (Dünya yüzeyi) |
|---|---|---|
| **(A) Madde ekvator kuşağı** — $v_{eq}=\omega_{gövde}R$ | gövdenin kendi malzemesinin katı-cisim dönüşü (M-38/M-39 **R1**) | $465$ m/s |
| **(B) Ortam ekvator düzlemi** — $v_{eq}=v_\theta=2\sqrt{GM/R}$ | ortamın kendi dolaşımı (M-22 / M-38-M-39 **R2**) | $1{,}58\times10^{4}$ m/s |
| *(C) Dönme entrainment'ı* — $v_{eq}=\xi\,\omega R$ | dıştaki alan kuplajı (M-40) | $2{,}1\times10^{-7}$ m/s |

**Aday (A) figürün doğru kaynağıdır.** Gövdenin malzemesi katı cisim olarak döner, dolayısıyla $v(\theta)=\omega_{gövde}R\cos\theta$ **tam** geçerlidir — 11.2.4'ün istediği profil hiçbir varsayım gerektirmeden buradan gelir. Atama zorunludur: gözlenen $J_2$/$J_4$ **dönme eksenine** kilitlidir, oysa ortamın dolaşım ekseni Dünya'da $23{,}44°$ eğiklikle ondan ayrılır — kaynak (B) olsaydı imza yanlış eksende çıkardı.

**Aday (B) gövde figürüne değil, disk toplanmasına aittir** (R2): galaktik disklerin ve halka sistemlerinin ekvator düzleminde jilet inceliğinde toplanması bu rejimin işidir ve hiçbir kavrama kesri içermez. Yüzeyde $15{,}8$ km/s'lik dolaşım gerçektir, ama figürün simetri eksenini o belirlemez.

**Aday (C) elenmiştir** — ve zaten hiçbir zaman aday değildi: $\xi$ **dıştaki alan** kanalıdır, yüzey deplasmanı değil.

> **Düzeltme kaydı — bir önceki düzeltmenin düzeltmesi (3 Ağustos 2026).** Bu bölümün bir ara sürümü, M-39'un $v_e=\phi\,\omega R$ ifadesindeki $\phi$'yi M-40'ın $\xi$'si ile **aynı nicelik** sayıp "arada dokuz mertebe var, F5'in figüre katkısı sıfırdır" sonucuna varıyordu. **Bu yanlıştı.** Blok H'nin mimarisi iki kavrama kanalını baştan ayırır: **içeride deplasman kafesi** ($\mathcal{R}=\phi=1-1/n^2$, M-16 — *öteleme*, yerel, Fizeau ile ölçülü) ve **dışarıda alan** ($\xi$, M-40 — *açısal*, dipolar kuyruk). $0{,}6$ ile $4{,}6\times10^{-10}$ arasındaki uçurum bir çelişki değil, iki farklı kanalın okumasıdır.
>
> Asıl hata $\phi$'nin değerinde değil, **kullanımındaydı**: M-39 $v_e=\phi\omega R$'yi $\Omega_{ortam}=\phi\,\omega\approx0{,}6\,\omega$ olarak okuyordu, yani yerel öteleme taşımasını ortamın **küresel açısal hızına** yükseltiyordu — M-40'ın mutlak dışladığı nicelik budur. Düzeltme M-39'a işlenmiştir (Varsayım 2 ve 4, R1/R2 ayrımı): $\phi$ hızdan çıkarılmış, genliğe deplase edilen pay olarak bağlanmıştır. $\phi$'nin üssü de ardından **türetilmiştir** ($p=1$; M-39 Varsayım 4'ün iki-fazlı taşıma ifadesinden) ve $\kappa_5$ sınırı $\lesssim0{,}014$'e inmiştir.

**Kurulacak olan budur.** (B)'nin figüre ne verdiği henüz hesaplanmamıştır ve üç soruyu birlikte cevaplamayı gerektirir:

1. **Profil.** Disk dolaşımının yüzeydeki enlem bağımlılığı gerçekten $\cos\theta$ mıdır, yoksa disk kalınlığı ayrı bir profil mi dayatır?
2. **Nesne.** Dolaşan ortamdır ($\rho_0$); basıklık ise maddenin figürüdür ($\rho_n$). Basınç deseninin maddeye geçişi $\rho_0/\rho_n=\tfrac14$ çarpanını taşır — ama deseni **kuran** hız ortamınkidir. İki yoğunluğun hangi adımda girdiği açıkça yazılmalıdır (DY-1'in "tek gradyan, iki nesne" kuralı).
3. **Gözlemsel tavan.** Sonuç, 11.2.1'in $\%0{,}42$'lik hidrostatik fazlasının **içine sığmalıdır**. (B) $v^2$ ile ölçeklendiğinden bu, $\kappa_5$'e (A) altındakinden $\sim10^3$ kat daha sıkı bir üst sınır dayatır. Sınırın altında kalmak yetmez; teorinin figüre **hangi payı** verdiği de sayıyla söylenmelidir.

> **Korunan sonuç — cisimden bağımsızlık.** Aday (A) ile $v_{eq}\propto\omega R$ olduğundan, ivmeye geçildiğinde ($a=-\rho_n^{-1}\nabla P$) $\omega^2R^2$ ile merkezkaçın $\omega^2R$'si sadeleşir:
> $$\frac{a_{yanal}}{a_{merkezkaç}} = \kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi^{\,p}\cdot 2\sin\theta\,,\qquad p\in\{0,1,2\}$$
> Oran gövdenin boyutundan ve dönüş hızından **bağımsızdır**; yalnız kompozisyon çarpanına bağlıdır. Buradan çıkan kazanç korunur: klasik mekanikte $\omega$ arttıkça merkezkaç/itim oranı büyür ve bir yerde 1'i aşar — sert bir kopma tavanı vardır. Burada oran $\omega$ ile büyümediği için **bir hızda kararlı olan cisim her hızda kararlıdır**; tavan kalkmaz ama kompozisyona bağlı sabit bir çarpanla yükselir. Sadeleşme yalnızca $v_{eq}\propto\omega R$ olmasından geldiği için $\phi$'nin üssünden ($p$) **etkilenmez.**

---

## 11.2.6 Figür Denklemi — M-22'nin İki Uygulaması

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

İlk terim F1'in itim potansiyeli; ikincisi kafese bağlı maddenin **gerçek** dönme ataletidir (M-22'nin *"merkezkaç sanal değildir"* kaydı); son ikisi F4 ve F5'in paylarıdır.

**Serbest parametresiz çıktı.** $U_4=U_5=0$ ile, boyutsuz sürücü $q=\omega^2R^3/\mathcal{G}M$ ve eylemsizlik çarpanı $\lambda=I/MR^2$ cinsinden birinci mertebe figür:

$$\frac{f}{q}=\frac{5}{2\left[1+\tfrac{25}{4}\left(1-\tfrac32\lambda\right)^{2}\right]}$$

Dünya için ($q=3{,}4614\times10^{-3}$, $\lambda=0{,}3307$):

$$f_{öngörü}=3{,}3446\times10^{-3}\qquad\longleftrightarrow\qquad f_{gözlenen}=3{,}3528\times10^{-3}$$

**Basıklığın %99,76'sı M-22'nin U2 uygulamasından, serbest parametre olmadan çıkar.** Teorinin ek terimleri (F4, F5) kalan **%0,24**'ün içinde çalışmak zorundadır; 11.2.1'in tavanı budur. Kazanç, standart sonucun *ithal edilmesi* değil, aynı sayının teorinin kendi denge yasasından üretilmesidir — ve "merkezkaç" burada sanal bir çerçeve etkisi değil, ortamın gerçek ataletidir.

---

## 11.2.7 Sızma Kesri $\varepsilon$ — Sınandı ve Geri Çekildi

Figürü $q$, $q$'yu $\omega_{gövde}$ belirlediğine göre *"cisim neden bu hızda dönüyor?"* sorusu figür sorusunun parçasıdır. Bu bölümün bir ara sürümü buraya yeni bir parametre koyuyordu: **sızma kesri $\varepsilon$** — cismin 4B motorundan gelen dönüş ifadesinin, kafes yapısına bağlı olarak kendi ortamına aktarılan payı. Öneri, Güneş'in yavaş dönüşünü ($\varepsilon_\odot\approx0{,}996$) ve "güneş açısal momentum problemi"ni tek hamlede açıklıyor görünüyordu.

**Sınandı ve üç bağımsız gerekçeyle geri çekilmiştir.** Kayıt, gerekçeleriyle korunur; öneri değerlidir, fakat bu biçimde yürümez.

### (1) $\varepsilon$ yapısal değil, zamansaldır — kafes onu belirleyemez

Önerinin çekirdeği "kafes sıkılığı $\varepsilon$'u belirler"di. Fakat **sabit kütlede ve sabit yapıda** $\varepsilon$ yalnızca yaşla değişir. Güneş kütleli yıldızların açık kümelerdeki dizisi:

| Topluluk | Yaş | $P_{dönme}$ | $\varepsilon$ |
|---|---|---|---|
| T Tauri / ONC | 1 Myr | ~2 gün | **0,949** |
| Pleiades | 125 Myr | ~5 gün | **0,980** |
| Hyades | 625 Myr | ~10 gün | **0,990** |
| M67 | 4 Gyr | ~26 gün | **0,996** |
| Güneş | 4,57 Gyr | 25,4 gün | **0,996** |

Aynı kütle, aynı kafes, aynı kompozisyon — $\varepsilon$ yine de $0{,}95$'ten $0{,}996$'ya çıkıyor. Dolayısıyla $\varepsilon$ bir **yapı parametresi olamaz**; en fazla kafes *hızı* ($d\varepsilon/dt$) belirleyebilir. Öneri bu hâliyle yanlış nesneye bağlanmıştı.

### (2) Açıkladığı gözlem zaten açıklanmıştır

Yukarıdaki dizi, Skumanich yasasının ($\omega\propto t^{-1/2}$) ta kendisidir; Güneş'e çapalanınca kümeleri **%6–19** içinde verir (125 Myr'den itibaren). Manyetik frenleme ve jirokronoloji binlerce yıldızda bağımsız olarak desteklenmiştir. Kitabın kendi ilkesi burada bağlayıcıdır — Kısım 6 §6.3.2'nin Pioneer kaydı: *"Evrenakı ısıl geri tepmeyi dışlamadığından bu çözüm burada da kabul edilir."* Evrenakı manyetik frenlemeyi de dışlamaz; dolayısıyla Güneş'in yavaş dönüşü için **yeni bir parametre gerekmez.**

### (3) Başlık sayısı ($L_{sızan}/L_{gezegen}\approx1{,}4$) bir artefakttır

En sert kayıt budur. Kütle–dönüş yasasının Güneş kütlesine ekstrapolasyonu **497 km/s** verir; Güneş'in **kopma (breakup) hızı** ise $\sqrt{\mathcal{G}M/R}=437$ km/s'dir — arada yalnız **%14** vardır. Yani $L_{serbest}\approx L_{kopma}$ ve

$$\frac{L_{kopma}}{L_{gezegen}}=\frac{4{,}23\times10^{43}}{3{,}13\times10^{43}}=1{,}35$$

Elde edilen "1,4" bu orandır. Ve $L_{kopma}\sim L_{disk}$ ifadesi, standart yıldız oluşumunun **zaten bilinen** temel gözlemidir: çöken bulut bir yıldızın tutabileceğinden çok fazla açısal momentum taşır, fazlası diske gider — diskler bu yüzden vardır. Sayı yeni bir kanıt değil, bu bilinen ifadenin yeniden yazımıdır.

### Ayakta kalan: yasanın tanım alanı daraltılmalı

Sınav, $\varepsilon$'u düşürürken bağımsız ve kalıcı bir sonuç bıraktı: **Kısım 3 §3.4.4'ün kütle–dönüş yasası yıldızlara uygulanamaz.**

| Gövde | Yasanın $v_{serbest}$'i | Gözlenen | Durum |
|---|---|---|---|
| T Tauri (en genç, 1 Myr) | 497 km/s | ~25 km/s | yasa **20 kat** yüksek — *doğumda bile* |
| Beyaz cüce | 382 km/s | ~0,5 km/s | tanım alanı dışı (çökmüş kalıntı) |
| **Nötron yıldızı** | 590 km/s | $7{,}5\times10^4$ km/s | yasa **127 kat aşılıyor** — $\varepsilon<0$ |

Nötron yıldızı satırı belirleyicidir: $\varepsilon\in[0,1]$ tanımlıysa negatif değer alamaz. Sebep açıktır — çökmüş kalıntıların dönüşü 4B motorun ifadesinden değil, çökme sırasındaki **açısal momentum korunumundan** gelir ($R$ $10^5$ kat küçülür, $\omega$ $10^{10}$ kat büyür). Yasa, *yerinde oluşmuş* gövdeler için kurulmuştur.

> **Sonuç.** $\varepsilon$ kitaba **girmez.** Kullanıcının çekirdek sezgisi — kafesin, dönüşün ne kadarının ortama geçtiğini belirlediği — çürütülmüş değildir; ama yeri $\varepsilon$ değil $d\varepsilon/dt$'dir ve orada manyetik frenlemeyle **yarışmak** zorundadır. Yerini hak etmesi için ayırt edici bir vaka gerekir: manyetik alanı ve rüzgârı ihmal edilebilir olan, buna karşın yine de dönüş kaybeden bir gövde sınıfı. Bulunmadıkça figür hesabı $\omega_{gövde}$'yi **gözlemden girdi olarak alır** (11.2.6) ve teori bu noktada bir açıklama borcu taşımaz.

---

## 11.2.8 Multipol Muhasebesi: Kim Ayrıştırılabilir?

Bir kuvvetin figüre katkı vermesi ile o katkının **ölçüde ayırt edilebilmesi** farklı şeylerdir. Sınav 1'in (6.6.2) multipol ayrıştırması bu ayrımı keskin biçimde koyar:

| Öğe | Ürettiği harmonikler | Ayrık imza? |
|---|---|---|
| Merkezkaç | saf $P_2$ | — (referans) |
| **F5** | **saf $P_2$** | **Yok** — merkezkaçla dejenere |
| **F4** | $P_2,\,P_4,\,P_6$ | **Var** — $J_4$ kanalı |

**F5'in basıklıktaki etkisi ölçüde sıfıra düşer** — ve sebebi genliğinin küçüklüğünden önce **dejenerasyondur**: F5, merkezkaç potansiyelinin sabit bir çarpanla yeniden ölçeklenmesine denktir. Gezegeni farklı bir şekle sokmaz; yalnızca *biraz daha hızlı dönüyormuş gibi* görünmesine yol açar. Dolayısıyla $J_4$ veya $J_6$'da aranacak ayrı bir F5 imzası **yoktur**; katkısı ne olursa olsun fite soğurulur. (İlk tasarım imzayı $J_4$'te arıyordu; gerekçesi "kuvvet profilleri farklı görünüyor" idi ve yanlıştı — farklı kuvvet profili, farklı multipol içeriği demek değildir.)

**Ayrıştırılabilir imzayı taşıyan kuvvet F4'tür.** Merkezkaç $J_4$'e birinci mertebede hiç katkı vermez, F4 verir — boş kanalda zayıf kuvvet görünür hâle gelir. Dünya için indüklenen $J_4$ payı **%4–8** mertebesindedir ve **işareti doğrudur**: gözlenen $J_4$, hidrostatik modellerin verdiğinden daha derindir ve F4 tam o yönde çalışır. Bu, sınav programının olumsuz olmayan ilk sonucudur — "geçilmiş sınav" değil, "teorinin öngörüsü önemli olacak büyüklükte" durumu. Dürüst sınırları (hidrostatik referansın $\sim\%10$ belirsizliği, hidrostatik-olmayan manto katkısı) 6.6.2'dedir.

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

**Ay tutarlılık kontrolü.** M-38'in gövde rejimi (R1) Ay verisiyle sınırlıdır: $\varepsilon(r_{Ay})<2\times10^{-5}$ ve $\varepsilon\propto r$ ile yüzeyde $\varepsilon(R_\oplus)<3{,}3\times10^{-7}$. $J_4=1{,}62\times10^{-6}$ olduğuna göre F4'e $J_4$'ün en çok **%20'si** kadar yer vardır; iddia %4–8'dir. **Geçiyor — fakat marj yalnız ~2,5 kat.** Öngörünün üst ucu doğrulanırsa Ay sınırı ile çatışma başlar; bu, iki bağımsız verinin aynı katsayıyı kıstırdığı gerçek bir sınavdır.

---

## 11.2.9 Gövde Sınıflarına Uygulama

*(Aşağıdaki okumalar $\phi$'nin üssü ($p$) sabitlenmeden nicelleştirilemez; şimdilik gözlemsel çapalar korunmuştur. Kompozisyon ekseninin "Güneş'te F5 yok" okuması ise geri çekilmiştir — 11.2.10.)*

- **Dünya.** Gözlenen $\sim\%0{,}42$'lik hidrostatik fazlası, teorinin toplam ek payına **üst sınır** verir. Fazlanın jeofizikte bağımsız olarak (hidrostatik-olmayan manto yapısıyla) modellenmiş olduğu, dolayısıyla teoriye düşen payın sıfıra kadar inebileceği kaydı için bkz. 6.6.2.
- **Güneş.** Ölçülen $J_2=2{,}2\times10^{-7}$, iç yoğunluk profili göz önüne alındığında hidrostatik/merkezkaç öngörüsüyle **uyumludur.** Bu bir kavrama ölçümü değildir: figürün küçük çıkması kavramanın yokluğundan da, **iki büyük terimin birbirini kısmen yemesinden** de gelebilir — F4 merkezkaçın zıddına çalışır ve 6.6.2'nin işaret kontrolü bunu bağımsız olarak doğrular.
- **Gaz devleri.** Satürn'ün sistemin en basık gezegeni olması, F4/F5 paylarının derin akışkan yapılarda büyümesiyle uyumlu bir adaydır; nicel iddia 11.2.5 kapanmadan yazılamaz.

---

## 11.2.10 Açık Kalemler ve Düzeltme Kayıtları

**Kurulacak:**
1. ~~$\phi$'nin üssü $p$~~ → **KAPANDI (3 Ağustos 2026):** $p=1$ türetildi (M-39, Varsayım 4). Kalan incelik, iki-fazlı taşımanın literal geçerliliği; yüzeyde ortam homojenleşiyorsa $p=2$'ye döner.
2. Ortam basınç deseninin ($\rho_0$) madde figürüne ($\rho_n$) geçiş adımı — DY-1'in "tek gradyan, iki nesne" kuralıyla.
3. Sonucun $\%0{,}42$ tavanına oturtulması: teorinin figüre verdiği payın **sayıyla** söylenmesi (sınırın altında kalmak yetmez).
4. F4'ün $J_4$ payının Ay üst sınırıyla ($\varepsilon(R_\oplus)<3{,}3\times10^{-7}$) birlikte tutarlılığı — mevcut marj yalnız $\sim$2,5 kat.

**Düzeltme kaydı — Güneş'in $\phi$ istisnası (3 Ağustos 2026, korunuyor).** Daha eski bir sürüm *"tam iyonize plazmada bağlı kafes bulunmaz ($\phi\approx0$), yanal itim sıfırlanır"* diyordu. Gerekçe üç yönden geçersizdi: **(i)** teorinin kavraması nükleon düzeyindedir, iyonizasyon elektronu söker — plazmadaki proton kayadaki protonun aynısıdır; **(ii)** $\phi_\odot\approx0$ Güneş'in makro girdabını iptal ederdi, oysa 3.8'in tamamı ona dayanır; **(iii)** aynı paragraf gaz devlerine en yüksek $\phi$'yi veriyordu, oysa Jüpiter'in iç kütlesinin çoğu basınçla iyonize metalik hidrojendir. Bu kayıt M-39'a da işlenmiş ve oradaki "yanal itim Güneş'te yoktur" maddesi geri çekilmiştir; buna bağlı olarak **Ek H §H.3'ün "Güneş'te yok" satırı ile §H.2'nin 3. kalemindeki "kompozisyon eksenini de sınar" ifadesi de dayanaksızdır** (Kısım 7 §7.5 bu öngörüyü içermez). Ayrıca özel bir Güneş istisnası gereksizdir: Sınav 1, F5'in figürde her yerde ayrı imza bırakmadığını göstermiştir.

**Düzeltme kaydı — plazma istisnası (3 Ağustos 2026, korunuyor).** Daha eski bir sürüm *"tam iyonize plazmada bağlı kafes bulunmaz ($\phi\approx0$), yanal itim sıfırlanır"* diyordu. Gerekçe üç yönden geçersizdi: **(i)** teorinin kavraması nükleon düzeyindedir, iyonizasyon elektronu söker — plazmadaki proton kayadaki protonun aynısıdır; **(ii)** $\phi_\odot\approx0$ Güneş'in makro girdabını iptal ederdi, oysa 3.8'in tamamı ona dayanır; **(iii)** aynı paragraf gaz devlerine en yüksek $\phi$'yi veriyordu, oysa Jüpiter'in iç kütlesinin çoğu basınçla iyonize metalik hidrojendir. Kayıt korunur, çünkü kaldırılan gerekçenin **neden** geçersiz olduğu hâlâ bağlayıcıdır; $\phi$'nin kendisi ise yukarıdaki kayıtla zaten düşmüştür.
