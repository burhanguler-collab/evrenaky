# 5.3 Kütle İçi Evrenakı Gradyanları

Bir önceki bölümde kütlelerin dış uzaydaki Evrenakı basıncını nasıl değiştirdiğini ölçmüştük. Bu bölümde ise bizzat **katı bir kütlenin kendi içyapısındaki** (merkezi ile kenarları arasındaki) Evrenakı basınç farklılaşmasını inceleyeceğiz.

> **Kanıt durumu notu:** Bu bölümde aktarılan sayısal değerler, yazarın rapor ettiği ilk ölçüm bulgularıdır; ham veri setleri ve hata analizleri manüskriptin ilerleyen sürümlerinde yayımlanacaktır. Bulgular, bağımsız tekrar öncesinde "rapor edilen sonuç" statüsündedir. Önceki iki bölümün aksine bu bölümde yalnızca Michelson interferometresi kullanılmıştır: ring osilatör ve attometer tekniklerinin katı bir numunenin *içine* uygulanması ayrı düzenek tasarımları gerektirdiğinden, bu çapraz doğrulamalar sonraki sürüme bırakılmıştır.

## Deney 1: Michelson İnterferometresi ile Kütle İçi Evrenakı Gradyanının Ölçümü

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/michelson_internal_gradient_dark.png" alt="Kütle İçi Gradyan Deneyi Karanlık Mod" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.8a: Kütle İçi Evrenakı Gradyanı Deney Düzeneği. Michelson interferometresi kolundaki 50x50x50 mm'lik cam küpün içi, merkezden kenarlara doğru ışık demetiyle taranarak içsel hız değişimleri ölçülür.</em></p>
</div>

Bu deney, bir önceki bölümde (5.2) kütle *dışı* gradyanı ölçen Michelson düzeneğinin doğrudan bir uzantısıdır; bu kez ölçülen etki kütlenin kendi *içindedir*. Bir ışık kolu referans olarak boş bırakılır, diğer kol ise cam kare prizmanın içinden geçirilerek camın içinde oluşan Evrenakı yoğunluğu değişiminin ışık hızına yansıması gözlenir (Şekil 5.8b).

### 5.3.1 Deneyin Amacı
Klasik optik kuralları, cam gibi homojen saydam bir cismin içerisinde ışık hızının her noktada aynı (sabit) olduğunu öngörür. Bu deneyin amacı, bu klasik kabulü yıkarak; homojen bir kütlenin (cam prizmanın) kendi içindeki Evrenakı yoğunluğunun her yerde aynı olmadığını ve buna bağlı olarak ışık hızının kütlenin merkezinde farklı, kenarlarında farklı olduğunu ispatlamaktır.

### 5.3.2 Teorik Altyapı ve Hipotez
Evrenakı kuramına göre, katı cisimler bir araya gelirken etraflarındaki Evrenakı'yı dışarı iterek kendi içlerinde düşük basınçlı bir alan yaratırlar. Bu itilim homojen değildir; cismin tam merkezinde Evrenakı yoğunluğu en düşük seviyedeyken, merkezden dış yüzeylere (kenarlara) doğru gidildikçe Evrenakı yoğunluğu artar. Hipotezimize göre: Işığın hızı Evrenakı yoğunluğu ile doğru orantılı olduğuna göre, bir ışık demeti cam bir prizmanın tam merkezinden geçerken hızı daha düşük, kenarlarına yakın yerlerden geçerken ise hızı daha yüksek olmalıdır.

### 5.3.3 Deney Düzeneği ve Ekipmanlar
Deney, standart Michelson interferometresi (Michelson & Morley, 1887) ile 650 nm dalga boyunda ışık kaynağı (lazer) kullanılarak tasarlanmıştır. İnterferometrenin referans kolu boş bırakılırken, diğer ışık kolunun güzergahına **50x50x50 mm ebatlarında kare cam prizma (küp)** yerleştirilmiştir (Şekil 5.8b, 5.8c). Bu cam küp, çok hassas bir step motor mekanizması üzerine oturtulmuştur. Step motor, cam küpü ışık demetine dik (yanal) eksende yavaşça hareket ettirebilecek şekilde dizayn edilmiştir.

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/michelson_prizma_sema.png" alt="Michelson interferometresi ve cam kare prizma bileşen şeması" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.8b: Düzeneğin bileşenleri. Işık kaynağı ve ışın ayırıcıdan sonra bir kol yansıtıcı A'ya (referans), diğer kol step motora bağlı cam kare prizmadan geçerek yansıtıcı B'ye gider; prizma, ışık demetine dik eksende taranır.</em></p>
</div>

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/cam_prizma_foto.png" alt="Deneyde kullanılan gerçek cam küp" style="max-width: 60%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.8c: Deneyde kullanılan 50×50×50 mm'lik gerçek cam kare prizma (küp). Ok, ışık demetinin küpü taradığı ekseni gösterir.</em></p>
</div>

### 5.3.4 Yöntem ve Uygulama
Deneyin işleyişi "kütle içi tarama" prensibine dayanır. Işık demeti sabit tutulurken, step motor yardımıyla cam küp yavaşça kaydırılır. Böylece sabit ışık demeti, cam küpün önce tam merkezinden, sonra yavaş yavaş kenarlarına doğru kayarak camın içini bir uçtan diğer uca "tarar". Işık demeti cam küpün merkezinden kenarlarına doğru ilerlerken, girişim desenleri yüksek çözünürlüklü kameralarla bilgisayara aktarılır ve piksel bazlı saçak (parmak) kaymaları analiz edilir. Işık demeti camın kenarlarına 2 mm kalana kadar yaklaştırılmış, ancak camın dışına çıkarılmamıştır.

### 5.3.5 Gözlem ve Bulgular
Eğer klasik fiziğin öngördüğü gibi ışık hızı camın her yerinde aynı olsaydı, cam küp hareket ettirildiğinde (ışık hep aynı 50 mm'lik cam kalınlığından geçtiği için) ekranda hiçbir girişim kayması olmamalıydı. Ancak bilgisayar destekli analizler, ışık demeti cam küpün bir kenarından diğerine doğru kaydırıldıkça girişim deseninde belirgin ve düzenli bir kayma olduğunu göstermiştir. Kayma, kenarlarda en düşük, merkeze doğru gidildikçe artarak en yüksek değerine ulaşmış ve karşı kenara doğru yeniden azalmıştır; bu simetrik profil, camın merkezi ile kenarları arasında tam **1,8 parmak (saçak)** genişliğinde bir farka karşılık gelir (Şekil 5.8d).

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/graf_prizma_kayma.png" alt="Prizma taraması saçak kayması grafiği" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.8d: Işık demeti cam prizmayı bir kenardan diğerine taradıkça ölçülen saçak kayması. Kaymanın merkeze doğru ~1,8 saçağa yükselip her iki kenarda sıfıra dönmesi, camın içindeki merkez-simetrik Evrenakı gradyanını doğrudan ortaya koyar.</em></p>
</div>

Tarama yapılan yüzeyden bakıldığında camın içindeki yaklaşık Evrenakı yoğunluğu dağılımı Şekil 5.8e'deki gibidir: camın dış kenarlarına doğru Evrenakı yoğunluğu artarken merkeze doğru azalır. Işık hızı Evrenakı yoğunluğuyla arttığından, ışık kenarlara yakın bölgelerde hızlanır, merkezde yavaşlar — grafiğin kemer biçimi tam da bu dağılımın izdüşümüdür.

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/cam_prizma_yogunluk_haritasi.png" alt="Cam prizma içindeki Evrenakı yoğunluğu haritası" style="max-width: 55%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.8e: Cam küpün kesitindeki yaklaşık Evrenakı yoğunluğu dağılımı ve taranan eksen. Merkez (açık bölge) en düşük yoğunluğu, köşe/kenarlara doğru koyulaşan bölgeler artan yoğunluğu temsil eder.</em></p>
</div>

### 5.3.6 Sonuç ve Değerlendirme
Gözlemlenen 1,8 saçaklık girişim kayması, günümüz kabullerine (dalga optiği) göre hesaplandığında, ışık hızının cam küpün merkezi ile kenarları arasında yaklaşık **4650 m/sn'lik (saniyede 4,65 km) bir hız farkına** sahip olduğuna işaret eder. Bu hesap dalga optiği kurallarıyla yapılmıştır; ancak bu bir ilkesel benimseme değil, teknik bir zorunluluktur: Evrenakı kuramı ışığın dalga yorumunu esas almaz (ışık, dönen katı zerrelerin akışıdır), fakat dalga optiğinin yerine geçebilecek bir hesap yöntemi henüz geliştirilmediğinden, kayma miktarı zorunlu olarak dalga optiği üzerinden sayısallaştırılmıştır.

Bu devasa fark; ışığın camın merkezinden geçerken daha yavaş, kenarlarına yakın bölgelerden geçerken ise ~4650 m/sn daha hızlı seyahat ettiğini gösterir. Sonuç, katı cisimlerin kendi içlerinde homojen bir Evrenakı dağılımına sahip olmadığını, merkezden dışa doğru artan bir Evrenakı gradyanı barındırdığı hipotezini güçlü biçimde destekler ve kütle *dışı* gradyan bulgularını (5.2) kütlenin *içine* taşıyarak tamamlar.

## 5.3.7 Tasarım Aşamasındaki Kurgular: DENEY 2 ve DENEY 8 (Ortam-İçi Asimetri)

*İsimlendirme Notu: Bu çalışmada önerilen tüm kavramsal deney kurguları, kıymetli aile bireylerine (Yusuf, Şeyma Nur, Enes, Merve) ithafen isimlendirilmiş olup, kuramsal fiziğin o soğuk soyut teorileri ile insani ve sıcak bağları sentezlemeyi amaçlamaktadır.*

Özellikle **DENEY 8 ve DENEY 2** kapsamında laboratuvar ortamında yürütülmesi planlanan ön optik/mekanik çalışmalarda; hareketli yoğun ortamların, ışığın optik kırılma indisleri ve girişim (interferometrik) ölçümleri üzerindeki etkileri test edilmektedir.

**Ortam İçi Asimetri (DENEY 2):** Bu deneyde, optik bir materyalin (örneğin hızla döndürülen devasa bir cam silindirin veya akan bir sıvının) içerisine gönderilen ışığın (Zerre'nin) hız profilindeki değişimler ölçülür. Evrenakı'nın akışkan direnci ve Zerre'nin translasyonel-rotasyonel (çizgisel hızdan spine) enerji aktarımı mekanizması, materyal içi hız profilinde merkeze göre kusursuz bir **asimetrik dağılım** öngörür. Eğer laboratuvar ölçümlerinde bu hız profili asimetrik değil de simetrik çıkarsa (veya ışık hızı maddenin dönüş hızından beklenen hidrodinamik tepkiyi almazsa), enerji aktarım (Zerre) mekanizması çürütülmüş sayılacaktır. Bu kurgu şu an tasarım aşamasındadır; kesin protokol, beklenen etki büyüklüğü ve ölçüm belirsizliği, deney düzeneği kurulduğunda ayrıca raporlanacaktır. Model, klasik akışkanlar mekaniğinin Fizeau (1851) sürüklenme deneyiyle tarihsel olarak uyumlu bir asimetri beklentisi taşır; ancak Evrenakı'ya özgü sapmanın ölçülüp ölçülemeyeceği henüz açık bir sorudur.

Evrenakı, sadece gökyüzündeki galaksilerin değil, laboratuvar masasındaki lazer ışınlarının da bizzat içinde yüzdüğü rasyonel, mekanik bir fiziksel okyanustur. Test edilebilir ayrım, işte o masanın üzerinde aranmaktadır.
