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

### İmza 1 — Boyutsal salınım (pulsasyon)

Kut, $W$ boyunca gidip geldikçe kesitimizdeki **görünen yarıçapı değişir**. Büyür, küçülür, kimi zaman tamamen kaybolur. Dışarıdan bakan biri için bu, nesnenin **nefes alması** gibi görünür.

Bu imza, 12.3'te kurulan bağ mekanizmasının doğrudan kaynağıdır: pulsasyon yapan iki kavite birbirine kuvvet uygular.

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
