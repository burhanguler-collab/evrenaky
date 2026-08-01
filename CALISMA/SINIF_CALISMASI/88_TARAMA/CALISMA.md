# 88_TARAMA — Galaksi başına açığı ne öngörüyor? · **NULL SONUÇ**

**14 değişken tarandı · başka-yere-bakma düzeltmesi yapıldı · hiçbiri eşiği aşmadı**

Hesap: `../../galaksi_acik_taramasi.py` · Çıktılar: [`SONUC.csv`](SONUC.csv) ·
[`tarama.png`](tarama.png)
Ön adım: [89_KAFES/GOZLEMSEL.md](../89_KAFES/GOZLEMSEL.md) md. 7 madde 1

---

## 0. Aranan şey

Açık $D=V_{bar}^2+v_{F4}-v_{gözl}^2$ varyansının **%68'i galaksiler arası**
([GOZLEMSEL.md](../89_KAFES/GOZLEMSEL.md) md. 4). Ve galaksi başına değişen bütün **bilinen**
adaylar elendi:

| Aday | Nerede elendi |
|---|---|
| $\Upsilon_*$ | [AYIRMA.md](../89_KAFES/AYIRMA.md) md. 3 |
| mesafe | [GOZLEMSEL.md](../89_KAFES/GOZLEMSEL.md) md. 3 |
| eğiklik | GOZLEMSEL.md md. 2 |
| basınç desteği · KAFES | GOZLEMSEL.md md. 1 · AYIRMA.md md. 2 |

Geriye adı olmayan bir %68 kaldı. Bu dosya onu **öngören** değişkeni arıyor.

## 1. Yöntem ve tuzağı

Hedef: galaksi başına $x=\text{medyan}(D/v_{öng}^2)$. 14 aday değişken.

**Bu bir taramadır** ve ham $p$ değeri yanıltıcıdır: 14 değişken denenince en iyisi
tesadüfen anlamlı görünür. Bu yüzden **başka-yere-bakma düzeltmesi** yapıldı — hedef
4000 kez karıştırılıp *tesadüfi en iyi* $\lvert\rho\rvert$'nun boş dağılımı kuruldu ve eşik
onun %95 diliminden alındı.

İki örneklem: **YOĞUN** (yalnız $\log g_{bar}\geq-10$, açığın olduğu rejim) ve **BÜTÜN EĞRİ**
(daha güçlü ama açık seyreltilmiş).

---

## 2. Sonuç — **hiçbir değişken eşiği aşmıyor**

### YOĞUN REJİM · n = 38 galaksi · eşik $\lvert\rho\rvert>0{,}455$

| Değişken | Spearman | |
|---|---|---|
| **log $V_{flat}$** | $\mathbf{-0{,}425}$ | eşiğin altında |
| log kovan kesri | $+0{,}244$ | |
| SPARC $Q$ | $+0{,}192$ | |
| log $R_{eff}$ | $-0{,}183$ | |
| log $SB_{disk}$ | $-0{,}169$ | |
| log $R_{HI}/R_{disk}$ | $-0{,}133$ | |
| log $M_{bar}$ | $-0{,}117$ | |
| log $L_{[3,6]}$ | $-0{,}111$ | |
| log $SB_{eff}$ | $+0{,}100$ | |
| log $R_{disk}$ | $-0{,}094$ | |
| log mesafe | $-0{,}071$ | |
| gaz kesri | $+0{,}068$ | |
| morfoloji $T$ | $-0{,}052$ | |
| eğiklik | $-0{,}029$ | |

### BÜTÜN EĞRİ · n = 141 galaksi · eşik $\lvert\rho\rvert>0{,}231$

| Değişken | Spearman |
|---|---|
| **SPARC $Q$** | $\mathbf{+0{,}185}$ |
| log $R_{HI}/R_{disk}$ | $-0{,}160$ |
| log $SB_{disk}$ | $-0{,}123$ |
| log $V_{flat}$ | $-0{,}121$ |
| log kovan kesri | $+0{,}104$ |
| *(kalan dokuzu $<0{,}09$)* | |

> ### İki örneklemde de: **hiçbiri eşiği aşmıyor**
>
> Kütle, ışıma, yüzey parlaklığı, disk ölçeği, etkin yarıçap, düz hız, gaz kesri,
> morfoloji, eğiklik, kalite bayrağı, mesafe, HI genişliği, kovan kesri —
> **on dördünün hiçbiri** galaksi başına açığı öngörmüyor.

---

## 3. İki yakın kaçış — ve ne söylüyorlar

**log $V_{flat}$: $-0{,}425$ (eşik 0,455).** Yoğun rejimde en güçlü, ama eşiği geçmiyor.
Yön: hızlı/kütleli galakside açık **küçük.** Bu, 97_BTFR md. 2'nin sınıf bandıyla kısmen
uyumludur ama tek başına iddia edilemez — ve bütün eğri örnekleminde $-0{,}121$'e düşüyor,
yani **kararlı değil.**

**SPARC $Q$: $+0{,}185$/$+0{,}192$** — iki örneklemde de aynı işaret ve mertebe. Yön: kalitesi
kötü veride açık **büyük.** Eşiği aşmıyor ama **kararlı olan tek değişken** bu. Gözlemsel bir
bileşenin varlığına işaret ediyor; ama $Q$ kaba bir bayraktır (1/2/3) ve tek başına %68'i
taşımaz.

---

## 4. Bunun anlamı

**Açığın üçte ikisi hâlâ adsız — ve artık bu bir eksiklik değil, bir bulgu.**

Elenenlerin listesi kapsayıcı: teorinin iki terimi ($F1$ ve $F4$), üç gözlemsel sistematik
(mesafe, eğiklik, basınç), bir girdi parametresi ($\Upsilon_*$), ve on dört galaktik değişken.
Geriye üç olasılık kalıyor:

| # | Olasılık | Durum |
|---|---|---|
| 1 | **Daireden sapan hareketler** (bar, warp, spiral kol) | **sınanmadı** — SPARC'ta ölçülü değil, dış veri gerek |
| 2 | Taranan 14 değişkenin **hiçbirine indirgenmeyen** bir galaksi özelliği (çevre, birleşme geçmişi, yaş) | katalogda yok |
| 3 | Açığın kendisi **tek bir sayı değil** — birkaç küçük etkinin toplamı, hiçbiri baskın değil | tarama bunu ayırt edemez |

**3. olasılık en olası ve en can sıkıcı olanıdır:** eğer açık dört beş bağımsız etkinin
her biri %10–20'lik toplamıysa, hiçbir tek değişken onu öngörmez ve hiçbir tek mekanizma
onu açıklamaz. Tarama tam olarak bu deseni verir.

---

## 5. Dürüstlük kayıtları

1. **Bu bir null sonuç ve öyle raporlanıyor.** En iyi değişkeni "aday" ilan edip
   $\lvert\rho\rvert=0{,}425$'i sunmak yanıltıcı olurdu; başka-yere-bakma eşiği 0,455 ve
   **altında kaldı.**
2. **Yoğun örneklem n=38.** GOZLEMSEL.md 52 galaksi diyordu; burada galaksi başına en az 3
   yoğun nokta koşulu 38'e indirdi. Bu, çözünürlüğü ciddi biçimde düşürüyor —
   $\lvert\rho\rvert<0{,}45$ olan gerçek bir ilişki **görünmez.**
3. **14 değişken kataloğun verdikleriyle sınırlı.** Çevre yoğunluğu, birleşme geçmişi, yıldız
   nüfusu yaşı, bar varlığı, warp genliği — hiçbiri SPARC'ta yok ve **taranmadı.**
4. **Doğrusal olmayan ve çok değişkenli ilişkiler taranmadı.** Spearman tek değişkenli ve
   monotondur. İki değişkenin birleşimi (örneğin $\Sigma$ **ve** $V_{flat}$) açığı öngörüyor
   olabilir; bu **denenmedi.**
5. **Hedef değişkenin kendisi gürültülü.** Galaksi başına medyan, 3–20 noktadan geliyor;
   ölçüm hatası hedefe girer ve bütün korelasyonları **aşağı** çeker. Yani null sonuç kısmen
   gürültüden olabilir — ama o zaman da "%68 galaksiler arası" ifadesinin bir kısmı gürültüdür,
   ki bu da ayrıca sınanmalı.
6. **Permütasyon eşiği tek bir hedefe göre kuruldu**, iki örneklem için ayrı ayrı. Aynı
   veriye iki kez bakılması ayrıca bir başka-yere-bakma katmanıdır ve düzeltilmedi.

---

## 6. Ne çıktı — üç cümle

1. **On dört değişkenin hiçbiri galaksi başına açığı öngörmüyor** — başka-yere-bakma
   düzeltmesinden sonra iki örneklemde de eşiğin altında.
2. **Kararlı olan tek işaret SPARC kalite bayrağı** ($+0{,}19$ her iki örneklemde) — gözlemsel
   bir bileşen var ama küçük.
3. **En olası okuma: açık tek bir sebepten değil, birkaç küçük etkinin toplamından geliyor.**
   Tarama tam olarak bu deseni verir ve bu, tek bir mekanizma aramanın **yanlış strateji**
   olabileceği anlamına gelir.

## 7. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **Hedefin gürültü payını ölç** — galaksi başına medyanın hata çubuğunu hesapla, "%68 galaksiler arası" oranını gürültüden arındır | md. 5.5 — null sonucun ne kadarı gürültü, bilinmiyor |
| 2 | Çok değişkenli tarama (iki ve üç değişkenli birleşimler, ağaç tabanlı) | md. 5.4 |
| 3 | Daireden sapan hareket verisi olan alt küme bul (bar/warp katalogları) | md. 4 olasılık 1 |
| 4 | "Birkaç küçük etki" hipotezini nicelle: her elenen adayın **kısmi** katkısını birlikte fitle | md. 4 olasılık 3 |

> ### Madde 1 yapildi -> [`GURULTU.md`](GURULTU.md)
>
> «%68 galaksiler arasi»nin **%78'i hata butcesi** (mesafe %59). Gercek pay ~%15.
> Ve seyreltme duzeltmesi log V_flat'i -0,92 gibi gosteriyor ama **tuzak:**
> az-gurultulu yarida -0,209'a duser, yani korelasyon gurultunun kendisinden.
> **Bu null sonuc ayakta ve guclendi.** Buna karsilik SINIF BANDI gercek —
> mesafe hatasi onun yalniz %26'sini acikliyor, 97_BTFR md.2 acik kaliyor.
