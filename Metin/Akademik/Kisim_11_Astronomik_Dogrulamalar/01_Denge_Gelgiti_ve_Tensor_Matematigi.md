# 11.1 Diferansiyel Sıkıştırma: Gelgit Tensörü ve Denge Gelgiti

Kısım 3.9'da okyanusların hareketini, uzaydan gelen görünmez bir "çekme" kuvvetiyle değil, Evrenakı akıntısının yarattığı **asimetrik yanal sıkıştırmayla (squeeze)** açıklamıştık. Bu bölümde o mekanizmayı matematiğe taşıyoruz: gelgit, radyal basınç alanının ikinci uzaysal türevidir. Standart fizikte "izsiz tensör" olarak soyutlanan özelliğin akışkanlar mekaniğinde **Evrenakı akı korunum yasası** olduğunu kanıtlayacak; hiçbir serbest parametre kullanmadan okyanus gelgit genliğini ($\Delta\zeta$) ve Güneş/Ay gelgit oranını (%46) türeteceğiz.

Gelgit, teoride yeni bir kuvvet değildir: **Kuvvet 1'in (kütle-itim, Ek M-35) uzaysal türevidir** ve tek bir yeni parametre bile gerektirmez.

> **Bu bölümün sözü — peşinen dürüst kayıt.** Türetimin ürettiği her sayı ($1/r^3$ yasası, $(+2,-1,-1)$ oranı, %46, 0,535 m) klasik gelgit kuramınınkiyle **birebir aynıdır.** Bu bölüm bir ayırt edici sınav değil, bir **tutarlılık türetimidir**: iddia, gözlemi klasik kuramdan farklı açıklamak değil, aynı sonuca mekanizmalı bir yoldan varmaktır. Ayrışan üç yapısal nokta 11.1.8'de toplanmıştır. Bölümün **ayırt edici bir sınavı yoktur**; şişkinlik kaymasının kaynağı da (11.1.9) ortam değil atomik sürtünmedir ve hesabı standart kuramla ortaktır.

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
| $\Phi$ | İtim potansiyeli, $\Phi\equiv(P-P_0)/\rho_n$ |
| $\Psi_T$ | Gelgit potansiyeli (ortak taşınma çıkarıldıktan sonraki artık) |
| $\zeta$ | Serbest yüzey yükseltisi (Anayasa S-27) |

**Varsayımlar**

1. **Kuvvet 1 geçerlidir:** $P(r)=P_0-\alpha M/r$, dolayısıyla $a_r=-\mathcal{G}M/r^2$ ve $\mathcal{G}=\alpha/\rho_n$ (Ek M-35).
2. **Uzanımlı gövde:** $b\ll r$; açılım birinci mertebede kesilir. Dünya–Ay için $b/r\approx0{,}017$.
3. **Akı korunumu:** Kaynaktan uzakta deplasman akısı ne yaratılır ne yok edilir. 11.1.3'te nicel biçime sokulur.
4. **Evrensel $\rho_n$:** Nükleon öz yoğunluğu bileşimden bağımsızdır ($2{,}7\times10^{17}$ kg/m³). Kuvvet 1 bu yüzden gövdenin *her* nükleonuna aynı ivmeyi verir.
5. **Kaynak dönmemektedir:** Ay kilitlidir, makro-girdabı bastırılmıştır (Bkz. 3.9.1). Dolayısıyla Dünya'ya yalnız Kuvvet 1 ve onun türevi etki eder; $\omega_1$ kökenli kuvvetler devrede değildir. Gerekçesi hemen aşağıdadır.

---

## 11.1.2 Kuvvet Envanteri: Kilitli Kaynak Neden Yalnız Kuvvet 1 Uygular?

Postülat 9'un beş hidrodinamik kuvveti iki köke ayrılır:

| Kol | Kuvvetler | Kilitli kaynakta |
|---|---|---|
| $\omega_2$ — **pompa** (boyutsal salınım) | **1** Radyal kütle-itim · **2** Diferansiyel sıkıştırma | **açık** |
| $\omega_1$ — **dönüş** (makro-vorteks) | 3 Vorteks sürüklenmesi · 4 Eksenel itim · 5 Yanal itim | **kapalı** |

Bu ayrım gelgit probleminde belirleyicidir, çünkü **Ay dönmemektedir.** Kilitli olduğu için kendi makro-girdabı bastırılmıştır (Bkz. 3.9.1 ve 3.4.4 — girdap rekabeti). Dönüş kolu kapalı olan bir kaynak, Dünya'ya vorteks sürüklenmesi, eksenel itim veya yanal itim uygulayamaz — bu üç kuvvetin taşıyıcısı yoktur.

Geriye yalnız pompa kolu kalır. Kuvvet 2 de bağımsız bir kuvvet olmadığı, Kuvvet 1'in uzaysal türevi olduğu için, **gelgitin tamamı tek bir kuvvete iner.**

Bu bir kısıt değil, türetimin temizliğidir: tensörün $(+2,-1,-1)$ yapısı $\omega_1$ kökenli hiçbir terimle karışmadan saf çıkar ve hesaba tek bir serbest katsayı girmez.

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

## 11.1.3 İtim Potansiyeli ve Çerçeve Adımı

Kütle-itim yasası $\vec a=-\frac{1}{\rho_n}\nabla P$'dir. $\rho_n$ sabit olduğundan bu ifade tam bir potansiyele indirgenir:

$$\Phi \equiv \frac{P-P_0}{\rho_n} \;\Longrightarrow\; \vec a = -\nabla\Phi,\qquad \Phi(r)=-\frac{\mathcal{G}M}{r}$$

Bu, standart fizikten ödünç alınmış bir kütleçekim potansiyeli **değildir**: basınç alanının nükleon öz yoğunluğuna bölünmüş hâlidir. Değeri aynı, kökeni farklıdır.

Gövde merkezi $\vec r$'de, gövde üzerindeki okyanus noktası $\vec r+\vec\xi$'dedir. İvme alanı açılır:

$$\vec a(\vec r+\vec\xi) = \vec a(\vec r) + (\vec\xi\cdot\nabla)\vec a + O(\xi^2)$$

**Kritik adım.** Kuvvet 1 gövdenin her nükleonuna $\vec a=-\frac{1}{\rho_n}\nabla P$ ile etki eder ve $\rho_n$ evrensel olduğundan bu ivme cismin cinsine bakmaz. Alanın **ortak** bileşeni $\vec a(\vec r)$ böylece gövdenin her noktasını aynı miktarda ivmelendirir: gövdeyi bir bütün olarak taşır, ama deforme etmez. Okyanusları kabartan, yalnızca bu ortak ivmeden sapan **artık ivmedir**:

$$\boxed{\;\Delta\vec a(\vec\xi) \equiv \vec a(\vec r+\vec\xi) - \vec a(\vec r) = \mathsf{T}\,\vec\xi,\qquad T_{ij}=\frac{\partial a_i}{\partial x_j}=-\frac{1}{\rho_n}\partial_i\partial_j P\;}$$

Gelgit tensörü, basınç alanının **ikinci** türevidir.

$\mathsf{T}$ simetrik olduğundan $\Delta\vec a(-\vec\xi)=-\Delta\vec a(\vec\xi)$ geçerlidir: gelgit ekseninin iki ucundaki artık ivmeler zıt yönlüdür, yani **ikisi de merkezden dışa** bakar. **Dünya'nın her iki yüzündeki — Ay'a bakan ve Ay'ın tam zıttındaki — çift okyanus şişkinliği, hiçbir ek varsayım olmadan doğrudan bu simetriden çıkar.**

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

## 11.1.4 Akı Korunumu ve Tensörün Bileşenleri

Önce ortamın korunum yasasını nicel biçime sokalım. Ek M-35'in ortam tepkisi $\dfrac{dP}{dr}=\dfrac{C\,Nq_n}{4\pi r^2}$ idi. Kaynağı çevreleyen herhangi bir $S$ küresi üzerinden basınç gradyanı akısı:

$$\oint_S \nabla P\cdot d\vec A = \frac{C\,Nq_n}{4\pi r^2}\cdot 4\pi r^2 = C\,Nq_n = \text{sabit}$$

Akı **yarıçaptan bağımsızdır.** Diverjans teoremiyle, kaynağı içermeyen herhangi bir küresel kabukta:

$$\int_V \nabla^2 P\,dV = \oint_{S_{dış}}\!\!\nabla P\cdot d\vec A \;-\; \oint_{S_{iç}}\!\!\nabla P\cdot d\vec A = 0 \;\Longrightarrow\; \nabla^2P=0$$

Fiziksel okuma nettir: kaynaktan çıkan deplasman akısı yolda ne çoğalır ne eksilir. **Evrenakı yaratılmaz, yok edilmez; yalnızca yer değiştirir.**

Bu sonucu şimdi *kullanmayacağız.* Tensörü ondan bağımsız kuracak, sonra iki yolun çakıştığını göstereceğiz.

**(a) Eksenel bileşen.** Doğrudan radyal ivmenin türevidir:

$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\!\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3} \;\Longrightarrow\; \Delta a_\parallel = +\frac{2\mathcal{G}M}{r^3}\,\xi_\parallel$$

*İşaret pozitif:* gelgit ekseni boyunca her iki uç da merkezden dışa kaçar.

**(b) Yanal bileşen.** Merkezden $\xi_\perp$ kadar yana kaymış noktada ivme yine kaynağa doğrudur; büyüklüğü $\mathcal{G}M/r'^2$ ($r'=\sqrt{r^2+\xi_\perp^2}\simeq r$), fakat doğrultusu merkez hattından $\xi_\perp/r$ kadar sapar:

$$a_\perp = -\frac{\mathcal{G}M}{r'^2}\cdot\frac{\xi_\perp}{r'} \simeq -\frac{\mathcal{G}M}{r^3}\,\xi_\perp \;\Longrightarrow\; T_\perp = -\frac{\mathcal{G}M}{r^3}$$

*İşaret negatif:* yanal doğrultularda hareket merkez hattına doğrudur. Bu, $1/r^2$ alanının **yakınsama geometrisidir** — radyal çizgiler kaynağa doğru birbirine yaklaşır, gövdenin yanakları merkez hattına itilir. Türetimde iz varsayımı kullanılmadı.

**Sıkıştırmanın çembersel olması.** Yukarıdaki hesapta $\xi_\perp$'nin *hangi* yanal doğrultu olduğu hiçbir yere girmedi — yalnız büyüklüğü girdi. Eksene dik bütün doğrultular kaynağa aynı uzaklıkta ve aynı yakınsama açısıyla baktığı için, gradyan yapısı **gövdenin Ay'a bakmayan bütün yanlarında eşittir.** Matematikte bunun karşılığı, $-1$ özdeğerinin **iki katlı dejenere** olmasıdır:

$$T_{\perp,1} = T_{\perp,2} = -\frac{\mathcal{G}M}{r^3}$$

Dejenerasyon, **gelgit ekseni** etrafındaki tam dönme simetrisinin ifadesidir. Sonuç fiziksel olarak şudur: sıkıştırma tek bir yönden gelen bir kıstırma değil, gelgit eksenini saran **eşit basınçlı bir kuşaktır** — çembersel sıkıştırma. Kuşağın hiçbir yerinde zayıf nokta yoktur; kaçış için tek yön kalır, o da gelgit eksenidir. Ve bu eksenin *iki* ucu birden açık olduğu için kabarma çift olur.

*(Kuşak, gelgit eksenine diktir — Dünya'nın ekvatoruna değil. Bkz. 11.1.3'teki uyarı.)*

**(c) İz bir sonuçtur.**

$$\mathrm{tr}\,\mathsf{T} = T_\parallel + 2T_\perp = \frac{2\mathcal{G}M}{r^3} - \frac{2\mathcal{G}M}{r^3} = 0$$

$$\boxed{\;\left(T_\parallel,\;T_\perp,\;T_\perp\right) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1)\;,\qquad \textstyle\sum\lambda_i = 0\;}$$

| Özdeğer | Doğrultu | Fiziksel okuma |
|---|---|---|
| $-1$ (×2, **dejenere**) | Gelgit eksenine dik **her** yön | **Neden:** Evrenakı, gelgit eksenini saran eşit basınçlı bir kuşakla çepeçevre sıkar |
| $+2$ | Gelgit ekseni boyunca | **Sonuç:** kuşaktan kaçan madde eksenin iki ucuna birden kabarır |

**Mekanizmanın üç adımı, tek tensörde.** Türetim boyunca kurulan zincir şudur: **(1)** Ay'ın kütle-itimi yakın yüzde güçlü, uzak yüzde zayıftır; merkeze göre fark alındığında gelgit ekseninin ön ve arka uçları dışa doğru artık ivme alır. **(2)** Gelgit eksenine dik doğrultularda gradyan yapısı her yerde eşittir — bu yüzden yanal sıkıştırma noktasal değil **çemberseldir.** **(3)** Hacmini koruyan gövde, eşit basınçlı kuşaktan kaçarak basıncın düştüğü tek yöne, yani gelgit eksenine uzar; eksenin iki ucu da açık olduğundan kabarma çift olur. Üç adım da tek bir tensörün üç bileşenidir.

*(Aynı sıkıştırma karşılıklıdır: Dünya da Ay'ı aynı geometriyle sıkar. Ay kilitli olduğu için oradaki kuşak gövde üzerinde dolaşmaz ve kabarma akışkan yerine magma üzerinde kalıcılaşır — mascon olgusu; Bkz. 3.9.5. Bu bölümün konusu Dünya'daki okyanus tepkisidir.)*

**İzsizlik bir varsayım değil, türetimin çıktısıdır.** Üç bileşen de bağımsız kuruldu ve iz kendiliğinden sıfır çıktı. Dahası $\mathrm{tr}\,\mathsf{T}=-\frac{1}{\rho_n}\nabla^2P$ olduğundan bu sonuç, bölümün başında akı korunumundan elde edilen $\nabla^2P=0$ ile **birebir aynı ifadedir**: iki bağımsız yol aynı sıfırı verir. Standart fizikte "gelgit tensörünün izsizliği" soyut bir alan özelliği olarak kaydedilir; burada iki yönden doğrulanmış bir **korunum teoremidir.** Yanaklardan sıkılan ($-1,-1$) hacim, eksende kabaran ($+2$) hacimle tam muhasebeleşir.

---

## 11.1.5 Nedenselliğin İspatı: Basınç Okuması

$(+2,-1,-1)$ simetrik bir nesnedir ve tek başına "yan sıkıştırma nedendir" demeye izin vermez — kinematik bir tensör nedensellik taşımaz. Nedensellik ancak fiziksel alana, yani basınca inilerek kurulur.

Çerçeve adımında taşınan kısım çıkarıldıktan sonra geriye kalan artık potansiyel, açılımın ikinci mertebe terimidir:

$$\Psi_T(\vec\xi) = -\tfrac12\left(T_\parallel\xi_\parallel^2 + T_\perp\xi_\perp^2\right) = -\frac{\mathcal{G}M}{2r^3}\left(2\xi_\parallel^2-\xi_\perp^2\right)$$

$\xi_\parallel=\xi\cos\psi$ ve $\xi_\perp=\xi\sin\psi$ konarak kapalı biçim:

$$\boxed{\;\Psi_T(\xi,\psi) = -\frac{\mathcal{G}M\,\xi^2}{2r^3}\left(3\cos^2\psi-1\right)\;}$$

Şimdi $\Phi=(P-P_0)/\rho_n$ tanımını tersine çevirip **artık basınç alanını** yazalım — teorinin fiilen konuştuğu büyüklük budur:

$$P_T(\xi,\psi) = \rho_n\Psi_T = -\frac{\rho_n\,\mathcal{G}M\,\xi^2}{2r^3}\left(3\cos^2\psi-1\right)$$

Gövde yüzeyinde ($\xi=b$) iki uç değer:

| Konum | $3\cos^2\psi-1$ | $P_T$ | Okuma |
|---|---|---|---|
| Eksen ($\psi=0^\circ,\,180^\circ$) | $+2$ | $-\dfrac{\rho_n\mathcal{G}Mb^2}{r^3}$ | **basınç açığı** |
| Yanaklar ($\psi=90^\circ$) | $-1$ | $+\dfrac{\rho_n\mathcal{G}Mb^2}{2r^3}$ | **basınç fazlası** |

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

## 11.1.8 Newton'la Sınır: Nerede Aynı, Nerede Ayrı

Dürüst kayıt özdeşlikten başlar:

| Büyüklük | Bu türetim | Klasik gelgit kuramı |
|---|---|---|
| Uzaklık yasası | $1/r^3$ | $1/r^3$ — aynı |
| Tensör özdeğerleri | $(+2,-1,-1)$ | $(+2,-1,-1)$ — aynı |
| Güneş/Ay oranı | 0,460 | 0,460 — aynı |
| Denge gelgiti genliği | 0,535 / 0,246 m | aynı |
| Büyük/küçük oranı | 2,70 | aynı |

**Tek bir sayı bile ayrışmaz.** Bu bölüm bir ayırt edici sınav değildir ve öyleymiş gibi sunulmaz. Ayrışma sayıda değil, üç yapısal noktadadır:

1. **İzsizlik teoremdir.** Klasik kuramda $\mathrm{tr}\,\mathsf{T}=0$, Laplace denkleminin soyut bir özelliği olarak kaydedilir; burada deplasman akısının korunumudur ve iki bağımsız yoldan üretilir (11.1.4).
2. **Eşdeğerlik ilkesi sonuçtur.** Klasik mekanikte postüla, burada $\rho_n$ evrenselliğinin türevi (11.1.7). Çerçeve adımı da aynı köke bağlıdır: ortak ivmenin gövdeyi deforme etmemesi, klasik türetimde eylemsiz çerçeve seçiminin sonucudur; burada Kuvvet 1'in her nükleona aynı ivmeyi vermesinin sonucudur. *(İki maddeyi ayrı saymıyoruz — kökleri aynı.)*
3. **Kuvvet envanteri kapalıdır.** Kilitli kaynağın dönüş kolu bastırılmış olduğundan gelgit, beş kuvvetten yalnız birine ve onun türevine iner (11.1.2). Klasik kuramda böyle bir envanter sorusu yoktur; teoride bu, tensörün saflığının gerekçesidir.

Bunlara mekanizmanın kendisi eklenir: teoride gelgiti yapan şey bir çekme değil, yapısı hesaplanabilen bir artık basınç alanıdır (kuşakta $+\tfrac12$, gelgit ekseninde $-1$). Bu alan klasik kuramda mevcut değildir — fakat bugünkü gözlem çözünürlüğünde iki kuramı ayıran bir ölçüm de henüz tanımlanmamıştır.

**Bu bölümün ayırt edici bir sınavı yoktur ve olduğu iddia edilmemektedir.** Şişkinlik kayması da (11.1.9) bu tabloyu değiştirmez: kaymanın kaynağı atomik sürtünmedir, hesabı standart kuramla ortaktır.

---

## 11.1.9 Şişkinlik Kayması: Kaymayı Yapan Sürtünme Atomiktir

Buraya kadar kurulan denge gelgiti **statik** tepkidir: kabarma, gelgit ekseniyle tam hizalıdır. Gözlem ise şunu söyler: şişkinlik ekseni Ay'ın doğrultusuyla çakışmaz, Dünya'nın hızlı dönüşü onu Ay'ın yaklaşık $3^\circ$ **önüne** taşır (Bkz. 3.9.2). Bu son adım, hangi sürtünmenin iş gördüğünü sormayı gerektirir.

### Ortam sürtünmesi bu işi *bu zaman ölçeğinde* yapamaz

Soruyu doğru sormak gerekir. Evrenakı sürtünmesi sıfır **değildir** — Postülat 7 $\eta_E$'yi "sıfıra çok yakın, kesinlikle sıfır değil" diye sabitler ve teori bu sıfır-olmayışı başka yerlerde kullanır: retrograd uyduların sönümü, halka bending-wave yitimi, yörünge kilitlenmesi (Bkz. 11.3.2). Ortam gerçekten sürükler; içinden geçtiği maddeye gerçekten tutunur. Mesele **yapıp yapmadığı değil, ne kadar sürede yaptığıdır.**

İki gevşeme zaman ölçeğini yan yana koyalım:

| Kanal | Gevşeme zamanı | Nereden |
|---|---|---|
| **Maddesel (atomik) sürtünme** | $\tau_{madde}\simeq QP/2\pi \approx 8{,}5\times10^{4}$ s ($\approx24$ saat) | $Q\approx12$, gelgit dönemi 12,42 sa |
| **Evrenakı kuplajı** | $\tau_{E}=\dfrac{2\rho_c b^{2}}{9\eta_E} \approx 1{,}5\times10^{21}$ s ($\approx5\times10^{13}$ yıl) | 11.3.2'nin Stokes yazımı, $\eta_E\approx3{,}3\times10^{-5}$ Pa·s |

$$\frac{\tau_E}{\tau_{madde}} \approx 1{,}8\times10^{16}$$

Evrenakı'nın gevşeme zamanı evren yaşının ~3500 katıdır. Gelgit ise **günlük** bir olaydır: 12,4 saatte bir tersine dönen bir zorlamaya, on altı mertebe daha yavaş bir kanalın derece mertebesinde faz kazandırması mümkün değildir. Üstelik yukarıdaki $\tau_E$ **en cömert** tahmindir: Ek M-43 Stokes yazımının Dünya–Ay rejiminde geçerli olmadığını, bağıl hızların kritik hızın ($v_{kav}$) çok altında kaldığını ve altkritik bastırmanın kuplajı daha da düşürdüğünü gösterir. Gerçek $\tau_E$ bundan büyüktür.

Muhasebenin öbür ucu da bunu doğrular: Dünya'nın ölçülen toplam gelgit enerji yitimi ~3,7 TW'tır ve ezici çoğunluğu **sığ denizlerdeki taban sürtünmesi ve türbülanstır** — su moleküllerinin kayaya sürtünmesi. Defter zaten kapalıdır.

**Sonuç:** kayma açısı ortamın değil **maddenin** defterindedir. Kaymayı yapan **atomik (malzeme) sürtünmesidir** — ortamın katkısı sıfır değil, fakat 11.1.9'un son bölümünde nicelendiği üzere $10^{-16}$ derece mertebesindedir.

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
> *Önceki taslakta bu kalem "teorinin ilk ayırt edici öngörü adayı" olarak yazılmıştı ve kaymanın Ek M-43'ün altkritik bastırmasından çıkacağı öngörülüyordu. **Bu yanlıştı ve geri alınmıştır:** yukarıdaki üç gerekçe ortam kuplajını dışlar. Yanlış rota, sürecin dürüst kaydı olarak burada bırakılmıştır.*

### Teorinin bu alanda söyleyebileceği tek ayrı şey: sıfırlanmayan taban

Malzeme sürtünmesi tümüyle sıfır olan bir gövde düşünülürse, standart kuram kayma açısının **tam olarak sıfır** olmasını gerektirir. Teoride ise $\eta_E\ne0$'dır; dolayısıyla sıfırlanmayan bir **artık kayma tabanı** kalır. İki kanalın faz katkıları gevşeme zamanlarıyla ters orantılı olduğundan bu tabanın büyüklüğü doğrudan yazılabilir:

$$\varepsilon_E \;\approx\; \varepsilon_{madde}\cdot\frac{\tau_{madde}}{\tau_E} \;\approx\; 3^\circ \times 5{,}6\times10^{-17} \;\approx\; \boxed{\;2\times10^{-16}\ \text{derece}\;}$$

Sayı, ayrımın hem gerçek hem de ölçülemez olduğunu aynı anda söyler: **sıfır değildir** (standart kuramın gerektirdiğinden farklıdır) ama Dünya'da maddesel terimin on altı mertebe altındadır. Bugün bir sınav oluşturmaz ve oluşturuyormuş gibi sunulmaz.

Kalemin sınanabilir hâle gelmesi, maddesel yitimin ihmal edilebilir olduğu ve gözlem penceresinin milyar yıl mertebesine uzadığı bir sistem gerektirir — yani tam olarak teorinin $\eta_E$'yi zaten kullandığı rejim (retrograd uydu göçü, kilitlenme zamanları, halka sönümü; Bkz. 11.3.2 ve Ek M-43). Gelgit kayması bu rejimin dışındadır; ayırt edici sınav gelgitte değil, o uzun-pencere olgularında aranmalıdır.

---

## 11.1.10 Geçerlilik Sınırı ve Açık Kalemler

**Geçerlilik sınırı.**

- $b\ll r$ birinci mertebe açılımıdır; $O(\xi^2)$ terimleri ihmal edilmiştir. Ay için $b/r\approx0{,}017$, hata mertebesi ~%2.
- İz sıfırlığı yalnız **kaynaksız** bölgede geçerlidir. Gövde içinde ($r<b$) akı sabit değildir, kapsanan nükleon sayısıyla büyür. Kaynak yoğunluğu $n_n=\rho_{madde}/m_n$ ile $\nabla^2P=Cq_n\rho_{madde}/m_n$ olur; Ek M-35'in $\mathcal{G}=\frac{Cq_n}{4\pi\rho_n m_n}$ ayrıştırması konduğunda tensör iz kazanır:

$$\mathrm{tr}\,\mathsf{T}\big|_{i\varsigma} = -4\pi\mathcal{G}\,\rho_{madde}$$

  Yani teori, gövde içinde Poisson denkleminin tam karşılığını üretir — yeni parametre girmeden, doğru katsayıyla. Bu bir öngörü değil, bir **tutarlılık kapanışıdır**: dışarıda sıfır, içeride $-4\pi\mathcal{G}\rho$.
- Denge gelgiti *statik* tepkidir; gerçek gelgit gecikmeli ve dinamiktir.
- Kuvvet envanteri argümanı (11.1.2) **kilitli kaynak** içindir. Hızlı dönen bir kaynağın $\omega_1$ kolu açıktır; o durumda Kuvvet 4/5 katkılarının ayrıca tartılması gerekir.

**Açık kalem — uzaklaşmanın bileşenleri.** 11.1.9'un kayma hesabı, Ay'ın ölçülen 3,8 cm/yıl'lık uzaklaşmasının **tamamını** öne kaymış şişkinliğin lob torkuna yükler. Bu varsayım altında çıkan açı ($2^\circ\!-\!3{,}5^\circ$) hem gözlemle hem bağımsız $Q$ değeriyle örtüşür. Fakat 3.9.4, uzaklaşmaya kozmolojik seyrelmeden gelen bir **taban terimi** de tanımlar. İki terimin bölüşümü nicel olarak sabitlenmemiştir ve buradaki uyum bir kısıt getirir: taban terimi uzaklaşmanın kayda değer bir kesrini taşısaydı, lob torkuna kalan pay küçülür ve geri çözülen kayma açısı gözlenen $\sim3^\circ$'nin altına düşerdi. Yani bu hesap, **lob teriminin baskın olduğunu** ve kozmolojik tabanın ikincil kaldığını söyler — 3.9.4'ün karşı-kayıt paragrafındaki okumayla uyumlu, aynı bölümün açılış paragrafındaki "asıl kaynak kozmolojiktir" ifadesiyle ise gerilim hâlindedir. Bölüşümün nicel kapatılması 7.4'ün hesap defterindedir.

---

Bir sonraki bölüm aynı basınç matematiğini dönen gövdenin kendi figürüne uygular: 11.2, Yanal İtimin $\sin2\theta$ yasasını türetir ve gezegen basıklığının klasik hidrostatik dengeden nerede ayrıldığını gösterir.
