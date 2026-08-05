## Bölüm 6.6 — Küresel Basıklık ve Gezegen Figürü

Standart jeofizik ve astrofizikte dönen bir gezegenin şekli (figürü), iki temel kuvvetin dengesi olarak kabul edilir: gezegenin kendi kütleçekimi (şişmeye karşı çalışır) ve ekvatoral merkezkaç kuvveti (şişme yönünde çalışır). 

Ancak uydu jeodezisi, Juno ve Cassini gibi misyonlardan elde edilen süper-hassas yerçekimi haritaları, Güneş Sistemi'ndeki dev cisimlerin standart hidrostatik modellerle açıklanamayan spesifik figür anomalileri (özellikle $J_2$ ve $J_4$ harmoniklerinde) taşıdığını göstermiştir. Evrenakı teorisi, gezegen figürünü saf bir "çekim-merkezkaç" düellosu olarak değil, eterin (Zerre Katarı) hidrodinamik akışının yarattığı **dört terimli** bir denge olarak ele alır ve bu sayede açıklanamayan anomalilere doğrudan çözüm getirir.

### 6.6.1 Dört Terimli Denge Mekanizması

Evrenakı teorisinde bir gezegenin figürü, şu dört kuvvetin ortak sonucudur:

| Şişmeye Karşı Çalışanlar (Baskılayıcı) | Şişme Yönünde Çalışanlar (Şişirici) |
| :--- | :--- |
| **1. Radyal Kütle-İtim (F1):** Klasik kütleçekimiyle sayısal olarak özdeştir. | **3. Merkezkaç Kuvveti (M-22):** Klasik fizikteki gibi "sanal bir atalet" değildir; dönen Evrenakı girdabının yarattığı dışa doğru olan **reel basınç gradyanıdır** ($dP/dR=\rho v_\theta^2/R$). |
| **2. Eksenel İtim (F4):** Dönme eksenine doğru ($-\hat R$) baskı yapan hidrodinamik kuvvet. | **4. Yanal İtim (F5):** Ekvator **düzlemine doğru** ($-\hat\theta$) meridyenel geri çağırma, $\propto\sin2\theta$. |

> **F5 bir "şişirici" değildir.** F5'i *"ekvator düzleminde dışa savrulmayı destekleyen"* sütuna koymak yanlıştır: F5 **meridyenel** bir geri çağırıcıdır ve tam da basıklığın kurulacağı yerde — ekvatorda, $\theta=0$'da — $\sin2\theta=0$ ile **sıfırdır** (11.2.4). Şişme yönünde çalışmaz; maddeyi ekvator *düzlemine* bastırır. Figürdeki payı ayrıca dejeneredir ve merkezkaça soğurulur (6.6.2). Doğru okuma: **F5 düzlemi tanımlar, gövdeyi şişirmez.**

Radyal itim (F1) kütleçekimiyle birebir aynı matematiksel ağırlığı taşıdığı için, hidrostatik hesapta merkezkaça karşı dengelenmesinin tabanını oluşturur. Teorinin gezegen figürüne kattığı temel imza ise, klasik fizik modellerinde bulunmayan **F4 (Eksenel İtim)** ve **F5 (Yanal İtim)** kuvvetleridir. 

**Kopma Sınırları ve Kararlılık Garantisi:** 
Eksenel İtim (F4) ile Merkezkaç (M-22), aynı dönme hareketinin iki farklı yüzü olarak doğduklarından, Evrenakı teorisinde bu ikisinin birbirine oranı ($F_4 / F_{merkezkaç} = \lambda$) dönüş hızından **bağımsız sabit bir sayıdır**. Klasik fizikte yıldızlar çok hızlı döndüğünde merkezkaç sonsuza gidip yıldızı parçalamakla tehdit ederken, Evrenakı'da merkezkaç ne kadar artarsa onu dengeleyen F4 baskısı da tam aynı oranda artar. Bu sayede nötron yıldızları ve devasa kara delikler gibi astronomik hızlarda dönen cisimler parçalanmadan kararlılıklarını (stability) koruyabilirler.

### 6.6.2 Multipol Ayrıştırması ve Jeodezik Kanıtlar ($J_4$ İmzası)

Figür kanıtının matematiksel anahtarı, bu kuvvetlerin kütleçekim potansiyelindeki multipol ($P_n$) spektrumlarına ayrıştırılmasıdır. 

* **Merkezkaç ve Yanal İtim (F5):** Her iki kuvvet de matematiksel olarak saf $P_2$ karakterindedir. Yanal itim (F5), merkezkaç potansiyelinin sabit bir çarpanla yeniden ölçeklenmesine denktir. Yani F5, gezegeni farklı bir şekle sokmaz; gezegenin *biraz daha hızlı dönüyormuş gibi* algılanmasına yol açar.
* **Eksenel İtim (F4):** F4 ise figür potansiyelinde benzersizdir; saf bir $P_2$ değil, çok daha zengin bir spektrum ($P_2, P_4, P_6$) üretir.

Bu durum teorik açıdan muazzam bir kanıt penceresi açar. Merkezkaç kuvveti, gezegenin $J_4$ harmoniğine birinci mertebede **hiç katkı vermez** (hidrostatik $J_4$, merkezkaçın yalnızca zayıf, ikinci mertebe bir tepkisidir). Eksenel itim (F4) ise birinci mertebeden çok güçlü bir $P_4$ ($J_4$) imzası doğurur.

**Dünya'nın $J_4$ Verisiyle Uyum:**
Standart hidrostatik modeller, Dünya'nın hesaplanan $|J_4|$ değerini gözlemlenen değerden daha küçük bulur. Gözlem verisi ($-1{,}62 \times 10^{-6}$), merkezkaç kaynaklı hidrostatik tahminlerden daha *derindir*. Evrenakı'nın öngördüğü Eksenel İtim'in (F4) yarattığı $J_4$ katkısı ise tam olarak bu ölçümle **aynı işaretli ve aynı yöndedir.** Teori, klasik fizikte "açıklanamayan gürültü" veya "iç manto anomalisi" olarak görülen bu derinleşmeyi, eksenel eter akışının zorunlu geometrik bir sonucu olarak kendi içinden türetir.

### 6.6.3 Kompozisyonun ($\phi$) Figüre Etkisi — Sınav Geri Çekilmiş, $\phi$ Türetilmiştir

> [!IMPORTANT]
> **$\phi$ üzerinden kurulan "dört cisim sınavı" yürütülemez.** Dört gövdeye $\phi_\odot\approx0$, $\phi_\oplus\approx0{,}18$, $\phi_J\sim0{,}5$, $\phi_S\gtrsim0{,}6$ atayıp jeodezi verileriyle uyum ilan eden kurgu **üç bağımsız gerekçeyle** çöker (Ek M-39 Açık Uçlar md. 1 ve 11.2.3 ile aynı yönde):
>
> 1. **$\phi_\odot\approx0$ varsayımı geçersizdir.** Kavrama nükleon düzeyindedir ve iyonizasyon yalnız elektronu söker — plazmadaki proton kayadaki protonun aynısıdır. Üstelik $\phi_\odot\approx0$, Kısım 3.8'in tamamının dayandığı Güneş'in makro girdabını iptal ederdi; ve aynı argüman iç kütlesinin çoğu basınçla iyonize metalik hidrojen olan **Jüpiter'e en yüksek payı** verirdi — tablonun kendi mantığıyla çelişir.
> 2. **Ölçüm kanalı yoktur.** F5'in potansiyeli **saf $P_2$**'dir (6.6.2) ve merkezkaçla dejeneredir; $J_4$'e hiç katkı vermez. Dolayısıyla gözlenen bir figür fazlasından $\phi$ **ölçülemez**. Dünya'nın %0,42'lik fazlasından $\phi_\oplus\approx0{,}18$ "okumak" döngüsel bir çıkarımdı: aynı fazla, 6.6.2'de $\kappa_5$'i **sınırlamak** için kullanılıyor; ikisi birden yapılamaz.
> 3. **Fazla, teoriye ait olmayabilir.** Dünya'nın %0,42'lik $J_2$ fazlası jeofizikte hidrostatik-olmayan manto yapısıyla bağımsız modellenmiştir; o açıklama fazlanın tamamını hesaba katarsa teorinin payı **sıfıra iner**.
>
> **Yerine geçen doğru okuma:** figürün ölçülebilir imzası F5'te değil **F4'tedir** ($J_4$ kanalı, %4–8, işaret doğru — 6.6.2 ve 11.2.7). F5'in figürdeki payı çürütülmedi, *görünmez.*

**Ve $\phi$ artık gözlemden okunan bir nicelik değildir — hesaplanır.** Kompozisyon çarpanı, figür verisine uydurulmak yerine 11.4.1-(4)'te doğrudan türetilmiştir:

$$\phi(\rho) = \min\!\left(\frac{\rho}{\rho_*},\;\phi_{doy}\right),\qquad \rho_*=\frac{m}{v},\quad v=\frac{b_{vdW}}{4N_A}\ \ (\text{ya da iyonik hacimler})$$

Belirleyici olan **fazdır**, yoğunluk değil: kafesler temas ettikten sonra daha fazla sıkıştırma kafesi de küçültür ve $\phi$ paketlenme yapısına kilitlenir.

| Faz | $\phi_{doy}$ | Gerekçe |
| :--- | :--- | :--- |
| **Kristal katı** | **0,68 ± 0,06** | bcc 0,680 · fcc/hcp 0,7405 |
| **Yoğun akışkan** | **0,47 ± 0,03** | sert-küre **donma** sınırı $\eta_f=0{,}494$ — denge akışkanı bunu aşamaz |
| Açık yapılı sıvı | 0,36–0,42 | H-bağı ağı paketlenmeyi seyreltir (su) |

Yöntem, kitabın bağımsızca bildiği iki değer üzerinde kalibre edilmiştir: sıvı su $0{,}423$ (optik ters okuma $0{,}437$, moleküler paketlenme kestirimleri $0{,}36$–$0{,}40$ — tam arada) ve üst manto forsteriti $0{,}70$ (ters okuma $0{,}61$). Türetilen değerler:

| Cisim | Faz | $\phi$ (türetilmiş) | Önceki (geri çekildi) |
| :--- | :--- | :--- | :--- |
| **Dünya** | kristal katı (yüzey/manto silikatı) | **0,70** | ~~0,18~~ (figüre uydurulmuştu) |
| **Jüpiter** | yoğun akışkan H/He | **0,45–0,47** | ~~~0,5~~ (isabetliydi, gerekçesi yoktu) |
| **Satürn** | yoğun akışkan H/He | **0,45 ± 0,03** | ~~≥0,6~~ (basıklıktan çıkarılmıştı) |
| **Güneş** | tam iyonize plazma | **$1-\delta$**, $\delta\lesssim10^{-13}$ — delokalize elektron gazı ara hacmi doldurur; eşik altı cep için 3.000–11.000 protonluk boşluk gerekir (11.4.1-(5)) | ~~≈0~~ (geçersiz; işaret **ters** çıktı) |

Faz kuralının bir öngörüsü vardır ve artık seçim değildir: $\phi_{Satürn}/\phi_{Dünya}=0{,}47/0{,}68=\mathbf{0{,}69}$.

> **Basıklık ile $\phi$ arasında sezgisel beklenti ters işaretlidir.** *"En basık gezegen en yüksek $\phi$"* beklentisi yanlıştır: basıklık $\mathcal{Q}=\omega^2R_e^3/\mathcal{G}M$ ile gelir, $\phi$ ise **fazla** — ve Satürn en düşük yoğunluklu dev olduğu için $\phi$'si en **düşük** olanlardandır. Satürn'ün ayrıcalığı $\phi$'de değil, dönüşünü figürüne en az soğurmasındadır ($\mathcal{Q}/J_2=9{,}5$, sistemin en yükseği — 11.4.6).

### Sonuç

$\phi$ üzerinden kurulan dört cisim sınavı yürütülemez; yerine iki şey geçer. **(i)** Figürün ayrıştırılabilir imzası **F4**'ün $J_4$ kanalıdır (6.6.2): işaret doğru, pay %4–8, sınırlayıcı belirsizlik ölçüm değil hidrostatik referans modelidir. **(ii)** $\phi$ artık gözlemden okunan değil **türetilen** bir niceliktir (11.4.1-(4)), dolayısıyla figür verisi onu sınamak yerine $\kappa_5$'i sınırlamak için serbest kalır: Dünya basıklığı $\kappa_5\lesssim0{,}0114$–$0{,}0131$ verir, Ay'ın düğüm gerilemesi ise altı kat sıkısını ($\lesssim2{,}1\times10^{-3}$, 11.4.3).

Bir "kusursuz uyum" tablosunun yerini daha zayıf ama **döngüsel olmayan** bir sonuç alır. F5'in gerçek gözlemsel içeriği figürde değil, gövde dışındadır: halka dikey frekansındaki **tek-parite $(R_e/r)^3$** terimi hiçbir kütle çokkutbuyla taklit edilemez ve Satürn halkalarında ölçülebilir (Sınav 11.4-A, 11.4.4).
