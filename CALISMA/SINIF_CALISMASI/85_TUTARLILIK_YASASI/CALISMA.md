# 85_TUTARLILIK_YASASI — Sınıf bandının mekanizma taraması · Çalışma dosyası

**148 galaksi · 8 grup (6 sınıf + S0 + BCD) · fit yok · nihai kurulum**

Hesap: `../../tutarlilik_yasasi.py` · Çıktılar: [`SONUC.csv`](SONUC.csv) · [`tutarlilik.png`](tutarlilik.png)
Ön adımlar: [86_NIHAI](../86_NIHAI/CALISMA.md) (sınıf bandı), [88_TARAMA](../88_TARAMA/CALISMA.md) (galaksi-düzeyi null), [89_KAFES/AYIRMA](../89_KAFES/AYIRMA.md) (kanal ayrıştırma yöntemi), [93_G_YEREL](../93_G_YEREL/CALISMA.md)

---

## 0. Soru (yazarın sorusu)

*"Evrenakı fitsiz, şeklen ölçüme çok benziyor ama bazen altta bazen üstte seyrediyor. Galaksilerde bazı değişkenler formüle az veya çok yansıyor. Sebebini bulabilir miyiz — böylece teori hiçbir fit değerine ihtiyaç duymaz?"*

Plan (onaylı): **(1)** hedef = galaksi başına gereken $a_0$ çarpanı $k_i$ (dış yarı, sayısal çözüm); **(2)** SPARC katalog + eğri biçiminden 10 aday değişken, **sınıf medyanları düzeyinde** tarama (galaksi düzeyi gürültü-baskın — [GURULTU](../88_TARAMA/GURULTU.md)); **(3)** iki kanal ayrımı: hizalanma (yalnız F4) vs ortam/$\mathcal{G}$ (bütün $v^2$); **(4)** en iyi adayla yasa denemesi; kapanış ölçütü: sınıf bandının ölçüm bütçesi düzeyine inmesi.

## 1. Hedefler — iki dilde

| Grup | $k$ (F4 dili) | $u$ ($v^2$ dili) | n |
|---|---|---|---|
| Sa–Sab | 1,20 | 1,06 | 12 |
| Sb–Sbc | 0,90 | 0,97 | 29 |
| Sc–Scd | 1,10 | 1,04 | 30 |
| Sd | 1,55 | 1,19 | 16 |
| Sdm–Sm | 1,00 | 1,01 | 28 |
| Im | 0,65 | 0,86 | 26 |
| S0 | 3,03 | 1,43 | 3 |
| BCD | 2,50 | 1,38 | 4 |
| **Band (8 grup)** | **0,667 dex** (std 0,211) | **0,221 dex** (std 0,071) | |

$k$: dış yarı sapmasını sıfırlayan $a_0$ çarpanı (yalnız F4'ü ölçekler, ikiye bölmeyle çözüldü). $u$: dış yarıda medyan $(v_{gözl}/v_{öng})^2$ (bütün $v^2$'yi ölçekler).

> ### Birinci bulgu — bandın "büyüklüğü" seçilen dile bağlı, ve doğru dil onu küçültüyor
>
> Aynı sapma F4-çarpanı dilinde **0,667 dex** görünürken, toplam-normalizasyon dilinde **0,221 dex**'e iniyor (hız cinsinden: altı ana sınıf $\pm\%7$ içinde; uçlar S0/BCD $+\%17$–20). Sebep cebirsel: F4'ün payı küçükken aynı hız açığını yalnız F4'le kapatmak devasa çarpan ister. **"Bazen altta bazen üstte" görüntüsünün doğru ölçüsü, sınıf başına $\pm\%7$'lik (uçlarda %20) bir toplam ölçek oynamasıdır** — dramatik bir F4 tutarsızlığı değil.

## 2. Kanal ayrımı — sapma hangi terime ait?

Ayırt edici: dış yarıya oturtulan **tek sayı** ($k_i$ ya da $u_i$), eğrinin iç/orta kısmını hangi kanalda daha iyi düzeltir? (İkisi de dış yarıda eşitlenir; fark iç/orta bölgeden gelir.)

| Grup | taban RMS | F4 kanalı ($k_i$) | $\mathcal{G}$ kanalı ($u_i$) | kazanan |
|---|---|---|---|---|
| Sa–Sab | 25,6 | **24,3** | 26,2 | F4 |
| Sb–Sbc | 27,4 | 16,3 | **13,8** | $\mathcal{G}$ |
| Sc–Scd | 16,7 | 10,0 | **9,6** | $\mathcal{G}$ |
| Sd | 10,2 | **7,2** | 7,3 | F4 (kılpayı) |
| Sdm–Sm | 9,9 | 7,2 | **6,3** | $\mathcal{G}$ |
| Im | 8,1 | 3,5 | **3,4** | $\mathcal{G}$ (kılpayı) |
| S0 | 27,9 | 19,5 | **15,9** | $\mathcal{G}$ |
| BCD | 19,1 | **5,3** | 5,4 | F4 (kılpayı) |

Galaksi bazında: F4 kanalı 65/148, $\mathcal{G}$ kanalı 83/148.

> ### İkinci bulgu — işaret ortam/$\mathcal{G}$ kanalından yana
>
> Beş grupta (ve galaksilerin %56'sında) sapma, **bütün $v^2$'yi ölçekleyen** bir düzeltmeyle daha iyi kapanıyor. Bu, [AYIRMA](../89_KAFES/AYIRMA.md)'nın bağımsız sonucuyla (fiziksel sınırına hiç dayanmayan tek kanal $\mathcal{G}$ idi) ve [93_G_YEREL](../93_G_YEREL/CALISMA.md)'in işaret ölçümüyle **aynı yöndedir.** Fark küçük ve kesin değil (üç grupta kılpayı) — bir eğilim, bir kanıt değil.

## 3. Değişken taraması — tek değişkenli yasa YOK

Sınıf düzeyi (8 nokta; $n=8$'de ~anlamlılık eşiği $|\rho|\gtrsim0{,}74$):

| Aday | $\rho$ (log $k$) | Aday | $\rho$ |
|---|---|---|---|
| iç yükselme dikliği | **−0,52** | eğri biçimi $V_{iç}/V_{dış}$ | **+0,52** |
| etkin yüzey parlaklığı | +0,45 | etkin kütle yoğunluğu | +0,45 |
| gaz kesri | −0,45 | eğri çalkantısı | −0,45 |
| $R_{HI}/R_{disk}$ | +0,29 | log $V_{flat}$ | +0,26 |
| merkezî disk SB | +0,17 | log $M_{bar}$ | **+0,05** |

**Hiçbir aday eşiğe yaklaşmıyor** (hedef $u$ alınınca sıralama aynı — $u$ ile $k$ sınıf sıralamasını korur). Galaksi düzeyinde de en iyisi $|\rho|=0{,}23$ (çalkantı) — 88_TARAMA'nın null'uyla tutarlı.

**Yasa denemesi** (en iyi aday, diklik): $\log k=0{,}28-0{,}65\,x$ uygulanınca band **daralmıyor** (0,667 → 0,693 dex). İki değişkenli deneme (diklik+biçim) sınıf-medyan artığını 0,21'den 0,16'ya indiriyor — 8 noktaya 3 parametre; anlam taşımaz ve **yasa ilan edilemez.**

## 4. Hüküm

1. **Katalogdan okunabilen tek değişkenli gözlemsel yasa yoktur.** Sınıf bandı; kütle, yoğunluk, gaz kesri, hız, eğri biçimi gibi tek eksenlerin hiçbirini izlemiyor. (Sd ile Im zıtlığı zaten bunu ima ediyordu.)
2. **Ama sorunun boyutu ve adresi netleşti:** doğru dilde (toplam normalizasyon) band $\pm\%7$'dir (uçlarda %20) ve kanal ayrımı ortam/$\mathcal{G}$ tarafını işaret eder. Yani aranan şey F4'e eklenecek bir hizalanma çarpanı değil, **$\mathcal{G}=\alpha/\rho_n$'nin (dolayısıyla $a_0$'ın) ortama bağlı küçük değişkenliğidir** — teorinin zaten iddia ettiği, ama nicel biçimi ($\rho_n$ neye bağlı?) henüz türetilmemiş olan kanun.
3. **Fitsizliğin kapanış yolu gözlemsel değil, teorik:** SPARC değişkenleri arasında mekanizmanın vekili yok; kapanış, $\rho_n$(ortam) bağıntısının teoriden türetilmesini ve/veya SPARC dışı bir dinamik-soğukluk ölçüsünü ($v/\sigma$) bekliyor.

## 5. Dürüstlük kayıtları

1. **8 noktalı taramanın gücü düşüktür** — $|\rho|<0{,}74$ olan gerçek bir ilişki görünmez. "Yasa yok" hükmü, "bu adaylarda ve bu çözünürlükte yok" demektir.
2. **S0 $n=3$, BCD $n=4$** (NGC6789 $N=4$ nokta ile veri eşiğinin altında kaldı; PGC51017 ters işaretli olduğundan çözüm tabana kırpıldı ve medyanı aşağı çeker). Uç grupların $k$ değerleri [07_S0_BCD](../07_S0_BCD/CALISMA.md)'nin farklı tanımlı çarpanlarıyla bire bir karşılaştırılamaz.
3. **Kanal sınavında iki kanal da dış yarıya oturtulmuş tek sayı kullanır** — adil; ama üç grupta fark kılpayıdır ve galaksi-düzeyi oy 83/148, %56'dır. Eğilim, kanıt değildir.
4. **$u$ dili ile $k$ dili aynı sıralamayı verir** (monoton dönüşüm); taramanın null'u dil seçiminden bağımsızdır.
5. **Aday listesi katalogla sınırlıdır.** Dinamik soğukluk ($v/\sigma$), bar/warp varlığı, çevre yoğunluğu SPARC'ta yok — mekanizmanın gerçek vekili bunlardan biri olabilir ve **taranamadı.**
6. Bütün hesaplar nihai kurulumla ($a_0=1{,}75\times cH_0/16{,}1$, yerel $\ell_\omega$, $\Upsilon_*=0{,}50$) yapıldı; fit yok.

## 6. Bundan çıkan iş

| # | İş | Neden / durum |
|---|---|---|
| ~~1~~ | ~~Teoriden ortam bağıntısını türet~~ → [NC_TURETIM.md](NC_TURETIM.md) + [LAMBDA_TURETIM.md](LAMBDA_TURETIM.md) | ✅ **yapıldı:** ortam-yoğunluğu yolu teorinin kendi M-44'üyle KAPANDI; doğru mekanizma tutarlılık istatistiği çıktı — kafes=çekirdek, pencere $[X,\langle A\rangle]$; $\sqrt{N}$ teoremleşti; kalan tek serbestlik $\lambda$ |
| ~~2~~ | ~~$v/\sigma$ verisi ekle, o eksende tara~~ → [SIGMA_SINAVI.md](SIGMA_SINAVI.md) | ✅ **yapıldı:** 18 galakside $+0{,}49$ ($p=0{,}019$) — öngörülen yönde **ilk anlamlı işaret**; doğrulama $n\gtrsim40$ kayıt-öncesi kip bekliyor |
| 3 | S0/BCD örneklemini büyüt (literatürden HI'lı mercek/tıkız cüce) | uçlar bandı domine ediyor ama $n=3$–4; G-8'in $\lambda<1$ çağrısının sınavı |
| 4 | Kanal sınavını iç-bölge artık **profiliyle** (tek RMS yerine yarıçap yarıçap) keskinleştir | md. 5.3 — kılpayı farkları ayrıştırabilir; Adım 7'nin "yalnız F4" öngörüsüyle gerilimi çözer |
| 5 | $\lambda$–incelik doğrulaması: $n\gtrsim40$, kayıt-öncesi kip → [KAYIT_ONCESI_PROTOKOL.md](KAYIT_ONCESI_PROTOKOL.md) | ⏳ **ilk deneme kapıda durdu:** W-farkı kestiricisi geçerlilik kapısını geçemedi ($-0{,}50$), sınav "uygulanamaz" ilan edildi; 99 galaksilik boru hattı hazır, geçerli σ/kalınlık kataloğu bekliyor |
