# 11.1 Diferansiyel Sıkıştırma: Gelgit Tensörü ve Denge Gelgiti

Bu bölüm, Kısım 3.9'da anlatılan "suya batan top" (hidrostatik mengene) analojisinin matematiksel olarak kanıtlandığı bölümdür. Standart fizik, Ay'ın okyanusları uzaktan çektiğini varsayarken; Evrenakı teorisi bunu bir diferansiyel basınç tensörü üzerinden izsiz ($\nabla^2 P = 0$) bir akışkan korunum yasasına bağlar. Gelgit, yeni bir kütleçekim kuvveti değil, kütle-itim alanının (M-35) uzaysal türevidir.

## 11.1.1 Varsayımlar

1. **Radyal Kütle-İtim Alanı Geçerlidir:** $P(r) = P_0 - \alpha \frac{M}{r}$, dolayısıyla radyal kütle itim ivmesi $a_r = -\frac{\mathcal{G}M}{r^2}$'dir.
2. **Uzanımlı Gövde:** Test cismi noktasal değil, yarıçapı $b \ll r$ olan uzanımlı bir gövdedir (Örn. Dünya).
3. **Kaynaksız Ortam:** Kaynaktan uzakta ortam kaynaksızdır, yani akışkan yaratılmaz veya yok edilmez: $\nabla^2 P = 0$.

## 11.1.2 Tensörel Türetim

Gövde merkezi $r$'de, gövde üzerindeki okyanus noktası merkezden $\vec\xi$ kadar uzakta olsun:

$$\Delta a_i(\vec\xi) = \frac{\partial a_i}{\partial x_j}\xi_j + O(\xi^2),\qquad T_{ij}\equiv\frac{\partial a_i}{\partial x_j} = -\frac{1}{\rho_n}\partial_i\partial_j P$$

Gelgit tensörü, basınç alanının **ikinci** türevidir.

**(a) Eksenel bileşen (Ay'a bakan ve zıt olan yönler):**
$$T_\parallel = \frac{da_r}{dr} = \frac{d}{dr}\left(-\frac{\mathcal{G}M}{r^2}\right) = +\frac{2\mathcal{G}M}{r^3} \;\Longrightarrow\; \Delta a_\parallel = +\frac{2\mathcal{G}M}{r^3}\xi_\parallel$$
*Sonuç Pozitif:* Uzak uç da yakın uç da merkezden **dışa** doğru kaçar. Bu, eksen boyunca okyanusların iki taraflı kabarmasıdır.

**(b) Yanal bileşenler (Ekvatoral yanaklar):**
Kaynaksız bölgede basınç izi sıfırdır ($\mathrm{tr}\,T = -\frac{1}{\rho_n}\nabla^2 P = 0$). Dolayısıyla:
$$T_\parallel + 2T_\perp = 0$$
$$T_\perp = -\frac{T_\parallel}{2} = -\frac{\mathcal{G}M}{r^3} \;\Longrightarrow\; \Delta a_\perp = -\frac{\mathcal{G}M}{r^3}\xi_\perp$$
*Sonuç Negatif:* Yanal doğrultularda hareket merkez hattına doğrudur. Bu, okyanusları yanlardan ezen **sıkıştırmadır**.

## 11.1.3 Matematiksel Sonuç ve Korunum Yasası

$$\boxed{\;\left(T_\parallel,\;T_\perp,\;T_\perp\right) = \frac{\mathcal{G}M}{r^3}\,(+2,\,-1,\,-1)\;,\qquad \textstyle\sum\lambda_i = 0\;}$$

| Özdeğer | Doğrultu | Fiziksel okuma |
|---|---|---|
| $-1$ (×2) | Yanal | **Neden:** Evrenakı yanaklardan sıkar |
| $+2$ | Eksenel | **Sonuç:** Yandan sıkışan madde eksen boyunca kabarır |

İz sıfırlığı ($\nabla^2P=0$) tam olarak şunu söyler: **Evrenakı yaratılmaz, yok edilmez; yalnızca yer değiştirir.** Standart fizikte "gelgit tensörünün izsizliği" soyut bir özellik olarak kaydedilir; teorimizde bu, **akışkan korunum yasasının ta kendisidir**.

## 11.1.4 Nicel Öngörü: Denge Gelgiti Yüksekliği

Gelgit potansiyeli $\Psi_T=-\frac{GMb^2}{2r^3}(3\cos^2\psi-1)$ ve serbest yüzey koşulu $g\,h+\Psi_T=$ sabit eşitliğiyle okyanus kabarması hesaplanır:

$$\boxed{\;\Delta h = \frac{3}{2}\,\frac{M}{M_\oplus}\left(\frac{b}{r}\right)^{3} b\;}$$

Bu formül, hiçbir serbest parametre içermeyen saf bir matematiksel sonuçtur:

| Kaynak | $M/M_\oplus$ | $(b/r)^3$ | Çıkan Yükseklik ($\Delta h$) |
|---|---|---|---|
| Ay | $1{,}229\times10^{-2}$ | $4{,}553\times10^{-6}$ | **0,53 m** |
| Güneş | $3{,}331\times10^{5}$ | $7{,}724\times10^{-14}$ | **0,25 m** |

**Oran Kontrolü:** Güneş ve Ay gelgitinin toplam kuvvete oranlandığında Güneş'in %46 ($0,46$) civarında etki yaptığı görülür. Açık okyanusta ölçülen denge gelgiti mertebesi ~0,5 metredir. Kıyılarda görülen metrelerce genlik, havza rezonansının (suyun kıyılara çarpıp yığılması) yerel büyütmesidir ve gök mekaniğine dâhil değildir. Sayılar gözlemle birebir örtüşür.
