# 95_RAR — Radyal İvme Bağıntısı: teorinin **biçimi** sınanıyor · Çalışma dosyası

> ### ⚡ NİHAİ KURULUM (1 Ağustos 2026 · karar: [86_NIHAI](../86_NIHAI/CALISMA.md))
>
> Bu dosyanın analizi **eski (A) kurulumla** yapıldı ve tarihsel kayıt olarak duruyor.
> Nihai kurulum: yerel $\ell_\omega$ + $a_0=1{,}75\times cH_0/16{,}1$. Nihai sayılar: RAR medyan artık **−0,003 dex** (eski −0,118), biçim eğimi **+0,051** (eski +0,101). Biçim sorunu yarıya indi ama **duruyor.**


**2693 nokta · 3,9 decade · referans: Lelli, McGaugh, Schombert & Pawlowski 2016, ApJ 836, 152
— Şekil 2'nin arkasındaki veri**

Hesap: `../../rar_sinavi.py` · Çıktılar: [`SONUC.csv`](SONUC.csv) · [`YONTEM.md`](YONTEM.md) ·
[`rar.png`](rar.png)

---

## 0. Bu sınav neyi soruyor — öncekilerden farkı

97_BTFR ve 96_ETG tek bir sayı ölçüyordu: medyan sapma ve gereken $a_0$ çarpanı. Bu sınav
başka bir şey soruyor:

> **Teorinin öngördüğü BİÇİM doğru mu — yoksa yalnız ölçeği mi tutuyor?**

$g_{öng} = g_{bar}+\sqrt{g_{bar}a_0}$ formülünün **şekli sabittir.** Eğer şekil doğruysa,
$a_0$'ın yanlış kalibre olması bütün noktaları **aynı miktarda** kaydırır ama artıkta
**eğilim oluşturmaz.** Artıkta ivmeye bağlı bir yapı varsa, sorun $a_0$'da değil
**formülün kendisindedir.**

3,9 decade ve 2693 nokta bunu ayırt edecek güçtedir. 16 ETG'yle yapılamayan sınav
([96_ETG](../96_ETG/CALISMA.md) md. 6) burada yapılabilir.

**Bu sınavda ΛCDM yoktur.** `_RAR.mrt` yalnız $(g_{bar}, g_{obs})$ çiftlerini verir; galaksi
kimliği, kütle ve yarıçap yoktur, zincir kurulamaz. 97_BTFR ve 96_ETG'de kuruldu, oraya
bakılmalıdır. Buraya sahte bir karşı taraf uydurulmadı.

---

## 1. Bütün örneklem

| Kurulum | medyan dex | saçılma | gereken $a_0$ |
|---|---|---|---|
| **EVRENAKI** $g_{bar}+\sqrt{g_{bar}a_0}$ — **fit yok** | $-0{,}060$ | 0,146 | **×1,61** |
| ampirik uyum ($g_\dagger$ **fitlenmiş**) | $+0{,}002$ | 0,133 | — |

Karşılaştırma **adil değildir** ve öyle işaretlenmiştir: ampirik eğrinin bir parametresi bu
veriye fitlenmiştir, teorinin hiçbiri fitlenmemiştir. Buna rağmen saçılma farkı 0,013 dex.

---

## 2. Asıl sonuç — **tek bir $a_0$ dört decade boyunca yetmiyor**

0,25 dex'lik kuşaklarda her kuşağın istediği çarpan ayrı ayrı çözüldü:

| $\log g_{bar}$ kuşağı | n | F4 payı | artık dex | gereken $a_0$ |
|---|---|---|---|---|
| −12,00 … −11,75 | 33 | 0,84 | $-0{,}197$ | **×2,86** |
| −11,75 … −11,50 | 112 | 0,80 | $-0{,}146$ | ×2,25 |
| −11,50 … −11,25 | 288 | 0,76 | $-0{,}119$ | ×2,01 |
| −11,25 … −11,00 | 390 | 0,70 | $-0{,}113$ | ×2,01 |
| −11,00 … −10,75 | 345 | 0,64 | $-0{,}095$ | ×1,89 |
| −10,75 … −10,50 | 269 | 0,57 | $-0{,}087$ | ×1,93 |
| −10,50 … −10,25 | 287 | 0,50 | $-0{,}052$ | ×1,57 |
| −10,25 … −10,00 | 262 | 0,43 | $-0{,}018$ | ×1,21 |
| −10,00 … −9,75 | 223 | 0,36 | $-0{,}013$ | ×1,16 |
| −9,75 … −9,50 | 165 | 0,30 | $+0{,}005$ | **×0,92** |
| *−9,50 ve üstü (4 kuşak)* | *304* | *0,12–0,24* | *+0,04…+0,07* | *elendi — md. 3* |

**Çarpan tek yönlü ve düzenli biçimde kayıyor: ×2,86 → ×0,92.** Saçılma 0,142 dex.

### Ve artık ivmeyle değişiyor — **biçim sınavı kalıyor**

| | $d(\text{artık})/d(\log g_{bar})$ |
|---|---|
| **teori** (fit yok) | $\mathbf{+0{,}0836}$ dex/dex |
| ampirik uyum (bir parametresi fitli) | $-0{,}0106$ dex/dex |

Ampirik eğrinin artığı **düz**; teorininki 2,5 decade boyunca **0,21 dex sürükleniyor.**
Sorun $a_0$'ın değerinde değil, **geçiş biçiminde.**

---

## 3. Sorunun **tam teşhisi** — iki uçta iki farklı ölçek isteniyor

Sürüklenme rastgele değil. İki uca bakın:

| Rejim | Teori ne yapar | Kuşağın istediği çarpan |
|---|---|---|
| **Derin** ($g_{bar}\ll a_0$) | $g_{öng}\to\sqrt{g_{bar}a_0}$ | **×2,86** |
| **Newton** ($g_{bar}\gg a_0$) | $g_{öng}\to g_{bar}$ | **×0,92 ≈ 1** |

Ve ampirik ölçek $g_\dagger = 1{,}20\times10^{-10}$ m/s², yani $a_0$'ın **×2,84 katı.**

> ### Ölçülen ×2,86 ile beklenen ×2,84 birebir aynı sayıdır
>
> Derin limitte hem teori hem ampirik uyum $\sqrt{g_{bar}\times\text{ölçek}}$ verir; oradaki
> çarpan **doğrudan $g_\dagger/a_0$'dır** ve ölçüm bunu 0,02 hassasiyetle doğruluyor. Newton
> limitinde iki taraf da $g_{bar}$'a gider, çarpan gerekmez — ölçülen ×0,92, beklenen ×1.
>
> **Yani teorinin iki asimptotu da doğru yerde. Yanlış olan aralarındaki geçiş.**

Bu **yeni bir bulgu değil, kitabın kendi kaydının nicel karşılığıdır.**
[07_Galaktik_Yorungeler.md:1345](../../../Metin/Akademik/Kisim_6_Kanitlar/07_Galaktik_Yorungeler.md)
şunu yazıyor:

> *"Model iç ve orta bölge için küçük, asimptot için büyük $a_0$ istemektedir; bu bir biçim
> uyuşmazlığıdır ve çözülmemiştir."*

Bu sınav o cümleyi **2693 noktayla ölçtü:** iç/orta ×0,9–1,2, asimptot ×2,9.

**Bunun anlamı önemlidir: düzeltme $a_0$'ı yeniden kalibre etmek değildir.** $a_0$'ı ×1,9'a
çekmek ortayı düzeltir, iki ucu birden bozar. Gereken şey $F1$ ile $F4$'ün **toplanma
biçiminin** türetilmesidir — şu an ikisi basitçe toplanıyor ($a_{tam}=a_{F1}+a_{F4}$) ve M-37
bunu gerektiriyor mu, gerektirmiyor mu, **gösterilmemiştir.**

---

## 4. Yüksek ivme kuşakları neden elendi

Dört kuşak tabloya girmedi. Gerekçe [96_ETG](../96_ETG/CALISMA.md) md. 3'ten buraya taşınan
kuraldır:

$$\frac{\partial \log g_{öng}}{\partial \log k} = \frac{1}{2}\cdot\frac{F4}{g_{bar}+F4}$$

F4'ün payı 0,25'in altına düşünce $a_0$'ın kaldıracı kalmaz; küçük bir açığı kapatmak için
saçma bir çarpan gerekir (bu kuşaklarda ×0,10 – ×0,31 çıkıyor, biri hiç çözülmüyor).
**Eleme teorinin lehine değildir:** elenen kuşaklarda artık $+0{,}04$ ile $+0{,}07$ arası,
yani teori orada **fazla** öngörüyor ve bu, tabloda görünmese de md. 2'deki eğilime dahildir.

---

## 5. Düşük ivme asimptot eğimi — **hüküm verilemez**

Teori tam $0{,}500$ der ($g_{obs}\to\sqrt{g_{bar}a_0}$).

| Eşik | n | eğim | fark |
|---|---|---|---|
| $\log g_{bar} < -10{,}5$ | 1441 | 0,587 | $+0{,}087$ |
| $\log g_{bar} < -11{,}0$ | 827 | 0,552 | $+0{,}052$ |
| $\log g_{bar} < -11{,}5$ | 149 | 0,301 | $-0{,}199$ |

**Bu sayı eşik seçimine aşırı duyarlı (0,301–0,587) ve ikili bir hüküm taşımaz.** Üç sebep:
(a) kesilmiş örnekte doğrusal regresyon yanlıdır; (b) en düşük eşik yalnız 149 nokta bırakıyor
ve örneğin **kenarında**; (c) noktalar bağımsız değil.

Söylenebilecek olan: eğim 0,5 civarındadır ve Newton'un 1,0'inden **açıkça** uzaktır.
**"0,500 doğrulandı" DENEMEZ.** İlk yazdığımda bir eşik seçip "doğrulanıyor" demiştim; o hüküm
geri çekildi ve betiğe eşik taraması eklendi.

---

## 6. Saçılma bütçesi — "tek yasa" iddiasının gerçek payı

| | dex |
|---|---|
| gözlenen saçılma (teorinin artığı) | 0,146 |
| bildirilen ölçüm hatası (bütçe) | 0,126 |
| **iç saçılma** (kök fark) | **0,075** |
| ampirik uyumun artığı | 0,133 |

Bildirilen hatalar: $e(\log g_{obs})$ medyan 0,110 · $e(\log g_{bar})$ medyan 0,080 dex.

**Gözlenen saçılmanın %74'ü bildirilen ölçüm hatasıyla açıklanıyor.** Geriye kalan iç saçılma
0,075 dex — yani gerçek bağıntı, ham grafiğin gösterdiğinden **çok daha dardır.** Bu, "tek
yasa" iddiasının sayısal karşılığıdır ve teorinin lehinedir: fitsiz bir eğri, 2693 noktayı
0,075 dex'lik bir iç saçılmayla topluyor.

**Ama dikkat:** iç saçılma teorinin *biçim* hatasını da içerir. Md. 2'deki 0,21 dex'lik
sürüklenme çıkarılırsa gerçek iç saçılma daha da küçüktür — yani bu satır teoriyi biraz
**cezalandırıyor**, kayırmıyor.

---

## 7. Dürüstlük kayıtları

1. **Noktalar bağımsız değildir.** 2693 nokta 153 galaksiden gelir; aynı galaksinin komşu
   yarıçapları güçlü biçimde ilişkilidir. `_RAR.mrt` **galaksi kimliği içermez**, bu yüzden
   kümeleme yapılamadı. Sonuç: bütün hata çubukları ve "n" değerleri **fazla iyimserdir**;
   gerçek serbestlik derecesi 2693'ten çok daha azdır. Kuşak medyanları bundan daha az
   etkilenir ama muaf değildir.
2. **Eşik seçimi bir karardır.** F4 payı $\geq 0{,}25$ eşiği [96_ETG](../96_ETG/CALISMA.md)
   md. 3'ten alındı ve burada **değiştirilmedi**; ama seçilmiş bir sayıdır. Eşik 0,35 olsaydı
   3 kuşak daha elenir ve saçılma 0,142'den düşerdi — yani eşiği yükseltmek teorinin
   **lehinedir** ve bu yüzden yükseltilmedi.
3. **Kuşak genişliği (0,25 dex) seçilmiştir.** Denenmedi; 0,20 ya da 0,33 ile sonuç biraz
   oynar. Eğilimin kendisi (×2,86 → ×0,92) kuşaklamadan bağımsızdır, çünkü ham artık
   dağılımında da görünür (grafik, sol alt panel).
4. **Ampirik uyum karşılaştırması adaletsizdir — teorinin aleyhine.** $g_\dagger$ bu veriye
   fitlenmiştir. Buna rağmen karşılaştırma kaldırılmadı, çünkü "biçim doğru mu" sorusunun
   yanıtı **ancak** düz artıklı bir referansla verilebilir.
5. **Asimptot eğimi hükmü geri çekildi** (md. 5). İlk sürümde bir eşik seçip
   "doğrulanıyor" yazmıştım.
6. **Md. 3'teki $g_\dagger/a_0 = 2{,}84$ ile ölçülen ×2,86 örtüşmesi bir doğrulama değil,
   bir TUTARLILIK kontrolüdür.** İki büyüklük aynı verinin aynı ucundan okunur; bağımsız
   değildirler. Anlamı şudur: hesap doğru yapılmıştır, teorinin derin limiti hakkında yeni
   bir bilgi vermez.
7. **$a_0$ oynatılmadı.** Bütün sayılar kitabın kalibre değeriyle
   ($4{,}224\times10^{-11}$ m/s²) hesaplandı.

---

## 8. Ne çıktı — üç cümle

1. **Teorinin iki asimptotu da doğru yerdedir** (derin limitte ölçek $g_\dagger$, Newton
   limitinde $g_{bar}$), ama **aralarındaki geçiş biçimi yanlıştır**: gereken çarpan
   ×2,86'dan ×0,92'ye düzenli biçimde kayıyor, artık eğimi $+0{,}0836$ dex/dex.
2. **Bu, kitabın 6.5.4.5'teki kendi kaydının nicel karşılığıdır** ("biçim uyuşmazlığı") ve
   düzeltmenin $a_0$'ı yeniden kalibre etmek **olmadığını** gösteriyor.
3. **Bağıntının iç saçılması 0,075 dex'tir** — gözlenenin yalnız %26'sı. Fitsiz bir eğri
   2693 noktayı bu darlıkta topluyor.

## 9. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **$F1$ ile $F4$'ün toplanma biçimini M-37'den türet.** Şu an $a_{tam}=a_{F1}+a_{F4}$ **varsayılıyor**; gerektiği gösterilmedi | md. 3 — açığın kaynağı burası. **En kritik iş.** [94_YEREL_LOMEGA](../94_YEREL_LOMEGA/CALISMA.md) buradaki $+0{,}0836$'yı $+0{,}0791$'e indirdi ($\ell_\omega$ yerel kurulunca) — azaldı, kapanmadı |
| 2 | Sınıf çalışmasının ×1,47–3,76 saçılmasını bu eğilimle karşılaştır | md. 2'deki ×0,92–2,86 bandıyla örtüşüyor — ama **ön ölçüm zayıf çıktı** (aşağı) |
| 3 | Kuşak medyanlarını galaksi başına kümeleyerek tekrar ölç | md. 7.1 — serbestlik derecesi bilinmiyor |
| 4 | $a_0$'ı ×1,9'a çekip dönüş eğrilerinde ne bozulduğunu ölç | md. 3 iki ucun birden bozulacağını söylüyor; **ölçülmeli** |
| 5 | İç saçılmayı biçim hatasından arındırıp tekrar hesapla | md. 6 — 0,075 bir üst sınırdır |

**Madde 2 doğrudan 97_BTFR'nin en kritik açık maddesine bağlanıyor.** Orada sınıftan sınıfa
gereken çarpanın değiştiği ve *hiçbir değişkenin bunu açıklamadığı* yazılıydı (en iyi
$r=-0{,}18$). O band naif $10^{-4\Delta}$ formülüyle hesaplanmıştı; sayısal çözümle
**×1,47–3,76** oldu (`sinif_carpan_duzeltme.py`). Buradaki ivme bağımlılığı (×0,92–2,86)
aynı bandı veriyor.

> **Ön ölçüm hipotezi ZAYIF gösteriyor.** Im ile Sd neredeyse aynı ivmede
> ($\log g_{bar} = -11{,}40$ ve $-11{,}31$) ama çarpanları ×1,47 ve ×3,76 — **2,6 kat** fark.
> Üstelik Im altı sınıfın **en düşük ivmelisi** ve **en küçük çarpanlısı** — beklenenin tersi.
> Galaksi başına Spearman$[\log k, \log g_{bar}] = -0{,}21$ ($n=140$, dış nokta) /
> $-0{,}16$ (medyan): yön doğru, ama güç sınıf çalışmasının kendi en iyi değişkeniyle
> ($-0{,}18$) **aynı mertebede** — saçılmanın ~%4'ü.
>
> Okuma: ivme sınıf saçılmasının bir kısmını açıklıyor olabilir ama **mekanizması değil.**
> Tam sınav (kısmi korelasyon dahil) yapılmadı.
