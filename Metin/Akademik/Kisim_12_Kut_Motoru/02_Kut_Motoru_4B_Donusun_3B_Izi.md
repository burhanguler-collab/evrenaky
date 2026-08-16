# 12.2 Kut Motoru: 4B Dönüşün 3B'ye Düşen İzi

Kısmın adı buradan gelir. **Kut motoru**, Evrenakı Teorisi'nde gördüğümüz hemen her dönmenin — Zerre'nin spininden gezegenin ekseninden yıldızın dönüşüne kadar — arkasında duran tek düzenektir: dördüncü uzay boyutunda dönen bir yapının, bizim üç boyutlu kesitimize düşen izi.

Bu bölüm o izin **matematiğini** verir ve neden üç ayrı görüngü ürettiğini gösterir. Sonuç dikkat çekici ölçüde kısıtlıdır: 4B'de bir çift dönüş, 3B'de yalnız **üç** imza bırakabilir. Ne daha fazlası ne daha azı.

---

## 12.2.1 SO(4): Dördüncü Boyutta Dönme

Üç boyutta dönme bir eksen etrafındadır. **Dört boyutta eksen yoktur — düzlem vardır.** Ve dört boyut, birbirine dik **iki** düzlem barındırabilir. Dolayısıyla en genel 4B dönme, iki bağımsız açısal hızla, iki dik düzlemde aynı anda döner:

$$R(\varphi_1,\varphi_2) = R_{\text{düzlem A}}(\varphi_1)\cdot R_{\text{düzlem B}}(\varphi_2)$$

Dik düzlem çiftleri yalnız üç tanedir:

| Çift | Düzlem 1 | Düzlem 2 |
|---|---|---|
| I | $XY$ | $ZW$ |
| II | $XZ$ | $YW$ |
| III | $YZ$ | $XW$ |

Her çiftte **bir düzlem bizim 3B kesitimizin içinde**, diğeri $W$ eksenini içerir — yani bizim göremediğimiz doğrultuya uzanır. Görebildiğimiz şey, ikinci dönüşün birincisi üzerindeki **etkisidir**.

$\varphi_1 = \varphi_2$ olduğunda dönme **izoklinik** adını alır ve özel bir simetri kazanır. Simülasyonda bu ayrı bir seçenektir.

**Genellik kesinleştirmesi.** "En genel 4B dönme iki dik düzlemde döner" hükmü eleman düzeyinde koşulsuz bir teoremdir: dört boyutlu dönme grubunun her elemanı, uygun bir dik taban seçildiğinde iki dik değişmez düzlemde $(\varphi_1,\varphi_2)$ açılarıyla dönme biçimine getirilir. Ancak bu iki değişmez düzlem, genel durumda koordinat eksenlerine **eğik** durur; dönme, $X,Y,Z,W$ eksenlerinden hiçbirini tek başına korumak zorunda değildir. Üretecin kesit-içi bileşeni $\vec\omega_1$ ile $W$-kanalı bileşeni $\vec\omega_2$ cinsinden iki açı $\theta_{1,2}=\tfrac12\big(|\vec\omega_1+\vec\omega_2|\pm|\vec\omega_1-\vec\omega_2|\big)$ bağıntısıyla verilir ve düzlemler ancak $\vec\omega_1\parallel\vec\omega_2$ olduğunda koordinat çiftlerine oturur. Yukarıdaki üç koordinat çifti, bu normal biçimin **kesit tabanı dönmeye göre hizalandığında** ortaya çıkan kanonik temsilcileridir: dördüncü eksen $W$ fiziksel olarak ayrıcalıklı olduğundan geriye kalan serbestlik kesitin sıradan 3B dönmeleridir ve bu serbestlik, eğik duran herhangi bir $W$-kanalı yönünü tek bir kesit eksenine döndürmeye daima yeter. İki katman ayrı okunmalıdır: *"iki dik düzlemde dönme"* bir teoremdir; *"üç koordinat çifti"* ise bu teoremin kesit diline çevrilmiş kanonik biçimidir — birincisi taban seçiminden bağımsızdır, ikincisi taban seçiminin ürünüdür ve tam da bu yüzden geneldir. Kut dinamiğinin hizalı ($\vec\omega_1\parallel\vec\omega_2$) kanonik biçimi seçtiği ise ayrı gerekçelendirme bekleyen bir varsayımdır ve statü envanterine kayıtlıdır (12.0.5).

Dönme matrisinin $R^{\mathsf T}R = I$ ve $\det R = +1$ koşullarını sağladığı — yani gerçekten bir dönme olduğu, uzatma ya da yansıtma içermediği — simülasyonun öz-sınamalarıyla sürekli denetlenir.

---

## 12.2.2 Kesit mi, Gölge mi?

4B bir yapıyı 3B'de "görmenin" iki farklı yolu vardır ve **aynı şey değildirler**:

| Okuma | Tanım | Ne verir |
|---|---|---|
| **Kesit** | $w = 0$ hiperdüzlemiyle arakesit | Gerçekten *bizim* uzayımızda olan |
| **Gölge** | $W$ boyunca izdüşüm | Tüm yapının bastırılmış hâli |

İkisi yalnız $\varphi_2 = 0$ ve $\varphi_2 = \pi$'de çakışır. Aradaki her açıda **farklı** şeyler gösterirler. Simülasyon ikisini de sunar ve yan yana karşılaştırmaya izin verir.

Teorinin kullandığı okuma **kesittir** — çünkü bizim ölçtüğümüz şey gölge değil, kendi uzayımızda gerçekten bulunan maddedir. Kesit okumasında bir Kut, $|w| < \varepsilon$ koşulunu sağladığı sürece görünür ve görünen yarıçapı

$$r_{\text{görünen}} = \sqrt{\varepsilon^2 - w^2}$$

olur. $w$ büyüdükçe küçülür, $|w| = \varepsilon$'da **kaybolur.**

---

## 12.2.3 Üç İmza

4B çift dönüşün 3B kesitimizde bırakabileceği izler tam olarak üçtür.

Bu bir gözlem değil, **sayımdır** — ve tamlığı iki adımda kapanır. **Birinci adım** bir sınıflandırma teoremidir: en genel 4B dönme, iki dik düzlemde çift dönmedir (12.2.1; Coxeter, Lounesto) — başka türde bir 4B dönme yoktur. **İkinci adım** üreteç sayımıdır: SO(4)'ün altı üreteci vardır. Üçü kesitimizin içindedir ($XY$, $XZ$, $YZ$) ve sıradan 3B dönme üretir — bunlar 4B'ye özgü iz değildir. Kalan üçü $W$ eksenini içerir ($XW$, $YW$, $ZW$) ve eksen adlandırması dışında özdeş davranır. $W$ içeren tek bir dönmenin $w=0$ kesitine yapabileceği her şey şu üç etkiyle tükenir: noktayı $w$ boyunca taşır — görünen yarıçap değişir (İmza 1); kesit-paralel bileşeni $\cos\varphi_2$ ile ölçekler — yönelimli hacim (İmza 2); dönme düzleminin kesitteki izini yatırır (İmza 3). Dönme lineer bir izometri olduğundan başka bir serbestlik derecesi kalmaz: **dördüncü bir imzaya yer yoktur.** 12.5.6'daki çürütme ölçütü #4, bu sayıma dayanır.

Sayım, taban seçiminden bağımsız olarak sağlamdır: $W$-kanalının üreteç uzayı, üç imza üretecinin gerdiği üç boyutlu bir uzaydır ve kesitin sıradan dönmeleri bu uzayı kendi içine taşır — kesit tabanının uygun hizalanması, keyfî yönde bir $W$-kanalını her zaman tek bir imza eksenine indirger (12.2.1'deki genellik kesinleştirmesi). En genel 4B dönmede kesit-içi dönme ile $W$-kanalı sıra değiştirmediğinden imzalar zamana bağlı katsayılarla birbirine **karışabilir**; fakat bu karışım her an üç imzanın doğrusal birleşimi içinde kalır ve dördüncü bir iz türü üretemez. Liste bu anlamda tamdır: üç imza, olası bütün $W$-kanalı etkilerinin **tabanıdır** ve bu taban, dönme dinamiğinin tamamı altında kapalıdır.

### İmza 1 — Boyutsal salınım (pulsasyon)

Kut, $W$ boyunca gidip geldikçe kesitimizdeki **görünen yarıçapı değişir**. Büyür, küçülür, kimi zaman tamamen kaybolur. Dışarıdan bakan biri için bu, nesnenin **nefes alması** gibi görünür.

Bu imza, 12.3'te kurulan bağ mekanizmasının doğrudan kaynağıdır: pulsasyon yapan iki kavite birbirine kuvvet uygular.

Buradaki hacim değişimi Evrenakı'nın yaratılıp yok olması değildir. 4B yapı korunurken, yapının 3B kesitimizde kalan hacmi değişmektedir. Bu nedenle pulsasyon, 4B taşınımın 3B kesitteki görünümü olarak okunur; bunun 3B radyal akışla tam nicel eşleştirilmesi ayrıca türetilecek bir kapanış bağıdır.

**$w\to V\to \dot V$ zinciri.** Salınımın matematiği tek zincirle kapanır. İkinci açısal hız $\omega_2$, Kut'u $W$ boyunca $w(t)=A_w\sin(\omega_2 t)$ yasasıyla taşır; görünen yarıçap $r_{\text{gör}}=\sqrt{\varepsilon^2-w^2}$ olduğundan kesit hacmi $V(t)=\tfrac{4\pi}{3}(\varepsilon^2-w^2)^{3/2}$ biçiminde soluk alıp verir. Zincirin en ayırt edici halkası, hacmin $w$'nin kendisine değil **karesine** bağlı olmasıdır: salınımın her iki ucu — Kut ister $W$'nin artı ister eksi yönüne sapsın — kesiti aynı ölçüde büzer. Bunun zorunlu sonucu, hacim pulsasyonunun $\omega_2$'de değil onun tam iki katında,

$$\boxed{\;\Omega = 2\,\omega_2\;}$$

frekansında gerçekleşmesidir: **Kut, dördüncü eksendeki her tam salınımda iki kez nefes alır.** Küçük salınım sınırında ($A_w\ll\varepsilon$) pulsasyon genliği kapalı biçimde $\Delta V = \pi\varepsilon A_w^2$ çıkar; genlik büyüdükçe soluk alışa yüksek harmonikler eklenir ve 12.3.2'de gösterileceği gibi bunlar etkiyi zayıflatmaz, güçlendirir. Ortamı süren nicelik hacmin kendisi değil değişim hızıdır: $\dot V(t)$, Kut'u ortama gömülü salınımlı bir kaynak yapar ve iki Kut arasındaki Bjerknes kanalının kaynak şiddeti tam olarak bu $\dot V$'dır. Dördüncü eksendeki görünmez salınım, üç boyutlu kesitte ölçülebilir bir basınç alışverişine böyle dönüşür.

### İmza 2 — Ayna terslenmesi

Bu, kısmın en az sezgisel ama en keskin sonucudur. $W$ içeren düzlemdeki dönme, 3B kesitimizde bir **yönelim tersinmesi** üretir. Ve bunun niceliksel yasası vardır:

$$\boxed{\;V(\varphi_2) = V_0\cos\varphi_2\;}$$

Buradaki $V$, kesitin **yönelimli hacmidir** (işaretli determinant). Sonuç:

| $\varphi_2$ | $\cos\varphi_2$ | Durum |
|---|---|---|
| $0$ | $+1$ | Özgün yönelim |
| $\pi/4$ | $+0{,}707$ | Küçülüyor |
| $\boldsymbol{\pi/2}$ | $\mathbf{0}$ | **Parite tersiniyor** |
| $\pi$ | $-1$ | Tam ayna görüntüsü |

**Parite, yarım turda değil ÇEYREK turda tersinir.** Bu, teorinin kiralite ile ilgili öngörülerinin matematiksel kaynağıdır — ve doğrudan sınanabilir bir ifadedir.

#### Kesit okumasında türetim

$V(\varphi_2)=V_0\cos\varphi_2$ yasası yalnız gölge için değil, teorinin fiziksel okuması olan $w=0$ **kesiti** için de kurulur. Kesitte parite gözlenebiliri şudur: cisme yapışık malzeme çerçevesi $(\mathbf e_1,\mathbf e_2,\mathbf e_3)$, ikinci dönüş $R(\varphi_2)$ ile $ZW$-düzleminde taşınırken, kesitin bu çerçeveden ölçebildiği üçlünün yönelimli hacmi — $\det[P R\mathbf e_1,\,PR\mathbf e_2,\,PR\mathbf e_3]$; burada $P$, dördüncü bileşeni atan izdüşümdür. Dönüş ilk iki eksene dokunmaz, üçüncünün kesit-paralel bileşenini $\cos\varphi_2$ ile ölçekler; determinant doğrudan $\cos\varphi_2$ verir. Kritik nokta şudur: bu ifade, gölge okumasındaki determinantla **özdeştir**. Kesit ile gölge *nokta kümesi* olarak yalnız $\varphi_2=0$ ve $\pi$'de çakışır; fakat parite, kesit üzerindeki bir noktanın birinci-mertebe (teğetsel) verisidir ve kesit hiperdüzlemi üzerindeki bir noktada "kesitteki iz" ile "$W$ boyunca izdüşüm" aynı lineer işlemdir. Biçim (İmza 1) iki okumada ayrışırken, yönelim yasası (İmza 2) her açıda örtüşür: **ayna terslenmesi, okuma seçimine bağlı olmayan bir imzadır.**

Tanımın operasyonel karşılığı ve bir ince ayrım burada netleştirilmelidir. Kesit, cisme enlemesine yatan bir malzeme eksenini ucundan göremez; onu, malzemeye işlenmiş bir doğrultunun kesiti **deldiği noktadan** okur — ve bu delme izinin doğrultusu tam olarak $PR\mathbf e_3=\cos\varphi_2\,\hat z$ çıkar: işaret dönüşü çeyrek turda, kesitin kendi ölçümüyle görülür. Buna karşılık "kesitte o anda bulunan malzemenin yönelimi" ayrı bir sorudur: kesit içeriği zamanla değişir ve o içeriğin dilim-eşyönelimine göre determinantı her açıda $+1$'dir, çünkü dönüş bir izometridir ve dilimi kesite daima yönelim koruyarak oturtur. Bu sabit $+1$ bir karşı-örnek değil, bir teşhistir: ortam geometrisine çıpalanan, cismin kendi malzeme işaretlerini görmeyen bir yönelim, kiralite hakkında **kör** bir gözlenebilirdir. Malzemeye çıpalanan her tanımda — ister vektörlerin kesit izi, ister dilim içine izdüşürülmüş malzeme ekseni — yasa aynı $\cos\varphi_2$ olarak geri gelir. Zamanla iz sürmeye dayalı hız okumalarına ise kesitten malzeme akışının eklediği bir görünür kayma terimi karışır; bu terim İmza 3'ün kinematiğine girer, anlık yönelim determinantına girmez. **Parite yasası kesit okumasında ek terimsiz, aynen ayaktadır.**

Terslenme anının kaybolma anıyla ilişkisi ise yasadan çıkmaz; ayrı bir kinematik sorudur. Terslenme $\varphi_2=\pi/2$'ye çakılıdır; kaybolma $|w|=\varepsilon$ koşuluna, yani $W$-salınımının genlik ve fazına bağlıdır. Salınım, merkezi eksenden $\varepsilon$ uzaklıkta taşıyan aynı $ZW$-dönüşünün rijit sonucuysa ($w=\varepsilon\sin\varphi_2$), görünen yarıçap $r_{\text{gör}}=\varepsilon|\cos\varphi_2|$ olur: pulsasyon zarfı ile parite zarfı tek eğride birleşir ve terslenme tam kaybolma anında, sıfır boyutta gerçekleşir — doğrudan izlenemez, kaybolma öncesi ile sonrasının ayna karşılaştırmasıyla saptanır. Kilit kırıksa — genlik $\varepsilon$'un altındaysa ya da faz kaymışsa — cisim çeyrek turda görünür boyuttadır ve terslenme canlı izlenir: doku düzlemsel yozlaşmadan geçer, ayna görüntüsü olarak çıkar. **Terslenme ile kaybolmanın eşzamanlı olup olmadığı, böylece motorun iç kinematiğini ($A_w$, faz) sınayan bağımsız bir gözlenebilirdir.**

### İmza 3 — Eksen doğrusal salınımı

Üçüncü imza, dönme düzleminin kendisinin kesitimizde **salınıyor** görünmesidir. Sabit bir eksen etrafında düzgün dönme beklerken, gözlemlenen şey ekseni yalpalayan bir dönmedir.

---

## 12.2.4 Neden "Motor"?

Üç imzanın birlikte yaptığı şey şudur: **3B'de kendiliğinden açıklanamayan bir dönme kaynağı sağlarlar.**

Üç boyutlu bir akışkanda dönmeyi başlatan şey bir torktur; tork da bir kuvvet dağılımıdır; o da bir başka kaynağı gerektirir. Zincir geriye doğru uzar. 4B dönüş bu zinciri keser: **3B'de gördüğümüz dönme, 4B'de zaten var olan bir dönmenin izidir.** Yerel bir neden aramak gereksizdir, çünkü neden yerel değildir — bir boyut yukarıdadır.

Ama bu tek başına yetmez. Motorun 3B'de bir dönme *kaynağı* sağlaması, o dönüşün kurulan **yapılara nasıl geçtiğini** açıklamaz. Zincirin eksik halkası budur ve **12.4** onu kurar: dolanımın toplanabilirliği sayesinde yapının dönüşü üyelerinkinden tam olarak türetilir. Yörüngelerin tesadüfi olmadığı iddiası (12.5.5) ancak o halka kurulduktan sonra ayakta durur.

<p style="margin:20px 0;padding:16px;border:1px solid #22c55e;border-radius:10px;background:rgba(34,197,94,0.07)"><a href="Simulasyon/kisim12/kut_4b_donus.html" target="_blank" rel="noopener" style="display:inline-block;padding:12px 22px;background:#166534;color:#ffffff;border-radius:8px;font-weight:700;text-decoration:none;font-size:1.05em">&#9654;&#65039; SİMÜLASYONU AÇ — 4B dönüşün 3B'ye yansıması</a><br><span style="color:#a1a1aa;font-size:0.9em;display:inline-block;margin-top:8px">Yan yana <b>4B</b> ve <b>3B</b> panel. Üç dik düzlem çifti (XY+ZW, XZ+YW, YZ+XW) tek tek seçilir; <b>izoklinik</b> kip ayrıca açılır. <b>Kesit</b> ve <b>gölge</b> okumaları karşılaştırmalı gösterilir — yalnız $\varphi_2 = 0$ ve $\pi$'de çakıştıkları doğrudan izlenir. Üç imza ayrı ayrı vurgulanabilir; ayna terslenmesinde $V = V_0\cos\varphi_2$ eğrisi canlı çizilir ve çeyrek turdaki parite dönüşü işaretlenir. Onlarca Kut'a kadar ölçeklenir. <b>12 öz-sınama</b> açılışta koşar (dönme matrisi ortogonalliği, $\det = +1$, kesit yarıçapı, düzlemsel dizilimde $\delta = 0$ dahil). Tek dosya, dış bağımlılık yok.</span></p>

---

## 12.2.5 Ne İddia Edilmiyor

Bu bölüm 4B dönüşün **var olduğunu kanıtlamaz**. Yaptığı şey daha dar ve daha dürüsttür: *eğer* 4B'de bir çift dönüş varsa, 3B'de tam olarak neyin görüleceğini hesaplar — ve o üç imzanın dışında bir şey göremeyeceğimizi gösterir.

Bu, teoriyi **çürütülebilir** kılar. Üç imzanın dışında bir 4B kökenli iz gözlemlenirse, bu kurgu yanlıştır.
