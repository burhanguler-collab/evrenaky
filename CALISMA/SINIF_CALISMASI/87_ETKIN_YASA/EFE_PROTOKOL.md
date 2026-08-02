# EFE kayıt-öncesi protokolü — dış ortam akısının F4'e etkisi (iş 2)

**Statü: PROTOKOL — veri henüz açılmadı.** Bu dosya, dış alan etkisi (EFE) sınavının bütün
kararlarını *veriye bakmadan önce* sabitler (85'teki `KAYIT_ONCESI_PROTOKOL.md` kipinde). Sonuç
bölümü boştur ve veri edinilip kapılar geçilene kadar boş kalacaktır.

---

## 1. Hipotez ve mekanizma (önceden ilan)

**Teorinin mekanizması:** F4'ün $\sqrt{N}$ toplanması, taşıyıcı yapının kaskad koherensine bağlıdır
($\lambda$ kanalı; ince/soğuk yapı korur, çalkantı söndürür — `85_TUTARLILIK_YASASI`). Komşu
yapılardan gelen **dış ortam akısı** bu koherense dışarıdan eklenen bir bozucudur: güçlü dış alan
→ kaskad bozulur → $\lambda$ düşer → etkin F4 düşer → galaksinin **gereken çarpanı $k$ düşer.**

**H1 (yön, önceden kilitli):** $k$ ile dış alan şiddeti $e_N$ arasında **negatif** ilişki:
$\rho_s[k, e_N] < 0$.

**MOND ile ayrıştırıcı ikincil imza (önceden ilan):** MOND'da EFE toplam dış ivmenin fonksiyonudur
ve iç çalkantıdan bağımsızdır. Teoride ise etki $\lambda$ kanalından geçer; dolayısıyla **iç
çalkantı ($v/\sigma$) kontrol edildiğinde** dış-alan sinyalinin bir kısmı $\lambda$'ya devredilmeli,
kısmi korelasyon ham korelasyondan **zayıflamalıdır.** MOND-tipi EFE'de kısmi korelasyon ham
değerini korur. Bu ikincil imza sınavın asıl ayrıştırıcısıdır; birincil yön iki çerçevede aynıdır.

## 2. Veri ve eşleştirme

- **$e_N$ (dış Newton alanı, galaksi başına):** Chae, Lelli, Desmond, McGaugh, Li & Schombert
  (2020), ApJ 904, 51 — büyük-ölçek yapı haritalarından türetilmiş çevre kestirimleri
  (yayının kendi kataloğu). **Edinim bekliyor** — dosya indirilmesi kullanıcı onayına bağlıdır.
- **$k$ (gereken $a_0$ çarpanı, galaksi başına):** mevcut boru hattı (`94_YEREL_LOMEGA` /
  `sinif_carpan_duzeltme.py` sayısal çözümü, nihai kurulum) — **yeniden hesaplanmaz**, kayıtlı
  değerler kullanılır.
- Eşleştirme SPARC galaksi adıyla birebir; el ile ad düzeltmesi yapılırsa tek tek gerekçelenir.

## 3. Geçerlilik kapıları (sınav koşulmadan denetlenir; geçilemezse sınav "uygulanamaz")

1. **Bağımsızlık:** $e_N$, dönüş eğrisinden veya $k$'dan türetilmiş olmamalı (Chae+2020'de çevre
   haritasından gelir — bekleneni ✓; yine de yayın metninden doğrulanacak).
2. **Örneklem:** eşleşen $n\geq40$; altında kalırsa sonuç ancak "işaret" statüsünde raporlanır
   ($\sigma$ sınavındaki kural).
3. **Dinamik aralık:** $e_N$'in örneklemdeki yayılımı en az bir mertebe olmalı; değilse kaldıraç
   yoktur, sınav uygulanamaz.

## 4. Kestirici ve karar kuralları (önceden kilitli)

- Birincil: Spearman $\rho_s[\log k, \log e_N]$, **tek yönlü** (H1: negatif), permütasyon $p$
  (10 000 permütasyon, tohum 42), $\alpha=0{,}05$.
- İkincil (ayrıştırıcı): kısmi Spearman $\rho_s[\log k, \log e_N \mid v/\sigma, \log M_{bar},$
  Hubble tipi$]$. Yorum kuralı: kısmi değer hamın yarısının altına inerse "λ-kanalı lehine",
  ham değerini korursa "MOND-tipi doğrudan EFE lehine" kaydedilir.
- Karar: $\rho_s<0$ ve $p<0{,}05$ → **A5 doğrulandı** (ortam kanalının dış-alan yüzü);
  $p\geq0{,}05$ → aleyhte kayıt (A5 açık kalır, yön yeniden türetilmeli);
  $\rho_s>0$ anlamlı → **çerçeve aleyhine güçlü kayıt** — gizlenmez, 7.4'e taşınır.
- Bu dosya yazıldıktan sonra kestirici/kapı değişikliği yapılamaz; zorunlu kalınırsa değişiklik
  sonuca bakılmadan, gerekçesiyle buraya eklenir (85'te olduğu gibi).

## 5. Bilinen karıştırıcılar (önceden kayıt)

- $e_N$ kütleyle ve yoğun çevreyle korelidir; S0/BCD uçları yoğun çevrede oturur — kısmi
  korelasyonun kontrol listesi bu yüzden ($v/\sigma$, $M_{bar}$, tip) üçlüsüdür.
- $k$'nın kendi ölçüm bütçesi (uzaklık %59 payla baskın) $e_N$'den bağımsızdır — gürültü sinyali
  ancak sıfıra çeker, sahte negatif üretmez (tek yönlü sınav bu yüzden meşrudur).

## 6. SONUÇ — **SINAV UYGULANAMAZ** (Kapı 3 geçilemedi)

**Veri edinildi:** Chae ve ark. (2020) Tablo 2'nin **erratum ile düzeltilmiş** hâli (Chae ve ark.
2021, ApJ 910, 81, DOI 10.3847/1538-4357/abebdc; IOP suppdata `apjabebdct1_ascii.txt`) →
[`veri_chae2021_tablo2.txt`](veri_chae2021_tablo2.txt). Orijinal 2020 tablosu **kullanılmadı** —
erratum, o tabloda $e_{\rm env}$ değerlerinin galaksilerle eşleşmesinin indeks hatalı olduğunu
kaydeder; düzeltilmemiş tabloyla koşulacak her sınav geçersiz olurdu. Hesap: `../../efe_sinavi.py`,
birleşik veri: [`SONUC_EFE.csv`](SONUC_EFE.csv).

**Kapı denetimleri:**

| Kapı | Ölçüm | Hüküm |
|---|---|---|
| 1 — bağımsızlık | $e_{\rm env}$, Desmond (2018) büyük-ölçek yapı hesabından; dönüş eğrisine ve $k$'ya bakmaz | GEÇTİ |
| 2 — örneklem | eşleşen $n=141$ (94'ün 141 galaksisinin tamamı) | GEÇTİ |
| 3 — dinamik aralık | $e_{\rm env}$ yayılımı **0,71 dex** ($\approx$5,1 kat); eşik $\geq1$ dex idi | **KALDI** |

**Hüküm:** Protokolün kendi cümlesi bağlayıcıdır: *"değilse kaldıraç yoktur, sınav uygulanamaz."*
SPARC galaksilerinin çevre alanları yarım mertebeden biraz geniş bir banda sıkışıktır (yayının
kendi ifadesi de "almost one order of magnitude"dır); önceden konulan 1-dex eşiği bu veriyle
sağlanmaz. **Birincil sınav hükümsüzdür ve bu veriyle kurtarılamaz** — eşiği şimdi gevşetmek,
protokolün yasakladığı şeyin ta kendisidir.

**Süreç ihlali kaydı (gizlenmez):** Betik, kapı denetimini ve kestiricileri **tek koşuda** bastı;
kapı hükmü okunmadan sayılar da ekrana geldi. 85'teki emsalde sonuç hiç görülmeden "uygulanamaz"
denebilmişti; burada denemedi — bu, protokolün "sonuca bakılmadan" ilkesinin süreç tarafında bir
ihlalidir ve düzeltilemez. Görülen sayılar şeffaflık gereği aşağıda durur, ama **hüküm değeri
sıfırdır** (kapı düşmüş + sonuç görülmüş): $\rho_s[\log k,\log e_{\rm env}]=-0{,}161$, tek yönlü
perm. $p=0{,}031$ ($n=141$); kısmi ($\log M_{bar}$, tip) $-0{,}162$; $v/\sigma$ altkümesi ($n=15$)
$+0{,}067$. Yön H1 ile uyumlu görünür — ve tam da bu yüzden kayıt tutulur: ileride "aslında
anlamlıydı" diye geri çağrılamasın. Bundan sonra bu veri kümesine yapılacak her bakış en fazla
**işaret** statüsü taşıyabilir, doğrulama asla.

**Bundan çıkan iş:** (i) A5'in meşru yolu, daha geniş çevre-aralıklı bir örneklem üzerine **yeni**
bir kayıt-öncesi protokoldür — aday veri: Chae ve ark. (2021, ApJ 921, 104 — Paper II) genişletilmiş
çevre kestirimleri ve/veya küme-içi diskler; eşik tasarımı bu deneyimden öğrenilen tek dersle
(aralık eşiği, kaynak yayının ölçülmüş yayılımına göre konur) veriye bakılmadan yazılır.
(ii) İkincil imza (kısmi korelasyon ayrıştırıcısı) tasarımı doğruydu ve yeni protokole taşınır.

Bu protokol Claude Fable 5 tarafından yazılmıştır (kayıt-öncesi kip; 85'in protokol şablonu).
SONUÇ bölümü, kapı denetiminin ardından aynı gün işlenmiştir; md. 1–5 değiştirilmemiştir.
