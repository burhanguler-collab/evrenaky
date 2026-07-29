## Bölüm 6.5 — Galaktik Yörüngeler ve Karanlık Madde Probleminin Çözümü

Astrofiziğin son yüzyıldaki en büyük çözülemeyen gizemlerinden biri, galaksilerin dış kollarındaki yıldızların dönme hızlarıdır. Klasik Newton mekaniğine ve Einstein'ın Genel Görelilik teorisine göre, galaksinin merkezinden uzaklaştıkça kütleçekim kuvvetinin $1/r^2$ ile zayıflaması ve dolayısıyla yıldızların yörünge hızlarının düşmesi gerekir. Tıpkı Güneş Sistemimizde Güneş'ten uzaklaştıkça gezegenlerin daha yavaş dönmesi gibi.

Ancak 1970'lerde Vera Rubin ve meslektaşları tarafından yapılan hassas gözlemler, sarmal galaksilerin dış kollarındaki yıldızların hızının düşmediğini, aksine çok yüksek hızlarda **sabitlendiğini** (asimptota oturduğunu) kanıtlamıştır. Standart fiziğe göre bu hızlarda dönen yıldızların galaksiden kopup uzaya savrulması gerekirdi. Bu muazzam hızı dengede tutacak görünürde hiçbir kütle olmadığı için astrofizikçiler, galaksiyi devasa bir hale gibi saran görünmez bir kütle uydurmak zorunda kaldılar: **Karanlık Madde**.

Bu bölüm, Evrenakı teorisinin hiçbir "görünmez madde" varsayımına ihtiyaç duymadan, sadece kendi yerel mekanik postülatlarıyla bu kozmolojik anomalinin üstesinden nasıl geldiğini ve düz dönüş eğrilerini doğal yollarla nasıl türettiğini göstermektedir.

### 6.5.1 Kütleçekim Grafiği ve $1/r$ Kuvvetinin Yükselişi

Evrenakı teorisinde galaksi merkezlerindeki süper kütleli kara deliklerin dönüş hızları olağanüstü yüksektir. Teorinin temel postülatlarından olan **Eksenel İtim (F4)** ve ona bağlı hidrodinamik yansımalar, galaksi çekirdeğindeki bu devasa dönüşün (devrin) bir sonucudur.

Kritik nokta şudur: Klasik merkezcil kütleçekim $1/r^2$ profiliyle zayıflarken, teorinin öngördüğü eksenel kuvvet (Kısım 4'te türetildiği üzere) $1/r$ profiliyle sönümlenir. Galaksinin dış bölgelerine çıkıldıkça $1/r^2$'ye tabi klasik çekim hızla gücünü yitirir, ancak $1/r$ ile sönümlenen eksenel kuvvet profilde giderek baskın hale gelir. 

### 6.5.2 Matematiksel İspat: Düz Dönüş Eğrisinin Türetilmesi

Dairesel yörüngede dönen bir yıldızın dengede kalabilmesi için Merkezcil İvme'nin, kütleçekim ivmesi ile teorinin öngördüğü eksenel ivmenin toplamına eşit olması şarttır:

$$a_{merkezcil} = a_{kütleçekim} + a_{eksenel}$$

Terimleri kendi fiziksel bağımlılıklarıyla açtığımızda:
1. **Merkezcil İvme:** $\frac{v^2}{r}$
2. **Klasik Kütleçekim (Newton):** $\frac{GM}{r^2}$
3. **Eksenel Kuvvet (Evrenakı):** $\frac{K}{r}$ *(Buradaki K sabiti, merkezdeki süper kütleli kara deliğin devri ve galaktik çekirdeğin dönüş karakteristiği ile orantılıdır)*

Eşitliği kuralım:
$$\frac{v^2}{r} = \frac{GM}{r^2} + \frac{K}{r}$$

Denklemin her iki tarafını da yarıçap ($r$) ile çarptığımızda, yörünge hızı $v$ şu şekilde doğrudan elde edilir:
$$\mathbf{v = \sqrt{\frac{GM}{r} + K}}$$

Bu zarif ve kompakt denklemin sunduğu fiziksel sonuç son derece derindir:
Klasik fizikte $K=0$'dır; dolayısıyla yarıçap ($r$) büyüdükçe hız sıfıra yaklaşır. Ancak Evrenakı teorisinde, galaksinin çok uzak dış kollarına gidildiğinde ($r \to \infty$), $\frac{GM}{r}$ terimi sıfıra yaklaşsa dahi yıldızın hızı sıfıra düşmez. Hız doğrudan **$\sqrt{K}$** limitine, yani sabit bir asimptota kilitlenir.

Astronomların teleskoplarla gözlemlediği meşhur **"Düz Dönüş Eğrisi" (Flat Rotation Curve)** profili, teorik altyapıda hiçbir yama kullanılmadan, tamamen doğal yollarla elde edilmiştir.

### 6.5.3 Gerçek Gözlem Verileriyle Sınama

Bu matematiksel model ($v = \sqrt{A/r + B}$), evrendeki farklı galaksi türlerinin hassas teleskop ölçümleriyle test edildiğinde kusursuz bir ampirik başarı sergilemektedir. Aşağıdaki testlerde kırmızı kesik çizgiler saf Newton mekaniğini, mavi çizgiler ise Evrenakı teorisinin $1/r$ eklemli formülünü temsil etmektedir.

#### 1. Sarmal Galaksiler: M33 ve NGC 3198
Sarmal galaksiler, karanlık madde probleminin en belirgin gözlemlendiği yapılardır. 
M33 (Triangulum) galaksisinde Newton kütleçekimi hızla düşüşe geçerken, Evrenakı modeli ölçülen hızı ~120 km/s bandında kusursuzca yakalamaktadır. Benzer şekilde, dönüş eğrisinin 30 kpc gibi inanılmaz uzak mesafelere kadar dümdüz kalmasıyla bilinen devasa NGC 3198 galaksisinde, $1/r$ eksenel itim kuvveti yıldız hızlarını ~150 km/s bandında pürüzsüz bir doğrulukla kilitlemektedir.

![M33 Gözlem Testi](Gorseller/m33_gozlem_testi.png)
![NGC 3198 Gözlem Testi](Gorseller/ngc3198_gozlem_testi.png)

#### 2. Dev Eliptik Galaksiler: M87 ve NGC 4472
Eliptik galaksiler sarmal bir diske sahip olmadıkları için net dönüş eğrileri vermezler. Yıldızlar rastgele yörüngelerde bir arı kovanı gibi hareket eder (hız dağılımı). Ancak bu galaksileri saran devasa sıcak X-ışını gaz halelerinden hesaplanan kütleçekim potansiyelleri ("Efektif Dairesel Hız" $V_c$), sarmal galaksilerdeki asimptotik düz yapıyı birebir tekrar eder. 
Evrenin en meşhur dev eliptik galaksilerinden olan M87 ve NGC 4472'nin merkezlerinde korkunç hızlarda dönen süper kütleli kara delikler bulunur. Bu devasa çekirdek dönüşünden kaynaklı eksenel itim, galaksi eliptik de olsa formülün aynı mükemmellikte çalışmasını sağlar.

![M87 Eliptik Testi](Gorseller/m87_eliptik_testi.png)
![NGC 4472 Eliptik Testi](Gorseller/ngc4472_eliptik_testi.png)

#### 3. Cüce Küresel (Dwarf Spheroidal) Galaksiler: Derin Bir Fiziksel Öngörü
Fornax (Ocak) gibi cüce küresel galaksiler, evrendeki karanlık maddenin oransal olarak en yoğun bulunduğu düşünülen, sadece 1-2 kpc boyutlarındaki minicik yapılardır. Çok düşük kütlelerine rağmen efektif hız profilleri $\sim18$ km/s bandında asimptota oturur.
Evrenakı modeli bu galaksilerde de pürüzsüz çalışarak hızı dengeler. Ancak burada astrofiziğe karşı çok derin bir meydan okuma yatar: Güncel astronomiye göre cüce küresellerde süper kütleli kara delik **yoktur**. 
Bu durum, teori açısından iki muazzam öngörüden birine işaret eder:
1. Ya astronomi cüce küresellerin merkezindeki karanlıkta kalmış devri (ışıma yapmayan kütleli yapıları) henüz görememektedir.
2. Ya da bu $1/r$ yasası sadece spesifik bir kara delik devrinden ibaret değildir; bizzat Evrenakı'nın/uzay-zamanın kendiliğinden oluşturduğu daha temel ve fundamental bir topolojik girdap yapısından kaynaklanmaktadır.

![Fornax Küresel Testi](Gorseller/fornax_kuresel_testi.png)

### Sonuç
Evrenakı teorisinin kinematik denklemleri; sarmal, eliptik ve cüce küresel gözetmeksizin, dönen bir çekirdeğe sahip tüm galaktik yapılarda "Karanlık Madde" varsayımını tamamen ortadan kaldırmakta ve kütleçekim anomalisini kendi iç dinamikleriyle, saf matematiksel bir kesinlikle çözmektedir.
