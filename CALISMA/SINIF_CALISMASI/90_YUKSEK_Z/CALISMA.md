# 90_YUKSEK_Z — Teorinin **ilk SPARC dışı sınavı** · Çalışma dosyası

> ### ⚡ NİHAİ KURULUM (1 Ağustos 2026 · karar: [86_NIHAI](../86_NIHAI/CALISMA.md))
>
> Bu dosyanın analizi **eski (A) kurulumla** yapıldı ve tarihsel kayıt olarak duruyor.
> Nihai kurulum: yerel $\ell_\omega$ + $a_0=1{,}75\times cH_0/16{,}1$. Nihai sayılar: Yüksek-$z$ $f_{DM}$ artığı **+0,186'ya YÜKSELDİ** (eski +0,118) — nihai kurulumun tek kötüleşen ölçütü. Bu dosyanın açığı artık teorinin **birincil** açık kalemi.


**Genzel R. ve ark. 2017, Nature 543, 397 · arXiv:1703.04310 · 6 galaksi, $0{,}85<z<2{,}38$**

Hesap: `../../yuksek_z_sinavi.py` · Veri: `../../veri/_genzel2017_tablo1.csv`
Çıktılar: [`SONUC.csv`](SONUC.csv) · [`yuksek_z.png`](yuksek_z.png)

---

## 0. Neden bu sınav özel

Bu çalışmanın bütün sonuçları bugüne dek **tek bir veri kümesinden** okundu: SPARC. Kitabın
kendi en ağır özeleştirisi de buydu —

> *"Evrenakı'nın türetimlerinin tamamı sınandıkları aynı dönüş eğrilerinden okunmuştur…
> $a_0$ post-hoc, $\ell_\omega$ aynı örnekten… **Evrenakı'nın türetimleri öngörü statüsünü
> henüz kazanmamıştır.**"* (7.4 madde 12)

Genzel+2017 verisi **bu çalışmaya hiç girmedi.** Kalibrasyon yok, fit yok, ayar yok.
Teori ne diyorsa o.

Ve sınav bir **ayırt edici**: [91_A0_KOPRU](../91_A0_KOPRU/CALISMA.md) iki okuma bırakmıştı ve
$z=2$'de %31 ayrışıyorlar.

| | $a_0(z)$ |
|---|---|
| **KOZMİK** (kitabın $cH_0/16{,}1$ okuması) | $a_0(0)\times H(z)/H_0$ |
| **SABİT** ([92_M_TUT](../92_M_TUT/CALISMA.md)'un $\mathcal{G}m_n/\ell_\omega^2$ okuması) | $a_0(0)$ |

---

## 1. Yöntem — kütle modeli **gerekmiyor**

Evrenakı'da karanlık madde yoktur. Genzel'in ölçtüğü $f_{DM}$ bizde **F4'ün payıdır:**

$$f_{DM}=\frac{v_{F4}^2}{v_c^2}$$

B kurulumunda $a_{F4}=\sqrt{a_{F1}a_0}$, yani $v_{F4}^2=v_{bar}\sqrt{a_0R}$. Bunu
$v_c^2=v_{bar}^2+v_{F4}^2$ içine koyup $s=v_{bar}/v_c$ için çözelim:

$$s^2+s\,\frac{\sqrt{a_0R}}{v_c}-1=0 \;\Longrightarrow\;
s=\frac{-b+\sqrt{b^2+4}}{2},\quad b=\frac{\sqrt{a_0R}}{v_c}
\;\Longrightarrow\; f_{DM}^{öng}=1-s^2$$

> **Yalnız $v_c$ ve $R$ gerekiyor.** Kütle modeli, $\Upsilon_*$, disk geometrisi, eğiklik —
> hiçbiri girmiyor. İkisi de Genzel Tablo 1'de **doğrudan ölçülmüş** büyüklüklerdir.

$a_0(0)=\mathcal{G}m_n/\ell_\omega^2=8{,}78\times10^{-11}$ m/s² — 92_M_TUT'un ölçtüğü
$\ell_\omega=35{,}7$ fm ile. **Yüksek-$z$ verisine hiç bakılmadan sabitlendi.**

### Girdi denetimi — tabloyu doğru mu okudum?

Genzel'in kendi sayıları birbirini tutuyor mu? $v_{bar}$'ı iki ayrı yoldan çıkardım:
(a) verdikleri $f_{DM}$'den, (b) verdikleri $M_{bar}$ ve kovan oranından.

Oranlar: **1,00 · 1,06 · 1,07 · 1,08 · 1,07 · 1,05** (medyan 1,07). %7'lik fark küresel
yaklaşımın diske göre fazlasıdır — beklenen. **Tablo doğru okundu.**

---

## 2. Çapa — formül yerelde tutuyor mu?

Aynı formül, aynı $a_0$, SPARC'ta eğrinin orta yarıçapında (140 galaksi):

| | |
|---|---|
| öngörülen $f_{DM}$ medyan | 0,706 |
| ölçülen $f_{DM}$ medyan | 0,655 |
| **fark** | **$+0{,}048$** |
| saçılma | 0,180 |

**Çapa tutuyor.** Yani formül $z\approx0$'da doğru mertebeyi veriyor ve yüksek-$z$'deki sapma
formülün kendisinden değil, evrimden (ya da yüksek-$z$'ye özgü bir şeyden) geliyor.

---

## 3. Sonuç — sayılar

| Galaksi | $z$ | $R_{1/2}$ | $v_c$ | **gözlenen $f_{DM}$** | **SABİT** | **KOZMİK** |
|---|---|---|---|---|---|---|
| COS4 01351 | 0,854 | 7,3 | 276 | 0,21 (0,11–0,31) | 0,396 | 0,471 |
| D3a 6397 | 1,500 | 7,4 | 310 | 0,17 (<0,38) | 0,364 | 0,495 |
| GS4 43501 | 1,613 | 4,9 | 257 | 0,19 (0,10–0,28) | 0,359 | 0,498 |
| zC 406690 | 2,196 | 5,5 | 301 | 0,00 (<0,08) | 0,332 | 0,511 |
| zC 400569 | 2,242 | 3,3 | 364 | 0,00 (<0,07) | 0,228 | 0,374 |
| D3a 15504 | 2,383 | 6,0 | 299 | 0,12 (<0,26) | 0,345 | 0,541 |

| Okuma | medyan $f_{DM}$ | medyan artık | yayının aralığında | üst sınırı **aşan** | $\langle\lvert$artık$\rvert/\sigma\rangle$ |
|---|---|---|---|---|---|
| **SABİT** | 0,352 | $+0{,}210$ | **1/6** | 5/6 | **3,28** |
| **KOZMİK** | 0,496 | $+0{,}349$ | 0/6 | 6/6 | **6,10** |
| *gözlenen* | *0,145* | — | — | — | — |

---

## 4. Hüküm — iki parça, biri lehte biri aleyhte

### (a) Ayırt edici çalıştı: **SABİT okuma kazandı**

| | |
|---|---|
| medyan $\lvert$artık$\rvert$ | SABİT **0,210** · KOZMİK 0,349 |
| $\langle\lvert$artık$\rvert/\sigma\rangle$ | SABİT **3,28** · KOZMİK 6,10 |
| yayının aralığına düşen | SABİT **1/6** · KOZMİK **0/6** |

**Kozmik okuma her galakside daha kötü ve altısının altısında üst sınırı aşıyor.**
$a_0\propto cH(z)$ okuması bu veriyle **desteklenmiyor.**

Bu, [91_A0_KOPRU](../91_A0_KOPRU/CALISMA.md)'nün önerisini doğruluyor: $a_0$ kozmik bir
ivme değil, **mikro sabitlerden gelen** bir büyüklüktür. Kitabın $a_0=cH_0/16{,}1$ okuması
ve ondan türeyen $(\rho_0/\rho_n)^2$ ifadesi **düşmelidir.**

### (b) Ama teori yine de **fazla öngörüyor** — ve bu ciddi

Kazanan okumada bile medyan artık $+0{,}21$. Yerel çapanın kayması $+0{,}048$; geriye
**$\sim+0{,}16$'lık gerçek bir yüksek-$z$ açığı** kalıyor.

> **Teorinin ilk SPARC dışı sınavı, niceliksel olarak başarısızdır.**
> Altı galaksinin beşinde öngörü yayının üst sınırının üstünde. Bu satır silinmedi,
> yumuşatılmadı; sonucun yarısı budur.

Fiziksel okunuşu: teori bu sıkı, yoğun, yüksek-$z$ disklerinde **gereğinden çok F4 üretiyor.**
Yani $a_0$'ın *değeri* değil, F4'ün **yoğun rejimde nasıl doyduğu** eksik —
[95_RAR](../95_RAR/CALISMA.md)'ın ölçtüğü geçiş biçimi sorununun aynısı, şimdi
$z\sim2$'de ve çok daha büyük.

---

## 5. Dürüstlük kayıtları

1. **Genzel'in $f_{DM}$'si model bağımlıdır.** NFW halesi + $n=1$ disk + kovan üçlü
   modelinin fit çıktısıdır. Bizim öngörümüz yalnız $v_c$ ve $R$ kullanır, ama
   *karşılaştırıldığı sayı* onların mass modelinden gelir. Bağımsız değildir.
2. **Altı galaksi seçilmiştir** — en kütleli, en geniş, en iyi gözlenen. Yüksek yüzey
   yoğunluklu uca eğilimli, yani düşük $f_{DM}$'ye eğilimli bir örneklem. Bu, teorinin
   aşımını **abartıyor olabilir.** Lang+2017'nin 101 galaksilik yığılmış eğrisi bu
   yanlılığı azaltır ve **işlenmemiştir.**
3. **Asimetrik sürükleme.** Bu diskler $v/\sigma\sim3$–5, yani basınç desteği ciddidir.
   Genzel'in $v_c$'si bu düzeltmeyi **içerir** ve doğru karşılaştırma odur. Ama M-37
   dairesel yörünge için kuruludur; düzeltilmiş bir $v_c$'yi ona vermek bir varsayımdır.
4. **$a_0(0)$ yerel örneklemden geldi** (92_M_TUT'un $\ell_\omega=35{,}7$ fm'si). Bu bir
   kalibrasyondur — ama **yüksek-$z$ verisine bakılmadan** yapılmıştır, yani bu sınav için
   öngörüdür.
5. **Çapa kayması $+0{,}048$ düzeltilmedi.** Düzeltilseydi SABİT okumanın artığı
   $+0{,}21 \to +0{,}16$ olurdu; hüküm değişmezdi (hâlâ 5/6 üst sınırın üstünde).
6. **Üst sınırlı dört galakside** artık hesabı üst sınıra göre yapıldı, yani teoriye
   **en elverişli** okuma. Gerçek $f_{DM}$ daha küçükse aşım daha büyüktür.
7. **Tablo elle aktarıldı.** PDF'ten okunup `veri/_genzel2017_tablo1.csv`'ye yazıldı;
   iç tutarlılık denetimi (md. 1) geçti ama ikinci bir göz denetlemedi.
8. **$H(z)$ için ΛCDM genişleme geçmişi kullanıldı** ($\Omega_m=0{,}3$, $\Omega_\Lambda=0{,}7$).
   Evrenakı'nın kendi genişleme geçmişi farklıysa KOZMİK okumanın eğrisi de değişir —
   ama SABİT okuma bundan **etkilenmez**, çünkü $H$ hiç girmez.

---

## 6. Ne çıktı — üç cümle

1. **Ayırt edici çalıştı ve SABİT okuma kazandı:** $a_0\propto cH(z)$ altı galaksinin
   altısında üst sınırı aşıyor, sabit okuma birinde aralığa giriyor; ortalama sapma
   $6{,}10\sigma$'ya karşı $3{,}28\sigma$. **$a_0$ kozmik zamanla değişmiyor.**
2. **Ama teori bu veride niceliksel olarak başarısız:** kazanan okumada bile medyan
   $f_{DM}$ aşımı $+0{,}21$ (yerel çapa düşüldükten sonra $+0{,}16$). Beş galakside öngörü
   yayının üst sınırının üstünde.
3. **Açık, 95_RAR'ın açığının aynısı:** yoğun/yüksek ivme rejiminde F4 **fazla** üretiyor.
   $a_0$'ın değeri değil, **geçiş biçimi** eksik.

## 7. Bundan çıkan iş

| # | İş | Neden |
|---|---|---|
| **1** | **Lang+2017'nin 101 galaksilik yığılmış eğrisiyle tekrarla** | md. 5.2 — altı galaksi seçilmiş; yığılmış eğri yanlılığı kırar |
| **2** | F4'ün yoğun rejimde doyumunu türet | md. 6.3 — 95_RAR ile aynı açık; ikisi tek sorun olabilir |
| 3 | Kitabın $a_0=cH_0(\rho_0/\rho_n)^2$ ifadesini kaldır | md. 4a — bu sınav kozmik okumayı reddetti |
| 4 | Asimetrik sürüklemeli sistemler için M-37'yi genişlet | md. 5.3 — $v/\sigma\sim3$'te dairesel varsayım zorlanıyor |

**Madde 2 artık iki bağımsız veri kümesinden geliyor** (SPARC'ın yüksek ivme kuşakları ve
Genzel'in $z\sim2$ diskleri). İkisi de aynı şeyi söylüyor: **F4 yoğun rejimde çok güçlü.**
Bu, teorinin şu andaki tek somut ve tekrarlanmış açığıdır.
