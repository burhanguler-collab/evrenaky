Verification complete. All five routes run, with two genuine clashes and one previously unrecorded inconsistency found.

---

# BAĞIMSIZ YENİDEN TÜRETİM — BEŞ YOL

Betik: `C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\CALISMA\matematik\ustel_bagimsiz_bes_yol.py` (mpmath, 50 hane; ana oturumun `K=P → dP/dχ=−CP/P₀` yolu hiç kullanılmadı)

Ortak boyutsuz değişken: **u ≡ ρ_nΦ/P₀ = 4Φ/c₀² = 4μ/r**. Üstel: P = P₀e^(−u). Lineer: P = P₀(1−u). Kalibrasyon denetimi: P₀/ρ₀ = c₀² oranı 1.0000000000000000 ✓

---

## YOL 1 — ENTALPİ YOLU → **ÇÖKÜYOR (ayrım üretmiyor)**

**Kurulum.** M-50'nin tam barotropik potansiyeli: U(ρ) = c₀²ρ·ln(ρ/ρ₀), buradan P = ρU′−U. Sayısal denetim (ρ/ρ₀ = 0,3 / 1,0 / 3,7): oran **1.0000000000000000** ✓ — P = c₀²ρ doğrulandı. Entalpi M-44 md.6'nın Bernoulli'sinde geçen niceliktir: h = ∂U/∂ρ = c₀²(1+ln(ρ/ρ₀)).

**Matematik.** Deplasman kanalında ρ = ρ₀ sabittir (k=0). O hâlde χ-bağımlı en genel biçimde h = ∂U/∂ρ hesaplanınca:

    h(ρ₀, χ) = g(χ)c₀² = c_loc² = P/ρ₀   ⟹   h ∝ P  (ÖZDEŞ ORANTI)

**Sonuç profili: BELİRSİZ.** "χ, basınca değil entalpiye lineer bağlanır" önermesi deplasman kanalında **hiçbir yeni bilgi taşımıyor**, çünkü orada h ile P birbirine tam orantılıdır. Yol ne üstel ne lineer seçer.

> ⚠️ **DÜZELTME KAYDI — mevcut çalışma notu hatalı.** `ustel_turetim_uc_yol.md` "Yol 3 — Stiff entalpi", `h = c₀²ln(P/P₀)` alıp üstel çıkarıyor. Ama `c₀²ln(P/P₀)`, **ρ-kanalının** entalpisidir (∫dP/ρ boyunca ρ = P/c₀² değişir). Kuyu profili ise **deplasman kanalıdır** (ρ sabit, χ değişir). İki kanalı karıştırmak, M-44'ün *"Kritik Ayrım: Deplasman Bağıntısı Bir Hâl Denklemi Değildir"* hükmünün aynadaki ihlalidir. **Bu yol kitaba bu hâliyle taşınmamalı.**
>
> M-3′'ün üstel yoğunluk profili (ρ = ρ₀e^(−v²/2c²)) gerçek ve teorinin kendi malı, ama **başka kanalda**. Emsal teşkil eder, kanıt teşkil etmez.

**Kullanılan varsayımlar:** stiff hâl denklemi; h = ∂U/∂ρ (M-44'ün kendi Bernoulli'si). *Kazanç: birinci mertebe zincirin korunduğu doğrulandı* — fark = 8(Φ/c₀²)² (u=1e−3'te 7,99e−6); M-8'in ΔP_yüzey = ρ_nΦ'si üstelde oran **0,99999999860775** ile korunuyor; δc/c₀ = −2Φ/c₀² oran **0,99999999930387** ✓

---

## YOL 2 — SİKLOSTROFİK DENGE / SIKIŞTIRILABİLİR EULER → **ÜSTEL (koşullu)**

M-9'un **kendi denklemiyle** (Geçerlilik Sınırı): ∇P/ρ₀ = v_θ²/r. Bu yol M-9'un kayıtlı açık ucunu (*"siklostrofik denge profilinin v_θ(r) nicel eşlenmesi"*) kısmen kapatıyor.

### 2a — v_θ = 2v_yörünge (YENİ, tam, zayıf alan gerekmez)

| denklem | kaynak |
|---|---|
| madde: v_orb²/r = (1/ρ_n)dP/dr | M-2 + dairesel yörünge |
| ortam: v_θ²/r = (1/ρ₀)dP/dr | M-9 |

Oran: v_θ/v_orb = √(ρ_n/ρ₀) = **2.00000000000000** — her r'de tam, çünkü ρ₀ = ρ_n/4 (M-8).

**Fiziksel okuma:** v_θ = √2·v_kaçış — ortam kuyuya bağlı değildir, M-9'un ağırlıksızlık teoremiyle bağımsız olarak tutarlı. **Öngörü:** Güneş'in 1 AU'sunda ortam 59,57 km/s dolaşır; Dünya yüzeyinde 15,82 km/s. Sürüklenme zarfı (Postülat 7) tarafından perdelenmesi gerekir — ayrı bir hesap kalemi.

### 2b — Kapanma: profil χ'den ek varsayım olmadan çıkıyor

χ-sektöründe tek frekans ω_C ≡ C/ρ₀ ([C] = kg·m⁻³s⁻¹ ⟹ [ω_C] = s⁻¹; M-46'nın ε = (C/ρ₀)/ω_n'i). [χ] = m²/s olduğundan v² boyutunu veren **tek** kombinasyon v_θ² ∝ ω_Cχ'dir. M-46'nın Poisson'u χ = K/r verdiği için v_θ² ∝ 1/r **otomatik** çıkar — Kepler-benzeri dolaşım varsayılmıyor, türetiliyor.

Genliğin kendisi de serbest değil. M-46'nın 𝒢 = Cq_n/(4πρ_n m_n)'siyle:

    ω_C K = C·Nq_n/(4πρ₀) = 𝒢·(ρ_n/ρ₀)·M = 4𝒢M = 4μc₀²   ← TAM ÖZDEŞLİK

Üsteldeki **4, ρ_n/ρ₀ = 4'ün ta kendisidir** (M-8'in sıkışma oranı) — fit değil.

### 2c — ÇATAL (yolun asıl bulgusu)

Kavrama Yasası'nın oran biçimi yerel olduğundan P/ρ₀ = c_loc², yani d(lnP)/dr = (v_θ/c_loc)²/r. İki kapanma:

| kapanma | denklem | profil | ODE çözümü (r = R_güneş) |
|---|---|---|---|
| **A** ham hız: v_θ² = ω_Cχ | dP/dr = 4μP₀/r² | **LİNEER** | 0.99999150998971826706 = 1−4μ/r ✓ |
| **B** yerel Mach: (v_θ/c_loc)² = ω_Cχ/c₀² | dlnP/dr = 4μ/r² | **ÜSTEL** | 0.99999151002575830236 = e^(−4μ/r) ✓ |

mpmath `odefun` ile (çözüm önceden varsayılmadan, s = 1/r değişkeninde, s=0 sınır koşuluyla) her iki kol analitik biçimlerle **tam** örtüştü (fark 0.000e+00). A ile B'nin farkı 3,60e−11 = 8(μ/r)² mertebesi.

**Çatalın hükmü:** Sıkıştırılabilir akışkanda tepki daima **Mach sayısının** fonksiyonudur, ham hızın değil. Kitap bunu kinematik kolda **zaten** kullanıyor (11.4.8.1, Λ_kin, Prandtl–Glauert). Aynı kuralın potansiyel koluna uygulanması yeni varsayım değil, mevcut kuralın tekrarı ⟹ **B ⟹ ÜSTEL**.

### 2d — Dönüşüz alt kol DIŞLANIYOR (yeni yapısal bulgu)

Bernoulli (½v²+h = sbt) + siklostrofik ⟹ v dv/dr = −v²/r ⟹ v ∝ 1/r (potansiyel girdap) ⟹ (1/ρ₀)dP/dr ∝ 1/r³ (log-log eğim sayısal: **−3.000000**) ⟹ **P = P₀ − A/r²**, kütle-itim 1/r³.

**Ne lineer ne üstel — üçüncü bir biçim, ve M-46/M-35 ile çelişerek dışlanıyor.** Hüküm: *ortamın kütle çevresindeki dolaşımı dönüşüz olamaz*; M-44 md.3'ün dönüşüzlük kısıtı kütle-itim kuyusunda geçerli değildir (χ kaynak terimi vortisite kaynağıdır). Bu, M-44'ün Açık Uçlar'ına yazılacak bağımsız bir kalem.

---

## YOL 3 — EYLEM İLKESİ → **ÜSTEL, ve lineeri ÖLDÜRÜYOR** ⭐

**Kurulum.** M-44'ün iç enerjisine χ eklenir. Hem stiff dalga kanalını hem lineer/üstel deplasmanı veren **en genel iki aday**:

    (I)  ÇARPIMSAL:  U = g(χ)·c₀²ρ·ln(ρ/ρ₀)              ⟹ P = g(χ)c₀²ρ
    (II) TOPLAMSAL:  U = c₀²ρ·ln(ρ/ρ₀) + Cχ(1 − ρ/ρ₀)    ⟹ P = c₀²ρ − Cχ

P = ρU_ρ − U her iki adayda ve 9 (g,ρ) kombinasyonunda oran **1.0000000000000000** ✓

**İki adayın da geçtiği sınav.** ∂U/∂χ, ρ=ρ₀'da **her ikisinde de 0.0000e+00** ⟹ ∇²χ = −q_n n_m ikisinde de bozulmuyor. *(Not: prompt'un "Poisson değişmez" gerekçesi tek başına ayırt edici değil — bunu net kaydetmek gerekir.)*

**AYIRT EDİCİ SINAV — dalga kanalının hızı.** (∂P/∂ρ)_χ, yerel yayılma hızına eşit mi?

| aday | χ | (∂P/∂ρ)_χ | P/ρ = c_loc² | ORAN |
|---|---|---|---|---|
| ÇARPIMSAL | 0 | 8,98755179e16 | 8,98755179e16 | **1.00000000000000** |
| ÇARPIMSAL | 1e21 | 8,97273697e16 | 8,97273697e16 | **1.00000000000000** |
| ÇARPIMSAL | 1e22 | 8,84061797e16 | 8,84061797e16 | **1.00000000000000** |
| TOPLAMSAL | 0 | 8,98755179e16 | 8,98755179e16 | 1.00000000000000 |
| TOPLAMSAL | 1e21 | 8,98755179e16 | 8,97273697e16 | **1.00165109206479** |
| TOPLAMSAL | 1e22 | 8,98755179e16 | 8,83940364e16 | **1.01675997094316** |

Çarpımsal biçimde Kavrama Yasası'nın **oran** ve **diferansiyel** biçimleri her χ'de özdeştir. Toplamsal (lineer) biçimde kuyunun içinde ayrışırlar: dalga hızı c₀'da donar, ışık hızı c₀Λ²'ye düşer.

### Bunun bedeli: GW170817

| ortam | Φ/c₀² | lineer okumada \|Δv\|/v | üstel |
|---|---|---|---|
| Dünya yüzeyi | 6,96e−10 | 1,39e−09 | 0 (özdeş) |
| Samanyolu (200 km/s) | 4,45e−07 | **8,90e−07** | 0 (özdeş) |
| Güneş yüzeyi | 2,12e−06 | 4,24e−06 | 0 (özdeş) |
| nötron yıldızı | 0,2 | 3,30e−01 | 0 (özdeş) |

Kısıt 4,2e−16. **Lineer okuma Samanyolu potansiyelinde bile ~9 mertebe ihlal ediyor** (noktasal oran; integre edilmiş varış farkı olarak — ışığın Shapiro gecikmesi mertebesinde — daha da beter).

> 🔴 **YENİ BULGU — kayıtlı olmayan iç tutarsızlık.** M-44 "GW170817 **otomatik** sağlanır" diyor, gerekçe (∂P/∂ρ)_χ = c₀². M-9 de "her yoğunluk pürüzü **tam c₀** hızında" diyor. Ama M-42, ışığın c_loc = c₀Λ² ile gittiğini söylüyor. Harfi harfine okunursa **GW ile ışık aynı hızda gitmiyor** ve "otomatik" iddiası çöküyor. Bu, üstelden bağımsız bir açıktır ve kitapta kayıtlı değildir.
>
> **Çarpımsal (üstel) biçim bunu bir özdeşliğe çeviriyor:** (∂P/∂ρ)_χ = P/ρ = c_loc² her noktada, dolayısıyla GW ve ışık **aynı** yerel hızda gider ve ihlal özdeş sıfırdır. Yani üstel biçim, M-44'ün iddiasını gerçekten otomatik yapan **tek** biçimdir.

**Kullanılan varsayımlar:** M-44'ün eylemi; P = ρU_ρ − U; k=0. *g'nin biçimi burada türetilmiyor — onu Yol 4 kilitliyor.* Yol 3 varlık + yapısal uyumluluk kanıtıdır, teklik kanıtı değil.

---

## YOL 4 — ÖLÇEK KAPANMASI → **ÜSTEL (teklik)** ⭐

**Kurulum.** Genel tepki ailesi dP/dχ = −(C/P₀ⁿ)Pⁿ. Çözüm: P = P₀[1−(1−n)u]^(1/(1−n)), κ = 4n−3, β = 2n−1; n=1 ⟹ e^(−u).

**Matematik (boyut argümanı).** n ≠ 1 ise yasa **mutlak bir basınç ölçeği** (P₀) açıkça taşımak zorundadır. Postülat 4: P₀, ρ₀, c₀ **yereldir**, evrensel sabit değildir ⟹ yasada mutlak ölçek görünemez. Yalnız n = 1'de katsayı C/P₀ olur ve içinde basınç ölçeği kalmaz.

**Kesin test (form-değişmezlik).** Λ⁴ derinliğindeki yerel gözlemci, kendi P₀^loc = P₀Λ⁴'ü ile **aynı yasayı** yazabilmeli: F(u₀+u₁) = F(u₀)F(u₁).

| n | F(u₀+u₁) | F(u₀)F(u₁) | ihlal |
|---|---|---|---|
| 0 | 0,9988 | 0,9988002 | 2,0000e−07 |
| 0,5 | 0,99880036 | 0,99880046 | 9,9940e−08 |
| **1 (üstel)** | 0,9988007197120864 | 0,9988007197120864 | **1,3364e−51** |

Yalnız n = 1 form-değişmezdir (1,3e−51 = yuvarlama; yapısal olarak tam sıfır).

**Kullanılan varsayımlar:** yalnızca Postülat 4 + χ'nin toplamsallığı (M-46'nın lineer Poisson'u). **Hiçbir maddesel varsayım yok.**

---

## YOL 5 — ARŞİMET / DEPLASMAN MUHASEBESİ → **ÜSTEL**

**Kurulum.** M-46'nın **kendi kaydettiği** dışlanan-hacim modeli: P = c₀²ρ/(1−f), f = n_m V_cep.

    dP/df = c₀²ρ/(1−f)² = P/(1−f)

Sayısal denetim (f = 0 / 1e−6 / 1e−3 / 0,1): oran **1.0000000000000000** ✓ ve (∂P/∂f)_ρ = ρ₀c₀² = **6,0666e33 Pa** — M-46'nın kaydettiği 6,07e33 ile birebir.

**Kritik nokta:** tepki katsayısı **sabit değil, mevcut P ile ölçekleniyor**. Kabuk kabuk birikim çarpımsaldır:

| N kabuk | (1−u/N)^N | e^(−u)'dan sapma |
|---|---|---|
| 1 | 0,999 | 4,9983e−07 |
| 10 | 0,99900044988002099748 | 4,9953e−08 |
| 10⁴ | 0,99900049978342496335 | 4,9950e−11 |
| 10⁸ | 0,99900049983336999667 | 4,9950e−15 |

N→∞'da tam e^(−u); çarpım değişmeli olduğu için **kabukların sırasından bağımsız**.

Kök neden K = ρ(∂P/∂ρ) = ρc_loc² = P özdeşliği: g = 1,0 ve 0,6 için K/P = **1.0000000000000000** ✓

**Dürüstlük kaydı:** M-46 bu modelin f ∝ n_m olduğu için kaynak dışında sıfırlandığını, dolayısıyla 1/r profili veremediğini kaydediyor — ve haklı. Yol 5 bileşik bir argümandır: **profil M-46'nın χ'sinden, genlik yasası sertlikten**. Ayrıca bu yol, ana oturumun K=P yolunun kabuk diliyle yeniden yazımıdır — **bağımsız değildir**.

---

# KARŞILAŞTIRMA TABLOSU

| yol | sonuç profili | kullanılan varsayımlar | bağımsızlık | güç |
|---|---|---|---|---|
| **1** Entalpi | **BELİRSİZ** (h ∝ P) | stiff EOS, h = ∂U/∂ρ | — | ✗ ayrım üretmiyor |
| **2a** v_θ = 2v_orb | (profilden bağımsız) | M-9 + M-2 + M-8 | **tam bağımsız** | ✓✓ yeni öngörü |
| **2b** Siklostrofik | **ÜSTEL** (Mach yerel) / LİNEER (ham hız) | M-9, M-46, M-1 oran + yerellik | mekanizma bağımsız, öncül ortak | ✓✓ |
| **2d** Dönüşüz kol | **P₀ − A/r²** → DIŞLANIR | + dönüşüzlük | tam bağımsız | ✓ yeni hüküm |
| **3** Eylem | **ÜSTEL** (lineer GW170817'de ölür) | M-44 eylemi, P = ρU_ρ−U | **tam bağımsız (gözlemsel)** | ✓✓✓ |
| **4** Ölçek kapanması | **ÜSTEL** (teklik) | yalnız Postülat 4 | öncül = yerellik | ✓✓✓ |
| **5** Kabuk/Arşimet | **ÜSTEL** | K = ρc² = P (stiff kimlik) | ana oturumun yolu ≡ | ✓ |

**Sayım:** 4 yol üstel (2b, 3, 4, 5) · 1 yol belirsiz (1) · 2 rakip biçim dışlandı (dönüşüz 1/r²; ham-hız lineer).

## ÇAKIŞMALAR ve hükümleri

1. **Yol 1 üsteli desteklemiyor.** Prior çalışma notunun "stiff entalpi" yolu kanal karıştırması. **Kitaba taşınmamalı.**
2. **Yol 2'nin ham-hız kolu LİNEER veriyor.** Hüküm: yerel Mach kolu doğru, çünkü sıkıştırılabilir tepki Mach'ın fonksiyonudur ve kitap bunu 11.4.8.1'de zaten yapıyor.
3. **Dönüşüz Bernoulli 1/r² veriyor.** Hüküm: kütle-itimin 1/r²'siyle çeliştiği için dışlanır; ortam dolaşımı dönüşüz olamaz.

## En sağlam yol hükmü

**YOL 3 + YOL 4 çifti** — ve bu çift, ana oturumun yolundan da prior notun Yol 2'sinden de **gerçekten bağımsızdır**:

- **Yol 4 tekliği verir**, tek öncülü Postülat 4'tür (hiçbir maddesel varsayım yok). Prior notun "çarpımsal bileşim" yolundan farkı: o fonksiyonel-denklem, bu boyut/ölçek argümanı — matematiksel olarak aynı teoreme çıkıyorlar, dolayısıyla **ikisini iki bağımsız kanıt saymak yanlış olur**.
- **Yol 3 gözlemsel bir kilit ekler**: lineer biçim eyleme yazıldığında dalga kanalının hızı yerel yayılma hızından ayrışır ve GW170817'yi ~9 mertebe ihlal eder. Bu, üsteli **saf yapı argümanından çıkarıp ölçülmüş bir gözleme bağlar** — Merkür'den bağımsız ikinci bir gözlemsel kilit. Denetimin en değerli çıktısı budur.

**Dürüst çerçeve:** Beş yol *beş bağımsız doğrulama değildir*. Üsteli veren dört yolun tamamı, tek bir fiziksel öncülün farklı denklemlerdeki ifadesidir: **ortamın tepkisi mutlak arka plana değil yerel duruma referanslıdır.** Bu öncül Postülat 4'ün kendisidir. Yani üstel biçim teoriye eklenen bir yenilik değil, **Postülat 4'ün deplasman kanalına uygulanmasıdır**; lineer biçim ise c₀ ve P₀'ı gizlice evrensel sabit saymanın artığıdır — teorinin açıkça yasakladığı şey. Yolların değeri bağımsız onay değil, **öncülün kaç ayrı denklemde aynı sonuca çıktığını** göstermektir. Buna karşılık Yol 2a, Yol 2d ve Yol 3'ün GW170817 kolu gerçekten bağımsız yeni kalemlerdir.

**Bağımsız gözlem denetimi (yeniden koşuldu):** Üstel Λ = e^(−x) → Merkür **42,980680**″/yy; GR referansı 42,980676; lineer 50,144129; ölçüm 42,9799 ± 0,0009. Işık bükülmesi 4μ/b = **1,751190**″ (üstelde 1. mertebede özdeş, fark 4,5e−12).

---

# KİTABA YAZILACAK TÜRETİMİN İSKELETİ

Öneri: **M-51 · Üstel Ölçek Yapısı: Deplasman Kanalının Yerel Tepkisi** · [T (yapı) / S (n=1)], Blok I'e (Eylem İlkesi) M-46'dan sonra.

**Varsayımlar** (yeni girdi yok, hepsi kayıtlı): 1) M-44'ün iki değişkenli hâl denklemi ve k=0 · 2) M-46'nın Poisson'u ∇²χ = −q_n n_m · 3) M-1'in oran biçimi, **yerel** olarak: c_loc² = P/ρ · 4) Postülat 4 · 5) M-8'in ρ₀ = ρ_n/4'ü.

**Adımlar:**
1. **Sorunun kurulumu.** M-46'nın P = P₀ − Cχ'si küçük-deplasman kesiti. Sabit C, yasaya mutlak bir basınç ölçeği yerleştirir — Postülat 4 ile çelişir. Genel aile: dP/dχ = −(C/P₀ⁿ)Pⁿ, κ = 4n−3, β = 2n−1.
2. **Teklik (Yol 4).** Form-değişmezlik ⟹ n = 1 ⟹ **P = P₀e^(−Cχ/P₀)**, ve M-46'nın zincir denetimiyle (Cχ/P₀ = 4Φ/c₀²) **P(r) = P₀e^(−4μ/r)**, Λ = e^(−Φ/c₀²). Tablo: n vs β vs Merkür; ihlal 1,3e−51 ↔ 2e−07.
3. **Eylem düzeyi (Yol 3).** U(ρ,χ) = g(χ)c₀²ρ·ln(ρ/ρ₀), g = Λ⁴. Poisson bozulmaz (∂U/∂χ|_{ρ₀} = 0) **ve** (∂P/∂ρ)_χ = P/ρ = c_loc² her noktada. Karşıt aday U = c₀²ρln(ρ/ρ₀) + Cχ(1−ρ/ρ₀) Poisson'u da bozmaz ama dalga hızını c₀'da dondurur.
4. **GW170817 kilidi.** Lineer okumada GW ile ışık ayrışır (Samanyolu'nda 8,9e−07 ≫ 4,2e−16); üstelde özdeş sıfır. **M-44'ün "otomatik" iddiasını gerçekten otomatik yapan tek biçim.** (Aynı zamanda M-44/M-9'un kayıtsız açığının düzeltme kaydı.)
5. **Ortamın dinamiği (Yol 2).** M-9'un siklostrofik dengesi: v_θ = 2v_orb (tam); boyut zorunluluğuyla v_θ² ∝ ω_Cχ ⟹ 1/r profili M-46'dan gelir; ω_C K = 4𝒢M **tam özdeşlik** (üsteldeki 4 = ρ_n/ρ₀). Yerel Mach kapanması ⟹ e^(−4μ/r). Dönüşüz kol dışlanır (1/r² ⟹ kuvvet 1/r³). → M-9'un açık ucu kısmen kapanır; yeni öngörü: 1 AU'da 59,57 km/s ortam dolaşımı (sürüklenme zarfı perdelemesi açık kalem).
6. **Yapısal süreklilik.** M-42'nin tüm ilişkileri (ℓ,f ∼ Λ; c_loc ∼ Λ²; yerel Lorentz null) aynen korunur; lineer yazım **birinci mertebe kesiti** olarak yeniden konumlanır. M-8 (ΔP = ρ_nΦ, oran 0,999999998) ve M-42 (δc/c₀ = −2Φ/c₀², oran 0,999999999) korunur.
7. **Kapanan gözlem.** β = 1 ⟹ Merkür 42,9805″/yy (0,69σ). M-42'nin Geçerlilik Sınırı'ndaki "β belirlenmemiştir / Merkür kapanmamıştır" kalemi **kapanır**; 7.4 md.12 güncellenir.

**Geçerlilik Sınırı'na yazılacaklar:** n=1 yapısal olarak zorunlu, gözlemsel olarak Merkür'le n = 1,000000 ± 3,1e−05 · derin rejimde (Λ→0) hâl denkleminin stiff kalıp kalmadığı M-3′'ün açık ucuyla ortak · ortam dolaşımının sürüklenme zarfıyla eşlenmesi yapılmadı · **Yol 1 (entalpi) ayrım üretmez, gerekçe olarak kullanılmamalı.**

**Açık Uçlar'a:** dönüşüz-olmama sonucunun M-44 md.3 ve M-50'nin Clebsch genişletmesiyle uzlaştırılması · v_θ = 2v_orb öngörüsünün ölçülebilir imzası · g(χ) = Λ⁴ özdeşleştirmesinin M-42'nin γ_ℓ = −1 mekanizmasıyla bağı (ikisi aynı açık kalemin iki yüzü olabilir).