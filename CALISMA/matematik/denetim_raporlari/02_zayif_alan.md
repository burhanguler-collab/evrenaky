## LAMBDA TARAMASI — ÜSTEL ÖLÇEK YAPISINA GEÇİŞİN KİTAP İÇİ ETKİ HARİTASI

Kök: `C:\Users\ASUS\Desktop\EvrenAKI\KITAP3\websitesi\Metin\Akademik`
Tarama: `Lambda` 185 vuruş / 29 dosya · `M-42` 111 vuruş / 25 dosya · `c_{loc}`+`n_{eff}`+`c_{yerel}` 130 vuruş. Hepsi bağlamıyla okundu.

**Genel sonuç:** Yapısal ilişkilerin (ℓ,f ∝ Λ · c_loc = c₀Λ² · n_eff = 1/Λ² · c_loc/(ℓf) ≡ 1 · ν_tik ∝ Λ/γ · Λ_kaynak/Λ_alıcı) **hiçbiri** değişmiyor — vuruşların ~%80'i A sınıfı. B sınıfı 36 vuruş, mekanik "birinci mertebe" notu. **Ama 22 ayrı C kalemi var ve ikisi gerçek fizik değiştiriyor (C-16 ve C-4).**

---

# ⚠️ C SINIFI — GERÇEK FİZİK / YENİDEN HESAP

## ⛔ C-16 · EN DERİN ÇATIŞMA: M-44'ün "v_ses = c₀ tam olarak" kutusu üstel yapıyla ÇELİŞİR

**`Kisim_8_Ekler\19_Ek_M_Blok_I_Eylem_Ilkesi.md:26, 40, 42`**

Mevcut metin (satır 40, kutulu):
$$P=c_0^2\rho \Longrightarrow (\partial P/\partial\rho)_\chi=c_0^2 \Longrightarrow \boxed{v_{ses}=c_0\ \text{tam olarak}}$$
ve satır 42: *"stiff (Zel'dovich) akışkan … GW170817 otomatik sağlanır."*

**Sorun (bu denetimde bulundu, ana oturumda hesaplanmamış):** Üstel öneri (∂P/∂χ)_ρ = −C·(P/P₀) diyor. Tam diferansiyel (Maxwell) koşulu:
- Mevcut yazım: ∂²P/∂χ∂ρ = 0 (birinciden) ↔ −(C/P₀)c₀² (ikinciden) → **ÇELİŞKİ**.
- Tek tutarlı çözüm: **P(ρ,χ) = c₀²ρ · exp(−Cχ/P₀)**, yani
  (∂P/∂ρ)_χ = P/ρ = c₀²Λ⁴ ve (∂P/∂χ)_ρ = −(C/P₀)P ✓ (çapraz türevler eşit ✓)

**Sonucu:** üstel yapıda dalga kanalının ses hızı sabit c₀ **değil**, yerel c_loc = √(P/ρ) = c₀Λ²'dir. M-44 Varsayım 1'in *"Kavrama Yasası'nın **oran** biçimi geçerlidir: c₀²=P/ρ"* (satır 26) **aynen ve TAM olarak** korunur; kırılan şey Adım 2'nin daha güçlü iddiası olan "c₀ küresel sabittir".

**Ve bu bir kayıp değil, kazanç:** GW170817 hâlâ otomatiktir, ama daha güçlü bir gerekçeyle — GW ile Zerre **aynı** c_loc'u paylaşır, dolayısıyla Δv/v ≡ 0 özdeş olarak sıfırdır (mevcut gerekçe "ikisi de tam c₀'dedir" idi, ki farklı potansiyellerde birebir eşitliği garanti etmez). Postülat 4 ile de uyum artar: sabit c₀ iddiası eylemin içinden çıkarılmış olur.

**Karşı taraf, dürüst kayıt:** Doğrusal yazım (P = c₀²ρ − Cχ) tam diferansiyel olarak **tutarlıdır** ve (∂P/∂ρ)_χ = c₀² sabitini korur — ama o zaman c_loc = √(P/ρ) ile M-42'nin c₀Λ²'si O(Φ²)'de **ayrışır**. Yani mevcut kitapta zaten kayıtsız bir ikinci mertebe iç tutarsızlık var; üstel yapı onu **kapatan** biçimdir.

**Gereken işlem:** M-44 Adım 2 yeniden yazılmalı: kutulu sonuç `v_ses = c_loc = √(P/ρ)`; stiff nitelemesi *oran biçiminde* korunur; GW170817 satırı "ortak c_loc" gerekçesine geçer. Bağlı yerler: `19_Ek_M_Blok_I:17` (madde A: "basınç salınımları c₀ ile yayılır" — GW170817'nin gerektirdiği), `:213` (χ dalgaları v_m; ρ-sektörü "**yerel** c₀'de" — bu ifade zaten doğru yönde), `08_Sembol_Sozlugu:11` (R-3: "akustik dalga hızı tam c₀"), `07_Matematiksel_Ekler:17` (Blok I özeti: "ses hızı **tam c₀**").

## ⛔ C-4 · M-42'nin "yapısal sınır" tezi ÇÜRÜTÜLDÜ

**`Kisim_8_Ekler\18_5_Kuvvet_Matematigi.md:1367–1371`**

Mevcut metin: *"Bu türetim biçimsel olarak bir optik-ortam kuruluşudur… **Sınır:** Kütleli cisim yörüngeleri. Bir skaler indis, n'nin hıza bağlı olmadığı sürece kütleli parçacıkların hareketini tam üretmez; günberi kaymasının ikinci mertebe payı bu yüzden indisin **dışındadır**… Merkür'ün açık kalması rastlantı ya da eksik hesap değil, **kullanılan yapının cinsinden gelen bir sınırdır.**"*

**Bu tez yanlıştır ve ana oturum sayısal olarak çürütmüştür.** Teorinin kendi eyleminden — S = −mc₀²∫Λ_g√(1−V²/c_loc²)dt — çıkan yörünge denklemi (dx/dφ)² = (A − BΛ²)/Λ⁴ − x², üstel Λ ile presesyon/GR = 1.0000001 verir. Λ_kin çarpanı *tam olarak* "n'nin hıza bağlı olması"dır ve teoride 11.4.8.1'de zaten türetilmiştir. Yani indis skaler değil, **çarpım yapılı**dır; ikinci mertebe pay indisin dışında değil, Λ_kin ile birlikte tam içindedir.

**Gereken işlem:** Paragraf tümüyle silinip yerine üstel türetim + eylem kaydı konmalı; "optik analojiden çıkıp ortamın dinamiğine geçmek gerekir" cümlesi *"geçildi: hacim modülü K = ρc² = P özdeşliği"* ile değiştirilmeli.

## C-1 · M-42 Geçerlilik Sınırı — Merkür kaydı

**`18_5_Kuvvet_Matematigi.md:1356, 1357`** — *"Yapı **birinci mertebedir**… β parametresi belirlenmemiştir"* / *"Bu nedenle **Merkür günberi kayması hâlâ kapanmamıştır**: presesyon (2+2γ−β)/3 ile ölçeklenir; γ=1 sağlandı, β=1 gerekiyor. β olmadan öngörü (4−β)/3 × 43″/yüzyıldır."*
→ **Kapandı.** Üstel Λ (κ=1) → β = 0,999933 ≈ 1, presesyon ölçeği (7−κ)/6 = 1 (tam GR); Merkür 42,9805″/yy, ölçüm 42,9799 ± 0,0009 → **0,69σ**. Doğrusal yazım β = ½ → 50,1439″ → 7960σ, **dışlanır**. Yani üstel yapı Merkür'ü kapatmakla kalmıyor, doğrusal yazımı gözlemle **eliyor**.

## C-2 · **`18_5:1362`** — Açık Uçlar: *"β parametresi: Ortamın O(Φ²) tepkisinin P(Φ) hâl ilişkisinden türetilmesi. Kapanırsa Merkür'ün 43″'si de kapanır — teorinin kalan tek klasik GR sınavı."* → **Kalem kapanır** (istenen tam olarak yapılan iş: K = P ile P = P₀e^{−4μ/r}).

## C-3 · **`18_5:1365`** — *"Ayırt edicilik: γ=1 ile teori 1PN düzeyinde GR ile gözlemsel olarak ayrışmaz. Ayrışma ancak β'da veya ikinci mertebede aranabilir."*
→ **Yeniden yazılmalı:** β de 1 çıktığı için 1PN'de ayrışma yok; ayrım **güçlü alana** taşınır: gölge b_krit = 2eμ = 5,4366μ vs GR 3√3μ = 5,1962μ (**+%4,63**, EHT arenası) · **ufuk yok, tekillik yok** · r = 2μ'de 1+z = 1,65 sonlu.

## C-5 · **`18_5:1346–1352`** (P₀ Üzerindeki Sonucu) — zincir (1−k)/2·(ρ_nΦ/P₀) = 2Φ/c₀² → P₀ = ((1−k)/4)ρ_nc₀².
→ Sayı **değişmez** (6,07×10³³ Pa), ama zincirin iki halkası artık birinci mertebedir: ΔP_yüzey = ρ_nΦ ve δc/c₀ = −2Φ/c₀², üstel yazımın açılımlarıdır. TAM biçim: −ln(P/P₀) = 4Φ/c₀². "Birinci mertebede" notu + tam bağıntı eklenmeli.

## C-6 · **`18_5:1651`** (H.2 Öncelik 1′) — *"P(Φ) hâl ilişkisinin O(Φ²/c₀⁴) terimi ⟹ β · Merkür'ün 43″'ını kapatır; **GR'dan ayrışmanın aranacağı tek yer**"*
→ İş **yapıldı**; ayrıca "tek yer" iddiası artık yanlış (ayrışma güçlü alanda). Satır kapanan kaleme taşınmalı.

## C-7 · **`18_5:1693`** (H.3 öngörü tablosu) — *"| *Merkür günberi kayması 43″/yüzyıl* | *Radar telemetrisi* | **Türetilemiyor** — ikinci mertebe β (7.4 md.12) |"*
→ **"Sınandı ✓ 42,9805″/yy (0,69σ); doğrusal yazım 50,14″ ile 7960σ dışlanır"**. Aynı tabloya iki yeni satır: gölge +%4,63 (EHT) ve ufuk yokluğu.

## C-8 · **`18_5:1173–1179`** (M_min · Minimum Karadelik Kütlesi)
Mevcut: R_ρ = (3M/4πρ_n)^{1/3} ile **Schwarzschild yarıçapı** kesişimi → M_min = (1/G)√(3c⁶/32πGρ_n) ≈ 8,3 M☉; *"Altında R_ρ > R_s — sıkışmış cisim **ufkunun dışında** kalır, karadelik oluşamaz."*
→ **Formül ve sayı aynen geçerli** (r_ph = 2μ = R_s sayısal olarak birebir; 8,26 M☉), ama **anlamı değişir**: ufuk eşiği değil **gölge/foton-küresi eşiği**. "Karadelik oluşamaz" → "gölge oluşamaz". Kütle boşluğu okuması korunur.

## C-9 · **`Kisim_6_Kanitlar\03_Ekvatoral_Vorteks_ve_Yorunge_Anomalileri.md:178`**
*"**Karşı Kayıt — kalan kalem.** Λ yapısı yalnız **birinci mertebeyi** (γ=1) verir. Merkür'ün günberi kayması ayrıca ortamın ikinci mertebe tepkisini (β, O(Φ²/c₀⁴)) gerektirir ve **henüz türetilmemiştir.** Teorinin GR'ın klasik sınavları karşısındaki **kalan tek boşluğu** budur (7.4 md.12)."*
→ Kutu tümüyle yeniden yazılmalı: boşluk kapandı.

## C-10 · **`Kisim_7_Tartisma_ve_Sonuc\04_Tartisma_ve_Sonuc.md:165`** (md.14)
Madde başlığı *"İkinci mertebe tepki (β parametresi) — Merkür günberi kayması"*; içeriği "birinci mertebe tamamen kapatıldı, β belirsiz". → Madde **kapanan kalemler** bölümüne taşınmalı; β = 1 türetimi ve 0,69σ kaydı yazılmalı.

## C-11 · **`Kisim_7\04_Tartisma_ve_Sonuc.md:119`**
*"Yerel saatle ölçülen λ'da **Λ'nın hangi kuvvetinin artakaldığı**, M-42'nin Λ mekaniğiyle titizce kurulmadan yazılmamalıdır… **Kalem: λ'nın Λ bağımlılığının M-42 çatısında türetilmesi.**"*
→ Üstel çatıda **yeniden kurulmalı** (λ = c_loc/f = c₀Λ²/(f₀Λ) = c₀Λ/f₀ → tam biçim λ ∝ e^{−Φ/c₀²}; Dünya yüzeyi kestirimi 7×10⁻¹⁰ değişmez). Kalem artık kapatılabilir.

## C-12 · **`Kisim_7\04:193 (iii)`** + **`19_Ek_M_Blok_I:167`** + **`:355`**
*"**Λ ölçeklemesi çıkmaz** — maddenin ortam içindeki bağlı yapısının modelini gerektirir"* / *"Cetvellerin ve saatlerin neden tam Λ ile ölçeklendiği (M-42'nin γ_ℓ=−1'i)…"*
→ **Kısmen kapanır, tam kapanmaz.** Üstel yapıyla artık türetilmiş olan şey Λ'nın **biçimi**dir (stiff'te K = ρc² = P olduğundan oransal düşüş → exp). Açık kalan yalnız **γ_ℓ = −1** (cetvel kanalı üssü), hâlâ yerel değişmezlik gözleminden sabitli. Kalem daraltılarak yeniden yazılmalı — silinmemeli.

## C-13 · **`Kisim_4_Bilimin_Tekilligi\02_Evrensel_Sabitler_4_Sinirlar_ve_Itirazlar.md:63`**
*"(Kalan kalem: Merkür günberi kayması için ayrıca β parametresi — ortamın ikinci mertebe tepkisi — gerekir; bkz. 7.4 md.12.)"* → Parantez kaldırılıp kapanış kaydı konmalı.

## C-14 · **`Kisim_4\02_Evrensel_Sabitler_4:99`** (§4.2.16)
*"GR'ın ürettiği kalan sayıların (**Merkür günberi kayması** — ikinci mertebe β gerektirir; **r_ISCO**; **kritik dönüş limitleri**) aynı yolla bağımsızca türetilmesi, teorinin önündeki en büyük matematiksel sınav olarak durmaktadır."*
Ayrıca **`:91`**: *"kara deliklerin dönüş limitlerini… reddetmez"*.
→ Merkür listeden çıkar. **r_ISCO ve kritik dönüş limitleri ise C sınıfı yeniden hesap ister:** ufuk olmayan bir yapıda ISCO ve Kerr tavanı ayrı türetilmeli — üstel metrikte hesaplanmamıştır.

## C-15 · **`19_Ek_M_Blok_I_Eylem_Ilkesi.md:204, 211, 217, 225`** — M-46 ÇEKİRDEK DEĞİŞİKLİK NOKTASI
- `:204` Varsayım 3: *"(∂P/∂χ)_ρ ≡ −C"* (sabit) → **−C·(P/P₀)**
- `:211` Adım 2: *"δP = −Cχ ⟹ P(r) = P₀ − CNq_n/4πr"* → **P(r) = P₀·exp(−Cχ/P₀) = P₀e^{−4μ/r}**
- `:217` Sonuç kutusu: aynı düzeltme; `:218`'in 𝒢 = Cq_n/4πρ_n m_n **birinci mertebede aynen** kalır (tam ivme: a = −(𝒢M/r²)e^{−4μ/r}, SINAV C'de oran 1,0000000000)
- `:225` Geçerlilik Sınırı: *"**güçlü-alan davranışı yazılmamıştır**"* → **yazıldı** (üstel yapı güçlü-alan uzantısının kendisi)
- `:208–210` **Poisson denklemi ∇²χ = −q_n n_m ve χ = Nq_n/4πr DEĞİŞMEZ** — vurgulanarak korunmalı.

## C-17 · **`19_Ek_M_Blok_I:243`**
*"𝒢≠0, P ∝ 1/r ve P'nin kaynakta **doğrusal** olmasını birlikte ister"* (dokuz elenen yolun ortak öncülü).
→ Öncül gevşetilmeli: istenen şey **χ'nin 1/r olması**dır, P'nin χ'de doğrusallığı değil. **Dokuz elemenin dokuzu da ayakta kalır** (hepsi χ'nin uzaklık yasasını hedefliyor) — bu, önerinin M-46'nın eleme tablosunu hiç zedelemediğinin kaydıdır ve açıkça yazılmalı.

## C-18 · **`19_Ek_M_Blok_I:268`**
*"Zincir denetimi: Cχ/P₀ ile 4Φ/c₀² aynı olmalıdır ve Dünya yüzeyinde 2,7777×10⁻⁹ ↔ 2,7844×10⁻⁹ — %0,24."*
→ Üstel yapıda bu **tanım gereği tam** olur: Cχ/P₀ ≡ −ln(P/P₀) ≡ 4Φ/c₀². %0,24'lük artık, Φ'nin gözlemsel girdisinin hatasıdır. Denetim cümlesi buna göre güçlendirilebilir.

## C-19 · Φ'NİN TANIMI — SEMBOL DÜZEYİNDE KARAR GEREKİYOR
**`Kisim_8_Ekler\08_Sembol_Sozlugu.md:130`** ve **`:217 (S-28)`**, **`10_Ek_M_Blok_B:54`**, **`17_Ek_B:29`**
Mevcut: *"Φ ≡ (P₀−P)/ρ_n ≥ 0; dış alanda Φ = +𝒢M/r"* — **iki eşitlik de TAM olarak** kurulmuş (17 Ağu 2026 kararı).
→ Üstel yapıda **ikisi aynı anda tam olamaz**: P = P₀e^{−4Φ/c₀²} ise (P₀−P)/ρ_n = Φ − 2Φ²/c₀² + … İki seçenek:
- **(a)** (P₀−P)/ρ_n ilişkisi "birinci mertebede" diye işaretlenir, Φ ≡ 𝒢M/r tam kalır;
- **(b)** Φ **logaritmik kuyu derinliği** olarak yeniden tanımlanır: **Φ ≡ −(c₀²/4)·ln(P/P₀)** — bu tanım hem Φ = 𝒢M/r'yi hem Λ = e^{−Φ/c₀²}'yi **tam** yapar ve zayıf alanda eski tanıma iner.
**(b) daha temizdir** ve 17 Ağustos kararının ruhunu (Φ = kuyu derinliği, pozitif) bozmaz. Karar S-28'de kayda geçmeli; Φ_it = −Φ ilişkisi her iki seçenekte korunur.

## C-20 · UFUK DİLİ — **`Kisim_11_Astronomik_Dogrulamalar\03_Kutle_Spin_Iliskisi_ve_Zarf_Rejimleri.md`**
Etkilenen satırlar: **`200`** (*"Karadelikler | zarf yok, **ufuk var**"*), **`1006`** (L(M,t) kutusunda *"**ufuk tavanı** 𝒢M²/c_yerel"*), **`1014`** (*"Kırılma tavanı **olay ufkunda** değerlendirilirse (R = 2𝒢M/c₀²)…"*), **`1021`**, **`1022`** (*"R4 | zarf yok, ufuk var"*), **`1623`**, **`1805`** (üç-kollu kutuda *"≤ 𝒢_yerel/c_yerel | **ufuk var**"*), **`1856`**, **`1858`**, **`1916`**, ayrıca SVG etiketleri **`53`, `459`, `1268`, `1694`, `1734`**.
→ Üstel Λ = e^{−μ/r} **hiçbir sonlu r'de sıfırlanmaz: UFUK YOK, TEKİLLİK YOK.** Sayısal hiçbir şey değişmez (2μ = R_s birebir), dolayısıyla 290 kompakt nesnenin tavan sınavı, R4 rejimi, 918 ↔ 898 oranı **aynen ayakta**. Değişen tek şey **ontolojik etiket**: "ufuk tavanı" → "**gölge / foton-küresi tavanı**" (r_ph = 2μ). Şekil etiketleri de dahil sistematik terim değişimi gerekir.
Ek olarak **`:857`**: *"Standart fizikte a*≤1 Kerr geometrisinin mutlak sınırıdır… tek bir nesnede a*>1 ölçülürse standart çerçeve çöker"* → ufuksuz yapıda tavanın gerekçesi Kerr geometrisi olamaz; kavrama/kilitli-kafes gerekçesine yeniden bağlanmalı.

## C-21 · **`Kisim_11\04_Saturn_Halkalari_ve_Dikey_Salinim.md:937 (ii)`** ve **`:1367 (11.4-iv/ii)`**
*"(ii) Λ_grav ile Λ_kin'in birlikte büyük olduğu durumlar (**derin kuyuda hızlı hareket**), çünkü çarpım yapısı iki terimin ayrı ayrı ölçülmesinden farklı bir öngörü verir… **Üçü de hesaplanmamıştır.**"*
→ **HESAPLANDI.** Ana oturumun eylemi (S = −mc₀²∫Λ_g√(1−V²/c_loc²)dt) tam olarak bu çarpım yapısıdır; günberi hesabı zayıf-kuyu/hızlı-hareket ucunu, karadelik yörüngeleri derin-kuyu ucunu kapsar. Kalem (ii) kapanır; (i) M→1 ve (iii) tercihli çerçeve açık kalır.

## C-22 · **`Kisim_11\04_Saturn:910`** (kutulu) + **`:922`** — Λ_kin'de HANGİ c?
Kutu: Λ = Λ_grav·Λ_kin, **Λ_kin = √(1 − V²/c²)** — "c" belirsiz. Satır 922 (kapsam kuralı 2) doğru cevabı zaten veriyor: *"M = V/c_loc olduğundan…"*.
→ Kutu **açıkça c_loc yazmalı**: Λ_kin = √(1 − V²/c_loc²), c_loc = c₀Λ_grav². Bu ikinci-mertebe-duyarlı bir ayrımdır ve günberi hesabının kullandığı biçimdir; c₀ yazılırsa yörünge denklemi bozulur. Aynı düzeltme **`00_KARNE:264`** kutusunda ve **`Kisim_3_Makro_Evren\04_Kutle_Itim_Mekanizmasi.md:292, 308`**'de gerekli.

---

# B SINIFI — DOĞRUSAL BİÇİM AÇIKÇA YAZILI (üstel + "birinci mertebede" notu)

Tümü aynı işlem: `Λ ≡ e^{−Φ/c₀²}` (tam) yazılıp `= 1 − Φ/c₀² + O(Φ²/c₀⁴)` birinci mertebe kesimi olarak eklenecek.

| Dosya:satır | Mevcut metin |
|---|---|
| `Kisim_8_Ekler\18_5_Kuvvet_Matematigi.md:1292` | **ANA TANIM EVİ** — kutulu `Λ ≡ 1 − Φ/c²; ℓ∝Λ, f∝Λ, c_loc∝Λ²` |
| `18_5:1268–1272` | `ε ≡ Φ/c₀²`, `c_loc = c₀(1+γ_c ε)` doğrusal ansatz — üstel için `ln`-açılımına çevrilmeli (γ'lar aynı kalır) |
| `18_5:1277, 1280–1283, 1286` | Üç kısıt (γ_f=−1, γ_c=−2, γ_ℓ=−1) — birinci mertebede aynen geçerli, "ε'nin birinci mertebesi" notu |
| `18_5:1300` | `n_eff = 1/Λ² = 1+2Φ/c₀²` — ikinci eşitlik birinci mertebe |
| `18_5:1317` | M-19 simetri notu: `1/γ ≈ 1−v²/2c² ↔ Λ = 1−Φ/c₀²` |
| `18_5:52` | Sembol tablosu satırı: `Λ | Yerel madde ölçek çarpanı, 1−Φ/c₀²` |
| `18_5:1611` | H.1 katalog tablosu M-42 satırı: `Λ=1−Φ/c₀²; c_loc∝Λ²` |
| `Kisim_8_Ekler\08_Sembol_Sozlugu.md:15` | **R-10 kuralı**: "daima madde ölçeği Λ = 1−Φ/c₀² yazılır" |
| `08_Sembol_Sozlugu.md:87` | Λ sembol satırı + değer kolonu `1−Φ/c₀²` |
| `08_Sembol_Sozlugu.md:130` | Φ satırı: "Λ = 1−Φ/c₀²'de geçen Φ budur" *(C-19 ile birlikte)* |
| `08_Sembol_Sozlugu.md:200` | **S-11**: "Λ = madde ölçeği (1−Φ/c₀², **resmî tanım**)" |
| `08_Sembol_Sozlugu.md:217` | **S-28**: "Λ = 1−Φ/c₀²; M-42" *(C-19)* |
| `Kisim_2_Mikro_Evren\04_Isik_Hizi_ve_Zerre.md:43` | Kutuda `Λ ≡ 1−Φ/c²` (+`:44–46` yapısal, A) |
| `Kisim_1_Giris\06_Evrenaki_Terminolojisi.md:55` | Zerre-Saati tanımı: `Λ = 1−Φ/c₀²` |
| `Kisim_1_Giris\06_Evrenaki_Terminolojisi.md:81` | Sözlük satırı: `Λ = 1−Φ/c₀²`; değer `Dünya yüzeyi 1−7×10⁻¹⁰` (üstelde aynı) |
| `Kisim_4\02_Evrensel_Sabitler_4:55` | "madde ölçeği Λ = 1−Φ/c₀²" (İtiraz 3, 2 çarpanı) |
| `Kisim_4\02_Evrensel_Sabitler_4:81` | `Λ ≡ 1−Φ/c², ℓ∝Λ, ν∝Λ, c_loc=c₀Λ²` (İtiraz 5 katman 3) |
| `Kisim_4\03_Kutlecekimsel_Merceklenme.md:19` | "madde ölçeği Λ = 1−Φ/c₀²" (+`:20` A) |
| `Kisim_6_Kanitlar\02_Kutlecekimsel_Kizila_Kayma_Sentezi.md:8` | Notasyon kutusu: `Λ ≡ 1−Φ/c₀²` |
| `Kisim_6\02:37` | `f_tik ∝ Λ²/Λ = Λ, Λ ≡ 1−Φ/c²` |
| `Kisim_6\02:79` | "**Birinci mertebede** Λ = 1−Φ/c₀²" — nitelemesi **zaten var**, yalnız tam biçim eklenecek |
| `Kisim_6\03_Ekvatoral_Vorteks:174` | "madde ölçeğinin (Λ = 1−Φ/c₀²)" |
| `Kisim_6\05_Galaktik_Yorungeler.md:1287` | `Λ ≡ 1−Φ/c²; ℓ,f∝Λ, c_loc=c₀Λ²` |
| `Kisim_6\98_Ne_Ogrendik.md:11` | "Λ = 1−Φ/c₀² madde ölçeğidir, Ek M-42" |
| `Kisim_8_Ekler\13_Ek_M_Blok_E:68` | Varsayım 4 / ölçek ayrımı: `Λ ≡ 1−Φ/c₀²` |
| `13_Ek_M_Blok_E:91` | "**Birinci mertebede** Λ = 1−Φ/c₀²" — niteleme var |
| `13_Ek_M_Blok_E:124` | Varsayım 3: `Λ ≡ 1−Φ/c₀² madde ölçeğidir` |
| `13_Ek_M_Blok_E:134` | Kutulu `ν_tik ∝ Λ/γ, Λ ≡ 1−Φ/c²` |
| `Kisim_8_Ekler\10_Ek_M_Blok_B:55` | M-8 Varsayım 5: `Λ = 1−Φ/c₀²`, `δc/c₀ = 2δf/f` |
| `Kisim_8_Ekler\17_Ek_B:29` | Ek B.3: `Λ=1−Φ/c₀²`, `δc/c₀ = −2Φ/c₀²` |
| `Kisim_8_Ekler\07_Matematiksel_Ekler.md:16` | Blok H özeti: `Λ=1−Φ/c₀² (c_loc=c₀Λ²)` |
| `Kisim_11\04_Saturn:874` | `Λ_grav = 1−Φ/c₀²` |
| `Kisim_11\04_Saturn:910` | Kutulu `Λ_grav = 1−Φ/c²` *(+C-22)* |
| `00_KARNE_Dogrulama_Durumu.md:264` | Kutulu `Λ_grav = 1−Φ/c₀²` *(+C-22)* |
| `Kisim_7\04_Tartisma_ve_Sonuc.md:127` | md.8: "madde ölçeği Λ=1−Φ/c₀² cetveli ve saati *aynı* çarpanla ölçekler" |
| `Kisim_7\04_Tartisma_ve_Sonuc.md:165` | md.14: "madde ölçeği Λ = 1−Φ/c₀²" *(+C-10)* |

---

# A SINIFI — YAPISAL, ÜSTEL İLE AYNEN GEÇERLİ (işlem gerekmez)

Bu vuruşların hepsi ℓ,f ∝ Λ · c_loc = c₀Λ² · n_eff = 1/Λ² · c_loc/(ℓf)≡1 · ν_tik ∝ Λ/γ · Λ_kaynak/Λ_alıcı ilişkilerini kullanıyor; üstel Λ ile **her mertebede** korunuyor. Λ_ref sadeleşmesi, ortak-mod null'ları, δc/c₀ = 2δf/f (birinci mertebe), ΔP_yüzey = ρ_nΦ (birinci mertebe) hepsi ayakta.

- **`18_5_Kuvvet_Matematigi.md`**: 15, 29, 38, 1086–1088, 1094, 1100, 1120, 1146, 1190, 1298, 1299, 1304, 1315, 1334, 1338, 1339, 1443, 1618, 1626, 1682, 1687, 1688, 1689, 1690, 1691, 1692
  - `:1334` (jeodetik taşınım payı, Fermat holonomisi ∮∂⊥(ln n_eff)ds = 4πμ/r): **üstelde de tam** — ln n_eff = −2 ln Λ = 2Φ/c₀², holonomi birinci mertebede aynı. `:1335` tur açığı (−½, Λ_kin) da aynen. **6.606 mas/yıl korunur.**
  - `:1358` (ortak-mod ↔ diferansiyel; M-15/M-16 etkilenmez): aynen geçerli.
- **`08_Sembol_Sozlugu.md`**: 13, 21, 45 (R-11), 88, 90, 160, 176
- **`Kisim_6\02_Kutlecekimsel_Kizila_Kayma_Sentezi.md`**: 5, 7, 9, 11, 33, 35, 39, 41, 42, 44, 46, 68, 70, 71, 72, 74, 76, 77, 83, 85, 88, 90, 91, 108, 115
  - `:11` özellikle önemli: *"Kavrama Yasası c₀=√(P/ρ) (M-1) **yayılma hızının kendisidir ve değişmeden korunur**"* — üstel yapı bu cümleyi **tam** yapar; doğrusal yazımda O(Φ²)'de bozulur. **Üstel geçişin kitap-içi en güçlü dayanağı bu satırdır.**
- **`Kisim_8_Ekler\13_Ek_M_Blok_E`**: 54, 65, 67, 80, 81, 82, 85, 88, 89, 93, 95, 98, 101, 102, 104–109, 113, 122, 123, 127, 128, 129, 137, 140, 145, 148
- **`Kisim_8_Ekler\10_Ek_M_Blok_B`**: 46, 54, 60, 61, 62, 63, 80 · **`17_Ek_B`**: 39 · **`15_Ek_M_Blok_G`**: 187 · **`19_Ek_M_Blok_I`**: 85
- **`Kisim_4\02_Evrensel_Sabitler_4`**: 57, 82 · **`03_Kutlecekimsel_Merceklenme`**: 20
- **`Kisim_2\04_Isik_Hizi_ve_Zerre`**: 38–40 (Yön Kuralı, k<1), 44, 45, 46, 48
- **`Kisim_6\03_Ekvatoral_Vorteks`**: 169, 174, 176, 182, 184, 185, 186 (ξ zinciri: bükülme → c_loc=c₀Λ² → δc/c₀=2Φ/c₀² → ξ → 41,0 mas/yıl — **birinci mertebe, korunur**)
- **`Kisim_6\05_Galaktik_Yorungeler`**: 1285, 1287, 1291, 1300, 1303, 1308, 1310, 1320, 1322, 1324, 1422 (G-6 yanlışlama ölçütü)
  - Galaktik alanda Φ/c₀² ≤ 1,6×10⁻⁶ → üstel/doğrusal fark ~10⁻¹²; **163 galaksi fiti, a₀ ∝ c₀⁻³ zinciri, |δc/c₀| ≤ 3×10⁻⁶ kilidi aynen geçerli. Tersine hesabın 0,29 sonucu ve altı kademlik uçurum değişmez.**
- **`Kisim_1_Giris\03_Evrenaki_Postulasi`**: 306, 308, 343, 356, 359, 372, 384 (Ek C envanteri; **Λ yeni serbest parametre getirmez — üstelde de getirmiyor**)
- **`Kisim_3_Makro_Evren\04_Kutle_Itim_Mekanizmasi`**: 292, 293, 305, 308 (Λ_kin ile M&M/rezonatör null'ları) *(c belirsizliği → C-22)*
- **`Kisim_3_Makro_Evren\07_Kozmolojik_Genisleme`**: 37 (Λ_kaynak/Λ_alıcı → kozmolojik zamansal ölçek oranı; **oran yapısı korunur**)
- **`Kisim_9_Mikro_Dogrulamalar\06_Zitterbewegung`**: 42 (α_is kararlılığı = ortak-mod öngörüsü; **üstelde de tam**)
- **`Kisim_11\04_Saturn`**: 908, 910, 912, 920, 922, 929, 933, 935, 1318 (Λ_kin türetimi Prandtl–Glauert; **üstel Λ_grav ile çarpım yapısı tam tutarlı** — C-21/C-22'ye bakınız)
- **`Kisim_7\04_Tartisma_ve_Sonuc`**: 157, 159, 169, 181, 182, 183, 219 · **`Kisim_6\98_Ne_Ogrendik`**: 21 (Λ_ref) · **`Kisim_7\07`**: 15 (zamansal ↔ konumsal ayrımı; "M-42'nin Λ yapısıyla karıştırılmamalıdır" uyarısı aynen doğru)
- **`00_KARNE`**: 248–262, 266, 269, 270, 275, 285, 293, 359, 640, 709

---

# ETKİLENMEYENLER (N/A) — farklı Λ, dokunulmamalı

| Yer | Ne |
|---|---|
| `Kisim_11\04_Saturn:582, 594, 595, 602, 1306, 1357` · `00_KARNE:41` | **Halka kalınlığı Λ ≡ 2π𝒢Σ/Ω²a_b** — tamamen başka nicelik. ⚠️ **Sembol çakışması:** S-11 "indissiz Λ daima madde ölçeğidir" diyor; M-42 yeniden yazılırken bu çakışma daha görünür olacak — `Λ_h` gibi indislenmesi önerilir. |
| `Kisim_6\00:46, 95` · `Kisim_7\07:12, 53, 91, 141, 240` · `Kisim_6\05:181, 199, 251` · `08_Sembol:87, 200` (parantez) | **ΛCDM / Λ_kozm** — standart fizik aktarımı |
| `19_Ek_M_Blok_I:169, 175, 328, 336, 352, 362` · `Kisim_12\98:76` | **Λ_Σ** (kohezyon uzunluğu, M-50) |
| `08_Sembol:176` · `dump.tmp:55` | **λ_z** (Zerre aralığı) |
| `Kisim_2\05_Mikro_Makro:364, 394, 404, 410, 436` | JS değişken adları (`erwLambda`) |
| `Kisim_11\99_Kaynakca:61` · `Kisim_4\99_Kaynakca:37` | Kaynakça açıklamaları |
| `Kisim_9\08_Polarizasyon:20` · `Kisim_11\03:14, 42, 44, 189, 855, 857, 899, 909, 1006, 1625, 1805` · `Kisim_1\03:356` | Terk edilmiş `c_yerel` yazımı (R-11 ihlali) — üstelden bağımsız, ayrı hijyen kalemi |
| `Kisim_7\00_CALISMA_Acik_Konular:627` | Λ, Zerre aralığı anlamında kullanılmış → **S-11 ihlali** (λ_z olmalı); çalışma dosyası |
| `dump.tmp:35, 41, 55` | Geçici dosya, yayın metni değil |

**Λ HİÇ GEÇMEYEN kısımlar (doğrulandı):** `Kisim_5_Deneyler` (tümü) · `Kisim_10_Yorunge_Dogrulamasi` (tümü — a₀/galaktik zincirler Λ kullanmıyor, üstel geçiş Kısım 10'a **hiç dokunmuyor**) · `Kisim_12_Kut_Motoru` (yalnız Λ_Σ) · `Kisim_13_Hakem_Degerlendirmeleri`.

---

# ÖZET MUHASEBE

**Kapanan:** Merkür 43″ (0,69σ) · M-42'nin β açık ucu · H.2 öncelik 1′ · 7.4 md.14 · 6.3.3 Karşı Kayıt · 11.4-iv(ii) · Λ'nın *biçiminin* türetilmemişliği · M-46'nın "güçlü-alan yazılmamıştır" sınırı.
**Yeni kazanılan ayırt edicilik:** gölge b_krit = 2eμ (+%4,63 vs GR, EHT) · ufuk yok / tekillik yok · sonlu kızıla kayma.
**Yeni yazılması gereken:** M-44 dalga kanalı (C-16) · Φ'nin tanımı (C-19) · "ufuk" dilinin Kısım 11.3 boyunca gölge diline çevrilmesi (C-20) · r_ISCO ve kritik dönüş limitleri (C-14).
**Bedeli, dürüst kayıt:** "ses hızı küresel olarak tam c₀" iddiası düşer (yerine yerel c_loc); 1PN'de GR'dan ayrışma tümüyle biter (β de 1); Λ_kin kutularındaki "c" belirsizliği artık zararsız değil, c_loc olarak yazılmak zorunda.
**Kırılan hiçbir A sınıfı ilişki yok:** bükülme 1,7512″, Shapiro 247 µs, jeodetik 6.606 mas/yıl, GP-B 41,0 mas/yıl, LAGEOS 30,6/31,4 mas/yıl, kızıla kayma −Φ/c₀², Lorentz null'ları, P₀ = 6,07×10³³ Pa, 163 galaksi fiti, M_min ≈ 8,3 M☉ — hepsi sayısal olarak korunuyor.