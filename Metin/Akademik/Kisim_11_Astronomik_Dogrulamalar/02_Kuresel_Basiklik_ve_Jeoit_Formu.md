# 11.2 Yanal İtim: Küresel Basıklık ve Jeoit Formu Matematiği

Standart hidrostatik modellerde dönen bir gezegenin basıklığı (oblateness), kütleçekimi ile merkezkaç kuvveti arasındaki dengeye bağlanır. Ancak dev gezegenlerde gözlenen ve klasik hidrostatik dengeyle açıklanamayan anomaliler ($J_4$ harmoniği, aşırı basıklık), Evrenakı teorisinde dördüncü bir denge faktörü olan **Yanal İtimin ($\sin 2\theta$ yasası)** doğal bir sonucudur (Bkz. Ek M-39).

## 11.2.1 Geometri ve Varsayımlar

1. **Koordinat Geometrisi:** Küresel koordinatlarda $R=r\cos\theta$ (eksene uzaklık) ve $z=r\sin\theta$ (ekvator düzlemine uzaklık), burada $\theta$ ekvatordan ölçülen enlemdir.
2. **Kavrama Kesri ($\phi$):** Gezegenin rotasyonel sürüklemesi tam eşzamanlı değildir. Ortam, Fizeau akıntı deneyinde olduğu gibi ($\mathcal{R}=\phi=1-1/n^2$), yalnızca madde kafesinin hacmi kadar bir kesirle ($\phi$) taşınır. Dolayısıyla gezegen yüzeyindeki ekvatoral sürüklenme hızı $v_e = \phi\,\omega R$'dir. 
3. **Deplasman Kapanışı (Yanal İtim):** Akışın bıraktığı basınç açığı kinetik ölçeklemeyle belirlenir: $\Delta P(\theta) = -\kappa_5\,\rho\,v(\theta)^2$. İdeal akış için $\kappa_5 = \frac{1}{2}$ kabul edilir.

## 11.2.2 Yanal Kuvvetin ($\sin 2\theta$) Türetimi

Yüzeydeki enleme bağlı Evrenakı akış hızı $v(\theta) = v_e\cos\theta$ olduğundan, yüzey basınç profili:
$$P(\theta) = P_{kutup} - \kappa_5\,\rho\,v_e^2\cos^2\theta$$

Basıncın küresel yüzeydeki açısal gradyanı ($\nabla_\theta P = \frac{1}{r}\frac{dP}{d\theta}$) alınır. Türev operatörü işletildiğinde:
$$\frac{d}{d\theta}(\cos^2\theta) = -2\cos\theta\sin\theta = -\sin2\theta$$
$$\frac{dP}{d\theta} = \kappa_5\rho v_e^2\sin2\theta$$

Birim hacme düşen kuvvet $f_{yanal} = -\nabla P$ olduğundan:

$$\boxed{\;f_{yanal}(\theta) = -\frac{\kappa_5\,\rho\,v_e^{2}}{r}\,\sin 2\theta\qquad [\mathrm{N/m^3}]\;}$$

*Matematiksel İmza:* Eksi işareti ($-\hat\theta$), kuvvetin yönünün her iki yarımküreden de **ekvatora doğru** olduğunu gösterir.

## 11.2.3 Merkezkaç Oranı ve Kompozisyon Bağımlılığı

İvme formuna geçildiğinde ($a_{yanal} = f_{yanal}/\rho_n$) ve $v_e = \phi\,\omega R$ (burada $R = r\cos\theta$) yerine konulduğunda, Yanal İtim ivmesinin Merkezkaç ivmesine ($a_{merkezka\text{ç}} = \omega^2 R$) oranı sadeleşir:

$$\frac{a_{yanal}}{a_{merkezka\text{\c{c}}}} = \kappa_5\left(\frac{\rho_0}{\rho_n}\right)\phi^{2}\cdot 2\sin\theta$$

Bu denklem, gezegen figürü dinamiğinin kalbidir. Yanal itim, gezegenin kendi boyutu veya dönüş hızından tamamen bağımsızdır; yalnızca **kompozisyon çarpanına ($\phi$)** bağlıdır.

- **Plazma ve Yıldızlar (Güneş):** Tam iyonize plazmada bağlı kafes bulunmaz ($\phi \approx 0$). Yanal itim sıfırlanır. Güneş'in ölçülen $J_2$ basıklığı ($2{,}2\times10^{-7}$) saf hidrostatik/merkezkaç öngörüsüyle kusursuz örtüşür.
- **Karasal Gezegenler (Dünya):** Taşıl ve dış çekirdek sıvısıyla $\phi \approx 0{,}18$ mertebesindedir. Bu, Dünya'nın katı hidrostatik denge modelinde gözlenen ~%0,42'lik zayıf basıklık fazlasını karşılar.
- **Gaz Devleri (Jüpiter, Satürn):** Moleküler/sıvı bağlı yapı oldukça derindir ($\phi \gtrsim 0{,}5 - 0{,}6$). Merkezkaça eklenen bu devasa yanal katkı, Satürn'ün sistemin en basık gezegeni olmasının mekanik gerekçesidir.

## 11.2.4 Yanal İtimin Kararlılık Analizi

Kuvvetin büyüklüğü $|f| \propto \sin2\theta$ yapısındadır.
1. **Ekvatorda ($\theta=0^\circ$):** Kuvvet sıfırdır, ancak kararlı dengedir. En küçük sapmada madde tekrar ekvatora doğru itilir.
2. **Kutupta ($\theta=90^\circ$):** Kuvvet sıfırdır, ancak kararsız dengedir. Madde kutuplarda barınamaz, ekvatora savrulur.
3. **Maksimum Ezme ($\theta=45^\circ$):** İki eksenin ortasındaki orta enlemlerde ezici kuvvet zirveye ulaşır.

Standart fizikte merkezkaç potansiyeli $\cos\theta$ yapısındayken (ekvatorda maksimum), Evrenakı'nın Yanal İtimi $\sin2\theta$ yapısındadır (45°'de maksimum). Bu fark, yüksek dereceli küresel harmoniklerde ($J_4, J_6$) uydu jeodezisinde ayrıştırılabilir, eşsiz bir dinamik imza bırakır.
