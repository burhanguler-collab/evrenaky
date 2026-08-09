# 9.5 Casimir Etkisi ve Vakum Basıncı

Havasız ortamda, mutlak sıfıra yakın sıcaklıkta, yüksüz iki iletken plaka mikron-altı mesafeye yaklaştırıldığında birbirini **iter gibi değil, çeker gibi** davranır: dışarıdan içeriye doğru net bir basınç ölçülür. Standart fizik bunu "vakum enerjisi" ve "sanal parçacıklarla" açıklar; Evrenakı Teorisi'nde ise olay, dolu bir okyanusun içinde duran iki levhanın hidrodinamiğidir: plakalar arasındaki dar bölgeye ortamın **dalgalanmaları** tam kapasite sığamaz, dışarıdaki dalgalanma basıncı içeridekinden büyük kalır ve plakalar birbirine bastırılır. Bu bölümün görevi bu resmi sayıya bağlamak ve ölçüm literatürüyle yüzleştirmektir.

> **Kapsam ve tamamlanma notu:** Bu bölüm sınırlı kapsamla yazılmıştır: mekanizmanın ölçek sınaması, mod-dışlama türetiminin yapısı ve sayısal karşılaştırma. Derin katman — dalgalanma spektrumunun pencere mekaniğinden türetimi, mod-serbestlik sayımı ve malzeme/sıcaklık düzeltmeleri — 9.5.6'nın açık kalemleri olarak 7.4 envanterine bağlıdır; kalemler kapandığında bölüm genişletilerek **tamamlanacaktır.**

## 9.5.1 Doğrulanacak Gözlem Envanteri

| # | Gözlem | Ölçülen değer / davranış | Kaynak |
|---|---|---|---|
| G-1 | Kuvvet yasası | $F/A = \dfrac{\pi^2\hbar c}{240\,a^4}$; $a=1$ µm'de $\approx1{,}3$ mPa, $a^{-4}$ ile büyür | Casimir, 1948 (öngörü) |
| G-2 | Hassas doğrulama | torsiyon sarkacı (~%5); AFM küre-plaka (~%1) | Lamoreaux, 1997; Mohideen & Roy, 1998 |
| G-3 | Malzeme bağımlılığı | sonlu iletkenlik ve pürüz kuvveti öngörülebilir biçimde düşürür | Mohideen & Roy, 1998 |
| G-4 | İşaret çevrimi | uygun sıvıyla ayrılmış asimetrik malzeme çiftinde kuvvet **itici** olabilir | Munday ve ark., 2009 |
| G-5 | Sıcaklık düzeltmeleri | büyük aralıkta termal katkı | Sushkov ve ark., 2011 |

G-4 özellikle kaydedilmelidir: "dış basınç plakaları iter" biçimindeki en yalın okuma her zaman çekim öngörür; işaretin malzeme dizilimiyle çevrilebilmesi, mekanizmanın **mod muhasebesi** düzeyinde kurulmasını zorunlu kılar.

## 9.5.2 Ölçek Sınaması: Statik Basınç Değil, Dalgalanma Payı

Teorinin arka plan basıncı devasadır: $P_0=\frac{1-k}{4}\rho_nc^2\sim10^{33}$ Pa (M-8). Eğer plakalar statik $P_0$'ın kendisini kısmen perdeliyor olsaydı, kuvvet bu ölçekte olurdu — ölçülenin **~36 mertebe** üstü. Demek ki plakaların perdeleyebildiği şey statik zemin değil, onun üzerindeki küçücük **dalgalanma payıdır**: ortam, M-9'un kararlılık teoreminin izin verdiği sınırlar içinde (kavitasyon eşiğinin çok altında) sürekli dalgalanır; bu dalgalanmaların taşıdığı basınç payı, statik zeminin yanında ihmal edilebilir ama **iki plaka arasında seçici olarak eksiltilebilir** olan tek kalemdir. Güdük sezgi ("araya tam kapasite dalgalanamaz") burada nicelleşir: Casimir kuvveti, Evrenakı'nın statik ağırlığı değil, **sesinin gölgesidir.**

## 9.5.3 Mod-Dışlama Türetiminin Yapısı

Türetim üç yapı taşından kurulur; ikisi teoride hazırdır, biri ithal edilir ve açıkça işaretlenir:

1. **Plakalar ayna gibidir (teoriden):** metalik fazda delokalize elektron gazı ara hacmi doldurur ($\phi\to1$; 11.4.1) — iletken plaka, Evrenakı dalgalanmalarına karşı hemen hemen tam yansıtıcı bir rampadır (2.6'nın rampa mekaniğinin sürekli-yüzey hâli). Sonlu iletkenlikte yansıtıcılık kısmidir → G-3'ün malzeme bağımlılığının nitel adresi.
2. **Aradaki bölgede mod dışlanır (geometri):** iki ayna arasında yalnız $a$'ya sığan duran-dalga modları yaşayabilir; uzun dalgalı dalgalanmalar dışlanır. Dışarıda tam spektrum, içeride budanmış spektrum → net içe basınç. Boyut analizi tek başına $a^{-4}$'ü verir: [enerji/hacim] ölçeğini kuran iki büyüklük mod enerjisi ($\hbar\times$frekans) ile hız $c$ ise, $F/A\propto\hbar c/a^4$ zorunludur.
3. **Mod başına enerji (ithal — açıkça):** dalgalanma modu başına $\tfrac12\hbar\omega$ payı, standart fizikten **denetlenecek teorem** olarak alınır (KARNE yöntem kaydı); teorideki karşılığı $\hbar=\delta\tau/2\pi$'dir (M-11) ve bu payın pencere mekaniğinden türetimi açık kalemdir (9.5.6/i).

Bu üç taşla standart mod toplamı (Casimir, 1948) aynen yürür ve kapalı form geri gelir:

$$\boxed{\frac{F}{A} = \frac{\pi^2}{240}\,\frac{\hbar c}{a^4} = \frac{\pi^2}{240}\,\frac{(\delta\tau/2\pi)\,c}{a^4}}$$

Teorinin okuma farkı katsayılarda değil kimliklerdedir: $\hbar$, fotoelektrik eğimden sabitlenen $\delta\tau$ çarpımıdır; $c$, ortamın Kavrama Yasası hızıdır ($\sqrt{P_0/\rho_0}$, M-1); ve "vakum", boşluk değil, dalgalanan dolu bir okyanustur.

**Katsayı dürüstlüğü:** $240$ paydası, ışık hızıyla yayılan **iki** kutuplanma serbestliğinin sayımına denk düşer; tek skaler (boyuna basınç) serbestlik $480$ verirdi. Teorideki doğal aday, dalgalanmaların Zerre-diski kutuplanma serbestliğidir (2.4.3, 2.9 — iki enine yönelim); bu sayımın türetimi açık kalemdir (9.5.6/ii).

## 9.5.4 Sayısal Karşılaştırma

$a=1$ µm için $F/A = \pi^2\hbar c/(240\,a^4) \approx 1{,}3\times10^{-3}$ Pa; $a=100$ nm'de $\approx13$ Pa. Mohideen & Roy'un AFM ölçümleri (0,1–0,9 µm aralığı) bu eğriyi ~%1 hassasiyetle izler (iletkenlik/pürüz düzeltmeleriyle); Lamoreaux'nun torsiyon ölçümü büyük aralıkta ~%5 ile aynı yasayı verir. $a^{-4}$ taraması, mod-dışlama geometrisinin parmak izidir ve bütün ölçüm ailesince doğrulanır (G-1, G-2 ✅).

**G-4'ün okunuşu:** iki plaka arasına üçüncü bir ortam (sıvı) girdiğinde muhasebe üç bileşenli olur — dalgalanma basıncı artık "içerisi boş / dışarısı dolu" değil, üç ortamın yansıtıcılık sıralamasına bağlıdır; uygun sıralamada içerideki pay dışarıyı aşar ve kuvvet itici olur. Bu, mod-muhasebesi okumasının nitel zaferidir: en yalın statik-basınç resmi bu işareti asla üretemez (nicel model açık kalemdir, 9.5.6/iii).

## 9.5.5 Standart Fizikle Yüzleşme: "Vakum Enerjisi"nin Adresi

Standart çatıda Casimir kuvveti, "boş uzayın sıfır-nokta enerjisinin" kanıtı sayılır — ve aynı çatı bunun bedelini kozmolojide öder: sıfır-nokta enerjisinin beklenen yoğunluğu, gözlenen kozmolojik yoğunluktan ~$10^{120}$ kat büyüktür ("vakum felaketi"; 1.2'nin kriz envanteri). Teoride bu felaket **hiç doğmaz**, çünkü iki ayrı soru karışmaz: **(a)** dalgalanmaların *fark* basıncı ölçülebilir ve küçüktür — Casimir bunu ölçer; **(b)** ortamın *mutlak* enerji içeriği devasadır ($P_0\sim10^{33}$ Pa) ama kuvvet üretmez, çünkü teoride kuvvetin tek kaynağı **basınç gradyanıdır** ($\nabla P_0=0$ → ortam ağırlıksızdır; M-9 teoremi). Standart fizik mutlak içeriği "yerçekimsel" kaynak sayarak felakete düşer; teoride mutlak zemin, tanımı gereği kuvvetsizdir. Casimir böylece teoride bir tuhaflık değil, arka planın **varlığının ve dalgalandığının** laboratuvar-ölçekli doğrudan tanığıdır — Kısım 5'in gradyan deneyleriyle aynı ailenin en küçük ölçekli üyesi.

## 9.5.6 Açık Kalemler

Tümü 7.4 envanterine bağlanır; bölüm bu kalemler kapandığında genişletilecektir:

i. **Mod enerjisinin teori-içi türetimi:** $\tfrac12\hbar\omega$ payının pencere mekaniğinden ($\delta$, $\tau$) çıkarılması — karacisim kalemiyle (9.2.7/iii) aynı cephe: ikisi de ortam dalgalanma istatistiğinin yerlileştirilmesidir.
ii. **Serbestlik sayımı:** katsayı 240'ı kuran iki kutuplanma serbestliğinin Zerre-diski yönelim mekaniğinden (2.4.3) türetimi.
iii. **Üç-ortam muhasebesi:** itici Casimir'in (G-4) nicel modeli; yansıtıcılık sıralaması → işaret kuralı.
iv. **Malzeme ve sıcaklık düzeltmeleri:** kısmi yansıtıcılığın (sonlu iletkenlik, $\phi<1$) ve termal katkının (G-5) rampa mekaniğinden hesabı.
v. **Dalgalanma spektrumunun kaynağı:** ortam dalgalanmalarını besleyen mekanizmanın (Zerre trafiği, kohezyon salınımları — M-4/M-5 kanallarıyla ilişkisi) tanımlanması ve M-9 kararlılık sınırıyla tek çerçevede gösterimi.

---

**Bölüm özeti:** Casimir kuvveti teoride "boşluğun enerjisi" değil, dolu okyanusun **dalgalanma gölgesidir**: iletken plakalar ($\phi\to1$ rampaları) aralarındaki dar bölgeden uzun-dalga dalgalanmalarını dışlar, dışarıdaki dalgalanma basıncı net içe itki bırakır. Ölçek sınaması mekanizmayı tek başına seçer — statik $P_0$ okuması 36 mertebe ıskalarken, mod-dışlama hem $a^{-4}$ yasasını hem 1,3 mPa genliğini verir. Formüldeki $\hbar$, fotoelektrikten sabitlenen $\delta\tau/2\pi$'dir: fotoelektrik, Compton ve karacisimden sonra Casimir, aynı çarpımı okuyan **dördüncü bağımsız olgu ailesidir.** Ve standart fiziğin $10^{120}$'lik vakum felaketi teoride doğmaz: mutlak zemin kuvvetsizdir ($\nabla P_0=0$), ölçülebilir olan yalnız farktır. Derin katman (mod enerjisi, serbestlik sayımı, üç-ortam ve termal muhasebe) 7.4'e bağlı açık kalemlerdir; **bölüm o kalemler kapandığında tamamlanacaktır.**
