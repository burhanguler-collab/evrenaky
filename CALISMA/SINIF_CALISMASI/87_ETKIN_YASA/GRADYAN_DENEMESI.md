# Gradyan denklemi denemesi — tam zincir + türetim girişimi + ayrıştırma (iş 15)

**Statü: ÇALIŞMA KAYDI — kitaba işlenmedi (kullanıcı kararı: önce tartışma).**
Hesaplar: `../../gradyan_denemesi.py` + oturum-içi yan-sınavlar.

G1 (gradyan denklemi): $v^2=V_{bar}^2+\sqrt{g_{bar}a_0}\,R\cdot W$, $W=\min(1,a_0/g_{bar})$;
adil kalibrasyon (dış-yarı medyan sapma $=0$): $k=0{,}935\Rightarrow a_0^{G1}=6{,}92\times10^{-11}$
(M-45 bandı 6,8–9,3'ün içinde).

## 1. Tam zincir sonuçları (P = resmî denklemin kayıtlı değerleri)

| Ölçüt | P (resmî) | G1 (gradyan) |
|---|---|---|
| Defter medRMS (141) | 12,48 | **12,04** |
| Sb–Sbc / Sdm–Sm | 21,19 / 9,93 | **18,92 / 8,54** |
| BTFR v3 (eğim · norm) | 3,717 · 0,978 | 3,708 · **0,992** |
| RAR.mrt biçim eğimi | **+0,0002** | −0,0043 (o da ≈0) |
| Rotmod biçim eğimi | **−0,002** | +0,011 |
| Yüksek-z | **5/6** (−0,072) | 4/6 (−0,083) |
| Sınıf bandı | **16,2 %** | 17,7 % |
| dSph / MIGHTEE | geçti | **etkilenmez** (küresel limitte özdeş; sıfır-nokta braket içi) |

## 2. Türetim girişimi — ve yan-sınavda çürümesi

**Aday zincir (Kelvin/düzlemsel-akı):** dolanım akış çizgileriyle taşınır (Kelvin); yassı kaynak,
deplasman akısını disk düzlemine yoğunlaştırır; kolonun içtiği pay düzlemsel akı yoğunluğuyla
($g_{bar}$) ölçülür → etkin besleme $M_{eff}=V_{bar}^2R/\mathcal{G}=M_{kaps}f_{geo}$; Rankine/
pencere argümanı $\ell_\omega=\sqrt{V_{bar}^2R/a_0}$ tanımıyla aynen taşınır. Biçim olarak G1'i
üretir; küresel limitte $f_{geo}=1$ (dSph/kovan sonuçlarıyla tutarlı).

**Yan-öngörü sınavı — DESTEKLENMEDİ:** bu mekanizma doğruysa G1'in galaksi-başına kazancı
$f_{geo}$ ile artmalıydı. Ölçüm (141 galaksi; $f_{geo}$ dış-yarı medyanı 0,90–2,74):

- kazanç ~ $f_{geo}$: Spearman $\mathbf{-0{,}005}$ — **korelasyon yok.**
- kazanç ~ kovan kesri: $-0{,}058$ (yönü doğru ama ≈0); saf-disk medyan $+0{,}20$, kovanlı $-0{,}47$.

**Yerelleştirme:** kazanç difüz — her $R/R_{dış}$ kuşağında $+0{,}2$…$0{,}5$ km/s, tek mekanizma
odağı yok; en büyük pay derin kuşakta ($-11$…$-10{,}5$: $+0{,}62$), yüksek-ivme kuşaklarında
hafif negatif.

## 3. Ayrıştırma — kazancın gerçek kaynağı kalibrasyon-kriteri etkileşimi

$k$ taraması (medyan RMS):

| $k$ | P | G1 |
|---|---|---|
| 0,935 | 12,76 | 12,04 |
| 1,038 | 12,48 | 11,71 |
| **1,10** | **11,87** | **11,92** |

**RMS-optimal noktada iki besleme fiilen eşittir** (≈11,9; kesişirler). Resmî kriter (dış-yarı
medyan sapma $=0$ — ilkeli: sıfır dış yanlılık) her forma kendi $k$'sını verince fark doğar
(12,48'e 12,04) ama bu fark **beslemenin temel üstünlüğü değil**, kriterin iki biçimle farklı
etkileşimidir. (Not: $k$'yı RMS için büyütmek dış bölgeyi sistematik fazla-öngörüye iter —
kriter değişikliği önerilmiyor; bu satır yalnız kaynak ayrıştırmasıdır.)

## 4. HÜKÜM (tartışmaya taşınan)

1. **G1'in ölçülen kazanımları gerçektir** (resmî kriter altında RMS 12,04; BTFR norm 0,992;
   Sb–Sbc 18,92) — ama üç bulgu kazancı temel olmaktan çıkarır: $f_{geo}$ imzası yok, kazanç
   difüz, RMS-optimalde eşitlik.
2. **Türetim girişimi bu turda başarısız:** Kelvin/düzlemsel-akı zinciri biçimi üretir ama ayırt
   edici imzası veride yok — aday statüsü verilemez (kayma-hipotezi emsali: kuruldu, sınandı,
   desteklenmedi; kayıt silinmez).
3. **Öneri: P resmî kalır** (türetilmiş pencere; yüksek-z 5/6; dar band; RAR ≈0). G1 bu defterde
   ölçülmüş-alternatif olarak açık durur; meşrulaşmasının tek yolu $f_{geo}$'nun koherens/λ
   fiziğinden, *yan-öngörüleriyle birlikte* türetilmesidir — bugünkü ilk deneme bunu veremedi.
4. Benimseme durumunda gerekecek ek koşumlar (kayıt): $\ell_\omega$ yasası sınavlarının
   (yarıçap artığı, 158-galaksi eğimi, kütle üssü) G1 tanımıyla tekrarı; panellerin/defterlerin
   taşınması; yüksek-z gerilemesinin (5/6→4/6) kabulü.

## 5. Dürüstlük kayıtları

1. G1'in BTFR'si bu defterin v3-konvansiyonlu koşumudur (3,708/0,992); dış notların 3,703/1,005
   sayıları hiçbir boru hattımızda üretilmemiştir ve kullanılmaz.
2. Yan-sınav Spearman'ları tanımlayıcıdır ($n=141$); ama $-0{,}005$'in "imza yok" okuması güç
   analizine dayanmaz — imza olsaydı işaretin görünmemesi için saçılmanın kazancın ~50 katı
   olması gerekirdi; kazanç zaten küçük (0,44 km/s medyan) — bu da "temel değil" okumasını
   destekler.
3. Bu deneme ve türetim girişimi Claude Fable 5 tarafından yapılmıştır; gradyan biçimi iki dış
   notun (Gemini) önerisidir, sayıları alınmamış, biçimi denetimden geçirilmiştir.
