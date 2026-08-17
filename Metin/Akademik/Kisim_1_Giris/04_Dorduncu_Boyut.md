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

Ve bu sahne kurulduğu anda ölçülebilir bir sonuç da doğar: elektron **devindiği için hem bileşik hem asimetriktir.** Devinim ⟺ iç asimetri ⟹ bileşiklik ölçütü gereği (Oe-5; bkz. 1.4.7), bölünemeyen temel parçacık (Kut) devinemez; onun payına yalnızca boyutsal salınım, yani Salınımlı Dönme düşer. Aynı şekilde, ışık katarının mermisi olan **Zerre** de bileşik olmasına rağmen kusursuz eksenel simetrisi ($D_{XW}=0$) nedeniyle devinmez (polarizasyonunu bu sayede korur). Standart fiziğin "nokta parçacık" saydığı elektron ise, teoride Kutlardan kurulu asimetrik (kutuplu) bir yapılanmadır; Larmor devinimi bunun doğrudan imzasıdır.

## 1.4.7 Çift Dönüş ve Devinimli Dönme: Açık Epürün Üç Boyutlu Sonucu

Dört boyutun üç boyutta hiçbir karşılığı olmayan en özgün hareketi **çift dönüştür** (Clifford, 1873): cisim, birbirine tamamen dik iki düzlemde (örneğin XY ve ZW) **aynı anda ve kinematik olarak bağımsız hızlarla** dönebilir. Üç boyutta bu imkânsızdır; bir cisim aynı anda iki bağımsız düzlemde dönemez. *(Kinematik bağımsızlık dinamik bağımsızlık demek değildir: cisim **rijit ve serbest** ise iki hızın oranı serbest kalmaz, gövdenin kendi kütle dağılımı tarafından kilitlenir — 1.4.8 md.3.)* Çift dönüşün üç boyuta yansıması ise iki bileşenin bileşkesidir:

$$\underset{\text{XY bileşeni: 3B'de görünür dönüş}}{\underbrace{x = R\cos\omega_1 t,\ y = R\sin\omega_1 t}} \qquad \underset{\text{ZW bileşeni: 3B'de Z doğrusunda salınım}}{\underbrace{z = r\cos\omega_2 t,\ w = r\sin\omega_2 t}}$$

XY bileşeni bize normal bir dönüş olarak görünür; ZW bileşeni ise Z doğrultusunu periyodik olarak modüle eder. Bu nedenle teorimizde bu duruma; dördüncü boyuttaki matematiksel kökeni itibarıyla **"Çift Dönüş" (Double Rotation)**, bizim üç boyutlu uzayımızdaki gözlemsel karşılığı itibarıyla ise **"Devinimli Dönme" (Precessing Rotation)** adını veriyoruz.

Bu ad **asimetrik bileşik** gövdelere aittir. Teorinin bölünemeyen temel parçacığı olan **Kut**'de ve kusursuz simetriye sahip olan **Zerre**'de ise W dağılımı figür ekseni etrafında tam simetriktir: eksen kıpırdamaz ve geriye yalnızca boyutsal salınım kalır. Bu hâle **"Salınımlı Dönme" (Oscillatory Rotation)** adını veriyoruz. İki adın ayrımı, aşağıdaki kutunun iki satırının ta kendisidir ve teoride bir ölçüt olarak kullanılır (Oe-5): **devinim ⟺ iç asimetri ($D_{XW}\neq0$) ⟹ bileşiklik.** Boyutsal salınım dört boyutlu olmanın imzasıdır ve her gövdede bulunur; devinim ise yalnızca asimetrik bir iç yapısı olanda görünür. Temel parçacık (Kut) devinemez. Ölçüt tek yönlü okunur: devindiği görülen her gövde bileşiktir, ama her bileşik gövde devinmez — kusursuz simetrisi sayesinde doğrusal polarizasyonunu milyarlarca yıl taşıyabilen **Zerre** bunun en mükemmel örneğidir.

> [!IMPORTANT]
> **ZW bileşeni Z'nin uzunluğunu değiştirir, yönünü değil — ve ayrım bu bölümün belkemiğidir.**
>
> Bir noktanın hızı, ZW dönüşü altında $v_z=-\omega_2w$, $v_w=+\omega_2z$, ve **$v_x=v_y=0$**'dır: ZW düzlemi X ile Y'ye hiç dokunmaz. Kesitimizde ($w=0$) görünen hız alanı bu yüzden $(-\omega_1y,\;+\omega_1x,\;0)$ — saf Z etrafında dönüş. Ekseni **eğmek** için Z ile X (ya da Y) arasında kuplaj, yani bir XZ/YZ bileşeni gerekir; ZW tam olarak bunlara diktir.
>
> Sonuç, 1.4.3'ün altı-düzlem tablosuyla birebir aynıdır ve iki koşulda ayrışır:
>
> | Gövdenin W dağılımı | 3B'de görünen |
> |---|---|
> | figür ekseni etrafında **tam simetrik** | yalnız **boyutsal salınım** (imza 1) ve ayna-terslenme (imza 2); eksen **tam sabit** — *Salınımlı Dönme; Kut'un ve Zerre'nin hâli* |
> | **asimetrik** ($D_{XW}\neq0$) | eksen oynar — ama **doğrusal salınım** olarak, koni olarak değil (1.4.8); *Devinimli Dönme; bileşiklerin hâli* |
>
> Yani çift dönüşün ekseni oynatması için gövdenin W'deki dağılımının kendi dönme ekseni etrafında simetrik **olmaması** gerekir; ve o hâlde bile hareket bir koni değil, bir **doğru parçası üzerinde ileri-geri salınımdır.** Bu ayrım kaybedilmemelidir: koni klasik serbest devinimle dejeneredir, doğrusal salınım **değildir** (11.7.6).

Aşağıdaki açık epür, üç temel durumun aksonometrik sonucunu yan yana gösterir:

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
- **Durum C — Çift dönüş (XY + ZW):** Dördüncü boyuta özgü hareket. XY bileşeni görünür dönüşü üretir; ZW bileşeni ise Z doğrultusunu modüle eder. *(Epürün sağ paneli, ekseni oynatan genel durumu canlandırır. Kesin sonuç yukarıdaki kutudadır ve iki koşulludur: gövdenin W dağılımı figür ekseni etrafında **simetrikse** eksen sabit kalır ve geriye yalnız boyutsal salınım kalır; **asimetrikse** eksen bir yay üzerinde **doğrusal** olarak salınır — koni çizmez. Nicel yasa 1.4.8'dedir.)*

Kaydırıcılarla iki dönüşün açısal hızını (ω₁: 3B bileşeni, ω₂: W bileşeni) ve Durum C için koni açısını değiştirebilirsiniz.

<iframe src="Metin/5d_sim.html" width="100%" frameborder="0" style="height: 720px; min-height: 720px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); margin: 20px 0; border: 1px solid #333; background: #0b0f19;"></iframe>

### Simülasyonda İzlenmesi Gerekenler

1. **A'dan B'ye geçişte** soldaki daire hiç değişmez — değişen tek şey dairenin hangi düzlemde durduğudur. Buna rağmen sağdaki görüntü kökten farklılaşır: dönüş, uzayımızdan tamamen silinir ve geriye yalnızca X doğrultusunda bir yassılma/salınım kalır. Dönüşün "görünür olması", hareketin değil, **düzlemin bizim kesitimizde olup olmamasının** sonucudur.
2. **Durum B'de** ω₂'yi yavaşlatıp "R" harfini izleyin: küre her tam yassılmadan sonra ters yönde açılır — sağ-el yapısı sol-el yapısına dönüşür. Bu ayna-terslenme, hareketin gerçekten dördüncü boyuttan geçtiğinin en keskin geometrik kanıtıdır; üç boyut içindeki hiçbir dönüş bunu yapamaz.
3. **Durum C'de** ω₂ = 0'a yakın seçilirse eksen neredeyse sabitlenir (saf Durum A'ya yaklaşır); ω₂ büyüdükçe koninin taranma hızı artar. Yani devinim hızı, dönüşün **W bileşeninin büyüklüğünün doğrudan ölçüsüdür** — ve bu bağ artık niteliksel değil, aşağıda **niceliksel** olarak yazılır.

### Nicel bağ: $\omega_2/\omega_1$ serbest değildir

Yukarıdaki üç madde kaydırıcıların davranışını anlatır; kaydırıcıda $\omega_1$ ile $\omega_2$ ayrı ayrı seçilebilir çünkü **kinematik** olarak bağımsızdırlar. Ama sınanacak olan şey bir simülasyon değil, **rijit ve serbest** bir cisimdir — ve orada oran serbest kalmaz.

**Neden kilitlenir.** Dört boyutlu bir dönüşün iki değişmez düzlem hızı ile üç boyutlu rijit cisim hareketi arasında bir sözlük vardır. Serbest bir simetrik topacın **duruşu** — dönme açısı $\phi$, eğim $\theta$, öz-dönme $\psi$ — dört boyutlu dönüş grubunun tek-parametreli bir altgrubudur, yani tam olarak bir çift dönüştür; iki değişmez düzlemin hızları $(\dot\phi\mp\dot\psi)/2$ çıkar. Serbest topaçta $|\dot\psi| = \dot\phi\cos\theta\cdot\varepsilon$ olduğundan ($\varepsilon=(C-A)/C$, gövdenin **dinamik eliptikliği**) sonuç kapalı bir bağıntıdır:

$$\boxed{\;\frac{\omega_2}{\omega_1}=\varepsilon\cos\theta\;}$$

**Üç sonucu vardır ve üçü de epürün kendisini açıklar.**

- **Durum C'nin $\omega_2\to0$ ucu artık türetilmiştir:** $\varepsilon\to0$ demek $C=A$ demektir, yani atalet bakımından küresel bir cisim. Böyle bir cisimde iki düzlem hızı eşitlenir — dönüş **izoklin** olur — ve üç boyutlu izdüşümü saf dönüştür, koni taranmaz. *"$\omega_2$ sıfıra giderken eksen sabitlenir"* bir kaydırıcı gözlemi değil, bir teoremdir.
- **Devinim hızının ölçüsü W bileşenidir — ve W bileşeninin ölçüsü basıklıktır.** Zincir kapanır: gövde ne kadar basıksa çift dönüşü izoklinlikten o kadar sapar, koni o kadar hızlı taranır.
- **Koni açısı $\theta$ bağıntıya çarpan olarak girer, ondan çıkmaz.** Yani bağıntı **hızı** verir, **genliği** vermez. Bu ayrım 1.4.10'un belirleyici deneyini doğrudan biçimlendirir.

> **Dürüstlük kaydı — ispatın hangi cebirde yürüdüğü.** Yukarıdaki sözlük, dört boyutlu dönüş grubunun kuaterniyon cebiri üzerindeki gerçeklemesiyle kurulur ve orada dördüncü koordinat **duruş** değişkenidir, maddenin içine uzandığı W ekseni değil. Dolayısıyla elde edilen şey **cebirsel bir özdeşliktir**: çift dönüşün iki hızı ile serbest devinim arasındaki bağ kesindir. Fiziksel W dönüşünün *aynı* cebiri ürettiği ayrı bir adımdır ve burada gösterilmemiştir — Postülat 2'nin uzanımsal W'si ile bu gerçekleme arasındaki köprü **açık kalemdir** (7.4). Bağıntının gökteki sınavı Kısım XI'dedir (11.7.6) ve orada binde iki ile tutar.
>
> Ve bir sınır: özdeşlik **simetrik** topaç için kesindir. Üç eksenli gövdede hareket iki bağımsız frekanslıdır ve duruş artık tek-parametreli bir altgrup değildir. Hıza etkisi ikinci mertebedir — Dünya'da $\%0{,}0006$ — dolayısıyla bağıntı ayakta kalır, grup-kuramsal ifade zayıflar.

### W asimetrisi kanalı: eksenin gerçek 4B izi · **[T]**

Yukarıdaki kutuda kaydedildiği gibi, gövdenin W dağılımı figür ekseni etrafında **tam simetrikse** eksen kıpırdamaz. Ama böyle bir simetriyi gerektiren hiçbir şey yoktur: bir gövdenin dördüncü boyuttaki dağılımının, üç boyutta seçtiği dönme ekseni etrafında simetrik olması için sebep bulunmaz. Simetri kırıldığında kanal açılır ve kırılmanın ölçüsü tek bir çapraz momenttir:

$$\delta\;\equiv\;\frac{D_{XW}}{D_{XX}},\qquad D_{XW}=\int\rho\,x\,w\,dV$$

**Serbest 4B cisim dinamiği** (so(4) Euler–Arnold denklemi) bu kurulumda kapalı bir sonuç verir:

$$\boxed{\;\theta \;=\; 0{,}1806\;\delta\ \ \text{radyan},\qquad \text{taranma hızı}=\omega_2\;}$$

Üç özelliği kaydedilmelidir; üçü de sayısal olarak sınanmıştır:

- **Genlik asimetriyle doğrusaldır** — katsayı $\delta=10^{-6}$'dan $10^{-1}$'e beş mertebe boyunca sabittir. $\delta=0$'da hareket **tam sıfırdır.**
- **Genlik $\omega_2$'den bağımsızdır**; $\omega_2$ yalnızca **hızı** belirler. Yani genliği geometri, ritmi W dönüşü verir.
- **Polarizasyon doğrusaldır.** Eksenin izi bir büyük-çember yayı üzerinde ileri-geri gider; yassılığı $10^{-3}$–$10^{-7}$ ölçülmüştür (koni için bu sayı $1$ olurdu).

> **Ve bu kanalın asıl işi ayrı bir olgu üretmek değil, var olanı BESLEMEKTİR.** Doğrusal bir zorlama, serbest devinim rezonansını uyardığında **dairesel** bir yanıt üretir: rezonans yalnız prograde tarafta olduğu için retrograde yarıyı keser. Yani içkin kanal, gövdenin kendi serbest yalpalamasının **sürücüsüdür** — ve bu, sönümsüzlük iddiasını bir gözlemden bir mekanizmaya çevirir. Dünya'da karşılığı Chandler yalpalamasıdır: klasik tabloda $11$–$38$ yılda sönmesi gerekirken $120$ yıldır sönmemiştir, ve rezonans gereken asimetriyi yüz kat düşürür ($\delta\approx5{,}4\times10^{-8}$).
>
> **Ama sürüş okuması gerçek veriyle sınandı ve düştü.** Determinist bir sürücü rezonansın fazını kilitlerdi; 127 yıllık IERS serisi bunu **dışlıyor** ve ilk gözlemsel sınırı veriyor: $\delta\lesssim1{,}6\times10^{-9}$ (11.7.6). **Kanalın doğru işi sürmek değil, sönümü iptal etmektir** — anti-sönüm faz dayatmaz, yalpalama kendi fazıyla sürüklenir **ama sönmez**, ki bu zaten 1.4.10'un cümlesidir. Gözlem buna izin verir: $30\lesssim Q_{etkin}\lesssim1000$, klasik bandın on katına kadar.

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

Gök cisimlerinde gözlemlediğimiz, kökeni standart fizikte kafa karışıklığı yaratan yalpalamaların (precession) **sırrı buradadır** *(nükleonun kendi durumu ayrıdır ve aşağıda 1.4.11'de ayrıca kurulur: orada kapanan şey 4B kanalıdır, gövdenin devinme yeteneği değil)* — ve bu iddianın en keskin gözlemsel adresi, aşağıda ayrılan iki olgu sınıfının **ikincisidir.** Bütün dış etkilerden uzak yapılacak hassas dönme deneyleri bu iddiayı doğrudan sınayacaktır: teori, yalıtılmış serbest dönüşte net bir devinim imzası öngörür. Bu imza gözlenirse dördüncü boyutlu Çift Dönüş modeli güçlü bir doğrulama kazanır; eksen mutlak sabit kalırsa teori bu noktada yanlışlanmış olur.

> [!IMPORTANT]
> **İki olgu sınıfı ayrılmalıdır — çünkü klasik tork kanalı yalnız birine girebilir.**
>
> Gözlenen eksen yalpalamaları tek bir olgu değildir. Cismin bir **tork ortamı** varsa — yakın, kütleli komşular ve basık bir figür — klasik bir kanal da açıktır; yoksa açık değildir:
>
> | Sınıf | Gözlenen örnek | Klasik tork kanalı |
> |---|---|---|
> | **Zorlanmış devinim** | Dünya'nın luni-solar devinimi | **açık** |
> | **Serbest devinim** | Dünya'nın **Chandler yalpalaması** · izole pulsar **PSR B1828-11** | **yapısal olarak kapalı** — serbest devinim torkla üretilmez |
>
> **Yukarıdaki iddia ve Belirleyici Deney ikinci satıra aittir.** Bir cismin tork ortamı varsa içkin kanal onun gölgesinde kalır; **tork ortamının bulunmadığı yerde ise rakibi yoktur** — ve orada iddianın en keskin ayağı sönümsüzlüktür: klasik tabloda serbest devinim iç sürtünmeyle söner, teoride sönmez.

> [!WARNING]
> **Deneyin hangi katmanı ayrıştırır, hangisi ayrıştırmaz — 1.4.8'in nicel bağından sonra.**
>
> $\omega_2/\omega_1=\varepsilon\cos\theta$ bağıntısı devinimin **hızını** gövdenin kütle dağılımına kilitler, ve o hız klasik serbest devinimin verdiğiyle **özdeştir** (Kısım XI, 11.7.6: Dünya'da binde iki). Dolayısıyla yukarıda sayılan iki katmandan **yalnız biri ölçtüğü şeyi ayrıştırır**:
>
> | Katman | Ayrıştırır mı? | Neden |
> |---|---|---|
> | Devinimin **hızı** | **Hayır** | $\varepsilon\cos\theta$ ile kilitli; klasik sonuçla özdeş |
> | Devinimin **varlığı** ($\theta=0$ konfigürasyonunda) | **EVET** | bağıntı $\theta$'yı **çarpan** olarak taşır, üretmez; klasikte $\theta$ bir başlangıç koşuludur ve sıfırsa sıfır kalır. Teori $\theta$'nın kendiliğinden sıfırdan farklı olmasını gerektirir |
> | Devinimin **kalıcılığı** (sönümsüzlük) | **EVET** | klasik tabloda iç sürtünme söndürür |
>
> Bu, deneyi zayıflatmaz — **hedefini keskinleştirir.** Ölçülecek şey koninin ne kadar hızlı tarandığı değil, hareketin **varlığı, polarizasyonu ve kalıcılığıdır.**

> [!IMPORTANT]
> **Deneyin aradığı üç imza — ve hiçbiri koni değil.**
>
> 1.4.8'in W-asimetrisi kanalı, yalıtılmış cisim deneyinin ne ölçmesi gerektiğini kesinleştirir:
>
> | Aranan | Teorinin öngörüsü | Klasik beklenti |
> |---|---|---|
> | **Boyutsal salınım** (gövdenin 3B boyunun ritmik değişimi) | var, $\omega_2$ ritminde | **yok** — hiçbir klasik mekanizma üretmez |
> | **Ayna-terslenme** (yarım turda sağ-el ⟶ sol-el) | var | **yok** |
> | **Eksen hareketinin polarizasyonu** | **doğrusal** (yay), genlik $0{,}1806\,\delta$ | serbest devinim daima **dairesel** (yassılık $\approx1$) |
> | **Sönümsüzlük** | söner değil | iç sürtünme söndürür |
>
> Kusursuz simetrik bir cisimde ($\delta=0$) eksen hiç kıpırdamaz; dolayısıyla deneyin eksen ayağı aslında **W dağılımının asimetrisini ölçer.** Bu, iddiayı zayıflatmaz — **ölçülebilir bir niceliğe bağlar:** gözlenen genlikten $\delta$ doğrudan okunur, gözlenmezse $\delta$'ya üst sınır konur.
>
> Ve laboratuvar cismi burada gökten üstündür: $\delta$ gökte gövdenin verilmiş bir özelliğidir, laboratuvarda ise **numune seçilerek değiştirilebilir** — genliğin $\delta$ ile doğrusal değişmesi, imzanın kendisinden bağımsız ikinci bir sınavdır.
>
> Her iki sınıfın nicel muhasebesi — hangi payın ne kadar olduğu, hangi sayının teorinin kendi çıktısı olduğu, ve sönümsüzlük iddiasının şu andaki gözlemsel durumu — **Kısım XI'in işidir ve orada yapılmıştır** (11.7.3 zorlanmış olgu, 11.7.6 serbest olgu). Bu bölümün kurduğu şey mekanizmadır; ölçüm oraya aittir.

## 1.4.11 Sonuç: Üç İzdüşüm İmzası ve Kısımlara Köprü

Epür analizinin bütün sonucu tek cümlede toplanır: **dördüncü boyuttaki bir dönüş, üç boyutta asla "dönüş" olarak görünmez; kendini ancak dolaylı imzalarıyla ele verir.** Bu imzalar üç tanedir:

1. **Boyutsal Salınım (Pulsasyon):** Saf W'li dönüşün (XW, YW, ZW) tek görünür izi, dönüş düzleminin üç boyutla kesişim doğrusu üzerindeki sinüs salınımıdır.
2. **Ayna-terslenme:** W'de yarım tur atan bir cisim, üç boyuta ayna görüntüsü olarak geri döner (sağ eldiven sol eldivene dönüşür) — bu, hareketin gerçekten dördüncü boyuttan geçtiğinin en keskin geometrik kanıtıdır.
3. **Eksenin Doğrusal Salınımı:** Bir cisim hem üç boyut içinde dönüyor hem de dönüşünün bir bileşeni W'ye taşmışsa (çift dönüş), **ve W'deki dağılımı dönme ekseni etrafında simetrik değilse**, görünür eksen sabit kalamaz: bir yay üzerinde ileri-geri salınır. Genliği asimetriyle doğrusaldır ($\theta=0{,}1806\,\delta$), ritmi $\omega_2$'dir, ve **polarizasyonu doğrusaldır** — klasik serbest devinim daima dairesel olduğu için ayrışan imza budur (1.4.8, 11.7.6). *(Simetrik cisimde eksen kıpırdamaz; o hâlde geriye yalnız birinci ve ikinci imza kalır.)*

Bu üç imza, izleyen kısımların başvuru tanımlarıdır. Mikro evrende (Kısım 2) Zerre'nin ve nükleonların çift dönüşü bu imzalar üzerinden okunacak; makro evrende ise **birinci ve üçüncü imza birlikte** çalışır. Birinci imzanın makro muhasebesi şaşırtıcıdır: nükleon pulsasyonunun **salınan** payı rastgele fazlar yüzünden $1/\sqrt N$ ile bastırılır ($10^{-26}$ mertebesi) — bu yüzden makro cisim nefes almaz, ve gözlem bunu doğrular. Ama pulsasyonun **kalıcı** payı kaybolmaz: kütle-itimin ta kendisini kurar. Mekanizması ve matematiği **1.4.12**'dedir — ve teorinin belkemiği orasıdır. Üçüncü imza ise, gövdenin W dağılımı dönme ekseni etrafında simetrik değilse, $\omega_2$ ritminde doğrusal bir **eksen salınımı** öngörür; ve o salınım, gövdenin serbest devinim rezonansını uyararak **yalpalamanın sürücüsü** olur — sönümsüzlüğün mekanizması budur (11.7.6). **Ve iki olgu sınıfı ayrı okunmalıdır** (1.4.10'un kutusu): tork ortamı bulunan gövdelerin **zorlanmış** deviniminde klasik kanal baskındır (11.7.3); **serbest** devinimde ise o kanal yapısal olarak kapalıdır ve içkin kanal rakipsizdir — Dünya'nın Chandler yalpalaması ve izole pulsar PSR B1828-11 bu sınıftadır (11.7.6). Bu yüzden iddia, Kısım 5'teki gözlemsel programın doğrudan sınama konusudur; sınavın en temiz biçimi **yalıtılmış laboratuvar cismidir**, ama gökte de rakipsiz olduğu bir adresi vardır.


---

## 1.4.12 Birinci İmzanın Bedeli: Pulsasyon Kütle-İtimi Nasıl Kurar

Bu bölüm kitabın belkemiğidir. Üç imzadan **birincisi** — boyutsal salınım — üç boyutta yalnız bir titreşim olarak görünür; ama makro ölçekte bıraktığı iz titreşim değildir. **Kütle-itimin kendisidir.** Zincir burada baştan sona kurulur.

### Önce bir yanlış okuma elenmeli: ortada nehir yok

Kütle-itimin alanı M-35'te bir **kaynak şiddetiyle** yazılır: nükleon başına $q_n$, ve $N$ nükleon için

$$\Phi_q(r)=\frac{N q_n}{4\pi r^{2}},\qquad \frac{dP}{dr}=+\,C\,\Phi_q(r)
\quad\Longrightarrow\quad P(r)=P_0-\frac{C N q_n}{4\pi r}$$

$q_n$'in birimi m³/s'dir ve bu, onu bir **taşıma debisi** — ortamdan sürekli akan bir nehir — sanmaya davet eder. **O okuma yanlıştır, ve teorinin kendi rakamıyla elenir.**

Dünya için $Nq_n=5{,}78\times10^{32}$ m³/s'dir. Bu gerçekten taşınan bir hacim olsaydı, yüzeyden geçmesi gereken radyal hız

$$v=\frac{Nq_n}{4\pi R_\oplus^{2}}=1{,}13\times10^{18}\ \mathrm{m/s}=3{,}8\times10^{9}\,c_0$$

olurdu. Oysa teorinin **kendi** ortam hızı DY-1'den bellidir: $v_\theta=2\sqrt{\mathcal{G}M/R}=1{,}58\times10^{4}$ m/s. Aradaki fark **on dört mertebedir.**

> $$\boxed{\;\text{Nehir okuması, teorinin kendi ortam hızıyla } 10^{13{,}9} \text{ kat çelişir. } q_n \text{ bir taşıma debisi DEĞİLDİR.}\;}$$

### Doğru okuma: durgun denge, akan bir şey yok

Evrenakı'nın bir yerden gelmesi gerekmez; **hiçbir yere gitmez de.** Nükleon ortamı deplase eder, arka plan basıncı geri iter, ve ikisi bir **durgun denge gradyanında** buluşur. Alan gerçektir, akış değildir.

Bu, hidrostatiğin sıradan bir gerçeğidir: atmosferde basınç gradyanı vardır ve hiçbir şey akmaz — yerçekimi ile gradyan dengededir. Burada dengeyi kuran şey yerçekimi değil, nükleonun kesintisiz çalışan pompasıdır. $q_n$ o pompanın **şiddetidir**, taşıdığı miktar değil; birimi m³/s çıkar çünkü kaynak terimi öyle normalize edilir ($\nabla^2\chi=-q_nn_m$, M-46).

Ve bu okuma üç soruyu birden düşürür: *"Evrenakı nereden geliyor?"* (hiçbir yerden — taşınan yok), *"nereye gidiyor?"* (hiçbir yere), *"korunum ihlal ediliyor mu?"* (hayır — $\nabla^2P=0$ kaynaksız bölgede zaten sağlanır ve taşıma olmadığı için içeride de bir madde açığı doğmaz).

### Kaynak şiddeti türetilmiştir — sıfır serbest parametreyle

Zincirin gücü buradadır: $q_n$ ölçülmüş bir sayı değil, **türetilmiş** bir sayıdır.

| Girdi | Değer | Statüsü |
|---|---|---|
| $v_t=\sqrt2\,c_0$ — girdap duvarının denge hızı | $4{,}2397\times10^{8}$ m/s | **türetilmiş** (Ek A.2) |
| $u_r/v_t=\sqrt{m_p/m_e}$ — eş-güç kilidi | $42{,}8504$ | **türetilmiş** (M-45) |
| $r_n$ — nükleon yarıçapı | $0{,}8414$ fm | ölçüm |

$$q_n=4\pi r_n^{2}\,u_r=4\pi r_n^{2}\,\sqrt2\,c_0\,\sqrt{\tfrac{m_p}{m_e}}
=\mathbf{1{,}616\times10^{-19}\ m^{3}/s}$$

Aynı zincir dolanım kolunu da verir: $\gamma_n=2\pi r_n v_t=2{,}241\times10^{-6}$ m²/s, ve iki kolun oranı $\ell_\omega=q_n/2\gamma_n=r_n\sqrt{m_p/m_e}=36{,}05$ fm. **Üç sayı, tek bir çapadan, serbest parametresiz.**

### Ve nükleonun 4B kanalı devinim değil, yalnız pulsasyon üretir

Burada teorinin kendi kilidi çarpıcı bir sonuç verir. Her kol kendi yarıçapında okunduğunda:

$$\omega_1=\frac{v_t}{r_n},\qquad
\omega_2=\frac{u_r}{\ell_\omega}=\frac{\sqrt{m_p/m_e}\;v_t}{\sqrt{m_p/m_e}\;r_n}=\frac{v_t}{r_n}
\quad\Longrightarrow\quad \boxed{\;\omega_2=\omega_1\;}$$

Eşitlik sayısal bir tesadüf değil, **cebirsel bir özdeşliktir**: $\sqrt{m_p/m_e}$ pay ve paydada sadeleşir. Yani nükleonun çift dönüşü **tam izoklindir** ($5{,}0389\times10^{23}$ rad/s, iki kolda da).

> **Sembol kaydı — $\omega_1$, Compton frekansının adı değildir.** Bu kitapta $\omega_1$ ve $\omega_2$ yalnızca 4B çift dönüşün 3B-içi ve W-eksenli bileşenlerini gösterir; ikisi de yukarıdaki gibi duvar hızı yasasından ($\Omega=\sqrt2\,c_0/r$, M-3) okunan **hızlardır**, frekans değil. İkisi arasında bir hız hiyerarşisi de yoktur — nükleonda $\omega_2=\omega_1$'dir. Standart fiziğin Compton frekansı, bu hızlardan **türetilen** frekansın gözlemsel sağlama noktasıdır; teorinin çapası değildir.

Ve izoklin çift dönüşün üç boyuta düşen izi 1.4.8'de kesinleştirilmişti: **saf dönüş artı saf pulsasyon, eksen hareketi sıfır.** Buradan yapısal bir sonuç çıkar:

> **Nükleonun 4B kanalı kütle-itim üretir, devinim üretmez.** İzoklinlik bunu bir seçim olmaktan çıkarıp bir teoreme dönüştürür: eş-güç kilidi iki kolu eşitlediği anda, W bileşeninin üç boyuttaki bütün payı pulsasyona — yani F1'e — gider.

> **Teoremin kapsamı — dikkat.** Yukarıdaki sonuç **W kanalı hakkındadır**; nükleonun kusursuz bir küre olduğunu söylemez ve devinemeyeceği anlamına gelmez. Nükleon kompozit bir girdaptır; iç yapısı (standart fiziğin kuark dediği akış deseni) onu ideal küreden ayırır, dolayısıyla $\varepsilon=(C-A)/C\neq0$'dır ve gövde kendi figüründen doğan devinimi sergileyebilir — tıpkı Dünya gibi, tıpkı bileşik çekirdekler gibi. Kapanan şey yalnızca **4B kanalının devinime katkısıdır**; klasik figür kanalı açık kalır. Bu ayrım teorinin genel kuralını bozmaz, tersine tamamlar: **devinim ölçekten değil, gövdenin kendi figüründen doğar.**

Teorinin iki ayrı yerde bağımsız olarak kurduğu şey burada tek noktada buluşur: M-45'in eş-güç kilidi (mikro) ile izoklin dönüşün izdüşüm teoremi (geometri), aynı sonucu verir.

### Makroya geçiş: neden gezegen nefes almaz ama çeker

Nükleonun pulsasyonu iki paya ayrılır ve ikisi makroda **taban tabana zıt** davranır:

| Pay | Faz bağımlılığı | Toplanma | Dünya'da ($N=3{,}57\times10^{51}$) |
|---|---|---|---|
| **salınan (AC)** | fazlar rastgele | $\sqrt N$ ⟹ göreli genlik $1/\sqrt N$ | $1{,}7\times10^{-26}$ ⟹ **kaybolur** |
| **kalıcı (DC)** — kaynak şiddeti | faz**sız** bir skalerdir | **doğrusal**, $N$ kat | $Nq_n$ ⟹ **kütle-itim** |

Bu, gözlemin dayattığı iki şeyi aynı anda verir: gezegenler görünür biçimde **nefes almaz** (AC payı ölür), ama kütleleriyle orantılı bir alan **kurar** (DC payı doğrusal toplanır). Ve toplanmanın doğrusallığı bir varsayım değil, kaynak şiddetinin skaler olmasının sonucudur — dolanım kolu $\gamma_n$ ise vektörel olduğu için $\sqrt N$ ile toplanır ve makroda 34 mertebe geride kalır (11.3.7).

### Bölümün tek cümlesi

*Dördüncü boyuttaki dönüşün üç boyuta düşen birinci imzası bir titreşimdir; o titreşimin salınan payı kalabalıkta kaybolur, kalıcı payı ise doğrusal toplanarak evrendeki en tanıdık kuvveti kurar — ve o payın şiddeti, tek bir denge hızından serbest parametresiz türetilir.*

> [!WARNING]
### Zincirin açık halkası: aranan şey bir sabit değil, **ortamın kendi ölçeğidir**

Yukarıda **türetilmiş** olan şey kaynağın *şiddetidir* ($q_n$). Şiddeti basınca çeviren katsayı $C$ ise türetilmemiştir; değeri kütle-itim katsayısının ölçülen yerel değerinden geri çözülür ($C=2{,}343$) ve Ek C'de $(Cq_n)$ çifti **[F]** sayılmaya devam eder.

**Ama bu kalemin doğru adı $C$ değildir.** Postülat 4 gereği aranan şey evrensel bir sabit **olamaz**: $c_0$ nasıl yerelse, ortamın deplasman tepkisi de yereldir. Evrensel bir eşleşme aramak postülatla çelişir. Boyut analizi doğru adı zaten söyler — $[C]=(\text{yoğunluk})(\text{hız})/(\text{uzunluk})$:

$$C=\frac{\rho_0\,c_0}{L_\ast}\qquad\Longrightarrow\qquad
\boxed{\;\mathcal{G}=\underbrace{\frac{\sqrt2\,r_n^{2}\sqrt{m_p/m_e}}{4m_n}}_{\text{nükleon yapısı}}\times\frac{c_0}{L_\ast}\;}$$

$c_0=\sqrt{P_0/\rho_0}$ zaten ortamın durumundan çıkıyordu; ama $(P_0,\rho_0)$ ikilisi bir **hız** verir, **uzunluk** vermez. Eksik olan tek şey odur:

$$L_\ast=\frac{\rho_0c_0}{C}=8{,}64\times10^{24}\ \mathrm{m}$$

**Ve hiyerarşi saf bir uzunluk oranına iner.** M-46'nın empedans oranı, hiçbir katsayı taşımayan bir orandır:

$$\frac{\ell_\omega}{L_\ast}=\frac{3{,}61\times10^{-14}}{8{,}64\times10^{24}}=4{,}17\times10^{-39}$$

> **Kütle-itim zayıftır çünkü nükleonun ölçeği, ortamın ölçeğine göre $10^{-39}$ mertebesindedir.** Soyut bir *"neden zayıf"* sorusu değil, iki fiziksel uzunluğun karşılaştırması.

Aynı oran, nükleonun kendi ritmine göre normalize edildiğinde kuplajın **boyutsuz şiddetini** verir:

$$\varepsilon\equiv\frac{C/\rho_0}{\omega_n}=6{,}88\times10^{-41},\qquad
\varepsilon=\frac{\ell_\omega}{L_\ast}\cdot\frac{c_0}{u_r},\qquad\frac{u_r}{c_0}=\sqrt2\sqrt{m_p/m_e}=60{,}60$$

İki yazım tek kalemdir ($4{,}17\times10^{-39}/60{,}60=6{,}88\times10^{-41}$); Ek C'de sayı değişmez.

**Postülat 4 ile uyum bir kabul değil, zincirin sonucudur.** $c_0$ ortamın durumundan geliyor, kuplaj ise **ortama** kuruluyor; ikisi de yerel olduğuna göre $\mathcal{G}=[\text{nükleon}]\times c_0/L_\ast$ **zorunlu olarak yereldir.** Yerellik dayatılmıyor, üretiliyor — ve fark burada keskindir: Newton $G$'yi evrensel bir sabit olarak postülatlar ve yerelliği öngöremez; burada yerellik kuplajın doğasından çıkar.

> [!WARNING]
> **Bu bir değişken değiştirmedir, yeni bir iddia değil — ve M-35'e faturası sıfırdır.** $[C]=(\text{yoğunluk})(\text{hız})/(\text{uzunluk})$ olduğu için *her* $C$ bu biçimde yazılabilir. M-35'in hiçbir denklemi değişmez: $\Phi_q$, $dP/dr=C\Phi_q$, $P(r)=P_0-CNq_n/4\pi r$, $1/r^2$ yasası, Gauss akısı, iz sıfırlığı, gelgit tensörü — hepsi aynen durur, ve iki yazım aynı $\mathcal{G}$'yi altı hane verir. Ek C'de kalem sayısı da aynı kalır: **bir tane.** Değişen yalnız o kalemin adı ve yorumudur — soyut bir kuplaj katsayısı yerine **Evrenakı'nın kendi yapısal uzunluğu.**
>
> Dolayısıyla bu bölüm $\mathcal{G}$'nin değerini **öngörmez**; kütle-itimin mekanizmasını kurar ve kaynak yanını parametresiz kapatır. Kalan tek bilinmeyenin kimliği ise M-46'da kesinleşmiştir: aranan şey ortamın bir **uzunluğu** değil, madde ile ortam arasındaki **kuplajın şiddetidir** — $L_\ast$ onun uzunluk kılığıdır. Gerekçesi ve dokuz elemenin dökümü M-46'nın Açık Uçlar kutusundadır.
>
> İkinci kayıt: kaynak şiddetinin $\omega_2$ ve deplasman hacminden *ayrıca* hesabı (M-35'in ilk niyeti, $q_n\sim f\cdot\Delta V$) yapılmamıştır; M-45 onun yerine kararlı $u_r$ ile kapatmıştır. İki yolun aynı sayıyı vermesi gösterilirse zincir bir kez daha kapanır.
