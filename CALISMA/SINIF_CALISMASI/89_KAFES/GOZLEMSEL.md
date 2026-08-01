# Dördüncü aday sınandı — basınç desteği, eğiklik **ve mesafe**

Hesap: `../../gozlemsel_ayirma_sinavi.py` · Çıktılar: [`GOZLEMSEL.csv`](GOZLEMSEL.csv) ·
[`gozlemsel.png`](gozlemsel.png) · Ön adım: [`AYIRMA.md`](AYIRMA.md)

**Yoğun rejim ($\log g_{bar}\geq-10$): 694 nokta, 52 galaksi · fit yok**

---

## 0. Açıklanacak olgu

Yoğun rejimde **baryonlar tek başına gözlemi aşıyor:** $V_{bar}^2>v_{gözl}^2$, noktaların
%31,5'inde (2σ ötesinde %11,8). $F4$ pozitif tanımlı olduğu için ona dokunan hiçbir hikâye
bunu kapatamaz. [AYIRMA.md](AYIRMA.md) üçünü ele aldı — $\Upsilon_*$ elendi, KAFES elendi,
$\mathcal{G}$ ayakta — ve dördüncüyü açıkta bıraktı: **$v_{gözl}$'ün kendisi eksik olabilir.**

---

## 1. (4a) Basınç desteği — **elendi, radyal imzası ters**

Hız dağılımı varsa gözlenen dönme gerçek dairesel hızdan küçüktür:

$$v_c^2=v_{dönme}^2+3{,}36\,\sigma^2\frac{R}{R_{1/2}}
\;\;\xrightarrow{R_{1/2}=1{,}678R_d}\;\;
v_c^2-v_{dönme}^2=2{,}00\,\sigma^2\frac{R}{R_d}$$

**Yönü doğru** — gerçek $v_c$ daha büyükse açık küçülür. Ama **imzası var:** düzeltme $R$ ile
**doğrusal büyür.**

| Gereken $\sigma$ | |
|---|---|
| medyan | **62,6 km/s** |
| %90 | 177 km/s |
| *gözlenen: gaz 8–12 · yıldız diski 20–40 · kovan 100–200* | |

Zaten ağır. Ama belirleyici olan imza:

| $R/R_{disk}$ | n | $D$ medyan | $D/v_{öng}^2$ |
|---|---|---|---|
| 0,0 – 0,5 | 180 | 14 484 | **0,227** |
| 0,5 – 1,0 | 186 | 11 476 | 0,198 |
| 1,0 – 1,5 | 119 | 7 162 | 0,110 |
| 1,5 – 2,5 | 155 | −1 017 | −0,019 |
| 2,5 – 6,0 | 54 | −428 | **−0,010** |

$$\text{Spearman}[D/v_{öng}^2,\;R/R_{disk}]=\mathbf{-0{,}382}$$

**4a pozitif bekliyor. Ölçülen negatif.** Açık *içe doğru* büyüyor, düzeltme *dışa doğru*
büyümek zorunda. **Disk asimetrik sürüklemesi elendi.**

### Kovan basıncı ayrı sınandı — o da yetmiyor

Kovan içinde $\sigma$ yüksek olduğu için basınç desteği orada gerçekten büyüktür ve
yukarıdaki $\propto R$ formülü geçerli değildir. Bu yüzden ayrı bakıldı:

| kovan kesri | n | $D/v_{öng}^2$ |
|---|---|---|
| **0,00 – 0,01 (kovansız)** | **152** | **0,166** |
| 0,01 – 0,15 | 33 | 0,203 |
| 0,15 – 0,35 | 97 | −0,036 |
| 0,35 – 1,00 | 412 | 0,189 |

Spearman $+0{,}155$ — zayıf ve tekdüze değil. **Kovanı hiç olmayan 152 noktada açık hâlâ
0,166.** Kovan basıncı açığın bir kısmını taşıyabilir ama **tek başına yetmez.**

---

## 2. (4b) Eğiklik — **yetmiyor**

$v_{gözl}\propto1/\sin i$. $i$ fazla tahmin edilmişse $v_{gözl}$ küçük çıkar.

| | |
|---|---|
| gereken $\lvert\Delta i\rvert$ medyan | **7,9°** (%90: 25,5°) |
| SPARC'ın bildirdiği $e_i$ medyan | **4,0°** |
| kayma $2e_i$'yi aşan nokta | **%47,1** |

**Gereken kayma bildirilen hatanın ~2 katı**, ve yarısında 2σ'yı aşıyor.

Ve eğiklikle ilişki yok: Spearman $+0{,}123$, kuşaklar tekdüze değil (0,124 → 0,206 → 0,117 →
0,218). 4b doğruysa açık **düşük** eğiklikte büyük olmalıydı ($\sin i$ belirsizliği yüz-üste
doğru büyür); öyle değil.

**Eğiklik tek başına elendi.**

---

## 3. (4c) Mesafe — sınava sonradan eklendi ve **elendi**

Varyans ayrıştırması (md. 4) galaksi başına bir sistematik olduğunu gösterdiği için mesafe
hatasını da sınamak zorunlu oldu. $V_{bar}^2\propto D$ (fotometrik kütle $D^2$, yarıçap $D$),
$v_{gözl}$ ise mesafeden **bağımsız.** Yani mesafe hatası tam bu tür bir açık üretir ve
**galaksi başınadır.**

| | |
|---|---|
| gereken $\lvert\Delta D/D\rvert$ medyan | 15,4% |
| SPARC'ın bildirdiği $e_D/D$ medyan | 14,4% |

Büyüklük olarak **makul** görünüyor. Ama belirleyici sınav mesafe **yöntemidir:**

| $f_D$ (yöntem) | n galaksi | $D/v_{öng}^2$ | $e_D/D$ |
|---|---|---|---|
| 1 — Hubble akışı | 22 | 0,127 | 25,0% |
| **2 — TRGB** | 5 | **0,245** | **5,0%** |
| 4 — UMa üyeliği | 8 | 0,198 | 13,9% |

$$\text{Spearman}[\text{açık},\;e_D/D]=\mathbf{-0{,}043}$$

**Mesafesi en iyi bilinen galaksilerde açık EN BÜYÜK.** Mesafe hatası sebep olsaydı tam tersi
olurdu. Korelasyon sıfır. **Mesafe elendi.**

*(Uyarı: TRGB kümesi yalnız 5 galaksi. Ama 38 galaksi üzerinden korelasyon da sıfır, yani
sonuç tek bir küçük kümeye dayanmıyor.)*

---

## 4. Varyans ayrıştırması — **ve asıl bulmaca burada**

Açık galaksi **başına** mı, galaksi **içinde** mi değişiyor?

| | varyans | pay |
|---|---|---|
| galaksiler **arası** | 0,0429 | **%68** |
| galaksi **içi** | 0,0203 | %32 |

> ### DUZELTME -> [88_TARAMA/GURULTU.md](../88_TARAMA/GURULTU.md)
>
> Bu %68'in **%78'i hata butcesidir** (mesafe %59 · egiklik %15 · v_gozl %4).
> Gercek galaksiler-arasi pay toplam varyansin ~**%15'i.** Mesafe ve egiklik
> acigin ORTALAMASININ sebebi olarak elenmisti (md. 2-3) ama SACILMAYA katkilari
> ayri bir seydir ve orada hesaplanmadi. Asagidaki "adsiz %68" okumasi bu
> duzeltmeyle birlikte okunmalidir.

**Açığın üçte ikisi galaksiden galaksiye değişiyor.** Bu, bir mantık zinciri kuruyor:

| Aday | Nerede değişir | Durum |
|---|---|---|
| mesafe | **galaksi başına** | **elendi** (md. 3) |
| eğiklik | **galaksi başına** | **elendi** (md. 2) |
| $\Upsilon_*$ | **galaksi başına** | **elendi** ([AYIRMA.md](AYIRMA.md) md. 3) |
| basınç desteği | yarıçapla | **elendi** (md. 1) |
| KAFES | yarıçapla | **elendi** (AYIRMA.md md. 2) |
| $\mathcal{G}(\rho_{yerel})$ | **yarıçapla** | ayakta — ama %68'i açıklayamaz |

> ### Elemelerden sonra geriye kalan
>
> Galaksi başına değişen bütün **bilinen** adaylar elendi. Yarıçapla değişen adaylardan
> yalnız $\mathcal{G}$ ayakta, ama o da varyansın **%32'sini** açıklayabilir.
>
> Yani **açığın %68'i için elimizde adlandırılmış bir sebep yok.**

### Bunun bir okuması var — ve teorinin içinde

$\mathcal{G}=\alpha/\rho_n$'de $\rho_n$ **ortamın** yoğunluğudur. Eğer ortamın durumu
noktadan noktaya değil **galaksi ölçeğinde** belirleniyorsa, $\mathcal{G}$ galaksi başına bir
sayı olur — ve %68 tam olarak bunu söyler.

Bu, [97_BTFR](../97_BTFR/CALISMA.md) md. 2'nin yıllardır açık duran maddesine de bir aday
verir: sınıflar arası çarpan bandı (×1,14–2,67) **galaksi başına $\mathcal{G}$** olabilir.

**Ama bu bir hipotez.** Ölçülen şey "%68 galaksi başına"dır; ona *"$\mathcal{G}$ galaksi
ölçeğinde belirlenir"* demek bir yorumdur, ölçüm değil.

---

## 5. Dürüstlük kayıtları

1. **Mesafe adayını ben başta atlamıştım.** AYIRMA.md'de "gözlemsel" adayı basınç desteği ve
   eğiklikle sınırlı yazmıştım; mesafe daha güçlü bir adaydı ($V_{bar}^2\propto D$ tam olarak
   gereken ölçekleme) ve varyans ayrıştırması onu zorunlu kıldı.
2. **TRGB kümesi n=5.** Md. 3'ün en zayıf noktası. Bütün örneklem üzerinden korelasyonun
   sıfır olması bunu destekliyor ama küçük sayı uyarısı geçerli.
3. **Kovan basıncı tam olarak modellenmedi.** Küresel bir bileşen için doğru düzeltme
   Jeans denklemidir, $\propto R$ formülü değil. Md. 1'in son bölümü kovanı yalnız
   *korelasyonla* elemiştir, hesapla değil.
4. **Gereken $\sigma$ hesabı $R_{disk}$'e bağlı** ve SPARC'ın $R_{disk}$'i tek üstel disk
   uydurmasından gelir; kovanlı sistemlerde anlamı zayıflar.
5. **%68 galaksiler arası oranı, aykırı galaksilere duyarlıdır.** Galaksi başına en az 3
   nokta koşulu konuldu; ağırlıklandırma yapılmadı. Kırpma denenmedi.
6. **Dördüncü adayın üçüncü bacağı sınanmadı:** daireden sapan hareketler (bar, warp,
   spiral kol akışları). Onlar da $v_{gözl}$'ü etkiler, galaksi başına **ve** yarıçapla
   değişir, ve SPARC'ta ölçülmemiştir.
7. **Bu dosya hiçbir hikâyeyi doğrulamıyor** — dördünü eledi ve geriye adı olmayan bir
   %68 bıraktı. Eleme, açıklama değildir.

---

## 6. Ne çıktı — üç cümle

1. **Dördüncü adayın üç bacağı da elendi:** disk basınç desteği (radyal imza ters, $-0{,}382$),
   eğiklik (gereken 7,9° vs bildirilen 4,0°, korelasyon yok), mesafe (en iyi mesafeli
   galakside açık en büyük, korelasyon $-0{,}043$).
2. **Kovan basıncı açığın bir kısmını taşıyabilir ama kovansız 152 noktada açık hâlâ 0,166.**
3. **Asıl bulgu varyans ayrıştırması:** açığın **%68'i galaksiden galaksiye** değişiyor, ve
   galaksi başına değişen bütün bilinen adaylar elendi. **Adı olmayan bir sistematik var.**

## 7. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **Galaksi başına açığı neyin öngördüğünü tara** (kütle, $\Sigma$, morfoloji, $V_{max}$, gaz kesri, $Q$, $R_d$, çevre) | md. 4 — %68'in adı yok; bulunması gereken şey bu |
| 2 | Daireden sapan hareketleri ele al (bar/warp/kol) | md. 5.6 — dördüncü adayın sınanmamış bacağı |
| 3 | Kovan basıncını Jeans denklemiyle doğru modelle | md. 5.3 |
| 4 | %68'i galaksi başına $\mathcal{G}$ hipoteziyle sına — 97_BTFR md. 2'nin bandıyla örtüşüyor mu? | md. 4'ün son kutusu |

**Madde 1 önce ve tek başına.** Elemeler bitti; şimdi %68'i öngören değişkeni bulmak gerekiyor.
O bulunmadan hangi fiziğin sorumlu olduğu söylenemez — ve bulunursa 97_BTFR md. 2 de
kapanabilir.
