# σ SINAVI — λ'nın kaskad okuması dış veriyle: **ilk anlamlı işaret (+0,49, p=0,02)**

**18 galaksi · üç dış kaynak, I12 ölçeğine uyumlanmış · fit yok**

Hesap: `../../vsigma_sinavi.py` · Çıktılar: [`VSIGMA.csv`](VSIGMA.csv) · [`vsigma.png`](vsigma.png)
Öngörü: [LAMBDA_TURETIM.md](LAMBDA_TURETIM.md) — $k$ (dolayısıyla $\lambda$), diskin dinamik soğukluğu $v/\sigma$ ile **artmalı.**

## Veri (elle aktarılan, kaynaklı; uydurma yok)

| Kaynak | Ne | Galaksi | Uyumlama |
|---|---|---|---|
| Ianjamasimanana ve ark. 2012 (AJ 144, 96; Tablo 1) | THINGS süper-profil $\sigma_{dar}$ | 15 | birincil ölçek |
| Stilp ve ark. 2013 (ApJ 765, 136; Tablo 4) | süper-profil $\sigma_{merkez}$ | 2 (NGC1705, UGC04483) | ×0,81 (ortak galaksilerin medyan oranı) |
| Iorio ve ark. 2017 (MNRAS 466, 4159; Tablo 2) | LITTLE THINGS medyan $\sigma$ | 2 (DDO168, UGC07559) | ×0,67 (aynı yöntem) |

İlk turun 13 galaksisine 6 eklendi (UGC04305'in $k$'sı çözülemedi — F4 sıfırken bile aşım; 99-tipi veri): **iki uç artık temsilli** — çalkantılı/seyrek uçta UGC04483, UGC07559, NGC2366; BCD ucunda NGC1705. 99_KARMASIK üyeleri (3) denetim bayrağıyla dahil.

## Sonuç

| Kip | Spearman | tek yönlü perm. $p$ | n |
|---|---|---|---|
| **Tüm örneklem** | **+0,49** | **0,019** | 18 |
| Temiz (99 hariç) | +0,44 | 0,050 | 15 |
| Yalnız I12 (tek kaynak) | +0,39 | 0,086 | 14 |
| Sınıf-medyanı | +0,54 | — | 6 grup |

**İşaret öngörülen yönde ve ilk kez anlamlılık eşiğinde.** Sinyalin kaldıracı tam öngörünün dediği yerden geliyor: en düşük $v/\sigma$'lı üç sistem (3,5–6,4) en küçük çarpanları taşıyor ($k=0{,}27$–$0{,}44$) — çalkantılı ortam mikro dolanımı söndürüyor; dinamik-soğuk disklere doğru $k$ yükseliyor.

## Dürüstlük kayıtları

1. **Bu, ardışık ikinci analizdir** (ilk tur $n=13$'te $+0{,}11$ vermişti; örneklem büyüyünce $+0{,}49$'a çıktı). Ardışık bakmanın kendisi bir başka-yere-bakma katmanıdır; $p=0{,}019$ bu yüzden nominal değerinden zayıf okunmalıdır. **"Doğrulandı" denemez; "ilk anlamlı işaret" denir.**
2. Kaldıracı taşıyan üç düşük-uç galaksiden ikisi uyumlanmış kaynaklardandır (S13u/Io17u); uyumlama çarpanları (%20–30) log ölçekte küçüktür ama sıfır değildir. Tek-kaynak kip (+0,39, $p=0{,}086$) eşiğin hemen altındadır.
3. NGC1705 (BCD) $k=4{,}45$ ile **pencerenin hâlâ üstündedir** — v/σ eğilimine kabaca uysa da $[X,\langle A\rangle]$ ihlali sürüyor; uçlar sorusu bu sınavla kapanmadı.
4. $v$ olarak eğrinin dış-yarı medyan hızı kullanıldı (ilk turda katalog $V_{flat}$); iki tanım sıralamayı pratikte değiştirmez ama bir seçimdir.
5. $n=18$, hedeflenen $\gtrsim40$'ın altındadır: erişilebilir yayınlanmış galaksi-başına $\sigma$ tabloları (THINGS + VLA-ANGST + LITTLE THINGS) SPARC ile bu kadar kesişiyor. 40'a çıkmak yeni yayın taraması (HALOGAS/MHONGOOSE tekil çalışmaları, kenardan-görünüm kalınlık katalogları) ister.

## Hüküm ve sıradaki iş

G-8'in $\lambda$–incelik ayağı **"sınanmamış"tan "ilk anlamlı işaret"e** ilerledi: yön doğru, büyüklük eşikte, iki bağımsız kip (temiz, sınıf-medyanı) aynı yönde. Kayıt-öncesi doğrulama için: (1) örneklemi bağımsız kaynaklarla $n\gtrsim40$'a çıkar ve **bu kez tek, önceden ilan edilmiş kiple** koş; (2) kenardan-görünüm kalınlık ölçüsüyle paralel sınav; (3) NGC1705/BCD ucunu temiz veriyle çöz.
