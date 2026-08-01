# 93_G_YEREL — $\mathcal{G}$ yerel mi? · Çalışma dosyası

**737 ölçüm noktası · 110 galaksi · fit yok · $a_0$ oynatılmadı**

Hesap: `../../g_yerel_sinavi.py` · Çıktılar: [`SONUC.csv`](SONUC.csv) · [`g_yerel.png`](g_yerel.png)

---

## 0. Sınanan iddia

Teoride $\mathcal{G}=\alpha/\rho_n$. $\rho_n$ ortamın **yerel** yoğunluğudur; $c$'nin sabit
olmadığı bir kuramda (Postülat 4) $\mathcal{G}$ de sabit olamaz. Madde ortamı sıkıştırıyorsa
yoğun bölgede $\rho_n$ artar → **$\mathcal{G}$ düşer.**

Yani teori şunu **öngörür**: $\mathcal{G}_{yerel}/G$, yerel baryonik yüzey yoğunluğuyla
azalmalı.

**Ölçüm.** F4'ün payının düşük olduğu bölgede öngörü F1 baskındır:

$$\frac{\mathcal{G}_{yerel}}{G}=\frac{v_{gözl}^2-v_{F4}^2}{V_{bar,Newton}^2}$$

$V_{bar}$ SPARC'tan gelir ve **evrensel Newton $G$'siyle** hesaplanmıştır. Oran 1'den saparsa
ya $\mathcal{G}$ yereldir, ya $\Upsilon_*$ yanlıştır, ya da F1'in kendisi eksiktir.
F4 için [94_YEREL_LOMEGA](../94_YEREL_LOMEGA/CALISMA.md)'nın B kurulumu kullanıldı.

---

## 1. Sonuç 1 — eğilim **var ve öngörülen yönde**

| $\log\Sigma_*$ ($M_\odot$/pc²) | n | $\mathcal{G}_{yerel}/G$ medyan | saçılma |
|---|---|---|---|
| 1,50 – 1,75 | 67 | **1,138** | 0,291 |
| 1,75 – 2,00 | 96 | 1,009 | 0,184 |
| 2,00 – 2,25 | 129 | 1,047 | 0,295 |
| 2,25 – 2,50 | 121 | 0,984 | 0,266 |
| 2,50 – 2,75 | 76 | 0,797 | 0,257 |
| 2,75 – 3,00 | 81 | 0,821 | 0,188 |
| 3,00 – 3,25 | 48 | 0,784 | 0,323 |
| 3,25 – 3,50 | 36 | **0,821** | 0,442 |

$$\frac{d\log(\mathcal{G}_{yerel}/G)}{d\log\Sigma_*}=\mathbf{-0{,}093}
\qquad \text{Spearman}=\mathbf{-0{,}305}\ (n=737)$$

**İşaret teorinin öngördüğü işarettir.** Ve kararlı: F4 payı eşiği 0,15 / 0,25 / 0,35 / 0,50
alındığında Spearman sırasıyla $-0{,}39$ / $-0{,}32$ / $-0{,}31$ / $-0{,}32$.

Galaksi başına kümelendiğinde (noktalar bağımsız değil): Spearman $-0{,}620$, eğim
$-0{,}589$ dex/dex — **çok daha dik.** İki ölçek aynı şeyi ölçmüyor olabilir; galaksi düzeyi
sınıf saçılmasını da taşır. **Eğimin büyüklüğü belirsizdir; güvenilir olan işaretidir.**

---

## 2. Sonuç 2 — dejenerasyon **kırılamadı, ve bu yapısal**

$$V_{bar}^2=\frac{\mathcal{G}_{yerel}}{G}\Big[\,\underbrace{V_{gaz}^2}_{\Upsilon_*\ \text{yok}}
+\ \Upsilon_*V_{disk}^2+R_B\Upsilon_*V_{kovan}^2\,\Big]$$

$\mathcal{G}$'yi %20 büyütmek ile $\Upsilon_*$'ı %20 büyütmek **yıldız terimi için aynı
şeydir.** Ama gaz terimi $\Upsilon_*$ içermez — yani gaz baskın noktalar ikisini ayırır:

- oran gaz kesrinden **bağımsız** → $\mathcal{G}$ yerelliği
- oran gaz kesriyle **değişiyor** → $\Upsilon_*$ yanlışlığı

**Bu kaldıraç yok.** Dört ayrı kesitte de (pay < 0,15 / 0,25 / 0,35 / 0,50) noktaların
**tamamı** gaz kesri $<0{,}2$ kuşağında kaldı. Sebep basit ve yapısaldır: F4'ün payının
düşük olduğu bölge zaten **yıldız baskın** bölgedir. Veri eksikliği değil, ölçümün sınırı.

> **Bu yöntemle $\mathcal{G}$ ile $\Upsilon_*$ ayrılamaz.** Bunu bir eksiklik olarak kaydediyorum,
> bir yorumla örtmüyorum.

---

## 3. Ama bir **işaret argümanı** var — ve teorinin lehine

| | Ne gerektirir |
|---|---|
| **Ölçülen** | oran $\Sigma_*$ ile **azalıyor** |
| $\Upsilon_*$ açıklaması | $\Upsilon_*$ yoğunlukla **azalmalı** |
| Yıldız nüfusu fiziği | 3,6 µm'de yoğun bölgeler (kovan, iç disk) **yaşlı ve kırmızıdır** → $\Upsilon_*$ **artmalı** |
| $\mathcal{G}=\alpha/\rho_n$ | yoğun yerde **azalmayı doğrudan öngörür** |

**$\Upsilon_*$ açıklaması, yıldız nüfusu fiziğiyle ters işaret istiyor.** Teorinin açıklaması
istemiyor.

Bu bir **kanıt değildir** — dejenerasyon kırılmadı, ve $\Upsilon_*$'ın 3,6 µm'deki gerçek
gradyanı bu çalışmada ölçülmedi. Ama iki açıklamadan biri fizikle uyumlu, öteki değil.

*(Not: sapma yalnız $\Upsilon_*$ ile kapatılsaydı $\Upsilon_*=0{,}50\times0{,}930=0{,}465$
olurdu — popülasyon sentezi bandının 0,3–0,8 içinde. Yani ortalama değer olarak $\Upsilon_*$
açıklaması da elenemiyor; elenemeyen şey **sabit** bir $\Upsilon_*$ değil, eğimin işaretidir.)*

---

## 4. Sonuç 3 — genel ölçek

| | |
|---|---|
| $\mathcal{G}_{yerel}/G$ medyan | **0,930** |
| saçılma | 0,306 dex |
| çeyreklikler | 0,78 – 1,24 |

Medyan 1'e yakın: **F1'in genel ölçeği doğru.** Sapma bir eğilimdir, bir kayma değil. Bu,
$\mathcal{G}=\alpha/\rho_n$ okumasıyla tutarlı — ortalama yoğunlukta $\mathcal{G}\approx G$,
uçlarda sapıyor.

Ama saçılma **büyük** (0,306 dex, yani ×2). Bunun ne kadarı gerçek $\mathcal{G}$ değişimi,
ne kadarı ölçüm hatası, eğiklik belirsizliği ve $\Upsilon_*$ galaksi-içi gradyanı — **ayrılmadı.**

---

## 5. Dürüstlük kayıtları

1. **Dejenerasyon kırılmadı** (md. 2). Bu dosyanın en önemli sınırıdır ve başlıkta durmalı:
   ölçülen şey "$\mathcal{G}$ yereldir" değil, "**F1'in normalizasyonu yüzey yoğunluğuyla
   azalıyor**"dur. İki yorumdan hangisi doğruysa o.
2. **Noktalar bağımsız değil.** 737 nokta 110 galaksiden gelir. Kümelenmiş ölçüm ayrıca
   verildi ve **altı kat daha dik** bir eğim çıkardı ($-0{,}589$ vs $-0{,}093$). Bu fark
   açıklanmadı; galaksi düzeyi büyük olasılıkla sınıf saçılmasını da taşıyor.
3. **Eğilim tekdüze değil.** 2,00–2,25 ve 2,75–3,00 kuşakları komşularının üstünde. Sekiz
   kuşağın hepsi tek yönde inmiyor; eğim genel bir eğilimdir, bir yasa değil.
4. **F4 modeli sonuca giriyor.** $v_{F4}$ çıkarılıyor ve o, 94_YEREL_LOMEGA'nın B kurulumundan
   geliyor — kendisi de türetilmemiş bir kurulum. Eşik 0,15'te F4'ün etkisi asgarîdir ve
   eğilim orada da aynı ($-0{,}39$); ama sıfır değildir.
5. **$\Sigma_*$ ile $V_{bar}$ aynı fotometriden gelir.** İkisi aynı verinin farklı
   fonksiyonelleridir (yerel vs integral), yani tümüyle bağımsız değildir. Ortak bir
   fotometri yanlılığı ikisine birden girer.
6. **$\Upsilon_*$'ın galaksi-içi gradyanı ölçülmedi.** Md. 3'ün argümanı literatür
   beklentisine dayanıyor, bu çalışmanın bir ölçümüne değil.
7. **Bu sınav teoriyi doğrulamıyor, bir öngörüsünün işaretini doğruluyor.** Fark önemlidir:
   $\mathcal{G}=\alpha/\rho_n$'nin **niceliksel** biçimi ($\rho_n$'nin $\Sigma_{bar}$'a nasıl
   bağlandığı) hiç sınanmadı, çünkü teori onu henüz vermiyor.

---

## 6. Ne çıktı — üç cümle

1. **F1'in normalizasyonu yüzey yoğunluğuyla azalıyor** — eğim $-0{,}093$ dex/dex, Spearman
   $-0{,}305$, dört ayrı kesitte kararlı. İşaret teorinin öngördüğü işarettir.
2. **Ama $\mathcal{G}$ ile $\Upsilon_*$ ayrılamıyor** ve ayrılamaması yapısaldır: F4'ün
   ihmal edilebilir olduğu bölge zaten yıldız baskındır, gaz kaldıracı hiçbir kesitte doğmuyor.
3. **Yine de iki açıklamadan biri fizikle uyumsuz:** $\Upsilon_*$ savı, 3,6 µm'de yoğun
   bölgelerin daha yaşlı olması gerçeğiyle **ters işaret** istiyor. $\mathcal{G}=\alpha/\rho_n$
   istemiyor.

## 7. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **Gaz baskın sistemlerde ayrı sınav kur** — F4'ü çıkarmak yerine *modelleyip* gaz zengini dış bölgelere git | md. 2 — dejenerasyonu kırmanın tek yolu; bu bölgede F4 baskın olduğu için F4 modeli sınava girer, o yüzden 94'ün 2. maddesi önce çözülmeli |
| 2 | $\Upsilon_*$'ın 3,6 µm galaksi-içi gradyanını literatürden **girdi** al, oranı ondan arındır | md. 6 — argümanı ölçüme çevirir |
| 3 | Teoriden $\rho_n(\Sigma_{bar})$ bağıntısını türet | md. 7 — şu an yalnız işaret sınanabiliyor, biçim değil |
| 4 | Eğiklik ve mesafe belirsizliğini saçılma bütçesine kat | md. 4 — 0,306 dex'in ne kadarı gerçek, bilinmiyor |

**Madde 3 kritik.** Teori $\mathcal{G}$'nin yoğunlukla azaldığını söylüyor ama **ne kadar**
azaldığını söylemiyor. O bağıntı olmadan bu sınav bir işaret kontrolünden öteye geçemez.
