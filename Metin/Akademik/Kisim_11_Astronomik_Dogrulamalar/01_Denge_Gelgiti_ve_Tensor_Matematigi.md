# 11.1 Diferansiyel Sıkıştırma: Gelgit Tensörü ve Denge Gelgiti

Okyanuslar çekilmez — **sıkılır.** Kısım 3.9'da kurulan mekanizmanın özü budur: Dünya, Evrenakı denizinin içinde her an, her yönden sıkışmış hâlde duran bir gövdedir ve gelgit, bu sıkışmanın Ay tarafından **asimetrikleştirilmesidir.** Gelgidin asıl kaynağı, boş uzaydan uzanan görünmez bir "çekme" değil, gövdenin zaten içinde yaşadığı **Evrenakı sıkıştırmasıdır — Kuvvet 2.** Ay'ın yaptığı tek şey, bu sıkıştırmanın haritasını değiştirmektir: kütle-itim alanının (Kuvvet 1) gövde üzerindeki yönlü farkı, sıkıştırmayı gelgit eksenini saran kuşakta **pekiştirir**, eksenin iki ucunda **gevşetir.** Su, pekişen mengeneden kaçıp gevşeyen iki uca pompalanır. Sıkıştırma nedendir; kabarma sonuçtur.

Bu bölüm o mekanizmayı sayıya döker. Türetim, sıfır serbest parametreyle şunları üretir: gelgit alanının $1/r^3$ yasası, tensörün $(+2,-1,-1)$ özdeğer yapısı, $0{,}535$ m'lik denge genliği, Güneş/Ay oranı $0{,}460$ ve büyük/küçük gelgit oranı $2{,}70$ — hepsi gözlemle uyum içinde. Cebirin biçimi tanıdıktır: bir alanın ikinci türevleri. Teorinin gücü yeni bir matematik icat etmesinde değil, o türevin **neyin** türevi olduğunu ve suyu **neyin** ittiğini gösterebilmesindedir: standart fizikte kabarmanın yerinde bir nedeni yoktur — burada vardır, adı konmuştur ve her noktada içe bakan gerçek bir basınçtır.

Bölümün sonunda mekanizma iddiası ölçüme bağlanır: kilitli bir kaynağın (Ay) gelgit tensörü ile Dünya'ya göre dönen bir kaynağın (Güneş) gelgit tensörü, teoride **yapıca** farklıdır — Newton'da ise kaynağın dönmesi dış alana hiç girmez. Dünya iki kaynağı aynı anda, aynı aletlerle ölçtüğü için bu, kurulmayı bekleyen değil hâlihazırda işleyen bir **doğal diferansiyel deneydir** (11.1.8).

---

## 11.1.1 Notasyon ve Varsayımlar

**Notasyon**

| Sembol | Anlam |
|---|---|
| $M$ | Gelgiti yaratan kaynağın kütlesi (Ay veya Güneş) |
| $r$ | Kaynak ile gövde merkezi arası uzaklık |
| $b$ | Gövde yarıçapı (Dünya), $b\ll r$ |
| $\vec\xi$ | Gövde merkezinden ölçülen iç konum, $\lvert\xi\rvert\le b$ |
| **gelgit ekseni** | Gövde merkezini kaynağa bağlayan doğrultu (Dünya–Ay doğrultusu). **Dünya'nın dönme ekseni değildir** — 11.1.3'teki uyarıya bkz. |
| $\psi$ | $\vec\xi$ ile **gelgit ekseni** arasındaki açı |
| $\Phi$ | İtim potansiyeli, $\Phi\equiv(P-P_0)/\rho_n$ (Kuvvet 1'e ait) |
| $a_2$ | Kuvvet 2'nin taban sıkıştırma büyüklüğü; yönden bağımsızdır, $r$'ye bağlı olabilir (ivme boyutunda) |
| $\Psi_T$ | Gelgit potansiyeli (ortak taşınma çıkarıldıktan sonraki artık) |
| $\zeta$ | Serbest yüzey yükseltisi (Ek D · S-27) |
| $\rho_c$ | Gövdenin ortalama kütle yoğunluğu (Dünya: $5{,}515\times10^{3}$ kg/m³) — 11.1.9'da kullanılır |
| $\ell$ | Küresel harmonik derece (yük ve tepkinin açısal mertebesi) |

**Varsayımlar**

1. **Kuvvet 1 geçerlidir:** $P(r)=P_0-\alpha M/r$, dolayısıyla $a_r=-\mathcal{G}M/r^2$ ve $\mathcal{G}=\alpha/\rho_n$ (Ek M-35).
2. **Kuvvet 2 geçerlidir:** gövde, yönsüz taban sıkıştırması $a_2$ ile her yönden sıkılmış hâldedir (Ek M-36). Gövde ölçeğinde sabit olduğu **varsayılmaz**; $r$'ye bağlı olmasına izin verilir. Büyüklüğünün ve radyal yasasının şekli neden etkileyemediği 11.1.3'te türetilir — bu, sıkıştırma denizinin derinliğinin ölçülmesine gerek kalmadan öngörü üretilebilmesi demektir.
3. **Uzanımlı gövde:** $b\ll r$; açılım **ivme alanında** birinci mertebede (potansiyelde ikinci mertebede) kesilir. Dünya–Ay için $b/r\approx0{,}017$. Bir üst mertebe yalnız hata kestirimi için yazılır (11.1.3, 11.1.10).
4. **Akı korunumu:** Kaynaktan uzakta Kuvvet 1'in deplasman akısı ne yaratılır ne yok edilir. 11.1.4'te nicel biçime sokulur.
5. **Evrensel $\rho_n$:** Nükleon öz yoğunluğu bileşimden bağımsızdır ($2{,}7\times10^{17}$ kg/m³). Kuvvet 1 bu yüzden gövdenin *her* nükleonuna aynı ivmeyi verir.
6. **Kaynak, Dünya'ya göre dönmemektedir:** Ay gelgit kilitlidir; Dünya–Ay doğrultusuna göre dönme hızı **tam olarak sıfırdır** ve makro-girdabı bastırılmıştır (Bkz. 3.9.1). Dolayısıyla Dünya'ya yalnız pompa kolu (Kuvvet 1 + Kuvvet 2) etki eder; $\omega_1$ kökenli kuvvetler devrede değildir. Ayrımın çerçevesi 11.1.8'de netleştirilir.

---

## 11.1.2 Kuvvet Envanteri: Mengene ve Harita

Postülat 9'un beş hidrodinamik kuvveti iki köke ayrılır:

| Kol | Kuvvetler | Kilitli kaynakta |
|---|---|---|
| $\omega_2$ — **pompa** (boyutsal salınım) | **1** Radyal kütle-itim · **2** Sıkıştırma | **açık** |
| $\omega_1$ — **dönüş** (makro-vorteks) | 3 Vorteks sürüklenmesi · 4 Eksenel itim · 5 Yanal itim | **kapalı** |

Ay Dünya'ya göre dönmediği için envanter gelgit probleminde kendiliğinden sadeleşir: gelgit kilidi, gövdenin dönüşünü yörünge dolaşımıyla aynı faza oturtur; Dünya–Ay doğrultusuna göre bağımsız bir sirkülasyon kalmaz ve Ay'ın kendi makro-girdabı bastırılmıştır (Bkz. 3.9.1 ve 3.4.4 — girdap rekabeti). Dönüş kolu kapalı bir kaynak Dünya'ya vorteks sürüklenmesi, eksenel itim veya yanal itim uygulayamaz — bu üç kuvvetin taşıyıcısı yoktur. Geriye pompa kolunun iki kuvveti kalır ve gelgit tam olarak bu ikisinin iş bölümüdür:

- **Kuvvet 2 mengenedir.** Gövdeyi fiilen sıkan, suyu fiilen iten basınç odur. Dünya bu sıkıştırmanın *içinde* durur; gelgit olsun olmasın, mengene her an kapalıdır.
- **Kuvvet 1 haritadır.** Ay'ın kütle-itim alanı yakın yüzde güçlü, uzak yüzde zayıftır; bu yönlü fark, mengenenin **nerede pekişip nerede gevşeyeceğini** çizer. Kendisi suyu kaldırmaz — sıkıştırmayı yeniden dağıtır.

Bu iş bölümünün hesap açısından bedeli sıfırdır: aşağıda görüleceği gibi mengenenin mutlak derinliği ($a_2$) şekil farkında düşer, harita ise tek bir gradyanla çizilir — hesaba tek bir serbest katsayı girmez. Mekanizma gerçek anlamda **ikilidir**; sayı tek bir gradyana iner. İkisini karıştırmamak, bu bölümün her adımında işleyecek olan ayrımdır: *genliği harita belirler, işi mengene yapar.*

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

### Kuvvet 2 — sıkıştırma denizi

Kuvvet 1 ile Kuvvet 2 aynı $\omega_2$ (pompa/boyutsal salınım) kanalından beslenir (Ek M-36) ve tek bir basınç alanının iki yüzüdür: **Kuvvet 2 alanın düzeyidir** — gövdeyi bir noktada her yönden aynı büyüklükte sıkan hâl, $a_2$; **Kuvvet 1 aynı alanın eğimidir** ve yönlüdür. Gelgit, düzeyin eğim tarafından modüle edilmesidir: deniz sıkar, harita yön verir.

Yönsüz sıkıştırmanın tek başına şekil bozamayacağı geometrinin zorunlu sonucudur: yönden bağımsız bir büyüklük gövdenin hiçbir noktasını diğerinden ayırt edemez; gövdeyi yalnız hacimce sıkar, ovalleştirmez. Şekil bozmak için sıkıştırmanın **asimetrikleşmesi** gerekir — ve tam da bu yüzden gelgit, Kuvvet 2'nin iptali değil **etkinleşmesidir:** simetrik mengene görünmezdir, asimetrik mengene okyanusu kaldırır.

#### Sıkıştırma denizinin derinliği hesaba girmek zorunda değildir

Öngörünün parametresizliği buradan gelir ve varsayılmaz, türetilir. Kaynağın kendi payını taşıyan bir sıkıştırmanın $r$'den bağımsız olması beklenemez; $da_2/dr\ne0$ ise yakın yüz uzak yüzden farklı sıkışır ve bu fark $O(b/r)$ mertebesindedir — Kuvvet 1'in gelgit terimiyle aynı mertebe. Soru bu yüzden ciddiyetle kapatılmalıdır: tabanın $r$ bağımlılığı şekle karışır mı?

Tabanı gövde üzerinde açalım ($\xi_\parallel\equiv\vec\xi\cdot\hat r=\xi\cos\psi$; $a_2'\equiv da_2/dr$):

$$a_2(\vec r+\vec\xi) \;=\; \underbrace{a_2(r)}_{\ell=0} \;+\; \underbrace{a_2'(r)\,\xi\cos\psi}_{\ell=1} \;+\; \underbrace{\tfrac12 a_2''(r)\,\xi^2\cos^2\psi}_{\ell=0\,\oplus\,\ell=2} \;+\; O(\xi^3)$$

Şekle katkıyı terimlerin büyüklüğü değil **açısal mertebeleri ($\ell$)** belirler. Gelgit bir $\ell=2$ olgusudur; bir yükün gelgide karışabilmesi için $P_2(\cos\psi)$ ile örtüşmesi gerekir.

**$\ell=0$ — hacim, şekil değil.** İzotropik terim gövdenin hiçbir noktasını diğerinden ayırt edemez; sıkışabilir gövdede hacmi küçültür, şeklini değiştirmez.

**$\ell=1$ — yer değiştirme, şekil değil.** Doğrusal terim $\cos\psi$ ile gider, yani **tektir**: gelgit ekseninin iki ucunda eşit büyüklükte ve zıt işaretlidir; $P_2$ ile örtüşmesi özdeş olarak sıfırdır ($\int_{-1}^{1}P_1P_2\,d\mu=0$). Serbest bir gövdeye uygulanan $\ell=1$ yükünün denge tepkisi **rijit yer değiştirmedir** — küresel bir yüzeyin $\ell=1$ deformasyonu, tanımı gereği o kürenin ötelenmesidir. Fiziksel okuma: yakın yüzü uzak yüzden sert sıkan bir taban gövdeye **net kuvvet** uygular; o kuvvet yörünge hareketine yazılır, şekle değil. Bu sonuç $a_2$'nin **ne büyüklüğüne ne radyal yasasına** bağlıdır — taban ne kadar derin olursa olsun, birinci mertebe artığının gelgit tensörüne katkısı özdeş olarak sıfırdır.

**$\ell=2$ — tek gerçek katkı, bir mertebe daha küçük.** Şekle karışabilecek yegâne terim ikinci türevdir. $\cos^2\psi=\tfrac13+\tfrac23P_2(\cos\psi)$ ile $\ell=2$ payı $\tfrac13a_2''\,\xi^2P_2$'dir; Kuvvet 1'in gelgit terimiyle oranı ($a_1\equiv\mathcal{G}M/r^2$, $a_2\propto r^{-n}$ için $a_2''r^2=n(n{+}1)a_2$):

$$\frac{\bigl|\text{Kuvvet 2'nin }\ell{=}2\text{ payı}\bigr|}{\bigl|\text{Kuvvet 1'in gelgit terimi}\bigr|} \;=\; \frac{n(n+1)}{6}\cdot\frac{a_2}{a_1}\cdot\frac{b}{r}$$

Dünya–Ay'da $b/r=0{,}0166$ ve kaynak payı $a_2\sim a_1$ mertebesinde kaldığı sürece bu, $n=1$ için $\%0{,}6$, $n=2$ için $\%1{,}7$'dir — 11.1.10'da ilan edilen $O(\xi^2)$ kesme hatasının ($\sim\%2$) içinde kalır.

Teorinin kendi yapısı aynı sonucu daha keskin söyler: tabanın kaynağa ait payının radyal eğimi **yeni bir kuvvet değildir.** Ek M-35'in alanında düzeyin kaynak payı $P(r)-P_0=-\alpha M/r$'dir; eğimi alınırsa

$$\frac{1}{\rho_n}\frac{d}{dr}\bigl[P(r)-P_0\bigr] \;=\; \frac{\alpha M}{\rho_n r^{2}} \;=\; \frac{\mathcal{G}M}{r^{2}} \;=\; \lvert\vec a_1\rvert$$

— **Kuvvet 1'in kendisi çıkar.** Teoride tek bir basınç alanı vardır; düzeyin eğimi ile eğimin kendisi aynı nesnedir, tensöre ayrıca bir $da_2/dr$ kalemi eklemek aynı fiziği iki kez saymak olurdu. Tabanın geri kalan payı — gövdeyi çevreleyen $P_0$ arka basıncı — evrendeki bütün maddenin $\omega_2$ kolektifinin kurduğu denge düzeyidir; Dünya–Ay ölçeğinde gradyansızdır.

**Sonuç.** $a_2$'nin ne değeri ne radyal yasası bu türetimde sabitlenir — sabitlenmesine gerek kalmadığı türetilmiştir. Sıkıştırma denizi hesaba derinliğiyle değil **varlığıyla** girer; gelgit onun modülasyonunu okur.

### Kuvvet 1 — yönlü gradyan

Kütle-itim yasası $\vec a_1=-\frac{1}{\rho_n}\nabla P$'dir. $\rho_n$ sabit olduğundan ifade tam bir potansiyele indirgenir:

$$\Phi \equiv \frac{P-P_0}{\rho_n} \;\Longrightarrow\; \vec a_1 = -\nabla\Phi,\qquad \Phi(r)=-\frac{\mathcal{G}M}{r}$$

Bu, standart fizikten ödünç alınmış bir "kütleçekim potansiyeli" **değildir**: basınç alanının nükleon öz yoğunluğuna bölünmüş hâlidir. Değeri aynı, kökeni ve nesnesi farklıdır — burada $\Phi$'nin arkasında gerçek bir akışkanın gerçek basıncı durur.

Gövde merkezi $\vec r$'de, okyanus noktası $\vec r+\vec\xi$'dedir. İvme alanı açılır:

$$\vec a_1(\vec r+\vec\xi) = \vec a_1(\vec r) + (\vec\xi\cdot\nabla)\vec a_1 + O(\xi^2)$$

**Ortak bileşen taşır, deforme etmez.** $\rho_n$ evrensel olduğundan Kuvvet 1 gövdenin her nükleonuna aynı ivmeyi verir; alanın ortak bileşeni $\vec a_1(\vec r)$ gövdeyi bir bütün olarak taşır. Bu, Kuvvet 2 için kurulan mertebe teoreminin bu alandaki karşılığıdır: orada $\ell=0$ ve $\ell=1$ payları gövdeyi sıkıyor ya da kaydırıyordu, burada ortak ivme gövdeyi taşıyor — hiçbiri şekle karışmıyor. Haritayı çizen, ortak ivmeden sapan **artık kısımdır:**

$$\boxed{\;\Delta\vec a_1(\vec\xi) \equiv \vec a_1(\vec r+\vec\xi) - \vec a_1(\vec r) = \mathsf{T}_1\,\vec\xi,\qquad (T_1)_{ij}=\frac{\partial (a_1)_i}{\partial x_j}=-\frac{1}{\rho_n}\partial_i\partial_j P\;}$$

Bu, Kuvvet 1'in kendi gradyan tensörüdür — **henüz gelgit değildir.** Gelgidi üreten, bu gradyanın Kuvvet 2'nin sıkıştırmasını yerel olarak nasıl değiştirdiğidir; ilişki 11.1.4'te kurulur.

$\Delta\vec a_1$ ifadesi $\vec\xi$'de doğrusaldır, dolayısıyla **tektir**: $\Delta\vec a_1(-\vec\xi)=-\Delta\vec a_1(\vec\xi)$. Fakat sıkıştırmaya giren şey bu vektörün kendisi değil, **dışa normal üzerindeki izdüşümüdür** — ve o izdüşüm **çifttir.** Küresel yüzeyde $\hat n=\hat\xi$ olduğundan:

$$\boxed{\;\hat n\cdot\Delta\vec a_1(\vec\xi)\Big|_{\lvert\xi\rvert=b} = b\,\bigl(\hat n\cdot\mathsf{T}_1\cdot\hat n\bigr)\;}$$

Sağ taraf $\hat n$'de bir **karesel formdur**, $\hat n\to-\hat n$ altında değişmez. Gelgit ekseninin iki ucunda izdüşüm birebir aynı değeri alır ($+2\mathcal{G}Mb/r^3$); kuşağın her yerinde yine tek bir değer ($-\mathcal{G}Mb/r^3$).

**Çift şişkinliğin kaynağı budur.** Dünya'nın her iki yüzündeki — Ay'a bakan ve Ay'ın tam zıttındaki — kabarma, hiçbir ek varsayım olmadan bu çift yapıdan çıkar: bir vektörün iki uçta yön değiştirmesinden değil, **sıkıştırmanın iki uçta eşit miktarda gevşemesinden.** Standart anlatının en zorlandığı soru — "Ay arka yüzdeki suyu nasıl kabartıyor?" — teoride hiç doğmaz: arka yüzü kimse kabartmıyor; mengene orada da gevşiyor ve kuşaktan kaçan su oraya da doluyor.

> [!CAUTION]
> **Gelgit ekseni ≠ dönme ekseni.** Bu bölümde geçen her "eksen" sözcüğü, gövde merkezini kaynağa bağlayan **Dünya–Ay doğrultusunu** gösterir; Dünya'nın kendi dönme eksenini (ve dolayısıyla ekvatoru) göstermez. İkisi ne çakışıktır ne paraleldir:
>
> 1. **Yönelim.** Gelgit ekseni kaynağın konumuyla belirlenir; dönme ekseni gövdenin kendi mekaniğiyle. Aralarındaki açı sabit bile değildir — eksen eğikliği ve Ay'ın 5°'lik yörünge eğikliği yüzünden sürekli değişir (Bkz. 3.9.3).
> 2. **Sıkıştırma kuşağı ekvator değildir.** $-1$ özdeğerlerinin tanımladığı çembersel kuşak, **gelgit eksenine** diktir; coğrafi ekvatorla çakıştığı anlar istisnadır, kural değil.
> 3. **Günde iki gelgitin sebebi bu ayrımdır.** Kuşak ve şişkinlikler gelgit eksenine kilitlidir; Dünya bu yapının *altından* kendi ekseni etrafında döner. Yeryüzündeki bir nokta her turda iki şişkinlikten de geçer — günde iki yüksek gelgit buradan gelir (ardışık iki tepe arası, Ay günü nedeniyle 12 sa 25 dk). İki eksen çakışık olsaydı şişkinlikler kutuplarda sabitlenir, gelgit hiç dolaşmazdı.
>
> Aynı geometri iki gelgitin neden eşit olmadığını da verir: gelgit ekseni dönme eksenine eğik olduğundan, bir noktanın gün içinde geçtiği iki şişkinlik farklı enlemlerden kesilir (*günlük eşitsizlik*). **Bölüm 11.2'nin ekseni ise dönme eksenidir** — oradaki Yanal İtim ($\sin2\theta$) gövdenin kendi dönüşünden doğar ve kuşağı gerçekten ekvatordadır.

> [!NOTE]
> **Bernoulli okumasıyla uzlaşma.** Bölüm 3.9.2 gelgiti, Ay'ın Dünya–Ay arasındaki Evrenakı akıntısını hızlandırmasına bağlar: hızın arttığı yerde iç basınç düşer (Bernoulli, 1738). Bu bölümdeki türetim ise statik $P(r)=P_0-\alpha M/r$ alanı üzerinden yürür. İkisi rakip değil, **aynı alanın iki çerçevedeki okunuşudur:** gövdeyle taşınan çerçevede bağıl hız sıfırdır ve alan statik görünür — tensör matematiği bu çerçevede işler; gövdeye göre akan çerçevede aynı basınç yapısı Bernoulli profili olarak okunur. Geçiş terimi, çerçeve adımında çıkarılan ortak taşınma teriminin ta kendisidir. Bütün sayılar statik gradyandan türetilmiştir; Bernoulli okuması mekanizmanın yerel görünümüdür, ikinci bir hesap kalemi değildir.

---

## 11.1.4 Akı Korunumu ve Sıkıştırmanın Yeniden Dağılımı: Gelgit Tensörü

Önce Kuvvet 1'in korunum yasası. Ek M-35'in ortam tepkisi $\dfrac{dP}{dr}=\dfrac{C\,Nq_n}{4\pi r^2}$ idi; kaynağı çevreleyen herhangi bir $S$ küresi üzerinden basınç gradyanı akısı:

$$\oint_S \nabla P\cdot d\vec A = \frac{C\,Nq_n}{4\pi r^2}\cdot 4\pi r^2 = C\,Nq_n = \text{sabit}$$

Akı **yarıçaptan bağımsızdır.** Diverjans teoremiyle, kaynağı içermeyen her küresel kabukta:

$$\int_V \nabla^2 P\,dV = \oint_{S_{dış}}\!\!\nabla P\cdot d\vec A \;-\; \oint_{S_{iç}}\!\!\nabla P\cdot d\vec A = 0 \;\Longrightarrow\; \nabla^2P=0$$

Fiziksel okuma nettir: **Evrenakı yaratılmaz, yok edilmez; yalnızca yer değiştirir.** Bu sonucu şimdilik kenara koyuyoruz — tensör aşağıda izsizliğe hiçbir yerde başvurulmadan bileşen bileşen kurulacak ve izin kendiliğinden sıfır çıktığı görülecek. (İki adım aynı $1/r^2$ yasasından beslendiği için bunlar iki bağımsız ispat değil, aynı korunum içeriğinin iki okunuşudur; kazanç, izsizliğin hiçbir adımda *varsayılmaması* ve soyut bir alan özelliği yerine adı konmuş bir korunum ilkesi olarak okunmasıdır.)

**(a) Eksenel bileşen.** Radyal ivmenin türevi:

$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\!\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3} \;\Longrightarrow\; \Delta a_{1,\parallel} = +\frac{2\mathcal{G}M}{r^3}\,\xi_\parallel$$

*İşaret pozitif:* gelgit ekseni boyunca her iki uçta da artık dışa bakar — Kuvvet 1'in haritası, eksen uçlarında Kuvvet 2'nin içe yönlü sıkıştırmasını **gevşetir.**

**(b) Yanal bileşen.** Merkezden $\xi_\perp$ kadar yana kaymış noktada ivme yine kaynağa doğrudur; büyüklüğü $\mathcal{G}M/r'^2$ ($r'=\sqrt{r^2+\xi_\perp^2}\simeq r$), doğrultusu merkez hattından $\xi_\perp/r$ kadar sapar:

$$a_\perp = -\frac{\mathcal{G}M}{r'^2}\cdot\frac{\xi_\perp}{r'} \simeq -\frac{\mathcal{G}M}{r^3}\,\xi_\perp \;\Longrightarrow\; T_\perp = -\frac{\mathcal{G}M}{r^3}$$

*İşaret negatif:* yanal doğrultularda artık merkez hattına doğrudur — Kuvvet 1, gelgit eksenine dik her yönde Kuvvet 2'nin sıkıştırmasını **pekiştirir.** Bu, $1/r^2$ alanının **yakınsama geometrisidir:** radyal çizgiler kaynağa doğru birbirine yaklaşır, gövdenin yanakları merkez hattına itilir.

**Sıkıştırma kuşağı çembersel.** Hesapta $\xi_\perp$'nin *hangi* yanal doğrultu olduğu hiçbir yere girmedi — yalnız büyüklüğü girdi. Eksene dik bütün doğrultular kaynağa aynı uzaklıkta ve aynı yakınsama açısıyla baktığı için pekiştirme, gövdenin bütün yanaklarında eşittir; matematikteki karşılığı $-1$ özdeğerinin **iki katlı dejenere** olmasıdır:

$$T_{\perp,1} = T_{\perp,2} = -\frac{\mathcal{G}M}{r^3}$$

Dejenerasyon, gelgit ekseni etrafındaki tam dönme simetrisinin ifadesidir: pekiştirme tek yönden gelen bir kıstırma değil, ekseni saran **eşit basınçlı bir kuşaktır** — 3.9.2'nin çembersel sıkıştırması, sayıya dökülmüş hâliyle. *(Kuşak gelgit eksenine diktir, ekvatora değil — 11.1.3'teki uyarı.)*

### Net sıkıştırma: gelgidin gerçek öznesi

Bir yüzey noktasındaki **net** içe sıkıştırma, Kuvvet 2'nin taban değeri ile Kuvvet 1'in artık katkısının toplamıdır ($\hat n$: dışa normal). 11.1.3'ün karesel formu buraya konduğunda kapalı biçim çıkar:

$$\boxed{\;a_{net}(\hat n) \;=\; a_2 \;-\; b\,\bigl(\hat n\cdot\mathsf{T}_1\cdot\hat n\bigr)\;}$$

| Bölge | Kuvvet 1'in harita değeri | Net sıkıştırma | Sonuç |
|---|---|---|---|
| Gelgit ekseni ($\hat n=\hat\xi_\parallel$) | $+2\mathcal{G}Mb/r^3$ (gevşetici) | $a_2-\dfrac{2\mathcal{G}Mb}{r^3}$ | **mengene gevşer** — su buraya dolar |
| Kuşak ($\hat n=\hat\xi_\perp$) | $-\mathcal{G}Mb/r^3$ (pekiştirici) | $a_2+\dfrac{\mathcal{G}Mb}{r^3}$ | **mengene pekişir** — su buradan kaçar |

Bu tablo, 3.9.2'de sözle kurulan mekanizmanın niceliğidir ve gelgidin gerçek öznesini gösterir: **suya dokunan tek kuvvet, her noktada içe bakan $a_{net}$ sıkıştırmasıdır.** $a_{net}$ bir skalerdir ve gövdenin her noktasında pozitiftir (içe doğrudur); $\hat n$'ye bağlı olan tek şey büyüklüğüdür. Yön hiçbir yerde dönmez — ne eksende, ne kuşakta, ne aradaki herhangi bir enlemde. Koşul, tabanın azami gevşemeyi karşılamasıdır:

$$a_2 \;>\; b\,\lambda_{maks}(\mathsf{T}_1) \;=\; \frac{2\mathcal{G}Mb}{r^{3}} \;=\; 1{,}10\times10^{-6}\ \mathrm{m/s^2}\quad(\text{Ay})$$

ve herhangi bir fiziksel taban için fazlasıyla sağlanır: Dünya'nın kendi yüzey itiminin ($9{,}8$ m/s²) yedi mertebe altındadır. Gelgit böylece tanımını bulur: **daima içe bakan tek bir sıkıştırmanın enlemsel modülasyonu.** Madde, $a_{net}$'in büyük olduğu kuşaktan küçük olduğu eksene akar.

Kuvvet 2'nin asıl işi budur ve vazgeçilmezdir. Onsuz, eksen uçlarında kalan artık **dışa bakan** bir vektör olurdu — mekanizma, teorinin reddettiği "uzaktan çekme" resmine geri düşerdi. Sıkıştırma denizi sayesinde deforme eden nicelik hiçbir yerde işaret değiştirmez: gelgit baştan sona bir **itme–sıkma** olayıdır. Standart kuramın böyle bir tabanı yoktur; onda gelgit, işareti çerçeveye göre dönen bağıl bir artıktan ibarettir (karşılaştırma: 11.1.8 ve 11.1.11).

**Genlik farktan okunur — ve fark parametresizdir.** Kuşak ile eksen arasındaki net sıkıştırma farkında $a_2$ düşer:

$$a_{net}(\text{kuşak}) - a_{net}(\text{eksen}) = \left(a_2+\frac{\mathcal{G}Mb}{r^3}\right) - \left(a_2-\frac{2\mathcal{G}Mb}{r^3}\right) = \frac{3\mathcal{G}Mb}{r^3}$$

— tam olarak $(+2)-(-1)=3$ özdeğer farkı. Mengenenin mutlak derinliği şekil farkına girmez; bu bir eksiklik değil, öngörünün gücüdür: **sıkıştırma denizinin derinliği ölçülmeden gelgit genliği hesaplanabilir.** Taban $r$'ye bağlı olsa da sonuç değişmez: uçların gerçek değerleri $a_2(r)\mp a_2'b$'dir, $a_2'$ terimi iki uçta zıt işaretlidir ($\ell=1$) ve şekli belirleyen $\ell=2$ payı tam olarak $3\mathcal{G}Mb/r^3$'te kalır — taban eğimi gövdeye net kuvvet uygular, o da yörüngeye yazılır (11.1.3).

Böylece tensör, Kuvvet 2'nin ne büyüklüğü ne radyal yasası ölçülmeden şu değere ulaşır:

$$\boxed{\;\left(T_\parallel,\;T_\perp,\;T_\perp\right) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1)\;,\qquad \textstyle\sum\lambda_i = 0\;}$$

| Özdeğer | Doğrultu | Fiziksel okuma |
|---|---|---|
| $-1$ (×2, **dejenere**) | Gelgit eksenine dik **her** yön | **Neden:** Kuvvet 2'nin sıkıştırması, ekseni saran eşit basınçlı kuşakta pekişir |
| $+2$ | Gelgit ekseni boyunca | **Sonuç:** sıkıştırma orada gevşer; kuşaktan kaçan su eksenin iki ucuna birden kabarır |

**Mekanizmanın üç adımı, tek tensörde.** **(1)** Dünya, Kuvvet 2'nin sıkıştırma denizinin içinde her yönden sıkılmış durur. **(2)** Ay'ın Kuvvet 1'i yakın yüzde güçlü, uzak yüzde zayıftır; merkeze göre farkı, sıkıştırmayı gelgit ekseninde gevşetir, eksene dik her yönde eşit büyüklükte pekiştirir. **(3)** Hacmini koruyan gövde, pekişen kuşaktan kaçarak gevşeyen tek yöne — gelgit eksenine — uzar; eksenin iki ucu da açık olduğundan kabarma çifttir.

**İzsizlik varsayım değil, korunum teoremidir.** Üç bileşen de izsizliğe başvurulmadan kuruldu ve iz kendiliğinden sıfır çıktı; $\mathrm{tr}\,\mathsf{T}_1=-\frac{1}{\rho_n}\nabla^2P$ olduğundan bu, bölüm başında akı korunumundan elde edilen $\nabla^2P=0$ ile aynı ifadedir. Standart fizikte "gelgit tensörünün izsizliği" Laplace denkleminin soyut bir özelliği olarak kaydedilir; burada adı konmuş bir muhasebedir: **yanaklardan sıkılan ($-1,-1$) hacim, eksende kabaran ($+2$) hacimle tam denkleşir — deplasman akısı yaratılmaz, yok edilmez.**

*(Sıkıştırma karşılıklıdır: Dünya da Ay'ı aynı geometriyle sıkar. Ay kilitli olduğu için oradaki kuşak gövde üzerinde dolaşmaz; kabarma akışkan yerine magma üzerinde kalıcılaşır — mascon olgusu, Bkz. 3.9.5. Bu bölümün konusu Dünya'daki okyanus tepkisidir.)*

---

## 11.1.5 Nedenselliğin İspatı: Basınç Okuması

$(+2,-1,-1)$ simetrik bir nesnedir; nedensellik ancak fiziksel alana — basınca — inilerek kurulur. Teorinin üstünlüğü tam burada görünür hâle gelir: teori basınç *diliyle* konuşur, çünkü nesnesi gerçekten bir basınçtır.

Çerçeve adımında taşınan kısım çıkarıldıktan sonra kalan artık potansiyel, açılımın ikinci mertebe terimidir:

$$\Psi_T(\vec\xi) = -\tfrac12\left(T_\parallel\xi_\parallel^2 + T_\perp\xi_\perp^2\right) = -\frac{\mathcal{G}M}{2r^3}\left(2\xi_\parallel^2-\xi_\perp^2\right)$$

$\xi_\parallel=\xi\cos\psi$, $\xi_\perp=\xi\sin\psi$ ile kapalı biçim:

$$\boxed{\;\Psi_T(\xi,\psi) = -\frac{\mathcal{G}M\,\xi^2}{2r^3}\left(3\cos^2\psi-1\right)\;}$$

$\Phi=(P-P_0)/\rho_n$ tanımı tersine çevrilirse **artık basınç alanı** — teorinin fiilen konuştuğu büyüklük — çıkar:

$$P_T(\xi,\psi) = \rho_n\Psi_T = -\frac{\rho_n\,\mathcal{G}M\,\xi^2}{2r^3}\left(3\cos^2\psi-1\right)$$

Gövde yüzeyinde ($\xi=b$) iki uç değer:

| Konum | $3\cos^2\psi-1$ | $P_T$ | Okuma (sıkıştırma tabanına göre) |
|---|---|---|---|
| Eksen ($\psi=0^\circ,\,180^\circ$) | $+2$ | $-\dfrac{\rho_n\mathcal{G}Mb^2}{r^3}$ | **mengene gevşek** (basınç açığı) |
| Yanaklar ($\psi=90^\circ$) | $-1$ | $+\dfrac{\rho_n\mathcal{G}Mb^2}{2r^3}$ | **mengene pekişik** (basınç fazlası) |

$P_T$ yalnız $\psi$'ye bağlıdır, azimuta değil: yanaklardaki basınç fazlası tek bir noktada değil, **gelgit eksenini saran tam bir kuşak boyunca** aynıdır — $-1$ özdeğerinin dejenerasyonunun basınç dilindeki karşılığı. *(Bu tablo Kuvvet 1'in artık payını gösterir; mutlak değil, Kuvvet 2'nin taban sıkıştırmasına **göre** okunur: eksen tabana göre gevşek, kuşak tabana göre pekişiktir. Taban düzeyi $\psi$'den bağımsız olduğu için tabloya girmez — 11.1.3.)*

**Nedensellik böylece türetilmiştir.** Ortak taşınma çıkarıldıktan sonra kalan şey gerçek bir basınç alanıdır: **kuşakta yüksek, gelgit ekseninde düşük.** Akışkan daima $-\nabla P$ yönünde, kuşaktan eksene akar; kuşağın hiçbir yerinde zayıf nokta olmadığı için kaçış yalnız gelgit ekseninden olur ve eksenin iki ucu da açıktır. **Sıkıştırma nedendir, kabarma sonuçtur** — ve açık ile fazlanın oranının tam $2{:}1$ olması, $(+2,-1,-1)$ yapısının basınç dilindeki birebir karşılığıdır.

Klasik türetimde bu tabloya karşılık gelen hiçbir şey yoktur: orada suya dokunan bir basınç alanı yazılmaz, yalnız ivme farkı vardır — deformasyonu yapan yerel etken adsız kalır (11.1.11).

**Ek M-26 ile çapraz denetim.** Kuşaktaki basıncın eksendekini aşma miktarı:

$$P_T(90^\circ)-P_T(0^\circ) = +\frac{3}{2}\cdot\frac{\rho_n\mathcal{G}Mb^2}{r^3} \;>\; 0$$

M-26'nın "suya batan top"u tamamen farklı bir yoldan — hidrostatik derinlik–basınç muhasebesinden — aynı işareti vermişti ($F_{yan}-F_{dikey}\propto\rho g r>0$). İki bağımsız argüman, aynı elipsoid.

---

## 11.1.6 Denge Gelgiti Genliği ve Güneş/Ay Oranı

Okyanus serbest yüzeyi, toplam basıncın dengelendiği yüzeydir. Potansiyel diliyle:

$$g\,\zeta(\psi) + \Psi_T(b,\psi) = \text{sabit},\qquad g=\frac{\mathcal{G}M_\oplus}{b^2}$$

> **Bu bir "eşpotansiyel" değil, eş-basınç yüzeyidir.** $\Phi\equiv(P-P_0)/\rho_n$ tanımı $\rho_n$ sabit olduğu için birebir tersine çevrilebilir; "toplam potansiyelin sabit olduğu yüzey" cümlesi, **"toplam basıncın sabit olduğu yüzey" (izobar) ile aynı cümledir.** Serbest yüzeyin fiziksel tanımı da budur: üstündeki basınç her yerde $P_{atm}$ olduğu için su, basınç dengesizliği kalmayana dek akar. Potansiyel dili yalnız cebiri kısaltır; teorinin konuştuğu büyüklük 11.1.5'in $P_T$'sidir. Buradaki $g$ de standart bir "yerçekimi ivmesi" değil, Dünya'nın kendi Kuvvet 1'inin yüzey değeridir.

**Sabit, hacim korunumundan sıfırlanır.** Su yaratılmadığına göre $\langle\zeta\rangle=0$; $\langle 3\cos^2\psi-1\rangle=0$ (Legendre $P_2$'nin küre ortalaması sıfır) olduğundan sabit tam sıfırdır. Buradan:

$$\zeta(\psi) = -\frac{\Psi_T}{g} = \frac{1}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^3 b\,\left(3\cos^2\psi-1\right)$$

> **$\mathcal{G}$ sadeleşti.** Sonuçta ne $\mathcal{G}$, ne $\alpha$, ne $Cq_n$ kaldı — yalnız kütle oranı ve geometri. Denge gelgiti **sıfır parametreli** bir öngörüdür; teorinin serbest kalemlerinin hiçbirine dokunmaz.

$A\equiv\dfrac{M}{M_\oplus}\left(\dfrac{b}{r}\right)^3 b$ kısaltmasıyla tepe ve çukur ayrışır:

$$\zeta(0^\circ)=+A\ \ (\text{kabarma tepesi}),\qquad \zeta(90^\circ)=-\tfrac12 A\ \ (\text{yanak çukuru})$$

$$\boxed{\;\Delta\zeta \equiv \zeta(0^\circ)-\zeta(90^\circ) = \frac{3}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^{3} b\;}$$

**$3/2$ katsayısı etiketi belirler:** $\Delta\zeta$ bir yükseklik değil, **tepe–çukur tam genliğidir.** Kabarma ortalama seviyenin $+A$ üstüne çıkarken yanaklar $-A/2$ altına iner — mengeneden kaçan su ile mengenenin bastırdığı su, tek muhasebenin iki yüzü.

### Sayılar

$b=6{,}371\times10^6$ m alınarak:

| Kaynak | $M/M_\oplus$ | $(b/r)^3$ | Tepe $+A$ | Çukur $-A/2$ | Genlik $\Delta\zeta$ |
|---|---|---|---|---|---|
| **Ay** | $1{,}229\times10^{-2}$ | $4{,}553\times10^{-6}$ | $+0{,}357$ m | $-0{,}178$ m | **0,535 m** |
| **Güneş** | $3{,}331\times10^{5}$ | $7{,}724\times10^{-14}$ | $+0{,}164$ m | $-0{,}082$ m | **0,246 m** |

**Güneş/Ay yarışı.** Güneş'in Dünya üzerindeki toplam itim kuvveti ($\propto M/r^2$) Ay'ınkinin **179 katıdır** — bu yüzden onun etrafında dolanırız. Fakat gelgiti yaratan toplam kuvvet değil, sıkıştırma haritasının keskinliğidir — kuvvetin gövde boyunca **değişimi** — ve gradyan uzaklığın küpüyle zayıflar:

$$\frac{\text{Güneş gelgiti}}{\text{Ay gelgiti}} = \frac{M_\odot}{M_{Ay}}\left(\frac{r_{Ay}}{r_\odot}\right)^{3} = \frac{2{,}709\times10^7}{(389{,}2)^3} \approx 0{,}460$$

Aynı $0{,}460$ genlik tablosundan da okunur ($0{,}246/0{,}535$): tensör oranı ile genlik oranı birbirini doğrular. Güneş toplam itimde 179 kat üstün, sıkıştırma haritasında Ay'ın yarısından azdır — $1/r^2$ ile $1/r^3$ arasındaki farkın bütün gücü buradadır (ayrıntı: 3.9.2.2). *(Bu oran iki kaynağın da saf Kuvvet 1 taşıdığı yaklaşımıyla hesaplanmıştır; Güneş'in dönüş kolu payının tensöre yaptığı yapısal ek 11.1.8'in konusudur ve orada gösterildiği üzere skaler genliğe etkisi ihmal mertebesindedir.)*

**Büyük ve küçük gelgit.** İki kaynağın genlikleri hizalanmaya göre toplanır veya çıkarılır:

| Durum | Geometri | Hesap | Genlik |
|---|---|---|---|
| Büyük gelgit (*spring*) | Ay ve Güneş hizalı | $0{,}535+0{,}246$ | **0,781 m** |
| Küçük gelgit (*neap*) | Ay ve Güneş dik | $0{,}535-0{,}246$ | **0,289 m** |
| Oran | — | $0{,}781/0{,}289$ | **2,70** |

Açık okyanusta ölçülen denge gelgiti genliği ~0,5 m mertebesindedir (Pugh & Woodworth, 2014); türetilen 0,535 m bu mertebeyi serbest parametresiz karşılar. Kıyılarda görülen metrelerce genlik, havza rezonansının yerel büyütmesidir — gök mekaniğine değil kıyı hidrodinamiğine aittir ve denge modelinin kapsamı dışındadır. Hassas doğrulama boyutsuz oranlardadır: Güneş/Ay $0{,}460$ ve büyük/küçük $2{,}70$ — ikisi de gözlemin standart değerleridir.

---

## 11.1.7 Eşdeğerlik İlkesi: Varsayım Değil, Sonuç

Tensörün biçimine bir kez daha bakalım: $T_{ij}=-\frac{1}{\rho_n}\partial_i\partial_jP$. Buradaki $\rho_n$ **nükleon öz yoğunluğudur** — su, kaya, demir, cıva fark etmez; hepsi aynı nükleonlardan kuruludur ve aynı $\rho_n$'yi taşır. Gelgit ivmesi, üzerine etki ettiği maddenin bileşiminden **zorunlu olarak** bağımsızdır.

Klasik mekanikte bu bağımsızlık bir postülattır: eylemsiz kütle ile kütleçekimsel kütlenin eşitliği varsayılır, deneyle sınanır, fakat açıklanmaz. Teoride **türetilmiştir** — tek bir evrensel $\rho_n$ olduğu için başka türlüsü yazılamaz. Çerçeve adımı da aynı köke bağlıdır: ortak ivmenin gövdeyi deforme etmemesi, klasik türetimde bir çerçeve seçiminin sonucudur; burada Kuvvet 1'in her nükleona aynı ivmeyi vermesinin sonucudur.

İfade tersine de okunur ve teoriyi ölçüme bağlar: $\rho_n$'nin evrenselliği bozulsaydı gelgit bileşime bağlı olurdu. MICROSCOPE uydusunun titanyum–platin çifti için bildirdiği $\eta_{EP}\lesssim10^{-15}$ sınırı (Touboul ve ark., 2022) ile Eöt-Wash burulma terazisi ölçümleri (Schlamminger ve ark., 2008), teoride $\rho_n$ evrenselliğinin sınavıdır: bu deneylerin null sonuçları, klasik mekaniğin açıklamadan taşıdığı bir postülatı değil, teorinin bir **türetiminin girdisini** doğrular.

---

## 11.1.8 Newton'la Sınır ve Ayırt Edici Sınav

Kayıt özdeşlikten başlar. Kilitli kaynak — Ay — için iki kuram aynı sayıları verir:

| Büyüklük | Bu türetim | Klasik gelgit kuramı |
|---|---|---|
| Uzaklık yasası | $1/r^3$ | $1/r^3$ |
| Tensör özdeğerleri | $(+2,-1,-1)$ | $(+2,-1,-1)$ |
| Güneş/Ay oranı | 0,460 | 0,460 |
| Denge gelgiti genliği | 0,535 / 0,246 m | aynı |
| Büyük/küçük oranı | 2,70 | aynı |

Bu özdeşlik teori için bir zorunluluktur, sürpriz değil: gözlemle uyuşan her kuram bu sayıları vermek zorundadır ve klasik kuram bu sayıları bir asırdır doğru vermektedir. Ayrışma, sayının **nasıl** üretildiğinde ve — birazdan görüleceği gibi — özdeşlik tablosunun **sessiz koşulunda** yatar. Yapısal farklar dörttür:

1. **Mekanizma adlandırılmıştır.** Teoride gelgiti yapan şey, gövdenin zaten içinde bulunduğu Evrenakı sıkıştırmasının (Kuvvet 2) yönlü bir gradyanla (Kuvvet 1) yeniden dağılmasıdır — kuşakta pekişme, eksende gevşeme. Klasik kuramda deformasyonu yapan yerel bir etken yoktur; tek aktör soyut potansiyelin kendisidir (11.1.11).
2. **Deforme eden nicelik işaret-belirlidir.** Klasik türetimde gelgidi yapan nicelik, gövde boyunca işareti dönen bağıl bir vektör alanıdır. Teoride deforme eden nicelik hiçbir yerde yön değiştirmeyen bir skalerdir: $a_{net}(\hat n)=a_2-b(\hat n\cdot\mathsf{T}_1\cdot\hat n)$ her noktada içe bakar, yalnız büyüklüğü enlemle modüle olur (11.1.4). Çift şişkinlik bir vektörün ters dönmesinden değil, sıkıştırmanın iki uçta eşit gevşemesinden çıkar. Klasik kuramın tabanı olmadığı için işaret-belirliliği de yoktur.
3. **İzsizlik teoremdir.** Klasik kuramda $\mathrm{tr}\,\mathsf{T}=0$, Laplace denkleminin soyut bir özelliği olarak kaydedilir; burada deplasman akısının korunumudur ve türetimin hiçbir adımında varsayılmadan çıkar (11.1.4).
4. **Eşdeğerlik ilkesi sonuçtur.** Klasik mekanikte postülat, burada $\rho_n$ evrenselliğinin türevi (11.1.7).

Bu dört fark yorum düzeyinde kalsaydı bölüm burada biterdi. Kalmaz — çünkü özdeşlik tablosunun sessiz bir koşulu vardır: **tablo yalnız *kilitli* kaynak için geçerlidir.**

### Sınavın kaynağı: kilitli kaynak ↔ dönen kaynak

Özdeşlikler 11.1.2'nin kuvvet envanterine dayanır: Ay kilitli olduğu için $\omega_1$ kolu kapalıdır ve gelgit saf pompa kolundan gelir. **Güneş kilitli değildir.** Dönüş kolu açıktır — ve bu kol bütün hâlinde açılır: F4 varsa F5 de vardır, ikisi de $\omega_1$'in ürünüdür.

> [!IMPORTANT]
> **"Dönüyor" hangi çerçeveye göre?** "Güneş dönüyor, Ay dönmüyor" cümlesi **mutlak** (yıldızlara göre) hızların kıyası olarak okunursa yanlıştır: Ay da kendi ekseni etrafında döner — üstelik Güneş'inkine çok yakın bir hızla. Cümle **Dünya'ya göre** okunmalıdır; o çerçevede ayrım mutlaktır:
>
> | Kaynak | Yıldızlara göre dönme | **Dünya'ya göre dönme** |
> |---|---|---|
> | **Ay** | 27,32 gün | **yok** — hız tam olarak sıfır |
> | **Güneş** | ~25,4 gün | ~27,3 gün (Carrington sinodik) |
>
> Gelgit kilidi zaten bunun tanımıdır: Ay'ın dönüşü yörünge dolaşımıyla aynı fazda olduğu için Dünya–Ay doğrultusuna göre hiç dönmez. Teorinin iddiası tam bu çerçevededir: **gelgit kilidi gövdenin makro-girdabını bastırır** (3.9.1; girdap rekabeti 3.4.4) — ortama göre bağımsız sirkülasyon kalmayınca $\omega_1$ kolunu besleyecek kaynak ortadan kalkar; serbest dönen gövdede kalır. Ayrım **ikilidir (kilitli/serbest)**, sürekli bir hız ölçeği değil.
>
> Ve bu, sınavı keskinleştirir: iki kaynağın mutlak dönme hızları neredeyse eşit olduğuna göre, tensör yapılarında bulunacak herhangi bir fark mutlak hıza yazılamaz — **yalnız kilitlilik durumuna** yazılabilir. Karışıklık değişkeni kendiliğinden elenmiştir.

**Kuvvet 3 tensöre girmez** — iki gerekçeyle. **(i)** M-37, Kuvvet 3 ile Kuvvet 4'ün aynı vorteksin teğetsel ve eksenel bileşenleri olduğunu ve tek bir $a_{madde}(R)$ tarafından yönetildiğini türetir; F3'ün radyal gradyan içeriği F4'ün $\beta$'sında zaten sayılıdır. **(ii)** F3'ün kendine ait etkisi $\eta_E$ üzerinden işleyen doğrusal bir artık kuplajdır (M-37, Adım B) ve zaman ölçeği $\tau_E$'dir — 11.1.9'da gösterildiği üzere gelgit periyoduna göre yirmi iki mertebe yavaştır; statik tensöre ölçülebilir katkı yapamaz.

Kalan iki kuvvette kritik olan **geometridir** — hiçbiri Kuvvet 1 gibi küresel-radyal değildir:

| Kuvvet | Geometri | Yön | Yasa |
|---|---|---|---|
| **F1** | küresel | $-\hat r$ (küresel yarıçap) | $1/r^2$ |
| **F4** | **silindirik** | $-\hat R$ (dönme eksenine dik) | $1/R$ (Ek M-38) |
| **F5** | **meridyenel** | $-\hat\theta$ (ekvatora doğru) | $\propto\sin2\theta$ (Ek M-39) |

Her ikisi de kaynağın **kendi dönme eksenine** göre tanımlıdır; gelgit tensörü alanın türevi olduğuna göre bu geometrileri miras alır.

### Karışımın tensörü

Dünya, Güneş'in ekvator düzlemine yakındır (heliografik enlem $\pm7{,}25^\circ$). Üç katkı üst üste konduğunda özvektörler: **(1)** gelgit ekseni (Güneş–Dünya doğrultusu), **(2)** yörünge doğrultusu (ekliptik içinde, gelgit eksenine dik), **(3)** ekliptiğe dik (Güneş'in dönme ekseni doğrultusu). Özdeğerler:

$$\boxed{\;(T_1,T_2,T_3)=\frac{\mathcal{G}M}{r^{3}}\Bigl(2+\beta,\;\;-(1+\beta),\;\;-(1+\gamma)\Bigr),\qquad \mathrm{tr}\,\mathsf{T}=-\gamma\,\frac{\mathcal{G}M}{r^{3}}\;}$$

$$\beta \equiv \frac{Br}{\mathcal{G}M}\ \ (\text{F4 payı}),\qquad \gamma \equiv \frac{2a_5^{(0)} r^{2}}{\mathcal{G}M}\ \ (\text{F5 payı})$$

*(Ön çarpan $\mathcal{G}M/r^3$'tür — 11.1.6'nın $A$ kısaltmasıyla karıştırılmamalıdır; o bir uzunluk, bu bir ivme gradyanıdır. $B$ ve $a_5^{(0)}$, F4 ve F5'in genlik katsayılarıdır: $\vec a_4=-\dfrac{B}{R}\hat R$, $\vec a_5=-a_5^{(0)}\sin2\theta\,\hat\theta$.)*

İki katkı **iki ayrı imza** üretir ve birbirine karışmaz:

**(a) F4 → dejenerasyon kırılır, iz korunur.** Silindirik $1/R$ alanı tek başına $(+1,-1,0)$ verir; izi sıfırdır (iki boyutlu akı korunumu), fakat özdeğerleri dejenere değildir. F1 ile toplandığında yanal çiftin eşitliği bozulur: ekliptik içindeki yanal özdeğer $-(1+\beta)$ olurken ekliptiğe dik olan $-1$'de kalır. **Sıkıştırma kuşağı artık çember değil, elipstir.**

**(b) F5 → iz ihlal edilir.** Meridyenel $\sin2\theta$ alanının ıraksaması ekvator düzleminde sıfır değildir: $\nabla\!\cdot\!\vec a_5\big|_{\theta=0} = -2a_5^{(0)}/r$. *(Kuvvetin kendisi ekvatorda sıfırdır — $\sin2\theta|_{\theta=0}=0$ — ama tensöre giren şey kuvvet değil türevidir ve $d(\sin2\theta)/d\theta$ tam orada maksimumdur.)* Bu sonuç F5'in radyal yasasından **bağımsızdır.**

### Newton bunu üretemez

Klasik kuramda bir kaynağın **dönüp dönmediği dış alanına hiç girmez.** İki imzanın Newton'daki karşılığı:

| İmza | Newton | Teori |
|---|---|---|
| **Yanal dejenerasyonun kırılması** | Yalnız gövdenin basıklığından ($J_2$). Güneş için $J_2(R_\odot/r)^2 = 2{,}2\times10^{-7}\times(4{,}65\times10^{-3})^2 \approx 5\times10^{-12}$ | $\beta$ — apsidal presesyon üst sınırı $\lesssim10^{-9}$ |
| **Boşlukta iz** | $\nabla^2\Phi=0$ gereği **tam olarak sıfır** — her kaynak, her uzaklık, her çokkutuplu mertebe | $-\gamma\,\mathcal{G}M/r^3 \ne 0$ |

Birinci satırda Newton'un arka planı vardır ama **200 kat aşağıdadır** — gerçek bir keşif penceresi kalır. İkinci satırda arka plan **tam sıfırdır**: boşlukta ölçülen sıfırdan farklı bir gelgit izi, Newton'un kendi vakum denklemini ihlal eder. İkinci kanal bu yüzden temizdir.

**Sınavın ölçek referansı.** Güneş için gelgit tensörünün ölçeği:

$$\frac{\mathcal{G}M_\odot}{r^{3}} = \frac{1{,}327\times10^{20}}{(1{,}496\times10^{11})^{3}} = 3{,}96\times10^{-14}\ \text{s}^{-2} \;\approx\; 40\ \mu\text{E}$$

(1 E = 1 Eötvös = $10^{-9}$ s⁻².) Aranan iz $\gamma$ ile bunun çarpımıdır: $\gamma\sim1$ için ~40 μE, $\gamma\sim10^{-3}$ için ~40 nE. Gradyometri sınıfı aletlerin tek bileşen gürültüsü mE/$\sqrt{\text{Hz}}$ mertebesindedir — sinyal anlık duyarlılığın altındadır ve frekansı bilinen bir zorlamada uzun integrasyonla aranır; asıl iş, iz artığının okyanus yükleme, atmosferik basınç ve $J_2$ arka planından ayrıştırılmasıdır. Mevcut gradyometri verisinden $\gamma$ üzerine fiilen hangi sınırın çıktığı 7.4'ün hesap kalemidir.

### Doğal diferansiyel deney

| Kaynak | Açık kollar | Gelgit tensörü |
|---|---|---|
| **Ay** — kilitli (Dünya'ya göre dönmüyor) | yalnız pompa kolu (F1 + F2) | $(+2,\,-1,\,-1)$ · iz $=0$ · **dejenerasyon kusursuz** |
| **Güneş** — serbest (Dünya'ya göre ~27,3 günde bir tur) | pompa kolu (F1 + F2) + F4 + F5 | $(2{+}\beta,\,-(1{+}\beta),\,-(1{+}\gamma))$ · **iz $\ne0$** · **dejenerasyon kırık** |

**Dünya bu iki kaynağı aynı anda, aynı aletlerle ölçmektedir.** Kilitli olan kontrol, dönen olan numunedir — kurulması gereken bir düzenek değil, hâlihazırda işleyen bir deney. Aranan gözlemsel büyüklük, gelgit tensörünün **üç özdeğerinin ayrı ayrı** çıkarılmasıdır (gradyometri); Ay ve Güneş bileşenleri frekansta zaten ayrıktır. İki imzanın **yönü de bellidir**: özvektörler Güneş'in dönme eksenine kilitlidir — Newton'un noktasal kaynak alanında böyle bir ayrıcalıklı yön yoktur.

**Sınavın statüsü.** Yapı türetilmiştir ve parametresizdir: $(2{+}\beta,-(1{+}\beta),-(1{+}\gamma))$ ve $\mathrm{tr}=-\gamma\,\mathcal{G}M/r^3$, alanların geometrisinden çıkar; iz bağıntısı F5'in radyal yasasından bağımsızdır. Genlikler öngörülmemiştir: $\beta$ apsidal presesyondan $\lesssim10^{-9}$ ile sınırlıdır (F4 payı Ek M-38'de galaktik kolektif vortekse atanır; Güneş'in yerel dolaşımı zayıftır), $\gamma$'nın kalemi $\kappa_5$'tir ve serbesttir (Ek M-39). Sınav bu yüzden iki yönlü keskindir: **sıfırdan farklı bir boşluk izi bulunursa Newton'un vakum denklemi ihlal edilmiş olur — kesin ayrım; bulunmazsa $\kappa_5$ üzerindeki sınır her ölçüm turunda daralır.** Ölçüm duyarlılığının nicel değerlendirmesi ve $\beta,\gamma$'nın 11.1.6 genliğine kesin sayısal etkisi 7.4'ün hesap kalemleridir; ikisi de bölümün mertebe iddialarını değiştirmez.

> **Ölçek kaydı — neden Güneş'te zayıf, galakside belirleyici.** F4 ve F5 dönüş kolundan beslenir ve kolun gücü ortamın dönme hızıyla ölçeklenir. Güneş'in yerel dolaşımı galaktik kolektif vorteksin yanında sönüktür; yerel pay ölçülebilir mertebeye ancak yaklaşır. Galaktik ölçekte ise aynı iki kuvvet **baskın** hâle gelir ve düz dönüş eğrilerini üreten şey olur (Bkz. Kısım 10). Kepler yasası bu yüzden evrensel değil, **belirli bir kol dengesinin** yerel sonucudur: Güneş Sistemi'nde çalışır, galakside çalışmaz. Bunun gelgit hesabına yansıması da nettir: $\beta,\gamma\approx0$ sadeleştirmesi yalnız Güneş Sistemi ölçeğine özgüdür. Kaynak hızlı dönen bir galaksi ya da $\omega_1$ kolu güçlü herhangi bir gövde olduğunda sadeleştirme düşer; F4 ve F5 tensöre baskın katkılar olarak girer ve yapıyı (kırık dejenerasyon, sıfırdan farklı iz) köklü biçimde değiştirir — böyle sistemlerin gelgit hesabı, buradaki tam birleşik tensörle yürütülmelidir. *(Kıyas Güneş ile galaksi arasındadır, Güneş ile Ay arasında değil: Güneş–Ay ayrımı kilitliliktir, hız değil.)*

---

## 11.1.9 Şişkinlik Kayması: Kaymayı Yapan Sürtünme Atomiktir

Buraya kadar kurulan denge gelgiti **statik** tepkidir: kabarma, gelgit ekseniyle tam hizalıdır. Gözlem, şişkinlik ekseninin Ay'ın yaklaşık $3^\circ$ **önünde** seyrettiğini söyler (Bkz. 3.9.2) — Dünya'nın hızlı dönüşü kabarmayı öne taşır. Bu adım, hangi sürtünmenin iş gördüğünü sormayı gerektirir ve teori burada iki kanalı titizlikle ayırır.

### İki kanal, iki zaman penceresi

Evrenakı sürtünmesi sıfır değildir — Postülat 7, $\eta_E$'yi "sıfıra çok yakın, kesinlikle sıfır değil" diye sabitler ve teori bu sıfır-olmayışı milyar yıl ölçeğindeki olgularda fiilen kullanır: retrograd uyduların sönümü, halka bending-wave yitimi, yörünge kilitlenmesi (Bkz. 11.3.2). Mesele ortamın sürükleyip sürüklemediği değil, **ne kadar sürede** sürüklediğidir. İki gevşeme zamanı yan yana:

| Kanal | Gevşeme zamanı | Nereden |
|---|---|---|
| **Maddesel (atomik) sürtünme** | $\tau_{madde}\simeq QP/2\pi \approx 8{,}5\times10^{4}$ s ($\approx24$ saat) | $Q\approx12$, gelgit dönemi 12,42 sa |
| **Evrenakı kuplajı** | $\tau_{E}=\dfrac{2\rho_c b^{2}}{9\eta_E} \gtrsim 2{,}2\times10^{27}$ s ($\gtrsim7\times10^{19}$ yıl) | 11.3.2'nin Stokes yazımı, geçerli en sıkı sınırla ($\eta_E\lesssim2{,}3\times10^{-11}$ Pa·s; 11.4.8) |

$$\frac{\tau_E}{\tau_{madde}} \gtrsim 2{,}5\times10^{22}$$

Evrenakı'nın gevşeme zamanı evren yaşının ~5 milyar katıdır; gelgit ise 12,4 saatte bir tersine dönen **günlük** bir zorlamadır. Yirmi iki mertebe yavaş bir kanal, günlük bir zorlamaya derece mertebesinde faz kazandıramaz — sonuç sınır seçimine duyarlı bile değildir (süpersedilmiş gevşek Phoebe sınırıyla dahi arada on altı mertebe kalır). Üstelik $\tau_E$ en cömert tahmindir: Ek M-43, Dünya–Ay rejiminde bağıl hızların kritik hızın ($v_{kav}$) çok altında kaldığını ve altkritik bastırmanın kuplajı daha da düşürdüğünü gösterir. Muhasebenin öbür ucu aynı hükmü verir: Dünya'nın ölçülen toplam gelgit enerji yitimi ~3,7 TW'tır ve ezici çoğunluğu sığ denizlerdeki taban sürtünmesi ile türbülanstır — su moleküllerinin kayaya sürtünmesi.

**Sonuç:** kayma açısı **maddenin** defterindedir; ortam kanalının payı, aşağıda nicelendiği üzere $10^{-22}$ derece mertebesindedir. İki kanal rakip değildir — **farklı zaman pencerelerinde** çalışırlar ve hangisinin baskın olduğunu olgunun periyodu belirler: günlük gelgitte madde, milyar yıllık göçlerde Evrenakı.

### Doğru muhasebe: kaymayı madde yapar, torku Evrenakı taşır

| Soru | Cevap | Nereye ait |
|---|---|---|
| Şişkinliği ne öne taşır? | Okyanus–taban sürtünmesi, türbülans, havza yitimi | **madde** (atomik) |
| Öne taşınmış şişkinlik Ay'a ne yapar? | Yer değiştirmiş kütle fazlası kendi **gradyan lobunu** taşır; lob Ay'a teğetsel itki verir | **Evrenakı** (Kuvvet 1) |

Bu, 3.9.4'ün lob-işaret kuralıdır: teorinin katkısı kaymayı üretmek değil, kaymanın ürettiği torku **taşıyan aracıyı adlandırmaktır** — Ay'a dokunmadan itki veren şey, yer değiştirmiş kütlenin Evrenakı'daki basınç çukurudur.

### Nicel: kayma açısı serbest değildir

$\varepsilon$ bir tahmin değildir; **Ay'ın ölçülen uzaklaşma hızından geri çözülür.** Öne kaymış şişkinliğin torku Ay'ın yörünge açısal momentumunu besler:

$$\Gamma = \frac{3}{2}\,k_2 \sin(2\varepsilon)\,\frac{\mathcal{G}M_{Ay}^{2}R_\oplus^{5}}{r^{6}} \;=\; \frac{dL}{dt},\qquad L = M_{Ay}\sqrt{\mathcal{G}M_\oplus r}\;\Longrightarrow\;\frac{dL}{dt}=\frac{L}{2r}\frac{dr}{dt}$$

Ölçülen $dr/dt = 3{,}8$ cm/yıl (Ay Lazer Menzillemesi; Dickey ve ark., 1994) konduğunda:

| Büyüklük | Değer |
|---|---|
| $L$ (Ay yörünge açısal momentumu) | $2{,}88\times10^{34}$ kg·m²/s |
| $dL/dt$ | $4{,}50\times10^{16}$ N·m |
| $\mathcal{G}M_{Ay}^2R_\oplus^5/r^6$ | $1{,}17\times10^{18}$ N·m |
| **$k_2\sin(2\varepsilon)$** | **$0{,}0256$** |

Kalan tek girdi Dünya'nın Love sayısı $k_2$'dir — bir malzeme özelliği:

| $k_2$ | Kayma açısı $\varepsilon$ | Karşılık gelen $Q$ |
|---|---|---|
| $0{,}35$ | $2{,}10^\circ$ | 13,7 |
| $0{,}30$ | $2{,}45^\circ$ | 11,7 |
| $0{,}25$ | $2{,}94^\circ$ | 9,8 |
| $0{,}20$ | $3{,}68^\circ$ | 7,8 |

$$\boxed{\;\varepsilon \approx 2^\circ\!-\!3{,}5^\circ\;}$$

Gözlemle bildirilen ~$3^\circ$ bu bandın içindedir ✓. Çıkan kalite çarpanı $Q\approx8\!-\!14$, Dünya için bağımsız bilinen düşük gelgit $Q$'suyla (~12) örtüşür ✓. İki bağımsız gözlem — uzaklaşma hızı ve $Q$ — aynı açıyı verir. *(Bu kalem kaynağı atomik olduğu için standart kuramla ortaktır ve ayırt edici sınav taşımaz; bölümün ayırt edici sınavı 11.1.8'dedir.)*

### Sıfırlanmayan taban: teorinin bu kanaldaki tek ayrı sözü

Malzeme sürtünmesi tümüyle sıfır olan bir gövdede standart kuram kayma açısının **tam sıfır** olmasını gerektirir. Teoride $\eta_E\ne0$ olduğu için sıfırlanmayan bir **artık kayma tabanı** kalır; iki kanalın faz katkıları gevşeme zamanlarıyla ters orantılıdır:

$$\varepsilon_E \;\approx\; \varepsilon_{madde}\cdot\frac{\tau_{madde}}{\tau_E} \;\approx\; 3^\circ \times 4{,}0\times10^{-23} \;\approx\; \boxed{\;1\times10^{-22}\ \text{derece}\;}$$

Sayı, ayrımın hem gerçek hem bugün ölçülemez olduğunu birlikte söyler: sıfır değildir, fakat Dünya'da maddesel terimin yirmi iki mertebe altındadır. Kalemin sınanabilir hâle geldiği rejim, maddesel yitimin ihmal edilebilir olduğu ve gözlem penceresinin milyar yıla uzadığı sistemlerdir — tam olarak teorinin $\eta_E$'yi zaten kullandığı yer (retrograd uydu göçü, kilitlenme zamanları, halka sönümü; Bkz. 11.3.2 ve Ek M-43).

---

## 11.1.10 Geçerlilik Sınırı ve Açık Kalemler

**Geçerlilik sınırı.**

- $b\ll r$ birinci mertebe açılımıdır; $O(\xi^2)$ terimleri ihmal edilmiştir. Ay için $b/r\approx0{,}017$, hata mertebesi ~%2. Kuvvet 2'nin taban eğiminden gelen $\ell=2$ artığı (11.1.3) bu bandın içindedir (%0,6–%1,7).
- İz sıfırlığı yalnız **kaynaksız** bölgede geçerlidir. Gövde içinde ($r<b$) akı, kapsanan nükleon sayısıyla büyür: $\nabla^2P=Cq_n\rho_{madde}/m_n$, ve Ek M-35'in $\mathcal{G}=\frac{Cq_n}{4\pi\rho_n m_n}$ ayrıştırmasıyla tensör iz kazanır:

$$\mathrm{tr}\,\mathsf{T}\big|_{i\varsigma} = -4\pi\mathcal{G}\,\rho_{madde}$$

  Teori, gövde içinde Poisson denkleminin tam karşılığını yeni parametre girmeden, doğru katsayıyla üretir — dışarıda sıfır, içeride $-4\pi\mathcal{G}\rho$. Bir **tutarlılık kapanışıdır.**
- Denge gelgiti *statik* tepkidir; gerçek gelgit gecikmeli ve dinamiktir (kayma: 11.1.9; havza tepkisi kapsam dışı: 11.1.6).
- Kuvvet envanteri argümanı (11.1.2) **kilitli kaynak** içindir; serbest dönen kaynakta F4/F5 katkıları 11.1.8'in birleşik tensörüyle tartılır.
- **Ölçülen gövdenin kendi dönüşü hesaba katılmamıştır — bilinçli bir iş bölümü.** 11.1.6'nın $g=\mathcal{G}M_\oplus/b^2$'si küresel, dönmeyen Dünya varsayar; oysa Dünya serbest döner, kendi F4/F5'ini taşır ve küre değildir. İki etki farklı mertebelerde ve farklı geometrilerde girer: gövdenin kendi F4/F5'i **eksenel-simetrik ve zamanla sabit** bir figür deformasyonu üretir (basıklık, $J_2$ imzası), gelgit ise gelgit eksenine kilitli, **günlük dolaşan** bir artıktır; birinci mertebede ayrışırlar. Figür hesabı 11.2'nin konusudur; oradaki $\sin2\theta$ yasasının bu bölümün $g$'sine etkisi $g$'deki enlemsel değişimle ölçeklenir (~%0,5) ve mertebe iddialarını değiştirmez.

**Kapanmış kalem — uzaklaşmanın bileşenleri.** 11.1.9'un kayma hesabı, Ay'ın 3,8 cm/yıl'lık uzaklaşmasının tamamını lob torkuna yükler; bu bağımsız olarak doğrulanmıştır (3.9.4): Dünya'nın kaybettiği açısal momentum ($-4{,}93\times10^{16}$ kg·m²/s², gün uzaması 2,3 ms/yüzyıldan) ile Ay'ın kazandığı ($+4{,}50\times10^{16}$, LLR'den) **%91 doğrulukla** dengelenir — bütçe gelgit aktarımıyla tek başına kapanır. Kozmolojik seyrelme, üzerine binen çok daha yavaş bir taban terimidir ($\lesssim$%10); kayda değer pay taşısaydı geri çözülen kayma açısı $0{,}7^\circ$'ye düşerdi — gözlenenin dörtte biri. Ayrıştırılamayan ~%9'luk artığın sınanması 7.4'ün kalemidir.

**Açık kalemler (7.4'e yazılı):** $\gamma$ üzerine gradyometriden fiilî sınır; $\beta,\gamma$'nın 11.1.6 genliğine kesin sayısal etkisi; uzaklaşma bütçesindeki ~%9 artığın ayrıştırılması.

---

## 11.1.11 Klasik Anlatının Vektör Muhasebesi: Sahipsiz Neden

Klasik diferansiyel gelgit türevi kinematik olarak tamdır — bu bölümün bütün sayılarını üretir ve buna itiraz yoktur. İtiraz, o matematiğin üzerine giydirilen **anlatıyadır** ve iki katmanlıdır: **(i)** yaygın anlatı, bağıl bir büyüklüğü arka yüze etki eden gerçek bir kuvvet gibi sunar — bu okuma Newton mekaniğinin *kendi içinde* yanlıştır ve aşağıda eylemsiz sistemin vektör envanteriyle çürütülür; **(ii)** doğru okunmuş klasik anlatı bile deformasyonu yapan yerel bir etkeni **adlandıramaz** — kabarma, bütünün düşüşünün muhasebesi olarak kalır, yerinde bir neden gösterilmez. Teoride ikisi de yoktur: suyu kaldıran etken baştan bellidir ve gerçektir — Evrenakı sıkıştırmasının kuşakta pekişip eksende gevşemesi.

<iframe src="animasyonlar/gelgit_vektor.html" width="100%" height="600" style="border:none;border-radius:12px;display:block;margin:24px auto;" title="Şekil 11.1.11-A — Eylemsiz Sistemde Kuvvet Envanteri ve Basınç Modelinin Okuması" loading="lazy"></iframe>

### 11.1.11.1 Eylemsiz Sistemde Gerçek Kuvvet Vektörleri

Dünya'nın kütle merkezini eylemsiz orijin $\mathbf{0}$ alalım; Ay $+\hat{x}$ yönünde $r$ uzaklığında olsun. Arka yüzeydeki (Ay'a zıt) bir sıvı parçacığı $\mathbf{x}_P = -b\,\hat{x}$'tedir. Newton kütleçekimi yalnızca çekicidir; vektörü daima kaynağa bakar. Eylemsiz sistemde $P$ üzerindeki gerçek ivmeler:

$$\vec{a}_{D} = +\frac{\mathcal{G}M_\oplus}{b^2}\,\hat{x} \quad \text{(Dünya'nın alanı, merkeze doğru)}\qquad \vec{a}_{A} = +\frac{\mathcal{G}M_{Ay}}{(r+b)^2}\,\hat{x} \quad \text{(Ay'ın alanı, Ay'a doğru)}$$

$$\boxed{\vec{a}_{top}^{(P)} = \left[\frac{\mathcal{G}M_\oplus}{b^2} + \frac{\mathcal{G}M_{Ay}}{(r+b)^2}\right]\hat{x}}$$

**Her iki katkı da $+\hat{x}$ yönlüdür.** Eylemsiz sistemde arka yüzde $-\hat{x}$ yönünde (uzaya doğru) etki eden gerçek kuvvet **yoktur** — ne büyük ne küçük, tam olarak sıfır. Bu, yeni bir sonuç değil, klasik kuvvet listesinin olduğu gibi okunmasıdır; aşağıdaki bütün argüman bu tek satıra dayanır. *(Simge kaydı: buradaki $\vec a_{top}$, 11.1.4'ün $a_{net}$'i ile karıştırılmamalıdır — o, sıkıştırmanın enlemsel modülasyonunu veren bir skalerdir.)*

### 11.1.11.2 Bağıl İvmenin Kuvvete Terfisi: Anlatı Hatası

Klasik türev, $P$'nin merkeze göre ivmesi için merkez ivmesini referans alır:

$$\vec{a}_{bağıl}^{(P)} \equiv \vec{a}_{A}^{(P)} - \vec{a}_{A}^{(M)} = \frac{\mathcal{G}M_{Ay}}{(r+b)^2}\,\hat{x} - \frac{\mathcal{G}M_{Ay}}{r^2}\,\hat{x} \;\approx\; -\frac{2\mathcal{G}M_{Ay}b}{r^3}\,\hat{x}$$

Sayı doğrudur — 11.1.4'ün $T_\parallel$'i bunun ta kendisidir. Fakat negatif bağıl ivme, **her ikisi de pozitif olan iki sayının farkıdır**: merkez $\mathcal{G}M_{Ay}/r^2$ ile Ay'a düşerken $P$ daha küçük ivmeyle düşer. Eksi işaret, $P$'nin *daha yavaş yaklaştığını* söyler — uzaklaştığını değil. Yaygın anlatı bu farkı çoğu kez "Ay arka yüzdeki suyu uzaya doğru bırakır / iter" biçiminde, arka yüze etki eden bir etken gibi sunar.

> **İtiraz tek cümleliktir ve kalıcıdır: bağıl bir büyüklük, gerçek bir kuvvete terfi ettirilemez.** 11.1.11.1'in envanteri gereği arka yüzde $-\hat{x}$ yönlü gerçek kuvvet sıfırdır; o yönde bir *etken* de yoktur. Bu, Evrenakı'nın Newton'a itirazı bile değildir — **Newton'un kendi vektör envanterinin** o anlatıya itirazıdır.

Bedeli pedagojik değil yapısaldır: yükselen kolonu "dışa itilen su" olarak okuyan biri, kabarmayı yerel bir kuvvet dengesi sanır ve kuşaktaki alçalmayı hesaptan düşürür — oysa iki bölge tek muhasebenin iki yüzüdür (11.1.6'nın $+A$ / $-A/2$ ayrışması).

### 11.1.11.3 İtirazın Sınırı

İtirazın gücü, gereğinden fazlasını iddia etmemesinde yatar; iki kalem klasik kurama yazılamaz ve yazılmaz. **(i) İş–enerji muhasebesi açık vermez:** denge şekli tek kolonun yükselmesi değil, eksende $+A$ yükselen suyun kuşakta $-A/2$ alçalan suyla yer değiştirmesidir; yer değiştirmeyi yürüten kuvvetler yataydır ve denge yüzeyi, hacim kısıtı altında toplam potansiyelin asgarisidir — sistem oraya kendiliğinden gider. Aynı muhasebe 11.1.5'in kendi akışıdır (yüksek basınçtan alçağa, kendiliğinden); klasik kurama enerji açığı yazan bir itiraz aynı hükmü teoriye de yazardı. **(ii) Diferansiyel yöntem genellemede kırılmaz:** bir arada tutulmayan cisimler dizisi kaynağa düşerken gerçekten gerilir — gelgit gerilmesi, Roche sınırı, Shoemaker–Levy 9'un 1992'de Jüpiter önünde parçalanması bunun gözlemidir; bağıl uzaklaşma merkeze göredir ve gerçektir.

Kalan çekirdek tek ve sağlamdır: **bağıl ivme gerçek bir kuvvet değildir, dolayısıyla yerel bir neden de değildir.**

### 11.1.11.4 İki Adım Karşısında Tek Adım

Standart karşı çıkış, hesabın serbest düşen çerçevede yapıldığı ve orada sözde kuvvetlerle çalışmanın meşru olduğudur. Çerçeve seçimi elbette meşrudur; sorun, çerçevenin beyan edilmemesi ve sözde kuvvetin anlatıya gerçek kuvvet diye sokulmasıdır. Çerçeve doğru beyan edildiğinde bile klasik kurulum kabarmayı **iki adımda** kurar:

1. Merkezin ivmesi çıkarılarak bir **fark** niceliği elde edilir — gerçektir ama kuvvet değildir; işareti seçilen çerçeveye bağlıdır.
2. Okyanus bu farkı, suyu fiilen kaldıran şeye — **basınca** — çevirir.

Klasik modelin dürüst hâli de bunu söylemek zorundadır: suyu kaldıran "uzaya çeken eksi vektör" değil, okyanustaki basınç gradyanıdır. Zayıflık, işin yapılmaması değildir — iş yapılır; zayıflık, **birinci adımın anlatıya kuvvet diye sokulması ve ikinci adımın adının hiç anılmamasıdır.** Sizi itmeyen bir el sizi kaldırmaz; kaldıran, o elin altındaki basınçtır — klasik model bunu yapar ama adını saklar.

Teori **tek adımdır:** su, kuşakta pekişen sıkıştırmadan kaçarak mengenenin gevşediği eksen uçlarına pompalanır. Kaldıran etken baştan itibaren basınçtır; ara nicelik, çerçeve seçimi, işaret dönüşümü gerekmez. Deforme eden nicelik, gövdenin zaten içinde bulunduğu ve hiçbir yerde yön değiştirmeyen Evrenakı sıkıştırmasıdır ($a_{net}$): her noktada içe bakar, yalnız büyüklüğü enlemle modüle olur (11.1.4; 11.1.8, md. 2).

### 11.1.11.5 Katı Dünya Gelgiti

Gelgit yalnız okyanusta değildir; katı Dünya da aynı $\ell=2$ yükü altında deforme olur. Genlik, denge gelgitinin radyal Love sayısıyla ölçeklenmiş hâlidir ($h_2\approx0{,}61$):

$$\Delta_{katı} \simeq h_2\,\Delta\zeta = 0{,}61\times0{,}535\ \text{m} \approx 0{,}33\ \text{m}$$

Bu deformasyon GNSS, VLBI ve süperiletken gravimetreyle rutin ölçülür (IERS Conventions, 2010) ve **çift şişkinlik yapısıyla, $2{:}1$ tepe/çukur oranıyla birlikte** doğrulanır: $(+2,-1,-1)$ yapısı yalnız akışkanda değil katı gövdede de geçerlidir — mekanizma iddiası akışkana özel bir kolaylığa dayanmaz.

**Ayrım kaydı — katı gelgit ile kalıcı jeoit karıştırılmamalıdır.** Dünya'nın uzun dönemli ortalama figüründe (jeoit) Ay yönlü bir ikili şişkinlik *aranmaz*: gelgit ekseni yüzeye göre günlük dolaştığı için yapı zaman ortalamasında silinir; kalan sıfır-frekanslı kalıcı pay $J_2$'nin içine yazılır. Ölçülen katı gelgit, ortalama figürün üzerindeki **günlük salınımdır** — ortalama figür 11.2'nin konusudur.

### 11.1.11.6 Bölüm Özeti

| Soru | Klasik anlatı | Bu bölümün hükmü |
|---|---|---|
| Bağıl ivmenin türevi doğru mu? | $-2\mathcal{G}M b/r^3$ | **Doğru** — 11.1.4'ün $T_\parallel$'i ile birebir aynı |
| Arka yüzde dışa yönlü gerçek kuvvet var mı? | (anlatıda ima edilir) | **Yok, tam sıfır** — Newton'un kendi envanteri |
| Deformasyonu yapan yerel etken kim? | adlandırılmaz (bağıl artık) | **Evrenakı sıkıştırması:** kuşakta pekişir, eksende gevşer; her noktada içe bakar |
| Kaç adım? | fark niceliği → (adı anılmayan) basınç | **tek adım:** sıkıştırma → kaçış |
| Gözlem ne diyor? | gelgit ve katı gelgit ölçülür | iki kuram aynı sayıyı verir; ayırt edici sınav **11.1.8'dedir** |

Klasik diferansiyel türev matematiksel olarak tamdır; eksiği sayısında değil, fiziğindedir — ürettiği negatif bağıl ivmenin eylemsiz sistemde gerçek bir kuvvet karşılığı yoktur ve deformasyonun yerinde bir nedeni gösterilmez. Teoride neden yerindedir, gerçektir ve adı konmuştur: **gelgit, Evrenakı sıkıştırmasının işidir.**

---

Bir sonraki bölüm aynı basınç matematiğini dönen gövdenin kendi figürüne uygular: 11.2, Yanal İtimin $\sin2\theta$ yasasını türetir ve gezegen basıklığının klasik hidrostatik dengeden nerede ayrıldığını gösterir.
