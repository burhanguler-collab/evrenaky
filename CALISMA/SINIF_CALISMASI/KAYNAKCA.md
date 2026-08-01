# SINIF_CALISMASI Kaynakça ve Veri Referansları

Bu belgede, Evrenakı teorisinin `SINIF_CALISMASI` testlerinde kullanılan verilerin ve karşılaştırmalı modellerin dayandığı bilimsel makalelerin listesi yer almaktadır. Çalışmadaki tüm dönüş eğrisi verileri, gözlemsel noktalar ve baryonik kütle hesaplamaları tamamen yayımlanmış, hakemli bilimsel literatürden (başlıca SPARC veritabanından) değiştirilmeden alınmıştır.

## 1. Temel Veritabanı ve Dönüş Eğrileri (SPARC)
Çalışmadaki 175 disk galaksisinin ham dönüş eğrileri (rotmod.dat), yüzey parlaklıkları ve $\Upsilon_*$ varsayımları bu temel makaleye dayanır. Tüm sınıflandırma testlerinde bu veri seti kullanılmıştır.
* **Lelli, F., McGaugh, S. S., & Schombert, J. M.** (2016). *SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves.* The Astronomical Journal (AJ), 152(6), 157. [DOI: 10.3847/0004-6256/152/6/157]

## 2. Radyal İvme Bağıntısı (RAR) ve Erken Tip Galaksiler (ETG)
`95_RAR` (2693 ivme noktası) ve `96_ETG` (16 Erken Tip Galaksi ivme halkası) testlerinde, Standart Bilim ile Evrenakı'nın "evrensellik" kıyaslamasında kullanılan veri setleri ve uyum (fit) fonksiyonları bu yayından alınmıştır.
* **Lelli, F., McGaugh, S. S., Schombert, J. M., & Pawlowski, M. S.** (2017). *One Law to Rule Them All: The Radial Acceleration Relation of Galaxies.* The Astrophysical Journal (ApJ), 836(2), 152. [DOI: 10.3847/1538-4357/836/2/152]

## 3. Baryonik Tully-Fisher İlişkisi (BTFR)
`97_BTFR` testinde, Evrenakı'nın eğim (şekil) öngörüsünü test etmek için kullanılan "farklı hız tanımlarına sahip" (V_flat, V_out vb.) 153 galaksilik özel BTFR veri seti bu çalışmaya dayanır (`BTFR_Lelli2019.mrt`).
* **Lelli, F., McGaugh, S. S., Schombert, J. M., Desmond, H., & Katz, H.** (2019). *The baryonic Tully-Fisher relation for different velocity definitions and implications for galaxy formation models.* Monthly Notices of the Royal Astronomical Society (MNRAS), 484(3), 3267-3278. [DOI: 10.1093/mnras/stz205]

## 4. Karanlık Madde Halo Modelleri (ΛCDM Kıyaslamaları İçin)
Standart Bilim'in (ΛCDM Modeli) yarıçap geri çözümleri ve teorik varsayımları (Abundance Matching, NFW yoğunluk profilleri vb.) için SPARC verilerine uygulanan karanlık madde halo kalibrasyonları bu çalışmadan (`WP50_M200.mrt`) alınarak Evrenakı ile çapraz incelemeye sokulmuştur.
* **Li, P., Lelli, F., McGaugh, S. S., Pawlowski, M. S., Zwaan, M. A., & Schombert, J. M.** (2020). *A Comprehensive Catalog of Dark Matter Halo Models for SPARC Galaxies.* The Astrophysical Journal Supplement Series (ApJS), 247(1), 31. [DOI: 10.3847/1538-4365/ab700e]

## 5. Yüksek Kırmızıya Kayma (High-z) Disk Galaksileri
Erken evrende (baryon ağırlıklı ve düşen dönüş eğrisine sahip) gözlemlenen yüksek kırmızıya kayma oranlı disk galaksilerinin analizleri için referans alınan makaleler:
* **Genzel, R., et al.** (2017). *Strongly baryon-dominated disk galaxies at the peak of galaxy formation epoch.* Nature, 543(7645), 397-401. [arXiv:1703.04310]
* **Lang, P., et al.** (2017). *Falling Outer Rotation Curves of Star-forming Galaxies at 0.6 ≲ z ≲ 2.6 Probed with KMOS3D and SINS/zC-SINF.* The Astrophysical Journal, 840(2), 92. [arXiv:1703.05491]

## 6. Gaz Dinamikleri, Karanlık Madde ve Ek Çalışmalar
* **Ianjamasimanana, R., et al.** (2012). [arXiv:1207.5041]
* **Stilp, A. M., et al.** (2013).
* **Ianjamasimanana, R., et al.** (2015).
* **Oh, S.-H., et al.** (2015).
* **Mogotsi, K. M., et al.** (2016).
* **Iorio, G., et al.** (2017). [arXiv:1611.03865]

---
**Veri Kullanım Etiği:** Evrenakı teorisi, kendi sonuçlarını iyileştirmek adına yukarıdaki yayımlanmış verilerin hiçbirine fit işlemi (eğri uydurma) veya veri seçimi (cherry-picking) uygulamamıştır. Yalnızca veri setlerinin kendi içindeki kalite bayrakları (örneğin SPARC'ın kendi belirlediği Q=3 düşük kalite bayrakları veya $i < 30^\circ$ eğiklik sınırları) filtrelenerek adil bir test ortamı kurulmuştur.
