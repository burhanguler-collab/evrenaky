# «%68 galaksiler arası» ölçüldü — **%78'i hata bütçesi**

Hesap: `../../varyans_gurultu_sinavi.py` · Çıktılar: [`GURULTU.csv`](GURULTU.csv) ·
[`gurultu.png`](gurultu.png)
Ön adım: [`CALISMA.md`](CALISMA.md) md. 7 madde 1 · [89_KAFES/GOZLEMSEL.md](../89_KAFES/GOZLEMSEL.md) md. 4

---

## 1. Hata bütçesi

Hedef: $x=1-v_{gözl}^2/v_{öng}^2$ (galaksi başına medyan). Üç hata kaynağı, ikisi galaksi başına:

| Kaynak | Türev | Nerede |
|---|---|---|
| $v_{gözl}$ ölçüm hatası | $\partial x/\partial v_{gözl}=-2v_{gözl}/v_{öng}^2$ | nokta başına (bootstrap, 600×) |
| **MESAFE** | $M\propto D^2,\;R\propto D \Rightarrow v_{öng}^2\propto D$, yani $\partial x/\partial\ln D=(1-x)$ | **galaksi başına** |
| **EĞİKLİK** | $v_{gözl}\propto1/\sin i \Rightarrow \partial x/\partial i=2(1-x)\cot i$ | **galaksi başına** |

### Yoğun rejim ($\log g_{bar}\geq-10$, n=38)

| | varyans | pay |
|---|---|---|
| **gözlenen galaksiler arası** | 0,04636 | (saçılma 0,215) |
| $v_{gözl}$ ölçüm hatası | 0,00198 | %4 |
| **MESAFE hatası** | **0,02727** | **%59** |
| EĞİKLİK hatası | 0,00708 | %15 |
| **toplam gürültü** | **0,03632** | **%78** |
| **KALAN — gerçek** | **0,01004** | **%22** (saçılma 0,100) |

### Bütün eğri (n=141)

Aynı desen: gürültü **%79** (mesafe %46, eğiklik %31, $v_{gözl}$ %3), kalan **%21**.

---

## 2. Sonuç — «%68 adsız sistematik» anlatısı büyük ölçüde çöküyor

[GOZLEMSEL.md](../89_KAFES/GOZLEMSEL.md) md. 4 *"açığın %68'i galaksiler arası ve galaksi
başına değişen bütün bilinen adaylar elendi"* diyordu ve son üç dosya bunun üzerine kuruldu.

**Doğrusu:** o %68'in **%78'i hata bütçesidir.** Gerçek galaksiler-arası pay, toplam
varyansın $0{,}68\times0{,}22\approx$ **%15'i.**

> ### Ve ince ayrım burada
>
> Mesafe ve eğiklik, açığın **ortalamasının SEBEBİ olarak** elenmişti
> ([GOZLEMSEL.md](../89_KAFES/GOZLEMSEL.md) md. 2–3): en iyi mesafeli galakside açık en
> büyüktü, eğiklikle korelasyon yoktu.
>
> Ama **saçılmaya katkıları ayrı bir şeydir** ve o ilk kez burada hesaplandı. İkisi birlikte
> galaksiler-arası saçılmanın **%74'ünü** üretiyor. "Sebep değil" ile "saçılma kaynağı değil"
> aynı şey değil — ben bu ikisini ayırmamıştım.

**Yani gerçek bir galaksi-başına değişim VAR** (saçılma 0,100 dex yoğun rejimde) ama
öncekinin **beşte biri** kadar.

---

## 3. Seyreltme tuzağı — ve ona düşmedim

Gürültü %78 ise ölçülen korelasyonlar $\sqrt{0{,}217}=0{,}465$ çarpanıyla **seyreltilmiş**
olmalı. Düzeltilirse [88_TARAMA](CALISMA.md)'nın null sonucu tersine dönerdi:

| Değişken | ham $\lvert\rho\rvert$ | seyreltme düzeltmeli | **az-gürültülü yarı** (n=19) |
|---|---|---|---|
| log $V_{flat}$ | $-0{,}427$ | $\mathbf{-0{,}917}$ | $\mathbf{-0{,}209}$ |
| log kovan kesri | $+0{,}290$ | $+0{,}623$ | $+0{,}311$ |
| SPARC $Q$ | $+0{,}235$ | $+0{,}504$ | $+0{,}191$ |

**Düzeltme log $V_{flat}$'i $-0{,}92$ yapıyor — neredeyse kusursuz bir öngörücü.** Ama bu bir
tuzak: eğer gerçek korelasyon $-0{,}92$ olsaydı, **gürültüsü az olan galaksilerde ham
korelasyon DAHA YÜKSEK** olurdu. Ölçülen $-0{,}209$ — yani **daha düşük.**

**Sebep:** seyreltme düzeltmesi gürültünün öngörücüden bağımsız olmasını gerektirir. Kütleli
galaksiler daha uzaktır, yani $e_D/D$ ile $V_{flat}$ ilişkilidir. O yüzden görünen $-0{,}427$
seyreltilmiş bir gerçek değil, **gürültünün ürettiği bir yapaylıktır.**

> **88_TARAMA'nın null sonucu ayakta.** Ve şimdi daha güçlü: yalnız "eşiği aşan yok" değil,
> "en iyi aday gürültü artefaktı".

---

## 4. Ama projenin en eski açık maddesi **ayakta kalıyor**

Aynı hata bütçesi 97_BTFR md. 2'nin sınıf bandına uygulandı. $\ln k$ için:

$$\frac{d\ln k}{d\ln D}=-\frac{2}{\text{F4 payı}}\qquad(\text{payı medyan }0{,}64)$$

| | dex |
|---|---|
| $e_D/D$ medyan | 0,139 |
| beklenen **galaksi başına** $k$ saçılması | 0,243 |
| **ölçülen** galaksi başına $k$ saçılması | **0,445** |
| → mesafe hatasının payı | **%30** (varyans) |

Sınıf **medyanları** için mesafe hatası $\sqrt{n}$ ile azalır ($n=12$–30):

| | dex |
|---|---|
| beklenen sınıf-medyanı saçılması | 0,0577 |
| **ölçülen sınıf bandı** ([94_YEREL_LOMEGA](../94_YEREL_LOMEGA/CALISMA.md) B) | **0,1130** |
| → mesafe hatasının payı | **%26** (varyans) |

**Sınıf bandı gerçektir.** Mesafe hatası dörtte birini açıklıyor, geri kalan %74 gerçek.
97_BTFR md. 2 **açık kalıyor** — ve bu, bu dosyanın teorinin lehine tek sonucu.

---

## 5. Dürüstlük kayıtları

1. **Bu dosya kendi çalışmamın üç dosyasını zayıflatıyor.** GOZLEMSEL.md md. 4'ün "%68
   galaksiler arası" ifadesi ve ona dayanan "adsız sistematik" anlatısı beşte birine indi.
   O dosyalar geri çekilmedi ama **bu düzeltmeyle birlikte okunmalıdır.**
2. **Gürültü tahmini kendi belirsizliğini taşıyor.** SPARC'ın $e_D$ ve $e_i$ değerleri
   yayınlanmış tahminlerdir; küçük ya da büyük olabilirler. $e_D$ %20 yanlışsa mesafe payı
   %59'dan %42 ya da %85'e kayar.
3. **Mesafe ve eğiklik hataları bağımsız varsayıldı.** Gerçekte ikisi de aynı gözlemsel
   modelden gelir (HI hız alanı hem eğikliği hem Tully-Fisher mesafesini besler) ve
   ilişkili olabilirler; ilişkiliyse toplam gürültü **fazla** hesaplanmıştır.
4. **Doğrusallaştırılmış türevler kullanıldı.** $e_D/D\sim0{,}14$ ve $e_i\sim4°$ için makul,
   ama $\cot i$ terimi yüz-üstü galaksilerde ($i\to30°$) hızla büyür ve doğrusallaştırma
   orada zayıflar.
5. **Galaksi içi varyansın gürültüsü ayrılmadı.** Yalnız galaksiler-arası bileşen için bütçe
   kuruldu. Toplam varyans ayrıştırması bu yüzden hâlâ tam değil.
6. **Az-gürültülü yarı n=19.** Md. 3'ün tuzak denetimi bu küçük örnekleme dayanıyor; yön
   açık ama sayı zayıf.
7. **Yoğun rejimde n=38.** 88_TARAMA'nın çözünürlük uyarısı aynen geçerli.

---

## 6. Ne çıktı — üç cümle

1. **«%68 galaksiler arası»nın %78'i hata bütçesidir** — tek başına **mesafe hatası %59.**
   Gerçek galaksi-başına değişim toplam varyansın ~%15'i.
2. **Seyreltme düzeltmesi log $V_{flat}$'i $-0{,}92$ gibi gösteriyor ama tuzak:** az-gürültülü
   yarıda $-0{,}209$'a düşüyor, yani korelasyon gürültünün kendisinden geliyor.
   **88_TARAMA'nın null sonucu ayakta ve güçlendi.**
3. **Ama sınıf bandı gerçek:** mesafe hatası onun yalnız %26'sını açıklıyor. **97_BTFR md. 2
   açık kalıyor.**

## 7. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **Mesafe hatasını modele kat** — $D$'yi galaksi başına serbest bırakıp önselini $e_D$ ile ver (Bayes) | md. 1 — mesafe saçılmanın %59'u; onu yok saymak bütün galaksi-başına sonuçları bozuyor |
| 2 | GOZLEMSEL.md ve AYIRMA.md'ye bu düzeltmenin notunu düş | md. 5.1 |
| 3 | Galaksi içi varyansın gürültüsünü de ayır | md. 5.5 |
| 4 | Sınıf bandını kalan %74 için yeniden incele | md. 4 — tek gerçek açık kalem orada |

**Madde 1 bu çalışmanın bundan sonraki en yüksek getirili işi.** Mesafe hatası galaksi-başına
saçılmanın %59'u; onu önselli bir parametre olarak modele katmak, hem sınıf bandını hem
$\ell_\omega^{mikro}$ saçılmasını hem 97_BTFR md. 2'yi aynı anda temizler. Kitabın 7.4'ünde
zaten kayıtlı olan *"önseller yok"* eksiği ile aynı iştir.
