# Mutlak açık üç hikâyeye karşı sınandı — **dejenerasyon kırıldı**

Hesap: `../../acik_ayirma_sinavi.py` · Çıktılar: [`AYIRMA.csv`](AYIRMA.csv) · [`ayirma.png`](ayirma.png)
Ön adım: [`CALISMA.md`](CALISMA.md) md. 4

**2889 nokta · 137 galaksi · fit yok**

---

## 1. Ölçülen açık ve üç aday

$$D(R)\;=\;V_{bar}^2+v_{F4}^{teori}-v_{gözl}^2 \;>\;0\quad(\text{yoğun bölgede})$$

Üç hikâye aynı sayıyı üretiyordu. Ama **farklı terimleri ölçekliyorlar**, ve bu onları
ayırıyor:

| Hikâye | Ne ölçekleniyor | Denklem | **Fiziksel sınır** |
|---|---|---|---|
| **KAFES** | yalnız $F4$ | $v_{gözl}^2=V_{bar}^2+s\,v_{F4}$ | $s\geq0 \Rightarrow \mathbf{D\leq v_{F4}}$ |
| **$\mathcal{G}$** | **bütün** $v^2$ | $v_{gözl}^2=u\,(V_{bar}^2+v_{F4})$ | $u\geq0 \Rightarrow \mathbf{D\leq v_{öng}^2}$ |
| **$\Upsilon_*$** | yalnız yıldız terimi | $v_{gözl}^2=v_{gaz}^2+w\,v_{yıl}^2+v_{F4}$ | $\Upsilon_*=0{,}5w \in [0{,}3;0{,}8]$ |

> **Neden $\mathcal{G}$ bütün $v^2$'yi ölçekler:** $V_{bar}^2\propto\mathcal{G}$ **ve**
> $v_{F4}^2=\sqrt{\mathcal{G}Ma_0}$ ile $a_0=\mathcal{G}m_n/\ell_\omega^2$ olduğundan
> $v_{F4}^2\propto\mathcal{G}$ de olur. İkisi aynı ölçekle — bu,
> [92_M_TUT](../92_M_TUT/CALISMA.md)'un türetiminin doğrudan sonucu.

**Ölçüt saçılma değil.** Saçılma karşılaştırması adil olmaz: her hikâye farklı büyüklükte bir
sayıya bölüyor. Adil ölçüt: **her hikâye kaç noktada fiziksel olarak imkansız bir değer
istiyor?**

---

## 2. Sınav A — imkansızlık, kuşak kuşak

| $\log g_{bar}$ | n | **KAFES** | **$\mathcal{G}$** | **$\Upsilon_*$** |
|---|---|---|---|---|
| −12,0 … −11,5 | 182 | 0,5% | **0,0%** | 97,8% |
| −11,5 … −11,0 | 806 | 0,7% | **0,0%** | 81,9% |
| −11,0 … −10,5 | 624 | 0,3% | **0,0%** | 61,5% |
| −10,5 … −10,0 | 578 | 1,7% | **0,0%** | 44,5% |
| −10,0 … −9,5 | 373 | **10,7%** | **0,0%** | 34,6% |
| **−9,5 … −9,0** | 230 | **24,8%** | **0,0%** | 22,2% |
| **TÜMÜ** | **2889** | **5,5%** | **0,0%** | **58,1%** |

> ### Belirleyici satır
>
> **En yoğun kuşakta — yani tam olarak etkinin olduğu yerde — KAFES hikâyesi noktaların
> %24,8'inde NEGATİF $F4$ istiyor.** Açık, $F4$ teriminin **tamamından** büyük. Kafes tam
> bastırma yapsa bile ($s=0$, F4 tümüyle silinse bile) o açığı kapatamaz.
>
> $\mathcal{G}$ hiçbir kuşakta sınıra dayanmıyor: **%0,0.**

### Ve bu koşul $a_0$'dan **bağımsız** — cebirsel olarak sadeleşiyor

$$D>v_{F4} \iff V_{bar}^2+v_{F4}-v_{gözl}^2>v_{F4} \iff \boxed{V_{bar}^2>v_{gözl}^2}$$

**$v_{F4}$ sadeleşiyor.** Yani KAFES'i eleyen şey bir model karşılaştırması değil, şu çıplak
olgudur: **baryonlar tek başına gözlemi aşıyor.** $F4$ pozitif tanımlı olduğundan eklenen her
şey durumu kötüleştirir — bastırma da kurtarmaz, sıfırlamak da.

Denetim: $a_0$ çarpanı ×1,0 / ×1,5 / ×2,08 / ×3 / ×6 alındı — **oran hiç değişmiyor.**
(Md. 5.4'te *"hüküm $a_0$'a duyarlı"* diye yazdığım çekince böylece **kapandı**; duyarlı değil.)

**Ölçüm gürültüsü mü?** En yoğun rejimde ($\log g_{bar}\geq-9{,}5$, $n=321$):

| | |
|---|---|
| $V_{bar}>v_{gözl}$ | **31,5%** |
| ve $V_{bar}>v_{gözl}+2\sigma_v$ | **11,8%** |

Noktaların **%11,8'inde aşım ölçüm hatasının 2σ ötesinde.** Gürültü değil.

## 3. Sınav B — gaz baskın noktalar: $\Upsilon_*$'ın kaldıracı yok

| Kesit | n | $D$ medyan | $D/v_{öng}^2$ |
|---|---|---|---|
| $v_{yıl}^2/V_{bar}^2<0{,}15$ | 54 | $+348$ | 0,116 |
| $<0{,}30$ | 189 | $+284$ | 0,081 |

**Açık sürüyor.** Ölçeklenecek yıldız olmayan yerde de açık var — $\Upsilon_*$ tek başına
açıklayamaz.

---

## 4. Hüküm

| Hikâye | Karar | Gerekçe |
|---|---|---|
| **$\Upsilon_*$ tek başına** | **ELENDİ** | %58,1 imkansız + gaz baskın noktada açık sürüyor |
| **KAFES tek başına** | **ELENDİ** | en yoğun kuşakta %24,8'inde **negatif $F4$** gerekiyor |
| **$\mathcal{G}=\alpha/\rho_n$** | **AYAKTA** | hiçbir kuşakta imkansız değer istemiyor (%0,0) |

### Bu, kafes yasasının yanlış olduğu anlamına **gelmez**

Anlamı şu: **açığın tamamı $F4$'ten gelmiyor.** En az bir bileşen $F1$'den gelmek zorunda, ve
$F1$ tarafında $\Upsilon_*$ elendiği için geriye $\mathcal{G}$ kalıyor.

Kafes, açığın bir **parçası** olabilir. Ama tek başına yer yetmiyor — 2889 noktanın 160'ında
matematiksel olarak imkansız.

### Ve bu, teorinin **kendi** yasasını öne çıkarıyor

$\mathcal{G}=\alpha/\rho_n$ zaten teorinin denklemi. [93_G_YEREL](../93_G_YEREL/CALISMA.md)
onu bağımsız olarak ölçmüştü: $\mathcal{G}_{yerel}/G$ medyan **0,930**, yoğunlukla eğim
$-0{,}093$. Bu dosyanın $\mathcal{G}$ okuması aynı sayıya varıyor
($u$ medyan $=1-0{,}054=0{,}946$). **İki bağımsız kurulum, aynı sonuç.**

Yani [89_KAFES/CALISMA.md](CALISMA.md) md. 3'te *"93_G_YEREL'in eğilimi kafes artefaktı
olabilir"* diye yazdığım şey **tersine döndü:** kafes değil, $\mathcal{G}$ birincil.

---

## 5. Dürüstlük kayıtları

1. **Bu sonuç, bir önceki turda söylediğimi keskinleştiriyor ve bir kısmını geri alıyor.**
   Kafes iddiasının *yönü* doğruydu ve etki gerçek (89_KAFES md. 2 duruyor). Yanlış olan,
   onu açığın **tek** sebebi sayabileceğimi ima etmemdi. Ayırıcı sınav bunu eliyor.
2. **$\mathcal{G}$'nin "ayakta kalması" onun doğru olduğunu kanıtlamaz.** En az kısıtlanan
   hikâye olması, en çok serbestliğe sahip olmasından da gelebilir: bütün $v^2$'yi ölçekleyen
   bir çarpan, doğal olarak daha az sınıra dayanır. Bu bir **eleme** sınavıdır, bir seçme
   sınavı değil.
3. **Dördüncü aday sınanmadı:** $v_{gözl}$'ün kendisinin eksik olması (basınç desteği,
   daireden sapan hareket, eğiklik hatası). O da açığı üretebilir ve bu dosyada **hiç
   ele alınmadı.** Özellikle iç bölgede ($\log g_{bar}>-10$) basınç desteği ciddidir.
4. ~~$a_0$ duyarlılığı ölçülmedi~~ → **ölçüldü, çekince kapandı** (md. 2). Koşul cebirsel
   olarak $V_{bar}^2>v_{gözl}^2$'ye sadeleşiyor; $v_{F4}$ düşüyor, yani sonuç $a_0$'dan ve F4
   modelinden **tümüyle bağımsız.** ×1,0'dan ×6'ya kadar oran hiç değişmiyor. Ayrıca aşımın
   %11,8'i ölçüm hatasının 2σ ötesinde — gürültü değil.
5. **Kuşaklar bağımsız değil** — 2889 nokta 137 galaksiden; aynı galaksinin komşu yarıçapları
   ilişkilidir. Yüzdeler nokta sayısına göre; galaksi başına ağırlıklandırma yapılmadı.
6. **Üç hikâye birbirini dışlamaz.** Gerçek durum bir karışım olabilir (kısmen $\mathcal{G}$,
   kısmen kafes, kısmen gözlemsel). Bu sınav yalnız *tek başına yeterli olup olmadıklarını*
   söylüyor.

---

## 6. Ne çıktı — üç cümle

1. **Dejenerasyon kırıldı:** $\Upsilon_*$ ve KAFES tek başına elendi, $\mathcal{G}$ ayakta.
2. **KAFES'i eleyen şey saçılma değil, yer:** en yoğun kuşakta açık $F4$'ün tamamından
   büyük — noktaların %24,8'inde negatif $F4$ gerekir.
3. **Ayakta kalan hikâye teorinin kendi denklemi:** $\mathcal{G}=\alpha/\rho_n$, ve
   93_G_YEREL'in bağımsız ölçümüyle (0,930 vs 0,946) örtüşüyor.

## 7. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **Dördüncü adayı ekle:** basınç desteği / daireden sapan hareketin açığa katkısı | md. 5.3 — hiç ele alınmadı ve iç bölgede büyük olabilir |
| ~~2~~ | ~~$a_0$ duyarlılığını ölç~~ | ✅ **yapıldı** — koşul $a_0$'dan bağımsız çıktı (md. 2) |
| 3 | $\rho_n(\Sigma_{bar})$ bağıntısını teoriden türet | $\mathcal{G}$ ayakta kaldı; şimdi **niceliksel** biçimi gerekiyor |
| 4 | Karışım modelini sına: açığın $x$ kadarı $\mathcal{G}$, $(1-x)$ kadarı kafes | md. 5.6 — ikisi birlikte olabilir |

> ### ✅ Madde 1 yapıldı → [`GOZLEMSEL.md`](GOZLEMSEL.md)
>
> Dördüncü adayın üç bacağı da elendi: **disk basınç desteği** (radyal imza ters, $-0{,}382$),
> **eğiklik** (gereken 7,9° vs bildirilen 4,0°), **mesafe** (en iyi mesafeli galakside açık
> **en büyük**, korelasyon $-0{,}043$).
>
> Ama orada daha önemli bir şey çıktı: **açığın %68'i galaksiden galaksiye değişiyor**, ve
> galaksi başına değişen bütün bilinen adaylar ($\Upsilon_*$, mesafe, eğiklik) **elendi.**
> $\mathcal{G}(\rho_{yerel})$ ise yarıçapla değişir, yani en çok %32'yi açıklayabilir.
> **Açığın üçte ikisinin adı yok.**
