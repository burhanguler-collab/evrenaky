# 9.9 "Tek Foton" Çift Yarık Deneyleri: Ölçüm, Yorum ve Zerre Katarı Mekaniği

Çift yarık deneyinin zayıf ışık ve "tek tek gönderim" versiyonları, standart kuantum mekaniğinin en çok anılan gizemi olarak sunulur. Bu bölümün konumu baştan ve açıkça kaydedilmelidir: **burada hiçbir deney tartışmaya açılmamaktadır.** Taylor'ın aylarca pozlanan plakası, Tonomura'nın yetmiş bin noktası, Grangier ekibinin koinsidans sayımları birer gerçekliktir; titizlikle yapılmış, defalarca tekrarlanmış ve teorinin hesap vermekle yükümlü olduğu ölçümlerdir. Eleştirinin hedefi ölçüm değil, ölçüm ile ondan çıkarılan ontolojik sonuç arasına sessizce yerleştirilen **yorum katmanıdır**.

Bu ayrım bölümün yöntemidir ve Kısım 9'un tamamında kullanılacaktır: her gözlem için önce ne ölçüldüğü, sonra ölçülenin üzerine ne eklendiği, en sonunda eklemenin hangi çıkarım kuralını ihlal ettiği ayrı ayrı yazılır. Kısım 2.8 mekanizmayı kurmuş, 9.3 saçak geometrisini sayıyla doğrulamış, 9.10 "foton"un imkânsızlığını standart fiziğin kendi matematiğiyle göstermiştir; bu bölüm ikisinin kesişimini işler — **yüz yıllık yorumun tam olarak nerede ölçümden ayrıldığını.**

## 9.9.1 Doğrulanacak Gözlem Envanteri

| # | Gözlem (deney) | Ölçülen değer / davranış | Kaynak |
|---|---|---|---|
| G-1 | Çok zayıf ışıkla çift yarık | Bir mil ötedeki muma denk şiddete kısılmış ışıkla, aylar süren pozlamada plakada girişim deseni oluştu | Taylor, 1909 |
| G-2 | Tek tek elektronlarla desen birikimi | Kütleli elektronlar yarıklara tek tek gönderildiğinde ekranda önce dağınık tekil vuruşlar göründü; sayı on binleri aşınca saçak deseni belirginleşti (~70.000 nokta) | Tonomura ve ark., 1989 |
| G-3 | Işın bölücüde anti-demetlenme | Habercili düzenekte iki dedektörün eşzamanlı tetiklenme oranı klasik dalga sınırının altında: $g^{(2)}(0)<1$ | Grangier ve ark., 1986 |
| G-4 | Hangi-yol ölçümü | Yol bilgisini üreten aygıt devreye girdiğinde desen silinir | standart kuantum optik |

Dördü de gerçektir ve teori dördünü de üretmek zorundadır. Aşağıdaki bölümlerin gösterdiği şey, bu dört ölçümün hiçbirinin "ışık bölünmez tek fotonlardan oluşur" önermesini **içermediğidir**; önerme ölçümden çıkarılmamış, ölçümün üzerine eklenmiştir.

## 9.9.2 Ölçüm ile Yorum Arasındaki Sınır

Envanterin her satırı iki katmana ayrıştırılabilir. Birinci katman aygıtın kaydettiğidir ve tartışma dışıdır. İkinci katman, o kayda eklenen ontolojik cümledir; tartışmanın tamamı buradadır.

| Ölçülen (tartışma dışı) | Eklenen yorum | Eklemenin statüsü |
|---|---|---|
| Kısılmış ışıkla, uzun pozda plakada desen oluştu (G-1) | "Düzenekte her an yalnızca tek bir foton vardı" | **Ölçülmedi.** Kaynak klasik ışıktır; zayıflatma durumun istatistik sınıfını değiştirmez, Fock durumu üretmez (9.10.6/a). Üstelik plakanın tek bir tanesi bile gelişebilmek için ≥3–4 soğurma ister (9.10.7.5) — "tek foton bir iz bıraktı" cümlesi o düzenekte ilkece gözlenemezdi |
| Ekranda ayrık, tekil noktalar birikti (G-2) | "Her nokta, yayılmış bir olasılık dalgasının o noktada çökmesidir" | **Çıkarım geçersiz.** Nokta, alıcının eşik olayıdır; kaydı üreten aygıtın kendisidir (9.10.7). "Çökme"nin ne olduğu, ne kadar sürdüğü ve neyin tetiklediği yüz yıldır yazılmamıştır — açıklama değil, açıklama boşluğunun adıdır |
| Eşzamanlı tetiklenme klasik sınırın altında kaldı (G-3) | "Demek ki aynaya gelen şey bölünmez tek bir fotondur" | **Dışlanmamış alternatif.** Ölçüm "klasik stokastik şiddet alanı değil" sonucunu verir; "bölünmez tanecik" sonucunu vermez. Faz-ortak dilim mekaniği aynı istatistiği Fock durumu olmadan üretir (9.9.6; 9.10.6/c) |
| Yol bilgisi üretildiğinde desen silinir (G-4) | "Gözlem/bilgi, dalga fonksiyonunu çökertir" | **Nedensel karıştırma.** Ölçen aygıt fiziksel bir cisimdir ve düzeneğe kütlesiyle, alanıyla, türbülansıyla girer. Deseni silen etkinin *fiziksel müdahale* mi yoksa *bilgi* mi olduğu ayrıştırılmamış; ayrıştırılmadan ikincisi tercih edilmiştir |

Tablonun okunuşu şudur: dört ölçümün dördünde de kayıt ile sonuç arasında **doldurulmamış bir adım** vardır ve bu adım her seferinde aynı yönde — nesne varsayımı lehine — doldurulmuştur.

## 9.9.3 Yorum Katmanının Anatomisi: Altı Çıkarım Hatası

Kısım 9 boyunca aynı altı hata farklı arenalarda tekrarlanır. Burada bir kez tanımlanır; sonraki bölümler kısaltmalarıyla atıf yapar.

| Kod | Hata | Tanımı | Kanonik örneği |
|---|---|---|---|
| **Y-1** | **Nesneleştirme** | Muhasebe birimini cisim sanmak | "Klik oldu → bir foton geldi" (9.10.2, 9.10.7.2) |
| **Y-2** | **Adres kayması** | Alıcının özelliğini kaynağa yazmak | Kesikliliği ışığın kendisine yazmak; oysa merdiven alıcının penceresindedir (9.2.1) |
| **Y-3** | **Tekil-olay çıkarımı** | İstatistiksel oranı tekil olayın ontolojisi sanmak | "Desen dalgadır → her tek olay da dalgadır" |
| **Y-4** | **Dışlanmamış alternatif** | İki seçenek sayıp birini eleyerek ötekini ispatlanmış saymak | "Klasik dalga değilse foton olmalı" — üçüncü mekanik hiç denetlenmeden |
| **Y-5** | **Döngüsel kalibrasyon** | Ölçülecek büyüklüğü ölçüm biriminin içinde varsaymak | Foton akısını, hiç foton saymadan $P/h\nu$ ile hesaplamak (9.10.7.3) |
| **Y-6** | **Dil kayması** | Aynı sözcüğün uyumsuz tanımları arasında sessizce geçiş yapmak | "Foton"un nokta mermi / dalga paketi / mod uyarımı / klik tanımları (9.10.2) |

Çift yarık yorumunun tarihsel gücü, bu altı hatanın **arka arkaya dizilmesinden** gelir: klik nesneleştirilir (Y-1), kesiklilik ışığa yazılır (Y-2), istatistikten tekil olay ontolojisi türetilir (Y-3), alternatif denetlenmeden elenir (Y-4), doğrulama zinciri kendi birimine dayanır (Y-5) ve bütün bunlar tek bir sözcüğün dört tanımı arasında gidip gelinerek anlatılır (Y-6). Zincirin her halkası tek başına savunulabilir görünür; birlikte okunduğunda ortaya çıkan şey bir ölçüm sonucu değil, bir **anlatı inşasıdır**.

## 9.9.4 Dirac Düsturunun Teşhisi

Yorumun en yoğun hâli Dirac'ın düsturudur: *"Her foton yalnızca kendisiyle girişim yapar."* Kopenhag okumasında mermi, gözlemlenene kadar bir olasılık dalgasıdır; her iki yarıktan aynı anda geçer, kendisiyle girişir ve ekranda rastgele bir noktada "çöker". Cümle üç varlık iddiası taşır ve üçü de birbirinden bağımsız olarak kapalıdır:

| Cümlenin iddiası | Gerektirdiği nitelik | Yasağı ve adresi |
|---|---|---|
| "Bir foton" | tek-sayılabilir, bölünmez nesne | Hiçbir kaynak saf $\lvert1\rangle$ üretemez; $p_0>0$, $p_2>0$ daima (9.10.6) |
| "İki yarıktan birden geçer" | uzaya yayılmış, keskin frekanslı durum | Keskin frekanslı tek foton Hilbert uzayında durum değildir ($\delta(0)$; 9.10.4) |
| "Ekranda bir noktaya çöker" | yerleşik, konumu tanımlı nesne | Kütlesiz spin-1 için konum operatörü yoktur; sonlu-$N$ durumu hiçbir bölgeye hapsedilemez (9.10.5) |

İkinci ve üçüncü iddia birbirini de dışlar: aynı nesneden hem keskin frekans hem anlık yerleşme istemek Fourier sınırının doğrudan ihlalidir (9.10.3). Dolayısıyla Kopenhag yorumunun "doğanın gizemi" diye sunduğu şey, doğada ölçülmüş bir tuhaflık değil, **tek nesneye zorla yüklenmiş bağdaşmaz niteliklerin iç tutarsızlığıdır**. Gizemin kaynağı deney değil, cümledir; ve mekanik acziyetin matematiksel bir itirafı olarak kalır.

## 9.9.5 "Müjdelenmiş" Foton Kurgusu ve Yarı-Geçirgen Ayna (Grangier ve ark., 1986)

Yorumun en güçlü kalesi, habercili (heralded) kaynaklarla yapılan ışın bölücü deneyidir. Kurgu şöyledir:

1. Kalsiyum atomları uyarılarak temel hâle dönerken zıt yönlerde iki ışıma yapmaları sağlanır.
2. Bir yöndeki ışıma dedektöre ulaştığında (müjdeleme), diğer yöne doğru giden şeyin "kesinlikle tek bir foton" olduğu **varsayılır**.
3. Bu ışık bir yarı-geçirgen aynaya (beam splitter) gönderilir; aynanın arkasındaki A ve B dedektörleri eşzamanlı olarak nadiren tetiklenir (anti-demetlenme, $g^{(2)}(0)<1$).

Ölçüm gerçektir ve klasik stokastik alan modellerinin sınırının altındadır. Sorun, ölçümden sonuca geçişte üç yerdedir:

1. **Müjdenin tekliği varsayımdır, ölçüm değildir (Y-1).** Habercili kaynakların kendi cebiri, öteki kolda $\propto\lambda^2$ mertebesinde çok-çift bulaşmasının **her zaman** bulunduğunu söyler; bulaşmayı bastırmak üretim hızını sıfıra götürür ve saflık ile verim aynı anda 1 olamaz (9.10.6/b).
2. **Elenen alternatif denetlenmemiştir (Y-4).** Klasik sınırın ispatı, klik olasılığının pozitif dağılımlı stokastik bir şiddet alanıyla orantılı olmasını varsayar. Faz-ortak dilim mekaniği (9.9.6) bu varsayım sınıfının dışındadır ve aynı anti-demetlenmeyi tanecik postülasına gerek olmadan üretir.
3. **Sonuç, kendi öncülüyle çelişecek biçimde kullanılmıştır (Y-6).** Aynı yorum, aynada koinsidans vermediği için "foton bölünmez tek bir noktadır" der; ardından aynı noktanın çift yarıkta iki yarıktan birden geçtiğini söyler. Birinci cümlede "nokta mermi", ikinci cümlede "yayılmış dalga" tanımı kullanılmakta ve geçiş hiç ilan edilmemektedir.

## 9.9.6 Evrenakı Okuması: Wake-Kilitli Dilim ve Faz Ortaklığı

Evrenakı ontolojisinde noktasal, dalgalanan, bölünmez bir "tek foton" yoktur. 9.10'da gösterildiği üzere "foton", alıcının pencere ısırığıdır; kaynaktan çıkan ise bir **Zerre Katarı dilimidir**. Yarı-geçirgen ayna ve çift yarık deneylerinin mekanik çözümü dört adımdadır.

**1. Faz ortaklığı ve "bölünmezlik" yanılsaması.** Yarı-geçirgen ayna, Evrenakı'da dönen bir rampadır — pencere mekanizmasının kendisi (2.6.3). "Foton bölünmez" anlatısının arkasındaki gerçek, katar dilimi içindeki **wake-kilit** mekanizmasıdır. Lazerden ya da atomik uyarımdan çıkan bir katar diliminde Zerreler birbirlerine wake üzerinden kilitlenmiştir; bu kilitlenme, dilim boyunca **göreli fazın ($\varphi$) ortak olması** demektir. Dilim rampaya vurduğunda faz ortak olduğu için rampa–katar senkronizasyonu bütün Zerreler için aynı sonucu verir. Yani dilim "somut bir bütün olduğu için" bölünmez değildir; **karar mekanizması ortak olduğu için hepsi aynı kaderi paylaşır** — ya birlikte geçerler ya birlikte yansırlar. Eşzamanlı tetiklenmenin klasik sınırın altında kalmasının nedeni ışığın tanecikliliği değil, faz-ortak dilimin aynanın pencere ritmiyle toplu etkileşimidir.

Bu okumanın doğrudan sınanabilir bir sonucu vardır ve teorinin bu arenadaki ayırt edici öngörüsüdür: bağımsız, **faz-karışık** mermiler (termal kaynak) gönderilseydi rampa onları bölerdi ve istatistik $g^{(2)}\geq1$ tarafına düşerdi. Anti-demetlenmenin adresi ışığın taneciklenmesi değil, **dilim-içi faz ortaklığıdır**; kaynak koherans yapısıyla istatistik arasındaki bu bağ, iki okumayı ayırt edebilecek ölçüm hattıdır (9.9.8/ii).

**2. Wake izi.** Bu somut katar dilimi hızla ilerlerken, arkasında ve çevresinde Evrenakı akışkanını yararak bir **wake** — hidrodinamik iz, yani basınç gradyanı alanı — bırakır.

**3. Çift yarık çözümü.** Katar diliminin kendisi (somut mermiler) yalnızca **tek bir yarıktan** geçer; yörüngesi tektir. Buna karşılık dilimin açtığı wake izleri **her iki yarıktan birden** geçer. İki yarıktan geçen bu eş-fazlı izler arka tarafta üst üste binerek 9.3'te türetilen $y=\lambda L/d$ geometrisini kurar ve mutlak akışkan içinde duran basınç vadileri — düşük basınç koridorları — yaratır. Tek yarıktan geçen dilim, kendi yarattığı bu gradyan alanının içine düşer ve vadilere doğru sürüklenir.

**4. İstatistiksel yığılma.** Tekil bir dilimin hangi vadiye düşeceğini, kontrolsüz varış fazı $\varphi$ belirler. Bir atımda ekranda yalnızca tek bir nokta görülür (G-2); tekil tespitin tek nokta olması teoride varsayım değil zorunluluktur, çünkü bir tespit bir dilimin bir pencereye varmasıdır. Binlerce dilim gönderildiğinde somut mermiler basınç vadilerinde birikir ve girişim deseni ancak o zaman belirir.

**Hangi-yol ölçümünün (G-4) okunuşu** aynı resimden çıkar ve "bilgi" kavramına hiç ihtiyaç duymaz: yol ölçen aygıt fiziksel bir cisimdir; kütlesi ve türbülansıyla wake tünellerini bozar, wake bozulunca örülecek geometri kalmaz. Deseni silen şey gözlemcinin bilgisi değil, aygıtın ortama yaptığı **mekanik müdahaledir** — ve bu, ilkece ölçülebilir bir farktır (9.9.8/iii).

**G-2'nin ayrı kaydı.** Tonomura deneyi elektronlarla yapılmıştır; elektron kütleli ve yerleşebilir bir girdaptır, dolayısıyla 9.10'un kütlesiz-nesne yasakları ona uygulanmaz. Buradaki yorum hatası farklıdır ve yalnızca ödünç almadır: "her parçacık kendisiyle girişir" düsturu ışık arenasında kurulmuş, geçerliliği hiç sınanmadan madde arenasına aktarılmıştır. Teoride elektron da tek yoldan geçer ve deseni kendi deplasman havuzunun izleri örer; madde tarafının nicel modeli açık kalemdir (9.3.6/iii).

Standart fiziğin "dalga–parçacık ikiliği" diye sunduğu çıkmaz, teoride **wake-kilitli katar dilimi, pencere ritmi ve hidrodinamik wake izi** ayrımıyla çözülür. Ne iki yarıktan birden geçen bir parçacık vardır, ne de çöken bir olasılık dalgası; deneyleri çözen şey Evrenakı akışkanı ile Zerre mermilerinin mekaniğidir.

## 9.9.7 İki Okumanın Karşılaştırılması

| Gözlem | Kopenhag yorumu | Evrenakı okuması | Ayırt edici sınav |
|---|---|---|---|
| G-1 zayıf ışıkta desen | tek foton kendisiyle girişti | katar dilimleri tek tek geçti, wake alanı deseni ördü | kaynak istatistiğinin bağımsız ölçümü; plaka eşiği (9.10.7.5) |
| G-2 tekil noktalar | olasılık dalgasının çökmesi | pencere olayı: bir dilimin varışı | pencere-içi zamanlama; ultrakısa atım rejimi (9.4.8/v) |
| G-3 anti-demetlenme | ışık bölünmez tanecik | faz-ortak dilim, rampa kararını toplu alır | **kaynak koheransı ↔ istatistik bağı:** faz-karışık kaynakta $g^{(2)}\geq1$ öngörüsü (9.9.8/ii) |
| G-4 desen silinmesi | bilgi dalga fonksiyonunu çökertir | ölçüm aygıtı wake'i mekanik olarak bozar | müdahale şiddeti ile görünürlük düşüşünün sürekli bağı (9.9.8/iii) |

Son sütun bölümün dürüstlük kaydıdır: teorinin okuması bugün nitel olarak eksiksizdir; nicel ayırt edici içerik dört kalemin üçünde ölçülebilir öngörü olarak durmakta ve açık kalem şeklinde kayıtlıdır.

## 9.9.8 Açık Kalemler

Tümü 7.4 envanterine (md. 19) bağlanır:

i. **Wake-vadi seçim mekaniği:** dilimin hangi yapıcı koridora düşeceğini belirleyen yerel senkron koşulunun nicel modeli; yalnız saçak konumlarının değil, parlaklık dağılımının da türetimi.
ii. **Faz ortaklığı ↔ istatistik bağı:** dilim-içi wake-kilidinin $g^{(2)}$ üzerindeki etkisinin nicel türetimi ve kaynak koherans yapısına göre öngörülen istatistik değişiminin sınanması — teorinin bu arenadaki ayırt edici sınavı; 9.2.7/vi (dilim boyu ↔ koherans uzunluğu) ile ortak cephe.
iii. **Hangi-yol müdahalesinin niceliği:** yol ölçen aygıtın wake alanına yaptığı bozulma ile desen görünürlüğündeki düşüşün ilişkisi. Teorinin ayırt edici öngörüsü, silinmenin kesikli bir "bilgi" eşiğine değil **sürekli bir müdahale şiddetine** bağlı olmasıdır; kısmi görünürlük ölçümleri bu bağı sınayabilir.
iv. **$\varphi$ dağılımının türetimi:** varış fazının düzgün dağılımının kaynak mekaniğinden çıkarılması — 9.3.6/iv, 9.7.6/iv ve M-11'in açık ucuyla aynı kalem.
v. **Madde arenası:** elektron çift yarığının (G-2) nicel istatistiği ve $\lambda=h/p$'nin girdap mekaniğinden türetimi (9.2.7/v, 9.3.6/iii ile ortak cephe).

---

**Bölüm özeti:** Çift yarık ailesinin dört kanonik ölçümü de gerçektir ve teori dördünü de kendi mekaniğiyle üretir; bu bölümün eleştirdiği şey ölçümler değil, ölçümlerin üzerine eklenen yorum katmanıdır. Katman ayrıştırıldığında görülen şudur: hiçbir ölçüm "ışık bölünmez tek fotonlardan oluşur" önermesini içermez — önerme altı çıkarım hatasının arka arkaya dizilmesiyle (Y-1…Y-6) inşa edilmiştir. Dirac düsturunun üç iddiası birbirinden bağımsız olarak kapalıdır ve ikisi birbirini de dışlar; gizemin kaynağı deney değil, cümledir. Habercili ışın bölücü deneyinin sonucu "klasik stokastik alan değildir"i ispatlar, "tek foton vardır"ı değil. Teorinin okumasında ne iki yarıktan birden geçen bir parçacık ne de çöken bir olasılık dalgası bulunur: wake-kilitli katar dilimi tek yarıktan geçer, wake izi iki yarıktan geçer, basınç vadileri deseni örer; anti-demetlenmenin adresi ise ışığın taneciklenmesi değil **dilim-içi faz ortaklığıdır** — ve bu okuma, faz-karışık kaynakta istatistiğin klasik tarafa düşmesini öngörerek kendini sınanabilir kılar. Ayırt edici nicel sınavlar (faz ortaklığı–istatistik bağı, wake-vadi seçim mekaniği, hangi-yol müdahalesinin sürekli-şiddet öngörüsü) açık kalem olarak kayıtlıdır.
