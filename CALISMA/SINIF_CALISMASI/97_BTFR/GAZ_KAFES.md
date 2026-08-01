# «Gazda kafes yapısı yok, F4'e katkısı az» — iddianın sınavı

Hesap: `../../gaz_kafes_sinavi.py` · Görsel: [`gaz_kafes.png`](gaz_kafes.png) · 121 galaksi, **fit yok**

**İddia (yazar, 31 Temmuz 2026):** *"Gaz F4 kuvvetinde kafes yapısı olmadığından etkisi oldukça
azdır. Bunu toplam kütle verisi olarak kullanamazsın."*

---

## 0. Önce: bu iddia hangi yöne bakıyor?

Tahminle cevaplanamaz, çünkü gaz F4'e **iki ayrı yerden** girer:

| | Nereye | Gaz çıkarsa |
|---|---|---|
| **(A) Pay** | $F4 = \mathcal{G}M_{kaynak}/\ell_\omega$ | $F4$ **küçülür** |
| **(B) Bölen** | $\ell_\omega=q_n/(2\gamma_n)$ — $\gamma_n$ dolanım debisi. Kafes gerekiyorsa gaz $\gamma_n$'e girmez, $\ell_\omega$ **büyür** | $F4$ yine **küçülür** |

Yani iki kanat da **aynı** yöne bakıyor: F4 zayıflar. F1 ($V_{bar}$) etkilenmez — pulsasyon kütle
deplasmanıdır, kafes gerektirmez; bu ayrımı iddianın kendisi yapıyor ("F4 kuvvetinde").

Üç uygulama sınandı ($f=M_{kafes}/M_{bar}$, gaz ağırlığı $w$):

| | Ölçekleme |
|---|---|
| **K1** yalnız pay | $F4 \to f\cdot F4$ |
| **K2** yalnız bölen | $F4 \to f\cdot F4$ |
| **K3** ikisi birden (mekanizmaya en sadık) | $F4 \to f^2\cdot F4$ |

---

## 1. Ayrıştırma denetimi — gaz ve yıldızı doğru mu ayırdık?

$$M_* = 0{,}5\,L_{3,6}, \qquad M_{gaz}=1{,}33\,M_{HI}$$

| | |
|---|---|
| $\log[(M_*+1{,}33M_{HI})/M_b^{yayın}]$ medyan | $\mathbf{+0{,}000}$ dex |
| saçılma | 0,003 dex |

**Ayrıştırma tam.** Lelli+2019'un yayınlanmış $M_b$'si bire bir bu iki parçanın toplamı, yani
sınav gerçekten gazı ayırıyor.

| Gaz oranı $M_{gaz}/M_{bar}$ | |
|---|---|
| medyan | **0,40** |
| aralık | 0,02 – 0,95 |
| gaz **baskın** ($f>0{,}5$) galaksi | **44/121** |
| gaz oranı ↔ $\log M_b$ (Spearman) | $\mathbf{-0{,}78}$ |

Bu son satır kritik: gaz oranı kütleyle **güçlü biçimde ters** ilişkili. Yani bu iddia sabit bir
kayma değil, **kütleye bağlı** bir düzeltmedir — eğimi de oynatır.

---

## 2. İddianın bedeli — üç uygulamanın hepsinde aleyhte

| Kurulum | $w$ | $v_{öng}/v_{ölç}$ | Eğim | Gereken $a_0$ |
|---|---|---|---|---|
| **mevcut hâl (gaz tam sayılır)** | **1,00** | **0,885** | **3,632** | **×2,02** |
| K1/K2 yalnız pay **ya da** yalnız bölen | 0,50 | 0,816 | 3,253 | ×3,12 |
| | 0,25 | 0,776 | 3,020 | ×4,58 |
| | **0,00** | **0,730** | **2,727** | **×6,24** |
| K3 ikisi birden | 0,50 | 0,752 | 2,977 | ×5,23 |
| | 0,25 | 0,691 | 2,691 | ×8,82 |
| | **0,00** | **0,640** | **2,485** | **×15,07** |
| *GÖZLENEN* | — | *1,000* | *3,530–3,738* | — |

**İki cephede birden kaybediliyor:**

1. **Normalizasyon.** Hız açığı $-11{,}5\%$'ten $-27\%$'e (K1) ya da $-36\%$'ye (K3) çıkıyor.
   Gereken $a_0$ çarpanı ×2,02'den **×6,24 – ×15,07**'ye. Kitabın kendi BTFR gerilimi kaydı
   (×2,26) ve sınıf çalışmasının bandı (×1,47–3,76) ile **örtüşme tümüyle kayboluyor.**
2. **Eğim — asıl kayıp burada.** Teorinin en güçlü sonucu eğimin gözlenen bandın içinde olmasıydı
   (3,632 · band 3,530–3,738). Gaz bastırılınca eğim **3,632 → 2,727** (K1) ya da **2,485** (K3)
   oluyor. Yani **ΛCDM zincirinin bölgesine** (2,716) düşüyor. Teorinin ΛCDM'e karşı tek net
   üstünlüğü tam olarak siliniyor.

Grafiğin orta ve sağ panelleri bunu sürekli olarak gösteriyor: $w$ 1'den 0'a giderken hiçbir
noktada iyileşme yok, her iki eğri de tek yönde kötüleşiyor.

---

## 3. Ama asıl sınav bu değil — **veri iddiayı destekliyor mu?**

İddianın **lehte** olabileceği tek yer vardı ve onu ayrıca sınadım. Mantık şu: gaz gerçekten
F4'e katkı vermiyorsa ve biz onu tam ağırlıkla sayıyorsak, **gaz zengini galaksileri fazla
öngörüyor** olmalıyız. O hâlde artık ($\log v_{öng}/v_{ölç}$) gaz oranıyla **artmalı**.

| Test | Sonuç | İddianın beklediği |
|---|---|---|
| Spearman[artık , gaz oranı] | $\mathbf{+0{,}01}$ | belirgin **pozitif** |
| Doğrusal eğim | $+0{,}005$ | belirgin pozitif |
| Gaz **zengin** yarı ($f>0{,}40$, $n=60$) medyan artık | $-0{,}051$ dex | daha az açık |
| Gaz **yoksul** yarı ($f<0{,}40$, $n=61$) medyan artık | $-0{,}055$ dex | daha çok açık |
| **Fark (zengin − yoksul)** | $\mathbf{+0{,}003}$ **dex** | belirgin pozitif |

**Fark sıfır.** 0,003 dex, yani binde 0,7 hız — ölçüm gürültüsünün çok altında. Gaz oranı 0,02'den
0,95'e, yani **kırk yedi kat** değişirken artık kılını kıpırdatmıyor.

Ve iddianın açıklayabileceğini umduğum şey de olmuyor:

| | |
|---|---|
| Spearman[galaksi başına gereken $a_0$ , gaz oranı] | $-0{,}08$ |
| Sınıf çalışmasının ×1,47–3,76 saçılmasını açıklıyor mu? | **Hayır** |

---

## 4. Cevap: **aleyhte** — ve iddianın öncülü de veriyle çelişiyor

**Sorunun cevabı: aleyhte.** Üç ayrı uygulamada da, hem normalizasyonu hem eğimi bozuyor; eğimi
ΛCDM'in bölgesine düşürdüğü için teorinin **en güçlü sonucunu** yok ediyor.

Ama daha önemlisi: iddia sadece elverişsiz değil, **veri tarafından desteklenmiyor.** Eğer gazın
F4'e katkısı gerçekten az olsaydı, gaz oranı 47 kat değişirken artıkta bunun izi görünürdü.
Görünmüyor.

> ### Bu, doğru okununca teorinin **lehine** bir bulgudur
>
> Ölçümün söylediği şu: **F4'ün kaynağı toplam baryonik kütledir, yıldız kütlesi değil.** Gaz,
> yıldızla *tam aynı ağırlıkta* F4 üretiyor — 121 galakside gaz oranı 0,02'den 0,95'e giderken
> tek bir sistematik sapma bırakmadan.
>
> Bu, teorinin **kütle-kaynaklı** kurulumunun bir başarısıdır. Kütle-itim, maddenin *hangi
> hâlde* olduğuna bakmıyor — sadece ne kadar olduğuna. Teori zaten bunu söylüyor
> (4.2.4: $\gamma_N/m = V_n/m_n = 1/\rho_n$, **evrensel**). Ölçüm o evrenselliği doğruluyor.
>
> Kafes koşulu eklemek, teoriye **gözlemin reddettiği** bir kısıt eklemek olurdu.

**Yapılacak iş: hiçbir şey.** Mevcut kurulum ($M_{kaps}$ ve $\ell_\omega$'da gaz tam ağırlıkla)
doğru olan kurulumdur ve değiştirilmemelidir.

---

## 5. Dürüstlük kayıtları

1. **Sınav çarpımsal ölçeklemeyi varsayar.** F4'ü $f$ ya da $f^2$ ile çarptım. Gazın F4'e girişi
   *çarpımsal olmayan* bir biçimdeyse (örneğin yarıçapa bağlı, ya da yalnız belirli bir yoğunluk
   eşiğinin altında), bu sınav onu kapsamaz. O hâlin ayrıca kurulması gerekir.
2. **Moleküler gaz ($H_2$) yok.** SPARC yalnız $M_{HI}$ verir; $M_{gaz}=1{,}33M_{HI}$ helyum
   düzeltmesidir. $H_2$ büyük sarmallarda daha çok bulunur, yani onu eklemek gaz oranını **kütleyle
   daha az** ters ilişkili yapardı — testin ayırt gücünü bir miktar **düşürür.** Ancak ölçülen
   korelasyon $+0{,}01$ olduğu için bu, sonucu değiştirecek mertebede değil.
3. **$V_{bar}$'daki gaz dokunulmadı.** F1'de gaz tam ağırlıkla duruyor. İddia F4 hakkında olduğu
   için bu doğru; ama eğer kafes koşulu F1 için de istenirse sonuç **daha da** kötüleşir
   ($V_{gaz}^2$ çıkarılırsa hız açığı büyür).
4. **Yalnız $V_f$ ve son ölçüm noktası kullanıldı.** Diğer altı hız tanımı ve üç yarıçap seçimi
   bu sınavda taranmadı; ana sınavdaki duyarlılık bandı (×1,73–2,02) burada tekrarlanmadı.
5. **Bu sınavı ben önermedim, yazar önerdi.** Sonuç yazarın beklediğinin tersi çıktı ve öyle
   yazıldı. Kaydı, teorinin lehine çıkan sonuçlarla aynı yerde duruyor.
