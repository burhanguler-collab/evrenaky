# Yarı-Küre Diferansiyel Analizi: Gelgit Kuvvetlerinde İşaret ve Çerçeve

Bu analiz, Dünya ve Ay'ı geometrik kütle merkezlerinden geçen bir düzlemle "Ön Yarı" ve "Arka Yarı" olarak ikişer hacimsel parçaya bölerek, **klasik diferansiyel (gelgit) kuvvetlerinin** bu yarı-küreler üzerinde nasıl davrandığını incelemektedir. Amaç, klasik hesapta hangi niceliğin gerçek kuvvet, hangisinin çıkarma sonrası kalan artık olduğunu sayısal olarak ayırmaktır. Hesaplamalarda her bir yarı-kürenin kütle merkezi ($d = \frac{3}{8}R$) kullanılmıştır.

## Parametreler ve Temel Veriler

**Girdiler**

| Büyüklük | Sembol | Değer |
|---|---|---|
| Kütleçekim sabiti | $G$ | $6.67430 \times 10^{-11}$ m³ kg⁻¹ s⁻² |
| Dünya kütlesi | $M_D$ | $5.9722 \times 10^{24}$ kg |
| Ay kütlesi | $M_A$ | $7.342 \times 10^{22}$ kg |
| Dünya yarıçapı | $R_D$ | $6.371 \times 10^{6}$ m |
| Ay yarıçapı | $R_A$ | $1.737 \times 10^{6}$ m |
| Dünya–Ay merkez mesafesi | $r$ | $3.844 \times 10^{8}$ m |

**Türetilen büyüklükler**

- Yarı-küre kütle merkezi uzaklığı: $d = \tfrac{3}{8} R$ → Dünya için $d_D = 2.389 \times 10^{6}$ m, Ay için $d_A = 6.514 \times 10^{5}$ m
- Klasik toplam çekim: $F_{klasik} = \dfrac{G M_D M_A}{r^2} = 1.98056 \times 10^{20}$ N
- Her yarı-kürenin merkezinde hissetmesi beklenen referans kuvvet: $F_{merkez} = F_{klasik}/2 = 0.99027 \times 10^{20}$ N
- Bir yarı-küreye etkiyen gerçek kuvvet: $F = \dfrac{G M_{karşı} \, (M/2)}{(r \mp d)^2}$ — ön yarı için $r-d$, arka yarı için $r+d$
- Diferansiyel (gelgit) kuvvet: $F_{dif} = F_{gerçek} - F_{merkez}$

Tüm sayısal değerler [`yari_kure_hesap.py`](yari_kure_hesap.py) betiğiyle üretilmiştir.

---

## 1. Dünya'nın Ay Tarafından Çekilmesi (Diferansiyel Analiz)
Klasik gelgit hesabında, gerçek (mutlak) kuvvetten, gezegenin merkez ivmesi (merkezcil kuvvet) **çıkarılarak** bağıl/diferansiyel kuvvet bulunur. Dünya'nın iki yarısı için bu işlemi yaptığımızda:

*   **Ön Yarıya Etkiyen Diferansiyel Kuvvet:** $+1.24253 \times 10^{18}$ N
    *(Kuvvet pozitiftir; Dünya'nın ön yarısı Ay'a doğru çekilir.)*
*   **Arka Yarıya Etkiyen Diferansiyel Kuvvet:** $-1.21958 \times 10^{18}$ N
    *(Değer negatiftir; klasik anlatının "su uzaya doğru kabarıyor" derken dayandığı nicelik budur. İşaretinin nereden geldiği §3'te ayrıştırılmaktadır.)*

### Kritik Sonuç: Diferansiyel Alan Bir Artıktır, Çekimin Kendisi Değildir
İki yarı-küreye etkiyen diferansiyel kuvvetleri toplayalım:

$$ F_{Net} = (+1.242 \times 10^{18}) + (-1.219 \times 10^{18}) = +2.295 \times 10^{16} \text{ N} $$

Bu değer, klasik noktasal çekim kuvvetinin ($1.98 \times 10^{20}$ N) yalnızca **%0.01'idir**; toplam pratikte sıfırlanmaktadır.

Bu sıfırlanma klasik matematiğin bir hatası değildir — **tanımın kendisidir.** Diferansiyel alan, kütle merkezinin ivmesi kasten çıkarıldıktan sonra geriye kalan artıktır; artığın cisim üzerindeki toplamının sıfıra yakın çıkması zorunludur. Ay'ın Dünya'ya uyguladığı gerçek çekim kaybolmuş değildir, çıkarılan terimin içindedir (bkz. §3.2, gerçek kuvvetlerin toplamı tam çekimi verir).

Ancak tam da bu nedenle şu yorum kapanır: arka yarı-küredeki eksi değer, **bağımsız bir fiziksel kuvvet olarak okunamaz.** Onu "suyu uzaya iten gerçek bir kuvvet" saymak, aynı toplamın Ay'ın net çekimini de silmesini kabul etmeyi gerektirir. Eksi değer, ancak ait olduğu artık alanın bir bileşeni olarak — yani çıkarılan merkez ivmesiyle birlikte — anlamlıdır. Bu bir çürütme değil, yorum üzerindeki bir kısıttır: klasik matematik tutarlıdır, klasik **anlatı** ("Ay arka yüzdeki suyu uzaya doğru itiyor") değildir.

---

## 2. Ay'ın Dünya Tarafından Çekilmesi
Aynı işlemi Dünya'nın Ay kütlesi üzerindeki gelgit gerilimi için yaparsak (Ay'ı ön ve arka olarak ikiye bölerek):

*   **Ay'ın Ön Yarısına Etkiyen Diferansiyel Kuvvet:** $+3.36465 \times 10^{17}$ N (Dünya'ya doğru)
*   **Ay'ın Arka Yarısına Etkiyen Diferansiyel Kuvvet:** $-3.34759 \times 10^{17}$ N (Dünya'dan uzağa, negatif)

### Toplam Net Kuvvet
$$ F_{Net} = (+3.36 \times 10^{17}) + (-3.34 \times 10^{17}) = +1.706 \times 10^{15} \text{ N} $$
Bu değer, toplam çekim kuvvetinin sadece **%0.0008'idir.** Ay için de diferansiyel toplam pratikte sıfırlanmaktadır — §1'de olduğu gibi bu, tanımın doğal sonucudur: kütle merkezi ivmesi çıkarıldığı için geriye kalan artık alanın cisim üzerindeki toplamı sıfıra yakın olmak zorundadır. Dünya'nın Ay'a uyguladığı gerçek çekim kaybolmuş değildir; çıkarılan referans terimin içindedir.

Oran farkına dikkat: Ay'da sıfırlanma Dünya'dakinden bir mertebe daha eksiksizdir (%0.0008'e karşı %0.01). Bunun nedeni Ay'ın yarıçapının Dünya–Ay mesafesine oranının daha küçük olması, yani $d_A/r$ oranının küçüklüğüdür; diferansiyel alan bu orana bağlı olarak zayıflar.

---

## 3. Eksi İşaret Nereden Doğuyor? — Çerçeve Testi

### 3.1 Kullanmadığımız itiraz: "çıkarma sırası keyfîdir"
Sık dile getirilen bir itiraz vardır: *"Arka yüzde küçük kuvvetten büyük kuvvet çıkarılıyor; aynı sırayı ön yüze uygularsanız ön yüz de eksi çıkar, demek ki işaret keyfîdir."*

Bu itiraz geçerli değildir ve bu çalışmada kullanılmamaktadır. Klasik formülasyonda çıkarma sırası sabittir ve daima aynıdır: **(gözlenen nokta) − (referans nokta)**. İşareti belirleyen, hangi sayının önce yazıldığı değil, gözlenen noktadaki kuvvetin referanstakinden büyük mü küçük mü olduğudur:

| Nokta | Gerçek kuvvet (eylemsiz çerçeve) | Referans (merkez) | Fark = gözlenen − referans |
|---|---|---|---|
| Ön yarı | $+1.00270 \times 10^{20}$ N | $+0.99027 \times 10^{20}$ N | $+1.24253 \times 10^{18}$ N |
| Merkez | $+0.99027 \times 10^{20}$ N | — | $0$ |
| Arka yarı | $+0.97807 \times 10^{20}$ N | $+0.99027 \times 10^{20}$ N | $-1.21958 \times 10^{18}$ N |

Kural tektir ve tutarlı uygulanmıştır; işaret farkı büyüklük karşılaştırmasından doğar. Bu nedenle eksi işaretini "hangi sayıyı hangisinden çıkardığınıza bağlı" diye eleştirmek klasik modeli yıkmaz. Asıl soru daha derindedir: **bu eksi işaret hangi çerçevede doğuyor ve neyi temsil ediyor?**

### 3.2 Asıl bulgu: işaret, kuvvetle değil çerçeveyle birlikte doğuyor
Tablonun ikinci sütununa dikkat edin. Eylemsiz (mutlak) çerçevede üç değer de **pozitiftir**; mesafeyle birlikte tekdüze azalır, ancak hiçbiri sıfırı geçip yön değiştirmez. Ay'a doğru bakan bir kuvvetler dizisi vardır, uzaya doğru bakan tek bir vektör yoktur.

Doğrulama: iki yarı-kürenin gerçek kuvvetleri toplandığında
$$1.00270 \times 10^{20} + 0.97807 \times 10^{20} = 1.98077 \times 10^{20}\ \text{N}$$
bulunur; bu, klasik toplam çekim değeri olan $1.98056 \times 10^{20}$ N ile **on binde bir** (%0.01) mertebesinde uyuşur. Kalan bu küçük fark, tesadüf değildir: §1'de bulunan diferansiyel toplamın ($+2.295 \times 10^{16}$ N) ta kendisidir — çünkü tanım gereği (gerçek kuvvetlerin toplamı) = (çekim) + (farkların toplamı). Yani gerçek kuvvetler **tam çekimi** verir; diferansiyel alan yalnızca üzerine binen artıktır.

Eksi işaret, ancak üçüncü sütuna geçildiğinde — merkezin ivmesi çıkarıldığında — ortaya çıkar. Çıkarılan şey, Dünya'nın kütle merkezinin Ay'a doğru serbest düşme ivmesidir. Dolayısıyla arka yüzdeki eksi vektör, suya etkiyen yeni bir kuvvetin yönü değil, **suyun altındaki zeminin ivmelenmesinin işaretidir.** Vektör dönmemiştir; ölçüm yapılan çerçeve ivmelenmektedir.

Buradan çıkan sonucun sınırını da açıkça çizmek gerekir: iki yarı-kürenin farklarının toplamının sıfıra yakın çıkması (§1) bir keşif değil, **tanımın kendisidir** — kütle merkezi ivmesi zaten kasten çıkarılmıştır, geriye kalan artık alanın toplam etkisi tanım gereği sıfıra yakındır. Bu nedenle "diferansiyel model Ay'ın net çekimini sıfırlıyor" biçimindeki bir itiraz, klasik modele karşı tek başına delil değildir.

### 3.3 Savunulabilir hat: işaret değil, nedensellik ve iş
Aradaki gerçek fark, farkın *varlığı* değildir. İki nokta arasındaki ivme farkı gerçektir ve çerçeve seçimiyle yok edilemez (genel görelilikte jeodezik sapma olarak çerçeveden bağımsız bir niceliktir). Bu çalışma da bunu inkâr etmez.

İnkâr edilen, farkın etrafına kurulan **mekanizma anlatısıdır**. Klasik anlatıda su iki adımda kaldırılır:
1. Aktif bir kaynağı olmayan bir *fark* niceliği hesaplanır (eksi vektör).
2. Okyanus bu farkı, gerçekte suyu kaldıran şeye — bir **basınç gradyanına** — çevirir.

Milyarlarca ton suyu metrelerce yükselten iş, birinci adımda değil ikinci adımda yapılır. Yani klasik model de sonuçta suyu **basınçla** kaldırmaktadır; fark niceliği yalnızca o basıncı üretmek için kullanılan ara bir defter kaydıdır ve tek başına bir enerji kaynağı değildir.

Evrenakı bu iki adımı tek adıma indirir. Yanlardan uygulanan taban sıkıştırması (Kuvvet 2) ile Ay'ın açtığı basınç gradyanı (Kuvvet 1), suyu kaldıran basıncı **doğrudan** verir; arada işaretini çerçeveden alan bir ara nicelik yoktur. Üstünlük iddiası bu nedenle "onların eksi işareti sahtedir" değil, şudur:

> Klasik model suyu iki adımda kaldırır ve ilk adımı, fiziksel karşılığı yalnızca seçilen çerçevede tanımlı olan bir farktır. Evrenakı aynı kabarmayı tek adımda, baştan basınç olarak üretir; her iki uçtaki kabarma da aynı mekanizmadan, ek varsayım olmadan çıkar.

---

## 4. Genel Çıkarım (Evrenakı Perspektifinden)
Gezegenleri iki yarı küre olarak incelemek, klasik hesabın **hangi niceliğinin gerçek kuvvet, hangisinin artık olduğunu** ayırmayı sağlar. Eylemsiz çerçevede her iki yarı-küreye etkiyen kütleçekim vektörlerinin tamamı $(+x)$ yönündedir; ikisi de kaynağa doğru çekilir ve toplamları tam çekimi verir (§3.2). Negatif (itici) bir kütleçekim vektörü hiçbir yerde ortaya çıkmaz.

Arka yarı-küredeki eksi değer, merkez ivmesi çıkarıldıktan sonra kalan artık alanın bir bileşenidir. Bu artık alan gerçektir ve ölçülebilir — inkâr edilen o değildir. İnkâr edilen, bu bileşenin **kendi başına suyu uzaya kaldıran aktif bir kuvvetmiş gibi anlatılmasıdır**; çünkü aynı toplam, tutarlı biçimde uygulandığında Ay'ın net çekimini de silmektedir (§1, §2).

Klasik modelde suyu fiilen kaldıran şey, bu farkın okyanusta dönüştüğü **basınç gradyanıdır** (§3.3). Evrenakı bu gradyanı ara bir adım olmadan, doğrudan Kuvvet 2 (taban sıkıştırma) ve Kuvvet 1 (gradyan) çiftinden üretir: her iki uçtaki kabarma, tek ve aynı hidrodinamik mekanizmadan, ek varsayım gerektirmeden çıkar.

---

## Kaynakça

1. Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica*, Kitap III.
2. Butikov, E. I. (2002). "A dynamical picture of the oceanic tides." *American Journal of Physics*, 70(9), 1001–1011.
3. Melchior, P. (1983). *The Tides of the Planet Earth*, 2. baskı. Pergamon Press.
4. Agnew, D. C. (2015). "Earth Tides." *Treatise on Geophysics*, Cilt 3, Elsevier.
5. Misner, C. W., Thorne, K. S. & Wheeler, J. A. (1973). *Gravitation.* W. H. Freeman. — Jeodezik sapma ve gelgit tensörü.
6. Williams, D. R. (2024). *Planetary Fact Sheets* (Dünya ve Ay). NASA/NSSDCA. — Kütle, yarıçap ve yörünge mesafesi değerleri.
