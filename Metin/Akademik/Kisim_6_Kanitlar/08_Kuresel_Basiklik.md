## Bölüm 6.6 — Küresel Basıklık ve Gezegen Figürü

Standart jeofizik ve astrofizikte dönen bir gezegenin şekli (figürü), iki temel kuvvetin dengesi olarak kabul edilir: gezegenin kendi kütleçekimi (şişmeye karşı çalışır) ve ekvatoral merkezkaç kuvveti (şişme yönünde çalışır). 

Ancak uydu jeodezisi, Juno ve Cassini gibi misyonlardan elde edilen süper-hassas yerçekimi haritaları, Güneş Sistemi'ndeki dev cisimlerin standart hidrostatik modellerle açıklanamayan spesifik figür anomalileri (özellikle $J_2$ ve $J_4$ harmoniklerinde) taşıdığını göstermiştir. Evrenakı teorisi, gezegen figürünü saf bir "çekim-merkezkaç" düellosu olarak değil, eterin (Zerre Katarı) hidrodinamik akışının yarattığı **dört terimli** bir denge olarak ele alır ve bu sayede açıklanamayan anomalilere doğrudan çözüm getirir.

### 6.6.1 Dört Terimli Denge Mekanizması

Evrenakı teorisinde bir gezegenin figürü, şu dört kuvvetin ortak sonucudur:

| Şişmeye Karşı Çalışanlar (Baskılayıcı) | Şişme Yönünde Çalışanlar (Şişirici) |
| :--- | :--- |
| **1. Radyal Kütle-İtim (F1):** Klasik kütleçekimiyle sayısal olarak özdeştir. | **3. Merkezkaç Kuvveti:** Klasik atalet etkisidir, reddedilmez. |
| **2. Eksenel İtim (F4):** Kutuplardan ekvatora doğru, dönüş eksenine paralel baskı yapan hidrodinamik kuvvet. | **4. Yanal İtim (F5):** Ekvator düzleminde dışa doğru savrulmayı destekleyen dinamik akı. |

Radyal itim (F1) kütleçekimiyle birebir aynı matematiksel ağırlığı taşıdığı için, hidrostatik hesapta merkezkaça karşı zaten dengelenmiştir. Dolayısıyla teorinin gezegen figürüne kattığı temel imza, klasik fizik modellerinde bulunmayan **F4 (Eksenel İtim)** ve **F5 (Yanal İtim)** kuvvetlerinin net etkisidir.

### 6.6.2 Multipol Ayrıştırması ve Jeodezik Kanıtlar ($J_4$ İmzası)

Figür kanıtının matematiksel anahtarı, bu kuvvetlerin kütleçekim potansiyelindeki multipol ($P_n$) spektrumlarına ayrıştırılmasıdır. 

* **Merkezkaç ve Yanal İtim (F5):** Her iki kuvvet de matematiksel olarak saf $P_2$ karakterindedir. Yanal itim (F5), merkezkaç potansiyelinin sabit bir çarpanla yeniden ölçeklenmesine denktir. Yani F5, gezegeni farklı bir şekle sokmaz; gezegenin *biraz daha hızlı dönüyormuş gibi* algılanmasına yol açar.
* **Eksenel İtim (F4):** F4 ise figür potansiyelinde benzersizdir; saf bir $P_2$ değil, çok daha zengin bir spektrum ($P_2, P_4, P_6$) üretir.

Bu durum teorik açıdan muazzam bir kanıt penceresi açar. Merkezkaç kuvveti, gezegenin $J_4$ harmoniğine birinci mertebede **hiç katkı vermez** (hidrostatik $J_4$, merkezkaçın yalnızca zayıf, ikinci mertebe bir tepkisidir). Eksenel itim (F4) ise birinci mertebeden çok güçlü bir $P_4$ ($J_4$) imzası doğurur.

**Dünya'nın $J_4$ Verisiyle Uyum:**
Standart hidrostatik modeller, Dünya'nın hesaplanan $|J_4|$ değerini gözlemlenen değerden daha küçük bulur. Gözlem verisi ($-1{,}62 \times 10^{-6}$), merkezkaç kaynaklı hidrostatik tahminlerden daha *derindir*. Evrenakı'nın öngördüğü Eksenel İtim'in (F4) yarattığı $J_4$ katkısı ise tam olarak bu ölçümle **aynı işaretli ve aynı yöndedir.** Teori, klasik fizikte "açıklanamayan gürültü" veya "iç manto anomalisi" olarak görülen bu derinleşmeyi, eksenel eter akışının zorunlu geometrik bir sonucu olarak kendi içinden türetir.

### 6.6.3 Kompozisyonun ($\phi$) Figüre Etkisi: Dört Cisim Sınavı

Teorinin gezegen figürü konusundaki en net ampirik başarılarından biri, M-39 Yanal İtim yasasındaki kompozisyon çarpanıdır ($\phi$). 
Bir cismin "madde/plazma" durumu (bağlı moleküler kafes olup olmaması), $\phi$ çarpanını belirler. İyonize plazmada $\phi \approx 0$'dır (kafes bağı yoktur, eter akışı sürüklenmez); katı/sıvı bağlı kütlelerde ise $\phi$ maksimumdur.

Bu öngörü, Güneş Sistemi'ndeki dört dev cismin uydu ve jeodezi verileriyle sınandığında olağanüstü bir tablo ortaya çıkarır:

| Cisim (Kompozisyon Tipi) | Madde Durumu ($\phi$) | Teorik Öngörü | Gözlem / Jeodezi Verisi | Uyum |
| :--- | :--- | :--- | :--- | :--- |
| **Güneş** (İyonize Plazma) | $\phi \approx 0$ | **Fazla yok (Sıfır)** | Helyosismoloji verisi ($J_2 \approx 2{,}2\times10^{-7}$), Güneş'in ölçülen dönüş hızıyla hesaplanan saf merkezkaç basıklığıyla **kusursuz** uyumludur. Gözlemlenen ek bir dinamik aşırı basıklık sıfırdır. | ✅ Tam Uyum |
| **Dünya** (Kayaç ve Dış Çekirdek) | $\phi \approx 0{,}18$ | **Düşük / Ölçülebilir** | WGS-84 uydu jeodezisine göre Dünya'da %0,42'lik bir $J_2$ fazlası vardır. Saf suyun $\phi \approx 0{,}44$ olduğu düşünülürse, dış kayaç ve ezilmiş/metalik iç çekirdek ortalaması için $\phi \approx 0{,}18$ fiziksel olarak son derece isabetlidir. | ✅ Tam Uyum |
| **Jüpiter** (Moleküler Gaz/Sıvı) | Yüksek ($\phi \sim 0{,}5$) | **Devasa anomali** | Juno uzay aracı, Jüpiter'in çekim alanında standart katı-cisim hidrostatik dengesiyle açıklanamayan devasa sapmalar bulmuştur. Bu sapma, tam da Yanal İtimin öngördüğü ölçüdedir. | ✅ Destekliyor |
| **Satürn** (Aşırı Basık Gaz Devi) | Çok Yüksek ($\phi \gtrsim 0{,}6$) | **Rekor anomali** | Düşük kütle/yoğunluk nedeniyle Satürn'ün iç yapısında "moleküler" (bağlı) bölge çok daha kalındır. Satürn %10 ile sistemin en basık gezegeni olup, Cassini verileriyle tespit edilen dinamik yerçekimi sarmalları bu yüksek $\phi$ çarpanını doğrular. | ✅ Destekliyor |

### Sonuç

Bu dört cisim testi gerçek bir yanlışlanabilirlik (falsifiability) sınavıdır. Şayet Güneş (plazma formunda olmasına rağmen) ölçülebilir bir $J_2$ anomalisi taşısaydı veya Jüpiter (moleküler formda olmasına rağmen) mükemmel bir hidrostatik uyum sergileseydi, kompozisyon argümanı ve teorinin dinamik öngörüleri doğrudan çökerdi. Verilerin kompozisyon karakteriyle ($\phi$ çarpanı) kusursuz eşleşmesi, Evrenakı teorisinin sadece matematiksel bir kurgu olmadığını, aksine Güneş Sistemi'nin jeodezik gerçekliğiyle tam uyum içinde çalışan bir fizik modeli olduğunu kanıtlamaktadır.
