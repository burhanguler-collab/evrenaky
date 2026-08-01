# `websitesi\CALISMA` Klasörü Hata İnceleme Raporu

Bu rapor, `websitesi\CALISMA` dizinindeki dosyaların (Python betikleri ve Markdown belgeleri) incelenmesi sonucunda tespit edilen hataları ve potansiyel sorunları listeler. İnceleme amacına uygun olarak, kod kalitesi ve teorik/mantıksal hatalar üzerinde durulmuştur.

> [!WARNING]
> Python dosyalarında genel olarak hataları gizleyen (maskeleyen) pratikler kullanılmıştır. Bu durum, arka planda çalışan matematiksel hataların veya veri okuma problemlerinin fark edilmesini engelliyor olabilir.

## 1. Python Kodlarındaki Hatalar ve Kötü Pratikler (Bad Practices)

### A. Çıplak (Geniş Kapsamlı) `except Exception:` Kullanımı
Birçok Python dosyasında hata yakalama blokları spesifik hataları (ör. `ValueError`, `FileNotFoundError`) yakalamak yerine tüm hataları yutacak şekilde `except Exception:` olarak yazılmıştır.
- **Etkilenen Dosyalar (Örnekler):** `uret_tam_veri_tablosu.py`, `sinif_ongoru_vs_fit.py`, `plot_upsilon_bant_rejim.py`, `plot_upsilon_bant_galeri.py`, `plot_turetim_fit_defteri.py`, `plot_tip_dokumu.py` vb.
- **Neden Bir Hata?** Bu kullanım, koddaki mantıksal hataları (Syntax, Indentation dışında kalan NameError, TypeError gibi) ve hatta `KeyboardInterrupt` gibi sistem kesintilerini gizler. Hata mesajı ekrana basılmadığı için verideki veya mantıktaki asıl sorunun ne olduğu anlaşılamaz.
- **Çözüm Önerisi:** Hatalar `except Exception as e: print(e)` şeklinde loglanmalı veya sadece beklenilen hata türleri (`except FileNotFoundError:`) yakalanmalıdır.

### B. Uyarıların Kapatılması (`warnings.filterwarnings('ignore')`)
Neredeyse tüm çizim ve hesaplama betiklerinin başında global olarak uyarılar gizlenmiştir.
- **Neden Bir Hata?** Numpy ve Pandas gibi veri kütüphaneleri sıfıra bölme (divide by zero), geçersiz logaritma (log of negative number) gibi durumlarda programı çökertmek yerine **uyarı (Warning)** verir. Tüm uyarıların kapatılması, grafiklerde veya tablolardaki hesaplamaların (NaN/Inf üretmesi) sessizce geçiştirilmesine neden olur.
- **Çözüm Önerisi:** Kodun hata ayıklama (debug) sürecinde `warnings.filterwarnings('ignore')` satırı geçici olarak kapatılmalı ve hangi işlemlerin uyarı ürettiği incelenerek matematiksel hatalar düzeltilmelidir.

### C. Sözdizimi (Syntax) İncelemesi
- Klasördeki tüm Python dosyaları derleyici (`compileall`) aracılığıyla test edilmiş olup, **hiçbir dosyada sözdizimi (syntax) hatası veya girinti (indentation) hatası bulunmamıştır.** Kodlar dizimsel olarak çalışabilir durumdadır.

---

## 2. Markdown Metinlerinde Belirtilen Teorik ve Mantıksal Hatalar

Dizindeki Markdown (`.md`) dosyaları, bir teorinin (Evrenakı Teorisi) verilerle sınanması üzerine hazırlanmıştır. Metinlerde yazarın bizzat tespit edip kayda geçirdiği ciddi fiziksel/teorik hatalar mevcuttur:

### A. Kitap ve Sınav Farklılıklarındaki Hatalar (`09_Kitap_Sinav_Farklari.md`)
Bu dosyada, kitabın güncel halinde **yanlış olduğu bilindiği halde bırakılmış** hatalar listelenmektedir:
1. **F5 Potansiyeli Hatası:** F5'in potansiyelinin saf $P_2$ olduğu, hiçbir harmonikte ayrı imza bırakmayacağı belirtiliyor. Kitaptaki "profiller farklı görünüyor ⟹ multipol içeriği farklı" çıkarımının **geçersiz ve hatalı** olduğu açıkça vurgulanmış.
2. **Sıkışma Kanalı Hızı:** Bir ara turda "sıkışma kanalının hızı $c/\\sqrt k$" olarak düzeltilmiş ancak bunun **hatalı olduğu** ve "hız $c$'dir" diyen orijinal metnin doğru olduğu belirtilerek metin geri alınmış.

### B. Sınavların Başarısızlıkları ve Yanlışlanan Öngörüler (`07_Teorinin_Sinanmasi.md`)
1. **Sınav 4'ün Çökmesi ($k=1/2$ Hatası):** Teori, kütleçekim dalgasının ışıktan 38,2 milyon yıl **önce** gelmesini öngörmüş ancak gözlem (GW170817) dalganın 1,74 saniye **sonra** geldiğini göstermiştir. Metinde bu durum *$\sim10^{15}$ mertebesinde yanlış* olarak tanımlanmış ve teorik model için ölümcül bir hata (yanlışlanma) olarak kayda geçmiştir. Bu hata, uygulamanın değil **hâl denkleminin temel hatası** olarak saptanmıştır.
2. **Sınav 3'ün Başarısızlığı:** Düzlem dışı gaz gecikmesinde teorinin keskin bir basamak öngördüğü, ancak gözlemin rampa şeklinde olduğu belirtilmiştir. (Hız uyuşmazlığı: 76-82 km/s).
3. **M-44 Politrop Türetimi:** Politrop türetiminde integral alımının bir "kategori hatası" (hâl denklemi ile durum denklemi karışıklığı) olduğu saptanmış ve geçersiz bulunmuştur.

## Sonuç Özeti

`websitesi\CALISMA` dizini, Evrenakı isimli bir fizik teorisinin Python simülasyonları ve test verileriyle sınırlarının zorlandığı bir çalışma alanıdır. Yapılan hata taramasında:
1. **Yazılım hataları açısından:** Projedeki Python kodları syntax olarak hatasız olsa da, Exception ve Warning'lerin "yutulması (mute edilmesi)" kurgulandığından, olası veri uyuşmazlıkları ve işlem hataları tespit edilemeyecek şekilde gizlenmiştir.
2. **Bilimsel/Teorik hatalar açısından:** Teorinin kendi sınavları (Özellikle Sınav 3 ve 4) açıkça başarısız olmuş (failed/falsified), yazar bu "hata ve yanlışlanmaları" metinlerde samimiyetle listelemiştir. 

**Önerilen Aksiyon:** Öncelikle `.py` uzantılı betiklerdeki `except Exception:` kullanımlarının kaldırılıp, hesaplamalardaki gerçek çalışma zamanı hatalarının (runtime errors) su yüzüne çıkarılması gerekmektedir.
