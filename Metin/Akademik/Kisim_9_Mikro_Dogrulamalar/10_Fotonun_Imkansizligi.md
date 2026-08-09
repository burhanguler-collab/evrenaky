# 9.10 "Foton"un İmkânsızlığı

Kitabın "foton"la hesabı yeni değildir: kavramın ontolojik reddi 2.2.1'de ("Foton İllüzyonunun Reddi"), dalga-parçacık ikiliğinin kriz kataloğu 1.2.2'de yapılmıştı. Kısım 9'un önceki bölümleri bu redde yeter-sebep davasını ekledi: kesikliliğin adresi alıcının penceresidir (9.2), fotoelektrik ve Compton yalnız katar, aralık ve pencere ile sayısal doğrulamadan geçer (9.4), kuantum optiğin klik istatistikleri paket mekaniğiyle çıkar (9.7), çift yarık wake geometrisiyle çözülür (9.9). Bütün bu hattın ortak hükmü **"foton gereksizdir"** idi. Bu bölümün iddiası bir basamak yukarıdadır: **"foton", kendisini taşıyan matematiğin içinde imkânsızdır.**

Yöntem beyanı baştan yapılmalıdır: bu bölümde Evrenakı mekaniği tanık sandalyesine çağrılmaz. İddianamenin bütün delilleri standart fiziğin **kendi** malzemesidir — kendi Fourier analizi, kendi Hilbert uzayı, kendi yerleşiklik teoremleri, kendi kaynak cebiri, kendi deney kayıtları ve kendi kurucularının tanıklığı. Teorinin karşılığı her sergide en fazla tek cümlelik köprü olarak anılır; hesabın tamamı 9.10.11'de toplanır.

## 9.10.1 İddia ve İşbölümü

Ders kitabı anlatısı "foton"a üç niteliği birden yükler:

| # | Nitelik | Dayandırıldığı gözlem |
|---|---|---|
| N-1 | **Tek-sayılabilirlik / bölünmezlik** — ışık "bir, iki, üç" diye sayılan bütün mermilerden oluşur | klik merdiveni, anti-demetlenme |
| N-2 | **Belirli frekans ve enerji** — her merminin tanımlı bir $\nu$'sü ve $E=h\nu$'sü vardır | fotoelektrik doğrusu, Compton kayması |
| N-3 | **Yerleşiklik** — mermi bir yerdedir; uçar, çarpar, soğurulur | ekrandaki nokta, dedektör kliki |

Bölümün göstereceği şudur: bu üç nitelik yalnız üçü birden değil, **ikişer ikişer bile** bağdaşmaz. N-2+N-3 çiftini Fourier analizi yasaklar (9.10.3), N-1+N-2 çiftini kuramın kendi durum uzayı yasaklar (9.10.4), N-1+N-3 çiftini kesin yerleşiklik teoremleri yasaklar (9.10.5). Ayrıca hiçbir kaynak böyle bir nesne üretemez (9.10.6), hiçbir aygıt onu tek başına ölçemez — yüz yılın bütün sensörleri üreticilerin kendi verileriyle denetlenir (9.10.7) —, üretildiği iddia edilen yerde muhasebe tutmaz (9.10.8–9.10.9) ve kavramın kurucuları bunu baştan beri söylüyordu (9.10.10). Geriye tek kaçış kalır — "foton aslında nesne değil, muhasebe birimidir" — ve o kaçışın vardığı yer teorinin zaten kurduğu penceredir (9.10.11).

## 9.10.2 Tanım Krizi: Aynı Kelimenin Dört Uyumsuz Sahibi

İddianameye tanım tespitiyle başlanır, çünkü standart literatürde "foton" kelimesi tek bir nesneyi göstermez; birbiriyle bağdaşmayan en az dört tanımı aynı anda taşır (kavramın tarihsel evrimi için Kidd ve ark., 1989):

| Tanım | Yaşadığı yer | Çelişki |
|---|---|---|
| **Nokta mermi** | ders kitabı; fotoelektrik/Compton anlatısı | konum operatörü yok (9.10.5) |
| **Dalga paketi** | kuantum optik pratiği | paketin bölünmezliği yok; ışın bölücüde genlik bölünür |
| **Mod uyarımı** | QED'in resmî tanımı | mod tüm uzayı kaplar; "çarpan" bir şey değildir |
| **Klik** | operasyonel tanım | kliki üreten dedektördür; ışığa dair ontolojik içerik taşımaz |

Sergilerin her biri bu tanımlardan hangisini vurduğunu belirtecektir. Şimdiden kaydedilmesi gereken tuhaflık şudur: bir kavramın yüz yıl sonra hâlâ dört uyumsuz tanımla iş görmesi, kavramın bir **cisme** değil, bir **muhasebe alışkanlığına** ad olduğunun ilk işaretidir.

## 9.10.3 Fourier Üçgeni: $E=h\nu$'nün Gizli Zaman Tabanı

Frekans, tekil bir anın değil bir **sürecin** özelliğidir: $\nu$'yü tanımlamak için en az bir periyot ($1/\nu$) gözlem gerekir ve hassasiyet Fourier sınırına tabidir:

$$\Delta\nu\,\Delta t \;\gtrsim\; \frac{1}{4\pi}$$

Bu, yorum değil teoremdir ve "foton"un iki niteliğini aynı nesnede yasaklar:

- **Keskin frekans** ($\Delta\nu\to0$) isteyen "foton", zamana sonsuz yayılmak zorundadır ($\Delta t\to\infty$) — hiçbir yere "varamaz", hiçbir klik üretemez.
- **Anlık varış** ($\Delta t\to0$) isteyen "foton", sonsuz frekans bandı taşımak zorundadır ($\Delta\nu\to\infty$) — "onun frekansı $\nu$" diye bir şey kalmaz ve $E=h\nu$'ye koyacak $\nu$ yoktur.

N-2 ile N-3 aynı nesnede bir arada olamaz; "belirli renkte bir nokta" matematiksel bir oksimorondur. Ölçek duygusu için: kırmızı ışığın periyodu $T=1/\nu\approx2{,}2$ fs'dir — "anlık" bir mermi tek periyodunu bile tamamlayamaz. Modern birkaç-periyotluk lazer atımları bunu her gün ölçer: atım kısaldıkça spektrum tam Fourier'in emrettiği gibi genişler. Frekans, tek merminin değil **dizinin** malıdır.

Aynı sergiye ikinci delil boyut analizinden gelir: $[h]=\text{J·s}=\text{J/Hz}$. Yani $E=h\nu$ formülü ancak bir **zaman tabanıyla** çarpılarak enerji üretir; saniye, formülün içine gömülüdür. Standart fizik bu sürenin sahibini hiç adlandırmaz — $h$'ye "eylem kuantumu" der ve sorgulamayı kapatır. Oysa formülün kendisi itiraf etmektedir: $h\nu$'nün enerji olabilmesi için bir süre şarttır; süresi olmayan noktasal bir cisim bu formülü **bozduramaz**. *(Sürenin sahibinin adı teoride bellidir: alıcı penceresi $\tau$; $E=\delta\cdot(\nu\tau)$ yazıldığında $\nu$'deki "saniye başına", $\tau$'nun saniyesiyle sadeleşir ve geriye saf sayım kalır — 9.2.2. Hesap 9.10.11'de.)*

## 9.10.4 Hilbert Uzayı Sınavı: Frekansı Belli "Tek Foton" Bir Durum Bile Değildir

Fourier sınırının operatör dilindeki karşılığı daha da serttir. Sürekli modda alan operatörleri $[\hat a(\omega),\hat a^\dagger(\omega')]=\delta(\omega-\omega')$ cebirini taşır; "frekansı $\omega$ olan tek foton" yazılmak istendiğinde:

$$|1_\omega\rangle=\hat a^\dagger(\omega)|0\rangle \quad\Longrightarrow\quad \langle 1_\omega|1_\omega\rangle=\delta(0)=\infty$$

Norm ıraksar: bu ifade Hilbert uzayında bir durum **değildir**. QED'in kendi kitabına göre fiziksel olan tek şey dalga paketidir:

$$|1_f\rangle=\int d\omega\, f(\omega)\,\hat a^\dagger(\omega)|0\rangle,\qquad \int|f(\omega)|^2 d\omega=1,\qquad \Delta\omega>0\ \text{zorunlu}$$

Ama o zaman "onun frekansı" diye bir nitelik yoktur; enerji de özdeğer değil, **beklenen değerdir**: $\langle E\rangle=\int|f(\omega)|^2\hbar\omega\,d\omega$. Sonuç kelimesi kelimesine kaydedilmelidir: **$E=h\nu$'nün sahibi olacak nesne, o formülü bayrak yapan kuramın durum uzayında mevcut değildir.** N-1+N-2 çifti (bölünmez ve frekansı belli tek kuantum) ancak normalize edilemeyen, tüm uzayı kaplayan bir düzlem dalga modu olarak "var"dır — ve tüm uzayı kaplayan şey ne üretilebilir, ne bir dedektöre varabilir.

## 9.10.5 Yerleşiklik Yasağı: Hiçbir Yerde Olamayan Nesne

Üç bağımsız teorem, N-3'ün (yerleşiklik) kapısını üç ayrı kilitle kapatır.

**(a) Konum operatörü yoktur.** Newton ve Wigner'in yerelleştirilebilirlik analizi (Newton & Wigner, 1949) ve Wightman'ın aksiyomatik keskinleştirmesi (Wightman, 1962): kütlesi sıfır, spini 1 olan parçacık için konum operatörü **tanımlanamaz**. Fotonun $|x\rangle$ durumu, $\psi(x)$ dalga fonksiyonu, konum olasılık yoğunluğu yoktur. "Foton $x$ noktasına çarptı" cümlesi, kuramın matematiğinde **yazılamaz** bile — oysa "foton"un bütün deneysel kanıtı tam olarak bu cümledir: ekrandaki nokta, dedektördeki klik.

**(b) Sonlu sayıda kuantum hiçbir bölgeye hapsedilemez.** Kesin yerleşiklik teoremi (Knight, 1961; tam karakterizasyon Licht, 1963): parçacık sayısı sonlu olan **hiçbir** durum, bir bölgenin dışında vakumdan ayırt edilemez olacak şekilde hazırlanamaz. Tek fotonun ($N=1$) korelasyon fonksiyonları uzayın **her yerinde** vakumdan farklıdır — "burada, başka yerde değil" diyemez. Teoremin ters yüzü daha da öğreticidir: kesin yerleşik durumlar yalnız **sonsuz kuanta süperpozisyonlarıdır** (koherent durumlar bu sınıftandır). Yani gerçekten sınırlı, cephesi olan her ışık atımı, zorunlu olarak bütün $N$'lerin süperpozisyonudur — kaynaktan çıkan gerçek sinyal hiçbir zaman $|1\rangle$ değildir. Kuramın kendi hükmü şudur: *gerçekten bir yerde olan ışık, sayılabilir tek mermi gibi değil, süreklilik gibi davranır.*

**(c) Yerleştirmeye çalışan, nedenselliği bozar.** Hegerfeldt teoremi (Hegerfeldt, 1974; 1998): enerjinin alttan sınırlı olması tek başına yeter — başlangıçta bir bölgeye (yaklaşık bile) yerleştirilen durum, evrimde **anında** tüm uzaya yayılır. Bialynicki-Birula bu sınırı Paley–Wiener teoremiyle keskinleştirdi (Bialynicki-Birula, 1998; Bialynicki-Birula & Bialynicka-Birula, 2009): foton enerji yoğunluğu en iyi ihtimalle üstel kuyrukla yerleşebilir, o yerleşme de zaman evriminde derhâl bozulur.

Dürüst kayıt: Hegerfeldt sonucunun yorumu (ani yayılmanın "paradoks" statüsü) literatürde tartışmalıdır; bölümün yaslandığı çekirdek, tartışmasız olan kısımdır — sonlu-$N$ durumlarının kesin yerleşemezliği (b) ve konum operatörünün yokluğu (a) teorem düzeyindedir. N-1+N-3 çifti (sayılabilir-tek **ve** bir yerde) matematiksel olarak kapalıdır.

## 9.10.6 Elde-Edilemezlik Zinciri: Hiçbir Kaynaktan Çıkmaz

Önceki üç sergi nesnenin **var olamayacağını** gösterdi; bu sergi, var olsaydı bile **elde edilemeyeceğini** gösterir — üç ayrı no-go ile.

**(a) Zayıflatma teoremi: klasik ışık asla tek foton olmaz.** Her zayıflatıcı (filtre, mesafe, ışın bölücü) aynı dönüşümü uygular: $\hat a\to\sqrt{\eta}\,\hat a+\sqrt{1-\eta}\,\hat v$. Bunun iki cebirsel sonucu vardır: koherent durum koherent kalır ($|\alpha\rangle\to|\sqrt{\eta}\,\alpha\rangle$), termal durum termal kalır ($\bar n\to\eta\bar n$) — durumun **sınıfı** hiçbir zayıflatmayla değişmez, Fock durumuna dönüşmez. Ve $g^{(2)}=\langle\hat a^\dagger\hat a^\dagger\hat a\hat a\rangle/\langle\hat a^\dagger\hat a\rangle^2$ oranında pay $\eta^2$, payda $\eta^2$ ile ölçeklenir: **istatistik karakteri kayıp altında değişmezdir** — termal ışığın $g^{(2)}=2$'si katrilyon kat kısmada da 2'dir. Sayısal vuruş: Poisson ışığında $P(2)/P(1)=\mu/2>0$ her şiddette; ortalaması $\bar n=1$ olan termal ışıkta ise $P(0)=\tfrac12$, $P(1)=\tfrac14$, $P(n\geq2)=\tfrac14$. **"Aygıtta ortalama bir foton" ≠ "tek foton."** Hüküm: Taylor'ın mum deneyinden (Taylor, 1909) gerçek anti-korelasyon ölçümlerine (Grangier ve ark., 1986) kadar geçen yaklaşık seksen yılın **bütün** "zayıf ışık" deneyleri klasik kaynak kullandı; dolayısıyla matematiksel kesinlikle hiçbirinde tek foton yoktu.

**(b) Üretim no-go'su: gerçek kaynaklar saf $|1\rangle$ veremez.** Süreç süreç:

- *Kendiliğinden salınım* (atom, kuantum nokta) — Wigner–Weisskopf çözümü: $|\psi(t)\rangle=c(t)|e,0\rangle+\int d\omega\,g_\omega(t)|g,1_\omega\rangle$ ve $|c(t)|^2=e^{-\Gamma t}>0$ her sonlu $t$'de. Atomda daima uyarım genliği kalır; alan durumu daima vakum bileşeni taşır. Saf tek-foton paketi yalnız $t\to\infty$ limitinde vardır — **"tek foton" bir asimptottur ve asimptot elde edilmez, ona yakınsanır.** Üstel paketin sonsuz kuyruğu, 9.10.5'in yerleşiklik yasağıyla birebir tutarlıdır.
- *Müjdelenmiş SPDC* (modern "tek foton" kaynaklarının çoğu; habercili hazırlama: Hong & Mandel, 1986): kaynak durumu iki-mod sıkıştırılmış vakumdur, $|\psi\rangle=\sqrt{1-\lambda^2}\,\sum_n\lambda^n|n,n\rangle$. Müjde kliki geldiğinde öteki kolda **her zaman** $\propto\lambda^2$ mertebesinde çok-çift bulaşması vardır; bulaşmayı bastırmak ($\lambda\to0$) üretim hızını sıfıra götürür. **Saflık × verim değiş-tokuşu cebirseldir**; ikisi birden 1 olamaz.
- *Sonlu uyarım atımı:* atım süresi sıfır olamayacağından, salınım yapan atomun aynı atım içinde yeniden uyarılma olasılığı sıfır değildir — iki-foton genliği daima vardır.

Her gerçek kaynağın çıktısı $\rho=p_0|0\rangle\langle0|+p_1|1_f\rangle\langle1_f|+p_2\rho_2+\dots$ biçimindedir; $p_0>0$ ve $p_2>0$ **kesinlikle**. Bu tespit marjinal bir itiraz da değildir; güncel literatür aynı sınırı ad koyarak inceler ve hükmü kendi diliyle verir: tam tek fotonlar, sonsuz kuyrukları nedeniyle istem üzerine üretilemez (Gulla ve ark., 2023).

**(c) Ölçüt analizi: deney "tek foton"u zaten seçemez.** "Tek foton ürettik" iddiasının operasyonel ölçütü $g^{(2)}(0)<\tfrac12$'dir. Ama klasik sınır $g^{(2)}(0)\geq1$'in ispatı bir varsayıma dayanır: klik olasılığının, pozitif dağılımlı **stokastik bir şiddet alanıyla** orantılı olması ($\langle I^2\rangle\geq\langle I\rangle^2$). Bütünsel yönlendirme mekaniği — dilimin tek kolu seçmesi (2.6.5, 9.7.2, 9.9.3) — bu varsayım sınıfının dışındadır ve $g^{(2)}(0)\approx0$'ı Fock durumu olmadan üretir. Yani anti-demetlenme ölçümü **"klasik stokastik alan değil"i ispatlar, "tek foton var"ı değil**: iki ontoloji aynı istatistiği verir, ölçüt aralarında karar veremez.

## 9.10.7 Aygıt Denetimi: "Tek Foton" Gören Sensör Yoktur, Attığını Kanıtlayan Kaynak da

9.10.6 elde-edilemezliği cebirle gösterdi; bu bölüm aynı hükmü ölçüm mühendisliğinin kendi belgeleriyle mühürler. Yöntem değişmez: aşağıdaki her sayı, sensör üreticilerinin veri sayfalarından ve endüstrinin kendi standart denklemlerinden alınmıştır. Denetimin sonucu tek cümledir: **yüz yılın bütün ışık sensörleri iki mimariden birindedir — biriktiren kova ya da eşikli kapan — ve ikisi de "tek foton"la değil, birikimin eşiği aşmasıyla çalışır.**

### 9.10.7.1 Kova Mimarisi: CCD ve CMOS — Endüstrinin Kendi Denklemi

Her görüntü sensörü pikseli, endüstrinin kendi terimiyle bir **kuyudur** (full well): poz boyunca fotoelektronlar kuyuda birikir, poz sonunda kuyu okunur. Okuma işlemi gürültülüdür ve alanın standart karakterizasyon yöntemi (foton transfer eğrisi: Janesick, 2007) her şeyi elektron cinsinden sayar. Endüstrinin sinyal-gürültü denklemi:

$$\mathrm{SNR}=\frac{\eta N}{\sqrt{\eta N+\sigma_{ok}^{2}+D\,t}}$$

($\eta$ kuantum verimi, $N$ piksele düşen foton sayısı, $\sigma_{ok}$ okuma gürültüsü, $Dt$ karanlık akım birikimi). Bugünün en iyi ticari bilimsel sensörlerinden Sony IMX455'in üretici değerleri: okuma gürültüsü $\sigma_{ok}\approx1{,}1$ e⁻, kuyu kapasitesi ~51 000 e⁻ (Sony Semiconductor, 2020). Denklem bu en iyi durumda bile şunu verir ($\eta=0{,}8$, $Dt\approx0$):

- **Fark edilebilirlik** (SNR = 1): $\eta N\approx1{,}7$ → $N\approx2$ foton — ve bu "tespit" değil, gürültüyle başa baş olmaktır;
- **Güvenilir tespit** (endüstri eşiği SNR = 5): $\eta N\approx26$ → $N\approx33$ **foton/piksel**;
- **Normal pozlama** (kuyunun dolması): ~50 000 e⁻ → $N\approx6\times10^{4}$ foton/piksel.

Aynı hesap saha pratiğiyle çakışır: bir kameranın "minimum aydınlanma 0,1 lux" beyanı, sensör düzleminde 3,76 µm'lik piksele 30 kare/s'de kare başına ≈190 foton demektir (555 nm'de 1 lux = $4{,}1\times10^{15}$ foton·s⁻¹·m⁻²). Kova mimarisinin hükmü nettir: tek foton, en iyi sensörün okuma gürültüsünün **altındadır**; "görüntü" denilen şey, piksel başına onlarca ile on binlerce merminin birikimidir.

### 9.10.7.2 Kapan Mimarisi: PMT, SPAD, SNSPD — "Tek Foton Sayıcı"ların Anatomisi

"Tek foton dedektörü" adıyla satılan bütün aygıtlar ikinci mimaridedir: **yarı-kararlı bir sistem eşiğin hemen altına kurulur ve herhangi bir pertürbasyonla çığ boşalır.** Üreticilerin kendi sayıları:

| Aygıt | Üretici verisi | Ne yapar |
|---|---|---|
| **PMT** (fotoçoğaltıcı) | fotokatot QE zirvede tipik %25–35; dinot kazancı $10^{6}$–$5\times10^{6}$; karanlık sayım yüzlerce klik/s (Hamamatsu, 2007) | fotokatottan kopan **bir elektron**, ~1 kV'luk dinot merdiveninde milyonlarca elektrona çoğaltılır; ayrımcı eşiğini aşan darbe "klik" sayılır |
| **SPAD** (Geiger-modu çığ diyodu) | zirve tespit verimi >%70 (yalnız 650 nm'de); karanlık sayım 25–1500 klik/s (sınıfa göre); ölü zaman 22 ns; aşırı-ışık koruma devresi (Excelitas, 2023) | kırılma geriliminin **üzerine** kutuplanmış diyot; tek taşıyıcı, $10^{7}$–$10^{8}$ taşıyıcılık kendi kendini besleyen çığı tetikler |
| **SNSPD** (süperiletken nanotel) | sistem verimi ~%90+; 1–3 K kriyojenik zorunlu; karanlık sayım düşük ama sıfır değil (Eisaman ve ark., 2011) | kritik akımın hemen altında tutulan nanotelde yerel süperiletkenlik çöker; bias akımı şönte boşalır |
| **qCMOS** | okuma gürültüsü 0,27 e⁻; piksel başına bireysel kalibrasyon + gerçek-zamanlı düzeltmeyle "foton sayısı çözme" (Hamamatsu, 2022) | ölçtüğü basamak **elektron** basamağıdır — alıcı yükünün merdiveni; sayı merdiveninin adresi yine alıcıdır (9.7.2/G-2) |

Bu tabloda üç imza vardır ve yüz yıllık gelişmeye rağmen **hiçbir aygıtta sıfırlanamamıştır**:

1. **Kayıp:** verim birden küçüktür — standart modelin kendi muhasebesiyle, "bölünmez ve tek başına yeterli" mermilerin %30–75'i **hiçbir iz bırakmadan** yok olur. En iyi SPAD bile klik başına ortalama ≥1,4 foton "harcar"; PMT 3–4 harcar.
2. **Karanlık klik:** her aygıt ışık yokken de klikler — saniyede onlarcadan binlerceye. Klik bir foton sertifikası değildir; eşiğin aşıldığının kaydıdır ve eşik termal pertürbasyonla da aşılır.
3. **Enerji defteri:** klik olarak okunan darbenin enerjisi ışıktan gelmez. PMT'de darbe başına besleme kaynağından çekilen enerji ~$10^{-10}$ J mertebesindedir; "tetikleyen fotonun" enerjisi ~$5\times10^{-19}$ J'dür — **klik enerjisinin ışıktan gelen payı milyarda bir mertebesindedir.** Işık, en iyi ihtimalle, boşalmaya kurulmuş bir kapanın tetiğine dokunur; kapanı boşaltan, güç kaynağıdır.

### 9.10.7.3 Kalibrasyon Döngüselliği: "%70 Verim" Nasıl Ölçülür?

Verim beyanının kendisi de denetlenmelidir. Ulusal metroloji zincirinde tek-foton dedektör verimi şöyle kalibre edilir: güç ölçerle mikrowatt düzeyinde ölçülen bir lazer, kalibre zayıflatıcılarla pikowatt altına indirilir ve **foton akısı, ölçülen gücün $h\nu$'ye bölünmesiyle hesaplanır**; verim = klik sayısı / hesaplanan akı (Eisaman ve ark., 2011). Zincirin hiçbir halkasında foton **sayılmaz**: "gelen foton sayısı", watt cinsinden ölçümün $E=h\nu$ muhasebesine bölümüdür. "Tek foton" burada ölçümün girdisi değil, **defter çıktısıdır** — aygıtların gerçekten gördüğü şey güç ve kliklerdir.

### 9.10.7.4 En Hassas Dedektör Dahil: Göz ve Fotoelektrik Çağının Aygıtları

Biyolojinin dedektörü de aynı denetimden geçer. Görme eşiğinin klasik ölçümü (Hecht ve ark., 1942): algı için korneaya **54–148 kuantum**, retinada ~500 çubuk hücrelik alana **5–14 soğurulma** gerekir. Tek "foton" görülmez; çubuk hücresi de biyokimyasal bir kapandır — tek izomerizasyon, enerjisi hücrenin kendi metabolizmasından gelen bir enzim çığıyla yükseltilir. Fotoelektrik çağının aygıtları ise kova mimarisinin en kabasıydı: Millikan'ın elektrometre/galvanometre okumaları en iyi ihtimalle ~$10^{-11}$ A duyarlıklıdır — saniyede ~$6\times10^{7}$ elektronluk **toplam akım**; metallerin verimiyle foton tarafı ~$10^{11}$–$10^{12}$ foton/s eder. "Tek foton bir elektron söker" cümlesinin doğduğu laboratuvarda tek olay hiç gözlenmedi; okunan şey daima yığın akımıydı (9.10.8'in fire muhasebesiyle aynı kayıt).

### 9.10.7.5 Kanonik Deneylerin Dedektör Envanteri: Kanıt Zincirinin Son Halkası

Denetim son olarak "tek foton"un kurucu deneylerine döner ve tek soru sorar: **iddiayı taşıyan klikleri hangi aygıt üretti — ve o aygıtın kendi belgesi ne diyor?**

| Deney (taşıdığı iddia) | Dedektörü | Aygıtın kendi kaydı |
|---|---|---|
| Taylor 1909 (zayıf ışıkla girişim) | fotoğraf plakası | gümüş halojenür tanesi gelişebilir hâle gelmek için **en az 3–4 soğurma** ister, pratikte hayli fazlasını (Mees, 1942); poz süresi aylardır — plaka, kova mimarisinin en yavaşıdır |
| Kimble–Dagenais–Mandel 1977 (anti-demetlenme) | fotoçoğaltıcılar | QE ≤ %30, kazanç $10^{6+}$, karanlık sayım > 0 (9.10.7.2): klik, besleme kaynaklı çığdır |
| Aspect ve ark. 1982 (Bell ihlali) | fotoçoğaltıcılar | çiftlerin ezici çoğunluğu hiç tespit edilmez; $S$ değeri, elenen olayların istatistiğinden gelir (9.7.4/Katman 1) |
| Grangier–Roger–Aspect 1986 ("foton aynada bölünmedi") | fotoçoğaltıcılar | tetiklerin ezici çoğunluğunda **hiçbir dedektör klik vermez**; "bölünmezlik", kliksiz olaylar denizinden ayıklanan koinsidans oranıdır ($\alpha$ parametresi) |
| Hensen ve ark. 2015 (boşluksuz Bell) | SPAD sınıfı çığ diyotları | 9.10.7.2'nin kapanı; foton toplama o kadar verimsizdir ki protokol "event-ready" ön filtreye mecburdur |
| Lita ve ark. 2008 (sayı merdiveni) | TES kalorimetre | ölçtüğü basamak enerji/yük basamağıdır; "%95 verim" $P/h\nu$ kalibrasyonludur (9.10.7.3) |
| bugünün kuantum optik laboratuvarı | neredeyse istisnasız SPCM ailesi (Excelitas) | 9.10.7.2'de denetlenen veri sayfasının ta kendisi: verim < 1, karanlıkta 25–1500 klik/s, ölü zaman 22 ns |

Envanterin vurucu tespiti — dürüst kaydıyla birlikte: makaleler dedektörlerini **saklamaz**; sınıfını, çoğu zaman markasını da verir. Saklanan şey daha incedir: **hiçbir makalede, kullanılan dedektörün "tek foton ölçtüğünü" belgeleyen tek bir satır yoktur — olamaz da, çünkü aygıtların kendi veri sayfalarında böyle bir kalem tanımlı değildir.** Veri sayfasının tanımladığı nicelikler bellidir: tespit verimi ($P/h\nu$ kalibrasyonlu istatistiksel oran), karanlık sayım, ölü zaman, art-atım olasılığı. "Single Photon Counting Module" adındaki "single photon" **ürün adıdır**; spesifikasyon tablosunda "tek fotonu birim doğrulukla kaydeder" diye bir satır yoktur ve hiçbir üretici böyle bir metrolojik taahhüt vermez. Deney makalesinde dedektör, yöntem bölümünde bir cümledir; verimi dipnottadır; "ışık bölünmez fotonlardan oluşur" hükmü ise başlıktadır. Kanıt zinciri eksiksiz yazıldığında kendini imha eder:

$$\text{iddia ("tek foton")} \;\leftarrow\; \text{istatistik (koinsidans oranları)} \;\leftarrow\; \text{klik (eşik aşımı)} \;\leftarrow\; \text{kapan/kova (verim}<1\text{, karanlıkta klik)} \;\leftarrow\; \text{"tek foton ölçer" ibaresi: hiçbir belgede yok}$$

Zincirin hiçbir halkasında tek foton **ölçülmez**; ilk halkadaki iddia, son halkada varsayılandır.

### 9.10.7.6 Kaynak Tarafı ve Hüküm

Önce dedektör denetiminin bilançosu tek tabloda toplanır — son sütun, standart modelin **kendi** sayılarıyla "bir sinyal kaç foton ister" sorusunun cevabıdır:

| Aygıt | Sinyal tanımı | Gereken foton |
|---|---|---|
| CMOS/CCD (Sony IMX455) | güvenilir piksel tespiti (SNR = 5) | ~33; normal pozlamada ~$6\times10^{4}$ |
| Kamera saha beyanı | "0,1 lux minimum aydınlanma" | ~190 /piksel·kare |
| PMT (Hamamatsu) | ayrımcı üstü klik | ortalama 3–4; karanlıkta **0 fotonla** yüzlerce klik/s |
| SPAD (Excelitas) | çığ kliki | ortalama ≥1,4 (yalnız zirve dalga boyunda); karanlıkta **0 fotonla** 25–1500 klik/s |
| Fotoğraf plakası (Taylor 1909'un dedektörü) | gelişebilir tane | tane başına ≥3–4 soğurma; pratikte hayli fazlası (Mees, 1942) |
| İnsan gözü (Hecht ve ark., 1942) | görme algısı | korneada 54–148 |
| Millikan'ın galvanometresi | okunabilir fotoakım | ~$10^{11}$–$10^{12}$ foton/s |

Tablonun okunuşu: "tek fotonla çalışan" hiçbir satır yoktur; sıfır fotonla çalışan satırlar vardır.

Kaynaklar aynı aynadadır. Metroloji tabanı pikowatt'ta durur — 550 nm'de 1 pW bile saniyede $2{,}8\times10^{6}$ mermidir; "saniyede bir foton" iddialı bir kaynak $3{,}6\times10^{-19}$ W'tır ve hiçbir güç ölçerin göremeyeceği bu düzeyin tek "kanıtı", yukarıda anatomisi çıkarılan eşikli kliklerin istatistiğidir — döngü kapanır. "Tek foton kaynağı" olarak satılan aygıtların (kuantum nokta, renk merkezi, müjdeli SPDC) uçtan uca bilançosu da aynıdır: tetik başına tespit olasılığı tipik %1–50, müjde verimi tipik %10–80 (Eisaman ve ark., 2011) — "tek foton üretildi" denilen olayların çoğunda hiçbir şey tespit edilmez ve sayım, kayıpların Poisson muhasebesiyle geri doldurulmasıyla yapılır; kalan boşluğu 9.10.6(b)'nin cebiri kapatır: $p_0>0$, $p_2>0$ her zaman.

Hüküm iki cümledir. **Mühendislik cümlesi:** yüz yılda iki mimari icat edilebildi — biriktiren kova, eşikli kapan; üçüncüsü yoktur. İkisi de "tek foton"u değil, **birikimin eşiği aşmasını** ölçer; "tek foton dedektörü" ticari addır, ölçüm tanımı değildir. **Teori cümlesi:** bu tablo, teorinin alıcı mekaniğinin mühendislikteki aynasıdır — kova = pencere birikimi ($N=\nu\tau$ vuruş), kapan = eşikli kopma ($h=\delta\tau$ ısırığı). Sensör endüstrisi, "tek foton"u yakalamaya çalışırken farkında olmadan hep aynı şeyi inşa etti: **alıcı penceresini.**

Dürüst kayıt: standart fiziğin cevabı "verim, gürültü ve karanlık sayım ilkesel değil, mühendislik kusurudur" olacaktır. Kayda üç katman geçirilir: (i) dokuz mertebelik teknolojik iyileşme üç imzanın hiçbirini sıfırlayamadı; sıfırlanacağına dair bir yol haritası da yoktur; (ii) "verim"in tanımı döngüseldir — foton akısı hiç sayılmadan $P/h\nu$ ile hesaplanır (9.10.7.3); (iii) en derinde, 9.10.4–9.10.5'in teoremleri "tek foton"un durum olarak zaten üretilip yerleştirilemeyeceğini söyler — mühendislik verisi, o teoremlerin laboratuvar yüzüdür.

## 9.10.8 Fotoelektrik Yüzleşme: Hiç Atılmamış "Tek Foton" ve Fire Muhasebesi

"Foton"un doğum belgesi sayılan fotoelektrik olayın kendi kaydı, iddianın iki temelini birden çürütür.

**Tarihsel kayıt:** 1887–1916 arasının bütün fotoelektrik deneyleri (Hertz, Lenard, Millikan) ark lambaları ve cıva çizgileriyle yapıldı — saniyede $10^{12}$–$10^{15}$ mermilik akılar. "Tek foton bir elektron söker" cümlesi tek fotonla **hiç sınanmadı**; 9.10.6(a) gereği sınanamazdı da: zayıflatılmış klasik ışık asla tek foton değildir. Foton anlatısının kuruluş belgeleri, iddiasını test etmemiş deneylerdir.

**Fire muhasebesi:** 254 nm cıva çizgisinde mermi başına 4,9 eV düşer; mütevazı 1 mW'lık huzme saniyede $1{,}3\times10^{15}$ adet "bölünmez, tam enerjili, tek başına yeterli" mermi demektir. Bir foton = bir elektron ise fotoakım $\approx0{,}2$ mA olmalıdır. Ölçülen kuantum verimi: teknik metal yüzeylerde $10^{-6}$–$10^{-7}$, en temiz koşullarda $10^{-4}$–$10^{-3}$. Saniyede katrilyon yeterli merminin **milyonda biri** iş yapar.

Dürüst kayıt ve asıl vuruş: standart fiziğin fireye cevabı vardır — yansıma, soğurma olasılığı, elektronun yüzeye ulaşamaması. Ama bu cevabın **her kalemi dalga aygıtından ithaldir**: yansıma Fresnel katsayısıyla (Maxwell), soğurma tesir kesitiyle (pertürbasyon hesabı — yine alan/dalga matematiği) hesaplanır. "Nokta mermi" anlatısı, klik anı dışında **hiçbir nicel soruya kendi diliyle cevap veremez**; bölünmezlik iddiası ile %99,9999 fire aynı ağızdan savunulur ve firenin mekanizması foton dilinde yazılamaz. İkinci bıçak "hangi elektron?" sorusudur: cm²'lik katot yüzeyine yayılmış dalga cephesi, femtosaniyeler içinde $10^{23}$ elektrondan tekine mekanizmasız "çöker" — ölçüm problemi her fotoelektrik olayın içine gömülüdür. *(Verimin mekanik muhasebesi teoride kurulmuştur: tek elektron tek katarla etkileşir, oranlar $\eta$–pencere–paralel katar sayısından çıkar — 9.4.2.)*

## 9.10.9 Nesne Muhasebesinin İflası: Defterlere Bölünen Nitelikler

Gerçek bir cismin momentumu, sayısı, boyutu ve kimliği, onu izleyen defterden bağımsızdır. "Foton"unkiler değildir:

| Nitelik | Standart kayıt | Hüküm |
|---|---|---|
| **Momentum (boşlukta)** | kütlesi tam sıfır, momentumu sıfır değil ($p=E/c$); itme gerçekten ölçülür (Lebedew, 1901; Nichols & Hull, 1903; uzayda güneş yelkeni: Tsuda ve ark., 2011) ve hesap tutarlıdır — 2.2.1'in açıkça teslim ettiği üzere. Ama momentumun **taşıyıcısı** sorusu soyut alan kavramına havale edilir; ortada eylemsizliği olan hiçbir şey yoktur | momentumu ölçülen ama ataleti olmayan "cisim" formülde yaşar, mekanikte değil (2.2.1, 2.3.8) |
| **Momentum (ortamda)** | Minkowski $n h\nu/c$ ↔ Abraham $h\nu/nc$ (Minkowski, 1908; Abraham, 1909): aynı "foton"a $n^2$ çarpanı farklı iki momentum; yüz yıllık açmaz. "Çözüm" (Barnett, 2010): ikisi de doğru — biri "kinetik", öteki "kanonik" defterde (ikiliğin kitaptaki kaydı: 2.4.2) | momentumu defter seçimine bağlı olan şey cisim değildir |
| **Sayı** | ivmeli gözlemci, eylemsiz gözlemcinin vakumunda termal "foton" banyosu görür (Unruh, 1976); sayı gözlemcinin ivmesine bağlıdır | varlığı gözlemcinin hareketine bağlı olan şey cisim değildir |
| **Boyut** | saçılma kesitleri "noktasal" der ($<10^{-18}$ m); koherans ölçümleri km'ye çıkar — aynı "nesne" için 20+ mertebe aralık | boyutu deneyin sorusuna göre 20 mertebe oynayan şey cisim değildir |
| **Kimlik** | QED tanımında "foton" bir modun uyarımıdır; mod, deneycinin kurduğu sınır koşullarının (kovuk, ayna) fonksiyonudur | kimliği, etrafına kurulan kutuya bağlı olan şey cisim değildir |
| **Özzaman** | kütlesiz nesnenin durgun çerçevesi yoktur; null dünya çizgisinde özzaman sıfırdır — 13 milyar yıllık yolculuk "onun için" tek andır | zamanı hiç akmayan, yeri hiç olmayan yolcu, yolcu değildir |

Tablonun her satırı tek başına yorumlanabilir bir tuhaflıktır; altısı birden tek kavram üstünde toplandığında tanı netleşir: nitelikleri deftere göre değişen şey **nesne değil, defterin kendisidir**.

## 9.10.10 Tarihsel Tanıklar: Kürsüde Standart Fiziğin Devleri

Bu iddianame dışarıdan bir saldırı değildir; kavramın kurucuları ve en yetkili kullanıcıları aynı ifadeyi baştan beri vermektedir.

- **Planck** kuantalamayı ışığa değil **duvara** yazdı ve foton fikrine yıllarca direndi; 1913'te Einstein'ı Prusya Akademisi'ne önerirken ışık kuantumu spekülasyonunda "hedefi ıskalamış olmasının ona karşı sayılmamasını" rica ediyordu (akt. Pais, 1982). Teorinin 9.2.4 tespitiyle aynı hüküm: Planck'ın ilk adresi doğruydu.
- **Millikan**, $h$'yi %0,5 hassasiyetle ölçtüğü makalenin içine şu cümleyi koydu: Einstein'ın denklemine kendisiyle ulaştığı yarı-korpüsküler kuram "bugün tamamen savunulamaz görünmektedir" (Millikan, 1916). Eğimi doğrulayan adam, mermiyi reddediyordu — eğim mermiyi kanıtlamaz ve bunu, eğimi ölçen kişi de biliyordu.
- **Bohr**, fotona 1924'ün BKS kuramına kadar direndi (9.4.6); koinsidans deneyleri BKS'nin istatistiksel korunumunu öldürdü ama fotonun yerleşiklik problemine tek satır çözüm getirmedi.
- **Wentzel** (1926) ve **Lamb & Scully** (1969), fotoelektrik olayı ışık **klasik dalga** + alıcı kuantumlu alarak eksiksiz türettiler — eşik, doğrusallık ve gecikmesizlik dahil. "Foton"un birinci kanıtı sayılan olgu, foton olmadan hesaplanır; kesikliliğin adresi alıcıdır — standart fiziğin kendi yarı-klasik hesabı, 9.2.1'in adres tespitini teyit eder.
- **Schrödinger** (1927), Compton kaymasını geri tepen elektrondan çift Doppler olarak türetti — 9.4.4'te mekanizma olarak iş gören hesabın kendisi.
- **Lamb**, QED'in kalbi olan Lamb kaymasının Nobelli sahibi, kariyerinin muhasebesini "Anti-photon" başlıklı makaleyle kapattı (Lamb, 1995): "foton diye bir şey yoktur" — kavramı fizikçilere sevdiren şeyin bir hatalar komedisi ile tarihsel kazalar olduğunu yazdı ve kelimenin kullanımının lisansa bağlanmasını önerdi.
- **Einstein**, kavramın babası, 1951'de Besso'ya elli yıllık bilinçli kafa yormanın kendisini "ışık kuantası nedir" sorusunun cevabına bir adım bile yaklaştırmadığını, bildiğini sananların yanıldığını yazdı (Speziali, 1972).

Bu tanıkların hiçbiri Evrenakı savunucusu değildir; tanıklıkları bu yüzden daha değerlidir: **kavram, kendi evinde bile hiç oturmadı.**

## 9.10.11 İkilem Kilidi ve Teorinin Cevabı

Sergiler toplandığında standart fiziğin önünde iki kapı kalır:

**Kapı 1 — "Foton nesnedir."** O hâlde 9.10.3–9.10.9 doğrudan öldürür: frekansı belli noktasal cisim Fourier'e (9.10.3), bölünmez-frekanslı kuantum durum uzayına (9.10.4), yerleşik tek kuantum Knight–Licht'e (9.10.5) takılır; hiçbir kaynak onu üretemez (9.10.6), hiçbir aygıt onu tek başına ölçemez (9.10.7), fotoelektrikteki muhasebesi dalga aygıtından ödünçtür (9.10.8), nitelikleri defterlere bölünmüştür (9.10.9).

**Kapı 2 — "Foton nesne değil, kuantumlanmış alışveriş birimidir."** Bu, modern kuantum optiğin fiilî geri çekilme hattıdır ("mod uyarımı", "FAPP yerleşiklik", "yararlı idealizasyon"). Ama her geri çekilme bir itiraftır: üstel kuyruğu kabul etmek "fotonun sınırı yoktur" demektir; $|1\rangle$'in idealizasyon olduğunu kabul etmek "elde edilen şey hiçbir zaman tek foton değildir" demektir; mod diline çekilmek, ders kitaplarındaki mermi anlatısını — fotoelektriğin, Compton'un yüz yıllık öğretim dilini — feda etmektir. Ve kapının arkasında teori beklemektedir: **kuantumlanmış alışveriş biriminin mekanizmalı hali zaten kurulmuştur** — $h=\delta\tau$, pencere ısırığı; standart fiziğin tek "foton" kelimesi teoride iki gerçekliğe ayrışır: uçuş birimi **wake-kilitli katar dilimi**, ölçüm birimi **alıcı penceresinin ısırığı**; ikisi pencerelerin ortak evrensel $\tau$'su sayesinde aynı $h\nu$'de buluşur (9.2.1).

Sergilerin teori tarafındaki karşılıkları tek tabloda kapanır:

| Sergi (standart açmaz) | Teorideki çözüm |
|---|---|
| Fourier üçgeni: frekanslı nokta yok | ritim katarın malıdır; frekans enerjiye değil **sayıma** girer: $E=\delta\cdot(\nu\tau)$ (9.2.2) |
| $\delta(0)$: frekanslı tek kuantum durum değil | "frekanslı nesne" aranmaz; aralıklı katar vardır, $\nu=c/\lambda$ bir tanımdır (9.2.1) |
| yerleşiklik yasağı; "kesin yerleşik ışık = süreklilik" | nokta cisim yok; milimetrelerce dilim ($L=c\tau\approx4{,}5$ mm) + wake var — kuramın "süreklilik" hükmü katarın ta kendisidir (9.2.2) |
| zayıflatma tek foton üretmez | şiddet = paralel katar sayısı; kısma **sayıyı** düşürür, dilim bütün kalır (2.6.5, 9.7.2) |
| kaynak no-go: saf $|1\rangle$ çıkmaz | kaynak Fock durumu değil, Zerre Paketi (yayım birimi) atar; teslim kuantumu alıcıdadır (9.2.1) |
| fotoelektrik fire | tek katar–tek elektron, $\eta$, pencere: fire mekanik muhasebedir (9.4.2) |
| "tek foton dedektörü" klikleri | kova = pencere birikimi, kapan = eşikli kopma: sensör mimarileri $h=\delta\tau$ alıcı penceresinin mühendislik kopyasıdır (9.2.1, 9.7.2, 9.10.7) |
| gözlemciye bağlı sayı | "sayı" alıcı penceresinin ısırık sayısıdır; alıcıya bağlılık teoride tanım gereğidir, skandal değil |
| boyut aralığı (nokta ↔ km) | dilim boyu (mm) ile dilimler-arası wake-kilit korelasyonu (koherans) ayrı büyüklüklerdir (9.2.7/vi) |
| kütlesiz momentum (boşlukta) | taşıyıcı bellidir: kütleli Zerre ($m_z$, Postülat 4); ışınım basıncı, dolu yağışının çadırı itmesi gibi klasik momentum aktarımıdır (2.2.1, 2.3.8) |
| ortam momentumu (Abraham–Minkowski) | momentum katarın ve ortamın ortak defteridir; ilk-ilke türetim açık kalemdir (9.10.12/ii) |

Bölümün hükmü tek cümleye iner: **"tek foton" ancak $t\to\infty$'da, tüm uzaya yayılmış, asimptotik bir muhasebe satırı olarak yaşar — ve muhasebe satırı elde edilmez, yazılır.** Işığın kendisinde yaşayan şey ise katardır.

## 9.10.12 Açık Kalemler

Sergilerin hiçbiri teorinin hesabına borç yazmaz; aşağıdakiler, teori tarafındaki karşılıkların hesap kalemleridir (tümü 7.4 envanterine bağlanır):

i. **Bütünsel yönlendirme istatistiğinin nicel türetimi:** $g^{(2)}(0)\approx0$'ı üreten dilim/pencere mekaniğinin $\varphi$ dağılımından çıkarılması — 9.7.6/iv ile aynı kalem.
ii. **Ortam-içi momentum muhasebesi:** Abraham–Minkowski ikiliğinin, katar–girdap–ortam momentum alışverişinden teori-içi hesabı (9.1 Fizeau ve 9.4.8/i ile ortak cephe).
iii. **Dilim boyu ↔ koherans uzunluğu:** 9.2.7/vi ile aynı kalem; bu bölümde yalnız boyut-aralığı sergisinin çözüm adresi olarak anılmıştır.
iv. **İvmeli alıcı penceresi:** Unruh okumasının mekanik türetimi — ivmeli elektron-girdabın ortam karşısındaki pencere davranışı ve "termal klik" istatistiğinin bu davranıştan çıkarılması; yeni kalem.
v. **Karanlık sayımın teori-içi türetimi:** eşikli aygıtların ışıksız kliklerinin — termal tetiklerin — pencere mekaniği ve ortam basınç dalgalanmalarından nicel hesabı; kapan mimarisinin enerji defterinin (klik başına ~$10^{-9}$'luk ışık payı, çığ istatistiği) teori diliyle yeniden yazılması; yeni kalem.

---

**Bölüm özeti:** "Foton"a yüklenen üç nitelik — tek-sayılabilirlik, belirli frekans, yerleşiklik — ikişer ikişer bile bağdaşmaz: frekanslı nokta Fourier'le (9.10.3), frekanslı tek kuantum kuramın kendi durum uzayıyla (9.10.4: $\delta(0)$), yerleşik tek kuantum kesin yerleşiklik teoremleriyle (9.10.5: Newton–Wigner, Knight–Licht, Hegerfeldt) çelişir. Nesne var olamadığı gibi elde de edilemez: zayıflatma durumu sınıf değiştirmez, gerçek kaynaklar her zaman vakum ve çok-foton bileşeni taşır, deneysel ölçüt ($g^{(2)}$) iki ontolojiyi ayıramaz (9.10.6). Aygıt denetimi aynı hükmü üreticilerin kendi verileriyle mühürler: yüz yılın bütün sensörleri ya biriktiren kovadır ya eşikli kapan; verim birden küçük, karanlık klik sıfırdan büyük, klik enerjisinin ışıktan gelen payı milyarda bir mertebesindedir — "tek foton duyarlılığı" hiçbir aygıtta tanımlı bir ölçüm değildir ve verim kalibrasyonu foton saymadan, $P/h\nu$ defteriyle yapılır (9.10.7). Doğum belgesi sayılan fotoelektrikte "tek foton" hiç atılmamıştır ve fire muhasebesinin her kalemi dalga aygıtından ödünçtür (9.10.8); nesnenin momentumu (kütlesiz itmesi ve ortamdaki ikiliği), sayısı, boyutu ve kimliği defterlere bölünmüştür (9.10.9); kavramın kurucuları — Planck'tan Millikan'a, Lamb'den Einstein'ın kendisine — aynı ifadeyi baştan beri vermektedir (9.10.10). Geriye kalan tek savunma "foton nesne değil muhasebe birimidir" itirafıdır; o birimin mekanizmalı hali teoride zaten kuruludur: $h=\delta\tau$, uçuş tarafında wake-kilitli katar dilimi, ölçüm tarafında alıcı penceresinin ısırığı (9.10.11). Işıkta yaşayan katardır; "foton", pencerenin defterine yazılan bir satırdır — ve defter satırı elde edilmez, yazılır.
