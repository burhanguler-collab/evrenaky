# 11.1 Diferansiyel Sıkıştırma: Gelgit Tensörü ve Denge Gelgiti

Kısım 3.9'da Dünya üzerindeki okyanusların (ve Ay'ın) hareketini, uzaydan gelen görünmez bir "çekme" kuvvetiyle değil, Evrenakı akıntısının yarattığı **asimetrik yanal sıkıştırmayla (squeeze)** açıklamıştık. 

Bu bölümde; nitel olarak ifade edilen "suya batan top" (hidrostatik mengene) analojisinden yola çıkarak, makroskobik mekaniği önce tensörel izsizlik denklemlerine ($\nabla^2 P = 0$) dönüştürecek, ardından hiçbir serbest parametre kullanmadan $0{,}53$ metrelik okyanus gelgitini ve $\%46$'lık Güneş/Ay oranını matematiksel olarak türeteceğiz.

## 11.1.1 Makroskobik "Suya Batan Top" Analojisi

Bir hidrostatik sıvı içine batırılmış, yarıçapı $r$, merkez derinliği $d$ olan yumuşak bir top (Dünya modeli) düşünelim. Top, akışkan basıncı ($P = \rho g \cdot \text{derinlik}$) nedeniyle alttan, üstten ve yanlardan kuvvetlere maruz kalır. 

*   **Alt ve Üst Kuvvetler:** Üstten vuran kuvvet $F_{üst} \propto \rho g (d-r)$, alttan vuran kuvvet $F_{alt} \propto \rho g (d+r)$'dir.
*   **Kaldırma Payının Ayrılması:** Alttan ve üstten vuran kuvvetlerin farkı ($F_{alt} - F_{üst} \propto 2\rho g r$) topu yukarı iten kaldırma kuvvetidir. Bu pay ayrıldıktan sonra, topu dikey eksende ezen "efektif dikey sıkıştırma", zayıf olan kuvvete ($F_{üst}$) eşittir: $F_{dikey\_ezme} = F_{üst} \propto \rho g(d-r)$.
*   **Yan Kuvvetin Baskınlığı:** Yanlardan vuran ortalama kuvvet ise merkez derinliğine bağlıdır: $F_{yan} \propto \rho g d$.

Bu iki sıkıştırma eksenini karşılaştırdığımızda matematiksel eşitsizlik doğar:
$$F_{yan} - F_{dikey\_ezme} \propto \rho g d - \rho g (d-r) = \rho g r > 0$$

**Sonuç:** Yanlardan vuran güç ($F_{yan}$), dikey eksendeki ezme gücünden daima daha büyüktür. Hacmini koruyan top, yanlardan gelen bu şiddetli sıkışmadan kaçarak basıncın nispeten zayıf kaldığı dikey eksene doğru uzamak zorundadır. **Elipsoid form (kabarma)**, uzaktan çekilmenin değil, yan kuvvetlerin galibiyetinin sonucudur.

## 11.1.2 Tensörel Türetim ve İzsizlik ($\nabla^2 P = 0$)

Şimdi bu makroskobik elipsoidi, saf Evrenakı (Cosmofluid) matematiğine dönüştürelim. Radyal kütle-itim alanı $P(r) = P_0 - \alpha \frac{M}{r}$'dir (dolayısıyla radyal ivme $a_r = -\frac{\mathcal{G}M}{r^2}$). Gelgit tensörü ($T_{ij}$), bu kütle-itim alanının **ikinci uzaysal türevidir**:

$$T_{ij}\equiv\frac{\partial a_i}{\partial x_j} = -\frac{1}{\rho_n}\partial_i\partial_j P$$

Gövde merkezi $r$'de, gövde üzerindeki okyanus noktası merkezden $\vec\xi$ kadar uzakta olsun. Kaynaktan (Ay'dan) uzaktaki bu bölgede Evrenakı akışkanı kaynaksızdır (yaratılmaz veya yok edilmez). Bu durum Laplace denklemiyle ifade edilir: $\nabla^2 P = 0$.

**(a) Eksenel bileşen (Ay'a bakan ve zıt yönler):**
$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3} \;\Longrightarrow\; \Delta a_\parallel = +\frac{2\mathcal{G}M}{r^3}\xi_\parallel$$
*(+2 Sonucu)*: Eksen boyunca sular merkezden dışa doğru (iki taraflı) fışkırır.

**(b) Yanal bileşenler (Ekvatoral yanaklar):**
Kaynaksız bölgede basınç izi sıfır olduğundan ($\mathrm{tr}\,T = 0$):
$$T_\parallel + 2T_\perp = 0 \;\Longrightarrow\; T_\perp = -\frac{T_\parallel}{2} = -\frac{\mathcal{G}M}{r^3}$$
*(-1 Sonucu)*: Yanal doğrultularda hareket merkeze doğrudur (sıkıştırma).

**Tensör Matrisi:**
$$\boxed{\;\left(T_\parallel,\;T_\perp,\;T_\perp\right) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1)\;,\qquad \textstyle\sum\lambda_i = 0\;}$$

Standart fizikte gelgit tensörünün izsizliği soyut bir geometri özelliği olarak öğretilir. Evrenakı teorisinde ise bu, **akışkan korunum yasasıdır**: Ekvatordan sıkılan (-1, -1) hacim yok olmaz, yer değiştirerek kutuplardan (+2) fışkırır. 

## 11.1.3 Sayısal Sınav: Denge Gelgiti ve %46 Oranı

Gelgit gradyanı ($T \propto M/r^3$), okyanus yüzeyinde $\Psi_T=-\frac{GMb^2}{2r^3}(3\cos^2\psi-1)$ potansiyeli yaratır. Serbest yüzey koşuluyla, okyanusun (Dünya yarıçapı $b$) ne kadar kabaracağı ($\Delta h$) serbest parametre olmadan doğrudan hesaplanır:

$$\boxed{\;\Delta h = \frac{3}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^{3} b\;}$$

| Kaynak | Kütle Oranı ($M/M_\oplus$) | Uzaklık Küpü $(b/r)^3$ | Çıkan Yükseklik ($\Delta h$) |
|---|---|---|---|
| **Ay** | $1{,}229\times10^{-2}$ | $4{,}553\times10^{-6}$ | **0,53 m** |
| **Güneş** | $3{,}331\times10^{5}$ | $7{,}724\times10^{-14}$ | **0,25 m** |

**Güneş / Ay Yarışı:** Güneş'in toplam akışkan (kütle-itim) gücü Ay'dan 177 kat büyüktür. Ancak yukarıdaki formülde görüldüğü üzere, gelgiti yaratan şey itim gücü değil, yanaklar arasındaki farktır (gradyan). Uzaklığın karesi ($1/r^2$) yerine küpüyle ($1/r^3$) zayıflayan bu asimetride; Güneş kütleden kazandığı 27 milyonluk avantajı, Ay'dan 390 kat uzakta olduğu için uzaklıktan ($390^3 \approx 59.000.000$) kaybeder:

$$\frac{\text{Güneş Gelgiti}}{\text{Ay Gelgiti}} = \frac{2{,}7\times10^7}{390^3} \approx 0{,}46$$

Açık okyanusta uydularla ölçülen denge gelgiti mertebesi tam olarak $0{,}5$ metredir ve Güneş'in etkisi %46 bandındadır. Sayılar serbest parametre olmaksızın, tamamen hidrodinamik basınç profili üzerinden gerçeğe birebir oturur.
