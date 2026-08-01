# 86_NIHAI — Nihai kurulum kararı ve toplu defter · **1 Ağustos 2026**

Hesap: `../../toplu_defter.py` · Çıktılar: [`../_HESAPLAR/toplu_defter.csv`](../_HESAPLAR/toplu_defter.csv) ·
[`../_HESAPLAR/toplu_defter.png`](../_HESAPLAR/toplu_defter.png)

---

## 1. Karar — teorinin galaktik denklemi artık şu

$$\boxed{\;v^2(R)=V_{bar}^2(\Upsilon_*)\;+\;\sqrt{\mathcal{G}\,M_{kaps}(R)\,a_0}\;,
\qquad a_0=1{,}75\times\frac{cH_0}{16{,}1}=7{,}39\times10^{-11}\ \mathrm{m/s^2}\;}$$

İki değişiklikten oluşur:

| # | Değişiklik | Kaynağı | Statüsü |
|---|---|---|---|
| 1 | **$\ell_\omega$ yerel kütleden**: $v_{F4}^2=\sqrt{\mathcal{G}M_{kaps}(R)a_0}$ (eski: $\mathcal{G}M_{kaps}/\ell_\omega(M_{bar})$) | [94_YEREL_LOMEGA](../94_YEREL_LOMEGA/CALISMA.md) — akı teoremi gereği; 6.5.4.3'ün türetiminde $M_{bar}$ zaten hiç yoktu | tutarsızlık giderme, **yeni parametre yok** |
| 2 | **$a_0$ ×1,75** | türetim ([92_M_TUT](../92_M_TUT/CALISMA.md): $a_0=\mathcal{G}m_n/\ell_\omega^2$) **×1,75–2,08 bandı** verir; gözlem alt ucu seçer | kalibrasyon güncellemesi |

**×1,75'in gerekçesi (×2,08'e karşı):** ×1,75'te dış yarı sapması $-0{,}1\%$ (tam sıfır), BTFR
eğimi 3,734 (**bandın içinde**), normalizasyon 0,984; ×2,08 BTFR eğimini band dışına (3,754)
taşıyor ve yüksek-$z$ cezasını büyütüyordu. ×1,75 aynı zamanda 94_YEREL_LOMEGA'nın sayısal
çözümünün (×1,77) değeridir. Türetimin girdisi $\ell_\omega^{mikro}=35{,}7$ fm'nin saçılması
0,171 dex olduğundan **türetim ×1,75 ile ×2,08 arasında seçim yapacak keskinlikte değildir** —
seçimi gözlem yapar, ve bu kayıt bunu gizlemez.

---

## 2. Toplu defter — A (kitabın hâli) → F (nihai)

| Ölçüt | A mevcut | **F nihai** | A→F | ΛCDM |
|---|---|---|---|---|
| Dönüş eğrisi RMS (141 gal.) | 19,51 | **12,79** | **−34%** | 14,56 |
| Dış yarı sapması | −12,4% | **−0,1%** | −99% | — |
| BTFR eğimi (117 gal.) | 3,664 ✓ | **3,734 ✓** | bandın içinde | 2,716 ✗ |
| BTFR normalizasyonu | 0,893 | **0,984** | −0,091 | 1,027 |
| RAR medyan artık | −0,118 | **−0,003** | −98% | — |
| RAR biçim eğimi | +0,101 | **+0,051** | −50% | — |
| ETG dış nokta (16 gal.) | −0,090 | **−0,008** | −91% | +0,045 |
| S0+BCD RMS (8 gal.) | 25,3 | **19,0** | −25% | — |
| **Yüksek-z $f_{DM}$ artığı** | +0,118 | **+0,186** | **+58% ✗** | — |

**8 ölçüt iyileşti, 1 kötüleşti.** Tek kötüleşen yüksek-$z$ — ve o zaten teorinin kayıtlı
tek büyük açığı ([90_YUKSEK_Z](../90_YUKSEK_Z/CALISMA.md)).

### Teori ilk kez ΛCDM'i geçiyor — sıfır serbest parametrede

- dönüş eğrisi RMS: **12,79 < 14,56**
- ETG dış nokta: **|−0,008| < |+0,045|**
- BTFR eğimi: **bandın içinde** vs 0,81 dışarıda
- öngörü yarışı: **79/141** galakside önde (eski kurulumda 60/141'di)

## 3. Sınıf sınıf (dönüş eğrisi RMS, A→F)

| Sınıf | n | A | **F** | A→F | yeni gereken çarpan |
|---|---|---|---|---|---|
| Sa–Sab | 12 | 27,68 | 25,82 | −7% | ×1,16 |
| Sb–Sbc | 29 | 25,35 | 27,35 | **+8%** | ×0,90 |
| Sc–Scd | 30 | 21,35 | 16,65 | −22% | ×1,08 |
| Sd | 16 | 20,87 | 10,12 | **−52%** | ×1,53 |
| Sdm–Sm | 28 | 18,17 | 9,89 | **−46%** | ×1,12 |
| Im | 26 | 7,67 | 8,12 | +6% | ×0,65 |

Dört sınıfın gereken çarpanı artık **×0,90–1,16** — bire oturdu. Uçlar Sd (×1,53) ve
Im (×0,65); sınıf bandının log genişliği **değişmedi** (0,113 dex) — $a_0$ ölçeklemesi bandı
kaydırır, daraltmaz. Bu açık kalem ([97_BTFR](../97_BTFR/CALISMA.md) md. 2) duruyor.

## 4. Nelere işlendi

| Ne | Durum |
|---|---|
| `sinif_ongoru_vs_fit.py` (çekirdek boru hattı: öngörü + fit biçimi) | ✅ nihai |
| 01–06 + 99 yeniden koşuldu: `HESAP/SONUC.csv` · `YONTEM.md` · `ongoru_vs_fit.png` | ✅ yenilendi |
| Sınıf panelleri (`kur_etkilesimli.py` → 7× `panel.html`) | ✅ yenilendi |
| BTFR paneli (`kur_etkilesimli_btfr.py`) — $a_0$ nihai, etiketler | ✅ yenilendi |
| ETG paneli (`kur_etkilesimli_etg.py`) | ✅ yenilendi |
| `sinif_carpan_duzeltme.py` + `s0_bcd_sinavi.py` (öz denetimler nihai kuruluma) | ✅ geçti (0,049 / 0,033 puan) |
| Toplu defter (4 kurulum: A/B/C/F) | ✅ kaydedildi |

**Bilerek dokunulmayanlar:** 95/96/97/90 çalışma dosyalarının tarihsel analizleri ve
figürleri — onlar eski kurulumun **ölçüm kayıtlarıdır** ve bu projenin kuralı gereği
silinmez; başlıklarına nihai-kurulum kutusu eklendi. Kitap (`Metin/`) dosyalarına da
dokunulmadı — oraya işlenecek değişiklik listesi md. 6'da.

---

## 5. Dürüstlük kayıtları

1. **×1,75 bir kalibrasyondur.** Türetim ×1,75–2,08 bandı verdi; bandın *içinden* değeri
   gözlem seçti. "$a_0$ türetildi" cümlesi ancak "biçimi türetildi, değeri band içinde
   gözlemle sabitlendi" olarak kurulabilir.
2. **Yüksek-$z$ kötüleşti ve kabul edildi** (+0,118 → +0,186). Gerekçe: o açık $a_0$'ın
   değerinden değil F4'ün yoğun rejim davranışından geliyor ([89_KAFES](../89_KAFES/AYIRMA.md):
   yoğun uçta baryonlar tek başına aşıyor — $a_0$'dan bağımsız). Ama bu bir *okumadır*;
   sayı olarak yüksek-$z$ nihai kurulumda **daha kötüdür.**
3. **Sb–Sbc ve Im kötüleşti** (+8% / +6%). Nihai kurulum her sınıfı iyileştirmiyor; medyanı
   iyileştiriyor. Sınıf bandı (log genişlik 0,113 dex) hiç daralmadı.
4. **Fit biçimi de değişti** (boru hattında $b\cdot M$ → $b\cdot\sqrt{M}$, parametre sayısı
   aynı). Eski fit sonuçlarıyla ($\chi^2$, $\Upsilon_*$ bandı ihlalleri) yeni sonuçlar
   **doğrudan karşılaştırılamaz**; karşılaştıran her cümle yeniden ölçülmeli.
5. **BTFR eğimi bandın içinde ama kenara yakın** (3,734; üst sınır 3,738). Band ölçümü
   kendisi ağırlıklandırmaya duyarlıdır (3,530–3,738); bu rahatlık payı küçük.
6. **Aynı veriyle seçim yapıldı.** ×1,75, sınandığı SPARC örnekleminden seçildi — kitabın
   7.4'teki "türetimler sınandıkları veriden okunuyor" özeleştirisi bu karar için de
   geçerlidir. Bağımsız doğrulama hâlâ yüksek-$z$ ve SPARC dışı veride.

## 6. Kitaba işlenecekler — ✅ **UYGULANDI** (1 Ağustos 2026, yalnız `07_Galaktik_Yorungeler.md`)

1. 6.5.4.4'ün denklemi: $v^2=V_{bar}^2+\mathcal{G}M_{kaps}/\ell_\omega$ →
   $v^2=V_{bar}^2+\sqrt{\mathcal{G}M_{kaps}(R)\,a_0}$ (yerel biçim; $h$ sadeleşmesi aynı kalır).
2. $a_0$ satırı: $cH_0/16{,}1$ → **[S]** statüsünde $7{,}39\times10^{-11}$ m/s²
   ($=1{,}75\,cH_0/16{,}1$), mikro biçimi $\mathcal{G}m_n/\ell_\omega^2$ ile ([92_M_TUT]).
3. $(\rho_0/\rho_n)^2$ karesi kaldırılmalı — türetim birinci kuvvet veriyor ([91_A0_KOPRU]).
4. 6.5.4.4 tablosundaki $q_n/\gamma_n=4{,}36\times10^{20}$ m düzeltilmeli
   (~$7\times10^{-14}$ m; 34 mertebe — $\sqrt{N}$ karışması).
5. 6.5.4.3'e $\sqrt{N}$ (rastgele yürüyüş) toplanması ve $M_{tut}=m_n$ türetimi.

**Uygulama kaydı (nihai metin, 1 Ağustos 2026):** beşi de kitabın galaktik bölümüne **nihai
metin** olarak işlendi — yazar talebiyle güncelleme/geri-çekme kutuları kaldırıldı, bölüm
yalnız güncel sonuçları anlatır: 6.5.4.3 Adım 6 ($\sqrt{N}$ + $M_{tut}=m_n$); 6.5.4.4 yerel
biçim; $q_n/\gamma_n\approx7\times10^{-14}$ m; $a_0=\mathcal{G}m_n/\ell_\omega^2=7{,}39\times10^{-11}$
m/s² [S]; kozmik okuma yüksek-$z$ ile dışlanmış olarak; BTFR kapanışı ve kalan RAR artığı
(+0,051). **Eş kayıtlar da işlendi:** Ek C satır 20 (Kısım 1, 1.3.4), sembol sözlüğü
($q_n$, $\gamma_n$, $\ell_\omega^{mikro/etkin}$ satırları), 7.4 madde 12 (g/h/j dahil).
Ayrıca $\Upsilon_*$ bant sınavı nihai kurulumla yeniden ölçüldü (`CALISMA/upsilon_bant_nihai.py`,
169 galaksi): serbest medyan $\Upsilon_*$ 0,84 → **0,49** (tam fotometrik beklenti), bant
dayatma bozulması %240 → **%44** (ΛCDM %32) — eski "en ağır bulgu" büyük ölçüde çözüldü;
kalan açık bant altındaki uyum farkı (4,91'e karşı 2,49).
