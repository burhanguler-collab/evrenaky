# 11.1 Diferansiyel Sıkıştırma: Gelgit Tensörü ve Denge Gelgiti

Kısım 3.9'da Dünya üzerindeki okyanusların (ve Ay'ın) hareketini, uzaydan gelen görünmez bir "çekme" kuvvetiyle değil, Evrenakı akıntısının yarattığı **asimetrik yanal sıkıştırmayla (squeeze)** açıklamıştık. 

Bu bölümde; gelgit mekaniğini, radyal basınç alanının ikinci uzaysal türevi olan **Tensör** matematiğine taşıyacağız. Standart fizikte "izsiz tensör" olarak soyutlanan özelliğin, akışkanlar mekaniğinde **Evrenakı akı korunum yasası** olduğunu kanıtlayacak ve hiçbir serbest parametre kullanmadan okyanus gelgit genliğini ($\Delta\zeta$) ve Güneş/Ay gelgit oranını ($\%46$) türeteceğiz. Gelgit, teoride yeni bir kuvvet değildir: **kütle-itim alanının (Ek M-35) uzaysal türevidir** ve tek bir yeni parametre bile gerektirmez.

> **Bu bölümün sözü — peşinen dürüst kayıt.** Türetimin ürettiği her sayı ($1/r^3$ yasası, $(+2,-1,-1)$ oranı, %46, 0,535 m) klasik gelgit kuramınınkiyle **birebir aynıdır.** Bu bölüm bir ayırt edici sınav değil, bir **tutarlılık türetimidir**: iddia, gözlemi klasik kuramdan farklı açıklamak değil, aynı sonuca mekanizmalı bir yoldan varmaktır. Ayrışan üç yapısal nokta 11.1.7'de ayrıca toplanmış, teorinin bu alandaki ilk ayırt edici öngörü adayı ise 11.1.8'e açık kalem olarak yazılmıştır.

---

## 11.1.1 Notasyon ve Temel Varsayımlar

**Notasyon:**
*   $M$: Gelgiti yaratan kaynağın kütlesi (Ay veya Güneş)
*   $r$: Kaynak ile gövde merkezi arası uzaklık
*   $b$: Gövde yarıçapı (Dünya), $b \ll r$
*   $\vec\xi$: Gövde merkezinden ölçülen iç konum, $|\xi|\le b$
*   $\psi$: $\vec\xi$ ile gövde–kaynak ekseni arasındaki açı
*   $\Phi$: **İtim potansiyeli**, $\Phi\equiv(P-P_0)/\rho_n$
*   $\Psi_T$: Gelgit potansiyeli (taşınan çerçevedeki artık)
*   $\zeta$: Serbest yüzey yükseltisi (su kabarması)

**Varsayımlar:**
1. **Radyal kütle-itim alanı geçerlidir:** $P(r)=P_0-\alpha M/r$, dolayısıyla $a_r=-\mathcal{G}M/r^2$ ve $\mathcal{G}=\alpha/\rho_n$.
2. **Uzanımlı gövde:** $b \ll r$; kuvvet açılımı birinci mertebede kesilir.
3. **Akı korunumu:** Kaynaktan uzakta deplasman akısı yaratılmaz veya yok edilmez.
4. **Taşınan gövde çerçevesi (Postülat 7):** Gövde, sürüklenme zarfı içinde akıntıyla **bir bütün olarak** taşınır.
5. **Evrensel $\rho_n$:** Nükleon öz yoğunluğu bileşimden bağımsızdır.

---

## 11.1.2 Çerçeve Adımı ve İtim Potansiyeli

Kütle-itim yasası $\vec a=-\frac{1}{\rho_n}\nabla P$'dir. Nükleon yoğunluğu ($\rho_n$) sabit olduğundan, bu ifade tam bir itim potansiyeline indirgenir:
$$\Phi \equiv \frac{P-P_0}{\rho_n} \;\Longrightarrow\; \vec a = -\nabla\Phi,\qquad \Phi(r)=-\frac{\mathcal{G}M}{r}$$
*(Bu, Newtonyen kütleçekim potansiyeli değil, doğrudan uzay basıncı alanıdır.)*

Gövde merkezi $\vec r$'de, gövde üzerindeki okyanus noktası $\vec r+\vec\xi$'dedir. İvme alanı açılır:
$$\vec a(\vec r+\vec\xi) = \vec a(\vec r) + (\vec\xi\cdot\nabla)\vec a + O(\xi^2)$$

**Kritik Adım:** Sürüklenme zarfı gereği (Postülat 7), gövde Evrenakı akıntısıyla bir bütün olarak taşınır. Yani $\vec a(\vec r)$ ivmesi gövdenin **her** noktasına eşit etki eder ve gövdeyi deforme etmez. Okyanusları deforme eden (kabartan), yalnızca bu ortak ivmeden sapan **artık ivmedir (Gelgit Tensörü)**:

$$\boxed{\;\Delta\vec a(\vec\xi) \equiv \vec a(\vec r+\vec\xi) - \vec a(\vec r) = \mathsf{T}\,\vec\xi,\qquad T_{ij}=\frac{\partial a_i}{\partial x_j}=-\frac{1}{\rho_n}\partial_i\partial_j P\;}$$

Tensör $\mathsf{T}$ simetrik olduğundan $\Delta\vec a(-\vec\xi)=-\Delta\vec a(\vec\xi)$ geçerlidir: Eksenin iki ucundaki artık ivmeler zıt yönlüdür (ikisi de merkezden dışa bakar). **Dünya'nın her iki yüzündeki (Ay'a bakan ve Ay'ın tam zıttındaki) çift okyanus şişkinliği, hiçbir ek varsayım olmadan doğrudan bu simetriden çıkar.**

> [!NOTE]
> **Kavramsal Uzlaştırma:** Kısım 3.9.2'de gelgit mekanizması, Ay'ın Evrenakı akıntısını hızlandırması ve hızlanan akışkanın basıncının düşmesi (Bernoulli Prensibi) üzerinden nitel olarak açıklanmıştır. Bu bölümdeki tensörel türetim ise statik $P(r) = P_0 - \alpha M/r$ alanı üzerinden yürütülmüştür. 
> İki yaklaşım birbiriyle çelişmez, aynı gerçeğin farklı referans çerçevelerinden okunmasıdır:
> Burada kurulan **taşınan çerçevede** gövde akıntıyla beraber hareket eder; bağıl hız sıfırdır ve alan gövdeye göre statik görünür (Laplace/Tensör matematiği uygulanır). Gövdenin dışından, **akıntının içinden** bakan bir gözlemci için ise aynı basınç farkları, akışkanın hızlanıp yavaşlaması (Bernoulli dinamiği) olarak okunur. Her iki çerçeve de yanaklardaki diferansiyel sıkıştırmanın fiziksel gerçekliğini doğrular.

---

## 11.1.3 Akı Korunumu ve Tensörün Bileşenleri

Önce ortamın korunum yasasını nicel biçime sokalım. Ek M-35'in ortam tepkisi $\dfrac{dP}{dr}=\dfrac{C\,Nq_n}{4\pi r^2}$ idi. Kaynağı çevreleyen herhangi bir $S$ küresi üzerinden basınç gradyanı akısı:

$$\oint_S \nabla P\cdot d\vec A = \frac{C\,Nq_n}{4\pi r^2}\cdot 4\pi r^2 = C\,Nq_n = \text{sabit}$$

Akı **yarıçaptan bağımsızdır.** Diverjans teoremiyle, kaynağı içermeyen herhangi bir küresel kabukta

$$\int_V \nabla^2 P\,dV = \oint_{S_{dış}}\!\!\nabla P\cdot d\vec A \;-\; \oint_{S_{iç}}\!\!\nabla P\cdot d\vec A = 0 \;\Longrightarrow\; \nabla^2P=0$$

Fiziksel okuma nettir: kaynaktan çıkan deplasman akısı yolda ne çoğalır ne eksilir. **Evrenakı yaratılmaz, yok edilmez; yalnızca yer değiştirir.**

Bu sonucu şimdi *kullanmayacağız.* Tensörü ondan bağımsız kuracak, sonra iki yolun çakıştığını göstereceğiz. Gelgit tensörünün üç bileşeni şöyle türetilir:

**(a) Eksenel Bileşen:** Doğrudan radyal ivmenin türevidir.
$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\!\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3}$$

**(b) Yanal Bileşen:** Merkezden $\xi_\perp$ kadar yana kaymış okyanus noktasında ivme kaynağa (Ay'a) doğrudur. Radyal (kaynağa) çizgilerin birbirine yaklaşmasından (yakınsama geometrisinden) ötürü gövdenin yanakları merkez hattına doğru itilir:
$$a_\perp = -\frac{\mathcal{G}M}{r'^2}\cdot\frac{\xi_\perp}{r'} \simeq -\frac{\mathcal{G}M}{r^3}\,\xi_\perp \;\Longrightarrow\; T_\perp = -\frac{\mathcal{G}M}{r^3}$$

**(c) İz Sıfırlığı (Sonuç):** Tensörün izi ($\mathrm{tr}\,\mathsf{T}$):
$$\mathrm{tr}\,\mathsf{T} = T_\parallel + 2T_\perp = \frac{2\mathcal{G}M}{r^3} - \frac{2\mathcal{G}M}{r^3} = 0$$

$$\boxed{\;(T_\parallel,\,T_\perp,\,T_\perp) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1),\qquad \mathrm{tr}\,\mathsf{T}=0\;}$$

**İzsizlik bir varsayım değil, türetimin çıktısıdır.** Üç bileşen de bağımsız kuruldu ve iz kendiliğinden sıfır çıktı. Dahası $\mathrm{tr}\,\mathsf{T}=-\frac{1}{\rho_n}\nabla^2P$ olduğundan bu sonuç, bölümün başında akı korunumundan elde edilen $\nabla^2P=0$ ile **birebir aynı ifadedir**: iki bağımsız yol aynı sıfırı verir. Standart fizikte "gelgit tensörünün izsizliği" soyut bir alan özelliği olarak kaydedilir; burada iki yönden doğrulanmış bir **korunum teoremidir.** Yanaklardan sıkılan ($-1,-1$) hacim, eksende kabaran ($+2$) hacimle tam muhasebeleşir.

| Özdeğer | Doğrultu | Fiziksel okuma |
|---|---|---|
| $-1$ (×2) | Yanal | **Neden:** Evrenakı çepeçevre yandan sıkar |
| $+2$ | Eksenel | **Sonuç:** yandan sıkışan madde eksen boyunca iki yöne kabarır |

---

## 11.1.4 Nedenselliğin İspatı (Basınç Okuması)

Tensördeki $(+2,-1,-1)$ yapısı, tek başına yan sıkıştırmanın "neden" olduğunu kanıtlamaz. Nedensellik, fiziksel basınç alanına inilerek görülür. Taşınan bileşen ivmeden çıkarıldıktan sonra geriye kalan "artık potansiyel" açılımın ikinci mertebe terimidir:
$$\Psi_T(\vec\xi) = -\tfrac12\left(T_\parallel\xi_\parallel^2 + T_\perp\xi_\perp^2\right) = -\frac{\mathcal{G}M}{2r^3}\left(2\xi_\parallel^2-\xi_\perp^2\right)$$
$$\boxed{\;\Psi_T(\xi,\psi) = -\frac{\mathcal{G}M\xi^2}{2r^3}\left(3\cos^2\psi-1\right)\;}$$

Bu ivme potansiyelini $\Phi=(P-P_0)/\rho_n$ üzerinden basınç alanına çevirelim — teorinin fiilen konuştuğu büyüklük budur:

$$P_T(\xi,\psi) = \rho_n\Psi_T = -\frac{\rho_n\,\mathcal{G}M\,\xi^2}{2r^3}\left(3\cos^2\psi-1\right)$$

Gövde yüzeyinde ($\xi=b$) iki uç değer:

| Konum | $3\cos^2\psi-1$ | $P_T$ | Okuma |
|---|---|---|---|
| Eksen ($\psi=0^\circ,\,180^\circ$) | $+2$ | $-\dfrac{\rho_n\mathcal{G}Mb^2}{r^3}$ | **basınç açığı** |
| Yanaklar ($\psi=90^\circ$) | $-1$ | $+\dfrac{\rho_n\mathcal{G}Mb^2}{2r^3}$ | **basınç fazlası** |

Akışkan daima yüksek basınçtan düşük basınca doğru akar ($-\nabla P$). Okyanus suları basınç fazlası olan yanaklardan, basınç açığı olan eksenlere doğru itilir. **Sıkıştırma nedendir, kabarma sonuçtur.** Üstelik açık ile fazlanın oranının tam $2{:}1$ olması, $(+2,-1,-1)$ özdeğer yapısının basınç dilindeki birebir karşılığıdır. Klasik türetimde bu tabloya karşılık gelen hiçbir şey yoktur; orada basınç alanı yoktur, yalnız ivme farkı vardır.

**Ek M-26 ile çapraz denetim.** Yanakların ekseni ne kadar aştığı:
$$P_T(90^\circ)-P_T(0^\circ) = +\frac{3}{2}\cdot\frac{\rho_n\mathcal{G}Mb^2}{r^3} \;>\; 0$$
M-26'nın "suya batan top"u, tamamen farklı bir yoldan — hidrostatik derinlik–basınç muhasebesinden — aynı işareti vermişti ($F_{yan}-F_{dikey}\propto\rho g r>0$). İki bağımsız argüman, aynı elipsoid.

---

## 11.1.5 Denge Gelgiti Genliği ve Güneş/Ay Oranı

Okyanus serbest yüzeyi ($\zeta$), toplam potansiyelin sabit olduğu yüzeydir. Hacim korunduğundan ($\langle\zeta\rangle=0$), bu sabit tam olarak sıfırdır. Serbest okyanus yüzeyinin deniz seviyesinden genliği şöyle hesaplanır:
$$\zeta(\psi) = -\frac{\Psi_T}{g} = \frac{1}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^3 b\,\left(3\cos^2\psi-1\right)$$

En uç noktalar olan $\psi=0^\circ$ (tepe) ve $\psi=90^\circ$ (çukur) arasındaki tam genlik (fark) şöyledir:

$$\boxed{\;\Delta\zeta = \frac{3}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^{3} b\;}$$

Bu formül, hiçbir serbest parametre barındırmaz. Gezegen yarıçapı $b=6{,}371\times10^6$ m alınarak denetlendiğinde:

| Kaynak | Kütle Oranı ($M/M_\oplus$) | Uzaklık $(b/r)^3$ | Tepe Yüksekliği | Çukur Derinliği | Tam Genlik ($\Delta\zeta$) |
|---|---|---|---|---|---|
| **Ay** | $1{,}229\times10^{-2}$ | $4{,}553\times10^{-6}$ | $+0{,}357$ m | $-0{,}178$ m | **0,535 m** |
| **Güneş** | $3{,}331\times10^{5}$ | $7{,}724\times10^{-14}$ | $+0{,}164$ m | $-0{,}082$ m | **0,246 m** |

**Güneş / Ay Yarışı ve %46 Oranı:** 
Güneş'in Dünya üzerindeki toplam itme kuvveti ($\mathcal{G}M/r^2$) Ay'dan $179$ kat büyüktür. Fakat gelgiti yaratan şey itme gücü değil, basınç farkı (gradyanıdır). Gelgit gradyanı küple ($1/r^3$) zayıfladığı için oran:
$$\frac{\text{Güneş Gelgiti}}{\text{Ay Gelgiti}} = \frac{M_\odot/M_{Ay}}{(r_{Ay}/r_\odot)^3} = \frac{2{,}709\times10^7}{389{,}2^3} \approx 0{,}460$$

Aynı $0{,}460$ sayısı yukarıdaki tablodan da okunur ($0{,}246/0{,}535$): tensör oranı ile genlik oranı birbirini doğrular.

**Büyük ve küçük gelgit.** İki kaynağın genlikleri, hizalanma durumuna göre toplanır veya çıkarılır:

| Durum | Geometri | Hesap | Genlik |
|---|---|---|---|
| Büyük gelgit (*spring*) | Ay ve Güneş hizalı | $0{,}535+0{,}246$ | **0,781 m** |
| Küçük gelgit (*neap*) | Ay ve Güneş dik | $0{,}535-0{,}246$ | **0,289 m** |
| Oran | — | $0{,}781/0{,}289$ | **2,70** |

Açık okyanusta ölçülen denge gelgiti genliği ~0,5 m mertebesindedir (Pugh & Woodworth, 2014) — türetilen 0,535 m bu mertebeyi serbest parametresiz karşılar. Kıyılarda görülen metrelerce genlik ise havza rezonansının yerel büyütmesidir; gök mekaniğine değil kıyı hidrodinamiğine aittir ve bu modelin kapsamı dışındadır.

*Dürüstlük kaydı:* Buradaki uyum bir **mertebe ve yapı** doğrulamasıdır, hassas doğrulama değil. Denge gelgiti kuramı okyanus havzalarının geometrisini, derinliğini ve dinamik tepkisini içermez; gerçek okyanusta ölçülen yerel genlikler bu değerden düzenli olarak sapar. Doğrulanan şey, sıfır parametreli türetimin doğru mertebeyi ve doğru Güneş/Ay oranını vermesidir.

---

## 11.1.6 Eşdeğerlik İlkesi: Varsayım Değil, Sonuç

Tensörün biçimine bir kez daha bakalım: $T_{ij}=-\frac{1}{\rho_n}\partial_i\partial_jP$. Buradaki $\rho_n$ **nükleon öz yoğunluğudur** — su, kaya, demir, cıva fark etmez; hepsi aynı nükleonlardan kuruludur ve hepsi aynı $\rho_n$'yi taşır. Dolayısıyla gelgit ivmesi, üzerine etki ettiği maddenin bileşiminden **zorunlu olarak** bağımsızdır.

Klasik mekanikte bu bağımsızlık bir postülattır: eylemsiz kütle ile kütleçekimsel kütlenin eşitliği varsayılır, deneyle sınanır, fakat açıklanmaz. Burada türetilmiştir — tek bir evrensel $\rho_n$ olduğu için başka türlüsü yazılamaz.

**Bunun bedeli ve sınavı.** İfade tersine de okunur: $\rho_n$'nin evrenselliği bozulsaydı gelgit bileşime bağlı olurdu. Bu, teoriyi eşdeğerlik ilkesi testlerine doğrudan bağlar. MICROSCOPE uydusunun titanyum–platin çifti için bildirdiği $\eta_{EP} \lesssim 10^{-15}$ sınırı (Touboul ve ark., 2022) ile Eöt-Wash burulma terazisi ölçümleri (Schlamminger ve ark., 2008), teoride $\rho_n$ evrenselliğinin sınavıdır: bu deneylerin null sonuçları, teorinin bir varsayımını değil bir **türetiminin girdisini** doğrular.

---

## 11.1.7 Newton'la Sınır: Nerede Aynı, Nerede Ayrı

Dürüst kayıt özdeşlikten başlar:

| Büyüklük | Bu türetim | Klasik gelgit kuramı |
|---|---|---|
| Uzaklık yasası | $1/r^3$ | $1/r^3$ — aynı |
| Tensör özdeğerleri | $(+2,-1,-1)$ | $(+2,-1,-1)$ — aynı |
| Güneş/Ay oranı | 0,460 | 0,460 — aynı |
| Denge gelgiti genliği | 0,535 / 0,246 m | aynı |
| Büyük/küçük oranı | 2,70 | aynı |

**Tek bir sayı bile ayrışmaz.** Bu bölüm bir ayırt edici sınav değildir ve öyleymiş gibi sunulmaz; bir **tutarlılık türetimidir**. İddia, gözlemi klasik kuramdan farklı açıklamak değil, aynı sonuca mekanizmalı bir yoldan varmaktır. Ayrışma sayıda değil, üç yapısal noktadadır:

1. **Çerçeve fizikseldir.** Merkez ivmesinin çıkarılması klasik türetimde eylemsiz çerçeveye geçmek için yapılan bir muhasebe adımıdır — meşrudur, ama fiziksel karşılığı gösterilmez. Burada Postülat 7'nin sürüklenme zarfının doğrudan sonucudur: çift şişkinlik, seçilmiş bir çerçevenin değil, **taşınan bir gövdenin** özelliğidir.
2. **İzsizlik teoremdir.** Klasik kuramda $\mathrm{tr}\,\mathsf{T}=0$, Laplace denkleminin soyut bir özelliği olarak kaydedilir; burada deplasman akısının korunumudur (11.1.3).
3. **Eşdeğerlik ilkesi sonuçtur.** Klasik mekanikte postüla, burada $\rho_n$ evrenselliğinin türevi (11.1.6).

Bunlara mekanizmanın kendisi eklenir: teoride gelgiti yapan şey bir çekme değil, yapısı hesaplanabilen bir artık basınç alanıdır (yanakta $+\tfrac12$, eksende $-1$). Bu alan klasik kuramda mevcut değildir — fakat bugünkü gözlem çözünürlüğünde iki kuramı ayıran bir ölçüm de henüz tanımlanmamıştır. Teorinin gelgit alanındaki ilk gerçek ayırt edici adayı, aşağıdaki açık kalemdir.

---

## 11.1.8 Geçerlilik Sınırı ve Açık Kalemler

**Geçerlilik sınırı.**

- $b\ll r$ birinci mertebe açılımıdır; $O(\xi^2)$ terimleri ihmal edilmiştir. Ay için $b/r\approx0{,}017$, hata mertebesi ~%2.
- İz sıfırlığı yalnız **kaynaksız** bölgede geçerlidir. Gövde içinde ($r<b$) akı sabit değildir, kapsanan nükleon sayısıyla büyür. Kaynak yoğunluğu $n_n=\rho_{madde}/m_n$ ile $\nabla^2P = C q_n \rho_{madde}/m_n$ olur; M-35'in $\mathcal{G}=\frac{Cq_n}{4\pi\rho_n m_n}$ ayrıştırması konduğunda tensör iz kazanır:

$$\mathrm{tr}\,\mathsf{T}\big|_{i\varsigma} = -4\pi\mathcal{G}\,\rho_{madde}$$

  Yani teori, gövde içinde Poisson denkleminin tam karşılığını üretir — yeni parametre girmeden, doğru katsayıyla. Bu bir öngörü değil, bir **tutarlılık kapanışıdır**: dışarıda sıfır, içeride $-4\pi\mathcal{G}\rho$.
- Denge gelgiti *statik* tepkidir; gerçek gelgit gecikmeli ve dinamiktir.

**Açık kalem — şişkinlik kayması.** Gözlenen şişkinlik ekseni Ay'ın doğrultusunda değil, yaklaşık $3^\circ$ önündedir (Bkz. 3.9.2). Standart kuram bunu okyanus sürtünmesine ve gövdenin $Q$ katsayısına bağlar. Teorinin kendi rotası farklıdır: kaymanın, ortamın artık kuplajından — Ek M-43'ün altkritik bastırma rejiminden — çıkması beklenir. Bu hesap henüz yapılmamıştır ve teorinin gelgit alanındaki **ilk ayırt edici öngörü adayıdır**: tutarsa kayma açısı serbest bir sönüm parametresi olmaktan çıkıp türetilmiş bir sayı olur; tutmazsa dürüst kayıt olarak yazılır.

---

Bir sonraki bölüm aynı basınç matematiğini dönen gövdenin kendi figürüne uygular: 11.2, yanal itimin $\sin2\theta$ yasasını türetir ve gezegen basıklığının klasik hidrostatik dengeden nerede ayrıldığını gösterir.
