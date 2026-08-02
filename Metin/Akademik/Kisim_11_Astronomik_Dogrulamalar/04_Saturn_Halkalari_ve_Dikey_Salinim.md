# 11.4 Satürn Halkaları ve Dikey Salınım (Ring Rain) Matematiği

Gezegen halkaları (Satürn modeli), Evrenakı'nın Yanal İtim (F5) alanındaki kararlı denge bölgesinin matematiksel bir izdüşümüdür. Madde, $f_{yanal}(\theta) = -(\kappa_5\rho v_e^2/r)\sin2\theta$ yasası gereği kutuplarda barınamaz, ekvator düzlemine doğru bastırılır. Ancak halkaların neden incecik (jilet gibi) kaldığı ve neden "ring rain" (halka yağmuru) mekanizmasıyla gezegene aktıkları, dikey salınım sönümlemesiyle hesaplanır (Bkz. Ek M-27).

## 11.4.1 Halka Kalınlığı ve Dikey Salınım Frekansı

Ekvatoral kararlı denge çevresinde ($\theta = 0^\circ$), küçük $\theta$ açıları için $\sin2\theta \approx 2\theta = 2(z/r)$ yaklaşımı yapılır (burada $z$ ekvator düzleminden dikey yükseklik, $r$ radyal uzaklıktır). Yanal kuvvet ivmesi:
$$a_z = -\left(\frac{2\,\kappa_5\,\rho_0\,v_e^2}{\rho_n\,r^2}\right) z$$

Bu denklem, standart basit harmonik osilatör ($\ddot{z} = -\Omega_z^2 z$) formundadır. Halka tanecikleri düzlem boyunca yukarı-aşağı harmonik salınım (pulsasyon) yapar. Dikey salınım frekansı:
$$\Omega_z = \frac{v_e}{r}\sqrt{\frac{2\,\kappa_5\,\rho_0}{\rho_n}}$$

Taneciklerin salınım hızı ve dolayısıyla halkanın maksimum dikey kalınlığı $h$, bu $\Omega_z$ frekansı ile yönetilir. Düzleme uygulanan Yanal İtim ne kadar güçlüyse (örneğin $\phi$ değeri yüksek gaz devlerinde), $\Omega_z$ o kadar yüksektir ve halka o kadar incedir. Satürn halkalarının şaşırtıcı inceliği (~10 metre) saf kütleçekiminden değil, Evrenakı'nın kompozisyona bağlı bu agresif $\sin2\theta$ ezme gücünden gelir.

## 11.4.2 Ortam Sönümü (Ring Rain)

Salınan halka tanecikleri mutlak bir vakumda dönmez; sürüklenen Evrenakı akışkanı içinde hareket ederler (Postülat 7 - Sürüklenme Zarfı). Tanecik, dikey salınım sırasında ortama göre bir bağıl dikey hız ($\dot{z}$) kazanır. 
Akışkanın Stokes biçimli sönüm katsayısı $\gamma_{ortam} = \frac{6\pi\eta_E r_t}{m}$ (burada $r_t$ tanecik yarıçapı, $m$ kütlesi) dikey hareketi zamanla sönümler.

Sönümlü harmonik osilatör denklemi:
$$\ddot{z} + \gamma_{ortam}\dot{z} + \Omega_z^2 z = 0$$

Gevşeme süresi $\tau = 2/\gamma_{ortam}$'dır. Zarf içi ortam kütle aktarmadığı halde, bu dikey sönümleme ve mikrometeorit çarpmalarından doğan plazma yükü, yörünge enerjisini emer. Yörünge enerjisini (ve açısal momentumunu) kaybeden taneciklerin yörüngesi yavaş yavaş bozunur. 

Sonuç olarak Satürn halkaları sarmal çizerek gezegenin atmosferine yağar (Cassini misyonunun "Ring Rain" keşfi). Bu sönüm yasası, halkaların jeolojik sürede kalıcı olamayacağını ve içe göçmek zorunda olduklarını nicel olarak ispatlar.
