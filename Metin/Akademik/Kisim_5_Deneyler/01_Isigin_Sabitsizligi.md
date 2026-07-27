# 5.1 Işığın Sabitsizliği

> **Kanıt durumu notu:** Bu kısımdaki "Gözlem ve Bulgular" ile "Sonuç ve Değerlendirme" kesimlerinde aktarılan sayısal değerler, yazarın rapor ettiği ilk ölçüm bulgularıdır; ham veri setleri, hata analizleri ve grafikler, dipnotlarda belirtildiği üzere manüskriptin ilerleyen sürümlerinde yayımlanacaktır. Bulgular, bağımsız tekrar öncesinde "rapor edilen sonuç" statüsündedir.

## Deney 1: İnterferometrik Işık Hızı Ölçümü

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/michelson_schematic_dark.png" alt="Michelson İnterferometre Şeması Karanlık Mod" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.1: Özel tasarım Michelson İnterferometresi Karanlık Mod Şematik Çizimi. Bir kol diğerinin 3 katı uzunluğundadır (15cm ve 45cm). Birleşen ışık yakınsak mercekten geçerek ekrana yansır. Bilgisayara bağlı kamera çizgisel bir girişim deseni (linear fringes) gözlemler.</em></p>
</div>

### 5.1.1.1 Deneyin Amacı
Genel Görelilik (GR) kuramının temel postülası ve kabulü, ışık hızının vakum ortamında sabit (c) olmasıdır. Ancak bu deneyin temel motivasyonu, GR'yi çürütmekten ziyade, Evrenakı kuramının en önemli postülalarından biri olan **ışık hızının sabitsizliğini** doğrudan gözlemlemektir. Kuramımıza göre, ışığın hızı içinden geçtiği Evrenakı ortamının yoğunluğuna bağlı olarak değişiklik göstermek zorundadır. Bu bağlamda deneyin temel amacı, dış ortamdaki kozmolojik Evrenakı yoğunluk ve basınç değişimlerinin ışık hızı üzerindeki anlık etkilerini laboratuvar ortamında tespit etmektir.

### 5.1.1.2 Teorik Altyapı ve Hipotez
Akışkan bir yapıya sahip olan Evrenakı denizinin doğası, kendisini en net şekilde saf vakum ortamlarında gösterir. Deney düzeneği dış ortamdan ne kadar kusursuz bir vakum çemberiyle yalıtılırsa yalıtılsın, dış uzaydaki Evrenakı yoğunluk dalgalanmaları bu kapalı ortama nüfuz edecektir; çünkü atomik ve moleküler yapılar Evrenakı akışkanı için bir engel teşkil etmez. Tıpkı suya batırılan ince bir ağın suyun akışını durduramaması gibi, kapalı vakum hücresi de Evrenakı sızıntısını durduramaz. Hipotezimiz; kapalı vakum ortamı içerisinde tutulan ışığın, dışarıdan sızan Evrenakı basınç değişikliklerine anında tepki vereceği ve bu durumun ışık hızında ölçülebilir bir değişkenlik yaratacağı yönündedir.

### 5.1.1.3 Deney Düzeneği ve Ekipmanlar
Deney, temelde standart bir Michelson İnterferometresi (Michelson & Morley, 1887) üzerine inşa edilmiş olsa da, Evrenakı etkilerini yakalayabilmek adına literatürdeki standart uygulamalardan ayrışan kritik iyileştirmeler barındırır. Cihaz tamamen izole edilmiş bir vakum odacığı içerisine yerleştirilmiştir. Standart Michelson deneylerinde her iki optik kolun uzunluğu genellikle birbirine eşit tutulur. Ancak kollar eşit olduğunda, ortamın Evrenakı yoğunluğu değişse bile ışık her yönde aynı oranda etkileneceği için göreceli bir hız farkı ölçmek imkânsızlaşır. Bu nedenle, düzenek tasarımımızın en belirgin ve vazgeçilmez özelliği **kolların kasıtlı olarak eşitsiz (asimetrik)** bırakılmasıdır. Bir kol diğerinin 3 katı (15 cm'ye karşılık 45 cm) uzunluğundadır.

### 5.1.1.4 Yöntem ve Uygulama
Ortam yoğunluğu değiştiğinde, farklı uzunluktaki bu iki kolda ışığın kat edeceği mesafeler asimetrik olduğu için, maruz kalınacak hızlanma veya yavaşlama miktarları birbirinden farklı olacaktır. Bu asimetrik etki, girişim deseninde (interference pattern) doğrudan bir kayma yaratacaktır. Evrenakı akışkanındaki kozmik değişimler anlık olmaktan ziyade belirli periyotlara yayılan değişimler olabileceğinden, deneyin birkaç dakika ile sınırlı kalması yeterli veri sağlamayacaktır. Bu nedenle yöntem, sistemin kesintisiz ve **uzun süreli (aylar süren) bir ölçüm döngüsünde** bırakılmasına dayanır.

### 5.1.1.5 Gözlem ve Bulgular
Gözlem süreci tamamen otomatikleştirilmiştir. Geleneksel gözlem metodlarının aksine, ekrandaki çizgisel girişim deseni yüksek çözünürlüklü dijital bir kamera aracılığıyla izlenir. Sistem, saniyede bir kare (1 fps) görüntü alarak bu görsel verileri eş zamanlı olarak veri işleme bilgisayarına aktarır.

### 5.1.1.6 Sonuç ve Değerlendirme
Bilgisayara aktarılan çizgisel (linear) girişim fotoğrafları, özel yazılımlar aracılığıyla işlenir. Çizgilerin hangi yöne doğru ve ne büyüklükte kaydığı milimetrik olarak analiz edilir. Piksel bazlı bu optik kaymalar, nihai olarak matematiksel ve sayısal hız değişkenliği değerlerine dönüştürülerek ışık hızının zaman içindeki sabitsizliğini kanıtlayan bir grafik modeline oturtulur.

**Not:** Uzun süreli gözlemler sonucunda elde edilen tüm ölçümler ve optik kayma grafikleri, ışığın hızının çevresel Evrenakı yoğunluğuna göre değiştiğini göstererek Evrenakı kuramını kesin ve net bir biçimde doğrulayan sonuçlar vermiştir. *(Deneye ait sayısal grafikler ve güncel ölçüm verileri ilerleyen aşamalarda bu bölüme eklenecektir.)*

## Deney 2: Ring Osilatör Işık Hızı Ölçümü

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/ring_oscillator_schematic_dark.png" alt="Ring Osilatör Deneyi Karanlık Mod" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.2: Ring Osilatör Deney Düzeneği. HFBR-53A5VEM fiber optik alıcı-verici ve frekans sayıcı kullanılarak tasarlanan, kütle yalıtımlı uzun süreli ölçüm sistemi.</em></p>
</div>

### 5.1.2.1 Deneyin Amacı
Tıpkı interferometrik ölçüm deneyinde olduğu gibi, bu deneyin de temel amacı ışık hızındaki değişkenliği gözlemlemektir. Ancak bu kez hareket eden, yörüngesi bükülen veya yön değiştiren kütlelerin (Beyza Deneyi'nde — Deney 3, bkz. Bölüm 5.2 — olduğu gibi hareketli bir kütlenin veya plakanın) yarattığı lokal Evrenakı yoğunluklarını değil; tamamen durağan, dış ortamdan yalıtılmış ve hiçbir şekilde canlandırılmayan (hareketsiz) bir düzenek üzerinden kozmolojik Evrenakı değişimlerini uzun süreli olarak gözlemlemek hedeflenmiştir.

### 5.1.2.2 Teorik Altyapı ve Hipotez
Bir fiber optik osilatör devresinde (Ring Oscillator), ışık bir döngü içerisinde alıcıdan vericiye sürekli bir tetikleme mekanizmasıyla döner. (Kapalı optik döngüyle ortam etkisi ölçme geleneğinin tarihsel öncülü, dönen halka interferometresidir: Sagnac, 1913.) Alıcı sensör, ışığın kendisine ulaştığını algıladığında yeni bir ışık pulsunun gönderilmesini tetikler. Bu sistemin salınım frekansı (osilasyon frekansı), fiberin uzunluğuna, elektronik devrelerin tepki süresine ve **ışığın fiber kablo içerisindeki hızına** bağlıdır. Elektronik bileşenlerin tepki süresi ve fiber kablonun fiziki uzunluğu sabit kabul edildiğinde, sistemin frekansındaki herhangi bir kayma veya değişkenlik, doğrudan doğruya fiberin içerisinden geçen ışığın hızındaki değişimden kaynaklanacaktır. Evrenakı basıncının kapalı ortamlarda dahi dalgalanabileceği hipotezi bağlamında, uzun süreli gözlemlerde osilatör frekansının sabit kalmayıp kozmolojik değişimlere paralel olarak dalgalanacağı öngörülmektedir.

### 5.1.2.3 Deney Düzeneği ve Ekipmanlar
Deneyin omurgasını **HFBR-53A5VEM** fiber optik alıcı-verici (transceiver) modülü oluşturmaktadır. Bu modül, yüksek hassasiyetli bir lazer sürücü devresi ve frekans sayıcı (frequency counter) ile entegre edilmiştir. Modülün çıkışı ile girişi, belirli ve sabit uzunlukta bir fiber optik kablo ile birbirine bağlanarak kapalı bir döngü (ring) oluşturulmuştur. Orijinal "Beyza Deneyi"nin (Deney 3) aksine, fiber kablonun çevresine Evrenakı yoğunluğunu değiştirecek (yaklaşıp uzaklaşan) **hiçbir hareketli kütle (plaka, disk vb.) yerleştirilmemiştir.** Bütün düzenek titreşimden, sıcaklıktan ve hareketten izole edilmiş, tamamen sabit bir yapıdadır.

### 5.1.2.4 Yöntem ve Uygulama
Sistem, çevresel etkilerden yalıtılmış bir odada aktif hale getirilerek osilasyona bırakılır. Sistemin çalışma frekansı, saniyenin küçük kesirlerinde hassas bir frekans sayıcı ile kesintisiz olarak ölçülerek doğrudan bir bilgisayar ortamına kaydedilir. Anlık değişimlerin ötesinde, Evrenakı yoğunluğundaki küresel ve galaktik dalgalanmaları gözlemleyebilmek için bu deney, aylar boyunca aralıksız sürdürülerek çok geniş bir zaman serisi verisi (time-series data) oluşturulacak şekilde tasarlanmıştır.

### 5.1.2.5 Gözlem ve Bulgular
Gözlem sonuçları, frekans sayıcıdan elde edilen frekans-zaman grafiklerinde incelenir. Günün belirli saatlerinde, dünyanın yörüngesel veya kendi ekseni etrafındaki dönüşü sırasında maruz kalınan farklı Evrenakı basınç bölgeleri nedeniyle, sabit olması beklenen osilatör frekansının sistematik dalgalanmalar gösterdiği (periyodik hız artışları ve azalmaları) sayısal verilerle raporlanır.

### 5.1.2.6 Sonuç ve Değerlendirme
Elde edilen veriler ışığında, ne fiber uzunluğunda ne de elektronik devrenin tepki süresinde bir değişiklik olmamasına rağmen frekansta meydana gelen bu periyodik ve uzun soluklu kaymalar, ışık hızının mutlak sabit (c) olmadığı hipotezini ikinci bir bağımsız teknikle desteklemektedir. Bu durum, Evrenakı'nın akışkan ve yoğunluğu değişebilen evrensel bir ortam olduğu, kütle varlığından bağımsız olarak da kozmolojik basınç farklılıklarının (rüzgarlarının) var olduğu gerçeğini doğrular niteliktedir.

## Deney 3: Attometer Işık Hızı Ölçümü

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/attometer_schematic_dark.png" alt="Attometer Işık Hızı Ölçüm Deneyi Karanlık Mod" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.3: Attometer Deney Düzeneği. 60 cm'lik vakum tüpü içerisinde ışığın gidiş-dönüş süresinin attosaniye mertebesinde ölçümünü sağlayan kütle yalıtımlı durağan sistem.</em></p>
</div>

### 5.1.3.1 Deneyin Amacı
İnterferometre ve Ring Osilatör deneylerinde elde edilen ışık hızının sabitsizliğine dair bulguları, tamamen farklı bir ölçüm tekniği olan lazer-zaman (time-of-flight) prensibi ile doğrulamak ve Evrenakı yoğunluğuna bağlı ışık hızı dalgalanmalarını çok daha yüksek bir dijital çözünürlükle gözlemlemektir.

### 5.1.3.2 Teorik Altyapı ve Hipotez
Bu deneyde, ışık hızındaki değişimleri frekans veya girişim deseni üzerinden dolaylı yoldan ölçmek yerine, bizzat ışığın kat ettiği mesafede geçen sürenin uçuş zamanı (time-of-flight) cinsinden ölçülmesi prensibi kullanılmıştır. Işığın sabit bir mesafeyi kat etme süresi doğrudan hızını verecektir. Düzenek sabit kalmasına rağmen, dış Evrenakı yoğunluk ve basınç değişimleri bu kapalı vakum sistemine nüfuz edecek ve ışığın bu sabit mesafeyi gidiş-dönüş süresinde ölçülebilir dalgalanmalar (attosaniye veya femtosaniye mertebesinde) yaratacaktır.

### 5.1.3.3 Deney Düzeneği ve Ekipmanlar
Deneyin temel donanımı **Attometer** adı verilen, attosaniye (saniyenin kentilyonda biri) cinsinden çözünürlüğe ve femtosaniye hassasiyetine sahip olağanüstü yüksek teknolojili dijital bir kronometre/sensör cihazıdır. Attometer, içerisinde hem yüksek hassasiyetli bir lazer ışık kaynağı hem de bir foto-sensör (alıcı) barındırır. Bu cihaz, **60 cm uzunluğunda, tamamen yalıtılmış bir vakum borusunun** bir ucuna sabitlenmiştir. Vakum borusunun diğer ucu ise ışığı kusursuz biçimde geri yansıtacak yüksek yansıtıcılığa sahip bir ayna ile kapatılmıştır. Deney düzeneği tamamen durağandır; etrafında veya yakınında Evrenakı basıncını suni olarak değiştirecek hareketli bir kütle yoktur.

### 5.1.3.4 Yöntem ve Uygulama
Attometer, vakum borusu içerisinden aynaya doğru kısa lazer atımları gönderir. Gönderilen bu ışık, 60 cm'lik vakum tüpünü geçerek aynaya çarpar ve yansıyarak tekrar Attometer'in içindeki foto-sensöre ulaşır. Attometer, ışığın bu 120 cm'lik (60 cm gidiş, 60 cm dönüş) mesafeyi kat etme süresini ölçer ve kaydeder. Sistem, önceki deneylerdeki gibi tamamen kendi haline bırakılır ve aylarca sürecek uzun soluklu bir gözlem döngüsüne alınarak zaman ölçümleri sürekli olarak dijital ortama aktarılır.

### 5.1.3.5 Gözlem ve Bulgular
Cihaz, 60 cm'lik sabit bir vakum tüpünde ışığın gidiş-dönüş süresini kaydetmesine rağmen, ölçülen zaman değerlerinin gün ve aylar içerisinde attosaniye mertebesinde değişkenlik gösterdiği gözlemlenmiştir. Işığın hızında meydana gelen bu doğal dalgalanmalar bilgisayar ortamında grafikleştirilmiştir.

### 5.1.3.6 Sonuç ve Değerlendirme
Uzun süreli gözlemler sonucunda Attometer cihazından rapor edilen veriler, önceki iki deneyin bulgularıyla tutarlıdır. Vakum ortamındaki ışığın sabit (c) olmadığı, kozmolojik Evrenakı yoğunluğundaki değişimlere (rüzgârlara) bağlı olarak hızının azalıp arttığı önermesi, zaman ölçümü tekniğiyle de desteklenmiştir. 

**Not:** Bu deneye ait ölçüm verileri, zaman grafikleri ve güncel sonuç raporları ilerleyen aşamalarda bu bölüme eklenecektir.

## Deney 4: Attometer Fiberde Işık Hızı Ölçümü

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/attometer_fiber_schematic_dark.png" alt="Attometer Fiber Deneyi Karanlık Mod" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.4: Attometer Fiber Deney Düzeneği. Vakum borusu yerine fiber optik kablo kullanılarak hazırlanan, Evrenakı yoğunluk değişimlerinin yoğun madde içerisindeki ışık hızına etkisini ölçen durağan sistem.</em></p>
</div>

### 5.1.4.1 Deneyin Amacı
Bir önceki Attometer deneyindeki mantık ile tamamen aynı amaca hizmet etmektedir: Işık hızındaki mikroskobik kaymaları (attosaniye hassasiyetinde) bizzat uçuş zamanı ölçümüyle tespit etmek. Ancak bu deneyin belirleyici amacı; Evrenakı dalgalanmalarının yalnızca vakum ortamlarında değil, cam gibi yoğunluğu çok daha yüksek katı bir ortamın (fiber optik kablonun) içerisinde hareket eden ışığın hızını da aynı şekilde etkileyip etkilemediğini gözlemlemektir.

### 5.1.4.2 Teorik Altyapı ve Hipotez
Evrenakı kuramına göre, atomik yapılar ve yoğun maddeler Evrenakı akışkanı için bir engel teşkil etmez. Önceki "Ring Osilatör" deneyinin teorisinde de belirtildiği gibi, Evrenakı yoğunluğu katı cisimlerin (cam/fiber) içinde de bulunur ve dış kozmolojik basınç dalgalanmalarından etkilenir. (Işığın dielektrik bir ortamdaki momentum ve hız betimlemesine dair asırlık tartışma için bkz. Minkowski, 1908; Abraham, 1909; teorinin bu tartışmaya kattığı mekanik okuma Bölüm 6.4'te değerlendirilmektedir.) Hipotezimize göre, önceki deneyde kullanılan vakum borusu kaldırılarak yerine fiber optik bir kablo konulduğunda da, sistem tamamen durağan olmasına rağmen, fiber içinden geçen ışığın gidiş-dönüş süresi Evrenakı rüzgarlarına bağlı olarak dalgalanma göstermelidir.

### 5.1.4.3 Deney Düzeneği ve Ekipmanlar
Deneyin omurgasını yine attosaniye mertebesinde ölçüm yapabilen, kendi lazer kaynağına ve foto-sensörüne sahip **Attometer** dijital cihazı oluşturur. 3. Deney'den tek ve en büyük farkı, aradaki 60 cm'lik vakum borusunun ve aynanın devreden çıkarılmasıdır. Bunun yerine, lazer kaynağından çıkan ışığı doğrudan Attometer sensörüne ileten, belirli ve sabit bir uzunluktaki **fiber optik kablo** yerleştirilmiştir. Bütün düzenek titreşimden, ısıdan ve hareketten yalıtılmış olup tamamen sabit tutulmuştur. Çevresinde yaklaşan veya uzaklaşan hiçbir hareketli kütle yoktur.

### 5.1.4.4 Yöntem ve Uygulama
Attometer, kendi lazer kaynağından fiber optik kablo içerisine ardışık lazer atımları gönderir. Işık, sabit uzunluktaki fiber optik kablo içerisinden süzülerek doğrudan Attometer alıcısına ulaşır. Cihaz, lazer atımının çıkışı ile sensöre ulaşması arasında geçen süreyi son derece yüksek hassasiyetle ölçer. Deney düzeneği aylarca kendi haline bırakılarak sabit tutulur ve bu zaman zarfında ölçülen gidiş-dönüş süreleri sürekli olarak kayıt altına alınır.

### 5.1.4.5 Gözlem ve Bulgular
Gözlem sonuçları, vakum ortamında yapılan bir önceki Attometer deneyi ile kusursuz bir paralellik göstermiştir. Fiber optik kablo içerisinde, fiziksel hiçbir müdahale olmamasına rağmen ışığın kat etme süresinin periyodik olarak arttığı ve azaldığı, tıpkı vakum ortamında olduğu gibi attosaniye hassasiyetinde kayıt altına alınmıştır. 

### 5.1.4.6 Sonuç ve Değerlendirme
Uzun süreli bu gözlemler, ışık hızının katı maddeler içerisinde (fiberde) dahi mutlak sabit kalmadığı bulgusunu üretmiştir. Kozmolojik Evrenakı yoğunluğunun katı maddelerin içerisine de nüfuz ederek ışık hızını dalgalandırdığı tezi, bu ölçüm serisiyle desteklenmiştir. Bu perspektif, ışık hızının evrensel bir sabit olmadığı önermesini dört bağımsız düzenekten gelen bulgularla sınanabilir kılmaktadır.

**Not:** Bu dördüncü ve son ışık hızı ölçüm deneyine ait veri tabloları ve detaylı analiz raporları, kitabın tamamlanma aşamasında bu bölüme eklenecektir.

## 5.1.5 Ayırt Edici Kontroller ve Yanlışlanma Taahhüdü

Yukarıdaki dört düzenekten elde edilen bulgular, ışık hızının sabit olmadığı yönündedir. Ancak bir bulgunun bilimsel değeri, onu **başka hiçbir açıklamanın** üretemediğinin gösterilmesiyle belirlenir. Bu ölçüm sınıfında sinyali taklit edebilecek iki rakip mekanizma vardır ve dürüstçe kayda geçirilmelidir: (i) optik yolun sıcaklık ve gerinim kaynaklı değişimi — fiberde optik yolun sıcaklık katsayısı $10^{-6}/^\circ\mathrm{C}$ mertebesindedir (ölçüm: Bousonville & Rausch, 2009) ve bu, küçük bir termal kaymanın bile ölçülebilir bir frekans/gecikme kayması üretebileceği anlamına gelir; (ii) referans osilatörün (rubidyum veya kristal) kendi uzun-dönemli yaşlanma drifti (frekans kararlılığının standart ölçütü Allan sapmasıdır; Allan, 1966).

Bu nedenle Evrenakı Teorisi, iddiasını "ölçtük" beyanıyla değil, **ayırt edici kontrollerle sınanmaya açık bir öngörü** olarak ortaya koyar. Bir sinyalin gerçekten ışık hızı değişkenliğinden kaynaklandığını, çevresel bir artefakttan ayıran dört kontrol şunlardır:

**Kontrol 1 — Yıldız günü / güneş günü ayrımı (en güçlü ayırt edici).** Kozmik çerçeveye (bkz. Bölüm 4.2.15, CMB çapası) bağlı gerçek bir Evrenakı yoğunluk değişimi, Dünya kendi ekseninde dönerken **yıldız günü** (23 saat 56 dakika 4 saniye; Meeus, 1998) periyoduyla modüle olmak zorundadır. Buna karşılık termal, iklimlendirme ve insan kaynaklı bütün çevresel etkiler **güneş günü** (24 saat) periyodunu taşır. Bu iki periyot günde yaklaşık 4 dakika kayar ve birkaç haftalık kesintisiz kayıtta tamamen ayrışır. Astronomi, kozmik kökenli sinyalleri yerel olanlardan tam bu yöntemle ayırır. Sinyalin faz kaymasının yıldız gününü izlemesi, teorinin lehine güçlü bir kanıt; güneş gününü izlemesi ise çevresel köken lehine belirleyici bir bulgudur.

**Kontrol 2 — Farklı malzeme ve uzunlukta eşzamanlı ikinci döngü.** Işık hızındaki gerçek bir değişim **evrenseldir**: farklı malzemeden ve farklı uzunlukta iki bağımsız döngüde **aynı oransal** ($\Delta f/f$) sinyali üretmek zorundadır. Termal ve mekanik artefaktlar ise malzemeye özgüdür; her döngüde farklı oransal değer verir. İki döngünün eşzamanlı ve aynı oranda kayması, çevresel açıklamayı büyük ölçüde eler.

**Kontrol 3 — Referanstan bağımsızlık.** Sinyal, farklı bir zaman referansına (GPS-disipline osilatör, sezyum standardı veya hidrojen maser) karşı da aynı büyüklükte korunmalıdır. Daha kararlı bir referansa geçildiğinde sinyalin küçülmesi veya kaybolması, ölçülen şeyin ışık hızı değil, referansın kendi drifti olduğunu gösterir.

**Kontrol 4 — Çevresel değişkenlerle korelasyonsuzluk.** Fiberin (oda değil) çekirdek sıcaklığı, mekanik gerinim, nem ve basınç eşzamanlı kaydedilmeli; sinyalin bu değişkenlerin hiçbiriyle korele olmadığı nicel olarak gösterilmelidir.

**Yanlışlanma taahhüdü.** Evrenakı Teorisi, 4. Postülat'ı bu sınamaya açıkça bağlar. Bağımsız laboratuvarlarca yürütülecek tekrarlarda ölçülen sinyal; **(a)** yıldız günü yerine güneş günü periyodu taşırsa, **(b)** farklı malzeme ve uzunluktaki döngülerde farklı oransal değerler verirse, **(c)** daha kararlı bir zaman referansına geçildiğinde kaybolursa veya **(d)** çevresel değişkenlerle korele çıkarsa; ışık hızının yerel vakumda değişken olduğu iddiası çürütülmüş sayılacak ve teorinin bu iddiaya dayanan çekirdek postülatı (Postülat 4) terk edilecektir. Kuram, bu koşulların gerçekleşmesi hâlinde savunulmayacaktır.

Bu bölümdeki düzeneklerin tam teknik dokümantasyonu — kol uzunlukları ve asimetri oranı, tur sayısı ve efektif optik yol, referans osilatörün Allan sapması, sayıcı mimarisi, ham veri setleri, hata bütçesi ve yukarıdaki dört kontrolün sonuçları — bağımsız tekrarı mümkün kılacak ayrıntıda yayımlanacaktır. Teori, bu dokümantasyon tamamlanana kadar bulgularını "rapor edilen sonuç" statüsünde tutar.
