# 11.1 Diferansiyel Sıkıştırma: Gelgit Tensörü ve Denge Gelgiti

Kısım 3.9'da Dünya üzerindeki okyanusların (ve Ay'ın) hareketini, uzaydan gelen görünmez bir "çekme" kuvvetiyle değil, Evrenakı akıntısının yarattığı **asimetrik yanal sıkıştırmayla (squeeze)** açıklamıştık. 

Bu bölümde; gelgit mekaniğini, radyal basınç alanının ikinci uzaysal türevi olan **Tensör** matematiğine taşıyacağız. Standart fizikte "izsiz tensör" olarak soyutlanan özelliğin, akışkanlar mekaniğinde **Evrenakı akı korunum yasası** olduğunu kanıtlayacak ve hiçbir serbest parametre kullanmadan okyanus gelgit genliğini ($\Delta\zeta$) ve Güneş/Ay gelgit oranını ($\%46$) türeteceğiz.

---

### 11.1.1 Notasyon ve Temel Varsayımlar

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

### 11.1.2 Çerçeve Adımı ve İtim Potansiyeli

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

### 11.1.3 Tensörün Bileşenleri ve Akı Korunumu

Gelgit tensörünün üç bileşeni birbirinden bağımsız olarak şu şekilde türetilir:

**(a) Eksenel Bileşen:** Doğrudan radyal ivmenin türevidir.
$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\!\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3}$$

**(b) Yanal Bileşen:** Merkezden $\xi_\perp$ kadar yana kaymış okyanus noktasında ivme kaynağa (Ay'a) doğrudur. Radyal (kaynağa) çizgilerin birbirine yaklaşmasından (yakınsama geometrisinden) ötürü gövdenin yanakları merkez hattına doğru itilir:
$$a_\perp = -\frac{\mathcal{G}M}{r'^2}\cdot\frac{\xi_\perp}{r'} \simeq -\frac{\mathcal{G}M}{r^3}\,\xi_\perp \;\Longrightarrow\; T_\perp = -\frac{\mathcal{G}M}{r^3}$$

**(c) İz Sıfırlığı (Sonuç):** Tensörün izi ($\mathrm{tr}\,\mathsf{T}$):
$$\mathrm{tr}\,\mathsf{T} = T_\parallel + 2T_\perp = \frac{2\mathcal{G}M}{r^3} - \frac{2\mathcal{G}M}{r^3} = 0$$

$$\boxed{\;(T_\parallel,\,T_\perp,\,T_\perp) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1),\qquad \mathrm{tr}\,\mathsf{T}=0\;}$$

İzsizlik, bir varsayım değil türetimin doğal sonucudur. Aynı zamanda $\mathrm{tr}\,\mathsf{T}=-\frac{1}{\rho_n}\nabla^2P$ olduğundan, $\nabla^2 P = 0$ sonucuna ulaşılır. Bu denklem uzay akışkanının **akı korunumunu** ifade eder: Kaynaktan çıkan deplasman akısı yolda ne çoğalır ne eksilir. Evrenakı yaratılmaz veya yok edilmez; ekvatordan sıkılan ($-1, -1$) hacim mecburen eksende uzar ($+2$).

---

### 11.1.4 Nedenselliğin İspatı (Basınç Okuması)

Tensördeki $(+2,-1,-1)$ yapısı, tek başına yan sıkıştırmanın "neden" olduğunu kanıtlamaz. Nedensellik, fiziksel basınç alanına inilerek görülür. Taşınan bileşen ivmeden çıkarıldıktan sonra geriye kalan "artık potansiyel" açılımın ikinci mertebe terimidir:
$$\Psi_T(\vec\xi) = -\tfrac12\left(T_\parallel\xi_\parallel^2 + T_\perp\xi_\perp^2\right) = -\frac{\mathcal{G}M}{2r^3}\left(2\xi_\parallel^2-\xi_\perp^2\right)$$
$$\boxed{\;\Psi_T(\xi,\psi) = -\frac{\mathcal{G}M\xi^2}{2r^3}\left(3\cos^2\psi-1\right)\;}$$

Bu ivme potansiyelini $\Phi=(P-P_0)/\rho_n$ üzerinden basınç alanına ($P_T$) çevirdiğimizde ve gövde yüzeyine ($\xi=b$) baktığımızda:
*   **Yanaklarda ($\psi=90^\circ$):** Basınç $+P_T$ olur (Basınç fazlası).
*   **Eksende ($\psi=0^\circ, 180^\circ$):** Basınç $-P_T$ olur (Basınç açığı).

Akışkan daima yüksek basınçtan düşük basınca doğru akar ($-\nabla P$). Okyanus suları basınç fazlası olan yanaklardan, basınç açığı olan eksenlere doğru itilir. **Sıkıştırma nedendir, kabarma sonuçtur.**

---

### 11.1.5 Denge Gelgiti Yüksekliği ve Güneş/Ay Oranı

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

Böylece, büyük Güneş kütlesine rağmen gelgitin %46'ya düşmesi ve okyanustaki 0.5 metrelik genlik, Evrenakı teorisinden milimetrik doğrulukla ve serbest parametresiz olarak türetilmiş olur.
