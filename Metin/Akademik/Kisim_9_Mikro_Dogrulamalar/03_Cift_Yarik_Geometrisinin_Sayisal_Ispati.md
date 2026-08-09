# 9.3 Çift Yarık Geometrisinin Sayısal İspatı

Çift yarık deneyi, standart fizikte "dalga–parçacık ikiliğinin" tahtıdır; Kısım 2.8 bu tahtın mekanizmasını parçalarına ayırmıştı: kenar kırınımı bir gradyan bükmesidir, girişim bir yörünge-kesişme ve wake-yığılma düzenidir, "tek foton ile girişim" ifadesinin operasyonel içeriği tekil olayların istatistiğidir. Bu bölümün görevi o mekanizmayı yeniden anlatmak değil, **sayısını doğrulamaktır**: perde üzerindeki saçak aralığını veren $y=\lambda L/d$ bağıntısının, Evrenakı'daki gerçek bir wake alanının iki yarık ardındaki girişim geometrisinden nasıl elde edildiği gösterilir ve ölçümle karşılaştırılır.

> **Kapsam ve tamamlanma notu:** Bu bölüm bilinçli olarak **sınırlı kapsamla** yazılmıştır: ışık tarafı ve geometri katmanı. Derin katman — wake periyodunun ilk-ilke türetimi, madde (elektron) çift yarığının nicel istatistiği ve saçak-saçak Fresnel karşılaştırması — 9.3.6'nın açık kalemleri olarak 7.4 envanterine bağlıdır; bu kalemler kapandığında bölüm genişletilerek **tamamlanacaktır.**

## 9.3.1 Doğrulanacak Gözlem Envanteri

| # | Gözlem | Ölçülen değer / davranış | Kaynak |
|---|---|---|---|
| G-1 | Çift yarık saçakları | aralık $\Delta y=\lambda L/d$; $\lambda$ ile doğru, $d$ ile ters orantı bütün taramada | Young, 1804; standart optik |
| G-2 | Tek kenar (Fresnel) kırınımı | saçaklar **aydınlık tarafta**; ölçek $\sqrt{\lambda L}$ ile büyür | Fresnel, 1819; DENEY 4 (2.8.1) |
| G-3 | Seyreltilmiş kaynak | tekil tespit daima **tek nokta**; desen ancak binlerce tespitin istatistiğinde belirir | Tonomura ve ark., 1989 (~70.000 nokta) |
| G-4 | Hangi-yol ölçümü | yol bilgisi alındığında desen silinir | standart kuantum optik |

## 9.3.2 Girdiler: Katar, Wake, Tespit

Türetim üç girdiden yürür; üçü de kitabın başka yerlerinde kuruludur:

1. **Katar ve aralık (9.1–9.2):** ışık, aralığı $\lambda$ olan Zerre katarıdır; dilim tek koldadır.
2. **Wake alanı (2.6.5, 2.8):** dilimin önündeki wake yapısı **iki yarığı birden tarar**; iki yarık, aynı dilimin ($\varphi$'si ortak) beslediği **iki eş-fazlı wake kaynağına** dönüşür. Wake deseninin uzaysal periyodu, onu açan katarın Zerre aralığı $\lambda$'dır — bu bağ bu bölümde **girdi** olarak alınır; ilk-ilke türetimi açık kalemdir (9.3.6/i).
3. **Tespit (9.2):** ekrandaki her klik bir pencere olayıdır; Zerreler wake'in yapıcı çizgilerine kapılarak (wake-tüneli takibi, 2.8) varış adreslerini seçer.

## 9.3.3 Geometrik İspat: $y = \lambda L/d$

İki eş-fazlı wake kaynağı, aralarında $d$ mesafe, ekran $L$ uzaklıkta olsun. Ekranın $y$ noktasına iki yarıktan ulaşan wake yollarının farkı, küçük açı rejiminde ($d\ll L$):

$$\Delta = d\sin\theta \approx d\,\frac{y}{L}$$

Wake tepeleri üst üste bindiğinde (yapıcı çizgi) yol farkı tam periyodun katıdır: $\Delta = m\lambda$. Buradan parlak saçak konumları ve aralığı:

$$y_m = m\,\frac{\lambda L}{d} \qquad\Longrightarrow\qquad \boxed{\Delta y = \frac{\lambda L}{d}}$$

Cebir standart iki-kaynak geometrisidir; teorinin katkısı formülde değil, **girişen şeyin kimliğindedir**: girişen, soyut bir olasılık genliği değil, Evrenakı'da açılmış gerçek bir wake alanıdır; periyodu Zerre aralığıdır; Zerre bu alanın yapıcı çizgilerinden **birini** izler — hiçbir noktada "kendisiyle girişmez."

**Sayısal karşılaştırma.** He-Ne lazer ($\lambda=632{,}8$ nm), $d=0{,}25$ mm, $L=1$ m:

$$\Delta y = \frac{632{,}8\times10^{-9}\times1}{0{,}25\times10^{-3}} = 2{,}53\ \text{mm}$$

— her optik laboratuvarında ölçülen değerle birebir; $\lambda$, $L$, $d$ taramalarının üçü de bağıntıyı izler (G-1 ✅). Kenar kırınımı ölçeği de aynı geometriden düşer: DENEY 4'ün $L=8$ m'sinde $\sqrt{\lambda L}\approx2{,}25$ mm — saçakların çıplak gözle seçilebilmesinin nedeni (G-2 ✅ yapı ve ölçek; saçak-saçak nicel karşılaştırma açık kalemdir, 9.3.6/ii).

## 9.3.4 Tekil Tespit İstatistiği

Teori, G-3'ü yapısal olarak zorunlu kılar: bir tespit bir dilimin varışıdır → **tek nokta**; hiçbir tekil karede desen olamaz. Dilimin hangi yapıcı çizgiye varacağını, kontrolsüz ve düzgün dağılımlı varış fazı $\varphi$ seçer (M-11'in açık ucu; 2.6.5'in 50/50 istatistiğiyle aynı kaynak); binlerce dilimin istatistiği wake geometrisini örer — Tonomura kaydının teorideki okunuşu budur. G-4'ün nitel mekanizması da aynı resimden gelir: yol ölçen cihazın kütlesi ve türbülansı wake tünellerini bozar; wake bozulursa örülecek geometri kalmaz (2.10 girişi). Her iki istatistiğin nicel modeli açık kalemdir (9.3.6/iv–v).

## 9.3.5 Standart Fizikle Yüzleşme ve Dejenerasyon Kaydı

Standart çatı $y=\lambda L/d$'yi Huygens ilkesi ve olasılık genliğiyle verir — ve saçak geometrisi düzeyinde teoriyle **aynı formülü** verir; bu arena, geometri katmanında iki kuramı sayıyla ayırt edemez. Dürüst kayıt budur. Ayrışma iki yerdedir: **(a) ontoloji** — standart çatı dalgalanan şeyin fiziksel doğasını boş bırakır ("dalga fonksiyonu neyin dalgasıdır?"), teori onu adlandırır: Evrenakı'daki wake alanı; parçacık tek yoldadır (makroskopik akrabası: damlacık-pilot dalga sistemleri — sınırlarıyla birlikte 2.6.5'te kayıtlı); **(b) pencere-içi rejim** — dilim boyu ($c\tau$), koherans ve ultrakısa-atım öngörüleri (9.2.7/vi, 9.4.8/v) geometrinin ötesinde ayırt edici içerik taşır.

## 9.3.6 Açık Kalemler

Tümü 7.4 envanterine bağlanır; bölüm bu kalemler kapandığında genişletilecektir:

i. **Wake periyodu = Zerre aralığı:** bu bölümün tek fiziksel girdisinin ($\lambda$-periyotlu wake) katar mekaniğinden ilk-ilke türetimi.
ii. **Fresnel nicel karşılaştırma:** DENEY 4 geometrisinin klasik Fresnel öngörüsüyle saçak-saçak karşılaştırması (2.8'in kendi kaydı).
iii. **Madde çift yarığı:** elektron için $\lambda=h/p$'nin girdap mekaniğinden türetimi (9.2.7/v ile ortak cephe) ve Tonomura istatistiğinin nicel modeli.
iv. **Varış fazı dağılımı:** $\varphi$'nin düzgün dağılımının kaynak mekaniğinden türetimi (M-11 açık ucu) — istatistiksel desenin tam temeli.
v. **Desen yıkımı:** hangi-yol ölçümünde wake bozulmasının nicel modeli.

---

**Bölüm özeti:** Çift yarık saçak formülü $y=\lambda L/d$, iki eş-fazlı wake kaynağının Evrenakı'daki girişim geometrisinden standart trigonometriyle çıkar ve ölçümle birebir örtüşür; kenar kırınımının $\sqrt{\lambda L}$ ölçeği aynı geometrinin öbür yüzüdür. Tekil tespitin tek nokta, desenin istatistik olması teoride varsayım değil zorunluluktur: parçacık tek yoldadır, girişen onun wake alanıdır. Geometri katmanında teori standart optikle dejeneredir — ayırt edici içerik wake'in ontolojisinde ve pencere-içi rejimdedir. Derin katman (wake periyodu türetimi, elektron istatistiği, Fresnel nicel karşılaştırma) 7.4'e bağlı açık kalemlerdir; **bölüm o kalemler kapandığında tamamlanacaktır.**
