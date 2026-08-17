# Üstel Ölçek Yapısının Türetimi — Üç Bağımsız Yol

> Çalışma notu, 17 Ağustos 2026 (Opus). `tartısma_matematik` Tartışma #3'ün türetim eki.
> Amaç: Λ = e^{−Φ/c₀²} biçiminin **teorinin kendi yapısından** çıktığını, dışarıdan seçilmediğini göstermek.
>
> ## ⚠️ DENETİM SONRASI DURUM (aynı gün, 8 ajanlı denetim) — BU DOSYA KISMEN GEÇERSİZ
> - **Yol 1 (yerellik/K=P) ÇÜRÜTÜLDÜ.** Deplasman kanalında M-44 `(∂P/∂ρ)_χ = c₀²` (sabit) yazıyor ⇒ K = ρ₀c₀² = P₀, P'yi izlemiyor. Ayrıca K hacimsel zorlanmanın katsayısıdır ve bu kanalda dV/V = 0 (k=0) — iki-kısmi-türev karıştırması, yani M-44'ün varlık nedeninin ihlali. Argüman ciddiye alınırsa üs **1** çıkar (k=1, M-8'i öldürür), oysa öneri üs 4 kullanıyor. **Gerekçe olarak kullanılmamalı.**
> - **Yol 3 (stiff entalpi) HATALI.** h = c₀²ln(P/P₀) **ρ-kanalının** entalpisidir (orada ρ = P/c₀² değişir); kuyu profili **deplasman kanalıdır** (ρ sabit, χ değişir). Deplasman kanalında h ∝ P özdeş olduğundan bu yol **hiçbir ayrım üretmiyor**. **Kitaba taşınmamalı.**
> - **Yol 2 (çarpımsal bileşim) AYAKTA** ve ana türetim olmalı — ama bir **aksiyom**, teorem değil. Bağımsız ajan aynı teoremi Postülat 4 **form-değişmezliği** olarak da kurdu: n ≠ 1 ise yasa mutlak bir basınç ölçeği taşımak zorundadır, Postülat 4 bunu yasaklar. *(İkisi matematiksel olarak aynı teorem — iki bağımsız kanıt sayılmamalı.)*
> - **YENİ ve en güçlü ayak — GW170817 kilidi (bu dosyada yok, eklenmeli):** lineer biçim eyleme yazıldığında dalga kanalının hızı c₀'da donar, ışık c_loc = c₀Λ²'ye düşer ⇒ ikisi ayrışır; ihlal Samanyolu potansiyelinde 8,9×10⁻⁷, kısıt 4,2×10⁻¹⁶ ⇒ **~9 mertebe**. Üstelde (∂P/∂ρ)_χ = P/ρ = c_loc² her noktada ⇒ ihlal **özdeş sıfır**. Üstel, M-44'ün "GW170817 otomatik" iddiasını gerçekten otomatik yapan **tek** biçim. Merkür'den bağımsız ikinci gözlemsel kilit.
> - Ayrıntı ve tam kayıt: `DEVIR_KAYDI_ustel_olcek.md` §4 · `denetim_raporlari\08_bagimsiz_bes_yol.md` · `denetim_raporlari\04_lambda_yayginlik.md` (C-16).

---

## Yol 1 — Yerellik zorunluluğu (Postülat 4)

**Argüman:** M-46'nın lineer yanıtı P = P₀ − Cχ, sabit bir C taşır. Ama sabit C, *her konumda aynı* basınç ölçeğini referans alır — yani ortamın tepki katsayısına **evrensel bir sabit** yerleştirir. Bu, Postülat 4'ün ("hiçbir şey evrensel sabit değil; c₀ dahil her şey yereldir") doğrudan ihlalidir.

Tepki katsayısı yerelleştirilirse:

$$-\left(\frac{\partial P}{\partial\chi}\right)_{\!\rho} = C_{yerel} = C_0\,\frac{P}{P_0}$$

**Bu ek bir varsayım değil, yerellik ilkesinin gereğidir.** İntegre edilir:

$$\frac{dP}{P} = -\frac{C_0}{P_0}d\chi \;\Longrightarrow\; P = P_0\,e^{-C_0\chi/P_0}$$

*Fiziksel okuma:* ortamın dışlanmaya karşı "geri itme" gücü, o noktadaki mevcut basıncıyla ölçeklenir — stiff ortamda sertlik zaten basıncın kendisidir (K = ρc² = P, çünkü c² = P/ρ). Sabit-C okuması, seyrelmiş bir bölgede ortamın *aynı* güçle geri ittiğini varsayar; bu, ortamın kendi hâl denklemine aykırıdır.

---

## Yol 2 — Çarpımsal ölçek bileşimi ⭐ **(en güçlü; saf yapı)**

Bu yol hiçbir maddesel (constitutive) varsayım kullanmaz. Yalnız iki kayıtlı gerçeği kullanır:

**(a) Kitap ölçekleri ÇARPIMSAL bileştirir.** 11.4.8.1'in kutulu sonucu:
$$\Lambda = \Lambda_{grav}\cdot\Lambda_{kin}$$
Bu tesadüfi bir yazım değil: Λ bir **ölçek çarpanıdır** (cetvel/saat yeniden ölçekleme), ve ardışık iki yeniden ölçekleme daima çarpılır.

**(b) Deplasman alanı TOPLAMSAL bileşir.** M-46: ∇²χ = −qₙnₘ — Poisson **lineerdir**, dolayısıyla iki kütlenin alanları toplanır: χ_toplam = χ₁ + χ₂ (aynı şekilde Φ_toplam = Φ₁ + Φ₂ zayıf alanda).

**Zorunluluk:** İki kütlenin ortak kuyusundaki bir cetvel, iki ölçeklemeyi *ardışık* görür ⇒ Λ(χ₁+χ₂) = Λ(χ₁)·Λ(χ₂). Bu fonksiyonel denklemin (sürekli, Λ(0)=1) **tek** çözümü üsteldir:

$$\boxed{\Lambda(\chi) = e^{-a\chi}}$$

Newton limitiyle a sabitlenir (Λ ≈ 1 − Φ/c₀²) ⇒ **Λ = e^{−Φ/c₀²}**, ve M-42'nin c_loc = c₀Λ² ilişkisiyle P = ρ₀c_loc² = P₀Λ⁴ = P₀e^{−4Φ/c₀²}.

**Bunun sertliği:** Mevcut lineer yazım Λ = 1 − Φ/c₀², çarpımsal bileşimi **sağlamaz**:
(1−U₁)(1−U₂) = 1 − U₁ − U₂ + U₁U₂ ≠ 1 − (U₁+U₂).
Yani kitabın kendi Λ = Λ_grav·Λ_kin yapısı ile Λ'nın lineer biçimi **ikinci mertebede birbiriyle çelişir.** Üstel biçim bu çelişkiyi kaldırır — bir yenilik eklemez, mevcut iç tutarsızlığı onarır.

**Sayısal doğrulama** (`ustel_turetim_sinavi.py` §2; Dünya yüzeyi U_⊕ = 6,96×10⁻¹⁰ ve Güneş'in 1 AU'daki U_☉ = 9,87×10⁻⁹ ile):
- Üstel: Λ₁Λ₂ − Λ(U₁+U₂) = **1,3×10⁻⁵¹** (yuvarlama; yapısal olarak tam sıfır) ✓
- Lineer: ihlal = U_⊕·U_☉ = **6,87×10⁻¹⁸** — sıfır değil.
*(Dürüst çerçeve: bu ihlal doğrudan bir gözlem çelişkisi değildir; üstel biçim g_tt'de GR ile ikinci mertebeye kadar özdeştir (her ikisi de 1−2U+2U²), dolayısıyla saat ağları iki teoriyi ayırmaz. Bulgunun anlamı, **lineer yazımın kitabın kendi çarpımsallığıyla tutarsız olduğudur**.)*

**Beklenen itiraz ve cevabı — "Λ_kin de üstel olmalı değil miydi?"**
Hayır, ve bu argümanı zayıflatmaz. Kısıt yalnız **taşıyıcı niceliğin toplamsal olduğu** yerde bağlar:
- Λ_grav'ın taşıyıcısı Φ (ya da χ) ve **Poisson lineerliği gereği toplamsaldır** (Φ_top = Φ₁+Φ₂) ⇒ çarpımsallık üsteli dayatır.
- Λ_kin'in taşıyıcısı hız ve **hızlar toplamsal değildir** (ardışık hız bileşimi doğrusal değil) ⇒ Λ_kin için üstel zorunluluğu doğmaz; 11.4.8.1'in √(1−V²/c₀²) biçimi Prandtl–Glauert'ten kendi türetimiyle gelir ve dokunulmaz.
Argümanın mantığı "bağımsız yeniden-ölçekleme nedenleri çarpılır"dır; hangi nedenin *içinde* üstel çıkacağını, o nedenin taşıyıcısının bileşim kuralı belirler.

---

## Yol 3 — Stiff entalpi (M-3′)

M-3′ stiff ortamın enerji defterini zaten logaritmik tutuyor: h = ∫dP/ρ = c₀² ln ρ (kitapta birebir bu ifadeyle). Stiff ortamda doğal değişken P değil **ln P**'dir. Deplasman alanı, ortamın doğal değişkenine lineer bağlanır:

$$C\chi = -P_0\ln(P/P_0) \;\Longrightarrow\; P = P_0e^{-C\chi/P_0}$$

*(M-3′'ün kendi hesabı v² = 2c²ln(ρ₀/ρ) ile aynı logaritmik yapı; oradaki "üstel seyrelme" ile buradaki "üstel kuyu" aynı ortamın iki yüzü.)*

---

## İkinci-mertebe belirsizliğinin kalkması (bonus tutarlılık)

Mevcut kitapta iki okuma ikinci mertebede **ayrışıyor** — bu, üstelden bağımsız, kayıtlı olmayan bir iç tutarsızlıktır:

*(Aşağıdaki üç satır `ustel_turetim_sinavi.py` §3 ile sayısal doğrulandı.)*

| Okuma | Λ | β | Merkür |
|---|---|---|---|
| (a) M-42'nin yazımı harfiyen: Λ = 1 − U | 1 − U | **+½** | 50,14″/yy |
| (b) Basınç zinciri harfiyen: P = P₀(1−4U) ⇒ Λ = (1−4U)^{1/4} | 1 − U − 1,5U² | **−1** | 71,63″/yy |
| **(c) Üstel: Λ = e^{−U}, P = P₀e^{−4U}** | e^{−U} | **+1** | **42,98″/yy** ✓ |

**Bu tablo, üstelden bağımsız bir bulgudur ve kitapta kayıtlı değildir:** aynı kanonun iki okuması β için +½ ve −1 veriyor (Merkür'de 50,1″ ↔ 71,6″). Yani mevcut lineer yazım ikinci mertebede **tanımsızdır** — hangi okumanın kastedildiği metinde belirtilmemiş. Üstel biçim tek tutarlı ailedir.

Üstel biçim, "Λ'nın biçimi" ile "P'nin biçimi"nin **aynı fonksiyonel şekli** taşıdığı tek ailedir; c_loc = c₀Λ² ilişkisi böylece birinci mertebede değil **her mertebede** geçerli olur. (a) ile (b)'nin farklı β vermesi, lineer yazımın ikinci mertebede tanımsız olduğunun kanıtıdır.

### Genel aile ve gözlemin seçimi
dP/dχ = −C(P/P₀)^n alınırsa (n: tepki üssü):
$$P = P_0\left[1-(1-n)\tfrac{4\Phi}{c_0^2}\right]^{1/(1-n)},\qquad \kappa = 4n-3,\qquad \beta = \frac{1+\kappa}{2} = 2n-1$$
Sayısal doğrulama (`ustel_turetim_sinavi.py` §1) — β_sayısal ile 2n−1 altı değerde birebir örtüştü:

| n | β | Merkür (″/yy) |
|---|---|---|
| 0 (sabit C) | −1 | 71,63 |
| 0,5 | 0 | 57,31 |
| 0,9 | +0,8 | 45,85 |
| **1 (yerel C, üstel)** | **+1** | **42,9805** ✓ |
| 1,1 | +1,2 | 40,12 |
| 1,5 | +2 | 28,65 |

- Merkür'ün ±0,0009″ hassasiyeti tepki üssünü **n = 1,000000 ± 3,1×10⁻⁵** bandına kilitler.

Yani: **yerellik (Yol 1) ve çarpımsal bileşim (Yol 2) n = 1'i yapısal olarak dayatıyor; Merkür bunu bağımsız olarak 2×10⁻⁵ hassasiyetle doğruluyor.** Serbest parametre eklenmedi — aksine β, serbest kalemden türetilmiş kaleme geçti.

---

## Kitaba geçerken kullanılacak sıralama önerisi
1. **Yol 2** ana türetim (saf yapı, en az varsayım, kitabın kendi 11.4.8.1'ine dayanır).
2. **Yol 1** fiziksel gerekçe (yerellik/Postülat 4 — neden sabit C yanlıştı).
3. **Yol 3** ortamın doğal değişkeni (M-3′ ile süreklilik).
4. Sonra: ikinci-mertebe belirsizliğinin kalkması, β = 2n−1 ailesi ve Merkür'ün n'yi kilitlemesi.
