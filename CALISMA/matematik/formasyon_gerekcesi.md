# FORMASYON GEREKÇESİ — Ortam Dolaşımı Neden ~0?

> Çalışma dosyası · 17 Ağustos 2026 (Opus) · `ortam_donusu_kilit_teoremi.md` §6 kalem 1'in kapatılması
> Sınav: `formasyon_gerekcesi_sinavi.py`

---

## Soru

Kilit teoremi dolaşımı **gözlemsel olarak** dışladı (4 gövde). Kohezyon dolaşımın *yokluğunu* **izinli** kılıyor. Ama açısal momentum serbest bir başlangıç koşuludur — teorinin *neden* sıfır olduğunu söylemesi gerekir, yoksa "şanslı başlangıç koşulu" olur.

**Cevap üç bağımsız ayaktan geliyor. İkisi dolaşımı yasaklıyor, biri maddenin onu kuramayacağını gösteriyor.**

---

## AYAK 1 — Diferansiyel dönüş bir denge durumu **değildir**

M-5 kohezyon kanalını **kesme modülü** rolünde kurar (Σ ↔ G_s, v_m = √(Σ/ρ₀) = 10⁴c₀). Kesme modülü olan bir ortam, **kararlı kesme akışını taşıyamaz**: diferansiyel dönüş kesme zorlanması biriktirir, elastik geri-çağırma devreye girer ve sistem **sıfır-kesme durumu etrafında salınır**. Siklostrofik profil w = 2v_yör (Ω ∝ r^{−3/2}, yani şiddetle kesmeli) bu yüzden bir **denge çözümü değildir**.

Salınım periyodu L/v_m:

| Ölçek | L/v_m | Yörünge periyodu / salınım |
|---|---|---|
| Ay yörüngesi | 1,3×10⁻⁴ s | 1,8×10¹⁰ |
| **Merkür yörüngesi** | **0,019 s** | **3,9×10⁸** |
| 1 AU | 0,050 s | 6,3×10⁸ |
| Satürn yörüngesi | 0,48 s | 1,9×10⁹ |
| Galaksi (10 kpc) | 3,3 yıl | 6,7×10⁷ |
| Hubble yarıçapı | **1,37×10⁶ yıl** | 1,0×10⁴ |

**İki sonuç:**
1. **Merkür'ün sekülér apsis ölçümü diferansiyel dönüşü sıfıra ortalar** — yörünge başına 3,9×10⁸ salınım çevrimi. Kilit teoreminin ölçtüğü Ω_sekülér, tanım gereği ⟨w⟩/r = 0.
2. **Hubble ölçeğinde elastik denkleşme süresi 1,37 milyon yıl** — evren yaşının 10⁻⁴'ü. Yani ilksel diferansiyel dönüş, evren yaşının **10⁴ katı önce** elastik olarak silindi. Bu, "şanslı başlangıç koşulu" itirazını kapatır: hangi başlangıç koşulundan başlanırsa başlansın, bugün diferansiyel dönüş yoktur.

---

## AYAK 2 — Katı (rigid) dönüş, sınırsız kohezyonlu ortamda **yasak**

Kesme içermeyen tek dönüş katı dönüştür (Ω = sabit) — Ayak 1 onu dışlamaz. Ama merkezcil gereksinim gerilme ister:

$$\frac{dP}{dr}=\rho_0\Omega^2 r \;\Longrightarrow\; \tau_{gerekli}=\frac{\rho_0\Omega^2r^2}{2}$$

**r ile sınırsız büyür.** Σ'yı aştığı yarıçap:

$$r_{max}=\frac{\sqrt{2\Sigma/\rho_0}}{\Omega}=\frac{\sqrt2\,v_m}{\Omega}$$

| Ω (rad/s) | r_max | R_Hubble ile |
|---|---|---|
| 10⁻⁶ | 137 pc | 3×10⁻⁸ |
| 10⁻¹⁴ | 1,4×10¹⁰ pc | 3,3 |
| 2,3×10⁻¹⁸ (gözlem sınırı) | 6,0×10¹³ pc | 1,4×10⁴ |

**Yapısal sınır** (yırtılma gözlenebilir evrenin içinde olmasın): **|Ω| < 3,26×10⁻¹⁴ rad/s.** Gözlem (2,3×10⁻¹⁸) bundan 1,4×10⁴ kat daha sıkı — yani yapısal argüman doğru yönü verip 4 mertebe kazandırıyor, ama tek başına gözlemi açıklamıyor.

**Sınırsız limit hükmü kesin:** Ortam sınırsızsa (monizm — okyanus gözlenebilir evrenin ötesine uzanır), **her Ω ≠ 0 sonlu bir yarıçapta ortamı yırtar** ⇒ **Ω = 0 tam.** Ve bu yeni bir varsayım değil: **M-7'nin yırtılmama koşulu** (P₀ + Σ > gerilme) zaten kanonda bağlayıcıdır. Katı dönüş, M-7'yi büyük yarıçapta kaçınılmaz olarak ihlal eder.

---

## AYAK 3 — Madde ortamı **döndüremez**

İki bağımsız kanal, ikisi de kapalı:

**(a) Elastik:** maddenin dönme enerji yoğunluğu ile Σ kıyası —

| Sistem | E_dönme/V (Pa) | / Σ |
|---|---|---|
| Güneş (dönme KE) | 1,7×10¹⁴ | **2,8×10⁻²⁸** |
| Jüpiter | 1,5×10¹¹ | 2,4×10⁻³¹ |
| Güneş sistemi yörünge KE | 5,0×10⁴ | 8,3×10⁻³⁸ |
| Galaksi (dönme KE) | 2,4×10⁻¹⁰ | 4,0×10⁻⁵² |

Maddenin elindeki enerji yoğunluğu Σ'nın 10⁻²⁶–10⁻⁵² katı. **Ortamı kesmeye zorlayacak enerji yok.**

**(b) Sürüklenme:** M-43'ün altkritik bastırması ~10²⁸ ⇒ tork kanalı da kapalı.

İki argüman birbirinden bağımsız ve aynı sonucu veriyor: **madde, kendi açısal momentumunu ortama aktaramaz.** Açısal momentum maddede kalır (yıldızın spini + gezegenlerin yörüngeleri) — nitekim gözlenen de bu.

---

## ⭐ BONUS — Mach ilkesi mekanik olarak açıklanıyor

Klasik bulmaca: **yerel eylemsizlik çerçevesi neden uzak yıldızlara göre dönmez?** GR'de bu, kozmolojik madde dağılımından gelen bir uyum sorunudur (Mach ilkesi; Lense–Thirring'in kozmolojik toplamı).

Bu teoride **bedava**: ortam **tek sürekli elastik gövdedir**; kesme rijitliği her yamayı küresel duruma kilitler. Denkleşme süresi L/v_m:
- Güneş sistemi: **5 saniye**
- Galaksi: **3,3 yıl**
- Gözlenebilir evren: **1,37 milyon yıl**

Yani yerel eylemsizlik çerçevesi, uzak maddeyle **elastik olarak kilitlidir** ve kilitlenme süresi kozmolojik ölçekte anlıktır. Mach ilkesi bir postülat ya da uyum değil, kohezyon kanalının sonucudur.

*(Bu, `05_Oturma_Yaricapi` ve `11.3`'ün zarf/çerçeve tartışmalarına bağlanabilir; teorinin "tercihli çerçeve" statüsünün de yeni bir okumasıdır: tercihli çerçeve vardır ama küresel olarak tek ve dönmeyendir.)*

---

## Muhasebe: soru kapandı mı?

| Kalem | Durum |
|---|---|
| Diferansiyel dönüş (siklostrofik w = 2v_yör) | **YASAK** — denge değil; sekülér ortalaması sıfır; ilksel değer 10⁴ denkleşme süresi önce silindi |
| Katı dönüş, sınırsız ortam | **YASAK** — M-7 ihlali; Ω = 0 tam |
| Katı dönüş, Hubble-kesikli ortam | **|Ω| < 3,3×10⁻¹⁴** yapısal; gözlem 1,4×10⁴ kat daha sıkı |
| Maddenin ortamı döndürmesi | **İMKÂNSIZ** — enerji oranı 10⁻²⁸, sürüklenme bastırması 10⁻²⁸ |

**Hüküm: "şanslı başlangıç koşulu" itirazı kapandı.** Dolaşımın yokluğu artık izin verilen bir seçenek değil, üç bağımsız yapısal nedenin sonucudur. Ve gözlemin yapısal sınırdan 10⁴ kat sıkı olması, sınırsız-ortam kolunun (Ω = 0 tam) lehine bir işarettir.

## Kalan açıklar (dürüst kayıt)

1. **⚠️→✅ Kesme salınımının ikinci-mertebe izi — hesaplandı, ve AYAK 3'ü yük taşıyıcı yapıyor.**
   Ayak 1, viskozite ~0 olduğu için diferansiyel dönüşü **söndürmüyor**, yalnız salınıma çeviriyor: ⟨w⟩ = 0 ama **⟨w²⟩ ≠ 0**. Λ_kin |v−w|'ye bağlı olduğundan ⟨w²⟩ ek bir saat terimi üretir: ⟨w²⟩/2c₀².
   **Sönüm hesabı (Kelvin–Voigt, η ≤ 2,3×10⁻¹¹ Pa·s):** 1 AU ölçeğinde τ_sönüm = **5,3×10⁴⁰ yıl**; 10 kpc'de 2,2×10⁵⁹ yıl. Evren yaşının 10³⁰ katı ⇒ **sönüm YOK.** Viskozite kolu kapalı.
   **Kızıla kayma kısıtı:** w_genlik = f·v_yör için terim/(Φ/c₀²) = f²/4. Merkür yörüngesinde:

   | f | w_genlik | terim | Φ/c₀² ile oran |
   |---|---|---|---|
   | 1,0 | 47,9 km/s | 6,4×10⁻⁹ | **0,25** |
   | 0,1 | 4,8 km/s | 6,4×10⁻¹¹ | 2,5×10⁻³ |
   | **0,02** | **957 m/s** | 2,6×10⁻¹² | **10⁻⁴** |

   GPS/Pound–Rebka kızıla kaymayı ~10⁻⁴ bağıl doğruladığından **w_genlik ≤ 0,02 v_yör** (Merkür yörüngesinde ≤ 957 m/s). Tam genlikte (2v_yör) terim Φ/c₀²'nin **kendisi mertebesinde** olur ve kızıla kayma kalibrasyonu çöker.
   **⇒ ÇÖZÜM: salınım hiç uyarılmadı.** Ayak 3 (madde ortamı kesemez: enerji oranı 10⁻²⁸, sürüklenme bastırması 10⁻²⁸) + M-9'un *"homojen arka plan ortamın tek doğal taban durumudur"* teoremi birlikte, **diferansiyel dönüşü hiç var olmamış** kılıyor. Salınacak bir şey yok.
   **Sonuç, yapı açısından önemli:** Ayak 1 tek başına yetmez (sönümsüz salınım kalıntısı bırakır); **Ayak 3 + M-9 yük taşıyıcıdır.** Üç ayağın iş bölümü şudur: Ayak 3 + M-9 kesmenin *hiç doğmadığını*, Ayak 1 *doğsa bile kararlı kalamayacağını*, Ayak 2 katı dönüşün de yasak olduğunu gösterir. Kitaba bu sırayla yazılmalı.
2. **Ortamın uzaysal erimi.** Ayak 2'nin en güçlü kolu (Ω = 0 tam) ortamın sınırsız olmasına dayanıyor. Teorinin monizmi bunu ima ediyor ama kozmolojik erim (Büyük Patlama, S_kozmik kaynak terimi) ile ilişkisi yazılmamış. Hubble-kesikli kolda sonuç 3,3×10⁻¹⁴'te kalıyor.
3. **Galaktik ölçek.** Denkleşme süresi 3,3 yıl olduğundan galaktik ortam da diferansiyel dönemez. Bu, M-37'nin galaktik "ortam kolonu"nu da (madde kolonu değil) dışlar — Tartışma #4'ün galaktik kontrolüyle tutarlı, ama kitapta açıkça yazılmalı.
4. **Σ alt sınırla kullanıldı.** Tüm sayılar Σ ≥ 10⁸P₀ ile; gerçek Σ daha büyükse Ayak 1 ve 3 güçlenir, Ayak 2'nin yapısal sınırı **gevşer** (r_max ∝ v_m). Bu ters yönlü duyarlılık kayda geçmeli.

## Kitaba yazılacaklar
- **Yeni türetim** (M-9'un ekine ya da kilit teoremiyle birlikte tek girdi): üç ayak + Mach sonucu.
- **M-5'e ek:** kesme modülünün ikinci yapısal görevi — diferansiyel dönüşü yasaklamak, yerel eylemsizlik çerçevesini küresel duruma kilitlemek.
- **M-7'ye ek:** yırtılmama koşulunun katı dönüşü de yasakladığı kaydı (Ω = 0 tam, sınırsız ortamda).
- **Mach ilkesi:** Kısım 7'nin "modern fiziğin açık krizleri" bölümüne aday — GR'de uyum sorunu, burada kohezyonun bedava sonucu.
