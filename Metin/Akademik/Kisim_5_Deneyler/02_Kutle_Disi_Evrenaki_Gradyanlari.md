# 5.2 Kütle Dışı Evrenakı Gradyanları

Bir önceki bölümde (5.1), durağan sistemler üzerinden Evrenakı'daki kozmolojik yoğunluk dalgalanmalarının ışık hızına olan doğrudan etkisini incelemiştik. Bu bölümde ise, bu kez durağan olmayan, bilakis belirli bir kütlenin (örneğin hareketli sıradan bir cam plakanın veya kütle bloğunun) yarattığı lokal çekim/itim (gradient) alanlarının, dış uzaydaki Evrenakı dokusunu nasıl değiştirdiğini ve bu lokal değişimin ışık hızına yansımasını aynı 3 farklı hassas teknikle ölçeceğiz.

> **Kanıt durumu notu:** Bu bölümde aktarılan sayısal değerler, yazarın rapor ettiği ilk ölçüm bulgularıdır; ham veri setleri ve hata analizleri manüskriptin ilerleyen sürümlerinde yayımlanacaktır. Bulgular, bağımsız tekrar öncesinde "rapor edilen sonuç" statüsündedir.

## Deney 1: Michelson İnterferometresi ile Kütle Dışı Evrenakı Gradyanının Ölçümü

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/michelson_gradient_schematic_dark.png" alt="Michelson Gradyan Deneyi Karanlık Mod" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.5a: Michelson Kütle Gradyanı Deney Düzeneği. Işık huzmesine asla temas etmeden yaklaşan ve uzaklaşan bir kütlenin (cam plakanın) yarattığı Evrenakı basınç farklılıklarını ölçen sistem.</em></p>
</div>

Tarihsel olarak Michelson ve Morley'in (1887) deneyi, o dönemde "ether" (esir) adı verilen ve bugün bu kitapta **Evrenakı** olarak tanımlanan ortamı aramak; daha doğrusu, Dünya'nın bu ortam içindeki hareketinden doğacağı varsayılan ışık hızı farkını ölçmek üzere kurulmuştu. Deneyin ortamı saptayamaması (boş sonuç), "ether yoktur" kanısını doğurmuştur (aether-sürüklenme deneylerinin tarihçesi için bkz. Swenson, 1972). Oysa bu boş sonuç, ortamın var olmamasından değil, ortamın **yanlış tanımlanmış** olmasından — yani ışık hızının Evrenakı yoğunluğuna bağlı değişkenliğinin göz ardı edilmesinden — kaynaklanmaktadır. Bu deney, tam da o tarihî reddin doğduğu cihazı, yani Michelson interferometresini, bu kez Evrenakı'nın varlığını **gösterecek** biçimde yeniden kullanır.

### 5.2.1 Deneyin Amacı
Bu deneyin temel amacı; sıradan ve küçük kütlelerin bile, kendi dışlarında, yakın çevrelerinde bir Evrenakı yoğunluk gradyanı (basınç farklılaşması) oluşturduğunu ve bu yoğunluk farklılaşmasının, yanından geçen ışığın hızını değiştirebileceğini deneysel olarak ortaya koymaktır. Ölçüm, ışık hızındaki en küçük değişimleri girişim deseninin kayması üzerinden görünür kılan, optikte en güvenilir araçlardan biri olan Michelson interferometresiyle yapılır.

### 5.2.2 Teorik Altyapı ve Hipotez
Evrenakı kuramına göre, her kütle bulunduğu ortamdaki Evrenakı akışkanını sıkıştırır veya yoğunluğunu değiştirir. Kütleye yaklaştıkça Evrenakı basıncında ve yoğunluğunda farklılıklar meydana gelir. Işık hızı mutlak sabit olmayıp ortamın Evrenakı yoğunluğuna bağlı olduğundan, bir ışık demetinin çok yakınına bir kütle yaklaştırıldığında — ışığa fiziksel olarak hiç dokunmasa bile — o bölgedeki Evrenakı yoğunluğu değişecek ve ışığın hızı da buna bağlı olarak değişecektir. Hipotez: Kütlenin yaklaşıp uzaklaşması, yalnızca etkilenen koldaki ışık hızını değiştirerek girişim deseninde kütle hareketiyle senkron bir kayma üretecektir.

#### 5.2.2.1 Tarihsel Bağlam: "Ether"i Aramaktan Evrenakı'yı Ölçmeye
Michelson & Morley deneyinin ana ekipmanı olan interferometrenin özgün amacı, ether kaynaklı ışık hızı farkını ölçebilmekti. Bu çalışmada aynı cihaz, ortamın hareketini değil, **bir kütlenin ortamda yarattığı yerel yoğunluk gradyanını** hedef alacak biçimde yeniden kurgulanmıştır. Böylece bir zamanlar ortamın yokluğuna delil sayılan araç, doğru tanımlama (Evrenakı) altında ortamın varlığına delil üretecek konuma gelir: eskiden "ether" aranıyordu; burada ölçülen ve gözlenebilir kılınan büyüklük Evrenakı'dır. (Aynı geleneğin diğer köşe taşları — yıldız sapmasının keşfi, tam sürüklenme girişimi ve akan ortamda kısmi sürüklenme — için bkz. Bradley, 1728; Stokes, 1845; Fizeau, 1851.)

### 5.2.3 Deney Düzeneği ve Ekipmanlar
Deney, standart bir Michelson interferometresi altyapısına dayanır (Şekil 5.5b). Işık kaynağından çıkan ışık, ışın ayırıcıya (splitter) ulaştığında ikiye ayrılarak yansıtıcı A ve yansıtıcı B'ye gider; aynalardan geri dönen iki demet splitter üzerinde yeniden birleşerek ekrana düşer. İki kol farklı yollardan geçip farklı zamanlarda birleştiğinden ekranda bir **girişim deseni** oluşur; desendeki en küçük kayma, kollar arasındaki en küçük farkı görünür kılar. Işık kaynağı olarak 650 nm dalga boyunda lazer kullanılmıştır. Düzeneğin en kritik parçası, kollardan birine paralel yerleştirilmiş, **300×30×5 mm** ebatlarında ve **250 gram** ağırlığındaki cam plakadır (kütle bloğu); bu plaka bilgisayar kontrollü bir step motora bağlanarak ışık demetine hassas biçimde yaklaştırılıp uzaklaştırılabilmektedir. Yansıtıcı A yönündeki kol hiçbir etkiye maruz bırakılmayarak **referans kolu** olarak kullanılmış, diğer kol ise etki altına alınmıştır.

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/michelson_kaynak_sema.png" alt="Michelson interferometresi bileşen şeması" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.5b: Deneyde kullanılan Michelson interferometresinin bileşenleri: ışık kaynağı, ışın ayırıcı, yansıtıcı A (referans kol) ve B, step motora bağlı hareketli plaka, ekran ve gözlemci.</em></p>
</div>

### 5.2.4 Yöntem ve Uygulama
İnterferometre, ekranda net girişim saçakları oluşturacak biçimde ayarlanır ve hareketli plaka uzaktayken sistemin kararlı hâle gelmesi beklenir. Ardından step motor yardımıyla 250 gramlık cam plaka, B yansıtıcısı yönündeki ışık demetine yavaşça yaklaştırılır. **En hayati kural, plakanın ışık demetine hiçbir zaman fiziksel olarak dokunmamasıdır** (arada en az 1 mm mesafe bırakılmıştır). Yansıtıcı aynalarla splitter arasındaki mesafe — yani ışığın kat ettiği yol — sabit tutulduğundan, girişim desenindeki herhangi bir kayma yalnızca ışık hızının değişimine bağlanabilir. Plaka ışık demetine yaklaştırılınca 5 dakika, uzaklaştırılınca 5 dakika bekletilmiş; bu döngü sürekli tekrarlanmış ve ekrandaki desenler yüksek çözünürlüklü kamerayla anlık olarak kaydedilmiştir.

### 5.2.5 Gözlem ve Bulgular
Cam plaka ışık demetine yaklaştırıldığında, ekrandaki girişim saçaklarının net biçimde bir sağa bir sola kaydığı gözlenmiştir (Şekil 5.5c). Aynalarla splitter arası mesafe milimetrik olarak sabit olduğundan, bu kaymanın tek açıklaması, plakanın yaklaştığı koldaki ışık hızının değişmiş olmasıdır. Saçakların kayması, tamamen plakanın yaklaşma-uzaklaşmasına bağlı olarak, hareketle senkron biçimde ilerlemiştir.

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/michelson_girisim_ham.png" alt="Ham girişim saçakları" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.5c: Ekranda gözlenen ham girişim saçakları. Ok, plaka yaklaştırılıp uzaklaştırıldıkça saçakların kayma yönünü gösterir.</em></p>
</div>

#### 5.2.5.1 Saçak Kaymasının Sayısallaştırılması
Görsel olarak tek başına anlam taşımayan saçak kayması, sayısal bir büyüklüğe dönüştürülmüştür. Elde edilen ilk girişim görüntüsü temel (başlangıç) kabul edilmiş; bu karenin karanlık saçakları esas alınarak aynı doğrultuda çizgiler çizilmiş ve resmin dışına, her bölüntüsü bir girişim saçağına karşılık gelen sabit bir **cetvel** oluşturulmuştur (Şekil 5.5d). Bu cetvelin konumu, tüm görüntülerin analizi boyunca sabit tutulmuş ve bir referans noktası işlevi görmüştür.

<div style="display:flex; gap:16px; flex-wrap:wrap; justify-content:center; margin: 30px 0;">
    <div style="flex:1; min-width:260px; text-align:center;">
        <img src="Gorseller/michelson_cetvel_referans.png" alt="Referans girişim karesi ve cetvel" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
        <p style="font-size: 0.85em; color: var(--text-muted); margin-top: 8px;"><em>Şekil 5.5d: Temel (referans) kare. Karanlık saçaklardan üretilen ve konumu sabit tutulan cetvel; her bölüntü bir saçağa karşılık gelir (0 ekseni yeşil).</em></p>
    </div>
    <div style="flex:1; min-width:260px; text-align:center;">
        <img src="Gorseller/michelson_cetvel_kaymis.png" alt="Kaymış girişim karesi ve X kayması" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
        <p style="font-size: 0.85em; color: var(--text-muted); margin-top: 8px;"><em>Şekil 5.5e: Plaka yaklaştığında saçaklar cetvele göre X kadar kayar. Bu kayma, sabit cetvel üzerinden saçak (parmak) cinsinden ölçülür.</em></p>
    </div>
</div>

Her yeni görüntüde karanlık saçaklardan aynı doğrultuda çizgiler çizilerek cetvele göre fark hesaplanmış, bu değerler bir bilgisayar programıyla saçak (parmak) cinsinden sayısallaştırılmıştır; ulaşılan hassasiyet minimum bir pikseldir. Sayısallaştırılan bu kaymalar zamana karşı grafiklendiğinde, saçak kaymasının plakanın hareketiyle birebir senkron seyrettiği açıkça görülür (Şekil 5.5f). Bu deney için kütleye bağlı saçak kayması yaklaşık **0,3 saçak (parmak)** genişliği olarak ölçülmüştür.

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/graf_michelson_kayma.png" alt="Saçak kayması ve plaka hareketi grafiği" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.5f: Saçak kaymasının (mavi) plaka uzaklığıyla (kırmızı) senkron seyri. Cam plakanın her yaklaşma-uzaklaşması, girişim deseninde ~0,3 saçaklık tekrarlı bir kaymaya karşılık gelir.</em></p>
</div>

### 5.2.6 Sonuç ve Değerlendirme
Kütleye bağlı ışık hızı değişimi, dalga optiği kuralları referans alınarak hesaplandığında yaklaşık **200 m/sn**'lik bir hız farkına karşılık gelmektedir. Sadece 250 gramlık sıradan bir cam kütlesinin — ışığa temas dahi etmeden — ışık hızını 200 m/sn mertebesinde değiştirmesi, uzay-zaman eğriliği gibi genel görelilik kavramlarıyla açıklanamayacak bir olgudur; Görelilik çerçevesinde böyle bir kütlenin ışık hızına etkisi hesaplanamayacak kadar sıfıra yakındır. Bu sonuç, her kütlenin çevresinde görünmez bir Evrenakı yoğunluk gradyanı bulunduğunu ve ışık hızının, yanından geçtiği kütlenin oluşturduğu Evrenakı basıncına anında tepki verdiğini güçlü biçimde destekler. Bir sonraki deneyde (Deney 2), aynı olgu tamamen bağımsız bir ölçüm ilkesiyle — fiber içindeki ışık hızının frekans sayımıyla — sınanarak bu bulgu çapraz doğrulanacaktır.

## Deney 2: Fiber Osilatör ile Kütle Dışı Evrenakı Gradyanının Ölçümü

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/ring_gradient_schematic_dark.png" alt="Fiber Osilatör Kütle Gradyan Deney Düzeneği (şematik)" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.6a: Fiber Osilatör Kütle Gradyanı Deney Düzeneği (şematik). HFBR-53A5VEMZ modülü ve fiber kablo yanına yaklaşıp uzaklaşan bir kütlenin (plakanın) fiber içindeki ışık hızına etkisini ölçen sistem.</em></p>
</div>

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/fiber_osilator_deney_duzenegi.png" alt="Fiber Osilatör Deney Düzeneği" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.6b: Deney düzeneğinin gerçek görünümü. Step motora bağlı hareketli plaka, fiber optik kabloya asla dokunmadan yaklaştırılıp uzaklaştırılırken; fiber osilatörün ürettiği frekans, çevresel etkilere karşı yalıtılmış bir kabin içinde bir frekans sayıcıyla sürekli izlenir.</em></p>
</div>

Bir önceki Michelson deneyi, kütlenin kendi dışında yarattığı Evrenakı gradyanının **açık ortamdaki (hava/vakum)** ışık hızını değiştirdiğini göstermişti. Bu ikinci deney ise, aynı gradyanın **yoğun bir katı maddenin — cam fiberin — içinden geçen ışığın hızını** da etkileyip etkilemediğini, girişim deseni sayımına dayanmayan, tamamen bağımsız bir ölçüm ilkesiyle (frekans sayımı) sınamak üzere tasarlanmıştır.

### 5.2.7 Deneyin Amacı
Bu deneyin temel amacı, Evrenakı yoğunluğuna bağlı olarak değişen ışık hızını ölçerek, dolaylı biçimde **Evrenakı yoğunluğunun kendisini ölçülebilir bir büyüklük hâline getirmektir.** Buradaki hedef, ışığın mutlak hızının kaç km/sn olduğunu saptamak değildir; ışık hızı hangi değerde olursa olsun, o hızda **ne kadar değişim** meydana geldiğini son derece yüksek bir çözünürlükle tespit etmektir. Böyle bir deneyin başlıca güçlüğü, ışık hızındaki çok küçük değişimleri güvenilir biçimde algılayabilecek bir düzenek kurmaktır; bu deneyin özgün katkısı da tam olarak bu hassasiyeti sağlayan ölçüm mimarisidir.

### 5.2.8 Teorik Altyapı ve Hipotez
Evrenakı kuramına göre, bir kütlenin çevresindeki Evrenakı yoğunluğu ve basıncı kütleye yaklaştıkça azalır, kütleden uzaklaştıkça artar; ışığın yerel hızı ise Kavrama Yasası gereği $c=\sqrt{P/\rho}$ ile belirlenir. Hem $P$ hem $\rho$ düştüğü hâlde $c$'nin **düşeceğini** garanti eden şey, yön kuralıdır (bkz. Bölüm 2.4.2 ve Ek B.3): yoğunluk basınca ancak $k<1$ kesriyle eşlik ettiğinden basınçtaki oransal düşüş daima daha büyüktür ve $\delta c/c = \tfrac{1-k}{2}\,\delta P/P_0 < 0$ olur — kütleye yaklaşan ışık zorunlu olarak yavaşlar. Bu önermeler, fiber optik kablonun içindeki Evrenakı için de geçerlidir. Buradan türetilen hipotez şudur: Bir kütle fiber kabloya yaklaştırıldığında, kütlenin oluşturduğu Evrenakı yoğunluk gradyanı fiberin içine nüfuz ederek o bölgedeki Evrenakı basıncını değiştirecek; dolayısıyla fiberden geçen ışığın hızı, dış kütlenin yakınlığına bağlı olarak ölçülebilir biçimde değişecektir. Işık hızındaki bu değişim, aşağıda tanımlanan fiber osilatörün frekansına birebir yansıyacaktır.

#### 5.2.8.1 Kavramsal Model: Yankı Osilatörü Analojisi
Deneyin işleyiş ilkesi, sesle kurulan basit bir düşünce deneyiyle sezgisel olarak kavranabilir. Karşılıklı duran iki kişiye şu talimat verilsin: *"Karşındaki kişinin 'Mai' dediğini duyduğun anda sen de 'Mai' diye seslen."* İlk kişi bir kez "Mai" dediğinde, iki kişi arasında kesintisiz, ardışık bir "Mai–Mai" döngüsü başlar. Belirli bir zaman aralığında tekrarlanan sözcük sayısı — yani **tekrar frekansı** — yalnızca üç etkene bağlıdır: (1) deneklerin tepki (refleks) süresi, (2) sesin havadaki hızı ve (3) denekler arasındaki mesafe.

Bu üç etkenden ikisi sabit tutulursa, tekrar frekansı doğrudan üçüncü etkenin bir ölçüsüne dönüşür. Refleks süresi ve mesafe sabitken frekans yalnızca ses hızına; ses hızı sabit tutulup mesafe değiştirildiğinde ise frekans yalnızca mesafeye bağlı olur (mesafe arttıkça frekans düşer, azaldıkça yükselir). Düzenek, ikinci deneği sesi geri yansıtan bir duvarla değiştirip tek deneğe "kendi yankını duyduğunda yeniden seslen" talimatı vererek de kurulabilir; ilke aynıdır. **Fiber osilatör tam olarak bu yankı döngüsünün ışıkla çalışan, elektronik karşılığıdır:** ses yerine ışık, hava yerine fiber, refleks yerine devrenin tepki süresi geçer ve frekans, fiber içindeki ışık hızının doğrudan bir göstergesi hâline gelir.

### 5.2.9 Deney Düzeneği ve Ekipmanlar
Düzeneğin elektronik kalbi; bir **HFBR-53A5VEMZ** fiber optik alıcı-verici (transceiver) modülü, ona bağlı bir lazer sürücü devresi ve yüksek çözünürlüklü bir frekans sayıcıdan (frequency counter) oluşur. Modüle **30,63 metre** uzunluğunda bir fiber optik kablo bağlanarak kapalı bir osilasyon döngüsü kurulmuştur. Deneyin kritik fiziksel unsuru, fiber kabloya paralel asılmış ~**300 gram** ağırlığındaki hareketli bir plakadır (kütledir); plaka, bilgisayar kontrollü bir step motora bağlanarak kabloya yaklaştırılıp uzaklaştırılabilmekte, ancak hiçbir aşamada fibere veya taşıyıcı düzeneğe temas etmemektedir. Ölçümlerin çevresel gürültüden arındırılabilmesi için osilatör, titreşim ve hava akımından yalıtılmış kararlı bir kabin (bkz. Şekil 5.6b) içine yerleştirilmiştir.

#### 5.2.9.1 Fiber Osilatörün Çalışma İlkesi
<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/fiber_osilator_blok_diyagram.png" alt="Fiber Osilatör Blok Diyagramı" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.6c: Fiber osilatörün blok şeması. Lazer sürücü devresinden çıkan ışık, ~30 m'lik fiber kablodan geçerek alıcıdaki yükselteç/sensöre ulaşır; devre, ışığın gidiş-gelişini kendi kendini besleyen bir açılıp-kapanma döngüsüne çevirir ve döngü frekansı bir frekans sayıcıyla okunur.</em></p>
</div>

Osilatörün çalışması, 5.2.8.1'deki yankı analojisiyle birebir örtüşür: Verici devresine bağlı lazer aktif olur ve ışık üretir. Üretilen ışık fiber boyunca ilerleyerek alıcı devredeki sensöre ulaşır. Sensör ışığın vardığını algıladığı anda lazerin ışık yaymasını durdurur; ancak bu esnada fiberin içinde hâlâ yol alan ışık vardır. Son ışık zerreleri sensöre ulaştığında alıcı devre, verici devreye yeniden ışık üretmesi için sinyal gönderir. Yeni üretilen ışık, fiber boyunca kat etmesi gereken mesafe nedeniyle sensöre ancak belli bir gecikmeyle varır. Böylece sistem, ışığın "açılıp-kapanması" biçiminde kendi kendini besleyen kararlı bir **osilasyon** üretir.

Bu osilasyonun frekansı üç etkene bağlıdır: (1) kullanılan elektronik devrelerin tepki süresi (refleks), (2) fiberin uzunluğu ve (3) ışığın fiber içindeki hızı. **Fiber uzunluğu ve elektronik tepki süresi sabit tutulduğunda, ölçülen frekans doğrudan ışık hızının bir fonksiyonu hâline gelir;** ışık hızındaki en küçük bir değişiklik bile osilatör frekansındaki değişiklik olarak gözlenebilir hâle gelir.

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/fiber_osilator_hfbr_devre.png" alt="HFBR-53A5VEMZ Alıcı-Verici Devre Şeması" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.6d: Osilatörün çekirdeğini oluşturan HFBR-53A5VEMZ fiber optik alıcı-verici modülünün açık devre şeması (lazer sürücü, PECL giriş, ön/son yükselteç ve sinyal-algılama katları).</em></p>
</div>

#### 5.2.9.2 Fiber İçindeki Işık Hızının Hesaplanması ve Cihaz Hassasiyeti
Ölçülen frekanstan ışık hızına geçerken, elektronik devrelerin tepki gecikmesinin hesaba katılması gerekir; bu gecikme, yankı analojisindeki deneğin refleks süresine karşılık gelen sabit bir büyüklüktür. Gecikme, frekans periyodunun hem yükselme hem de inme kenarlarında etki ettiğinden iki yükselme ve iki inme zamanı birlikte dikkate alınır. Kullanılan **HFBR-53A5VEMZ** modülünün veri sayfası (datasheet) değerlerine göre bu süreler (Avago Technologies, 2012). Aşağıdaki hesapta fiber içi ışık hızı $c_f$ ile ($c_f$: fiber içi ışık hızı; eski yazım $C$), osilatör frekansı ise $\nu_{osc}$ ile gösterilir ($\nu_{osc}$: osilatör frekansı; eski yazım $f$ — Fizeau katsayısı $f$ ile karışmaması için ayrıldı):

<div style="border:1px solid var(--border-color); border-radius:8px; padding:16px 22px; margin:20px auto; max-width:640px; font-family:'Courier New',monospace; line-height:1.9;">
tr = Data Output Rise Time = 3 ns × 2 = 6 ns<br>
tf = Data Output Fall Time = 3 ns × 2 = 6 ns<br>
l&nbsp;&nbsp;= Fiber kablo boyu = 30,63 m<br>
ν_osc = Ölçülen osilatör frekansı = 5.472.870 Hz<br>
c_f&nbsp;&nbsp;= Fiber içindeki ışık hızı = ?<br>
<br>
c_f = ν_osc · l / (1 − ν_osc · (tr + tf))<br>
c_f = 5.472.870 · 30,63 / (1 − 5.472.870 · (6×10⁻⁹ + 6×10⁻⁹))<br>
c_f = 167.634.008 m / 0,93432556<br>
<strong>c_f = 179.417.127 m/sn</strong>
</div>

Bu değer, deney düzeneğindeki fiber içinde ışığın hızının ~**179.417.127 m/sn** olduğunu verir. Ancak deneyin amacı bu mutlak değeri saptamak değil, bu değerde meydana gelen **değişimleri** yakalamaktır. Elektronik tepki süresi ve kablo boyu sabit olduğundan, frekanstaki her değişim yalnızca ışık hızındaki değişime karşılık gelir. Düzeneğin çözünürlüğü öylesine yüksektir ki, ışık hızındaki **33 m/sn** mertebesindeki bir farkı dahi algılayabilecek düzeydedir. Bu hassasiyet, sonraki bölümde raporlanan değişimlerin ölçüm gürültüsünün çok üzerinde olduğunu güvence altına alır. *(katalog, birim denetimi ve n≈1,67 tutarlılık notu: **Ek M-33**)*

### 5.2.10 Yöntem ve Uygulama
Osilatör çalıştırılıp sistemin kararlı bir frekansa oturması beklenir. Önce referans (temel çizgi) alınır: plaka fiberden 35 mm uzakta ve sabitken yarım saatlik bir gözlem yapılır; her 10 saniyede bir okunan frekansta bu süre boyunca hiçbir değişim gözlenmez — düzeneğin kütle yokluğunda kararlı olduğu böylece doğrulanır. Ardından step motorlar devreye alınır: plaka fibere **1 mm** kalana dek yaklaştırılıp 5 dakika bekletilir, sonra **35 mm** uzağa çekilip yine 5 dakika bekletilir. Bu ileri-geri döngü sürekli tekrarlanır ve **plaka hiçbir aşamada fibere fiziksel olarak temas etmez.** Frekans, plakanın hareketiyle eşzamanlı olarak (10 sn'de bir) kaydedilip grafiklenir.

Aynı düzenek üzerinde plaka malzemesi de değiştirilerek deney yinelenmiştir: cam, tahta, strafor, bakır, pleksiglas ve çelik ayrı ayrı denenmiş; yaklaşma-uzaklaşma süreleri ve fiberin yönelimi de değiştirilerek yüzlerce varyasyon çalışılmıştır. Ayrıca osilatör, uzun süreli bir gözlem için kararlı ve yalıtılmış bir ortama yerleştirilerek, Dünya'nın Güneş çevresindeki yörüngesi boyunca Güneş'e yaklaşıp uzaklaşmasına bağlı Evrenakı yoğunluğu değişiminin ışık hızına yansımasını izlemek üzere üç yıl boyunca kesintisiz çalıştırılmıştır. Bu geniş veri kümesinin ayrıntılı analizi ayrı bir çalışmanın konusu olup, burada yalnızca kütle kaynaklı ana etki ele alınmaktadır.

### 5.2.11 Gözlem ve Bulgular
Referans aşamasında (plaka 35 mm uzakta ve sabitken) frekansta hiçbir değişim gözlenmemiştir; osilatör, yarım saatlik gözlem boyunca sabit **5.472.870 Hz** değerini korumuştur. Bu aşama, düzeneğin kütle yokluğunda kararlı bir taban çizgisine sahip olduğunu doğrular (Şekil 5.6e).

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/graf_fiber_referans.png" alt="Referans ölçümü grafiği" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.6e: Referans (taban) ölçümü. Plaka 35 mm uzakta ve hareketsizken (kırmızı), ölçülen frekans (mavi) yarım saat boyunca hiç değişmez. Her nokta ≈ 10 sn.</em></p>
</div>

Step motorlar devreye alınıp plaka fibere 1 mm yaklaştırıldığında ise osilatör frekansı — dolayısıyla fiber içindeki ışık hızı — belirgin biçimde değişmiştir. Frekanstaki bu dalgalanmalar, plakanın ileri-geri hareketiyle birebir senkronize seyretmiştir: plaka yaklaştıkça frekans bir yöne, uzaklaştıkça karşı yöne kaymış ve bu örüntü her döngüde tekrarlanmıştır (Şekil 5.6f).

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/graf_fiber_plaka_dongusu.png" alt="Plaka döngüsü ve senkron frekans grafiği" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.6f: Plakanın 1 mm ↔ 35 mm döngüsü (kırmızı) ile osilatör frekansının (mavi) eşzamanlı salınımı. Frekans, kütlenin her yaklaşma-uzaklaşmasını birebir izler.</em></p>
</div>

Sadece 300 gramlık bir plakanın fibere yaklaşması, ışık hızında yaklaşık **4500 m/sn**'lik bir fark üretmiştir; bu değer, düzeneğin 33 m/sn'lik gürültü tabanının yaklaşık 136 katıdır (Şekil 5.6g).

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/graf_fiber_4500.png" alt="Kütleye bağlı ~4500 m/sn değişim grafiği" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.6g: 300 g plakanın yaklaşıp uzaklaşmasıyla frekansta gözlenen tekrarlı ve belirgin değişim; ışık hızına çevrildiğinde ~4500 m/sn'lik bir farka karşılık gelir.</em></p>
</div>

Gözlem sırasında beklenmedik bir davranış da kaydedilmiştir. Deneyin tasarımında üç olası sonuç öngörülmüştü: kütle yaklaştıkça ışık hızının azalması, artması veya değişmemesi. Gözlemin başında kütle yaklaştırıldığında ışık hızı **artmış**, ilerleyen saatlerde ise eğilim tersine dönerek kütle yaklaştığında ışık hızı **azalmıştır**. Her iki yönün de aynı deney içinde birlikte gözlenmesi ilk bakışta öngörülmeyen bir durumdur. Nitekim günlerce süren gözlemlerde, plakanın hareketiyle örtüşen periyotların dışında, kütleden bağımsız olarak da değişen ve zaman zaman **16.000 m/sn**'ye ulaşan hız farklılıkları veriye yansımıştır; bu harici etkenin kaynağı henüz kesin olarak saptanamamıştır (Şekil 5.6h).

**Bu gözlemin doğru okunması — iki kütle etkileşimi ve nedensel sınır:** Bu deneyde ışık boş uzaydan değil, bir kütlenin (fiber camının) **içinden** geçer; hızı, fiberin **kütle-içi** Evrenakı gradyanına bağlıdır (kütle-içi gradyanın doğrudan haritalanması için bkz. Bölüm 5.3). Plaka da ışığa değil, ışığın içinden geçtiği **diğer kütleye** (fibere) yaklaştırılır. Dolayısıyla ölçülen büyüklük tek bir kütlenin ışığa etkisi değildir; **yaklaşan iki kütlenin gradyanlarının üst üste binmesiyle** fiberin içinde oluşan bileşik Evrenakı yoğunluğudur. Ayrıca bu düzenekte **sıcaklık ölçümü yapılmamıştır**; iki madde arasında oluşan sıcaklık farkları dahi Evrenakı deplasmanını etkilediğinden, gözlenen iki yönlü tepkinin nedeni — gradyan süperpozisyonu mu, termal kaynaklı deplasman değişimi mi, yoksa hareketli plakanın önündeki geçici sıkışma cephesi mi — **tayin edilememiştir**. Bu nedenle deneyin kanıtladığı önerme şudur: **bir kütlenin iç gradyanı, başka bir kütlenin yaklaşmasıyla ölçülebilir biçimde değiştirilebilir.** Deney, "kütle yaklaştıkça ışık hızlanır mı, yavaşlar mı" sorusunu ise **yanıtlamaz** ve yanıtlamak zorunda da değildir — çünkü bu sorunun cevabı deneyden bağımsız olarak yerleşiktir: teorinin başka gözlemlerle doğrulanan kesin kuralı gereği **ışık, madde yanında ve içinde (düşük $P/\rho$ bölgesinde) yavaşlar** (Yön Kuralı, Bölüm 2.4.2; camda yavaşlama ve Fizeau doğrulaması $f=1-1/n^2$, Bölüm 3.4.6; SN 1987A yol bütçesi, Bölüm 2.4.4). Bu kural bu deneyin belirsizliğinden etkilenmez.

*Aday mekanizma notu (ayrıştırılması sıcaklık kontrolü gerektirir):* İki yönlü örüntünün ("önce artış, sonra azalış") teori içindeki adaylarından biri, hareketli plakanın sıkıştırılabilir ortamda (Postülat 1) önünde ittiği **geçici sıkışma cephesidir**: cephe yerel basıncı geçici yükseltir ($c$ artar), deplasman havuzu dengeye oturunca kalıcı açık kalır ($c$ azalır). Bu aday iki ölçekleme imzası taşır — geçici bileşen plakanın **yaklaşma hızıyla**, kalıcı bileşen plakanın **kütlesiyle** ölçeklenmelidir — ancak sıcaklık kaydı olmadan termal deplasman adayından ayrıştırılamaz. Kütleden bağımsız, ~16.000 m/sn'ye varan taban kaymaları için de başlıca aday termal etkidir (fiberde optik yolun sıcaklık katsayısı ≈$10^{-6}/^\circ$C; bkz. Bölüm 5.1.5). Neden ayrıştırması, sıcaklık-kontrollü tekrar deneyiyle birlikte Bölüm 7.4'te açık hesap kalemi olarak kayıtlıdır.

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/graf_fiber_gunlerce.png" alt="Günlerce süren gözlem grafiği" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color); background:#fff;">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.6h: Günlerce kesintisiz gözlem. Plakanın hızlı yaklaşma-uzaklaşma salınımları (dar dişler), kütleden bağımsız ve yavaş seyreden geniş bir taban kaymasının üzerine biner; toplam salınım zaman zaman ~16.000 m/sn'ye ulaşır.</em></p>
</div>

### 5.2.12 Sonuç ve Değerlendirme
Astronomik ölçekte "yok" sayılabilecek 300 gramlık sıradan bir kütlenin, fiber içindeki ışık hızında 4500 m/sn mertebesinde bir değişime yol açması, klasik fizik ve Görelilik kuramlarıyla açıklanamayan bir olgudur; Görelilik çerçevesinde böyle bir kütlenin ışık hızına etkisi hesaplanamayacak kadar sıfıra yakındır. Bulgunun iki yönlü yapısı (hem yavaşlama hem hızlanma) ise deneyin nedensel sınırını çizer: sıcaklık ölçümü yapılmadığından, gözlenen değişimin kaynağı (iki kütle gradyanının süperpozisyonu, termal deplasman veya geçici sıkışma) tayin edilememiştir. Bu belirsizlik deneyin ana kanıtını zayıflatmaz — kanıtlanan önerme, **bir kütlenin iç Evrenakı gradyanının başka bir kütle tarafından ölçülebilir biçimde değiştirilebildiğidir.** Işığın madde yanında ve içinde yavaşladığı kuralı ise bu deneyin yetki alanının dışındadır ve başka doğrulamalarla (camda yavaşlama, Fizeau katsayısı, SN 1987A) kesin olarak yerleşiktir; bu deneydeki yön belirsizliği o kuralı tartışmaya açmaz. Neden ayrıştırması için gereken sıcaklık-kontrollü tekrar, Bölüm 7.4'te açık hesap kalemi olarak kayıtlıdır.

Sonuç olarak deney; kütlelerin çevrelerinde görünmez bir Evrenakı alanı oluşturduğunu, kütleye yaklaştıkça bu alanın yoğunluğunun değiştiğini ve bu yoğunluk gradyanının en katı maddelerin (fiberin) içine dahi sızarak ışığın hızını belirlediğini, bağımsız bir ölçüm ilkesiyle (frekans sayımı) desteklemektedir. Michelson deneyinin girişim-deseni sonuçlarıyla aynı yönde olması, bulgunun tek bir yönteme özgü bir yapaylık olmadığını güçlendirir. Böylece Evrenakı (Mai), doğru tanımlanması hâlinde **gözlenebilir ve ölçülebilir** bir büyüklük olarak deneysel bir zemine oturmaktadır.

## Deney 3: Attometer ile Kütle Dışı Evrenakı Gradyanının Ölçümü

<div style="text-align: center; margin: 30px 0;">
    <img src="Gorseller/attometer_gradient_schematic_dark.png" alt="Attometer Kütle Gradyan Deneyi Karanlık Mod" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 0.9em; color: var(--text-muted); margin-top: 10px;"><em>Şekil 5.7: Attometer Kütle Gradyan Deney Düzeneği. 60 cm'lik vakum tüpüne fiziksel temas etmeden dışarıdan yaklaşıp uzaklaşan bir kütlenin, vakum içindeki ışığın uçuş zamanına (time-of-flight) olan etkisini ölçen sistem.</em></p>
</div>

### 5.2.13 Deneyin Amacı
Michelson ve Fiber Ring Osilatör deneylerinde elde edilen kütleye bağlı ışık hızı değişkenliği (Evrenakı gradyanı) olgusunu, bizzat gidiş-dönüş süresini kaydeden (time-of-flight) ultra yüksek çözünürlüklü Attometer cihazı ile doğrulamaktır. Temel amaç, dışarıdan vakum tüpüne yaklaştırılan sıradan bir kütlenin, vakum içerisindeki uçuş süresinde yaratacağı attosaniye mertebesindeki sapmaları tespit etmektir.

### 5.2.14 Teorik Altyapı ve Hipotez
Evrenakı teorisine göre, sıradan bir kütle dahi kendi etrafındaki Evrenakı basıncını değiştirerek bir gradyan yaratır. Bu gradyan, yalnızca hava veya fiber optik gibi maddesel ortamlara değil, en saf vakum ortamlarına bile nüfuz eder. Hipotezimize göre; ışık vakum bir tüpün içerisinde sabit bir mesafeyi kat ederken, tüpün dışından bu kütle yaklaştırıldığında vakumun içindeki Evrenakı yoğunluğu değişecek ve buna bağlı olarak ışığın 60 cm'yi gidiş-dönüş süresinde periyodik dalgalanmalar oluşacaktır.

### 5.2.15 Deney Düzeneği ve Ekipmanlar
Sistem, ışığın gidiş-dönüş uçuş süresini (time-of-flight) attosaniye çözünürlüğü ile ölçebilen **Attometer** dijital modülü, 60 cm'lik yalıtılmış bir vakum tüpü ve sonundaki yansıtıcı aynadan oluşur. Bir önceki deneyde olduğu gibi, vakum tüpüne paralel olarak yerleştirilmiş küçük bir kütle plakası (cam/metal) mevcuttur. Bu kütle plakası, bir step motor yardımıyla vakum tüpüne yaklaştırılıp uzaklaştırılabilecek şekilde kurulmuş olup, tüpe hiçbir şekilde mekanik bir temasta bulunmaz.

### 5.2.16 Yöntem ve Uygulama
Attometer cihazı aktif edilerek lazer atımlarının vakum içindeki standart uçuş süresi referans olarak kaydedilir. Ardından step motor devreye sokulur ve kütle plakası vakum tüpüne 1 mm kalana kadar yaklaştırılıp 5 dakika bekletilir; daha sonra uzaklaştırılarak döngü devam ettirilir. Attometer, kütlenin tüpe yaklaştığı ve uzaklaştığı anlarda ışığın tüp içindeki gidiş-dönüş süresini aralıksız olarak dijital ortama kaydeder.

### 5.2.17 Gözlem ve Bulgular
Önceki deneylerle mükemmel bir uyum sağlayacak şekilde, kütle plakası vakum tüpüne her yaklaştığında, Attometer ekranında okunan lazer uçuş süresinde attosaniye ve femtosaniye mertebesinde gecikmeler/hızlanmalar gözlemlenmiştir. Kütle uzaklaştığında ise uçuş süresi yeniden referans değerlerine dönme eğilimi göstermiştir. Kütlenin hareketi ile ışık hızındaki bu değişim tamamen senkronize ilerlemiştir.

### 5.2.18 Sonuç ve Değerlendirme
Kütleye fiziksel olarak temas etmeyen, tamamen yalıtılmış bir vakum tüpünün içerisinde bile ışık hızının, dışarıdaki bir kütlenin hareketine bağlı olarak değişmesi muazzam bir bilimsel atılımdır. Bu deney, kütlelerin kendi dışlarında oluşturdukları Evrenakı gradyanlarının (basınç farklılıklarının) doğrudan vakuma sızabildiğini ve ışığın bu Evrenakı rüzgârları eşliğinde hızını anlık olarak güncellediği bulgusunu zaman-ölçümü yöntemiyle de desteklemiştir.
