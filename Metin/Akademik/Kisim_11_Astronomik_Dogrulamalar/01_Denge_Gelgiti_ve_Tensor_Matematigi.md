# 11.1 Diferansiyel Sıkıştırma: Gelgit Tensörü ve Denge Gelgiti

Kısım 3.9'da okyanusların hareketini, uzaydan gelen görünmez bir "çekme" kuvvetiyle değil, Evrenakı akıntısının yarattığı **asimetrik yanal sıkıştırmayla (squeeze)** açıklamıştık. Bu bölüm o mekanizmayı matematiğe taşır. Cebirin biçimi tanıdıktır — bir alanın ikinci türevleri, yani bir Hessian; teorinin katkısı yeni bir matematik icat etmek değil, o türevin **neyin** türevi olduğunu ve gövde üzerinde neyi yeniden dağıttığını adlandırmaktır: gerçek bir taban sıkışmanın (Kuvvet 2), yönlü bir gradyanla (Kuvvet 1) yeniden dağıtılması.

Dünya, Evrenakı denizinin içinde zaten her yönden sıkışmış hâldedir: bu **taban sıkışma Kuvvet 2**'dir (Sıkıştırma, Ek M-36) ve gövdenin her noktasına — yakın yüz, uzak yüz, yanlar, fark etmez — **yönden bağımsız** etki eder: bir yön seçmez, dolayısıyla tek başına hiçbir yönü ayrıcalıklı kılamaz. Ay'ın **Kuvvet 1**'i (kütle-itim, Ek M-35) ise yönlüdür: Dünya'nın Ay'a bakan ve bakmayan yüzlerinde farklı büyüklüktedir. Bu yönlü fark, gelgit ekseninde tabandan **çıkarılır** (sıkışma orada gevşer, madde kabarır) ve gelgit eksenine dik yönlerde tabana **eklenir** (sıkışma orada pekişir, madde içeri iter). Evrenakı, kuşaktan eksene doğru akar — sıkışma nedendir, kabarma sonuçtur; aynı fiziksel anlatı 3.9.2'de kurulan hikâyenin ta kendisidir, burada yalnız sayıya dökülür.

> **Bu bölümün sözü — peşinen dürüst kayıt.** Türetimin ürettiği her sayı ($1/r^3$ yasası, $(+2,-1,-1)$ oranı, %46, 0,535 m) klasik gelgit kuramınınkiyle **birebir aynıdır** — çünkü nihai büyüklük yalnız Kuvvet 1'in gradyanına bağlıdır. Kuvvet 2 hesaptan **iptal olur**, hiç ölçülmesi gerekmez ve sıfır yeni parametre ekler; üstelik bu iptal varsayılmaz, 11.1.3'te açısal mertebe ($\ell$) muhasebesiyle türetilir ve tabanın ne büyüklüğüne ne radyal yasasına bağlıdır. Aynı olmayan şey sayının kendisi değil, ona nasıl varıldığıdır: burada bir potansiyelin ikinci türevi soyut bir alan özelliği olarak değil, gerçek bir taban sıkışmanın (Kuvvet 2) yönlü bir gradyanla (Kuvvet 1) yeniden dağıtılması olarak okunur — iki adı konmuş kuvvet, iki ayrı mekanizma. Bu özdeşliğin de sessiz bir koşulu vardır: **kaynağın kilitli olması.** Ay kilitlidir — Dünya'ya göre hiç dönmez; Güneş değildir. Teoride Dünya'ya göre dönen bir kaynağın gelgit tensörü kilitli olanınkinden **yapıca** farklıdır: yanal dejenerasyon kırılır (F4'ün silindirik geometrisi) ve boşluktaki iz sıfır olmaktan çıkar (F5'in meridyenel geometrisi). Newton'da ise kaynağın dönme durumu dış alana hiç girmez ve boşlukta iz $\nabla^2\Phi=0$ gereği **tam olarak sıfırdır.** Dünya iki kaynağı da aynı anda ve aynı aletlerle ölçtüğü için bu, hâlihazırda işleyen **doğal bir diferansiyel deneydir** — kilitli Ay kontrol, dönen Güneş numunedir. Kuruluşu 11.1.8'dedir.
>
> Sınavın **yapısı** türetilmiştir ve parametresizdir; **genliği** öngörülmemiştir ($\kappa_5$ serbest kalemdir). Bölüm bunu bir "şu sayı çıkmalı" öngörüsü olarak değil, iki yönlü keskin bir sınav olarak sunar. Şişkinlik kayması (11.1.9) bu sınava dâhil değildir: kaynağı atomik sürtünmedir ve hesabı standart kuramla ortaktır.

---

## 11.1.1 Notasyon ve Varsayımlar

**Notasyon**

| Sembol | Anlam |
|---|---|
| $M$ | Gelgiti yaratan kaynağın kütlesi (Ay veya Güneş) |
| $r$ | Kaynak ile gövde merkezi arası uzaklık |
| $b$ | Gövde yarıçapı (Dünya), $b\ll r$ |
| $\vec\xi$ | Gövde merkezinden ölçülen iç konum, $\lvert\xi\rvert\le b$ |
| **gelgit ekseni** | Gövde merkezini kaynağa bağlayan doğrultu (Dünya–Ay doğrultusu). **Dünya'nın dönme ekseni değildir** — aşağıdaki uyarıya bkz. |
| $\psi$ | $\vec\xi$ ile **gelgit ekseni** arasındaki açı |
| $\Phi$ | İtim potansiyeli, $\Phi\equiv(P-P_0)/\rho_n$ (Kuvvet 1'e ait) |
| $a_2$ | Kuvvet 2'nin taban sıkışma büyüklüğü; yönden bağımsızdır, $r$'ye bağlı olabilir (ivme boyutunda) |
| $\Psi_T$ | Gelgit potansiyeli (ortak taşınma çıkarıldıktan sonraki artık) |
| $\zeta$ | Serbest yüzey yükseltisi (Anayasa S-27) |
| $\rho_c$ | Gövdenin ortalama kütle yoğunluğu (Dünya: $5{,}515\times10^{3}$ kg/m³) — 11.1.9'da kullanılır |
| $\ell$ | Küresel harmonik derece (yük ve tepkinin açısal mertebesi) |

**Varsayımlar**

1. **Kuvvet 1 geçerlidir:** $P(r)=P_0-\alpha M/r$, dolayısıyla $a_r=-\mathcal{G}M/r^2$ ve $\mathcal{G}=\alpha/\rho_n$ (Ek M-35).
2. **Kuvvet 2 geçerlidir:** gövdenin içinde bulunduğu yönsüz taban sıkışma $a_2$ (Ek M-36). Gövde ölçeğinde sabit olduğu **varsayılmaz**; $r$'ye bağlı olmasına izin verilir ve bu bağımlılığın şekle katkı yapmadığı 11.1.3'te türetilir. Büyüklüğü de radyal yasası da bu bölümde hiç sabitlenmez.
3. **Uzanımlı gövde:** $b\ll r$; açılım **ivme alanında** birinci mertebede (potansiyelde ikinci mertebede) kesilir. Dünya–Ay için $b/r\approx0{,}017$. Bir üst mertebe yalnız hata kestirimi için yazılır (11.1.3, 11.1.10).
4. **Akı korunumu:** Kaynaktan uzakta Kuvvet 1'in deplasman akısı ne yaratılır ne yok edilir. 11.1.4'te nicel biçime sokulur.
5. **Evrensel $\rho_n$:** Nükleon öz yoğunluğu bileşimden bağımsızdır ($2{,}7\times10^{17}$ kg/m³). Kuvvet 1 bu yüzden gövdenin *her* nükleonuna aynı ivmeyi verir.
6. **Kaynak, Dünya'ya göre dönmemektedir:** Ay gelgit kilitlidir; Dünya–Ay doğrultusuna göre dönme hızı **tam olarak sıfırdır** ve makro-girdabı bastırılmıştır (Bkz. 3.9.1). Dolayısıyla Dünya'ya yalnız pompa kolu (Kuvvet 1 + Kuvvet 2) etki eder; $\omega_1$ kökenli kuvvetler devrede değildir. Buradaki "dönmeme" bir mutlak hız iddiası değildir — ayrımın tam ifadesi 11.1.8'dedir.

---

## 11.1.2 Kuvvet Envanteri: Kilitli Kaynak Neden Yalnız Pompa Kolunu Uygular?

Postülat 9'un beş hidrodinamik kuvveti iki köke ayrılır:

| Kol | Kuvvetler | Kilitli kaynakta |
|---|---|---|
| $\omega_2$ — **pompa** (boyutsal salınım) | **1** Radyal kütle-itim · **2** Sıkıştırma | **açık** |
| $\omega_1$ — **dönüş** (makro-vorteks) | 3 Vorteks sürüklenmesi · 4 Eksenel itim · 5 Yanal itim | **kapalı** |

Bu ayrım gelgit probleminde belirleyicidir, çünkü **Ay Dünya'ya göre dönmemektedir.** Gelgit kilidi, gövdenin dönüşünü yörünge dolaşımıyla aynı faza oturtur; Dünya–Ay doğrultusuna göre bağımsız bir sirkülasyon kalmaz ve kendi makro-girdabı bastırılır (Bkz. 3.9.1 ve 3.4.4 — girdap rekabeti). Dönüş kolu kapalı olan bir kaynak, Dünya'ya vorteks sürüklenmesi, eksenel itim veya yanal itim uygulayamaz — bu üç kuvvetin taşıyıcısı yoktur.

Geriye yalnız pompa kolu kalır — **iki kuvvet, tek gradyan.** Kuvvet 2 yönsüz bir taban sıkışmadır ve tek başına hiçbir şekil bozulması üretemez: yönden bağımsız bir büyüklük, gövdenin hiçbir noktasını diğerinden ayırt edemez. Uzaklıkla değişmesi de sonucu değiştirmez — radyal eğiminin taşıdığı pay $\ell=1$'dir, yani gövdeyi kaydırır, ovalleştirmez; ikisi de 11.1.3'te **varsayılmadan türetilir**. Gelgidin **yönünü ve büyüklüğünü** bu yüzden tümüyle Kuvvet 1'in gradyanı belirler; Kuvvet 2'nin rolü, bu gradyanın üzerine bindiği gerçek bir taban sağlamaktır — bir hikâye değil, gövdenin zaten içinde bulunduğu fiziksel bir sıkışma hâlidir. Sayısal sonuç **tek bir gradyana iner**, fakat mekanizma gerçek anlamda **ikilidir.**

Bu bir kısıt değil, türetimin temizliğidir: tensörün $(+2,-1,-1)$ yapısı $\omega_1$ kökenli hiçbir terimle karışmadan saf çıkar ve hesaba tek bir serbest katsayı girmez — Kuvvet 2'nin ne taban değeri ne radyal yasası dâhil.

> [!WARNING]
> **Karıştırılmaması gereken iki "yanal".** Bölüm 11.2'nin **Yanal İtimi** (Kuvvet 5, Ek M-39) ile bu bölümün **yanal sıkıştırması** aynı şey değildir:
>
> | | 11.1 — yanal sıkıştırma | 11.2 — Yanal İtim (Kuvvet 5) |
> |---|---|---|
> | Kök | $\omega_2$, pompa | $\omega_1$, dönüş |
> | Kaynağı | *uzaktaki* kütlenin alanı | gövdenin *kendi* dönüşü |
> | Yasa | $T_\perp=-\mathcal{G}M/r^3$ | $f_{yanal}\propto\kappa_5\rho v_e^2\sin2\theta$ |
> | Bileşim | bağımsız | $\phi$'ye bağlı |
> | Parametre | yok | $\kappa_5$ (serbest) |
>
> İkisi aynı gövdede toplanabilir, fakat kökenleri ve yasaları ayrıdır.

---

## 11.1.3 İki Kuvvetin Üst Üste Binmesi: Taban ve Gradyan

### Kuvvet 2 — yönsüz taban

Kuvvet 1 ile Kuvvet 2 aynı ω2 (pompa/boyutsal salınım) kanalından beslenir (Ek M-36), fakat tek bir basınç alanının iki ayrı yüzüdür: **Kuvvet 1 alanın eğimidir** ve yönlüdür; **Kuvvet 2 aynı alanın düzeyidir** ve yönsüzdür — gövdeyi bir noktada her yönden aynı büyüklükte sıkan bir hâl, $a_2$.

Tek başına yönsüz bir alan **hiçbir şekil bozulması üretemez** — bu bir eksik değil, geometrinin zorunlu sonucudur: yönden bağımsız bir büyüklük gövdenin hiçbir noktasını diğerinden ayırt edemez, gövdeyi yalnız hacimce sıkıştırır, ovalleştirmez.

#### Tabanın uzaklıkla değişmesi neden gelgit terimi doğurmaz

Yukarıdaki cümle, $a_2$'nin gövde üzerinde sabit olduğu peşinen kabul edilirse boş bir totolojidir. Asıl soru şudur: **taban, kaynağa uzaklıkla değişiyorsa ne olur?** Kaynağın kendi payını taşıyan bir sıkışmanın $r$'den bağımsız olması beklenemez; ve eğer $da_2/dr\ne0$ ise yakın yüz uzak yüzden farklı sıkışır, bu fark da $O(b/r)$ mertebesindedir — yani **Kuvvet 1'in gelgit teriminin tam olarak aynı mertebesi.** Öyleyse "taban iptal olur" iddiası kendiliğinden doğru değildir; türetilmesi gerekir. Bölümün geri kalanı buna dayandığı için soru burada, $a_2$ hakkında hiçbir kabul yapılmadan kapatılır.

Tabanı gövde üzerinde açalım ($\xi_\parallel\equiv\vec\xi\cdot\hat r=\xi\cos\psi$; $a_2'\equiv da_2/dr$):

$$a_2(\vec r+\vec\xi) \;=\; \underbrace{a_2(r)}_{\ell=0} \;+\; \underbrace{a_2'(r)\,\xi\cos\psi}_{\ell=1} \;+\; \underbrace{\tfrac12 a_2''(r)\,\xi^2\cos^2\psi}_{\ell=0\,\oplus\,\ell=2} \;+\; O(\xi^3)$$

Şekle katkı, terimlerin büyüklüğü tarafından değil **açısal mertebeleri ($\ell$)** tarafından belirlenir. Gelgit bir $\ell=2$ olgusudur; bir yükün gelgide karışabilmesi için $P_2(\cos\psi)$ ile örtüşmesi gerekir.

**$\ell=0$ — hacim, şekil değil.** İzotropik terim gövdenin hiçbir noktasını diğerinden ayırt edemez. Sıkışabilir bir gövdede hacmi bir miktar küçültür, şeklini değiştirmez.

**$\ell=1$ — yer değiştirme, şekil değil.** Kapanışın taşıyıcı adımı budur. Doğrusal terim $\cos\psi$ ile gider, yani **tektir**: gelgit ekseninin iki ucunda eşit büyüklükte ve zıt işaretlidir, eksen çifti üzerindeki ortalaması sıfırdır ve $P_2$ ile örtüşmesi özdeş olarak sıfırdır ($\int_{-1}^{1}P_1P_2\,d\mu=0$). Serbest bir gövdeye uygulanan $\ell=1$ yükünün denge tepkisi **rijit bir yer değiştirmedir** — küresel bir yüzeyin $\ell=1$ deformasyonu, tanımı gereği o kürenin ötelenmesidir. Fiziksel okuması da doğrudandır: yakın yüzü uzak yüzden daha sert sıkan bir taban, gövdeye **net bir kuvvet** uygular; o kuvvet yörünge hareketine yazılır, şekle değil.

Bu, aşağıda **Kritik adım**'da Kuvvet 1'in ortak bileşeni için kurulacak teoremin aynısıdır: orada her noktaya eşit bir ivme gövdeyi *taşıyordu*, burada tek bir yük gövdeyi *kaydırıyor*; ikisi de deforme etmiyor. Ve belirleyici olan şudur — bu sonuç $a_2$'nin **ne büyüklüğüne ne de radyal yasasına** bağlıdır. Taban ne kadar güçlü olursa olsun, nasıl bir $r$ bağımlılığı taşırsa taşısın, birinci mertebe artığının gelgit tensörüne katkısı **özdeş olarak sıfırdır.**

**$\ell=2$ — tek gerçek katkı, ve bir mertebe daha küçük.** Şekle karışabilecek yegâne terim ikinci türevdir. $\cos^2\psi=\tfrac13+\tfrac23P_2(\cos\psi)$ ayrıştırmasıyla $\ell=2$ payı $\tfrac13a_2''\,\xi^2P_2$ olur. Kuşak–eksen farkı cinsinden Kuvvet 1'in gelgit terimiyle kıyaslanırsa ($a_1\equiv\mathcal{G}M/r^2$):

$$\frac{\bigl|\text{Kuvvet 2'nin }\ell{=}2\text{ payı}\bigr|}{\bigl|\text{Kuvvet 1'in gelgit terimi}\bigr|} \;=\; \frac{a_2''b^{2}/2}{3\mathcal{G}Mb/r^{3}} \;=\; \frac{a_2''\,r^{2}}{6\,a_1}\cdot\frac{b}{r}$$

$a_2\propto r^{-n}$ için $a_2''r^2=n(n{+}1)a_2$ olduğundan oran $\frac{n(n+1)}{6}\cdot\frac{a_2}{a_1}\cdot\frac{b}{r}$'dir. Dünya–Ay'da $b/r=0{,}0166$ ve kaynak payı $a_2\sim a_1$ mertebesinde kaldığı sürece oran $n=1$ için $\%0{,}6$, $n=2$ için $\%1{,}7$ çıkar — yani **11.1.10'da zaten ilan edilmiş olan $O(\xi^2)$ kesme hatasının ($\sim\%2$) içindedir**, onun dışına taşan ayrı bir kalem değildir.

#### Aynı sonucun ikinci okunuşu: üçüncü bir alan yoktur

Yukarıdaki mertebe muhasebesi $a_2$ hakkında hiçbir şey bilmeden yürür. Teorinin kendi yapısı ise daha keskin bir şey söyler: tabanın kaynağa ait payının radyal eğimi **yeni bir kuvvet değildir.** Ek M-35'in alanında düzeyin kaynak payı $P(r)-P_0=-\alpha M/r$'dir; eğimi alınırsa

$$\frac{1}{\rho_n}\frac{d}{dr}\bigl[P(r)-P_0\bigr] \;=\; \frac{\alpha M}{\rho_n r^{2}} \;=\; \frac{\mathcal{G}M}{r^{2}} \;=\; \lvert\vec a_1\rvert$$

— **Kuvvet 1'in kendisi çıkar.** Teoride tek bir basınç alanı vardır; düzeyin eğimi ile eğimin kendisi aynı nesnedir. Tensöre ayrıca bir $da_2/dr$ kalemi eklemek bu yüzden aynı fiziği iki kez saymak olurdu. Gerekçe, 11.1.8'de Kuvvet 3 için kurulan çift-sayma gerekçesiyle aynıdır: F3'ün radyal gradyan içeriği F4'ün $\beta$'sında zaten sayıldığı için ayrıca eklenmez.

Tabanın geri kalan payı — gövdeyi çevreleyen $P_0$ arka basıncı — evrendeki bütün maddenin ω2 kolektifinin kurduğu denge düzeyidir, yerel bir kaynağa ait değildir ve Dünya–Ay ölçeğinde **gradyansızdır.** İki pay da şekle katkı yapamaz: birinin gradyanı yoktur, ötekinin gradyanı zaten hesaptadır.

**Sonuç.** $a_2$'nin ne sayısal değeri ne radyal yasası bu türetimde sabitlenir — hesaba giremeyecekleri türetildiği için gerek de yoktur. Teoriye tek gerekliliği, gövdenin gerçekten sıkışmış bir tabanda durduğunu sağlamaktır.

### Kuvvet 1 — yönlü gradyan

Kütle-itim yasası $\vec a_1=-\frac{1}{\rho_n}\nabla P$'dir. $\rho_n$ sabit olduğundan bu ifade tam bir potansiyele indirgenir:

$$\Phi \equiv \frac{P-P_0}{\rho_n} \;\Longrightarrow\; \vec a_1 = -\nabla\Phi,\qquad \Phi(r)=-\frac{\mathcal{G}M}{r}$$

Bu, standart fizikten ödünç alınmış bir kütleçekim potansiyeli **değildir**: basınç alanının nükleon öz yoğunluğuna bölünmüş hâlidir. Değeri aynı, kökeni farklıdır.

Gövde merkezi $\vec r$'de, gövde üzerindeki okyanus noktası $\vec r+\vec\xi$'dedir. İvme alanı açılır:

$$\vec a_1(\vec r+\vec\xi) = \vec a_1(\vec r) + (\vec\xi\cdot\nabla)\vec a_1 + O(\xi^2)$$

**Kritik adım.** Kuvvet 1 gövdenin her nükleonuna $\vec a_1=-\frac{1}{\rho_n}\nabla P$ ile etki eder ve $\rho_n$ evrensel olduğundan bu ivme cismin cinsine bakmaz. Alanın **ortak** bileşeni $\vec a_1(\vec r)$ böylece gövdenin her noktasını aynı miktarda ivmelendirir: gövdeyi bir bütün olarak taşır, ama deforme etmez. Bu, yukarıda Kuvvet 2 için kurulan mertebe teoreminin bu alandaki karşılığıdır — orada $\ell=0$ ve $\ell=1$ payları gövdeyi sıkıyor ya da kaydırıyordu, burada ortak ivme gövdeyi taşıyor; hiçbiri şekle karışmıyor. Okyanusları kabartan, Kuvvet 1'in bu ortak ivmeden sapan **artık kısmıdır**:

$$\boxed{\;\Delta\vec a_1(\vec\xi) \equiv \vec a_1(\vec r+\vec\xi) - \vec a_1(\vec r) = \mathsf{T}_1\,\vec\xi,\qquad (T_1)_{ij}=\frac{\partial (a_1)_i}{\partial x_j}=-\frac{1}{\rho_n}\partial_i\partial_j P\;}$$

Bu, Kuvvet 1'in kendi gradyan tensörüdür — **henüz gelgit tensörü değildir.** Gelgidi üreten, bu gradyanın Kuvvet 2'nin tabanını yerel olarak nasıl değiştirdiğidir; ilişki 11.1.4'te kurulur.

$\Delta\vec a_1$ ifadesi $\vec\xi$'de **doğrusal** olduğundan $\Delta\vec a_1(-\vec\xi)=-\Delta\vec a_1(\vec\xi)$ geçerlidir: gelgit ekseninin iki ucundaki artık ivmeler zıt yönlüdür, yani **ikisi de merkezden dışa** bakar. **Dünya'nın her iki yüzündeki — Ay'a bakan ve Ay'ın tam zıttındaki — çift okyanus şişkinliği, hiçbir ek varsayım olmadan doğrudan bu $\vec\xi\to-\vec\xi$ tekliğinden çıkar.**

> [!CAUTION]
> **Gelgit ekseni ≠ dönme ekseni.** Bu bölümde geçen her "eksen" sözcüğü, gövde merkezini kaynağa bağlayan **Dünya–Ay doğrultusunu** gösterir. Dünya'nın kendi dönme eksenini (ve dolayısıyla ekvatoru) göstermez; ikisi ne çakışıktır ne de paraleldir. Ayrım üç yüzden zorunludur:
>
> 1. **Yönelim.** Gelgit ekseni kaynağın konumuyla belirlenir; dönme ekseni gövdenin kendi mekaniğiyle. Aralarındaki açı sabit bile değildir — eksen eğikliği ve Ay'ın 5°'lik yörünge eğikliği yüzünden sürekli değişir (Bkz. 3.9.3).
> 2. **Sıkıştırma kuşağı ekvator değildir.** $-1$ özdeğerlerinin tanımladığı çembersel kuşak, **gelgit eksenine** diktir. Coğrafi ekvatorla ilgisi yoktur; ekvatorla çakıştığı anlar istisnadır, kural değil.
> 3. **Günde iki gelgitin sebebi tam olarak bu ayrımdır.** Kuşak ve şişkinlikler gelgit eksenine kilitlidir; Dünya ise kendi dönme ekseni etrafında bu yapının *altından* döner. Yeryüzündeki bir nokta her turda iki şişkinlikten de geçer — günde iki yüksek gelgit buradan gelir (ardışık iki tepe arası, Ay günü nedeniyle 12 sa 25 dk). İki eksen çakışık olsaydı şişkinlikler kutuplarda sabitlenir ve gelgit hiç dolaşmazdı.
>
> Aynı geometri, iki gelgitin neden eşit olmadığını da verir: gelgit ekseni dönme eksenine eğik olduğundan bir noktanın gün içinde geçtiği iki şişkinlik farklı enlemlerden kesilir (*günlük eşitsizlik*). Bu, standart gelgit kuramının da bilinen sonucudur; burada ek bir varsayımla değil, aynı iki-eksen geometrisinden çıkar.
>
> **Bölüm 11.2'nin ekseni ise dönme eksenidir.** Oradaki Yanal İtim ($\sin2\theta$) gövdenin kendi dönüşünden doğar ve kuşağı gerçekten ekvatordadır. İki bölümün "eksen"leri farklı nesnelerdir.

> [!NOTE]
> **Bernoulli okumasıyla uzlaştırma.** Bölüm 3.9.2 gelgiti, Ay'ın Dünya–Ay arasındaki Evrenakı akıntısını hızlandırmasına bağlar: hızın arttığı yerde iç basınç düşer (Bernoulli, 1738). Bu bölümdeki türetim ise statik $P(r)=P_0-\alpha M/r$ alanı üzerinden yürür. İkisi rakip mekanizma değil, **aynı alanın iki çerçevedeki okunuşudur.**
>
> Yukarıda kurulan taşınan çerçevede gövde ortamla birlikte gider; bağıl hız sıfırdır ve alan gövdeye göre statik görünür — tensör matematiği bu çerçevede işler. Gövdeye göre akan çerçevede ise aynı basınç yapısı, akışkanın hızlanıp yavaşlaması olarak, yani Bernoulli profili olarak okunur. İki okuma arasındaki geçiş terimi, çerçeve adımında çıkarılan ortak taşınma teriminin ta kendisidir.
>
> **Nicel sonuç tek yerden gelir:** aşağıdaki bütün sayılar statik gradyandan türetilmiştir. Bernoulli okuması mekanizmanın yerel görünümüdür, ikinci bir hesap kalemi değildir.

---

## 11.1.4 Akı Korunumu, Kuvvet 1'in Bileşenleri ve Kuvvet 2'nin Tabanının Yeniden Dağılımı

Önce Kuvvet 1'in kendi korunum yasasını nicel biçime sokalım. Ek M-35'in ortam tepkisi $\dfrac{dP}{dr}=\dfrac{C\,Nq_n}{4\pi r^2}$ idi. Kaynağı çevreleyen herhangi bir $S$ küresi üzerinden basınç gradyanı akısı:

$$\oint_S \nabla P\cdot d\vec A = \frac{C\,Nq_n}{4\pi r^2}\cdot 4\pi r^2 = C\,Nq_n = \text{sabit}$$

Akı **yarıçaptan bağımsızdır.** Diverjans teoremiyle, kaynağı içermeyen herhangi bir küresel kabukta:

$$\int_V \nabla^2 P\,dV = \oint_{S_{dış}}\!\!\nabla P\cdot d\vec A \;-\; \oint_{S_{iç}}\!\!\nabla P\cdot d\vec A = 0 \;\Longrightarrow\; \nabla^2P=0$$

Fiziksel okuma nettir: Kuvvet 1'in kaynaktan çıkan deplasman akısı yolda ne çoğalır ne eksilir. **Evrenakı yaratılmaz, yok edilmez; yalnızca yer değiştirir.** *(Bu, yalnız Kuvvet 1'in kendi akısıdır. Kuvvet 2 için ayrı bir akı hesabı gerekmez: yönsüz olduğu için tensör yapısı taşımaz, radyal değişiminin şekle katkısı ise 11.1.3'te $\ell=1$ olduğu — dolayısıyla özdeş olarak sıfır kaldığı — gösterilmiştir.)*

Bu sonucu şimdi *kullanmayacağız.* Kuvvet 1'in tensörünü, izsizliğe hiçbir yerde başvurmadan bileşen bileşen kuracak; sonra izin kendiliğinden sıfır çıktığını göreceğiz.

> **Bağımsızlık iddiası burada tartılır.** Yukarıdaki akı argümanı ile aşağıdaki bileşen hesabı **mantıksal olarak bağımsız değildir:** ikisi de $a_r\propto1/r^2$ yasasından beslenir ve küresel simetride $1/r^2$ ile $\nabla^2P=0$ matematiksel olarak eşdeğerdir. Bu yüzden "izsizlik iki bağımsız ispatla üretildi" demek yanlış olur; doğru ifade şudur: **aynı fiziksel içeriğin iki okunuşu.** Kazanç ispat sayısında değil, iki yerdedir: **(i)** izsizlik türetimin hiçbir adımında *varsayılmaz* — yakınsama geometrisinden çıkar, yani sonucu getirmeden sonuca varılır; **(ii)** soyut bir alan özelliği olarak değil, adı konabilen bir korunum ilkesi olarak okunur — deplasman akısı yaratılmaz, yok edilmez.

**(a) Eksenel bileşen.** Doğrudan radyal ivmenin türevidir:

$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\!\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3} \;\Longrightarrow\; \Delta a_{1,\parallel} = +\frac{2\mathcal{G}M}{r^3}\,\xi_\parallel$$

*İşaret pozitif:* gelgit ekseni boyunca her iki uç da merkezden dışa kaçar — yani Kuvvet 1'in kendisi, gelgit ekseninde Kuvvet 2'nin **içe doğru** taban sıkışmasının **tersi yönünde** bir katkı yapar.

**(b) Yanal bileşen.** Merkezden $\xi_\perp$ kadar yana kaymış noktada ivme yine kaynağa doğrudur; büyüklüğü $\mathcal{G}M/r'^2$ ($r'=\sqrt{r^2+\xi_\perp^2}\simeq r$), fakat doğrultusu merkez hattından $\xi_\perp/r$ kadar sapar:

$$a_\perp = -\frac{\mathcal{G}M}{r'^2}\cdot\frac{\xi_\perp}{r'} \simeq -\frac{\mathcal{G}M}{r^3}\,\xi_\perp \;\Longrightarrow\; T_\perp = -\frac{\mathcal{G}M}{r^3}$$

*İşaret negatif:* yanal doğrultularda hareket merkez hattına doğrudur — yani Kuvvet 1, gelgit eksenine dik yönlerde Kuvvet 2'nin taban sıkışmasıyla **aynı yönde**, onu pekiştiren bir katkı yapar. Bu, $1/r^2$ alanının **yakınsama geometrisidir** — radyal çizgiler kaynağa doğru birbirine yaklaşır, gövdenin yanakları merkez hattına itilir. Türetimde iz varsayımı kullanılmadı.

**Sıkıştırmanın çembersel olması.** Yukarıdaki hesapta $\xi_\perp$'nin *hangi* yanal doğrultu olduğu hiçbir yere girmedi — yalnız büyüklüğü girdi. Eksene dik bütün doğrultular kaynağa aynı uzaklıkta ve aynı yakınsama açısıyla baktığı için, gradyan yapısı **gövdenin Ay'a bakmayan bütün yanlarında eşittir.** Matematikte bunun karşılığı, $-1$ özdeğerinin **iki katlı dejenere** olmasıdır:

$$T_{\perp,1} = T_{\perp,2} = -\frac{\mathcal{G}M}{r^3}$$

Dejenerasyon, **gelgit ekseni** etrafındaki tam dönme simetrisinin ifadesidir: Kuvvet 1'in pekiştirici katkısı tek bir yönden gelen bir kıstırma değil, gelgit eksenini saran **eşit basınçlı bir kuşaktır** — çembersel sıkıştırma.

*(Kuşak, gelgit eksenine diktir — Dünya'nın ekvatoruna değil. Bkz. 11.1.3'teki uyarı.)*

### Taban ile gradyanın toplanması

Bir yüzey noktasındaki **net** içe-doğru sıkışma, Kuvvet 2'nin o noktadaki taban değeri ile Kuvvet 1'in artık katkısının toplamıdır ($\hat n$: dışa normal):

$$a_{net}(\vec\xi) \;=\; a_2 \;-\; \hat n\cdot\Delta\vec a_1(\vec\xi)$$

| Bölge | Kuvvet 1'in katkısı | Net sıkışma | Sonuç |
|---|---|---|---|
| Gelgit ekseni ($\hat n=\hat\xi_\parallel$) | $+2\mathcal{G}Mb/r^3$ (dışa) | $a_2-\dfrac{2\mathcal{G}Mb}{r^3}$ | **taban gevşer** — madde kabarır |
| Kuşak ($\hat n=\hat\xi_\perp$) | $-\mathcal{G}Mb/r^3$ (içe) | $a_2+\dfrac{\mathcal{G}Mb}{r^3}$ | **taban pekişir** — madde içeri iter |

Bu, 3.9.2'de sözle kurulan mekanizmanın niceliğe dökülmüş hâlidir: gelgit ekseninde Kuvvet 1'in farkı tabandan **çıkarılır**, kuşakta ise tabana **eklenir** — kuşaktaki net sıkışma büyük kaldığı (aslında bir miktar da arttığı) için gevşeyen eksene doğru akış olur.

**Taban iptal olur, fark kalır.** Kuşak ile eksen arasındaki net sıkışma farkında $a_2$ **düşer**:

$$a_{net}(\text{kuşak}) - a_{net}(\text{eksen}) = \left(a_2+\frac{\mathcal{G}Mb}{r^3}\right) - \left(a_2-\frac{2\mathcal{G}Mb}{r^3}\right) = \frac{3\mathcal{G}Mb}{r^3}$$

— tam olarak $(+2)-(-1)=3$ özdeğer farkı, $a_2$'nin sayısal değerinden **tamamen bağımsız.** Şekli belirleyen taban değil bu farktır; taban yalnız gerekçenin fiziksel gerçekliğidir (gövde zaten sıkışmış bir denizin içindedir — sıfırdan bir "çekme" değil), sonucun girdisi değildir.

> **Taban değişken olsa da sonuç aynıdır.** Yukarıdaki satırlarda eksenin iki ucuna da $a_2(r)$ yazıldı; oysa 11.1.3 tabanın $r$'ye bağlı olmasına izin veriyordu. Uçların gerçek değerleri $a_2(r)\mp a_2'b$'dir ve iki fark ayrışır:
>
> $$a_{net}(\text{kuşak})-a_{net}(\text{yakın uç}) = \frac{3\mathcal{G}Mb}{r^{3}} + a_2'b,\qquad a_{net}(\text{kuşak})-a_{net}(\text{uzak uç}) = \frac{3\mathcal{G}Mb}{r^{3}} - a_2'b$$
>
> $a_2'$ terimi iki uçta **zıt işaretlidir** ($\ell=1$); eksen çifti üzerindeki ortalaması, yani şekli belirleyen $\ell=2$ payı, tam olarak $3\mathcal{G}Mb/r^3$'te kalır. Taban eğimi gövdeye net bir kuvvet uygular ve yörünge hareketine yazılır — gelgit genliğine dokunmaz. Sonuç bu yüzden yalnız $a_2$'nin değerinden değil, **radyal yasasından da** bağımsızdır.

Kuvvet 2'nin ne büyüklüğü ne radyal yasası ölçülmeden — ve hiçbiri varsayılmadan — tensör şu değere ulaşır:

$$\boxed{\;\left(T_\parallel,\;T_\perp,\;T_\perp\right) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1)\;,\qquad \textstyle\sum\lambda_i = 0\;}$$

| Özdeğer | Doğrultu | Fiziksel okuma |
|---|---|---|
| $-1$ (×2, **dejenere**) | Gelgit eksenine dik **her** yön | **Neden:** Kuvvet 1, Kuvvet 2'nin tabanını gelgit eksenini saran eşit basınçlı bir kuşakta pekiştirir |
| $+2$ | Gelgit ekseni boyunca | **Sonuç:** Kuvvet 2'nin tabanı orada gevşer, kuşaktan kaçan madde eksenin iki ucuna birden kabarır |

**Mekanizmanın üç adımı, tek tensörde.** Türetim boyunca kurulan zincir şudur: **(1)** Dünya, Kuvvet 2'nin yönsüz tabanıyla zaten sıkışmış hâldedir. **(2)** Ay'ın Kuvvet 1'i yakın yüzde güçlü, uzak yüzde zayıftır; merkeze göre fark alındığında gelgit ekseninde bu tabanı gevşetir, eksene dik her yönde ise (yakınsama geometrisi gereği eşit büyüklükte) pekiştirir. **(3)** Hacmini koruyan gövde, pekişen kuşaktan kaçarak gevşeyen tek yöne, yani gelgit eksenine uzar; eksenin iki ucu da açık olduğundan kabarma çift olur. Üç adım da Kuvvet 2'nin tabanı ile Kuvvet 1'in gradyanının üst üste binmesinden çıkar.

*(Aynı sıkıştırma karşılıklıdır: Dünya da Ay'ı aynı geometriyle sıkar. Ay kilitli olduğu için oradaki kuşak gövde üzerinde dolaşmaz ve kabarma akışkan yerine magma üzerinde kalıcılaşır — mascon olgusu; Bkz. 3.9.5. Bu bölümün konusu Dünya'daki okyanus tepkisidir.)*

**İzsizlik bir varsayım değil, türetimin çıktısıdır.** Kuvvet 1'in üç bileşeni de izsizliğe başvurulmadan kuruldu ve iz kendiliğinden sıfır çıktı. (Kuvvet 2 tensöre hiç girmez: yönsüz olduğu için tensör yapısı taşımaz, birinci mertebe radyal değişimi ise $\ell=1$'dir — 11.1.3.) Dahası $\mathrm{tr}\,\mathsf{T}_1=-\frac{1}{\rho_n}\nabla^2P$ olduğundan bu sonuç, bölümün başında akı korunumundan elde edilen $\nabla^2P=0$ ile **birebir aynı ifadedir.** Yukarıdaki bağımsızlık kaydı gereği bu iki bağımsız ispat değil, tek içeriğin iki okunuşudur — fakat okunuşun kendisi kazançtır: standart fizikte "gelgit tensörünün izsizliği" soyut bir alan özelliği olarak kaydedilir, burada **adı konmuş bir korunum teoremidir.** Yanaklardan sıkılan ($-1,-1$) hacim, eksende kabaran ($+2$) hacimle tam muhasebeleşir.

---

## 11.1.5 Nedenselliğin İspatı: Basınç Okuması

$(+2,-1,-1)$ simetrik bir nesnedir ve tek başına "yan sıkıştırma nedendir" demeye izin vermez — kinematik bir tensör nedensellik taşımaz. Nedensellik ancak fiziksel alana, yani basınca inilerek kurulur.

Aşağıdaki $\Psi_T$ ve $P_T$, yalnız Kuvvet 1'in artık gradyanından gelir. Kuvvet 2 buraya hiç girmez: taban düzeyi $\psi$'den bağımsızdır, radyal eğiminin birinci mertebede taşıdığı pay ise $\ell=1$'dir ve gövdeyi ovalleştirmez, yalnız kaydırır (11.1.3). Aşağıdaki "açık"/"fazla" okuması bu yüzden **mutlak** değil, **Kuvvet 2'nin taban sıkışmasına göre** okunmalıdır: eksen tabana göre gevşek, kuşak tabana göre pekişiktir.

Çerçeve adımında taşınan kısım çıkarıldıktan sonra geriye kalan artık potansiyel, açılımın ikinci mertebe terimidir:

$$\Psi_T(\vec\xi) = -\tfrac12\left(T_\parallel\xi_\parallel^2 + T_\perp\xi_\perp^2\right) = -\frac{\mathcal{G}M}{2r^3}\left(2\xi_\parallel^2-\xi_\perp^2\right)$$

$\xi_\parallel=\xi\cos\psi$ ve $\xi_\perp=\xi\sin\psi$ konarak kapalı biçim:

$$\boxed{\;\Psi_T(\xi,\psi) = -\frac{\mathcal{G}M\,\xi^2}{2r^3}\left(3\cos^2\psi-1\right)\;}$$

Şimdi $\Phi=(P-P_0)/\rho_n$ tanımını tersine çevirip **artık basınç alanını** yazalım — teorinin fiilen konuştuğu büyüklük budur:

$$P_T(\xi,\psi) = \rho_n\Psi_T = -\frac{\rho_n\,\mathcal{G}M\,\xi^2}{2r^3}\left(3\cos^2\psi-1\right)$$

Gövde yüzeyinde ($\xi=b$) iki uç değer:

| Konum | $3\cos^2\psi-1$ | $P_T$ | Okuma (Kuvvet 2'nin tabanına göre) |
|---|---|---|---|
| Eksen ($\psi=0^\circ,\,180^\circ$) | $+2$ | $-\dfrac{\rho_n\mathcal{G}Mb^2}{r^3}$ | **taban gevşer** (basınç açığı) |
| Yanaklar ($\psi=90^\circ$) | $-1$ | $+\dfrac{\rho_n\mathcal{G}Mb^2}{2r^3}$ | **taban pekişir** (basınç fazlası) |

$P_T$ yalnız $\psi$'ye bağlıdır, azimuta değil: yanaklardaki basınç fazlası tek bir noktada değil, **gelgit eksenini saran tam bir kuşak boyunca** aynıdır. Bu, $-1$ özdeğerinin dejenerasyonunun basınç dilindeki karşılığıdır.

**Nedensellik böylece türetilmiş olur.** Ortak taşınma bileşeni çıkarıldıktan sonra geriye kalan, gerçek bir basınç alanıdır: **kuşakta yüksek, gelgit ekseninde düşük.** Akışkan daima $-\nabla P$ yönünde, yani kuşaktan eksene akar; kuşağın hiçbir yerinde zayıf nokta olmadığı için kaçış yalnız gelgit ekseninden olur ve o eksenin iki ucu da açıktır. **Sıkıştırma nedendir, kabarma sonuçtur** — ve açık ile fazlanın oranının tam $2{:}1$ olması, $(+2,-1,-1)$ özdeğer yapısının basınç dilindeki birebir karşılığıdır.

Klasik türetimde bu tabloya karşılık gelen hiçbir şey yoktur; orada basınç alanı yoktur, yalnız ivme farkı vardır.

**Ek M-26 ile çapraz denetim.** Kuşaktaki basıncın gelgit eksenindekini ne kadar aştığı:

$$P_T(90^\circ)-P_T(0^\circ) = +\frac{3}{2}\cdot\frac{\rho_n\mathcal{G}Mb^2}{r^3} \;>\; 0$$

M-26'nın "suya batan top"u, tamamen farklı bir yoldan — hidrostatik derinlik–basınç muhasebesinden — aynı işareti vermişti ($F_{yan}-F_{dikey}\propto\rho g r>0$). İki bağımsız argüman, aynı elipsoid.

---

## 11.1.6 Denge Gelgiti Genliği ve Güneş/Ay Oranı

Okyanus serbest yüzeyi, toplam potansiyelin sabit olduğu yüzeydir:

$$g\,\zeta(\psi) + \Psi_T(b,\psi) = \text{sabit},\qquad g=\frac{\mathcal{G}M_\oplus}{b^2}$$

> **Çeviri kaydı — bu bir "eşpotansiyel" değil, eş-basınç yüzeyidir.** Yukarıdaki koşul klasik jeopotansiyel yazımıyla biçimsel olarak özdeştir, fakat teoride ödünç alınmış bir nesne değildir: $\Phi\equiv(P-P_0)/\rho_n$ tanımı $\rho_n$ sabit olduğu için birebir tersine çevrilebilir, dolayısıyla "toplam potansiyelin sabit olduğu yüzey" ifadesi **"toplam basıncın sabit olduğu yüzey" (izobar) ile aynı cümledir.** Serbest yüzeyin fiziksel tanımı da budur: üstündeki basınç her yerde $P_{atm}$ olduğu için su, basınç dengesizliği kalmayana dek akar. Potansiyel dili yalnız cebiri kısaltmak içindir; teorinin konuştuğu büyüklük 11.1.5'te yazılan $P_T$'dir. Aynı şekilde buradaki $g$, standart bir "yerçekimi ivmesi" değil, Dünya'nın kendi Kuvvet 1'inin yüzey değeridir.

**Sabit, hacim korunumundan sabitlenir.** Su yaratılmadığına göre $\langle\zeta\rangle=0$ olmalıdır; $\langle 3\cos^2\psi-1\rangle=0$ (Legendre $P_2$'nin küre ortalaması sıfırdır) olduğundan sabit tam olarak sıfırdır. Buradan:

$$\zeta(\psi) = -\frac{\Psi_T}{g} = \frac{\mathcal{G}Mb^2}{2r^3}\cdot\frac{b^2}{\mathcal{G}M_\oplus}\left(3\cos^2\psi-1\right) = \frac{1}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^3 b\,\left(3\cos^2\psi-1\right)$$

> **$\mathcal{G}$ sadeleşti.** Sonuçta ne $\mathcal{G}$, ne $\alpha$, ne $Cq_n$ kaldı — yalnız kütle oranı ve geometri. Denge gelgiti **sıfır parametreli** bir öngörüdür ve teorinin serbest kalemlerinin hiçbirine dokunmaz.

$A\equiv\dfrac{M}{M_\oplus}\left(\dfrac{b}{r}\right)^3 b$ kısaltmasıyla tepe ve çukur ayrışır:

$$\zeta(0^\circ)=+A\ \ (\text{kabarma tepesi}),\qquad \zeta(90^\circ)=-\tfrac12 A\ \ (\text{yanak çukuru})$$

$$\boxed{\;\Delta\zeta \equiv \zeta(0^\circ)-\zeta(90^\circ) = \frac{3}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^{3} b\;}$$

**$3/2$ katsayısı buradan gelir ve etiketi belirler:** $\Delta\zeta$ bir *yükseklik değil*, **tepe–çukur tam genliğidir.** Kabarma ortalama seviyenin $+A$ üstüne çıkarken yanaklar $-A/2$ altına iner.

### Sayılar

$b=6{,}371\times10^6$ m alınarak:

| Kaynak | $M/M_\oplus$ | $(b/r)^3$ | Tepe $+A$ | Çukur $-A/2$ | Genlik $\Delta\zeta$ |
|---|---|---|---|---|---|
| **Ay** | $1{,}229\times10^{-2}$ | $4{,}553\times10^{-6}$ | $+0{,}357$ m | $-0{,}178$ m | **0,535 m** |
| **Güneş** | $3{,}331\times10^{5}$ | $7{,}724\times10^{-14}$ | $+0{,}164$ m | $-0{,}082$ m | **0,246 m** |

**Güneş/Ay yarışı.** Güneş'in Dünya üzerindeki toplam itme kuvveti ($\propto M/r^2$) Ay'ınkinin **179 katıdır** — bu yüzden onun etrafında dolanırız. Fakat gelgiti yaratan şey toplam kuvvet değil, kuvvetin gövde boyunca **değişimidir**; ve bu gradyan uzaklığın küpüyle zayıflar:

$$\frac{\text{Güneş gelgiti}}{\text{Ay gelgiti}} = \frac{M_\odot}{M_{Ay}}\left(\frac{r_{Ay}}{r_\odot}\right)^{3} = \frac{2{,}709\times10^7}{(389{,}2)^3} \approx 0{,}460$$

Aynı $0{,}460$ sayısı genlik tablosundan da okunur ($0{,}246/0{,}535$): tensör oranı ile genlik oranı birbirini doğrular. Güneş toplam itimde $179$ kat üstün, gelgitte Ay'ın yarısından azdır. $1/r^2$ ile $1/r^3$ arasındaki farkın bütün gücü buradadır (ayrıntılı tartışma: 3.9.2.2).

> **Bir koşul kaydı.** Yukarıdaki $0{,}460$, iki kaynağın da saf Kuvvet 1 taşıdığı varsayımıyla hesaplanmıştır. Ay için bu doğrudur (kilitli), Güneş için değildir (Dünya'ya göre serbest döner). Güneş tarafındaki F4+F5 payı, gelgit tensörünü yalnız ölçekleyerek değil **yapısını değiştirerek** etkiler; bu yüzden bölümün ayırt edici sınavı bu skaler oranda değil, tensörün özdeğerlerinin ayrı ayrı okunmasındadır. Kuruluşu 11.1.8'dedir.

**Büyük ve küçük gelgit.** İki kaynağın genlikleri hizalanma durumuna göre toplanır veya çıkarılır:

| Durum | Geometri | Hesap | Genlik |
|---|---|---|---|
| Büyük gelgit (*spring*) | Ay ve Güneş hizalı | $0{,}535+0{,}246$ | **0,781 m** |
| Küçük gelgit (*neap*) | Ay ve Güneş dik | $0{,}535-0{,}246$ | **0,289 m** |
| Oran | — | $0{,}781/0{,}289$ | **2,70** |

Açık okyanusta ölçülen denge gelgiti genliği ~0,5 m mertebesindedir (Pugh & Woodworth, 2014); türetilen 0,535 m bu mertebeyi serbest parametresiz karşılar. Kıyılarda görülen metrelerce genlik havza rezonansının yerel büyütmesidir — gök mekaniğine değil kıyı hidrodinamiğine aittir ve bu modelin kapsamı dışındadır.

> *Dürüstlük kaydı:* Genlikteki uyum bir **mertebe ve yapı** doğrulamasıdır, hassas doğrulama değil. Denge gelgiti kuramı okyanus havzalarının geometrisini, derinliğini ve dinamik tepkisini içermez; gerçek okyanusta ölçülen yerel genlikler bu değerden düzenli olarak sapar. Hassas olan, boyutsuz **oranlardır**: Güneş/Ay $0{,}460$ ve büyük/küçük $2{,}70$.

---

## 11.1.7 Eşdeğerlik İlkesi: Varsayım Değil, Sonuç

Tensörün biçimine bir kez daha bakalım: $T_{ij}=-\frac{1}{\rho_n}\partial_i\partial_jP$. Buradaki $\rho_n$ **nükleon öz yoğunluğudur** — su, kaya, demir, cıva fark etmez; hepsi aynı nükleonlardan kuruludur ve hepsi aynı $\rho_n$'yi taşır. Dolayısıyla gelgit ivmesi, üzerine etki ettiği maddenin bileşiminden **zorunlu olarak** bağımsızdır.

Klasik mekanikte bu bağımsızlık bir postülattır: eylemsiz kütle ile kütleçekimsel kütlenin eşitliği varsayılır, deneyle sınanır, fakat açıklanmaz. Burada türetilmiştir — tek bir evrensel $\rho_n$ olduğu için başka türlüsü yazılamaz.

**Bunun bedeli ve sınavı.** İfade tersine de okunur: $\rho_n$'nin evrenselliği bozulsaydı gelgit bileşime bağlı olurdu. Bu, teoriyi eşdeğerlik ilkesi testlerine doğrudan bağlar. MICROSCOPE uydusunun titanyum–platin çifti için bildirdiği $\eta_{EP}\lesssim10^{-15}$ sınırı (Touboul ve ark., 2022) ile Eöt-Wash burulma terazisi ölçümleri (Schlamminger ve ark., 2008), teoride $\rho_n$ evrenselliğinin sınavıdır: bu deneylerin null sonuçları, teorinin bir varsayımını değil bir **türetiminin girdisini** doğrular.

---

## 11.1.8 Newton'la Sınır ve Ayırt Edici Sınav

Dürüst kayıt özdeşlikten başlar. Aşağıdaki tablo, bu bölümün türetiminin dayandığı kaynak — **kilitli** Ay — için geçerlidir:

| Büyüklük | Bu türetim | Klasik gelgit kuramı |
|---|---|---|
| Uzaklık yasası | $1/r^3$ | $1/r^3$ — aynı |
| Tensör özdeğerleri | $(+2,-1,-1)$ | $(+2,-1,-1)$ — aynı |
| Güneş/Ay oranı | 0,460 | 0,460 — aynı |
| Denge gelgiti genliği | 0,535 / 0,246 m | aynı |
| Büyük/küçük oranı | 2,70 | aynı |

**Tek bir sayı bile ayrışmaz.** Bu bölüm bir ayırt edici sınav değildir ve öyleymiş gibi sunulmaz. Ayrışma sayıda değil, üç yapısal noktadadır:

1. **İzsizlik teoremdir.** Klasik kuramda $\mathrm{tr}\,\mathsf{T}=0$, Laplace denkleminin soyut bir özelliği olarak kaydedilir; burada deplasman akısının korunumudur ve türetimin hiçbir adımında varsayılmadan, yakınsama geometrisinden çıkar (11.1.4). *(Bunun "iki bağımsız ispat" olmadığı, aynı içeriğin iki okunuşu olduğu 11.1.4'ün bağımsızlık kaydında tartılmıştır — ayrışma ispat sayısında değil, sıfırın hangi ilkeye bağlandığındadır.)*
2. **Eşdeğerlik ilkesi sonuçtur.** Klasik mekanikte postüla, burada $\rho_n$ evrenselliğinin türevi (11.1.7). Çerçeve adımı da aynı köke bağlıdır: ortak ivmenin gövdeyi deforme etmemesi, klasik türetimde eylemsiz çerçeve seçiminin sonucudur; burada Kuvvet 1'in her nükleona aynı ivmeyi vermesinin sonucudur. *(İki maddeyi ayrı saymıyoruz — kökleri aynı.)*
3. **Kuvvet envanteri kapalıdır.** Kilitli kaynağın dönüş kolu bastırılmış olduğundan gelgit, beş kuvvetten yalnız pompa koluna — Kuvvet 2'nin tabanı ile Kuvvet 1'in gradyanının üst üste binmesine — iner (11.1.2, 11.1.4). Sayısal sonucun tek bir gradyana inmesi bir kolaylık kabulü değil, türetilmiş bir sonuçtur: tabanın $\ell=0$ payı hacmi, $\ell=1$ payı konumu değiştirir, $\ell=2$ payı ise açılımın bir üst mertebesindedir (11.1.3). Klasik kuramda böyle bir envanter sorusu yoktur; teoride bu, tensörün saflığının gerekçesidir.

Bunlara mekanizmanın kendisi eklenir: teoride gelgiti yapan şey bir çekme değil, gövdenin zaten içinde bulunduğu bir taban sıkışmanın (Kuvvet 2) yönlü bir gradyanla (Kuvvet 1) yeniden dağılmasıdır — kuşakta pekişme, gelgit ekseninde gevşeme (11.1.3–11.1.4). Bu iki-aktörlü mekanizma klasik kuramda mevcut değildir; orada tek aktör potansiyelin kendisidir.

Fakat bu üç madde de yorum düzeyindedir. Asıl soru şudur: **iki kuramı ayıran bir ölçüm var mıdır?** Vardır — ve yukarıdaki özdeşlik tablosunun sessiz koşulunda saklıdır.

### Sınavın kaynağı: tablo yalnız *kilitli* kaynak için geçerlidir

Özdeşlikler, 11.1.2'nin kuvvet envanterine dayanır: Ay kilitli olduğu için $\omega_1$ kolu kapalıdır ve gelgit saf Kuvvet 1'den gelir. **Güneş kilitli değildir.** Dönme kolu açıktır — ve bu kol bütün hâlinde açılır: F4 varsa F5 de vardır, ikisi de $\omega_1$'in ürünüdür.

> [!IMPORTANT]
> **"Dönüyor" hangi çerçeveye göre?** Bu, bölümün en kolay yanlış okunan noktasıdır ve peşinen kapatılmalıdır. "Güneş dönüyor, Ay dönmüyor" cümlesi **mutlak** (yıldızlara göre) dönme hızlarının karşılaştırması olarak okunursa yanlıştır: Ay da kendi ekseni etrafında döner — üstelik Güneş'inkine çok yakın bir hızla.
>
> Cümle **Dünya'ya göre** okunmalıdır; o çerçevede ayrım mutlaktır:
>
> | Kaynak | Yıldızlara göre dönme | **Dünya'ya göre dönme** |
> |---|---|---|
> | **Ay** | 27,32 gün | **yok** — hız tam olarak sıfır |
> | **Güneş** | ~25,4 gün | ~27,3 gün (Carrington sinodik) |
>
> Gelgit kilidi zaten bunun tanımıdır: Ay'ın dönüşü yörünge dolaşımıyla aynı fazda olduğu için Dünya–Ay doğrultusuna göre **hiç dönmez**, hep aynı yüzünü gösterir. Güneş ise Dünya–Güneş doğrultusuna göre yaklaşık dört haftada bir tam tur atar. Mutlak hızlar yalnız %8 ayrışırken, Dünya'ya göre durumlar birbirinin tam zıddıdır.
>
> Teorinin iddiası tam olarak bu çerçevededir: **gelgit kilidi, gövdenin kendi makro-girdabını bastırır** (3.9.1; girdap rekabeti 3.4.4). Ortama ve gelgit eksenine göre bağımsız bir sirkülasyon kalmadığı için $\omega_1$ kolunu besleyecek kaynak ortadan kalkar; serbest dönen gövdede kalır. Ayrım bu yüzden **ikilidir (kilitli / serbest)**, sürekli bir hız ölçeği değil.
>
> **Ve bu, sınavı zayıflatmak yerine keskinleştirir.** İki kaynağın mutlak dönme hızları neredeyse eşit olduğuna göre, tensör yapılarında bulunacak herhangi bir fark **mutlak hıza yazılamaz** — yalnız kilitlilik durumuna yazılabilir. Karışıklık değişkeni kendiliğinden elenmiştir; diferansiyel deney bu sayede daha temizdir.

**Kuvvet 3 neden tensöre girmiyor?** $\omega_1$ kolu üç kuvvet taşır (3, 4, 5) ama aşağıdaki tabloda yalnız ikisi var; bu bir atlama değil, iki gerekçenin sonucudur. **(i)** M-37 Kuvvet 3 ile Kuvvet 4'ün *aynı vorteksin* teğetsel ve eksenel bileşenleri olduğunu ve ikisinin de tek bir $a_{madde}(R)$ tarafından yönetildiğini türetir; F3'ün radyal gradyan içeriği bu yüzden F4'ün $\beta$'sında **zaten sayılmıştır** — ayrıca eklenmesi çift saymak olurdu. **(ii)** F3'ün kendine ait etkisi sıfırıncı mertebede sürüklemeyi *bastırmak*, birinci mertebede $\Delta v$ ile doğrusal bir **artık kuplaj** uygulamaktır (M-37 Adımlar B). Artık kuplaj bir statik basınç gradyanı değildir; $\eta_E$ üzerinden işler ve zaman ölçeği $\tau_E$'dir. 11.1.9'da gösterileceği üzere bu kanal gelgit periyoduna göre **yirmi iki mertebe** yavaştır — yani F3, statik tensör $T_{ij}=-\frac{1}{\rho_n}\partial_i\partial_jP$'ye ölçülebilir hiçbir katkı yapamaz.

Geriye kalan iki kuvvette kritik olan, **geometrileridir**. Hiçbiri Kuvvet 1 gibi küresel-radyal değildir:

| Kuvvet | Geometri | Yön | Yasa |
|---|---|---|---|
| **F1** | küresel | $-\hat r$ (küresel yarıçap) | $1/r^2$ |
| **F4** | **silindirik** | $-\hat R$ (dönme eksenine dik) | $1/R$ (Ek M-38) |
| **F5** | **meridyenel** | $-\hat\theta$ (ekvatora doğru) | $\propto\sin2\theta$ (Ek M-39) |

Her ikisi de kaynağın **kendi dönme eksenine** göre tanımlıdır. Gelgit tensörü alanın türevi olduğuna göre, bu geometrileri de miras alır.

### Karışımın tensörü

Dünya, Güneş'in ekvator düzlemine yakındır (heliografik enlem $\pm7{,}25^\circ$). Üç katkı bu noktada üst üste konduğunda tensörün özvektörleri şunlardır: **(1)** gelgit ekseni (Güneş–Dünya doğrultusu), **(2)** yörünge doğrultusu (ekliptik içinde, gelgit eksenine dik), **(3)** ekliptiğe dik (Güneş'in dönme ekseni doğrultusu). Özdeğerler:

$$\boxed{\;(T_1,T_2,T_3)=\frac{\mathcal{G}M}{r^{3}}\Bigl(2+\beta,\;\;-(1+\beta),\;\;-(1+\gamma)\Bigr),\qquad \mathrm{tr}\,\mathsf{T}=-\gamma\,\frac{\mathcal{G}M}{r^{3}}\;}$$

$$\beta \equiv \frac{Br}{\mathcal{G}M}\ \ (\text{F4 payı}),\qquad \gamma \equiv \frac{2a_5^{(0)} r^{2}}{\mathcal{G}M}\ \ (\text{F5 payı})$$

*(Buradaki ön çarpan $\mathcal{G}M/r^3$'tür — 11.1.6'nın $A\equiv\frac{M}{M_\oplus}(b/r)^3b$ kısaltmasıyla karıştırılmamalıdır; o bir uzunluktur, bu bir ivme gradyanıdır. Aynı harfi iki kez kullanmamak için burada açık yazıldı. $B$ ve $a_5^{(0)}$ sırasıyla F4 ve F5'in **genlik katsayılarıdır**, alanların kendisi değil: $\vec a_4=-\dfrac{B}{R}\hat R$, $\vec a_5=-a_5^{(0)}\sin2\theta\,\hat\theta$.)*

İki katkı **iki ayrı imza** üretir ve birbirine karışmaz:

**(a) F4 → dejenerasyon kırılır, iz korunur.** Silindirik $1/R$ alanı tek başına $(+1,-1,0)$ verir; izi sıfırdır (iki boyutlu akı korunumu). Fakat özdeğerleri dejenere değildir. F1 ile toplandığında yanal çiftin eşitliği bozulur: ekliptik içindeki yanal özdeğer $-(1+\beta)$ olurken ekliptiğe dik olan $-1$'de kalır. **Sıkıştırma kuşağı artık çember değil, elipstir.**

**(b) F5 → iz ihlal edilir.** Meridyenel $\sin2\theta$ alanının ıraksaması ekvator düzleminde sıfır değildir: $\nabla\!\cdot\!\vec a_5\big|_{\theta=0} = -2a_5^{(0)}/r$. *(Kuvvetin kendisi ekvatorda sıfırdır — $\sin2\theta|_{\theta=0}=0$ — ama tensöre giren şey kuvvet değil türevidir ve $d(\sin2\theta)/d\theta$ tam orada maksimumdur.)* Bu sonuç F5'in radyal yasasından **bağımsızdır**; hangi kuvvetle uzaklaşırsa uzaklaşsın iz bağıntısı aynı kalır.

### Newton bunu üretemez

Klasik kuramda bir kaynağın **dönüp dönmediği dış alanına girmez.** İki imzanın Newton'daki karşılığı:

| İmza | Newton | Teori |
|---|---|---|
| **Yanal dejenerasyonun kırılması** | Yalnız gövdenin basıklığından ($J_2$). Güneş için $J_2(R_\odot/r)^2 = 2{,}2\times10^{-7}\times(4{,}65\times10^{-3})^2 \approx 5\times10^{-12}$ | $\beta$ — apsidal presesyon üst sınırı $\lesssim10^{-9}$ |
| **Boşlukta iz** | $\nabla^2\Phi=0$ gereği **tam olarak sıfır** — her kaynak, her uzaklık, her çokkutuplu mertebe | $-\gamma\,\mathcal{G}M/r^3 \ne 0$ |

Birinci satırda Newton'un bir arka planı vardır ama **200 kat aşağıdadır** — arada gerçek bir keşif penceresi kalır. İkinci satırda ise arka plan **tam sıfırdır**: boşlukta ölçülen sıfırdan farklı bir gelgit izi, Newton'un kendi denklemini ihlal eder. İkinci kanal bu yüzden temizdir.

**Sınavın ölçek referansı.** "Temiz kanal" ifadesi, kanalın *kolay* olduğu anlamına gelmez; aranan büyüklüğün mertebesi yazılmadan iddia eksik kalır. Güneş için gelgit tensörünün ölçeği:

$$\frac{\mathcal{G}M_\odot}{r^{3}} = \frac{1{,}327\times10^{20}}{(1{,}496\times10^{11})^{3}} = 3{,}96\times10^{-14}\ \text{s}^{-2} \;\approx\; 40\ \mu\text{E}$$

(1 E = 1 Eötvös = $10^{-9}$ s⁻².) Aranan iz $\gamma$ ile bunun çarpımıdır: $\gamma\sim1$ için ~40 μE, $\gamma\sim10^{-3}$ için ~40 nE. Kıyas için gradyometri sınıfı aletlerin tek bileşen gürültüsü mE/$\sqrt{\text{Hz}}$ mertebesindedir — yani sinyal, *anlık* duyarlılığın altındadır ve yalnız frekansı bilinen bir zorlamada uzun integrasyonla erişilebilir. **Asıl güçlük duyarlılık değil ayrıştırmadır:** iz artığının okyanus yükleme, atmosferik basınç ve $J_2$ arka planından ayıklanması gerekir.

> **Dürüst kayıt — bu bölüm $\gamma$'ya bir üst sınır koymuyor.** Yukarıdaki satırlar sınavın ölçeğini verir, sonucunu vermez. Mevcut gradyometri verisinden $\gamma$ üzerine fiilen hangi sınırın çıktığı **bu bölümde hesaplanmamıştır** ve 7.4'ün hesap kalemine yazılıdır. Kanalın Newton arka planının tam sıfır olması onu *ilkece* temiz kılar; *fiilen* ne kadar sıkı olduğu henüz açık bir kalemdir. $\beta$ için verilen 200 katlık pencerenin $\gamma$ karşılığı yoktur.

Ve iki imzanın da **yönü bellidir**: özvektörler Güneş'in dönme eksenine kilitlidir. Newton'un noktasal kaynak alanında böyle bir ayrıcalıklı yön yoktur.

### Doğal diferansiyel deney

| Kaynak | Açık kollar | Gelgit tensörü |
|---|---|---|
| **Ay** — kilitli (Dünya'ya göre dönmüyor) | yalnız pompa kolu (F1 + F2) | $(+2,\,-1,\,-1)$ · iz $=0$ · **dejenerasyon kusursuz** |
| **Güneş** — serbest (Dünya'ya göre ~27,3 günde bir tur) | pompa kolu (F1 + F2) + F4 + F5 | $(2{+}\beta,\,-(1{+}\beta),\,-(1{+}\gamma))$ · **iz $\ne0$** · **dejenerasyon kırık** |

**Dünya bu iki kaynağı aynı anda, aynı aletlerle ölçmektedir.** Kilitli olan kontrol, dönen olan numunedir — kurulması gereken bir düzenek değil, hâlihazırda işleyen bir deneydir. Aranan gözlemsel büyüklük, gelgit tensörünün **üç özdeğerinin ayrı ayrı** çıkarılmasıdır (gradyometri); Ay ve Güneş bileşenleri frekansta zaten ayrıktır.

### Sınavın dürüst statüsü

| | |
|---|---|
| **Yapı** | türetilmiş, parametresiz. $(2{+}\beta,-(1{+}\beta),-(1{+}\gamma))$ ve $\mathrm{tr}=-\gamma\,\mathcal{G}M/r^3$, alanların geometrisinden çıkar |
| **İz bağıntısı** | F5'in radyal yasasından bağımsız — bu, sonucun en sağlam kısmıdır |
| **Genlikler ($\beta,\gamma$)** | **öngörülmemiştir.** $\beta$: F4 payı Ek M-38'de galaktik kolektif vortekse atanır, Güneş yavaş döndüğü için yerel pay küçüktür; apsidal presesyon $\beta\lesssim10^{-9}$ verir. $\gamma$: $\kappa_5$ serbest kalemdir (Ek M-39, [F]) |
| **Sınavın biçimi** | "şu sayı çıkmalı" değil; **"şu iki yapı bulunmalı, yoksa $\beta$ ve $\kappa_5$ şundan küçüktür"** |
| **İki yönlü keskinlik** | Sıfırdan farklı bir boşluk izi bulunursa Newton'un vakum denklemi ihlal edilir — kesin ayrım. Bulunmazsa $\kappa_5$ üzerindeki sınır her ölçüm turunda daralır |

**Ölçüm duyarlılığının nicel değerlendirmesi bu bölümde yapılmamıştır** (gelgit tensörünün üç özdeğerini ayrı ayrı çekmek için gereken gradyometri hassasiyeti, okyanus yükleme ve $J_2$ arka planından ayrıştırma dâhil) ve 7.4'ün hesap kalemine yazılmıştır. Burada kurulan şey sınavın **yapısı** ve hangi büyüklüğün hangi kanaldan sınırlandığıdır.

**Güneş için $\beta$ ve $\gamma$: ihmal edilebilir, ama açık iş.** 11.1.6'nın $0{,}246$ m ve $\%46$ sayıları, Güneş'in kendi F4/F5 payını ($\beta$, $\gamma$) yok sayarak (saf Kuvvet 1) hesaplanmıştır. Bu yaklaşıklık makuldür — $\beta$ zaten apsidal presesyondan $\lesssim10^{-9}$ ile sıkı sınırlıdır ve $\gamma$'nın da benzer mertebede kalması beklenir (Güneş'in yerel dolaşımı zayıftır, bkz. aşağıdaki ölçek kaydı) — ama **ikisinin de genliğe kesin sayısal etkisi bu bölümde hesaplanmamıştır.** Bu, 7.4'ün açık kalemidir.

> **Ölçek kaydı — neden Güneş'te zayıf, galakside belirleyici.** F4 ve F5 dönüş kolundan beslenir ve kolun gücü ortamın dönme hızıyla ölçeklenir. Güneş'in yerel dolaşımı, galaktik kolektif vorteksin yanında sönüktür; yerel payı ölçülebilir mertebeye ancak yaklaşır, belirleyici olamaz. Galaktik ölçekte ise aynı iki kuvvet **baskın** hâle gelir ve düz dönüş eğrilerini üreten şey olur (Bkz. Kısım 10). İki ortamın Evrenakı dönme hızları kıyaslanabilir büyüklükler değildir — bu yüzden Kepler yasası Güneş Sistemi'nde çalışır, galakside çalışmaz. Kepler evrensel bir yasa değil, **belirli bir kol dengesinin** yerel sonucudur. *(Bu paragraftaki kıyas **Güneş ile galaksi** arasındadır, Güneş ile Ay arasında değil: Güneş ile Ay'ın **mutlak** dönme hızları neredeyse eşittir ve aralarındaki ayrım Dünya'ya göre dönme, yani kilitlilik durumudur — yukarıdaki uyarıya bkz. Genlik zayıflığı $\beta$'yı küçültür; kilitlilik ayrımı ise yapının varlığını belirler. İki kalem karıştırılmamalıdır.)*
>
> **Bunun gelgit hesabına yansıması.** Bu bölümdeki $\beta,\gamma\approx0$ sadeleştirmesi yalnız **Güneş Sistemi ölçeğine** özgüdür — kaynağın yerel dolaşımı zayıf olduğu için geçerlidir. Kaynak hızlı dönen bir galaksi, bir galaktik çekirdek veya genel olarak $\omega_1$ kolu güçlü herhangi bir gövde olduğunda bu sadeleştirme **düşer**: F4 ve F5, gelgit tensörüne artık ihmal edilemeyecek, hatta **baskın** katkılar (büyük $\beta,\gamma$) olarak girer ve tensörün yapısını (dejenerasyon kırılması, sıfırdan farklı iz) köklü biçimde değiştirir. Böyle sistemlerdeki gelgit hesabı, yalnız Kuvvet 1'in $(+2,-1,-1)$'iyle değil, **F1+F2+F4+F5'in tam birleşik tensörüyle** ($\S$"Karışımın tensörü") yürütülmelidir — bu, bugün burada yapılmamış, ayrı bir hesap gerektiren açık bir iştir.

---

## 11.1.9 Şişkinlik Kayması: Kaymayı Yapan Sürtünme Atomiktir

Buraya kadar kurulan denge gelgiti **statik** tepkidir: kabarma, gelgit ekseniyle tam hizalıdır. Gözlem ise şunu söyler: şişkinlik ekseni Ay'ın doğrultusuyla çakışmaz, Dünya'nın hızlı dönüşü onu Ay'ın yaklaşık $3^\circ$ **önüne** taşır (Bkz. 3.9.2). Bu son adım, hangi sürtünmenin iş gördüğünü sormayı gerektirir.

### Ortam sürtünmesi bu işi *bu zaman ölçeğinde* yapamaz

Soruyu doğru sormak gerekir. Evrenakı sürtünmesi sıfır **değildir** — Postülat 7 $\eta_E$'yi "sıfıra çok yakın, kesinlikle sıfır değil" diye sabitler ve teori bu sıfır-olmayışı başka yerlerde kullanır: retrograd uyduların sönümü, halka bending-wave yitimi, yörünge kilitlenmesi (Bkz. 11.3.2). Ortam gerçekten sürükler; içinden geçtiği maddeye gerçekten tutunur. Mesele **yapıp yapmadığı değil, ne kadar sürede yaptığıdır.**

İki gevşeme zaman ölçeğini yan yana koyalım:

| Kanal | Gevşeme zamanı | Nereden |
|---|---|---|
| **Maddesel (atomik) sürtünme** | $\tau_{madde}\simeq QP/2\pi \approx 8{,}5\times10^{4}$ s ($\approx24$ saat) | $Q\approx12$, gelgit dönemi 12,42 sa |
| **Evrenakı kuplajı** | $\tau_{E}=\dfrac{2\rho_c b^{2}}{9\eta_E} \gtrsim 2{,}2\times10^{27}$ s ($\gtrsim7\times10^{19}$ yıl) | 11.3.2'nin Stokes yazımı, kitabın **geçerli en sıkı** sınırıyla ($\eta_E\lesssim2{,}3\times10^{-11}$ Pa·s; 11.4.8). *(Süpersedilmiş Phoebe sınırı $\eta_E\approx3{,}3\times10^{-5}$ Pa·s ile aynı ifade $\tau_E\gtrsim1{,}5\times10^{21}$ s verirdi — $1{,}4\times10^{6}$ kat gevşek; aşağıdaki muhakeme onunla bile geçerlidir.)* |

$$\frac{\tau_E}{\tau_{madde}} \gtrsim 2{,}5\times10^{22} \qquad\left(\text{gevşek sınırla bile } \gtrsim1{,}8\times10^{16}\right)$$

Evrenakı'nın gevşeme zamanı evren yaşının ~5 milyar katıdır. Gelgit ise **günlük** bir olaydır: 12,4 saatte bir tersine dönen bir zorlamaya, yirmi iki mertebe daha yavaş bir kanalın derece mertebesinde faz kazandırması mümkün değildir. Sonuç sınır seçimine duyarlı değildir — süpersedilmiş gevşek sınırla bile arada on altı mertebe kalır, yani muhakeme her iki durumda da aynı yere varır. Üstelik yukarıdaki $\tau_E$ **en cömert** tahmindir: Ek M-43 Stokes yazımının Dünya–Ay rejiminde geçerli olmadığını, bağıl hızların kritik hızın ($v_{kav}$) çok altında kaldığını ve altkritik bastırmanın kuplajı daha da düşürdüğünü gösterir. Gerçek $\tau_E$ bundan büyüktür.

Muhasebenin öbür ucu da bunu doğrular: Dünya'nın ölçülen toplam gelgit enerji yitimi ~3,7 TW'tır ve ezici çoğunluğu **sığ denizlerdeki taban sürtünmesi ve türbülanstır** — su moleküllerinin kayaya sürtünmesi. Defter zaten kapalıdır.

**Sonuç:** kayma açısı ortamın değil **maddenin** defterindedir. Kaymayı yapan **atomik (malzeme) sürtünmesidir** — ortamın katkısı sıfır değil, fakat bu bölümün sonunda nicelendiği üzere $10^{-22}$ derece mertebesindedir.

> **Ayrım kritiktir, çünkü teori $\eta_E$'yi başka yerlerde tam da bu yüzden kullanır.** Milyar yıl ölçeğinde işleyen olgularda — retrograd uydu göçü, kilitlenme, halka sönümü — Evrenakı kuplajı *tek* açıklamadır ve orada maddesel sürtünmenin yeri yoktur. Günlük ölçekte ise durum tersine döner. İki kanal rakip değil, **farklı zaman pencerelerinde** çalışır; hangisinin baskın olduğunu olgunun periyodu belirler.

### Doğru muhasebe: iki ayrı rol

Evrenakı elbette tablonun dışında değildir — ama rolü kaymayı *yaratmak* değil, kayan şişkinliğin doğurduğu **torku taşımaktır**:

| Soru | Cevap | Nereye ait |
|---|---|---|
| Şişkinliği ne öne taşır? | Okyanus–taban sürtünmesi, türbülans, havza yitimi | **madde** (atomik) |
| Öne taşınmış şişkinlik Ay'a ne yapar? | Yer değiştirmiş kütle fazlası kendi **gradyan lobunu** taşır; lob Ay'a teğetsel itki verir | **Evrenakı** (Kuvvet 1) |

Bu ayrım 3.9.4'te kurulan lob-işaret kuralının ta kendisidir: teorinin katkısı kaymayı üretmek değil, kaymanın ürettiği torku **taşıyan aracıyı adlandırmaktır.**

### Nicel: kayma açısı serbest değildir

Kayma açısı $\varepsilon$ bir tahmin değildir; **Ay'ın ölçülen uzaklaşma hızından geri çözülür.** Öne kaymış şişkinliğin Ay'a uyguladığı tork, Ay'ın yörünge açısal momentumunu besler:

$$\Gamma = \frac{3}{2}\,k_2 \sin(2\varepsilon)\,\frac{\mathcal{G}M_{Ay}^{2}R_\oplus^{5}}{r^{6}} \;=\; \frac{dL}{dt},\qquad L = M_{Ay}\sqrt{\mathcal{G}M_\oplus r}\;\Longrightarrow\;\frac{dL}{dt}=\frac{L}{2r}\frac{dr}{dt}$$

Ölçülen $dr/dt = 3{,}8$ cm/yıl (Ay Lazer Menzillemesi; Dickey ve ark., 1994) konduğunda:

| Büyüklük | Değer |
|---|---|
| $L$ (Ay yörünge açısal momentumu) | $2{,}88\times10^{34}$ kg·m²/s |
| $dL/dt$ | $4{,}50\times10^{16}$ N·m |
| $\mathcal{G}M_{Ay}^2R_\oplus^5/r^6$ | $1{,}17\times10^{18}$ N·m |
| **$k_2\sin(2\varepsilon)$** | **$0{,}0256$** |

Kalan tek girdi Dünya'nın Love sayısı $k_2$'dir — bir malzeme özelliğidir, teorinin parametresi değildir:

| $k_2$ | Kayma açısı $\varepsilon$ | Karşılık gelen $Q$ |
|---|---|---|
| $0{,}35$ | $2{,}10^\circ$ | 13,7 |
| $0{,}30$ | $2{,}45^\circ$ | 11,7 |
| $0{,}25$ | $2{,}94^\circ$ | 9,8 |
| $0{,}20$ | $3{,}68^\circ$ | 7,8 |

$$\boxed{\;\varepsilon \approx 2^\circ\!-\!3{,}5^\circ\;}$$

Gözlemle bildirilen ~$3^\circ$ bu bandın içindedir ✓. Dahası, çıkan kalite çarpanı $Q\approx8\!-\!14$, Dünya için bağımsız olarak bilinen düşük gelgit $Q$'suyla (~12, okyanus yitiminin baskınlığının imzası) örtüşür ✓. İki bağımsız gözlem — uzaklaşma hızı ve $Q$ — aynı açıyı verir.

> **Dürüst kayıt.** Bu hesap bir **ayırt edici sınav değildir.** Kullanılan tork bağıntısı standart gelgit kuramınınkiyle aynıdır ve $k_2$ ile $Q$ malzeme özellikleridir; ne teoriden türetilirler ne de standart kuramda türetilir (ikisi de ölçümle sabitlenir). Kaymanın kaynağı atomik olduğu için burada teoriye özgü bir öngörü **yoktur** ve olması da beklenmemelidir.
>
> *Bu kalem bir ayırt edici öngörü adayı **değildir**: yukarıdaki üç gerekçe ortam kuplajını dışlar, dolayısıyla kayma Ek M-43'ün altkritik bastırmasından çıkarılamaz.*

### Teorinin bu alanda söyleyebileceği tek ayrı şey: sıfırlanmayan taban

Malzeme sürtünmesi tümüyle sıfır olan bir gövde düşünülürse, standart kuram kayma açısının **tam olarak sıfır** olmasını gerektirir. Teoride ise $\eta_E\ne0$'dır; dolayısıyla sıfırlanmayan bir **artık kayma tabanı** kalır. İki kanalın faz katkıları gevşeme zamanlarıyla ters orantılı olduğundan bu tabanın büyüklüğü doğrudan yazılabilir:

$$\varepsilon_E \;\approx\; \varepsilon_{madde}\cdot\frac{\tau_{madde}}{\tau_E} \;\approx\; 3^\circ \times 4{,}0\times10^{-23} \;\approx\; \boxed{\;1\times10^{-22}\ \text{derece}\;}$$

*(Geçerli $\eta_E$ sınırıyla. Bu bir **taban** olduğu için sınır sıkılaştıkça küçülür: süpersedilmiş Phoebe sınırı aynı ifadede $2\times10^{-16}$ derece verirdi, yani $10^{-22}$ rakamı tabanın kendisi değil onun bugünkü en iyi **üst** kestirimidir. Hangi rakam alınırsa alınsın sonuç değişmez.)*

Sayı, ayrımın hem gerçek hem de ölçülemez olduğunu aynı anda söyler: **sıfır değildir** (standart kuramın gerektirdiğinden farklıdır) ama Dünya'da maddesel terimin yirmi iki mertebe altındadır. Bugün bir sınav oluşturmaz ve oluşturuyormuş gibi sunulmaz.

Kalemin sınanabilir hâle gelmesi, maddesel yitimin ihmal edilebilir olduğu ve gözlem penceresinin milyar yıl mertebesine uzadığı bir sistem gerektirir — yani tam olarak teorinin $\eta_E$'yi zaten kullandığı rejim (retrograd uydu göçü, kilitlenme zamanları, halka sönümü; Bkz. 11.3.2 ve Ek M-43).

**Kapsam kaydı:** Bu, *kayma kanalında* ayırt edici sınav bulunmadığı anlamına gelir — bölümün ayırt edici sınavı burada değil, 11.1.8'dedir (kilitli kaynak ile dönen kaynağın tensör yapısı). İki kalem karıştırılmamalıdır: kayma açısı standart kuramla ortaktır, kaynağın dönme durumuna bağlı tensör yapısı ise değildir.

---

## 11.1.10 Geçerlilik Sınırı ve Açık Kalemler

**Geçerlilik sınırı.**

- $b\ll r$ birinci mertebe açılımıdır; $O(\xi^2)$ terimleri ihmal edilmiştir. Ay için $b/r\approx0{,}017$, hata mertebesi ~%2. Kuvvet 2'nin taban eğiminden gelen $\ell=2$ artığı (11.1.3) bu bandın **içindedir** — kaynak payı $a_2\sim a_1$ mertebesinde kaldığı sürece %0,6–%1,7 — ayrı bir hata kalemi değildir.
- İz sıfırlığı yalnız **kaynaksız** bölgede geçerlidir. Gövde içinde ($r<b$) akı sabit değildir, kapsanan nükleon sayısıyla büyür. Kaynak yoğunluğu $n_n=\rho_{madde}/m_n$ ile $\nabla^2P=Cq_n\rho_{madde}/m_n$ olur; Ek M-35'in $\mathcal{G}=\frac{Cq_n}{4\pi\rho_n m_n}$ ayrıştırması konduğunda tensör iz kazanır:

$$\mathrm{tr}\,\mathsf{T}\big|_{i\varsigma} = -4\pi\mathcal{G}\,\rho_{madde}$$

  Yani teori, gövde içinde Poisson denkleminin tam karşılığını üretir — yeni parametre girmeden, doğru katsayıyla. Bu bir öngörü değil, bir **tutarlılık kapanışıdır**: dışarıda sıfır, içeride $-4\pi\mathcal{G}\rho$.
- Denge gelgiti *statik* tepkidir; gerçek gelgit gecikmeli ve dinamiktir.
- Kuvvet envanteri argümanı (11.1.2) **kilitli kaynak** içindir. Serbest dönen bir kaynağın $\omega_1$ kolu açıktır; o durumda Kuvvet 4/5 katkılarının ayrıca tartılması gerekir (11.1.8).
- **Ölçülen gövdenin kendi dönüşü hesaba katılmamıştır — bilinçli bir asimetri.** 11.1.6'nın geri-getirici ivmesi $g=\mathcal{G}M_\oplus/b^2$ küresel ve dönmeyen bir Dünya varsayar. Oysa Dünya serbest döner: kendi $\omega_1$ kolu **açıktır**, dolayısıyla kendi F4/F5'ini taşır ve yüzeyi küre değildir. Bölümün mantığı gereği bu tutarsızlık değil, iş bölümüdür — fakat kaydedilmesi zorunludur, çünkü 11.1.8 kaynağın Dünya'ya göre dönmesini belirleyici sayarken 11.1.6 ölçen gövdenin kendi dönüşünü ihmal eder. Gerekçe: iki etki farklı mertebelerde ve farklı geometrilerde girer. Gövdenin kendi F4/F5'i **eksenel-simetrik ve zamanla sabit** bir figür deformasyonu üretir (basıklık, $J_2$ imzası); gelgit ise gelgit eksenine kilitli ve **günlük periyotta dolaşan** bir artıktır. Birincisi ortalama figüre, ikincisi onun üzerindeki salınıma yazılır ve birinci mertebede ayrışırlar. Gövdenin figür hesabı **11.2'nin konusudur**; oradaki $\sin2\theta$ yasası bu bölümün $g$'sini küresel değerinden ne kadar saptırdığını verir. Denge gelgiti genliğine etkisi $\Delta\zeta$'nın kendisiyle değil, $g$'deki enlemsel değişimle ölçeklenir (~%0,5 mertebesi) ve bölümün mertebe iddiasını değiştirmez.

**Kapanmış kalem — uzaklaşmanın bileşenleri.** Yukarıdaki kayma hesabı, Ay'ın ölçülen 3,8 cm/yıl'lık uzaklaşmasının **tamamını** öne kaymış şişkinliğin lob torkuna yükler. Bu varsayımın kendisi artık bağımsız olarak doğrulanmıştır (3.9.4): Dünya'nın kaybettiği açısal momentum ($-4{,}93\times10^{16}$ kg·m²/s², gün uzaması 2,3 ms/yüzyıldan) ile Ay'ın kazandığı ($+4{,}50\times10^{16}$, LLR'den) **%91 doğrulukla** dengelenir — bütçe gelgit aktarımıyla tek başına kapanır.

Kozmolojik seyrelme, bu tablonun üzerine binen ve **çok daha yavaş bir taban terimidir** ($\lesssim$%10). Kayma açısı bunu bağımsız olarak da doğrular: taban terimi kayda değer bir pay taşısaydı ($\%72$, yani naif $r H_0$ tahmini kadar) lob'a kalan pay 3,6 kat azalır ve geri çözülen açı $0{,}7^\circ$'ye düşerdi — gözlenenin dörtte biri. *(3.9.4'ün sıralama kaydı da aynı hükmü verir: uzaklaşmanın asıl kaynağı gelgit frenlemesidir, kozmolojik seyrelme yalnız üzerine binen yavaş bir tabandır. Ayrıştırılamayan ~%9'luk artığın sınanması 7.4'ün kalemidir.)*


---

## 11.1.11 Klasik Gelgit Türevinin Vektörel Tutarsızlığı

Bu alt bölüm, klasik diferansiyel kütleçekim (tidal force) türevinin standart Newton mekaniği çerçevesinde dahi **nedensellik kırığı** içerdiğini göstermekte; söz konusu kırığın hem koordinat analizi hem de iş-enerji ilkesi üzerinden kapatılamaz olduğunu ortaya koymaktadır. Argüman Evrenakı'ya özgü bir önerme içermez: tümüyle klasik mekaniğin kendi araçlarıyla yürütülmüştür.


<iframe src="/animasyonlar/gelgit_vektor.html" width="100%" height="340" style="border:none;border-radius:12px;display:block;margin:24px auto;" title="Şekil 11.1.11-A — Klasik Modelin Vektör Çelişkisi ve Basınç Modeli Çözümü" loading="lazy"></iframe>



### 11.1.11.1 Eylemsiz Sistemde Gerçek Kuvvet Vektörleri


Dünya'nın kütle merkezini eylemsiz koordinat orijini $\mathbf{0}$ olarak seçelim; Ay'ı $+\hat{x}$ yönünde $r$ uzaklığına yerleştirelim. Dünya'nın arka yüzeyindeki (Ay'a zıt) bir sıvı parçacığının koordinatı $\mathbf{x}_P = -b\,\hat{x}$ ($b \approx R_\oplus$) olsun.

Newton kütleçekimi yalnızca **çekici** bir kuvvettir; vektörü daima kaynak kütleye doğru gösterir. Dolayısıyla eylemsiz sistemde parçacık $P$ üzerindeki gerçek ivmeler:

$$\vec{a}_{D} = +\frac{\mathcal{G}M_\oplus}{b^2}\,\hat{x} \qquad \text{(Dünya'nın çekimi, merkeze = } +\hat{x} \text{ yönünde)}$$

$$\vec{a}_{A} = +\frac{\mathcal{G}M_{Ay}}{(r+b)^2}\,\hat{x} \qquad \text{(Ay'ın çekimi, Ay'a = } +\hat{x} \text{ yönünde)}$$

Net gerçek ivme:

$$\boxed{\vec{a}_{net}^{(P)} = \left[\frac{\mathcal{G}M_\oplus}{b^2} + \frac{\mathcal{G}M_{Ay}}{(r+b)^2}\right]\hat{x}}$$

**Her iki katkı da $+\hat{x}$ yönlüdür.** Eylemsiz sistemde $P$ noktasında $-\hat{x}$ yönünde (uzaya doğru) etki eden sıfır gerçek kuvvet bulunmaktadır.

### 11.1.11.2 Diferansiyel İvme Türevi ve İşaret Kırığı

Klasik gelgit türevi, parçacık $P$'nin Dünya'nın kütle merkezine *göre* ivmesini hesaplamak için merkez ivmesini referans alır ve bağıl ivmeyi şöyle tanımlar:

$$\vec{a}_{bağıl}^{(P)} \equiv \vec{a}_{A}^{(P)} - \vec{a}_{A}^{(M)} = \frac{\mathcal{G}M_{Ay}}{(r+b)^2}\,\hat{x} - \frac{\mathcal{G}M_{Ay}}{r^2}\,\hat{x}$$

Taylor açılımıyla ($b \ll r$):

$$\vec{a}_{bağıl}^{(P)} \approx -\frac{2\mathcal{G}M_{Ay}b}{r^3}\,\hat{x}$$

Bu eksi işaret, klasik gelgit anlatısındaki "arka yüzeyin uzaya doğru kabarması" olgusunun matematiksel kaynağıdır. Ancak bu değerin fiziksel yorumu dikkatle incelenmelidir.

**Önemli kayıt:** Yukarıdaki türev, gerçek bir kuvvetin $-\hat{x}$ yönünde etki ettiğini göstermez. Gösterdiği şey, Ay'ın arka yüzey parçacığını merkeze göre *görece* daha yavaş çektiğidir; merkez $a_{A}^{(M)} = \mathcal{G}M_{Ay}/r^2$ ivmesiyle Ay'a düşerken parçacık $a_{A}^{(P)} = \mathcal{G}M_{Ay}/(r+b)^2$ ivmesiyle daha yavaş düşmektedir. Negatif bağıl ivme, **her iki ivmenin de pozitif olduğu iki sayı arasındaki farktır**; fiziksel bir itme kuvvetinin değil, koordinat referans seçiminin ürünüdür.

### 11.1.11.3 İş-Enerji Testi: Kapatılamaz Enerji Açığı

Gelgit kabarması fiziksel bir iştir: okyanus suyunun $\Delta h \approx 0{,}5$ m yükselmesi için hacim $V_{su} \sim 10^{17}$ m³ üzerinden yaklaşık $W \sim \rho g V \Delta h \sim 10^{20}$ J mertebe potansiyel enerji kazanılmaktadır.

Klasik gelgit anlatısına göre bu enerji, Ay'ın arka yüzey suyunu "daha az çekmesinden" kaynaklanmaktadır. Ancak iş ilkesi gereği $W = \vec{F} \cdot \Delta\vec{r}$; kuvvetin yokluğu ya da azalması iş üretmez. Daha kesin ifadeyle:

$$\Delta W_{arka} = \vec{a}_{bağıl}^{(P)} \cdot m\,\Delta\vec{r} = \left(-\frac{2\mathcal{G}M_{Ay}b}{r^3}\right)\cdot m\,\Delta r$$

Koordinat dönüşümünden türeyen $\vec{a}_{bağıl}$ terimi, serbest düşen (eylemsiz olmayan) bir referans çerçevesine ait *sözde (fiktif) bir ivmedir*. Standart mekanik pratiğinde sözde kuvvetler koordinat bütçesini kapamak için meşru araçlardır; ancak şu koşullarla:

1. Sözde kuvvetin **açıkça fiktif olarak beyan edilmesi** zorunludur.
2. Fiktif kuvvetlerin kendine özgü bir enerji kaynağı bulunmaz; enerji dengesi eylemsiz sistemde kurulmalıdır.

Klasik ders kitabı anlatısında bu iki koşul sistematik biçimde karşılanmamakta, bağıl ivmenin "Ay'ın arka suyu uzaya doğru çektiği" biçiminde yorumlanmasına zemin hazırlanmaktadır. Bu yorum $W > 0$ ile bağdaşmaz: eylemsiz sistemde arka yüzeye uygulanan gerçek net kuvvet $+\hat{x}$ yönlüdür; dolayısıyla uzaya ($-\hat{x}$) doğru kaldırma işi için gerçek bir kaynak yoktur.

### 11.1.11.4 Üç Cisim Genelleme Testi

Diferansiyel ivme yönteminin koordinat hilesi olduğu, aynı matematiğin keyfi bir sistemde ürettiği çelişki ile daha açık görülmektedir.

Uzayda sıralı üç cisim düşünelim: $C_1$, $C_2$ (merkez, Dünya rolü), $C_3$ (büyük çekici, Ay rolü). Aralarındaki eşit uzaklık $d$ olsun. Eylemsiz sistemde $C_3$'ün yarattığı gerçek ivmeler:

$$a_1 = \frac{\mathcal{G}M_3}{(2d)^2} = \frac{\mathcal{G}M_3}{4d^2} > 0\,, \qquad a_2 = \frac{\mathcal{G}M_3}{d^2} > 0$$

Her iki ivme de $+\hat{x}$ (yani $C_3$'e doğru) yönlüdür. $C_1$, $C_3$'e doğru ivmelenmektedir.

Klasik diferansiyel ivme türevi $C_2$'yi referans alarak uygulansa:

$$\vec{a}_{bağıl,1} = a_1 - a_2 = \frac{\mathcal{G}M_3}{4d^2} - \frac{\mathcal{G}M_3}{d^2} = -\frac{3\mathcal{G}M_3}{4d^2}$$

Sonuç $-\hat{x}$ yönlüdür, yani yöntem $C_1$'in $C_3$'ten **uzaklaştığını** öngörmektedir. Oysa kütleçekimi yalnızca çeker; her iki cisim de birbirlerine ve $C_3$'e doğru ivmelenmektedir. $C_2$'nin ön tarafındaki bir $C_0$ cismi için aynı işlem:

$$\vec{a}_{bağıl,0} = \frac{4\mathcal{G}M_3}{d^2} - \frac{\mathcal{G}M_3}{d^2} = +\frac{3\mathcal{G}M_3}{d^2}$$

Bu kez de $+\hat{x}$, yani $C_0$ da $C_2$'den uzaklaşıyor görünmektedir. Yöntemin ürettiği tablo: ortadaki cisim ($C_2 \equiv$ Dünya), hem önündeki hem de arkasındaki cisimleri kendinden uzağa doğru itmektedir — kütleçekiminin yalnızca çekici olduğu bir evrende fiziksel olarak imkânsız bir önermedir.

Bu sonuç, diferansiyel ivme türevinin **eylemsiz sistemde tek başına fiziksel vektör üretemeyeceğini** ve ancak serbest düşen referans çerçevesindeki koordinat dönüşümünün bir yapay ürünü olarak anlam taşıdığını kanıtlamaktadır.

### 11.1.11.5 "Non-İnertial Referans Meşrudur" İtirazının Sınırları

Yukarıdaki analiz karşısında yapılabilecek standart itiraz şudur: *"Serbest düşen (non-inertial) referans çerçevesinde merkezkaç terimi ortaya çıkar; bu fiziksel olarak meşrudur."*

Bu itiraz kısmen doğrudur: non-inertial sistemlerde sözde (fiktif) kuvvetlerle çalışmak standart bir araçtır. Ancak bu meşruiyetin üç sınırı bulunmaktadır:

**(i) Beyan zorunluluğu.** Sözde kuvvet kullanıldığında hesabın ivmeli referans çerçevesine ait olduğu ve ortaya çıkan kuvvetin koordinat yapısı olduğu açıkça belirtilmelidir. Klasik gelgit açıklamalarının büyük çoğunluğu bu ayrımı yapmaz ve bağıl ivme değerini doğrudan "Ay'ın arka taraftaki suyu uzaya itmesi" olarak yorumlar.

**(ii) Enerji kapanışı.** Sözde kuvvetlerin kendine özgü potansiyel enerji depolama kapasitesi yoktur. Bir kilogram suyun 0,5 m yükselmesi için ~5 J enerji gereklidir. Bu enerjinin eylemsiz sistemdeki kaynağı, sözde kuvvet çerçevesinde gösterilmelidir. Standart anlatı bu muhasebeden kaçınmaktadır.

**(iii) Genelleme kırığı.** Yukarıdaki üç cisim testi, aynı sözde kuvvet matematiğinin, kütleçekimi altında birbirine yaklaşan cisimlerin birbirinden uzaklaştığını "öngörmesine" yol açtığını göstermektedir. Sözde kuvvet bileşeni bu genelleme kırığını açıklamaz; yalnızca orijin seçiminin neden özel tutulması gerektiği sorusunu ertelemektedir.

### 11.1.11.6 Geoid Gözlem Testi

Eğer klasik model tam doğru olsaydı ve Ay, Dünya'nın katı gövdesini suyun altından Ay yönünde çekiyor olsaydı, Dünya'nın uzun dönemli denge figüründe (Geoid) hem Ay'a bakan hemde Ay'a ters yüzlerde katı kabukta belirgin yükselmeler gözlemlenmeliydi. Jeodezi ölçümleri bunu desteklememektedir: Geoid anomalileri kıtasal kütle dağılımı, izostatik ayarlama ve manto konveksiyonuyla açıklanmakta; Ay yönlü bir ikili şişkinlik **katı kabukta** yalnızca ~30 mm mertebesinde tespit edilmekte ve bu değer doğrudan gelgit potansiyeliyle uyumludur. Söz konusu deformasyon, Dünya'nın katı kabuğunun Ay'a doğru *çekildiğini* (gerçek kuvvet: $+\hat{x}$) göstermekte; klasik anlatının ima ettiği arka yüzde özerk bir "eksi kuvvet" bileşeninin varlığına kanıt teşkil etmemektedir.

### 11.1.11.7 Bölüm Özeti

| Soru | Klasik Yanıt | Analitik Kırık |
|---|---|---|
| Arka yüzdeki kabarmayı üreten kuvvet nedir? | Ay'ın arka suyu **daha az** çekmesi | Kuvvet eksikliği $-\hat{x}$ yönünde iş yapamaz: $W = F \cdot x$, $F_{\hat{x}} = 0 \Rightarrow W = 0$ |
| Bağıl ivmedeki eksi işaretin kaynağı nedir? | Diferansiyel çekim | İki pozitif sayı arasındaki fark; eylemsiz sistemde $-\hat{x}$ yönlü gerçek kuvvet yoktur |
| Non-inertial referans bunu kurtarır mı? | Evet, serbest düşen çerçevede sözde kuvvet meşrudur | Sözde kuvvet enerji üretmez; beyan edilmez; üç cisim genellemesinde kütleçekimini itici gösterir |
| Gözlem uyumu nedir? | Gelgit gözlemlenmektedir | Gözlem gelgiti doğrular; açıklama mekanizmasını değil. Geoid, $-\hat{x}$ kuvvetini desteklememektedir |

Klasik diferansiyel gelgit türevinin ürettiği negatif bağıl ivme değeri, eylemsiz koordinat sisteminde gerçek bir kuvvete karşılık gelmemektedir. Bu değer, orijinin serbestçe düşen Dünya merkezine sabitlenmesinin koordinat yapay ürünüdür. Söz konusu ayrımın farkında olunması, teorilerin hidrodinamik ve enerji muhasebesi testlerine karşı dürüstçe değerlendirilmesi açısından zorunludur.

---

Bir sonraki bölüm aynı basınç matematiğini dönen gövdenin kendi figürüne uygular: 11.2, Yanal İtimin $\sin2\theta$ yasasını türetir ve gezegen basıklığının klasik hidrostatik dengeden nerede ayrıldığını gösterir.

