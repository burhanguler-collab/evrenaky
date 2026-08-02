# Besleme sınavı — F4'ün kaynağı: $M_{kaps}$ mı, yerel $g_{bar}$ mı? (iş 4)

**Kaynak ve denetim kaydı:** Dış bir not (Gemini/Antigravity IDE çıktısı, kullanıcının ilettiği
`MOND_Eritilmis_Evrenaki.md`) resmî denklemin iki okumasının ayrıştığını ve verinin
$g_{bar}$-beslemeyi tercih ettiğini iddia etti. İddia **teorinin kendi boru hattından geçirildi**
(`../../besleme_sinavi.py`; 94'ün veri/konvansiyon kuralları birebir: $\Upsilon_*=0{,}50$, kovan
0,70, aynı 141 galaksi, aynı RMS tanımı; $a_0$ nihai $=7{,}39\times10^{-11}$).
Çıktı: [`SONUC_BESLEME.csv`](SONUC_BESLEME.csv).

## 1. Yapısal tespit — "eşdeğer yerel yazım" sayısal olarak eşdeğer değil

Resmî denklemin ikinci terimi $\sqrt{\mathcal{G}M_{kaps}(R)\,a_0}$'dır ($M_{kaps}$: fotometrik
kümülatif yıldız kütlesi + gazın kendi katkısı). "Eşdeğer yerel yazım" $a_{F4}=\sqrt{a_{F1}a_0}$
ise F4'ü $g_{bar}=V_{bar}^2/R$'den besler. Küresel simetride ikisi özdeştir; **yassı diskte
$V_{bar}^2\neq\mathcal{G}M_{kaps}/R$** (disk geometrisi) olduğundan ayrışırlar. Kitap 6.5.4.4 bu
ikisini tek yazım sayıyordu; dahası kendi defterimizde de ikili kullanım vardı: dönüş eğrisi/BTFR
sınavları $M_{kaps}$-beslemeyle, **95_RAR ise $g_{bar}$-beslemeyle** koşulmuştu. Bu tespit,
sayılardan bağımsız olarak kalıcıdır ve kitaba şerh düşülmüştür (6.5.4.4).

## 2. Ölçümler (141 galaksi; galaksi başına fit yok)

**B** = resmî ($M_{kaps}$) · **D** = $g_{bar}$-besleme · **M** = MOND (McGaugh fitli eğrisi,
$g_\dagger=1{,}2\times10^{-10}$):

| Ölçü | B | D | M |
|---|---|---|---|
| Genel medyan RMS (km/s), ortak $a_0$ | 12,79 | **12,04** | 11,59 |
| Genel medyan RMS, **eşit-kriter kalibrasyonla** (dış-yarı medyan sapma = 0) | 12,79 | **12,54** ($a_0^D=6{,}5\times10^{-11}$, $k=0{,}88$) | — ($g_\dagger$ zaten fitli) |
| Dış-yarı sapma medyanı (ortak $a_0$) | −0,1 % | +1,9 % | +4,4 % |
| Galaksi başına en düşük RMS | 45 | 31 | **65** |
| RAR biçim eğimi (rotmod noktaları, $n=2995$) | −0,043 | −0,033 | +0,027 |

Sınıf kırılımı `SONUC_BESLEME.csv`'dedir (dış notun RMS tablosu birebir yeniden üretildi —
hesabı doğruymuş; B'nin −0,1'lik dış sapması, nihai $a_0$ kalibrasyonunun tutarlılık denetimidir ✓).

## 3. Hüküm

1. **Ayrışma gerçek, tercih zayıf.** $g_{bar}$-besleme RMS'te öndedir ama avantajın yarısından
   fazlası kalibrasyon kayırmasıydı: $a_0$, B'nin dış sapmasını sıfırlayacak şekilde seçilmişti;
   aynı kriter D'ye uygulanınca fark 0,75'ten **0,25 km/s'ye** düşer. Yön korunur, kanıt gücü
   düşüktür.
2. **Biçim borcunu hiçbir besleme kapatmıyor.** Rotmod noktalarında eğimler: B −0,043, D −0,033 —
   D marjinal olarak daha düz, ama sıfır değil. Toplanma/besleme türetimi (7.4-12h; 95_RAR iş 1)
   tek adres olmaya devam ediyor; artık ölçülmüş bir hedefi var: doğru türetim hem beslemeyi
   seçmeli hem eğimi sıfıra çekmeli.
3. **MOND'un fitli eğrisi RMS'te hâlâ önde** (65/141) — dış not bunu vurgulamamıştı; saklanmaz.
   Bilinen geçiş-biçimi borcuyla tutarlıdır.
4. **DÜZELTİLMİŞ KAYIT — veri-seti uyuşmazlığı yoktu, konvansiyon farkı vardı.** Bu maddenin
   ilk hâli 95_RAR'ın +0,051'i ile buradaki −0,033'ü "zıt işaret" saymıştı. Yanlış: 95'in
   artığı **öngörü−gözlem**, buradaki **gözlem−öngörü** yönündedir (95'in derin kuşağında
   −0,197 dex artıkla ×2,86 çarpanın birlikte durması ancak öngörü−gözlemle mümkündür).
   Ortak konvansiyonda iki veri ürünü **aynı yöndedir**: derin uçta eksik, Newton yakasında
   fazla öngörü (RAR.mrt −0,051 ↔ rotmod −0,033, gözlem−öngörü). Kalan yalnız büyüklük
   farkıdır (nokta kümesi/kalite kesimi) ve biçim borcunun varlığını değiştirmez.

## 4. Dış nottan neyin alındığı, neyin alınmadığı

| Alındı (denetimden geçti) | Alınmadı (ve nedeni) |
|---|---|
| İki beslemenin ayrıştığı yapısal tespiti + RMS tablosu (birebir yeniden üretildi) | BTFR iddiaları (Orijinal 3,699/0,972 — 97'nin kayıtlı 3,734/0,984'üyle çelişiyor; yeniden üretilmedi) |
| Besleme sorusunun toplanma-biçimi borcuna bağlanması | "Kusursuz 1,005" dili (kalibrasyon kayırması hesaba katılmamış) |
| — | "Karanlık madde etkisi / karanlık kütle itimi (F4)" çerçevesi (teoriyle bağdaşmaz: F4 eksenel itimdir, karanlık madde envanteri yoktur) ve teori sesinde "kütleçekim" |
| — | "Gözlemcilere oynamak için Melted sürülebilir" hükmü (vitrin tercihi değil türetim sorusu) |

## 5. Dürüstlük kayıtları

1. Eşit-kriter kalibrasyonu **medyan dış sapmayı** sıfırlar (nihai $a_0$'ın kriteri); RMS-optimal
   kriter değildir — D için RMS-optimal $a_0$ aransaydı fark yine küçülür ama tablo "fitli" hâle
   gelirdi, aranmadı.
2. RAR eğimleri EKK doğrusudur ve noktalar galaksi içinde bağımsız değildir (95_RAR md. 7.1'in
   uyarısı burada da geçerli); eğimlerin mutlak değerleri değil **sıralaması** kullanılmıştır.
3. MOND satırı galaksi başına parametresizdir ama $g_\dagger$ literatürde aynı SPARC ailesine
   fitlidir; bizim $a_0$ da öyle. "Sıfır parametre" iki taraf için de yalnız *galaksi başına*
   doğrudur.
4. Bu sınav Claude Fable 5 tarafından, dış notun iddiasını denetlemek için koşulmuştur; dış not
   kaynak olarak anılır, hiçbir sayısı doğrudan alınmamıştır.
