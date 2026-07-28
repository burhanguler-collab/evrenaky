# 1.4 Evrenakı Teorisinin Doğumu: Dördüncü Uzanımsal Boyut

Önceki bölümler teorinin *neden* gerektiğini (1.2'deki krizler) ve *neyi* varsaydığını (1.3'teki postülatlar) ortaya koydu; bu bölümde ise teori ilk sonuçlarını üreterek doğar. Manifestoda (1.1) bu çalışmanın ana omurgası olarak ilan edilen ve 2. postülatla (1.3) aksiyomatik zemine oturtulan uzanımsal dördüncü boyutun kinematik sonuçları, burada betimsel geometrinin epür (Monge izdüşümü) yöntemiyle (Monge, 1799) adım adım türetilecektir. Cevaplanacak soru kesin ve tektir: **dördüncü boyutta dönen bir cismin bu dönüşü, üç boyutlu uzay kesitimizde nasıl görünür?** Bölümün sonunda ulaşılacak üç izdüşüm imzası — doğrusal salınım, ayna-terslenme ve devinim — kitabın geri kalanının başvuru tanımlarını oluşturacaktır.

> **Bu bölüm nasıl okunur?** Bu, kitabın en teknik kısmıdır (betimsel geometri, epür diyagramları, çift-dönüş kinematiği). Ama tek bir ana fikre iner: **dört boyutta dönen bir cisim, üç boyutlu uzayımızda asla "dönüş" olarak görünmez; kendini yalnızca üç dolaylı imzayla ele verir — salınım, ayna-terslenme ve devinim.** Geometrik türetimin ayrıntısıyla ilgilenmeyen okuyucu, doğrudan **1.4.11'deki sonuç** kısmına geçip bu üç imzayı öğrenebilir; sonraki bütün kısımlar yalnızca o üç imzaya başvurur.


## 1.4.1 Uzanımsal Dördüncü Boyutun Tanımı

Üç boyutlu uzayımız, birbirine dik üç eksenle tarif edilir: **X, Y, Z**. Uzanımsal dördüncü boyut, bu üç eksenin **her birine aynı anda dik olan** dördüncü bir doğrultudur; bu eksene **W** diyeceğiz. W ekseni zamansal bir parametre değildir; X, Y ve Z ile tamamen aynı türden, uzunluk ölçülebilen gerçek bir uzay doğrultusudur. Üç boyutlu uzayımız, dört boyutlu uzayın içinde `w = 0` denklemiyle tanımlı bir "kesit"tir — tıpkı bir kâğıt düzleminin (z = 0) üç boyutlu odanın içindeki bir kesit olması gibi. Biz, ölçüm araçlarımızla yalnızca bu kesit üzerindeki izdüşümleri görebiliriz; bir noktanın W koordinatı bizim için doğrudan görünmezdir.

## 1.4.2 Epür Yönteminin Dört Boyuta Genellenmesi

Klasik epürde üç boyutlu bir cisim, birbirine dik iki düzleme (alın ve plan düzlemlerine) ayrı ayrı izdüşürülür ve bu iki görünüş, ortak eksen boyunca "katlanarak" tek bir kâğıt düzleminde yan yana açılır. Aynı yöntem dört boyuta doğrudan genellenir: dört eksenli uzayda **altı** koordinat düzlemi vardır ve bir hareketi tam tarif etmek için, hareketin geçtiği düzlemin görünüşü ile ona ortak eksen üzerinden bağlı komşu görünüş yeterlidir.

Aşağıdaki tüm epürlerde düzen aynıdır:

- **Üst görünüş:** dönüşün gerçekleştiği düzlem (dairenin kendisi burada görünür),
- **Katlama hattı:** iki görünüşün paylaştığı ortak eksen,
- **Alt görünüş:** ortak ekseni paylaşan komşu düzlem (dönüşün bu görünüşteki izi),
- Kesikli düşey doğrular, iki görünüşteki aynı noktayı birbirine bağlayan **ait olma (korespondans) çizgileridir.**

## 1.4.3 Dört Boyutta Dönüşün Doğası: Eksen Değil, Düzlem

Üç boyutta dönüş bir **eksen** etrafında tanımlanır: dönen cismin üzerinde hareketsiz kalan tek şey, bir doğrudur (dönme ekseni). Dört boyutta ise bu tanım yetersizleşir; dönüş bir **düzlem içinde** gerçekleşir ve hareketsiz kalan şey bir doğru değil, dönüş düzlemine **tamamen dik olan ikinci bir düzlemdir** (sabit düzlem). X, Y, Z, W eksenlerinden ikişerli seçimle **altı temel dönüş düzlemi** oluşur ve bunlar iki gruba ayrılır:

| Dönüş Düzlemi | Sabit Düzlem | Üç Boyuttaki Görünümü |
|---|---|---|
| XY | ZW | Z ekseni etrafında normal dönüş |
| XZ | YW | Y ekseni etrafında normal dönüş |
| YZ | XW | X ekseni etrafında normal dönüş |
| **XW** | YZ | **X doğrusu boyunca Boyutsal salınım — dönüş görünmez** |
| **YW** | XZ | **Y doğrusu boyunca Boyutsal salınım — dönüş görünmez** |
| **ZW** | XY | **Z doğrusu boyunca Boyutsal salınım — dönüş görünmez** |

Matematiksel çekirdek tek satırdır. Örneğin XW düzleminde dönen bir nokta için:

$$x(t) = R\cos(\omega t), \qquad w(t) = R\sin(\omega t), \qquad y, z = \text{sabit}$$

Nokta gerçekte kusursuz bir daire çizer. Ancak üç boyutlu uzayımız yalnızca $w = 0$ kesitindeki izdüşümü gördüğünden, bize kalan tek şey $x(t) = R\cos(\omega t)$ ifadesidir: **hiçbir düzlemde dairesel iz yoktur; yalnızca X doğrusu boyunca ileri-geri, sinüs temposunda bir salınım vardır.**

## 1.4.4 Birinci Grup Epürler: Dönüş Düzlemi Üç Boyutun İçinde (XY, XZ, YZ)

Bu üç durumda dönüş düzleminin tamamı bizim uzayımızın içindedir; daire hangi görünüşte çizilirse çizilsin, o görünüş bizim erişebildiğimiz bir düzlemdir. Üç boyutlu sonuç her zaman bildiğimiz **normal dönüştür** ve geriye kalan üçüncü eksen, görünür dönme ekseni olur. Alt görünüşlerde noktanın yalnızca ortak eksen boyunca salınması, dönüşün "kaybolduğu" anlamına gelmez — daire zaten üst görünüşte, üç boyutun içinde tam olarak görünmektedir.

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 900 480" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif">
<text x="160" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">1) XY düzleminde dönüş</text>
<line x1="110" y1="150" x2="110" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<line x1="210" y1="150" x2="210" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<text x="42" y="98" font-size="11" fill="#9ca3af">XY</text>
<line x1="75" y1="150" x2="245" y2="150" stroke="#4b5563"/>
<line x1="160" y1="85" x2="160" y2="215" stroke="#4b5563"/>
<text x="250" y="154" font-size="11" fill="#9ca3af">X</text>
<text x="166" y="93" font-size="11" fill="#9ca3af">Y</text>
<circle cx="160" cy="150" r="50" fill="none" stroke="#00e5ff" stroke-width="1.8"/>
<g transform="translate(160,150)"><g>
<animateTransform attributeName="transform" type="rotate" values="0;-360" dur="6s" repeatCount="indefinite"/>
<circle cx="50" cy="0" r="5" fill="#00e5ff"/>
</g></g>
<line x1="40" y1="245" x2="280" y2="245" stroke="#8892b0" stroke-dasharray="7 5"/>
<text x="160" y="239" font-size="10" fill="#8892b0" text-anchor="middle">katlama hattı (ortak X)</text>
<text x="42" y="288" font-size="11" fill="#9ca3af">XZ</text>
<line x1="75" y1="340" x2="245" y2="340" stroke="#4b5563"/>
<line x1="160" y1="275" x2="160" y2="405" stroke="#4b5563"/>
<text x="250" y="344" font-size="11" fill="#9ca3af">X</text>
<text x="166" y="283" font-size="11" fill="#9ca3af">Z</text>
<line x1="110" y1="340" x2="210" y2="340" stroke="#00e5ff" stroke-width="3" opacity="0.3"/>
<circle cy="340" r="5" fill="#00e5ff">
<animate attributeName="cx" values="210;110;210" keyTimes="0;0.5;1" dur="6s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</circle>
<text x="160" y="438" font-size="12" fill="#cbd5e1" text-anchor="middle">3B sonucu: Z ekseni etrafında</text>
<text x="160" y="456" font-size="12" fill="#cbd5e1" text-anchor="middle">normal dönüş</text>
<text x="460" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">2) XZ düzleminde dönüş</text>
<line x1="410" y1="150" x2="410" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<line x1="510" y1="150" x2="510" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<text x="342" y="98" font-size="11" fill="#9ca3af">XZ</text>
<line x1="375" y1="150" x2="545" y2="150" stroke="#4b5563"/>
<line x1="460" y1="85" x2="460" y2="215" stroke="#4b5563"/>
<text x="550" y="154" font-size="11" fill="#9ca3af">X</text>
<text x="466" y="93" font-size="11" fill="#9ca3af">Z</text>
<circle cx="460" cy="150" r="50" fill="none" stroke="#00e5ff" stroke-width="1.8"/>
<g transform="translate(460,150)"><g>
<animateTransform attributeName="transform" type="rotate" values="0;-360" dur="6s" repeatCount="indefinite"/>
<circle cx="50" cy="0" r="5" fill="#00e5ff"/>
</g></g>
<line x1="340" y1="245" x2="580" y2="245" stroke="#8892b0" stroke-dasharray="7 5"/>
<text x="460" y="239" font-size="10" fill="#8892b0" text-anchor="middle">katlama hattı (ortak X)</text>
<text x="342" y="288" font-size="11" fill="#9ca3af">XY</text>
<line x1="375" y1="340" x2="545" y2="340" stroke="#4b5563"/>
<line x1="460" y1="275" x2="460" y2="405" stroke="#4b5563"/>
<text x="550" y="344" font-size="11" fill="#9ca3af">X</text>
<text x="466" y="283" font-size="11" fill="#9ca3af">Y</text>
<line x1="410" y1="340" x2="510" y2="340" stroke="#00e5ff" stroke-width="3" opacity="0.3"/>
<circle cy="340" r="5" fill="#00e5ff">
<animate attributeName="cx" values="510;410;510" keyTimes="0;0.5;1" dur="6s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</circle>
<text x="460" y="438" font-size="12" fill="#cbd5e1" text-anchor="middle">3B sonucu: Y ekseni etrafında</text>
<text x="460" y="456" font-size="12" fill="#cbd5e1" text-anchor="middle">normal dönüş</text>
<text x="760" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">3) YZ düzleminde dönüş</text>
<line x1="710" y1="150" x2="710" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<line x1="810" y1="150" x2="810" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<text x="642" y="98" font-size="11" fill="#9ca3af">YZ</text>
<line x1="675" y1="150" x2="845" y2="150" stroke="#4b5563"/>
<line x1="760" y1="85" x2="760" y2="215" stroke="#4b5563"/>
<text x="850" y="154" font-size="11" fill="#9ca3af">Y</text>
<text x="766" y="93" font-size="11" fill="#9ca3af">Z</text>
<circle cx="760" cy="150" r="50" fill="none" stroke="#00e5ff" stroke-width="1.8"/>
<g transform="translate(760,150)"><g>
<animateTransform attributeName="transform" type="rotate" values="0;-360" dur="6s" repeatCount="indefinite"/>
<circle cx="50" cy="0" r="5" fill="#00e5ff"/>
</g></g>
<line x1="640" y1="245" x2="880" y2="245" stroke="#8892b0" stroke-dasharray="7 5"/>
<text x="760" y="239" font-size="10" fill="#8892b0" text-anchor="middle">katlama hattı (ortak Y)</text>
<text x="642" y="288" font-size="11" fill="#9ca3af">XY</text>
<line x1="675" y1="340" x2="845" y2="340" stroke="#4b5563"/>
<line x1="760" y1="275" x2="760" y2="405" stroke="#4b5563"/>
<text x="850" y="344" font-size="11" fill="#9ca3af">Y</text>
<text x="766" y="283" font-size="11" fill="#9ca3af">X</text>
<line x1="710" y1="340" x2="810" y2="340" stroke="#00e5ff" stroke-width="3" opacity="0.3"/>
<circle cy="340" r="5" fill="#00e5ff">
<animate attributeName="cx" values="810;710;810" keyTimes="0;0.5;1" dur="6s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</circle>
<text x="760" y="438" font-size="12" fill="#cbd5e1" text-anchor="middle">3B sonucu: X ekseni etrafında</text>
<text x="760" y="456" font-size="12" fill="#cbd5e1" text-anchor="middle">normal dönüş</text>
</svg>
</div>

## 1.4.5 İkinci Grup Epürler: Dönüş Düzlemi W Eksenini İçeriyor (XW, YW, ZW)

Asıl ilgilendiğimiz durum budur. Dairenin çizildiği üst görünüşler (XW, YW, ZW) artık bizim uzayımızın düzlemleri **değildir** — katlama hattının öte tarafı, dördüncü boyutun tarafıdır (turuncu ile gösterilmiştir). Üç boyutlu uzayımıza kalan tek şey, alt görünüşteki (bizim tarafımızdaki) izdüşümdür: **ortak eksen doğrusu boyunca bir Boyutsal Salınım.** Dikkat edilirse üç durumda da nokta gerçekte hiç durmadan, sabit açısal hızla dönmektedir; ama biz dönüşün kendisini asla göremeyiz — yalnızca X, Y veya Z doğrusu üzerinde "nefes alan" bir gidiş-geliş gözleriz.

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 900 480" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif">
<text x="160" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">4) XW düzleminde dönüş</text>
<line x1="110" y1="150" x2="110" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<line x1="210" y1="150" x2="210" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<text x="36" y="98" font-size="11" fill="#ffb020">XW</text>
<line x1="75" y1="150" x2="245" y2="150" stroke="#4b5563"/>
<line x1="160" y1="85" x2="160" y2="215" stroke="#4b5563"/>
<text x="250" y="154" font-size="11" fill="#9ca3af">X</text>
<text x="166" y="93" font-size="11" fill="#ffb020">W</text>
<circle cx="160" cy="150" r="50" fill="none" stroke="#ffb020" stroke-width="1.8"/>
<g transform="translate(160,150)"><g>
<animateTransform attributeName="transform" type="rotate" values="0;-360" dur="6s" repeatCount="indefinite"/>
<circle cx="50" cy="0" r="5" fill="#ffb020"/>
</g></g>
<line x1="40" y1="245" x2="280" y2="245" stroke="#8892b0" stroke-dasharray="7 5"/>
<text x="160" y="239" font-size="10" fill="#8892b0" text-anchor="middle">katlama hattı (ortak X)</text>
<text x="42" y="288" font-size="11" fill="#9ca3af">XY</text>
<line x1="75" y1="340" x2="245" y2="340" stroke="#4b5563"/>
<line x1="160" y1="275" x2="160" y2="405" stroke="#4b5563"/>
<text x="250" y="344" font-size="11" fill="#9ca3af">X</text>
<text x="166" y="283" font-size="11" fill="#9ca3af">Y</text>
<line x1="110" y1="340" x2="210" y2="340" stroke="#00e5ff" stroke-width="3" opacity="0.3"/>
<circle cy="340" r="5" fill="#00e5ff">
<animate attributeName="cx" values="210;110;210" keyTimes="0;0.5;1" dur="6s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</circle>
<text x="160" y="438" font-size="12" fill="#cbd5e1" text-anchor="middle">3B sonucu: X doğrusunda salınım</text>
<text x="160" y="456" font-size="12" fill="#cbd5e1" text-anchor="middle">dönüş görünmez</text>
<text x="460" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">5) YW düzleminde dönüş</text>
<line x1="410" y1="150" x2="410" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<line x1="510" y1="150" x2="510" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<text x="336" y="98" font-size="11" fill="#ffb020">YW</text>
<line x1="375" y1="150" x2="545" y2="150" stroke="#4b5563"/>
<line x1="460" y1="85" x2="460" y2="215" stroke="#4b5563"/>
<text x="550" y="154" font-size="11" fill="#9ca3af">Y</text>
<text x="466" y="93" font-size="11" fill="#ffb020">W</text>
<circle cx="460" cy="150" r="50" fill="none" stroke="#ffb020" stroke-width="1.8"/>
<g transform="translate(460,150)"><g>
<animateTransform attributeName="transform" type="rotate" values="0;-360" dur="6s" repeatCount="indefinite"/>
<circle cx="50" cy="0" r="5" fill="#ffb020"/>
</g></g>
<line x1="340" y1="245" x2="580" y2="245" stroke="#8892b0" stroke-dasharray="7 5"/>
<text x="460" y="239" font-size="10" fill="#8892b0" text-anchor="middle">katlama hattı (ortak Y)</text>
<text x="342" y="288" font-size="11" fill="#9ca3af">XY</text>
<line x1="375" y1="340" x2="545" y2="340" stroke="#4b5563"/>
<line x1="460" y1="275" x2="460" y2="405" stroke="#4b5563"/>
<text x="550" y="344" font-size="11" fill="#9ca3af">Y</text>
<text x="466" y="283" font-size="11" fill="#9ca3af">X</text>
<line x1="410" y1="340" x2="510" y2="340" stroke="#00e5ff" stroke-width="3" opacity="0.3"/>
<circle cy="340" r="5" fill="#00e5ff">
<animate attributeName="cx" values="510;410;510" keyTimes="0;0.5;1" dur="6s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</circle>
<text x="460" y="438" font-size="12" fill="#cbd5e1" text-anchor="middle">3B sonucu: Y doğrusunda salınım</text>
<text x="460" y="456" font-size="12" fill="#cbd5e1" text-anchor="middle">dönüş görünmez</text>
<text x="760" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">6) ZW düzleminde dönüş</text>
<line x1="710" y1="150" x2="710" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<line x1="810" y1="150" x2="810" y2="340" stroke="#333c4d" stroke-dasharray="3 3"/>
<text x="636" y="98" font-size="11" fill="#ffb020">ZW</text>
<line x1="675" y1="150" x2="845" y2="150" stroke="#4b5563"/>
<line x1="760" y1="85" x2="760" y2="215" stroke="#4b5563"/>
<text x="850" y="154" font-size="11" fill="#9ca3af">Z</text>
<text x="766" y="93" font-size="11" fill="#ffb020">W</text>
<circle cx="760" cy="150" r="50" fill="none" stroke="#ffb020" stroke-width="1.8"/>
<g transform="translate(760,150)"><g>
<animateTransform attributeName="transform" type="rotate" values="0;-360" dur="6s" repeatCount="indefinite"/>
<circle cx="50" cy="0" r="5" fill="#ffb020"/>
</g></g>
<line x1="640" y1="245" x2="880" y2="245" stroke="#8892b0" stroke-dasharray="7 5"/>
<text x="760" y="239" font-size="10" fill="#8892b0" text-anchor="middle">katlama hattı (ortak Z)</text>
<text x="642" y="288" font-size="11" fill="#9ca3af">XZ</text>
<line x1="675" y1="340" x2="845" y2="340" stroke="#4b5563"/>
<line x1="760" y1="275" x2="760" y2="405" stroke="#4b5563"/>
<text x="850" y="344" font-size="11" fill="#9ca3af">Z</text>
<text x="766" y="283" font-size="11" fill="#9ca3af">X</text>
<line x1="710" y1="340" x2="810" y2="340" stroke="#00e5ff" stroke-width="3" opacity="0.3"/>
<circle cy="340" r="5" fill="#00e5ff">
<animate attributeName="cx" values="810;710;810" keyTimes="0;0.5;1" dur="6s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</circle>
<text x="760" y="438" font-size="12" fill="#cbd5e1" text-anchor="middle">3B sonucu: Z doğrusunda salınım</text>
<text x="760" y="456" font-size="12" fill="#cbd5e1" text-anchor="middle">dönüş görünmez</text>
</svg>
</div>

Bir **küre** için bu, çarpıcı bir görüntü üretir: XW düzleminde dönen (yani W'ye "yatan") bir kürenin üç boyutlu izdüşümü, dönme evresine bağlı olarak X doğrultusunda yassılıp yeniden açılan bir yapıdır. Küre bize doğru "nefes alır": tam boyutundan büzülür, bir an ince bir disk gibi olur, sonra **ayna-tersine dönmüş** olarak yeniden açılır (bu davranış 1.4.8'deki simülasyonun B durumunda birebir izlenebilir). *(Bu hareket, cismin uzayda sadece sağa-sola gittiği sıradan bir yer değiştirme salınımı değildir. Cismin uzayımızın dokusunda boyut kaybedip-kazandığı ve içinin dışına çıktığı topolojik bir ritim olduğu için teorimizde buna doğrudan **"Boyutsal Salınım"** adını veriyoruz.)* Dönüşün kendisini gösteren hiçbir dairesel iz, hiçbir dönme düzlemi üç boyutta mevcut değildir.

## 1.4.6 Soyut Spin'e Karşı Fiziksel Çift Dönüş (Wigner'in Sınırları)

Klasik mekaniğin makroskopik cisimler (örneğin jiroskoplar) için kurduğu devinim modeli, büyük ölçüde malzemenin esnekliği ve rijit cisim kısıtlamaları üzerinden çalışır. Ancak fiziğin en büyük krizi kuantum ölçeğine inildiğinde yaşanır: **Bir elektron esnek veya rijit değildir; hiçbir uzaysal hacmi olmayan noktasal bir parçacıktır. Buna rağmen manyetik alanda kusursuz bir Larmor devinimi (precession) sergiler (Larmor, 1897).** 

Uzayda yer kaplamayan bir şeyin esnemesi veya dönmesi fiziksel olarak nasıl mümkündür? 
Fizik camiası bu krizi aşmak için Eugene Wigner'in sınıflandırmasına başvurur (Wigner, 1939): Spin, Poincaré grubunun 3 boyutlu dönme simetrisini (SO(3)) temsil eden soyut bir "kuantum etiketidir". Yani standart fiziğe göre elektron gerçekte dönmez; matematiksel olarak dönüyormuş gibi davranır. 

Evrenakı Teorisi, Wigner'in SO(3) tabanlı mükemmel matematiksel sınıflandırmasını reddetmez; aksine o kusursuz matematiğin eksik bıraktığı **ontolojik (fiziksel) sahneyi** kurar. SO(3) bizzat 3 boyutlu dönme grubudur ve matematiği eksiksizdir; ancak bu matematik, uzayımızda var olan bir elektrona uygulandığında ontolojik bir kilitlenme yaratır: Noktasal elektron varsayımı standart fiziğin kendi içinde çözümsüzdür; Evrenakı ise elektrona hem hacim (geniş bir disk) verir hem de deviniminin kökeni olan o kilitli **çift dönüşü (Double Rotation)** W ekseninde konumlandırarak SO(3) matematiğini mekanik bir sahneye taşır. Dördüncü boyut, Wigner'in soyut matematiksel spinini yeniden "gerçek bir çarka" dönüştüren kurgudur.

## 1.4.7 Çift Dönüş ve Devinimli Dönme: Açık Epürün Üç Boyutlu Sonucu

Dört boyutun üç boyutta hiçbir karşılığı olmayan en özgün hareketi **çift dönüştür** (Clifford, 1873): cisim, birbirine tamamen dik iki düzlemde (örneğin XY ve ZW) **aynı anda ve bağımsız hızlarla** dönebilir. Üç boyutta bu imkânsızdır; bir cisim aynı anda iki bağımsız düzlemde dönemez. Çift dönüşün üç boyuta yansıması ise iki bileşenin bileşkesidir:

$$\underset{\text{XY bileşeni: 3B'de görünür dönüş}}{\underbrace{x = R\cos\omega_1 t,\ y = R\sin\omega_1 t}} \qquad \underset{\text{ZW bileşeni: 3B'de Z doğrusunda salınım}}{\underbrace{z = r\cos\omega_2 t,\ w = r\sin\omega_2 t}}$$

XY bileşeni bize normal bir dönüş olarak görünür; ZW bileşeni ise görünür dönüşün eksenini Z doğrultusunda periyodik olarak modüle eder. İkisinin bileşkesi, üç boyutlu gözlemci için tektir ve tanıdıktır: dönme ekseni sabit kalmaz, koni çizerek yalpalar — yani devinim (precession). Bu nedenle teorimizde bu duruma; dördüncü boyuttaki matematiksel kökeni itibarıyla **"Çift Dönüş" (Double Rotation)**, bizim üç boyutlu uzayımızdaki gözlemsel karşılığı itibarıyla ise **"Devinimli Dönme" (Precessing Rotation)** adını veriyoruz. Aşağıdaki açık epür, üç temel durumun aksonometrik sonucunu yan yana gösterir:

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 900 330" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif">
<text x="160" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">A: 3B-içi dönüş (XY)</text>
<circle cx="160" cy="160" r="55" fill="none" stroke="#4b5563"/>
<line x1="160" y1="92" x2="160" y2="228" stroke="#cbd5e1" stroke-width="1.5"/>
<ellipse cx="160" cy="160" rx="55" ry="15" fill="none" stroke="#00e5ff" stroke-width="1.5"/>
<circle r="4.5" fill="#00e5ff">
<animateMotion dur="5s" repeatCount="indefinite" path="M 215 160 A 55 15 0 1 0 105 160 A 55 15 0 1 0 215 160"/>
</circle>
<text x="160" y="262" font-size="12" fill="#cbd5e1" text-anchor="middle">Normal dönüş</text>
<text x="160" y="280" font-size="11.5" fill="#8892b0" text-anchor="middle">eksen sabit kalır</text>
<text x="460" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">B: W'li dönüş (XW)</text>
<circle cx="460" cy="160" r="55" fill="none" stroke="#4b5563" stroke-dasharray="4 4"/>
<circle cx="460" cy="160" fill="none" stroke="#00e5ff" stroke-width="1.8">
<animate attributeName="r" values="55;13;55" keyTimes="0;0.5;1" dur="5s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</circle>
<line x1="460" y1="94" x2="460" y2="112" stroke="#8892b0"/>
<path d="M 456 110 L 460 118 L 464 110 Z" fill="#8892b0"/>
<line x1="460" y1="226" x2="460" y2="208" stroke="#8892b0"/>
<path d="M 456 210 L 460 202 L 464 210 Z" fill="#8892b0"/>
<text x="460" y="262" font-size="12" fill="#cbd5e1" text-anchor="middle">Pulsasyon — dönüş görünmez</text>
<text x="460" y="280" font-size="11.5" fill="#8892b0" text-anchor="middle">küre nefes alır, ayna-terslenir</text>
<text x="760" y="28" font-size="13" fill="#f3f4f6" text-anchor="middle">C: Çift dönüş (XY + ZW)</text>
<circle cx="760" cy="160" r="55" fill="none" stroke="#4b5563"/>
<ellipse cx="760" cy="92" rx="27" ry="8" fill="none" stroke="#4b5563" stroke-dasharray="3 3"/>
<line x1="760" y1="160" x2="733" y2="92" stroke="#4b5563" stroke-dasharray="3 3"/>
<line x1="760" y1="160" x2="787" y2="92" stroke="#4b5563" stroke-dasharray="3 3"/>
<g>
<animateTransform attributeName="transform" type="rotate" values="21.67 760 160; 0 760 160; -21.67 760 160; 0 760 160; 21.67 760 160" keyTimes="0;0.25;0.5;0.75;1" dur="4s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
<ellipse cx="760" cy="160" rx="55" ry="15" fill="none" stroke="#00e5ff" stroke-width="1.5"/>
<circle r="4.5" fill="#00e5ff">
<animateMotion dur="5s" repeatCount="indefinite" path="M 815 160 A 55 15 0 1 0 705 160 A 55 15 0 1 0 815 160"/>
</circle>
</g>
<line x1="760" y1="160" stroke="#ffb020" stroke-width="2">
<animate attributeName="x2" values="787;760;733;760;787" keyTimes="0;0.25;0.5;0.75;1" dur="4s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
<animate attributeName="y2" values="92;100;92;84;92" keyTimes="0;0.25;0.5;0.75;1" dur="4s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</line>
<circle r="4" fill="#ffb020">
<animate attributeName="cx" values="787;760;733;760;787" keyTimes="0;0.25;0.5;0.75;1" dur="4s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
<animate attributeName="cy" values="92;100;92;84;92" keyTimes="0;0.25;0.5;0.75;1" dur="4s" calcMode="spline" keySplines="0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1;0.37 0 0.63 1" repeatCount="indefinite"/>
</circle>
<text x="760" y="262" font-size="12" fill="#cbd5e1" text-anchor="middle">DEVİNİM (precession)</text>
<text x="760" y="280" font-size="11.5" fill="#8892b0" text-anchor="middle">eksen koni çizerek yalpalar</text>
</svg>
</div>
## 1.4.8 Etkileşimli Simülasyon: Dördüncü Boyuttan Üç Boyuta İniş

Aşağıdaki simülasyon, epür analizinde çıkarılan üç temel durumu tek bir etkileşimli ekranda birleştirir. Anlatım yönü bilinçli olarak **dördüncü boyuttan üç boyuta doğrudur**: sol panel, dönüşün **gerçekte yaşandığı düzlemleri** (4B gerçekliği) gösterir; sağ panel ise bu gerçekliğin `w = 0` kesitimize düşen **izdüşümünü** — yani bizim üç boyutlu uzayımızın görebildiği tek şeyi.

Üç durum:

- **Durum A — 3B-içi dönüş (XY):** Dönüş düzlemi tamamen uzayımızın içindedir; izdüşüm hiçbir şey kaybettirmez, sağda bildiğimiz normal dönüş görünür.
- **Durum B — W'li dönüş (XW):** Daire dördüncü boyut tarafındadır. Uzayımıza kalan tek iz, X doğrultusundaki salınımdır: küre X yönünde yassılaşıp yeniden açılır ve her yarım turda **ayna-tersine döner** (sağ paneldeki "R" harfinin terslenmesini izleyin — sağ el yapısının sol el yapısına dönüşmesinin göstergesidir).
- **Durum C — Çift dönüş (XY + ZW):** Dördüncü boyuta özgü hareket. XY bileşeni görünür dönüşü üretirken, ZW bileşeni görünür dönme eksenini sürekli döndürür: sonuç, **koni çizerek yalpalayan bir eksen — devinimdir (precession)**. Kısım 3'te Güneş ve Merkür/Venüs için öne sürülecek gözlemsel imza budur.

Kaydırıcılarla iki dönüşün açısal hızını (ω₁: 3B bileşeni, ω₂: W bileşeni) ve Durum C için koni açısını değiştirebilirsiniz.

<iframe src="Metin/5d_sim.html" width="100%" frameborder="0" style="height: 720px; min-height: 720px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); margin: 20px 0; border: 1px solid #333; background: #0b0f19;"></iframe>

### Simülasyonda İzlenmesi Gerekenler

1. **A'dan B'ye geçişte** soldaki daire hiç değişmez — değişen tek şey dairenin hangi düzlemde durduğudur. Buna rağmen sağdaki görüntü kökten farklılaşır: dönüş, uzayımızdan tamamen silinir ve geriye yalnızca X doğrultusunda bir yassılma/salınım kalır. Dönüşün "görünür olması", hareketin değil, **düzlemin bizim kesitimizde olup olmamasının** sonucudur.
2. **Durum B'de** ω₂'yi yavaşlatıp "R" harfini izleyin: küre her tam yassılmadan sonra ters yönde açılır — sağ-el yapısı sol-el yapısına dönüşür. Bu ayna-terslenme, hareketin gerçekten dördüncü boyuttan geçtiğinin en keskin geometrik kanıtıdır; üç boyut içindeki hiçbir dönüş bunu yapamaz.
3. **Durum C'de** ω₂ = 0'a yakın seçilirse eksen neredeyse sabitlenir (saf Durum A'ya yaklaşır); ω₂ büyüdükçe koninin taranma hızı artar. Yani devinim hızı, dönüşün **W bileşeninin büyüklüğünün doğrudan ölçüsüdür** — Kısım 3'ün gözlemsel programı açısından kritik olan nicel bağ budur.

## 1.4.9 Klasik Mekaniğin Çıkmazı: Dış Kuvvet Neden Koni Çizer?

Dönen bir topacı veya jiroskobu düşünün: Kütle-itim cismi **aşağı** doğru iter. Klasik mekaniğin en temel mantığına göre, aşağı çekilen bir cismin aşağı doğru ivmelenmesi gerekir. Ancak topaç aşağı düşmez; kütle-itim doğrultusuna 90 derece dik bir şekilde **yana** doğru kayar ve sürekli yana kayarak bir koni (devinim) çizer. Klasik fizik, bu olağanüstü durumu matematikte "Tork" tanımının içindeki **vektörel çarpım (cross product)** kuralıyla, fiziksel mekanizma göstermeksizin çözer. Kural basittir: *"Vektörel çarpımın sonucu, her iki vektöre de 90 derece dik olmak zorundadır."* Böylece denklem, aşağı çeken kuvveti — nedenselliği açıklanmaksızın — 90 derece yana saptırarak topacı düşmekten kurtarır ve ona sonsuz bir çember çizdirir.

Bu salt-formel çözümün temel nedeni, klasik fiziğin **dönmeyi bir "eksen" (tek boyutlu bir ok) zannetmesidir.** Açısal momentum, 3 boyutlu uzayda bir ok (pseudovector/sahte vektör) olarak kabul edilir. Oysa dönme bir eksen etrafında değil, daima **iki boyutlu bir düzlem içinde** gerçekleşir. 

Evrenakı teorisi bu noktada farklı bir mekanizma önerir: Devinim (yalpalama), aşağı doğru olan bir dış kuvvetin nedensellik gösterilmeden 90 derece yana sapıp cismi sarsması değildir. Devinim; cismin bizzat 4. boyuttaki **"Çift Dönüş"ünün (örneğin XY ve ZW düzlemlerindeki eşzamanlı hareketin)** bizim üç boyutlu uzayımıza düşen mecburi, doğal ve tamamen içsel izdüşümüdür. Salt formel bir kurala (vektörel çarpıma) veya dış torka ihtiyaç duymaz.

## 1.4.10 Teorinin Test Edilebilirliği ve Temel İddiamız

Bir teorinin bilimselliği, onun test edilebilir (yanlışlanabilir) somut öngörülerde bulunmasına bağlıdır. Evrenakı teorisinin 4. boyut hipotezi salt soyut bir matematiksel kurgu değildir; doğrudan laboratuvar ortamında veya uzayda test edilebilecek kesin bir kinematik iddiaya dayanır.

Bu iddia, **Devinimli Dönme (Precession)** olgusunun doğası üzerine kuruludur:

1. **Üç Boyutta Klasik Beklenti (doğru aktarımıyla):** Klasik mekanik torksuz devinimi tanır — Euler'in serbest devinimi (Poinsot hareketi): asal eksenine tam oturmamış dönen bir cismin görünür ekseni, korunan açısal momentum vektörü etrafında koni çizer; Dünya'nın Chandler yalpalaması bunun gözlenmiş örneğidir. Ancak klasik tabloda iki kesin sınır vardır: (a) **asal eksenine tam oturmuş simetrik bir cisim** için serbest devinim sıfırdır — böyle bir cismin ekseni, dış tork yokken sonsuza kadar sabit kalmak zorundadır; (b) var olan serbest devinim bile cismin iç sürtünmesi (esneklik/histerezis kayıpları) tarafından zamanla **söndürülür.**
2. **Dört Boyutta Doğallık Şartı:** Evrenakı teorisine göre ise devinimli dönme, dış bir kuvvetin veya eksen kaçıklığının eseri değil, dördüncü boyutu (W eksenini) içeren bir **"Çift Dönüş"ün en doğal, içsel ve kaçınılmaz üç boyutlu yansımasıdır.** Bu yüzden teorinin ayırt edici iddiası klasiğin iki sınırının tam üzerine kurulur: W-bileşeni taşıyan dönüş, (a) cisim asal eksenine kusursuz oturtulmuş olsa bile devinir ve (b) kaynağı içsel W-dönüşü olduğundan bu devinim **sönümlenmez.** 

**Belirleyici Deney (Experimentum Crucis):**
Bu ayırt edici fark, teoriyi doğrudan test edilebilir kılar. Ancak bu testin çok kritik mekanik bir şartı vardır: Deney sırasında nesneye dönüşü sürdürmesi için dışarıdan **sürekli bir tork (örneğin sürekli güç veren bir motor) uygulanmamalıdır.** Çünkü harici olarak uygulanan bu sürekli itki gücü, dördüncü boyutun yaratacağı o hassas doğal salınımı (devinimi) ezecek ve baskılayacaktır. 

Bu nedenle deney; ya (bir topaç gibi) ilk ivmesi verilip **serbest dönüşe bırakılmış** nesnelerle ya da atom altı parçacıklar ve gök cisimleri gibi **kendiliğinden dönen** yapılarla yapılmalıdır.

Eğer böyle serbest dönen bir nesne; kütle-itim, manyetik alan ve diğer tüm harici fiziksel etkilerden **tamamen yalıtılmış** bir ortamda (örneğin derin uzay boşluğundaki kusursuz bir vakum odasında) gözlemlenirse, klasik fiziğe göre: **asal eksenine oturtulmuş simetrik bir cismin** ekseni sabit kalmalı; kasıtlı eksen kaçıklığıyla başlatılan serbest devinim ise iç sürtünmeyle zamanla sönmelidir. Evrenakı teorisi bu iki noktada da son derece iddialıdır: Eğer nesnenin geometrik yapısı içsel bir dördüncü boyut bileşenine (Çift Dönüşe) sahipse, asal-eksen dönüşünde bile, hiçbir dış kuvvet olmamasına rağmen bu serbest cisim **kendi kendine devinim (yalpalama) yapacak ve bu devinim sönümlenmeyecektir.** Deneyin ayırt edici imzası dolayısıyla iki katmanlıdır: devinimin *varlığı* (asal-eksen konfigürasyonunda) ve *kalıcılığı* (sönümsüzlük).

Gök cisimlerinde ve nükleonlarda gözlemlediğimiz, kökeni standart fizikte kafa karışıklığı yaratan yalpalamaların (precession) sırrı buradadır. Bütün dış etkilerden uzak yapılacak hassas dönme deneyleri bu iddiayı doğrudan sınayacaktır: teori, yalıtılmış serbest dönüşte net bir devinim imzası öngörür. Bu imza gözlenirse dördüncü boyutlu Çift Dönüş modeli güçlü bir doğrulama kazanır; eksen mutlak sabit kalırsa teori bu noktada yanlışlanmış olur.

## 1.4.11 Sonuç: Üç İzdüşüm İmzası ve Kısımlara Köprü

Epür analizinin bütün sonucu tek cümlede toplanır: **dördüncü boyuttaki bir dönüş, üç boyutta asla "dönüş" olarak görünmez; kendini ancak dolaylı imzalarıyla ele verir.** Bu imzalar üç tanedir:

1. **Boyutsal Salınım (Pulsasyon):** Saf W'li dönüşün (XW, YW, ZW) tek görünür izi, dönüş düzleminin üç boyutla kesişim doğrusu üzerindeki sinüs salınımıdır.
2. **Ayna-terslenme:** W'de yarım tur atan bir cisim, üç boyuta ayna görüntüsü olarak geri döner (sağ eldiven sol eldivene dönüşür) — bu, hareketin gerçekten dördüncü boyuttan geçtiğinin en keskin geometrik kanıtıdır.
3. **Devinimli Dönme:** Bir cisim hem üç boyut içinde dönüyor hem de dönüşünün bir bileşeni W'ye taşmışsa (çift dönüş), görünür dönme ekseni sabit kalamaz; koni çizerek yalpalar.

Bu üç imza, izleyen kısımların başvuru tanımlarıdır. Mikro evrende (Kısım 2) Zerre'nin ve nükleonların çift dönüşü bu imzalar üzerinden okunacak; makro evrende (Kısım 3) ise üçüncü imza merkeze alınacaktır: eğer nükleonların ve gök cisimlerinin dönüşleri salt üç boyutlu değilse ve dördüncü uzanımsal boyutta bir dönüş bileşeni taşıyorsa, bunun kaçınılmaz ve ölçülebilir sonucu, her ölçekte gözlenen **eksen devinimidir** — Güneş'in yalpalaması ve Merkür ile Venüs'ün alışılmadık yörünge davranışları dahil. Devinim, bu çerçevede yalnızca bir tork sonucu değil; dönüşün dördüncü boyuttaki bileşeninin üç boyuta düşen zorunlu gölgesidir ve bu iddia, Kısım 5'teki gözlemsel programın doğrudan sınama konusudur.

