# 11.2 Yanal İtim: Küresel Basıklık ve Jeoit Formu Matematiği

Standart hidrostatik modellerde dönen bir gezegenin basıklığı (oblateness), kütleçekimi ile merkezkaç kuvveti arasındaki dengeye bağlanır. Evrenakı teorisinde denge **dört terimlidir**: radyal kütle-itim (F1), merkezkaç, eksenel itim (F4) ve yanal itim (F5). Bu bölüm F5'in $\sin2\theta$ yasasını türetir (Bkz. Ek M-39).

> **Peşinen dürüst kayıt — imza F5'te değil, F4'tedir.** Bölüm 6.6.2'nin (Sınav 1) multipol ayrıştırması iki sonuç verdi: **(i)** F5 saf $P_2$ üretir, dolayısıyla hiçbir yüksek harmonikte ($J_4$, $J_6$) **ayrı imzası yoktur**; genliği de Dünya basıklığından $\kappa_5\lesssim0{,}02$ ile sınırlanır — yani gezegen figüründe ölçülebilir etki bırakmaz. **(ii)** $J_4$ kanalı gerçekten açıktır, fakat **F4 için**: merkezkaç $J_4$'e birinci mertebede hiç katkı vermezken F4 verir, ve işaret kontrolü doğru çıkar (%4–8 düzeyinde). Dolayısıyla aşağıdaki türetim F5'in **yapısını** kurar; gözlemsel imzayı taşıyan kuvvet F4'tür.

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

Bu denklem, gezegen figürü dinamiğinin kalbidir ve iki yapısal sonucu vardır.

**Birinci sonuç — oran hızdan bağımsızdır.** Sağ tarafta ne $\omega$ ne $R$ vardır: yanal itimin merkezkaça oranı, gezegenin boyutundan ve dönüş hızından **tamamen bağımsızdır**, yalnızca kompozisyon çarpanına ($\phi$) bağlıdır. Bunun bedava getirdiği bir kazanç vardır: **dönen cisimlerin parçalanmaması için ayrı bir mekanizma gerekmez.** Klasik mekanikte $\omega$ arttıkça merkezkaç/çekim oranı büyür ve bir yerde 1'i aşar — sert bir kopma tavanı vardır. Burada oran $\omega$ ile büyümediği için **bir hızda kararlı olan cisim her hızda kararlıdır**; tavan kalkmaz ama kompozisyona bağlı sabit bir çarpanla yükselir.

**İkinci sonuç — $\rho_0/\rho_n$ katsayısı serbest değildir.** Ek M-8'in $\rho_0=\frac{1-k}{4}\rho_n$ sonucu ve $k=0$ ile bu çarpan **tam olarak $\tfrac14$**'tür. Yani oran yalnız $\kappa_5$ ve $\phi$ üzerinden ayarlanabilir; taban katsayı sabittir.

### Gövde sınıflarına uygulama

- **Karasal Gezegenler (Dünya):** Taşıl ve dış çekirdek sıvısıyla $\phi$ birkaç onda birlik mertebededir. Dünya'nın katı hidrostatik denge modelinde gözlenen ~%0,42'lik zayıf basıklık fazlası bu terimin **üst sınırını** verir: $\tfrac12\kappa_5\phi^2\lesssim0{,}0042$. *(Fazlanın jeofizikte bağımsız modellenmiş olduğu, dolayısıyla teorinin payının sıfıra kadar inebileceği kaydı için bkz. 6.6.2.)*
- **Gaz Devleri (Jüpiter, Satürn):** Moleküler/sıvı bağlı yapı oldukça derindir; $\phi$ en yüksek değerlerini burada alır. Merkezkaça eklenen bu katkı, Satürn'ün sistemin en basık gezegeni olmasının aday mekanik gerekçesidir.
- **Plazma ve Yıldızlar (Güneş):** Güneş'in ölçülen $J_2$ basıklığı ($2{,}2\times10^{-7}$), iç yoğunluk profili göz önüne alındığında hidrostatik/merkezkaç öngörüsüyle **uyumludur.** Fakat bu bir $\phi$ *ölçümü değildir*: yukarıdaki $\phi^2$ ölçeklemesiyle Güneş $J_2$'sinin ~%10'luk hassasiyeti ancak $\phi_\odot\lesssim0{,}9$ verir — yani $\phi=0$ ile de $\phi=0{,}8$ ile de uyumludur. Güneş'in figürünün küçük çıkması, kavramanın yokluğundan değil, **iki büyük terimin birbirini kısmen yemesinden** de kaynaklanabilir (eksenel itim F4 merkezkaçın zıddına çalışır — 6.6.2'nin işaret kontrolü bunu bağımsız olarak doğrular).

> [!WARNING]
> **Düzeltme kaydı (3 Ağustos 2026) — kaldırılan bir gerekçe.** Bu maddenin önceki sürümü şöyle yazıyordu: *"Tam iyonize plazmada bağlı kafes bulunmaz ($\phi\approx0$). Yanal itim sıfırlanır."* Bu gerekçe **üç yönden geçersizdir:**
>
> 1. **Teorinin kavraması nükleon düzeyindedir.** İyonizasyon **elektronu** söker; $\omega_1$ ve $\omega_2$ kolları ise nükleonun çift dönüşünden gelir. Plazmadaki proton, kayadaki protonun aynısıdır. Kavramayı kimyasal bağa yüklemek, teorinin kendi mekanizmasını terk etmektir — üstelik "Evrenakı için katı madde yoktur" kuralıyla da çelişir: ortam kabuktan ve mantodan geçtiğine göre kavrama kafesin sertliğinden gelemez.
> 2. **Güneş'in girdabını iptal eder.** $\phi_\odot\approx0$ olsaydı Güneş ortamı hiç sürüklemezdi; oysa Kısım 3.8'in tamamı Güneş'in gezegenleri taşıyan makro girdabını üretmesi üzerine kuruludur.
> 3. **Kendi paragrafıyla çelişir.** İki satır aşağıda gaz devlerine en yüksek $\phi$ verilir — oysa Jüpiter'in iç kütlesinin çoğu **basınçla iyonize metalik hidrojendir.** Güneş'i sıfırlayan gerekçe, Jüpiter'e en büyük payı verir.
>
> Ayrıca özel bir Güneş istisnası **gereksizdi**: Sınav 1 (6.6.2) $\kappa_5\lesssim0{,}02$ bularak yanal itimin gezegen figüründe **her yerde** ölçülebilir etki bırakmadığını göstermiştir. F5'i Güneş'te ayrıca iptal etmeye gerek yoktur.

## 11.2.4 Yanal İtimin Kararlılık Analizi

Kuvvetin büyüklüğü $|f| \propto \sin2\theta$ yapısındadır.
1. **Ekvatorda ($\theta=0^\circ$):** Kuvvet sıfırdır, ancak kararlı dengedir. En küçük sapmada madde tekrar ekvatora doğru itilir.
2. **Kutupta ($\theta=90^\circ$):** Kuvvet sıfırdır, ancak kararsız dengedir. Madde kutuplarda barınamaz, ekvatora savrulur.
3. **Maksimum Ezme ($\theta=45^\circ$):** İki eksenin ortasındaki orta enlemlerde ezici kuvvet zirveye ulaşır.

Standart fizikte merkezkaç potansiyeli $\cos\theta$ yapısındayken, Evrenakı'nın Yanal İtimi $\sin2\theta$ yapısındadır (45°'de maksimum). **Fakat kuvvet profillerinin farklı görünmesi, potansiyellerinin farklı multipol içerdiği anlamına gelmez** — ve buradaki ders geneldir: 6.6.2'nin multipol ayrıştırması F5'in **saf $P_2$** olduğunu, yani merkezkaçla aynı harmonikte oturduğunu ve $J_4$/$J_6$'da **ayrı imza bırakmadığını** gösterdi. İlk tasarım imzayı $J_4$'te arıyordu; gerekçesi "profiller farklı" idi ve yanlıştı.

Ayrıştırılabilir imzayı taşıyan kuvvet **F4'tür** (eksenel itim, Ek M-38): merkezkaç $J_4$'e birinci mertebede hiç katkı vermez, F4 verir — boş kanalda zayıf kuvvet görünür hâle gelir. Dünya için indüklenen $J_4$ payı %4–8 mertebesinde ve **işareti doğrudur** (gözlenen $J_4$ hidrostatik modellerin verdiğinden daha derindir; F4 tam o yönde çalışır). Bu, sınav programının olumsuz olmayan ilk sonucudur — geçilmiş bir sınav değil, "teorinin öngörüsü önemli olacak büyüklükte" durumu. Ayrıntı ve dürüst sınırları (hidrostatik referansın ~%10 belirsizliği, hidrostatik-olmayan manto katkısı) 6.6.2'dedir.
