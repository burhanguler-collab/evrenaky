# Sınıf-içi sürüklenme sınavı — sürüklenme galaksi-İÇİdir; λ aklandı, pencere hedefte (iş 7)

**Soru** (`TOPLANMA_TURETIMI.md` md. 3, aday ii): RAR artık sürüklenmesi geçiş **biçiminin** mi,
yoksa düşük-ivme kuşaklarını dolduran sınıfların pencere-üstü çarpanlarının (λ kanalı) mı eseri?
**Yöntem:** sabit-etkiler ayrıştırması — artık $=\log g_{obs}-\log g_{öng}$ (resmî B, adil
kalibre $k=1{,}011$), üç katman: küresel · sınıf-içi (sınıf ortalamaları düşülmüş) · galaksi-içi
(galaksi ortalamaları düşülmüş) + aralar. Okuma kuralı önceden yazıldı (betik başlığı).
Hesap: `../../sinif_ici_suruklenme.py` (141 galaksi, 2995 nokta).

## 1. Sonuç — ayrıştırma tablosu

| Katman | Eğim (dex/dex) |
|---|---|
| Küresel (referans) | −0,043 |
| Sınıf-içi (sabit etki) | −0,079 |
| **Galaksi-içi (sabit etki)** | **−0,074** *(galaksi-başına eğim medyanı −0,053, $n=141$)* |
| Galaksiler-arası (141 ortalama) | −0,028 |
| **Sınıflar-arası (6 medyan)** | **+0,0006 ≈ 0** |

Sınıf kırılımı: medyan artıklar ofset taşır (Sd $+0{,}061$, Im $-0{,}098$ — band) ama medyan
$g_{bar}$'a karşı **eğilimsizdir**; sınıf-içi eğimlerin çoğu negatif ve geç tiplerde büyür
(Sd $-0{,}18$, Im $-0{,}28$; aykırı: Sdm-Sm $+0{,}07$).

## 2. Hüküm

1. **Aday (ii) ÇÜRÜDÜ:** sürüklenme sınıf kanalının izi değildir — sınıflar-arası bileşen tam
   sıfır. λ/sınıf kanalı **bandı (ofsetleri)** taşır, sürüklenmeyi taşımaz; iki borç
   birbirinden **ayrışmıştır** (bu, 95_RAR md. 9-2 ve 97_BTFR md. 8'in "ivme sınıf saçılmasının
   mekanizması değil" bulgusunun tersten doğrulamasıdır).
2. **Geçiş-biçimi borcu gerçek ve galaksi-İÇİdir:** tipik galaksinin kendi içinde, iç (yüksek
   $g_{bar}$) bölge fazla, dış (düşük $g_{bar}$) bölge eksik öngörülür; galaksi-içi eğim −0,074 —
   küresel −0,043 bunun karışımla seyreltilmiş hâlidir. Galaksi içinde $g_{bar}$ yarıçapla
   birebir düştüğünden bu, **radyal bir pencere imzasıdır**: F4 içte bastırılmalı, dışta
   (göreli olarak) güçlenmelidir.
3. **Tek hedef kaldı — aday (i):** kanal-arası bastırma / geçiş penceresinin türetimi. Bu,
   $r_0$'ın türetimiyle (Blok H, H.2 öncelik 1) aynı iştir ve artık keskin bir sayısal hedefi
   vardır: türetilen pencere, galaksi-içi artık eğimini $-0{,}07$'den $\approx0$'a çekmelidir —
   kayma ağırlığı gibi *yanlış* pencereler bunu sağlayamıyor (TOPLANMA_TURETIMI md. 2), yani
   ölçü ayırt edicidir.

## 3. Dürüstlük kayıtları

1. Galaksi-içi noktalar bağımsız değildir; eğimler tanımlayıcıdır, $p$ üretilmemiştir. Ama üç
   katmanın **sıralaması** (iç ≫ arası ≈ 0) gürültü yorumuna kapalıdır: galaksi-başına eğim
   medyanı da (−0,053) aynı işarettedir.
2. Sdm-Sm'nin pozitif sınıf-içi eğimi (+0,07) aykırıdır ve açıklanmamıştır; pencere türetimi
   bu sınıfta da sınanmalıdır.
3. Sabit-etki eğimleri EKK'dır; adil-kalibre $k=1{,}011$ vortisite taramasından alınmıştır,
   bu sınav için yeniden ayarlanmamıştır.
4. Bu sınav Claude Fable 5 tarafından koşulmuştur; okuma kuralı betiğe veriden önce yazılmıştır.
