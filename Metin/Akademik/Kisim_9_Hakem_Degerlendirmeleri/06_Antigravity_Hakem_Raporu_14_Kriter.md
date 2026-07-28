# Evrenakı Teorisi — Akademik Sürüm Hakem Raporu
## (99_Hakemlik_Standarti.md'deki 14 Kriterli Standarda Göre)

---

## Beyanlar (Kriter 14 Gereği)

1. **Hakem Kimliği ve Yöntem Beyanı:** Bu rapor, Google DeepMind tarafından geliştirilen **Antigravity AI** yapay zekâ modeli (Advanced Agentic Coding) tarafından üretilmiştir. İnsan akran denetiminin (human peer review) yerine geçmez. Değerlendirme tarihi: **28 Temmuz 2026**. İnceleme, Akademik Sürüm metinlerinin, matematiksel türetimlerin, 7.4/7.5 sınırlılık/öngörü tablosunun, Ek C parametre envanterinin ve `99_Hakemlik_Standarti.md` tüzüğündeki 14 temel kriterin tamamının doğrudan kod/metin taraması ve analiziyle yürütülmüştür.
2. **İlişki ve Çıkar Çatışması Beyanı:** Hakemin yazarla kişisel, kurumsal veya finansal çıkar ilişkisi yoktur. Hakem, bu projede pair-programming ve sistem mimarisi yardımcısı olarak görev yapmaktadır; bu durum raporun epistemolojik nesnelliğini ve sert eleştiri hakkını kısıtlamaz, aksine metnin iç yapısını ve kodlama altyapısını en derin ayrıntısına kadar inceleme imkânı sağlamıştır.
3. **Kapsam Dışı Beyanı:** Kısım 5 (Deneyler ve Kanıtlar) — yazarın çalışma planında ayrı ve sonraya bırakılmış bir yazım/deneysel uygulama fazı olduğundan bu turda değerlendirilmemiştir; hiçbir kriterde deneysel detay eksikliği puan kırma nedeni yapılmamıştır. Standardın yer tutucusu olan Kriter 15 (veri açıklığı) bu nedenle uygulanmamıştır.
4. **Epistemolojik ve Metodolojik Kabul Beyanı:** Teorinin kurucu tercihleri (Zerre akışkanlığı, foton kavramının reddi, değişken $c$, kütle-itim ontolojisi, Büyük Patlama'nın mekanizmalı savunusu) postülat statüsünde kabul edilmiş, varlıkları tek başına kusur sayılmamış; yalnızca tutarlı uygulanışları, nicel sonuçları ve 14 kritere uygunlukları denetlenmiştir.

---

## Puan Tablosu

| # | Kriter | Puan (10 üzerinden) |
|---|---|---|
| 1 | İç tutarlılık ve terminoloji disiplini | 7,0 |
| 2 | Tekil mekanizma ve tutumluluk (Occam'ın Usturası) | 6,5 |
| 3 | Hasım pozisyonun doğru aktarımı (Saman adam denetimi) | 5,0 |
| 4 | Öz-eleştiri, dürüst kayıt + bağımsız karşı-gözlem taraması | 7,5 |
| 5 | Yeniden türetimin değerlendirilmesi ve varsayım bilançosu | 6,0 |
| 6 | Yanlışlanabilirlik öngörülerinin denetimi ve ölüm koşulları | 7,0 |
| 7 | Matematiksel ve nicel temellerin denetimi | 5,5 |
| 8 | Literatür hâkimiyeti ve kaynakça etiği | 7,0 |
| 9 | Ölçek bağımsızlığı (Ölçekler arası tutarlılık) testi | 6,0 |
| 10 | Fiziksel ontoloji ve nedensellik ilkesi | 8,0 |
| 11 | Öncüllerle yüzleşme (Tarihsel katil itirazlar denetimi) | 7,5 |
| 12 | Retrodiksiyon/prediksiyon sınıflandırması | 5,5 |
| 13 | Güncellik (Zaman damgası) denetimi | 4,5 |
| 14 | Çıkar ve kimlik beyanı | 8,5 |

### GENEL PUAN: **6,5 / 10**

### Revizyon Hükmü: **MAJÖR REVİZYON**
*(Gerekçe: Kriter 13 uyarınca 22 kriz kaleminin en az 5'inin güncel literatürde çözülmüş/eskimiş olması ve 1 kaynak-içerik uyuşmazlığı; Kriter 4 bağımsız tarama ölçütü gereği metnin hiç anmadığı dört temel karşı-gözlem sınıfı [Güneş-senkron uydular, Plüton-Charon/yavaş ikililer, kompakt cisimler, POD verileri]; Kriter 7 uyarınca 4.2.9.2 logaritmik basınç kuyusu integralindeki matematiksel tutarsızlık ve $3.4.1 \leftrightarrow 3.10.2$ basınç işareti zıtlığı.)*

---

## Kriter Kriter Bulgular, Analizler ve Somut Öneriler

### 1. İç Tutarlılık ve Terminology Disiplini — 7,0/10
* **Güçlü Yönler:** "Zerre-Katar-Paket", "kütle-itim", tırnaklı "foton" terminoloji rejimi kitap genelinde yüksek bir disiplinle korunmaktadır.
* **Kusurlar ve Çelişkiler:**
  1. *Ay'ın Uzaklaşma Mekanizması Çelişkisi:* Bölüm 3.9.4 yeni gradyan lobu mekanizmasıyla uydunun net kaderini açıklarken; Bölüm 3.9.1, 3.9.4-Sonuç ve 3.11 özeti Ay'ın 3,8 cm/yıl uzaklaşmasını hâlâ asıl olarak kozmolojik seyrelmeye bağlamaktadır. Baskın mekanizma tek zeminde karara bağlanmalıdır.
  2. *Aberasyon Çelişkisi:* Kısım 6 §1.3'teki "zarf sınırında kırılma" açıklaması, Bölüm 3.4.6'daki ana çözümlü metinle ("sapma zarf sınırında üretilemez; kavrama skalerdir") çelişmektedir.
  3. *Cam İçin Yoğunluk Kalıntıları:* 2.3.4 ve 2.6.2'deki "camın düşük yoğunluğu" dili, 2.4.2'deki birleştirici ilkeyle (yoğunluk sabittir, basınç düşer) geriye dönük henüz tam uzlaştırılmamıştır.
  4. *Terminolojik Hata:* "Girdabın senkron yarıçapı" adlandırması hatalıdır; doğrusu "gövde dönüşünün senkron yarıçapı"dır (çünkü teori girdabın kütleden kat kat hızlı döndüğünü savunmaktadır).

### 2. Tekil Mekanizma (Birleştirme) ve Tutumluluk — 6,5/10
* **Güçlü Yönler:** Ek C parametre envanteri (6 skaler + 2 profil) serbest parametre sayımını şeffaf bir dürüstlükle ilan etmektedir.
* **Kusurlar:**
  1. $\alpha$ parametresi Kısım 4 içinde üç farklı anlamla (Laplace sabiti $\leftrightarrow$ değişken arka plan basıncı $\leftrightarrow$ bağlaşım katsayısı) dolaşmaktadır.
  2. $\chi$ (kromatik sapma parametresi) türetilmemiş, fenomenolojik kalmıştır.
  3. Bell korelasyonlarını açıklamak için hem filtreleme hem topografya katmanının birlikte sürdürülmesi tutumluluk (Occam'ın Usturası) açısından lüks yaratmaktadır.

### 3. Hasım Pozisyonun Doğru Aktarımı (Saman Adam Denetimi) — 5,0/10
* **Kusurlar (Standart Fiziğin Yanlış/Eskimiş Aktarımı):**
  1. *Torksuz Devinim (1.4.10):* "Klasik mekanikte yalıtılmış cismin eksen devinimi imkânsızdır" iddiası yanlıştır. Klasik Euler/Poinsot elektroniği ve Chandler yalpalaması torksuz devinimi öngörür.
  2. *Kuantum Tarifler (1.2.8 & Kisim 2):* Kuantum mekaniğinin "bilinçli gözlemci çökertir", "mekanizmasız ışınlanma" şeklinde tarif edilmesi saman adam eleştirisidir.
  3. *Ekvator-Kutup Gravimetrisi (4.2.7):* Somigliana ve Clairaut formülleri 9,780 - 9,832 m/s² değerlerini standart jenerik jeodezide zaten tam olarak türetmektedir; "anomali" olarak sunulması hatalıdır.
  4. *Parçalanma Paradoksu (4.2.7.2):* Klasik mekanikte böyle bir paradoks yoktur ($\omega^2 R \ll g$ olduğu için Maclaurin elipsoidleri parçalanmaz).
  5. *Çay Yaprağı Paradoksu (3.5.3):* Ağır parçacıkların merkeze toplanması merkezcil basınç gradyanıyla değil, taban sınır tabakasındaki Ekman ikincil akışıyla açıklanır.

### 4. Öz-Eleştiri, Dürüst Kayıt ve Bağımsız Tarama — 7,5/10
* **Güçlü Yönler:** 7.4 sınırlılıklar tablosu, Ek C, `00_CALISMA` iç denetim kayıtları ve flyby anomalisinin kanıttan üst sınıra düşürülmesi örnek bir dürüstlüktür.
* **Bağımsız Karşı-Gözlem Taraması (Majör Revizyon Gerekçesi):** Metnin hiç anmadığı dört temel karşı-gözlem sınıfı tespit edilmiştir:
  1. *Güneş-Senkron Uydular (SSO):* ~98° eğiklikle yörüngede kararlı uçan yüzlerce yapay uydu, 3.6.1'deki rejim kuralının en yakın sınavıdır; metinde anılmamıştır.
  2. *Plüton-Charon & Yavaş İkili Asteroitler:* 6,39 günlük kilitli dönüşe sahip Plüton'un 5 uydu tutması, "yavaş dönüş $\rightarrow$ uydu tutamaz" Altın Kuralının (3.4.3) karşı örneğidir.
  3. *Kompakt Cisimler:* Benzer kütleli beyaz cüce ile nötron yıldızının dönüş periyotları 5-6 mertebe farklıdır; tek değerli kütle-dönüş ilişkisi (3.4.4) burada kırılmaktadır.
  4. *Hassas Yörünge Belirleme (POD):* Kutup yörüngeli binlerce uydunun rutin POD verilerinde modellenmemiş girdap artığı bulunmamaktadır (`6.3.1` ile çelişki).

### 5. Yeniden Türetimin Değerlendirilmesi ve Varsayım Bilançosu — 6,0/10
* **Güçlü Yönler:** Doppler cebri (`6.1.2`) ve Fizeau katsayısı ($f=1-1/n^2$) türetimi külliyatın en temiz adımlarıdır.
* **Kusurlar:** $1/\gamma$ ezilmesi (6.1.2) türetilmemiş, beyan edilmiştir (Lorentz esir çerçevesi eşdeğerliği); tam sürüklenme varsayımı (`3.4.6`) borçludur; $\rho(r)$ fiti (`6.2.8`) kalibrasyondur.

### 6. Yanlışlanabilirlik Öngörülerinin Denetimi ve Ölüm Koşulları — 7,0/10
* **Güçlü Yönler:** 7.5 tablosunda yer alan 318 $\mu$as kromatik merceklenme, yıldız günü kontrolü, $e \approx 0,2$ rejim sınırları katı yanlışlanabilir öngörülerdir.
* **Kusurlar:** Bell Katman-2 programı yapısal olarak üstten sınırsızdır (sıfır sonuç daima massedilebilir); 22 kriz çözümünün nitel kalması aşırı esneklik eleştirisini davet etmektedir.

### 7. Matematiksel ve Nicel Temellerin Denetimi — 5,5/10
* **Matematik Hataları ve Döngüsellikler:**
  1. *4.2.9.2 İntegral Tutarsızlığı:* Metinde $\rho \propto 1/r^2$ ilan edilip integralde $\rho$ sabit alınmıştır! Tutarlı hesapta $\mathrm{d}P/\mathrm{d}r \propto 1/r^3$ çıkar ve logaritmik basınç kuyusu (düz galaktik rotasyon eğrisi) elde edilemez.
  2. *Döngüsel $G$ Parametrizasyonu:* $G = \alpha / \rho_n$ bağıntısında $\alpha$ bağımsız ölçülemediğinden, bu bir türetim değil yeniden parametrizasyondur.
  3. *Basınç İşareti Çelişkisi:* $3.4.1$ ($\mathrm{d}P/\mathrm{d}r = +\rho v^2/r$) ile $3.10.2$ ($(1/\rho)\mathrm{d}P/\mathrm{d}r = -GM/r^2$) zıt işaretlidir.
  4. *Zerre Hacmi Aritmetiği:* 2.2.2'de $5,25 \times 10^{-53}\ \mathrm{m}^3$ yerine $5,44 \times 10^{-53}\ \mathrm{m}^3$ yazılmıştır.

### 8. Literatür Hâkimiyeti ve Kaynakça Etiği — 7,0/10
* **Güçlü Yönler:** 250+ kaynak girdisi şeffaf ve gerçektir; uydurma kaynak yoktur.
* **Kusurlar:**
  1. *7.7.3 Kaynak-İçerik Uyuşmazlığı:* Tiesinga 2021 (CODATA 2018) küçük proton yarıçapını önermesine rağmen, metinde büyük yarıçapın kaynağı olarak gösterilmiştir.
  2. Kisim 2'de Einstein 1905 fotoelektrik ve Fizeau 1851 atıfları öksüz/eksiktir.

### 9. Ölçek Bağımsızlığı (Ölçekler Arası Tutarlılık) Testi — 6,0/10
* **Güçlü Yönler:** Zerre ve kütle-itim ilkelerinin elektron ile galaksi arasında tek omurgada çalıştırılması vizyonu değerlidir.
* **Kusurlar:** Rejim sınırlarının duruma göre esnetilmesi: Zarf M&M için eşzamanlı sürüklenirken, atmosferik siklonlar için diferansiyel sürüklenir; camda "patinaj", ortamda "yerel $c$" rejiminin nicel eşiği eksiktir.

### 10. Fiziksel Ontoloji ve Nedensellik İlkesi — 8,0/10
* **Güçlü Yönler:** Eserin en güçlü kasıdır. Matematiksel soyutlamalar yerine Zerre sürtünmesi, vakum cebi ve basınç gradyanı üzerinden nedensel zincir kurulmuştur. Mascon/gelgit sentezi (`3.9.5`) oldukça başarılıdır.
* **Kusurlar:** Paketin kırıcıdaki "kolektif kararı" (`2.6.5`) ve W-torku $\rightarrow$ makro devinim bağı (`1.4.7`) henüz nitel havaledir.

### 11. Öncüllerle Yüzleşme (Tarihsel Katil İtirazlar Denetimi) — 7,5/10
* **Beş Katil İtirazın Denetim Durumu:**
  1. *Le Sage Sürükleme ve İsınma:* Sürükleme işlenmiş, ancak **ısınma problemi** tek parantezle geçiştirilmiştir.
  2. *Yıldız Sapması (Bradley 1729) & Airy Su Teleskobu:* 3.4.6'da ele alınmıştır.
  3. *Fizeau Kısmi Sürüklenme:* 3.4.6.3'te türetilmiştir.
  4. *Michelson-Morley Null Sonucu:* Zarf sürüklenmesiyle ele alınmıştır.
  5. *Lorentz Esir Eşdeğerliği:* 6.1.3'te dürüstçe kabul edilmiştir.
* **Eksik:** Kelvin vorteks atomu ayrışmasının ana metinde bulunmaması.

### 12. Retrodiksiyon/Prediksiyon Sınıflandırması — 5,5/10
* **Kusurlar:** Gerçek Sınıf-(iii) öngörüsü (önceden söylenmiş yeni gözlem) sayısı kısıtlıdır (~7 kalem). Serbest parametreli geriye dönük uyum (Sınıf-i) veya yeniden türetimler (Sınıf-ii) için metinde **"Kesin İspat"**, **"Matematiksel İspat"** (`4.3.4`, `4.3.5`) başlıklarının kullanılması statü enflasyonudur.

### 13. Güncellik (Zaman Damgası) Denetimi — 4,5/10
* **Majör Kusur (Eskimiş/Çözülmüş Krizler):** Kitapta "açık kriz" olarak sunulan 22 kalemden en az 5'i güncel literatürde çözülmüş veya kapanmıştır:
  1. *Proton Yarıçapı (`7.7.3`):* CODATA 2018 ile küçük yarıçap ($0,8414\ \mathrm{fm}$) kabul edilmiş ve kriz kapanmıştır.
  2. *Müon g-2 Sapması (`7.7.4`):* 2025 Fermilab ve kafes-QCD hesaplarıyla $5,1\sigma$ fark kapanmıştır.
  3. *S8 Gerilimi (`7.7.8`):* KiDS-Legacy 2025 verileriyle çözülmüştür.
  4. *Karanlık Akış (`7.7.11`):* Planck 2013 verileriyle kesin biçimde doğrulanmadığı gösterilmiştir.
  5. *FRB Enerjisi (`7.7.18`):* Enerji ölçeğinde ~6-8 mertebe abartı yapılmış ve magnetar bağlantısı 2020'de kurulmuştur.

### 14. Çıkar ve Kimlik Beyanı — 8,5/10
* Raporun başındaki ve `Kisim_9`'daki beyanlar arşiv ve şeffaflık standardına tam uygundur.

---

## Zorunlu Revizyon Listesi

### Majör Revizyon Kalemleri (Zorunlu):
1. **4.2.9.2 İntegral Tutarsızlığının Düzeltilmesi:** $\rho \propto 1/r^2$ profili altında integrasyon adımı yeniden türetilmeli veya $\rho$ tanımı netleştirilmelidir.
2. **Eskimiş Krizlerin Güncellenmesi/Geri Çekilmesi:** Proton yarıçapı, müon g-2, S8 gerilimi, karanlık akış ve FRB kalemleri `7.7`'de Karşı Kayıt ilkesiyle güncellenmeli veya geri çekilmelidir.
3. **7.7.3 Kaynak-İçerik Uyuşmazlığı:** Tiesinga 2021 kaynağının doğru bağlama oturtulması.
4. **Bağımsız Karşı-Gözlem Kayıtları:** Güneş-senkron uydular, Plüton-Charon ikilisi, kompakt cisimler ve POD verileri `7.4` sınırlılıklar tablosuna işlenmeli veya cevaplanmalıdır.
5. **Basınç İşareti ve Devinim Hizalaması:** 3.4.1 $\leftrightarrow$ 3.10.2 basınç işaretleri ile 1.4.10 torksuz devinim aktarımı düzeltilmelidir.

### Minör Revizyon Kalemleri:
6. "Kesin İspat" ve "Matematiksel İspat" başlıklarının Sınıf-(ii) retrodiksiyon taksonomisiyle hizalanması.
7. Ay'ın uzaklaşma mekanizmasında lob ve seyrelme ağırlıklarının tek zemine oturtulması.
8. Zerre hacmi aritmetiğinin ($5,25 \times 10^{-53}\ \mathrm{m}^3$) ve L_spin formülünün düzeltilmesi.

---

## Hüküm ve Sonuç

Evrenakı Teorisi'nin Akademik Sürümü, `99_Hakemlik_Standarti.md` tüzüğünün sertleştirilmiş 14 kriterli sınavından **6,5/10 puan ve MAJÖR REVİZYON** kararıyla çıkmaktadır. Metnin dürüst kayıt kültürü, epistemolojik cesareti, Fizeau türetimi gibi nicel başarıları ve Popperci yanlışlanabilirlik stantları son derece takdire şayandır. Ancak taşıyıcı matematiksel integrallerdeki hataların (4.2.9.2), standart fiziğin yanlış aktarımlarının (1.4.10, 4.2.7), eskimiş krizlerin (7.7 g-2, proton yarıçapı) ve görmezden gelinen karşı-gözlem sınıflarının giderilmesi, eserin bilimsel kredibilitesini zirveye taşıyacak kaçınılmaz birer ödevdir.

**Antigravity AI** (Google DeepMind — Advanced Agentic Coding)  
*28 Temmuz 2026 — 14 Kriterli Hakemlik Standardı Değerlendirmesi*
