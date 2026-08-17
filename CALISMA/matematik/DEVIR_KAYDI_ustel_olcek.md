# DEVİR KAYDI — Üstel Ölçek Yapısı (Λ = e^{−Φ/c₀²})

**Tarih:** 17 Ağustos 2026 · **Oturum:** Fable 5 (limit doldu) → Opus 5 devraldı
**Amaç:** Sonraki oturum bu konuşmayı hiç görmemiş olarak devralabilsin. Hiçbir şey ima edilmedi.
**Kitap metnine bu konuda HİÇBİR DEĞİŞİKLİK YAPILMADI.** (Bkz. §7 — yalnız jeodetik düzeltmeleri, ayrı iş, uygulandı.)

---

## 1. Tek paragrafta ne oldu

Kitabın iki ayrı açık kalemi — **Merkür'ün 43″/yy günberi kayması** (7.4 md.14, "GR'ın klasik sınavları karşısındaki kalan tek boşluk") ve **karadeliğin GR'dan ödünç alınmış eşiği** (M_min'in Schwarzschild yarıçapını girdi alması) — aynı kökten çıktı: M-46'nın **lineer** deplasman yanıtı P = P₀ − Cχ. Bu yanıt küçük-deplasman kesitidir. Yerel-referanslı (Postülat 4 uyumlu) hâli üstel verir:

$$\frac{dP}{d\chi} = -C\frac{P}{P_0} \;\Longrightarrow\; P = P_0e^{-C\chi/P_0} = P_0e^{-4\mathcal{G}M/c_0^2r},\qquad \Lambda = e^{-\Phi/c_0^2}$$

χ'nin Poisson denklemi (M-46) ve P₀ (M-8) **değişmiyor**; **sıfır yeni serbest parametre**. M-42'nin Λ = 1−Φ/c₀² yazımı bunun birinci mertebe kesimi olarak yeniden konumlanıyor; M-42'nin tüm yapısal ilişkileri (ℓ,f ∝ Λ; c_loc = c₀Λ²; n_eff = 1/Λ²; yerel Lorentz null) **aynen** geçerli. Merkür kapanıyor (0,69σ), lineer yazım gözlemle **eleniyor** (7960σ).

**Ama üç ciddi kayıt var** (§4): (i) türetimin ilk gerekçesi (K=P) çürütüldü, yerine iki daha güçlü gerekçe geçti; (ii) Merkür'ü kapatan şey üstel basınç profili *tek başına* değil, eylemin hız-bağımlı terimleridir; (iii) **ortamın dönme durumu açık kalemi**, sonucun tamamını taşıyor.

---

## 2. Üretilen dosyalar (hepsi `websitesi\CALISMA\matematik\`)

**Kayıt/analiz:**
| Dosya | İçerik |
|---|---|
| `tartısma_matematik` | Ana defter. **Tartışma #3** = çözüm; **Tartışma #3 DÜZELTME EKİ** (en üstte) = denetim sonrası ölçekleme. Tartışma #1 = GR kalıntı denetimi, #2 = karadelik problemi. |
| `ustel_turetim_uc_yol.md` | Türetim yolları. ⚠️ **Yol 3 (entalpi) HATALI — bkz. §4c.** |
| `KITAP_DUZENLEME_PLANI_ustel.md` | 10 maddelik ilk düzenleme planı (denetim öncesi; §6'nın tam listesiyle güncellenmeli) |
| `karadelik_cozum_calismasi.md` | *(yazılmadı — ajan oturum limitine takıldı; içeriği Tartışma #2 + #3 ekinde)* |
| `denetim_raporlari\01..08` | **8 denetim ajanının tam raporları** (UTF-8). Kritik olanlar: `04_lambda_yayginlik` (185 Λ vuruşunun A/B/C sınıflaması + tam dosya:satır listesi), `08_bagimsiz_bes_yol` (beş türetim yolu), `06/07_curutme_*` (düşmanca denetim) |
| **`M51_M54_TASLAK_ortam_hiz_alani.md`** | **⭐ TAŞIMAYA HAZIR KİTAP GİRDİLERİ** — ortamın hız alanı sonuçlarının dördü, kitabın kendi şablonuyla yazılmış: **M-51** Ortamın Statik Dengesi (+Σ'nın yapısal görevi) · **M-52** Ortam Dönüşü Kilit Teoremi · **M-53** Dolaşımın Yokluğunun Türetimi (üç ayak) · **M-54** Mach Sonucu. Sonunda **taşıma partisi kontrol listesi** (13 düzeltilecek satır + dokunulmayacaklar). Blok yerleşimi: Blok B'nin devamı. **Numara kararı bekliyor:** üstel yapı girdisi için M-55 önerildi. |
| `ortam_hiz_alani_cozumu.md` · `ortam_donusu_kilit_teoremi.md` · `es_duzlemlilik_cozumu.md` · `formasyon_gerekcesi.md` | Dört sonucun çalışma dosyaları (türetim ayrıntısı, açık kalemler, kitapta düzeltilecekler) |

**Sınav betikleri (hepsi koşuldu, sonuçları §3'te):**
| Betik | Ne sınar |
|---|---|
| `karadelik_gunberi_mp.py` | **Merkür günberi, mpmath 60 hane** — ana sonuç |
| `karadelik_yorunge_sinavi.py` | PPN β/γ okuması, iç tutarlılık, ufuk, gölge |
| `karadelik_ustel_profil_sinavi.py` | Foton küresi/gölge, ışın izleme, M_min |
| `ustel_isik_sinavi.py` | Işık bükülmesi + Shapiro tam Fermat integrali, Sgr A*/M87* gölge (µas) |
| `ustel_turetim_sinavi.py` | β = 2n−1 ailesi, çarpımsal bileşim, ikinci-mertebe belirsizliği |
| `ortam_dolasimi_mp.py` | ⚠️ **Ortam dolaşımı sınavı** — en kritik açık kalemin niceliği |
| `karadelik_gunberi_sinavi.py`, `ortam_dolasimi_sinavi.py` | float64 sürümler — **koşullanma nedeniyle güvenilmez, mpmath sürümlerini kullan** |

---

## 3. Doğrulanmış sayısal sonuçlar

| Nicelik | Üstel | Lineer (mevcut kitap) | Gözlem / GR | Kaynak |
|---|---|---|---|---|
| **Merkür günberi** | **42,9805″/yy** | 50,1439″/yy | 42,9799±0,0009 → **0,69σ** / lineer **7960σ** | `karadelik_gunberi_mp.py` |
| Venüs/Dünya/Mars/Ikaros | oran 1,0000001 | oran 7/6 tam | GR | aynı |
| PPN | **γ=1, β=1** | γ=1, β=½ | Cassini, LLR | `karadelik_yorunge_sinavi.py` |
| Nordtvedt η_N | 0 (tam) | −2 | LLR \|η_N\|<4,5×10⁻⁴ | `07_curutme_beta` |
| Işık bükülmesi (tam integral) | 1,7512″ | — | GR'dan fark 7,3×10⁻⁷″ ⇒ korunur | `ustel_isik_sinavi.py` |
| Shapiro (tam integral) | 247,244 µs | — | kitabın kaydı 247 µs | aynı |
| Jeodetik | 6.606 mas/yıl | aynı | GP-B 6.601,8±18,3 (holonomi 1. mertebe, korunur) | `04_lambda_yayginlik` A-177 |
| Gölge b_krit | **2eμ = 5,4366μ** | +%29,9 (Λ=1−x) veya +%100 (P-doğrusal) | GR 3√3μ = 5,1962μ ⇒ **+%4,63** | `karadelik_ustel_profil_sinavi.py` |
| Gölge Sgr A* / M87* | 55,73 / 41,53 µas | — | GR 53,27 / 39,70; EHT 51,8±2,3 / 42±3 → 1,04σ / 0,65σ | `ustel_isik_sinavi.py` |
| Ufuk | **yok** (e^{−μ/r} sıfırlanmaz) | r_c=4μ'de P<0 | GR: R_s'de z→∞ | analitik |
| Kızıla kayma r=2μ | 1+z = 1,65 (sonlu) | — | GR ∞ ⇒ **kategorik ayrım** | aynı |
| M_min | 8,26 M☉ (**gölge eşiği**) | 8,3 (ufuk eşiği) | LIGO kütle boşluğu | `karadelik_ustel_profil_sinavi.py` |
| Tepki üssü kilidi | n = 1,000000 ± 3,1×10⁻⁵ | — | Merkür hassasiyeti | `ustel_turetim_sinavi.py` |

**Kalibrasyon zinciri korunuyor:** ΔP_yüzey = ρₙΦ (oran 0,9999999986) · δc/c₀ = −2Φ/c₀² (oran 0,9999999993) · P₀ = ¼ρₙc₀² = 6,07×10³³ Pa **değişmez**.
**Denetimin hükmü:** hiçbir A-sınıfı ilişki kırılmıyor; Kısım 5 (deneyler) ve Kısım 10 (galaktik/a₀) Λ'yı hiç kullanmıyor — **üstel geçiş oralara dokunmuyor**. Galaktik alanda üstel/lineer farkı ~10⁻¹²; 163 galaksi fiti aynen ayakta.

---

## 4. TÜRETİMİN STATÜSÜ — dürüst kayıt (en önemli bölüm)

### 4a · ÇÜRÜTÜLEN: "stiff ortamda K = P" gerekçesi
İlk gerekçe *"stiff ortamda hacim modülü basıncın kendisidir (K = ρc² = P), dolayısıyla tepki çarpımsaldır"* idi. **İki bağımsız düşmanca ajan bunu çürüttü:**
1. Deplasman kanalında M-44 `(∂P/∂ρ)_χ = c₀²` yazıyor — **sabit**. Dolayısıyla K = ρ₀c₀² = P₀, kuyunun her yerinde aynı; K ile P derin kuyuda e^{4Φ/c₀²} kadar ayrışır.
2. **Kategori hatası:** K, dP'yi hacimsel zorlanmaya (dV/V) bağlar; deplasman kanalında dV/V = 0 (k=0). K bu kanalda hiçbir şeyin katsayısı değildir — M-44'ün varlık nedeni olan iki-kısmi-türev ayrımının ihlali.
3. Argüman ciddiye alınırsa stiff hidrostatik denge P = P₀e^{−Φ/c₀²} verir: üs **1** ve k=1 (M-8'i öldürür). Öneri üs **4** kullanıyor.
**⇒ Bu gerekçe kitaba yazılmamalı.**

### 4b · YERİNE GEÇEN İKİ GEREKÇE (daha güçlü)
**(i) Postülat 4 / form-değişmezlik (teklik).** n ≠ 1 ise yasa mutlak bir basınç ölçeği (P₀) açıkça taşımak zorundadır; Postülat 4 P₀, ρ₀, c₀'ı **yerel** ilan eder ⇒ yasada mutlak ölçek görünemez. Form-değişmezlik testi F(u₀+u₁) = F(u₀)F(u₁): yalnız n=1 sağlıyor (ihlal 1,3×10⁻⁵¹ ↔ n=0 için 2×10⁻⁷). Tek öncül Postülat 4 + χ toplamsallığı; **hiçbir maddesel varsayım yok**. *(Not: bu, benim "çarpımsal ölçek bileşimi" argümanımla matematiksel olarak AYNI teorem — ikisi iki bağımsız kanıt sayılmamalı.)*
**(ii) GW170817 gözlemsel kilidi — Merkür'den bağımsız ve çok daha sert.** İki ajan bunu birbirinden bağımsız buldu (biri eylemden, biri Maxwell çapraz-türev koşulundan):
- Lineer biçim eyleme yazıldığında dalga kanalının hızı √((∂P/∂ρ)_χ) = c₀'da **donar**, ışık ise c_loc = c₀Λ²'ye düşer ⇒ ikisi ayrışır. İhlal: Dünya yüzeyi 1,4×10⁻⁹ · **Samanyolu potansiyeli 8,9×10⁻⁷** · Güneş yüzeyi 4,2×10⁻⁶ · nötron yıldızı 0,33. GW170817 kısıtı **4,2×10⁻¹⁶** ⇒ lineer okuma **~9 mertebe ihlal**.
- Üstel biçimde (∂P/∂ρ)_χ = P/ρ = c_loc² **her noktada** ⇒ GW ve Zerre aynı yerel hızı paylaşır, ihlal **özdeş sıfır**.
- ⇒ **Üstel, M-44'ün "GW170817 otomatik sağlanır" iddiasını gerçekten otomatik yapan tek biçimdir.** Bu aynı zamanda kitapta **kayıtlı olmayan bir iç tutarsızlığın** düzeltmesidir (M-44/M-9 "tam c₀" ↔ M-42 "c_loc = c₀Λ²").
- Kitabın kendi cümlesi bunu destekliyor (`Kisim_6\02_...:11`): *"Kavrama Yasası c₀=√(P/ρ) yayılma hızının kendisidir ve değişmeden korunur"* — üstel bu cümleyi **tam** yapar, lineer O(Φ²)'de bozar.

### 4c · HATALI ÇALIŞMA NOTU — düzeltilmeli
`ustel_turetim_uc_yol.md`'nin **Yol 3 (stiff entalpi)** yolu **yanlıştır**: h = c₀²ln(P/P₀) **ρ-kanalının** entalpisidir (orada ρ = P/c₀² değişir); kuyu profili ise **deplasman kanalıdır** (ρ sabit, χ değişir). İki kanalı karıştırmak, M-44'ün *"Deplasman Bağıntısı Bir Hâl Denklemi Değildir"* hükmünün ihlali. Deplasman kanalında h ∝ P özdeş olduğundan bu yol **hiçbir ayrım üretmiyor**. **Kitaba taşınmamalı.**

### 4d · Merkür'ü kapatan şey ne DEĞİL
- **Saf M-2 (a = −∇P/ρₙ), üstel profille bile, TERS işaret veriyor: −28,65″/yy = −⅔ × GR.**
- Doğru sonuç yalnız tam eylemden: S = −mc₀²∫Λ_grav√(1−V²/c_loc²)dt.
- Ayrışım: **−0,667 (M-2 statik kanalı) + 1,667 (hız-bağımlı terimler) = 1,000 × GR.** 43″'nin %167'si M-2'de olmayan terimlerden.
- **M-2'nin kapsamı yeniden yazılmalı:** arka plan koordinat biçiminde **statik limit**tir; hareketli cisim için tek başına yetersiz.
- **"SINAV C tam eşleşme (oran 1,0000000000)" bir KİMLİKTİR, delil değil.** P = P₀Λ⁴ verildiğinde her iki yol −c₀²Λ³Λ′ verir — **her Λ için** (5 farklı Λ ile doğrulandı). Delil listesinden çıkarılmalı; "üs muhasebesi denetimi" olarak etiketlenebilir.
- **Merkür üstel biçimi SEÇMİYOR, yalnız κ=1 (β=1)'i sınıyor.** GR'ın izotropik ölçeği de κ=1'dir ve **ufku vardır**. x³ katsayısı 100'e kadar ayırt edilemiyor. "Ufuk yok" bir **ekstrapolasyondur** — dayanağı Postülat 4 form-değişmezliği + GW170817 kilidi, Merkür değil.

---

## 5. ✅ ORTAMIN DÖNME DURUMU — **ÇÖZÜLDÜ** (17 Ağu 2026, aynı gün)

> Tam analiz: `ortam_hiz_alani_cozumu.md` · Sınav: `ortam_hiz_alani_sinavi.py` · Defter: Tartışma #4

**Çözüm tek satırda:** M-9 gerekçesini **Euler denklemine** dayandırıyor; Euler **kohezyonsuz** akışkanın denklemidir. Teorinin ortamı kohezyonludur (M-4: Σ; M-5: Σ kesme modülü rolünde, Σ/P₀ > 10⁸), dolayısıyla kuyuyu **dolaşmadan, statik elastik dengede** tutabilir:
$$\frac{d\tau_{rr}}{dr}+\frac{3\tau_{rr}}{r}=\frac{dP}{dr}\;\Longrightarrow\;\tau_{rr}=\frac{\rho_n\Phi}{2}=\frac{\Delta P}{2}$$
τ/Σ = **5,1×10⁻¹⁶** (Merkür yörüngesi) — 14–15 mertebe marj; nötron yıldızı yüzeyinde dahi 3,4×10⁻⁹. **Dolaşım zorunluluk değil, serbest dinamik durum; kohezyon farkı kapatır; gözlem statik kolu seçer.**

**Madde kohezyonu görmüyor:** M-2 deplase edilen **hacme** (skaler ⇒ gerilme tensörünün **izine**) bağlanır; τ **izsizdir** ⇒ çiftlenmez. M-2 aynen geçerli.

**Çerçeve sorusu — iç içe zarf yapısı çözdü:** Güneş'in galaktik Hill yarıçapı 1,225 pc = 2,53×10⁵ AU (tüm sistem içeride) ⇒ ortam Güneş çerçevesinde durgun. Dünya'nın Hill yarıçapı 234,9 R_⊕ — kitabın kendi 235 R_⊕ değeriyle birebir ✓. GPS (4,17 R_⊕) Dünya zarfı içinde ⇒ −7 µs/gün ✓; Merkür Güneş zarfı içinde/kendi zarfı dışında ⇒ 42,98″ ✓. **İki hesabı birden doğru veren yapı.**

**✅ Galaktik zincir kontrolü yapıldı, temiz:** M-37'de madde profili (gözlenen dönüş eğrisi) yalnız M-2 + akı geometrisinden çıkıyor (`18_5:265`); ortam dolaşımı ayrı kol ve kitabın kendi cümlesiyle *"görünmez olduğu için ölçülmemiştir"* (`:280`). Düz dönüş eğrisi/a₀/163 galaksi fiti **etkilenmiyor**.

**KAZANÇ:** Merkür günberi = **ortam dönüşünün en hassas ölçümü**; |Ω_ortam| ≤ 1,4×10⁻¹⁸ rad/s (v_φ ≤ 81 nm/s; bir tur 1,4×10¹¹ yıl = evren yaşının 10 katı). GR'de karşılığı yok.

**Kitapta düzeltilecekler:** M-9 Geçerlilik Sınırı (*"madde düşer, ortam dolaşır"* → **"ortam gerilir"**) · M-9 Açık Uçlar (kohezyon/dolaşım bölüşümü) · M-37 statüsü (kohezyonsuz üst sınır) · M-22 varsayımı (opsiyonel durum) · M-2'ye iz/izsiz notu · 11.4.8.1'e "ambiyans ortam" netleştirmesi · KARNE'ye Ω_ortam sınavı.
**Kalan:** eş-düzlemlilik/prograd anlatısının dolaşımsız kurulması (F5 adayı, **doğrulanmadı**) · zarf kayma tabakası yitim/tork (eski kalem) · statik çözümün C/r³ kolu.

---

### (Aşağıdaki bölüm problemin ilk tespitidir — tarihsel kayıt olarak bırakıldı)
## 5-ESKİ. ⚠️ EN CİDDİ AÇIK KALEM — ortamın dönme durumu

Λ_kin'deki V, **yerel ortama göre** hızdır (11.4.8.1'in açık ifadesi). Hesap ortamı Güneş çerçevesinde **durgun** aldı. Ama teorinin kendi yapısı ortamın dolaştığını söylüyor:
- M-9 siklostrofik denge ∇P/ρ₀ = v_θ²/r, ρₙ/ρ₀ = 4 (M-8) ⇒ **v_θ = 2v_yör tam** (oran √(ρₙ/ρ₀) = 2,000, her r'de; M-37 profil teoremi de aynı). Bağımsız ajan da türetti.
- Merkür yörüngesinde ortam **95,74 km/s**; 1 AU'da 59,57 km/s; Dünya yüzeyinde 15,82 km/s.

**Nicel sonuç** (`ortam_dolasimi_mp.py`, mpmath 60 hane; w=0 kontrolü 42,9805 ✓):

| Ortam durumu | Merkür presesyonu | Sapma |
|---|---|---|
| w = 0 | 42,9805″/yy | 0,69σ ✓ |
| w = 1 m/s | 11.283,5″/yy | 1,2×10⁷σ |
| w = 2v_yör (M-9'un kendi dengesi) | 1,15×10⁹″/yy | 1,3×10¹²σ |

**Fizik:** dönen ortamda apsisler ortamla **sürüklenir**; sürüklenme hızı tam olarak ortamın açısal hızıdır (Ω_m = w/r). Gözlem yer bırakmıyor: **|Ω_ortam| ≲ 1,4×10⁻¹⁸ rad/s** (Güneş spininin 3×10⁻⁶'sı), yani v_φ ≲ 8×10⁻⁸ m/s.

**Bu bir çürütme değil, görünür hâle gelmiş ESKİ bir borç:** teorinin mevcut dinamiği (M-2) hiç w içermediği için gerilim doğmamıştı. Aynı sessiz varsayım **GPS'in kinematik teriminde de** kullanılıyor (−7 µs/gün). "Ortam merkezî cismin çerçevesinde durgundur" varsayımı kitapta baştan beri var, yazılmamış, şimdi nicelleşti.

**Çözüm adayları (hiçbiri yazılmadı):**
1. M-9'un dolaşımını kapsamla sınırlamak (galaktik makro-vorteks ↔ gezegen ölçeği).
2. M-43'ün altkritik ayrışması (10²⁸ bastırma) gereği yörüngenin ortamın kütle akışına bağlanmaması; saat yalnız |v−w|'nin **büyüklüğünü** görür — dikkat: |v−2v| = |v| olduğundan **saat terimi zaten etkilenmiyor**, bozulan yalnız dinamik çapraz terim.
3. Postülat 7'nin sürüklenme zarfı (Hill yarıçapı) ile perdeleme.
4. Bağımsız ajanın bulgusu: ortam dolaşımı **dönüşsüz olamaz** (dönüşsüz kol P = P₀ − A/r² ve kuvvet 1/r³ verip M-46/M-35 ile çelişir, dışlanıyor) — vortisite kaynağı χ'dir.

**Yan öngörü (yeni, ayrı iş):** 1 AU'da 59,57 km/s ortam dolaşımının gözlemsel imzası ve zarf perdelemesiyle uzlaştırılması.

---

## 6. Kitaba yapılacak düzenlemeler — TAM liste (HİÇBİRİ YAPILMADI)

Kaynak: `denetim_raporlari\04_lambda_yayginlik.md` (185 Λ vuruşu, 29 dosya, A/B/C sınıflı tam liste) + `01_envanter_ve_karne.md`.

**C sınıfı — gerçek fizik/yeniden yazım (22 kalem, kritik olanlar):**
| # | Yer | İşlem |
|---|---|---|
| C-16 | `19_Ek_M_Blok_I:26,40,42` | **M-44 Adım 2 yeniden yazılmalı:** kutulu sonuç `v_ses = c_loc = √(P/ρ)`; "tam c₀" iddiası düşer; GW170817 "ortak c_loc" gerekçesine geçer. Bağlı: `19:17,213`, `08_Sembol:11 (R-3)`, `07_Matematiksel_Ekler:17` |
| C-4 | `18_5:1367–1371` | **"Yapısal sınır" tezi silinmeli** (çürütüldü); yerine üstel türetim + eylem kaydı |
| C-15 | `19_Ek_M_Blok_I:204,211,217,225` | M-46 çekirdeği: `(∂P/∂χ)_ρ = −C` → **−C(P/P₀)**; `P = P₀ − Cχ` → **P₀e^{−Cχ/P₀}**; `:208–210` Poisson **DEĞİŞMEZ** vurgulanmalı; `:225` "güçlü-alan yazılmamıştır" → yazıldı |
| C-19 | `08_Sembol:130, 217 (S-28)`, `10_Blok_B:54`, `17_Ek_B:29` | **Φ tanımı kararı.** Önerilen (b): **Φ ≡ −(c₀²/4)ln(P/P₀)** — hem Φ = 𝒢M/r'yi hem Λ = e^{−Φ/c₀²}'yi tam yapar, zayıf alanda eski tanıma iner. Φ_it = −Φ korunur. *(17 Ağu Φ kararına dokunur)* |
| C-20 | `Kisim_11\03_Kutle_Spin...:200,1006,1014,1021,1022,1623,1805,1856,1858,1916` + SVG `53,459,1268,1694,1734` | **"Ufuk" dili → "gölge/foton-küresi" dili.** Sayısal hiçbir şey değişmiyor (2μ = R_s birebir): 290 nesne tavanı, R4 rejimi, 918↔898 oranı, a*≤1 (2.527 pulsar) **aynen ayakta**. `:857`'de a*≤1'in gerekçesi Kerr'den kavrama/kilitli-kafese bağlanmalı |
| C-8 | `18_5:1173–1179` | M_min: `R_ρ = R_s` → `R_ρ = r_ph = 2μ`; sayı aynı (8,26), anlam **gölge eşiği**; "karadelik oluşamaz" → "gölge oluşamaz" |
| C-22 | `Kisim_11\04_Saturn:910`, `00_KARNE:264`, `Kisim_3\04:292,308` | Λ_kin kutusunda **c_loc açıkça yazılmalı**: √(1−V²/c_loc²). c₀ yazılırsa yörünge denklemi bozulur |
| C-1,2,3,6,7 | `18_5:1356,1357,1362,1365,1651,1693` | Merkür/β kalemleri **kapandı** kaydına; "ayırt edicilik β'da" → **güçlü alanda** |
| C-9,10,13,14 | `Kisim_6\03:178`, `Kisim_7\04:165,167,169`, `Kisim_4\02:63,99` | "kalan tek boşluk" ifadeleri kaldırılmalı. `Kisim_4\02:99`'daki **r_ISCO ve kritik dönüş limitleri** üstel yapıda **yeniden hesaplanmalı** (yapılmadı) |
| C-11,12 | `Kisim_7\04:119,193`, `19:167,355` | λ'nın Λ bağımlılığı kapatılabilir (λ ∝ e^{−Φ/c₀²}); **γ_ℓ = −1 açık kalır** (daraltılarak yeniden yazılmalı) |
| C-21 | `Kisim_11\04_Saturn:937(ii),1367` | "Λ_grav·Λ_kin birlikte büyük — hesaplanmamıştır" → **hesaplandı**, kalem (ii) kapanır; (i) M→1 ve (iii) tercihli çerçeve açık |
| C-5,17,18 | `18_5:1346–1352`, `19:243,268` | P₀ zinciri "birinci mertebe" notu + tam biçim; M-46'nın **dokuz eleme yolu aynen ayakta** (öncül χ'nin 1/r'si, P'nin doğrusallığı değil) |

**B sınıfı — 36 vuruş, mekanik:** `Λ ≡ e^{−Φ/c₀²}` (tam) + `= 1 − Φ/c₀² + O(Φ²/c₀⁴)` notu. Tam dosya:satır listesi `04_lambda_yayginlik.md` B tablosunda (ana tanım evi `18_5:1292`; ayrıca `08_Sembol:15 (R-10), 87, 200 (S-11), 217 (S-28)`, `Kisim_2\04:43`, `Kisim_1\06:55,81`, `Kisim_4\02:55,81`, `Kisim_4\03:19`, `Kisim_6\02:8,37,79`, `Kisim_6\03:174`, `Kisim_6\05:1287`, `Kisim_6\98:11`, `13_Blok_E:68,91,124,134`, `10_Blok_B:55`, `17_Ek_B:29`, `07_Matematiksel:16`, `Kisim_11\04:874,910`, `00_KARNE:264`, `Kisim_7\04:127,165`).

**A sınıfı (~%80): işlem gerekmez** — yapısal ilişkiler her mertebede korunuyor.

**Yeni girdi:** **M-51 veya M-52 · Üstel Ölçek Yapısı** — rozet **[T (yapı) / S (n=1 gözlemsel kilit)]**, Blok I'e M-46'dan sonra. İskeleti `denetim_raporlari\08_bagimsiz_bes_yol.md` sonunda hazır (7 adım). ⚠️ **Numara çakışması:** M-51 jeodetik için ayrılmıştı (bkz. §7) — biri M-51, diğeri M-52 olmalı.

**Envanter:** yeni parametre **sıfır**; Ek C'de rozet değişimi **yok** (β'nın ve Λ'nın Ek C satırı yok). Bilanço **+0/−1**. Ek C.1'in "5 skaler + 2 profil" sayımı değişmez.
**KARNE:** güncellenecek `25–27, 46 (S-5), 70, 93, 135, 264, 292–295`; yeni satırlar **S-12 gölge çapı** (dürüstlük şartı: bugünkü EHT sistematiği ~%10, +%4,63'ü **ayırt etmez** — "koşulabilir ama bugün karar vermez") ve **S-13 ufuk yokluğu/sonlu kızıla kayma**.
**Bedava toplanacak önceden var olan bozukluklar:** atıf hatası "7.4 md.12" → **md.14** (`18_5:1371,1693`, `Kisim_6\03:178`, `Kisim_4\02:63`); **β beş anlamda** kullanılıyor, PPN β sözlükte kayıtlı değil ⇒ **β_PPN** ayrı sembol + S-29; halka kalınlığı Λ ⇒ **Λ_h** indislenmeli.

---

## 7. Bu oturumda kitapta YAPILAN değişiklikler (üstelden ayrı işler)

**Jeodetik presesyon** (Tartışma #2 öncesi karar) — `18_5_Kuvvet_Matematigi.md`: `:1264` işaretçi · Kapanan Gözlemler tablosu altına **"Jeodetik satırının mekanizma kaydı"** kutusu (doğru ayrışım **2−½**: taşınım holonomisi + tur açığı; eski "Thomas ½ + ölçek payı 1" düzeltme kaydıyla geçersiz) · `:1681` H.3 gerekçesi · M-42 Açık Uçlar'a "taşınım payı" kalemi + γ_ℓ parantezi onarıldı.
**Daha önce (Parti 1, aynı gün):** Φ/Φ_it/Φ_N ayrımı + S-28 (9 yer), M-19 açık ucu kapatıldı, "nedensel olarak en katı" dili, çekim→toplanma, faktör-2 atıfları. Tam liste `tartısma_matematik` İŞLEM KAYDI'nda.
**A2 (M-42 girdi/çıktı muhasebesi) bilinçli olarak DOKUNULMADI** — üstel geçiş bu kararı etkiliyor (β artık türetilmiş), yeni çerçevede ele alınmalı.

---

## 8. SONRAKİ OTURUM NE YAPMALI — sıralı iş listesi

1. ~~§5'i kapat~~ → **✅ KAPANDI** (17 Ağu 2026): kohezyonla tutulan statik denge + iç içe zarf yapısı. **Üstel yapının önündeki engel kalktı.**
1b. ~~Eş-düzlemlilik/prograd anlatısını dolaşımsız yeniden kur~~ → **✅ KAPANDI** (`es_duzlemlilik_cozumu.md`): eş-düzlemlilik zaten F5'te ve korunumlu (KARNE s.35: *"mekanizma borcu yoktur"*), dolaşıma hiç bağlı değil; prograd tercih zaten açık kalemdi. **Bedel: 81 çarpanı** (retro/prograd sürükleme asimetrisi) düşüyor — statik ortamda oran 1; 7.4 md.15 sınavı bunu karara bağlıyor. **İkinci bağımsız doğrulama: Ay** — dolaşan ortam Ay apsisini 13,73 günde döndürürdü, gözlenen 8,85 yıl ⇒ 236 kat aşım, Dünya ortamı da statik.
1c. ~~Satürn ortamının sınanması~~ → **✅ KAPANDI** (`ortam_donusu_kilit_teoremi.md`): **KİLİT TEOREMİ** — siklostrofik dolaşım ⇒ Ω_m = **2n** tam (kütle/yarıçaptan bağımsız; 4 sistemde 2,0000000000) ⇒ apsis yörünge başına iki tur ⇒ **kapalı elips olamaz**. Gözlenen elipslerin varlığı tek başına kanıt. **Dört ortam kilitli:** Güneş (Merkür, 1,9×10⁶×, Ω ≤ 2,3×10⁻¹⁸), Dünya (Ay 237× + LAGEOS-2 4.489×), Satürn (Titan 3,4×10⁴×, Ω ≤ 2,7×10⁻¹⁵), Jüpiter (Io 3.158×). **⭐ Σ'nın statüsü yükseldi:** artık Kepler elipslerinin varlık koşulu — Bell'den bağımsız ikinci gerekçe.
1d. ~~Formasyon gerekçesi~~ → **✅ KAPANDI** (`formasyon_gerekcesi.md`): üç ayak — **(3, yük taşıyıcı)** madde ortamı döndüremez (enerji oranı 2,8×10⁻²⁸; M-43 bastırması 10²⁸) + M-9'un homojen taban durumu ⇒ **kesme hiç doğmadı**; **(1)** diferansiyel dönüş denge değil, v_m/L kesme salınımı (Merkür'de 0,019 s; Hubble'da denkleşme 1,37 Myr = evren yaşının 10⁻⁴'ü); **(2)** katı dönüş sınırsız kohezyonlu ortamda M-7'yi ihlal eder ⇒ sınırsız limitte **Ω = 0 tam** (Hubble-kesikli: |Ω| < 3,3×10⁻¹⁴). **Rafinaj:** Ayak 1 tek başına yetmez — salınım sönmüyor (τ = 5,3×10⁴⁰ yıl) ve ⟨w²⟩ tam genlikte kızıla kaymayı çökertir (kısıt: w_gen ≤ 0,02 v_yör); yükü Ayak 3 + M-9 taşır. **⭐ BONUS: Mach ilkesi mekanik olarak açıklandı** — kesme rijitliği yerel çerçeveyi küresele kilitler (denkleşme: Güneş sistemi 5 s, galaksi 3,3 yıl, evren 1,37 Myr).
1e. **Yeni alt işler:** ortamın uzaysal erimi (Ω=0-tam kolu sınırsızlığa dayanıyor) · Σ'nın ters yönlü duyarlılığı (büyük Σ ⇒ Ayak 2 gevşer) · galaktik ölçekte hüküm · prograd tercih kaleminin artan zorluğu · 81 çarpanına bağlı satırların koşullu yazımı (`es_duzlemlilik_cozumu.md` §5) · **yeni katalog girdileri:** Ortam Dönüşü Kilit Teoremi + Formasyon Gerekçesi (üç ayak + Mach) · M-5'e ikinci yapısal görev · M-7'ye katı-dönüş yasağı · Mach sonucunun Kısım 7'ye adaylığı.
2. `ustel_turetim_uc_yol.md`'yi düzelt: **Yol 3 (entalpi) çıkarılmalı** (§4c); Yol 1 (K=P) çürütüldü olarak işaretlenmeli (§4a); yerine Postülat 4 form-değişmezliği + GW170817 kilidi (§4b) ana gerekçe yazılmalı.
3. **Kalan 4 denetim cephesini koştur** (oturum limitine takıldı, hiç koşmadı): güçlü-alan karadelik yapısı · EHT nicel · diğer güçlü alan (ikili pulsar, QNM/eko, NICER) · kozmoloji/galaktik. Prompt'lar workflow betiğinde hazır: `...\workflows\scripts\ustel-olcek-denetimi-wf_eb309e06-5d9.js` — `Workflow({scriptPath: ..., resumeFromRunId: 'wf_eb309e06-5d9'})` ile tamamlananlar önbellekten döner.
4. **Yıldız-kütleli yüzey ışıması kalemini nicelleştir:** 10 M☉ için R_ρ ≈ 26 km, 1+z ≈ 1,8 ⇒ yüzey görünür; süperkütlelilerde sorun yok (M87*: 1+z = e^{4,3×10⁵}). Teorinin cevap adayı: kilitli kafes bir **büyüme cephesidir**, enerji kafes bağlanmasına gider. Type-I patlama yokluğu ve Sgr A* yüzey-ışıma üst sınırları bu kalemi doğrudan sınar. Aynı zamanda **yıldız-kütleli ↔ süperkütleli keskin ayrım öngörüsü**.
5. **M-7 yırtılma tabanını geçerlilik sınırı olarak koy:** üstel profil yalnız r > 0,2025μ geçerli (P_yırt/P₀ = 2,64×10⁻⁹); 1+z ≤ 140. "r = 0,1μ'de 1+z = 2,2×10⁴" değeri **geri çekilmeli**.
6. **Derin-kuyu sayılarını yeniden hesapla:** nötron yıldızında ΔP_üstel/ΔP_lineer = 0,7226 (%28 kayma) ⇒ ξ, M-40 zinciri, NS kızıla kaymaları.
7. **r_ISCO ve kritik dönüş limitleri** üstel yapıda türetilmeli (`Kisim_4\02:99`'un kalan kalemi).
8. Onay gelirse §6'nın düzenleme partisini uygula (sıra: M-51/52 girdisi → M-44 C-16 → M-46 C-15 → M-42 → Φ kararı C-19 → ufuk dili C-20 → B sınıfı süpürme → KARNE/Ek C).

## 9. Önceki oturumlardan devreden, üstelle ilgisiz açık kalemler
- **A2:** M-42 girdi/çıktı muhasebesi (Yol 1 yeniden sıralama ↔ Yol 2 muhafazakâr) — üstel çerçevede yeniden ele alınmalı.
- **A5:** M-18 asimetrik kol deney bütçesi — Λ ortak-mod uygulanınca öngörü birinci mertebede sıfırlanıyor olabilir; **Kısım 5 deney tasarımını etkiler**, Enes kararı bekliyor.
- **Jeodetik:** taşınım payının (+2) girdap-yönelim dinamiğinden alt-düzey türetimi; Λ_kin'in Ek M'ye M-51 olarak aynalanması.
- **Parti 3:** notasyon süpürgesi (çıplak c → c₀, G → 𝒢, h → h_yör, γ ataması) — tam liste `tartısma_matematik` D bölümünde.
- **E1:** v_θ/v_yör sembol ihlali (M-30 ↔ Ek A.4). **E2:** M-50 ölçü beyanı (∫dt d⁴x ↔ d³x).
- Bağımsız araç denetimi `Kisim_8_Eylem_Plani_Antigravity.md` — iki sorusu cevaplandı (Tartışma #2, §6b).
