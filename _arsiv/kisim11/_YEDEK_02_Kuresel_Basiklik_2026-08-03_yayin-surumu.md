# 11.2 Küresel Basıklık ve Jeoit Formu

Dönen bir gök cismi neden küre değildir? Standart fizik bunu iki terimli bir dengeye bağlar: kütleçekimi içe çeker, "sanal" saydığı merkezkaç ekvatorda dışa iter, yüzey ikisinin ortak eşpotansiyeline oturur. Evrenakı'da terimlerin hiçbiri çekim değildir ve merkezkaç sanal değildir: gövdeyi içe bastıran şey ortamın kütle-itimi (F1, M-2), dışa direnen şey kafese bağlı maddenin **gerçek** dönme ataletidir (M-22, U2). Bu bölüm önce basıklığın teorideki mekanik zeminini kurar, sonra teorinin kendi formülasyonunu — **izobar okumasını** — kapalı bir bağıntıya döker ve sekiz gövdede gözlemle yüzleştirir.

> **Gözlemsel Hedef.** Figürü, iç yapı modellerine (eylemsizlik çarpanı $\lambda$) muhtaç yaklaşım formülleriyle değil, **fiilen ölçülmüş basınç alanının izobarından** okumak. Ulaşılan hassasiyet: Dünya **+%0,014**, Jüpiter **+%0,08**, Satürn **−%0,09** — ve bağıntının tersine çevrilmesiyle Satürn'ün bulutlar altında saklı dönme döneminin **10ˢ 33ᵈ 13ˢⁿ** olarak öngörülmesi (Cassini halka sismolojisi: 10ˢ 33ᵈ 38ˢⁿ).

---

## 11.2.1 Gözlem Tabanı ve İki Soru

Sınava girecek veri şudur; her satır uzay aracı ölçümüdür, hiçbiri model çıktısı değildir:

| Gövde | $a$ (km) | Dönme dönemi | $J_2$ | $J_4$ | $f_{gözlenen}$ | Kaynak |
|---|---|---|---|---|---|---|
| Dünya | 6.378,137 | 23ˢ 56ᵈ 04ˢⁿ | $1{,}08263\times10^{-3}$ | $-1{,}6199\times10^{-6}$ | $3{,}35281\times10^{-3}$ | WGS-84 / GRACE |
| Mars | 3.396,19 | 24ˢ 37ᵈ 23ˢⁿ | $1{,}9566\times10^{-3}$ | $-1{,}54\times10^{-5}$ | $5{,}888\times10^{-3}$ | MRO / MOLA |
| Jüpiter | 71.492 | 9ˢ 55ᵈ 30ˢⁿ (Sistem III) | $1{,}46966\times10^{-2}$ | $-5{,}8661\times10^{-4}$ | $6{,}4874\times10^{-2}$ | Juno |
| Satürn | 60.268 | **belirsiz** (metin) | $1{,}62906\times10^{-2}$ | $-9{,}3531\times10^{-4}$ | $9{,}7963\times10^{-2}$ | Cassini |
| Uranüs | 25.559 | 17ˢ 14ᵈ (manyetosfer) | $3{,}5107\times10^{-3}$ | $-3{,}42\times10^{-5}$ | $2{,}2927\times10^{-2}\pm\%3{,}5$ | Voyager 2 |
| Neptün | 24.764 | 16ˢ 07ᵈ (radyo) | $3{,}4084\times10^{-3}$ | $-3{,}34\times10^{-5}$ | $1{,}7081\times10^{-2}\pm\%7$ | Voyager 2 |
| Güneş | 695.700 | 25,38 gün (Carrington) | $2{,}2\times10^{-7}$ | $\approx0$ | $1{,}10\times10^{-5}\pm\%5$ | helyosismoloji + efemeris |

Dünya için boyutsuz sürücü $q=\omega^2R^3/\mathcal{G}M=3{,}4614\times10^{-3}$'tür ve literatürün bilinen kalemi şudur: gözlenen $f$, iç-yapı temelli hidrostatik modellerin yaklaşık **%0,42 üzerindedir.** Bu kalem doğru okunmazsa bölümün tamamı yanlış kurulur, çünkü ortada iki ayrı soru vardır:

1. **Kaynak sorusu** — gövdenin içi $J_2$'yi hangi değerde üretir? Bu, iç yoğunluk dağılımının işidir. Dünya'nın manto anomalileri ölçülen $J_2$'yi hidrostatik iç-yapı modellerinin üzerine çıkarır; %0,42'lik "fazla" burada, **kaynak yanında** yaşar.
2. **Denge sorusu** — yüzey, *fiilen ölçülen* alanın izobarına oturuyor mu? Bu, teorinin denge yasasının (M-22) işidir ve iç yapıdan bağımsız sınanabilir.

Bu bölümün ana sınavı ikinci sorudur. Ölçülen $J_2$ kaynak anomalilerini zaten içinde taşıdığından, izobar sınavı %0,42'lik kalemi otomatik soğurur: Dünya'da denge yasası **+%0,014** hassasiyetle tutar (11.2.6). Kaynak sorusundan teoriye düşen pay ise ayrık $J_4$ kanalındadır (11.2.7).

---

## 11.2.2 Terim Envanteri

Basıklık masasında dört Evrenakı öğesi oturur; karışmamaları için kaynakları ve nesneleri ayrı yazılır:

| Öğe | Katalog | Nesnesi | Yönü |
|---|---|---|---|
| **F1** — radyal kütle-itim | M-2 | gövde maddesi ($\rho_n$) | içe, küresel |
| **Merkezkaç gereksinimi** | — | gövde maddesi ($\rho_n$) | dışa, $\propto\omega^2R$ |
| **F4** — eksenel itim | M-38 | gövde maddesi | dönme eksenine doğru, $\propto1/R$ |
| **F5** — yanal itim | M-39 | gövde maddesi | ekvator düzlemine doğru, $\propto\sin2\theta$ |
| **M-22** — ortamın siklostrofik dengesi | M-22 / DY-1 | **ortam** ($\rho_0$) | denge yasası — kuvvet değil |

Son satır ayrı türdendir ve diğerleriyle toplanmaz: **M-22 bir kuvvet değil**, F1'in kurduğu $\nabla P$'nin ortamın dolaşımıyla dengede olduğunu söyleyen bir koşuldur (DY-1). Basıklık hesabına iki ayrı kapıdan girer ve kapılar karıştırılmamalıdır: figüre **U2 uygulamasıyla** girer (kafese bağlı gövde maddesinin dönme ataleti — 11.2.6), disk ve halka toplanmasına ise **U1 + R2** ile (ortamın kendi dolaşımı — 11.2.5).

**F4 ile F5 aynı olayın iki yüzüdür.** İkisi de gövdenin dönüşünden, tek mekanizmayla doğar: ekvator kuşağı, Evrenakı'yı düzlem boyunca dışa **deplase eder** (M-38, Varsayım 1). Deplasman yerel bir öteleme olayıdır — kafes, bulunduğu noktadaki ortamın $\phi=1-1/n^2$ kesrini kendi malzemesinin hızıyla taşır (M-16'nın Fizeau kanalı) ve bunun için ortamın küresel bir açısal hıza girmesi gerekmez; dönme patinajıyla ($\xi$, ayrı kanal) çelişki bu yüzden yoktur. Deplasman akısı silindir yanağından geçerken **F4**, yüzey basıncının enleme bağlı profilinden **F5** doğar.

---

## 11.2.3 Geometri ve Ortak Tanımlar

1. **Koordinatlar.** Küresel koordinatlarda $R=r\cos\theta$ (dönme eksenine uzaklık), $z=r\sin\theta$ (ekvator düzlemine uzaklık); $\theta$ ekvatordan ölçülen enlemdir: ekvator $\theta=0$, kutup $\theta=90°$.
2. **İki yoğunluk.** Aynı $\nabla P$ ortama $\rho_0$, maddeye $\rho_n$ ile etki eder; M-8'in $k=0$ hâliyle $\rho_n=4\rho_0$ (M-2 ↔ M-22 ayrımı). Figür hesabı **madde** hesabıdır, dolayısıyla $\rho_n$ ile yürür.
3. **Deplasman kapanışı.** Akışın bıraktığı basınç açığı kinetik ölçeklemeyle yazılır: $\Delta P(\theta)=-\kappa_5\,(\phi\rho_0)\,v(\theta)^2$ — yalnız deplase edilen $\phi$ kesri taşındığı için genlik $\phi$ ile **doğrusaldır** ($p=1$; M-39 Varsayım 4'ün iki-fazlı türetimi). İdeal akış $\kappa_5=\tfrac12$ verirdi; Dünya basıklığı $\kappa_5\lesssim0{,}014$–$0{,}017$ dayatır (bant, $\phi$'nin ~%10'luk hacim-kesri sistematiğinden).
4. **$\phi$ hacim kesridir, optik nicelik değil.** Blok D'nin tanımı bağlayıcıdır: $\phi$ bağlı yapının kapladığı **hacim kesri**, $1/n^2=1-\phi$ ise onun şeffaf ortamdaki **ölçüm yolu** (M-15'te $\phi$ girdi, $n$ çıktıdır). Metallerde ($n$ karmaşık) ve iyonize plazmada ($n<1$ ya da sanal) ters okuma çöker; hacim kesri tanımlı kalır.

---

## 11.2.4 F5'in Yapısı: $\sin2\theta$ Yasası

Bu türetim **hızdan bağımsızdır**: yüzeydeki teğetsel akışın ekvatoral değeri $v_{eq}$ ne olursa olsun, enlem profili $v(\theta)=v_{eq}\cos\theta$ olduğu sürece yapı aynı çıkar. (Hangi $v_{eq}$'nun doğru olduğu ayrı bir sorudur — 11.2.5.)

Yüzey basınç profili:
$$P(\theta) = P_{kutup} - \kappa_5\,\rho\,v_{eq}^2\cos^2\theta$$

Açısal gradyan ($\nabla_\theta P=\tfrac1r\,dP/d\theta$) alınır; $\tfrac{d}{d\theta}(\cos^2\theta)=-\sin2\theta$ olduğundan:

$$\frac{dP}{d\theta} = \kappa_5\rho v_{eq}^2\sin2\theta$$

Birim hacme düşen kuvvet $f=-\nabla P$ ile:

$$\boxed{\;f_{yanal}(\theta) = -\frac{\kappa_5\,\rho\,v_{eq}^{2}}{r}\,\sin 2\theta\qquad [\mathrm{N/m^3}]\;}$$

Eksi işareti ($-\hat\theta$), kuvvetin her iki yarımküreden de **ekvatora doğru** olduğunu söyler.

**Kararlılık deseni.** $|f|\propto\sin2\theta$ olduğundan:

| Enlem | Kuvvet | Denge |
|---|---|---|
| Ekvator ($\theta=0°$) | sıfır | **kararlı** — sapan madde geri itilir |
| Orta enlem ($\theta=45°$) | maksimum | ezme zirvesi |
| Kutup ($\theta=90°$) | sıfır | **kararsız** — madde barınamaz, ekvatora savrulur |

Ekvator, yanal itim alanının tek kararlı çekim noktasıdır. Halka sistemlerinin ve galaktik disklerin jilet inceliğinde ekvator düzleminde toplanması bu desene bağlanır (11.4, M-27); yörünge eş-düzlemliliği de aynı kaynaktan gelir.

> **Dikkat — düzlemde tutmak ile şişirmek aynı şey değildir.** F5 meridyenel bir **geri çağırıcı** kuvvettir ve tam da basıklığın kurulacağı yerde, ekvatorda, **sıfırdır**. Yörüngeleri ve halkaları düzlemde tutması bu yüzden güçlüdür; gövdeyi şişirmeye katkısı ise ayrı ve çok daha zayıf bir sorudur — cevabı 11.2.7'dedir: ölçüde görünmez.

---

## 11.2.5 Hız Kaynağı: Üç Aday, Bir Doğru Cevap

11.2.4 yapıyı verir ama $v_{eq}$'yu vermez. Genlik tamamen bu tek sayıya bağlıdır ($f_{yanal}\propto v_{eq}^2$) ve teoride üç aday vardır; üçü farklı nesnedir, farklı kanallara aittir, mertebeleri arasında uçurum vardır:

| Aday | Kaynak | $v_{eq}$ (Dünya yüzeyi) |
|---|---|---|
| **(A) Madde ekvator kuşağı** — $v_{eq}=\omega_{gövde}R$ | gövde malzemesinin katı-cisim dönüşü (M-38/M-39 **R1**) | $465$ m/s |
| **(B) Ortam ekvator düzlemi** — $v_{eq}=v_\theta=2\sqrt{\mathcal{G}M/R}$ | ortamın kendi dolaşımı (M-22 / M-38-M-39 **R2**) | $1{,}58\times10^{4}$ m/s |
| *(C) Dönme entrainment'ı* — $v_{eq}=\xi\,\omega R$ | dıştaki alan kuplajı (M-40) | $2{,}1\times10^{-7}$ m/s |

**Aday (A) figürün doğru kaynağıdır.** Gövde malzemesi katı cisim olarak döndüğünden $v(\theta)=\omega_{gövde}R\cos\theta$ profili hiçbir varsayım gerektirmeden **tam** sağlanır. Atama ayrıca zorunludur: gözlenen $J_2$/$J_4$ **dönme eksenine** kilitlidir, oysa ortamın dolaşım ekseni Dünya'da $23{,}44°$ eğiklikle ondan ayrılır — kaynak (B) olsaydı imza yanlış eksende çıkardı.

**Aday (B) gövde figürüne değil, disk toplanmasına aittir** (R2): galaktik disklerin ve halka sistemlerinin ekvator düzleminde toplanması bu rejimin işidir ve hiçbir kavrama kesri içermez. Yüzeydeki $15{,}8$ km/s'lik dolaşım gerçektir; ama figürün simetri eksenini o belirlemez.

**Aday (C) elenmiştir** — ve zaten hiçbir zaman aday değildi: $\xi$ **dıştaki alan** kanalıdır, yüzey deplasmanı değil.

> **Korunan sonuç — cisimden bağımsızlık.** Aday (A) ile $v_{eq}\propto\omega R$ olduğundan, ivmeye geçildiğinde ($a=-\rho_n^{-1}\nabla P$) $\omega^2R^2$ ile merkezkaçın $\omega^2R$'si sadeleşir:
> $$\frac{a_{yanal}}{a_{merkezkaç}} = \kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi\cdot 2\sin\theta \qquad (p=1)$$
> Oran gövdenin boyutundan ve dönüş hızından **bağımsızdır**; yalnız kompozisyon çarpanına ($\phi$, hacim kesri) bağlıdır. Kazanç şudur: klasik mekanikte $\omega$ arttıkça merkezkaç/itim oranı büyür ve bir yerde 1'i aşar — sert bir kopma tavanı vardır. Burada oran $\omega$ ile büyümediği için **bir hızda kararlı olan cisim her hızda kararlıdır**; tavan kalkmaz ama kompozisyona bağlı sabit bir çarpanla yükselir. Sadeleşme yalnız $v_{eq}\propto\omega R$ olmasından geldiği için $\phi$'nin üssünden etkilenmez.

---

## 11.2.6 Figür Denklemi: İzobar Okuması

### M-22'nin iki uygulaması — yanlış 2 çarpanına karşı

M-22 tek denge yasasıdır ($dP/dr=\rho v_\theta^2/r$) ama iki ayrı nesneye uygulanır; karıştırılırsa figüre yanlış bir 2 çarpanı sızar.

**(U1) Serbest madde — DY-1 rejimi.** Yalnız $\nabla P$ ile tutulan madde. Tek gradyan iki yoğunluğa etki eder: $\rho_0v_\theta^2=\rho_nv_{madde}^2$, ve M-8'in $\rho_n=4\rho_0$ sonucuyla $v_\theta=2\,v_{madde}$. Bu 2 çarpanı **serbest düşme dengesinin** malıdır.

**(U2) Kafese bağlı gövde maddesi — figür rejimi.** Gövde malzemesi $\nabla P$ ile değil **kafes rijitliğiyle** tutulur. Testi doğrudandır: serbest düşme dengesinde olsaydı yüzey hızı yörünge hızına eşit olurdu —

| | $\omega R$ | $\sqrt{\mathcal{G}M/R}$ | oran |
|---|---|---|---|
| Dünya | 465 m/s | 7.905 m/s | **0,059** |
| Jüpiter | 12.572 m/s | 42.096 m/s | **0,299** |
| Satürn | 9.871 m/s | 25.087 m/s | **0,394** |
| Güneş | 1.993 m/s | 436.762 m/s | **0,005** |

Hiçbiri 1'e yakın değildir: hiçbir gövdenin yüzey maddesi DY-1 rejiminde değildir. Figür hesabında $v_\theta=2\,\omega R$ yazmak bu yüzden hatadır — U1'in 2 çarpanı U2'ye **taşınmaz**.

U2'de M-22 hızı kapatan bir bağıntı değil, dışarıdan verilen $\omega$ karşısında basınç alanının uymak zorunda olduğu **koşuldur**; figür bu koşulun yüzeyidir:

$$U(r,\theta)\;=\;-\frac{\mathcal{G}M}{r}\;-\;\tfrac12\,\omega^2r^2\cos^2\theta\;+\;U_4+U_5\;=\;\text{sabit}$$

İlk terim F1'in itim potansiyeli, ikincisi kafese bağlı maddenin **gerçek** dönme ataleti (M-22'nin *"merkezkaç sanal değildir"* kaydı), son ikisi F4 ve F5'in paylarıdır — F5 merkezkaça soğurulur, F4'ün ayrık payı $J_4$ kanalında yaşar (11.2.7); ikisi de aşağıdaki okumayı bozmaz, çünkü okuma **ölçülmüş** alanı kullanır ve alan, kaynakları kim olursa olsun, ölçüldüğü gibidir.

### Türetim: kapalı bağıntı

Teorinin tezi şudur: yüzey, fiilen ölçülen basınç alanının izobarıdır. Alan gerçekten ölçülmüştür — uydu ve uzay aracı yörüngeleri teoride tam olarak bu alanın içinde uçar; $J_2$ ve $J_4$, F1 alanının ölçülmüş çok-kutup katsayılarıdır. İç yapıya dair hiçbir varsayıma gerek yoktur: $\lambda$'nın taşıdığı bütün bilgi ölçülen $J_2$'nin içinde zaten durur.

Adımlar:

1. **Alanın dış açılımı.** $V(r,\theta)=-\dfrac{\mathcal{G}M}{r}\Bigl[1-J_2\bigl(\tfrac ar\bigr)^2P_2(\sin\theta)-J_4\bigl(\tfrac ar\bigr)^4P_4(\sin\theta)\Bigr]$; Legendre değerleri: ekvatorda $P_2=-\tfrac12,\ P_4=\tfrac38$; kutupta $P_2=P_4=1$.
2. **İzobar koşulu.** $U=V-\tfrac12\omega^2r^2\cos^2\theta=$ sabit; iki uçta değerlendirilir: ekvator $r=a$, kutup $r=b=a(1-f)$.
3. **Ekvator değeri.** $U_{eq}=-\dfrac{\mathcal{G}M}{a}\bigl[1+\tfrac12J_2-\tfrac38J_4+\tfrac12q\bigr]$ — burada $\tfrac12\omega^2a^2=\tfrac12q\,\mathcal{G}M/a$ kullanıldı, $q=\omega^2a^3/\mathcal{G}M$.
4. **Kutup değeri.** $(1-f)^{-1}\simeq1+f+f^2$, $(1-f)^{-3}\simeq1+3f$ açılımlarıyla ($J_4$ zaten ikinci mertebedir): $U_{kutup}=-\dfrac{\mathcal{G}M}{a}\bigl[1+f+f^2-J_2(1+3f)-J_4\bigr]$.
5. **Eşitleme.** $U_{eq}=U_{kutup}$ düzenlenince:

$$\boxed{\;f=\tfrac32 J_2+\tfrac12 q\;+\;\underbrace{3J_2\,f-f^2+\tfrac58 J_4}_{\text{ikinci mertebe}}\;}$$

Birinci mertebede $f=\tfrac32J_2+\tfrac12q$; ikinci mertebe terimleri gaz devlerinde %2–6 düzeltme getirir ve $f$'te örtük olduklarından iki-üç yinelemeyle çözülür. Kesme hatası $O(f^3)$'tür: Dünya'da $\sim10^{-8}$ (ihmal), Jüpiter'de ~%0,3, Satürn'de ~%1 tavanı — ölçülmüş $J_4$'ün kullanılması bu payın bir bölümünü de soğurur.

**Bağıntı iki kesin limiti kendiliğinden içerir:**

| Limit | $J_2$ değeri | Bağıntının verdiği | Kesin değer |
|---|---|---|---|
| Nokta kütle (yıldız) | $J_2\to0$ | $f=q/2$ | $q/2$ ✓ |
| Homojen gövde (Maclaurin) | $J_2=q/2$ | $f=\tfrac54q$ | $\tfrac54q$ ✓ |

Arada hiçbir interpolasyon varsayımı yoktur; gövdenin iki uç arasında nerede durduğunu ölçülen $J_2$ söyler.

### Jeoit: izobarın öteki adı

Bölüm başlığındaki "jeoit formu" bu bağıntının ta kendisidir — bir çeviri farkıyla. Standart dilde jeoit, ortalama deniz yüzeyinin oturduğu **eşpotansiyel** yüzeydir; Evrenakı'da aynı yüzey **eş-basınç** yüzeyidir, izobardır. Kapalı bağıntı jeoidin küresel-harmonik **iskeletini** ($P_2$ payını, yani $f$'i) verir; jeoidin üzerindeki dalgalanmalar — Hindistan güneyindeki $-106$ m'lik çukur, Yeni Gine'deki $+85$ m'lik tümsek — ihlal değil, **alanın kendi engebesidir**: yerel kaynak anomalileri (manto yoğunluk yapıları) izobarı yerel olarak çukurlaştırır ve okyanus yüzeyi o engebeli izobarı ~$\pm1$ m dinamik topografya payıyla izler. Yani Dünya, denge yasasını iki ölçekte birden doğrular: küresel iskelette $+\%0{,}014$ (aşağıda), yerel engebede metre düzeyi izleme.

### Sekiz gövdede sınav

Girdilerin tamamı ölçümdür ($a$, $\mathcal{G}M$, $\omega$, $J_2$, $J_4$); serbest parametre yoktur.

| Gövde | $q$ | $f_{izobar}$ | $f_{gözlenen}$ | Sapma |
|---|---|---|---|---|
| **Dünya** | $3{,}4614\times10^{-3}$ | $3{,}35327\times10^{-3}$ | $3{,}35281\times10^{-3}$ | **+%0,014** |
| **Jüpiter** | $8{,}9196\times10^{-2}$ | $6{,}4923\times10^{-2}$ | $6{,}4874\times10^{-2}$ | **+%0,08** |
| **Satürn** (sismoloji dönemiyle) | $1{,}5763\times10^{-1}$ | $9{,}7872\times10^{-2}$ | $9{,}7963\times10^{-2}$ | **−%0,09** |
| **Güneş** (Carrington) | $2{,}0831\times10^{-5}$ | $1{,}0745\times10^{-5}$ | $1{,}100\times10^{-5}$ | **−%2,3** (ölçüm ±%5) |
| Neptün | $2{,}6078\times10^{-2}$ | $1{,}7991\times10^{-2}$ | $1{,}7081\times10^{-2}$ | +%5,3 (gözlem ±%7) |
| Mars | $4{,}5953\times10^{-3}$ | $5{,}2263\times10^{-3}$ | $5{,}888\times10^{-3}$ (yüzey) | −%11,2 → **Tharsis** |
| Uranüs (17,24 sa ile) | $2{,}9535\times10^{-2}$ | $1{,}9828\times10^{-2}$ | $2{,}2927\times10^{-2}$ | −%13,5 → **açık kalem** |
| *(Merkür, Venüs)* | — | — | — | figür ekseni devretmiştir (11.2.8) |

Satırlar üç sınıfa ayrılır ve her sınıf ayrı bir şey öğretir.

**(a) Denge yasası tutan gövdeler — Dünya, Jüpiter, Satürn, Güneş, Neptün.** İlk üçünde uyum ölçüm hassasiyeti düzeyindedir (binde 1'in altı). Dünya'nın %0,42'lik "hidrostatik fazlası" tabloda görünmez, çünkü o kalem alanın kaynağında yaşar ve ölçülen $J_2$'nin içindedir — izobar okuması onu otomatik taşır. Neptün'ün +%5,3'ü gözlem hatasının ($b$ yarıçapında ±30 km → $f$'te ±%7) içindedir; 1-bar seviyesini ±400 m/s'lik bölgesel rüzgârlar da biçimlendirir.

**(b) Yüzeyi izobarda olmayan gövde — Mars.** Yüzey figürü öngörünün %12,7 üzerindedir ve fark bir teori hatası değil, **ölçülmüş topografyadır**: Tharsis platosu. Teorinin diliyle: kafes rijitliği (U2) maddeyi izobara oturmak zorunda bırakmaz; izobar yalnız *akışkan davranan* gövdelerde figürü dikte eder. Mars, denge yasasının değil **kabuk mukavemetinin** sınavıdır ve her iki teoride de aynı kaleme yazılır. (Jeoit — areoid — düzeyinde bağıntı sağlanır; fakat areoid alandan türetildiği için bağımsız sınav sayılmaz ve tabloya konmaz.)

**(c) Girdisi kusurlu gövde — Uranüs.** −%13,5'lik sapma bağıntıya değil girdiye aittir: 17,24 saat, Voyager'ın **manyetosfer** ölçümüdür ve manyetosfer dönemlerinin iç dönmeyi temsil etmediği Satürn'de kanıtlanmıştır (aşağıda). Bağıntı tersine çevrilirse Uranüs'ün iç dönme dönemi $f$'in ±1σ bandıyla **15,6–16,0 saat** çıkar; şekil+rüzgâr modellemeleri de bağımsız olarak ~16,6 saate işaret eder. Sorun her figür teorisinde aynıdır — standart hidrostatik model de 17,24 saatle aynı %13'ü ıskalar. Uranüs bu bölümün **teoriden bağımsız açık kalemidir**; çözüm yeni bir görevin dönem ölçümündedir, teoride değil.

### Satürn: bağıntının tersine çevrilmesi — saklı dönemin öngörüsü

Satürn'ün iç dönme dönemi doğrudan ölçülemez: gövde bulutlarla örtülüdür ve manyetik ekseni dönme eksenine neredeyse tam oturduğundan manyetosfer sinyali güvenilmez — Voyager 10ˢ 39ᵈ 22ˢⁿ vermişti, bu "dönem" Cassini boyunca %1 kaydı. O hâlde bağıntıdaki üç gözlenirden ($f$, $J_2$, $q$) ikisi ölçülüp üçüncüsü öngörülür:

$$q=2\Bigl(f-\tfrac32J_2-3J_2f+f^2-\tfrac58J_4\Bigr)=0{,}15784\;\;\Rightarrow\;\;P=\frac{2\pi}{\sqrt{q\,\mathcal{G}M/a^3}}=\textbf{10ˢ 33ᵈ 13ˢⁿ}\;(\pm\sim2\text{ dk kesme payı})$$

Bağımsız ölçüm: Cassini, C halkası dalgalarının gövdenin iç titreşimlerince sürüldüğünü kullanarak — **halka sismolojisi** — iç dönemi $10ˢ\,33ᵈ\,38ˢⁿ\;(+1ᵈ52ˢⁿ/-1ᵈ19ˢⁿ)$ ölçtü. İki değer 25 saniye içinde örtüşür; her ikisinin bandı ~2 dakikadır. Voyager'ın manyetosfer dönemi kullanılsaydı $f$ öngörüsü −%1,35 sapardı — tablodaki −%0,09, doğru dönemin doğrulanmasıyla birlikte gelir. İzobar okuması burada yalnız figürü *açıklamaz*; ölçülemeyen bir niceliği *öngörüp bağımsız yöntemle doğrulatır*. Bölümün en güçlü tek sonucu budur.

### Güneş: nokta-kütle ucunun sınavı

Güneş'te $\tfrac32J_2=3{,}3\times10^{-7}$, $f$'in yalnız %3'üdür — kütle merkezde o kadar yoğunlaşmıştır ki gövde figür açısından nokta-kütle limitine ($f=q/2$) oturur. Ölçülen $J_2=2{,}2\times10^{-7}$ ile bağıntı $f=1{,}0745\times10^{-5}$ verir; gözlem $1{,}10\times10^{-5}\pm\%5$ → sapma **−%2,3, ölçüm hatasının içinde.** Kalan işaretli pay da anlaşılırdır: Güneş diferansiyel döner ve $q$ hangi dönemle kurulursa bir bant oluşur — Carrington dönemi (25,38 gün) $-\%2{,}3$, ekvatoral yüzey dönemi (24,47 gün) $+\%4{,}9$ verir; **gözlenen değer bandın içindedir.** Güneş açık kalem değildir; tersine, iç-yapı yaklaşımlarının giremediği $\lambda=0{,}070$ bölgesinde izobar okumasının çalıştığını gösteren uç sınavdır.

### Darwin–Radau neden ana yöntem değildir

Standart pratiğin aracı, eylemsizlik çarpanı $\lambda=I/MR^2$ üzerinden kurulan Darwin–Radau interpolasyonudur: $f/q=\tfrac52\bigl[1+\tfrac{25}{4}(1-\tfrac32\lambda)^2\bigr]^{-1}$. Dünya'da ($\lambda=0{,}3307$) $-\%0{,}2$ ile iyi çalışır; ama üç yapısal kusuru vardır ve üçü de izobar okumasında yoktur:

| Kusur | Darwin–Radau | İzobar okuması |
|---|---|---|
| Nokta-kütle limiti | $f/q\to0{,}3448$ — kesin değerin **%31 altı**; $\lambda\lesssim0{,}2$'de (tüm yıldızlar) kullanılamaz | $f/q\to0{,}500$, kesin ✓ |
| Girdi kalitesi | $\lambda$ yalnız Dünya/Mars/Ay'da bağımsız ölçülür; gaz devlerinde alan verisine ayarlı **model çıktısıdır** — "öngörü" saymak dolaşık akıl yürütmedir | tüm girdiler doğrudan ölçüm |
| Teoriye uygunluk | figürü kaynak modeline bağlar | figürü **alanın kendisinden** okur — teorinin tezi budur |

Aynı veriyle iki yöntemin sapmaları yan yana (DR / izobar): Dünya $-\%0{,}2$ / $+\%0{,}014$ · Jüpiter $+\%1{,}3$ / $+\%0{,}08$ · Satürn $+\%0{,}5$ / $-\%0{,}09$ · Güneş $-\%21{,}2$ / $-\%2{,}3$ · Neptün $+\%3{,}5$ / $+\%5{,}3$ (ikisi de gözlem bandı içinde; DR'ninki dolaşık girdiyle) · Uranüs'ü DR hiç hesaplayamaz — $\lambda$'sı ölçülmemiştir. DR bu bölümde yalnız çapraz-denetim aracı olarak anılır.

---

## 11.2.7 Multipol Muhasebesi: Kim Ayrıştırılabilir?

İzobar sınavı (11.2.6) **kaynağa kördür**: ölçülen $J_2$/$J_4$'ü kim üretmiş olursa olsun denge yasasını sınar. Kaynakları ayırmak ayrı bir muhasebedir, ve bir kuvvetin figüre katkı vermesi ile o katkının **ölçüde ayırt edilebilmesi** farklı şeylerdir. Sınav 1'in (6.6.2) multipol ayrıştırması ayrımı keskin koyar:

| Öğe | Ürettiği harmonikler | Ayrık imza? |
|---|---|---|
| Merkezkaç | saf $P_2$ | — (referans) |
| **F5** | **saf $P_2$** | **Yok** — merkezkaçla dejenere |
| **F4** | $P_2,\,P_4,\,P_6$ | **Var** — $J_4$ kanalı |

**F5'in basıklıktaki etkisi ölçüde sıfıra düşer** — sebebi genliğinin küçüklüğünden önce **dejenerasyondur**: F5, merkezkaç potansiyelinin sabit bir çarpanla yeniden ölçeklenmesine denktir. Gezegeni farklı bir şekle sokmaz; yalnızca *biraz daha hızlı dönüyormuş gibi* gösterir. $J_4$ ya da $J_6$'da aranacak ayrı bir F5 imzası **yoktur**; katkısı ne olursa olsun fite soğurulur. (Buradaki tuzak, kuvvet profilleri farklı görünüyor diye imzayı $J_4$'te aramaktır — farklı kuvvet profili, farklı multipol içeriği demek değildir.)

**Ayrıştırılabilir imzayı taşıyan kuvvet F4'tür.** Merkezkaç $J_4$'e birinci mertebede hiç katkı vermez, F4 verir — boş kanalda zayıf kuvvet görünür olur. Dünya için indüklenen $J_4$ payı **%4–8** mertebesindedir ve **işareti doğrudur**: gözlenen $J_4$, hidrostatik modellerin verdiğinden daha derindir ve F4 tam o yönde çalışır. Bu, sınav programının olumsuz olmayan ilk sonucudur — "geçilmiş sınav" değil, "teorinin öngörüsü önemli olacak büyüklükte" durumu; dürüst sınırları (hidrostatik referansın ~%10 belirsizliği, hidrostatik-olmayan manto katkısı) 6.6.2'dedir. İzobar sınavıyla çatışma yoktur: $J_4$'ün $f$'e girişi $\tfrac58J_4$ terimiyledir ve F4'ün %4–8'lik payı $f$'i ancak ~%0,005 oynatır — 11.2.6'nın tablosu bu ayrıştırmaya duyarsızdır.

> **Bölüm başlığı için sonuç.** Basıklığın gözlemsel imzasını taşıyan kuvvet **F5 değil F4'tür.** F5'in rolü figürü şişirmek değil, **düzlemi tanımlamaktır** (11.2.4).

### $J_4$ öngörüsü — çok-cisimli sınav

F4'ün beslendiği hız, deplasmanı yaratan **bağıl** dönüştür (M-38 R1): $\omega_{gövde}-\Omega_{ortam}$. $\Omega_{ortam}=\xi\,\omega$ ve $\xi\le3\times10^{-7}$ ile

$$F_4\;\propto\;\omega^2(1-\xi)^2=\omega^2\bigl[1-O(10^{-7})\bigr]$$

yani F4, M-22 ile aynı $\omega$'yı yedi hane hassasiyetle izler. F5'te $\omega$ ve $R$'yi sadeleştiren mekanizma burada da işlediğinden (11.2.5'in korunan sonucu) F4'ün merkezkaça oranı gövdeden bağımsız bir sabittir. Öngörü bu yüzden $J_4$'ün kendisinde değil, **$J_4/J_2$'de** yazılmalıdır:

$$\boxed{\;\left(\frac{\Delta J_4}{J_2}\right)_{F4}=\text{gövdeden bağımsız sabit}\;}$$

Ayrım önemlidir, çünkü $J_4/J_2$ gövdeden gövdeye **27 kat** değişir: Dünya $-1{,}50\times10^{-3}$, Jüpiter $-3{,}99\times10^{-2}$, Satürn $-5{,}74\times10^{-2}$. Dünya'nın ölçülen payı (%4–8) sabiti verir: $\Delta J_4/J_2=6{,}0\times10^{-5}$–$1{,}2\times10^{-4}$. Taşındığında:

| Gövde | Öngörülen $\Delta J_4$ | Kendi $J_4$'ünün yüzdesi |
|---|---|---|
| **Jüpiter** (Juno) | $8{,}8\times10^{-7}$–$1{,}8\times10^{-6}$ | **%0,15–0,30** |
| **Satürn** (Cassini) | $9{,}8\times10^{-7}$–$2{,}0\times10^{-6}$ | **%0,10–0,21** |

Gaz devlerinde beklenen sapma Dünya'nınkinden mertebelerce küçüktür; "her gövdede %4–8" beklentisi yanlış olurdu ve öngörünün doğru biçimi ancak $J_4/J_2$ üzerinden görünür. Ölçüm hassasiyeti fazlasıyla yeter (Juno $J_4$'ü $\sim10^{-8}$, yani %0,002 düzeyinde verir) — **sınavın sınırlayıcı belirsizliği ölçüm değil, hidrostatik referans modelidir.**

**Ay tutarlılık kontrolü.** M-38'in gövde rejimi (R1) Ay verisiyle sınırlıdır: $\varepsilon(r_{Ay})<2\times10^{-5}$ ve $\varepsilon\propto r$ ile yüzeyde $\varepsilon(R_\oplus)<3{,}3\times10^{-7}$. $J_4=1{,}62\times10^{-6}$ ve $c_4/c_2=27/50$ ile: F4'ün $P_2$ payı merkezkaça oranla $2{,}5\,\varepsilon/q<2{,}40\times10^{-4}$, buradan $\Delta J_2<2{,}59\times10^{-7}$ ve $\Delta J_4<1{,}40\times10^{-7}$ — F4'e $J_4$'ün en çok **%8,65'i** kadar yer vardır; iddia %4–8'dir. **Geçiyor, fakat marj alt uçta 2,2 kat, üst uçta yalnız 1,08 kattır** — sınırın %92'si tüketilir. Üstelik hesap $n=2$ ile $n=4$ tepki (Love) çarpanlarını eşit alır; gerçekçi gövdelerde $k_4<k_2$ olduğundan gerçek marj daha incedir. İki bağımsız verinin (Ay apsidal presesyonu ↔ Dünya $J_4$'ü) aynı katsayıyı kıstırdığı gerçek bir sınavdır ve üç sonuçtan biri doğrudur: **(i)** F4'ün payı iddianın alt ucundadır, **(ii)** Ay sınırı fazla muhafazakârdır, ya da **(iii)** ikisi çatışır ve M-38'in genlik ataması ($A_4$, rozet `[A]`) yeniden hesaplanmalıdır.

---

## 11.2.8 Merkür ve Venüs: Figür Ekseninin Devri

Bu iki gövde tablolardan çıkarılmıştır ve sebep *"$q$ çok küçük"* değildir — üç katmanlıdır ve üçü de teorinin kendi mekanizmasından çıkar.

**(i) Kavrama dönüşü yutmuştur.** İkisi de M-24'ün bastırılmış sınıfındadır: $g_{Merkür}=0{,}98$, $g_{Venüs}=1{,}00$ (Kısım 3 §3.4.4). Girdap rekabeti serbest dönüş ifadesinin neredeyse tamamını soğurmuştur ve zincir zorunlu akar: kavrama $\Rightarrow\omega\!\downarrow\Rightarrow q\!\downarrow\Rightarrow$ F4, F5 $\propto\omega^2\!\downarrow$. Sayılar: $q_{Merkür}=1{,}01\times10^{-6}$, $q_{Venüs}=6{,}1\times10^{-8}$ — Dünya'nın $1/3400$'ü ve $1/57.000$'i. Dönme kaynaklı figür pratikte yoktur; onunla birlikte F4/F5 de yoktur.

**(ii) Figürü belirleyen alan gelgit eksenine devreder.** Dönme terimi çökünce geriye Güneş'in diferansiyel sıkıştırması kalır (§11.1; teoride gelgit çekim değil, basınç alanının ikinci türevidir). Boyutsuz gelgit sürücüsü $t=(M_\odot/M)(R/a)^3$:

| | $q$ (dönme ekseni) | $t$ (gelgit ekseni) | $t/q$ |
|---|---|---|---|
| Merkür | $1{,}01\times10^{-6}$ | $4{,}51\times10^{-7}$ | **0,445** |
| Venüs | $6{,}11\times10^{-8}$ | $7{,}16\times10^{-8}$ | **1,17** |
| *(Dünya)* | $3{,}46\times10^{-3}$ | $2{,}58\times10^{-8}$ | $7{,}5\times10^{-6}$ |

İki sayı skaler gibi toplanamaz — §11.1'in uyarısı bağlayıcıdır: *gelgit ekseni ≠ dönme ekseni.* F4/F5 dönme eksenine kilitlidir (M-38/M-39, R1), gelgit Güneş–gövde doğrultusundadır; iki farklı doğrultuda iki $P_2$ yapısı tensörel toplanmak zorundadır. Üstelik teorinin gelgit tensörü Newton'unkiyle özdeş değildir: F4 dejenerasyonu kırar (yanal özdeğer çifti $-(1{+}\beta)$ ↔ $-1$), F5 izi ihlal eder ($\nabla\!\cdot\!\vec a_5=-2a_5/r$) — §11.1'in ayırt edici imzası buradadır.

**(iii) Kalıcı mı gezici mi — spin-yörünge durumu belirler.** Gelgit ekseni Güneş günü başına bir tur döner; hızlı dönen gövdede kalıcı figüre giremez, gezici deformasyon kalır:

| Gövde | Güneş günü | Spin-yörünge | Kalıcı gelgit bileşeni |
|---|---|---|---|
| Altı serbest gezegen | 0,4–1,0 gün | serbest | **yok** ($t/q\le10^{-6}$, ayrıca gezici) |
| Venüs | 116,8 gün | asenkron, retrograd | **yok** — ömür boyu $\sim1{,}4\times10^{10}$ çevrim, gezici |
| **Merkür** | 175,9 gün | **3:2 rezonans** | **VAR** — ardışık günberilerde aynı yüz Güneş'e döner |

Merkür'ün kalıcı bileşeni teoride türetilmiş sonuçtur: M-24'ün günberi ritmi $q_{peri}(e)=\sqrt{1+e}/(1-e)^{3/2}$, $e=0{,}206$ ile $1{,}55\to3{:}2$ verir — kilidin kendisi de kalıcı bileşenin varlığı da aynı mekanizmadan gelir.

**Sonuç.** Merkür'ün ölçülen $J_2$'si hidrostatik değerin ~200 katıdır; Venüs'ün $f$'i $10^{-5}$'in altındadır ve ölçülemez. Bu iki gövde hiçbir figür teorisini sınayamaz — ama teorinin şunu söylemesi gerekir ve söyler: *bastırılmış gövdelerde figür ekseni dönmeden gelgite devreder.* Kavrama mekanizmasının bedava getirdiği nitel sonuç budur.

---

## 11.2.9 Hüküm: "Kim Kazandı?"

Evrenakı (M-22 U2 + izobar okuması) ile standart akışkan figür teorisi, basıklık ($f$) konusunda rekabet içinde değildir; Evrenakı gözlenen basıklığı ölçüm hassasiyetinde üretir ve aynı izobar cebiri standart teoride de kurulabilir. Ayrım üç yerdedir:

1. **Denge yasası: ölçüm hassasiyetinde doğrulandı.** Serbest parametresiz sonuçlar: Dünya **+%0,014**, Jüpiter **+%0,08**, Satürn **−%0,09**; Güneş (−%2,3) ve Neptün (+%5,3) kendi ölçüm hatalarının içinde. Sapan iki gövdenin ikisi de nedenini kendisi söyler: Mars'ınki ölçülmüş topografyadır (Tharsis — kabuk rijitliği izobara oturmayı zorunlu kılmaz), Uranüs'ünki girdideki manyetosfer-dönemi kusurudur ve her figür teorisinde aynıdır. F5'i bu kalemleri "düzeltmek" için kullanmak yapısal hata olurdu; F5 dejeneredir ve fite soğurulur (11.2.7).

2. **Yöntem: figür, iç yapı modelinden değil ölçülen alandan okunur.** Kazanç iki katmanlıdır. *Pratik:* Darwin–Radau'nun üç kusuru (bozuk nokta-kütle limiti, dolaşık λ girdisi, kaynak-modeline bağımlılık) izobar okumasında yoktur; üstüne Satürn'ün saklı dönemi öngörülüp halka sismolojisiyle 25 saniye içinde doğrulanmıştır. *Dürüstlük:* bu cebir potansiyel teorisinin malıdır — standart fizikçi de aynı hesabı yapabilir; burada yenilen "standart fizik" değil, **iç-yapı-modeline-bağımlı yaklaşım alışkanlığıdır.** Teori bu yöntemi seçmek zorundaydı, çünkü kendi tezi budur: figür, kaynak modelinin değil, fiilen ölçülen alanın izobarıdır. Bu ayrım yapılmazsa karşılaştırma standart fiziğe haksızlık eder ve hakem denetiminde ilk düşecek kalem olur.

3. **Kavramsal zemin: Evrenakı kazandı.** Standart model gözlemi doğru hesaplar ama bunu "sanal kuvvet" dediği merkezkaç üzerinden yapar. Evrenakı aynı dengeyi uzay akışkanının **gerçek ataletiyle** (M-22) kurar; $J_2$ onun için soyut bir katsayı değil, F1 basınç alanının ölçülmüş dört-kutup biçimidir — uydu yörüngeleri bu alanın içinde uçtuğu için izobar okuması teoride bir tanım gereği değil, bir **mekanizma sonucudur.**

> **Sonuç:** Gezegen basıklıkları ($f$ ve $J_2$) iki teoriyi ayırt etmez; Evrenakı bunları ölçüm hassasiyetinde üretir. Ayırt edici imza $J_2$'de değil, F4'ün birinci mertebede yarattığı $J_4$ anomalilerindedir (11.2.7) — ve teoriden bağımsız tek açık kalem Uranüs'ün iç dönme dönemidir (öngörü: 15,6–16,0 saat; sınayacak olan gelecek görevin ölçümüdür).
