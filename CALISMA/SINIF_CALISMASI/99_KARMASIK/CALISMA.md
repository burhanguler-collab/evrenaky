# 99_KARMAŞIK — Seçim Etkisi Denetimi · Çalışma dosyası

> ### ⚡ NİHAİ KURULUM GÜNCELLEMESİ (1 Ağustos 2026 · karar: [86_NIHAI](../86_NIHAI/CALISMA.md))
>
> Teorinin galaktik denklemi değişti: $v^2=V_{bar}^2+\sqrt{\mathcal{G}M_{kaps}(R)\,a_0}$
> (yerel $\ell_\omega$) ve $a_0=1{,}75\times cH_0/16{,}1$. `HESAP/` altındaki
> `SONUC.csv`, `YONTEM.md`, `ongoru_vs_fit.png` ve `panel.html` **nihai kurulumla yenilendi.**
> Bu sınıfın nihai sayıları: öngörü RMS **19,05 (ΛCDM 18,27)** km/s · dış sapma **+1,9%** ·
> gereken $a_0$ çarpanı **—** · öngörü yarışı **16/32**.
>
> Aşağıdaki metin ve tablolar **eski (A) kurulumun tarihsel kaydıdır** — silinmedi;
> güncel sayılar için `HESAP/` ve [toplu defter](../_HESAPLAR/toplu_defter.csv).


**32 galaksi · sınıflandırılmadı · örneklemin %18'i**

Hesap: `../../sinif_ongoru_vs_fit.py 99_KARMASIK`
Çıktılar: [`GEREKCE.csv`](GEREKCE.csv) · [`HESAP/SONUC.csv`](HESAP/SONUC.csv) · [`HESAP/YONTEM.md`](HESAP/YONTEM.md) · [`HESAP/ongoru_vs_fit.png`](HESAP/ongoru_vs_fit.png) · [`HESAP/panel.html`](HESAP/panel.html)

---

## 1. Bu klasörün amacı diğerlerinden farklıdır

Burada bir morfolojik sınıf yok. Bu 32 galaksi, **benim koyduğum dört dışlama ölçütünden** en az
birine takıldı. Dolayısıyla sorulan soru "modeller bu sınıfta nasıl" değil:

> **Dışladığım galaksiler, hükmü değiştirir miydi?**

Bu soru sorulmak zorundadır çünkü örneklemin **%18'i** dışarıda ve ölçütleri ben seçtim.
Sessizce bırakmak seçim etkisi olurdu.

**Uyarı:** aşağıdaki sonuçlar model karşılaştırması olarak alıntılanmamalıdır. Bu galaksiler
zaten güvenilir sınav vermedikleri için dışlandılar; buradaki sayıların işlevi **ölçütlerimin
yansızlığını denetlemektir.**

---

## 2. Ölçütler ve tip dağılımı

| Ölçüt | $n$ |
|---|---|
| SPARC kalite bayrağı $Q=3$ (düşük) | 12 |
| Eğiklik $i<30°$ (yüz-üstü) | 12 |
| Dönüş eğrisinde $N<6$ nokta | 10 |
| Kendi tipinde $N<5$ galaksi (S0, BCD) | 8 |

Örtüşmeler var; toplam 32. Galaksi başına gerekçe [`GEREKCE.csv`](GEREKCE.csv)'de.

Tip dağılımı: Im 12 · Sm 8 · BCD 5 · S0 3 · Sc 2 · Sab 1 · Sbc 1

---

## 3. Toplam sonuç (32 galaksinin medyanı)

| Model | $k$ | RMS (km/s) | $\chi^2_{ind}$ | Hata çubuğu içinde |
|---|---|---|---|---|
| Yalnız baryonlar ($\Upsilon_*=0{,}50$) | 0 | 27,45 | 23,57 | %3 |
| **Standart bilim ÖNGÖRÜSÜ** | 0 | **18,27** | 14,87 | %4 |
| Evrenakı ÖNGÖRÜSÜ | 0 | 20,91 | **12,31** | **%17** |
| ΛCDM fit | 2 | 5,64 | 1,13 | %74 |
| **Evrenakı fit** | 2 | **4,26** | **0,93** | **%79** |

Öngörü yarışı: **17/32** ($+0{,}4\sigma$ — beraberlik).

**Fitlerin bu kadar iyi olması ($\chi^2_{ind}$ 0,93 ve 1,13) bir başarı göstergesi değil,
dışlama gerekçesinin doğrulanmasıdır:** hata çubukları büyük ve nokta sayısı az olduğunda iki
parametreli her model kolayca uyar. Bu galaksiler ayırt edici değil.

---

## 4. Gerekçeye göre kırılım — ve ölçütlerimin yansız olmadığı

| Gerekçe | $n$ | Öngörü RMS E/L | Fit $\chi^2$ E/L | Öngörü oyu |
|---|---|---|---|---|
| $N<6$ nokta | 10 | **10,8** / 16,0 | **0,79** / 1,64 | 6/10 $+0{,}6\sigma$ |
| **$Q=3$ düşük kalite** | 12 | **16,3** / 32,3 | **0,51** / 1,01 | **11/12 $+2{,}9\sigma$** |
| Eğiklik $i<30°$ | 12 | 22,6 / **18,3** | 1,01 / **0,91** | 4/12 $-1{,}2\sigma$ |
| Tip S0/BCD | 8 | 25,3 / **15,6** | **1,13** / 1,29 | 3/8 $-0{,}7\sigma$ |

**İki ölçüt ters yönde iş görüyor:**

- **$Q=3$ dışlaması teorinin aleyhine işledi.** O altkümede Evrenakı **11/12** kazanıyor
  ($+2{,}9\sigma$) — sınıflandırılmış örneklemdeki en güçlü Evrenakı sonucundan ($+1{,}6\sigma$,
  Im) daha güçlü. Bu 12 galaksiyi çıkarmakla teorinin kazandığı bir altkümeyi elemişim.
- **Eğiklik dışlaması teorinin lehine işledi.** Orada Evrenakı 4/12 ile geride; çıkarmakla
  kaybettiği bir altkümeyi elemişim.

Bunu **kabul ediyorum: dışlama ölçütlerim yansız değildi.** İkisini de fiziksel gerekçeyle
seçtim ($Q=3$ SPARC'ın kendi düşük-kalite bayrağı; $i<30°$'de $V_{obs}=V\sin i$ kötü belirlenir),
ama **hangi tarafa çalışacağını bilmeden seçtim ve sonradan denetlemedim.** Şimdi denetlendi.

---

## 5. Küresel hükme etkisi — ölçülmüş

| Örneklem | Öngörü oyu | Anlamlılık |
|---|---|---|
| Sınıflandırılmış (6 sınıf) | 60/141 = %43 | $-1{,}77\sigma$ |
| Karmaşık | 17/32 = %53 | $+0{,}35\sigma$ |
| **Tümü (dışlama yok)** | **77/173 = %45** | $\mathbf{-1{,}44\sigma}$ |

Tek tek ölçütler eklendiğinde küresel anlamlılık:

| Eklenen | Küresel $\sigma$ | Fark |
|---|---|---|
| $N<6$ (n=10, Evr 6) | $-1{,}55$ | $+0{,}22$ |
| **$Q=3$ (n=12, Evr 11)** | $\mathbf{-0{,}89}$ | $\mathbf{+0{,}88}$ |
| Eğiklik (n=12, Evr 4) | $-2{,}02$ | $-0{,}25$ |
| S0/BCD (n=8, Evr 3) | $-1{,}88$ | $-0{,}12$ |

**Sonuç: net etki küçük ama tek bir ölçüt büyük.** Dışlamanın tamamı kaldırılsa hüküm
$-1{,}77\sigma$'dan $-1{,}44\sigma$'ya gelir — yön değişmez, anlamlılık zaten eşiğin altındaydı,
altında kalır.

**Ama $Q=3$ ölçütü tek başına $+0{,}88\sigma$ oynatıyor.** Bu, tek bir metodolojik kararın
hükmü ne kadar etkileyebileceğinin somut ölçüsüdür ve kayda geçmelidir.

> **Karar: dışlama korunuyor, gerekçesi burada.** $Q=3$ ve $i<30°$ dışlamaları veri kalitesine
> dayanır, sonuca değil — ve $Q=3$ altkümesindeki $+2{,}9\sigma$'lık Evrenakı galibiyeti tam
> olarak **düşük kaliteli verinin ayırt edememesinin** beklenen sonucudur (o altkümede
> $\chi^2_{ind}$ 0,51 ve 1,01; iki model de hata çubuklarının içinde kalıyor). Yani o galibiyet
> teorinin lehine kanıt değildir. Ama **dışlamanın hükmü hangi yöne oynattığı artık ölçülmüş ve
> yazılıdır**; okuyucu isterse tersini savunabilir.

---

## 6. Dürüstlük kayıtları

1. **Bu klasörün sayıları model karşılaştırması olarak kullanılamaz** (madde 1 ve 3).
2. **Dışlama ölçütlerimin yansız olmadığı ölçüldü ve kaydedildi** (madde 4). Yön: $Q=3$ teorinin
   aleyhine, eğiklik lehine, ikisi büyük ölçüde birbirini götürüyor.
3. Altkümeler küçük ($n=8$–12); tek tek anlamlılıkları temkinli okunmalı. $11/12$ sonucu bile
   $n=12$ ile $+2{,}9\sigma$'dır ve çoklu-karşılaştırma düzeltmesi yapılmamıştır (dört altküme
   sınandı).
4. $N<6$ altkümesinde iki parametreli fit $N-k\leq4$ serbestlik derecesiyle çalışıyor; oradaki
   $\chi^2_{ind}=0{,}79$ neredeyse anlamsızdır.
5. Bu klasördeki 32 galaksi ileride kullanılabilir: ölçüt gevşetilirse, ya da S0/BCD için bağımsız
   örneklem eklenirse. Karar geri alınabilir çünkü gerekçeler galaksi başına yazılı.

---

## 7. Çalışmanın tamamı — nihai durum

| | Galaksi | Öngörü oyu (Evrenakı) |
|---|---|---|
| 6 morfolojik sınıf | 141 | 60/141 = %43 ($-1{,}77\sigma$) |
| Karmaşık (denetim) | 32 | 17/32 = %53 ($+0{,}35\sigma$) |
| **Toplam** | **173** | **77/173 = %45 ($-1{,}44\sigma$)** |

**Hiçbir kurulumda anlamlı bir küresel kazanan yok.** Sınıf içinde iki güçlü sonuç var ve ters
yönlü: ΛCDM Sd'de $-4{,}0\sigma$, Evrenakı $Q=3$ altkümesinde $+2{,}9\sigma$ — ve ikincisi
kalitesiz veriden geliyor, yani kanıt sayılmaz.

**Açık uçların hepsi duruyor:** her iki modelin de $\Upsilon_*$ ihlali (geç tiplerde zıt yönde),
ΛCDM implementasyonunun yayınlanmış fitlerle doğrulanmamış olması, $D$ ve $i$'nin sabit tutulması,
hata korelasyonunun yok sayılması, ve eksik itimin **teşhis edilememesi.**
