# ORTAMIN HIZ ALANI — Çözüm

> Çalışma dosyası · 17 Ağustos 2026 (Opus) · `DEVIR_KAYDI_ustel_olcek.md` §5'in kapatılması
> Sınav betiği: `ortam_hiz_alani_sinavi.py` · İlgili: `ortam_dolasimi_mp.py`

---

## 1. Problem

Üstel ölçek yapısının Merkür kapanışı, ortamın Güneş çerçevesinde **durgun** olması varsayımına asılıydı. Ama M-9'un Geçerlilik Sınırı ortamın dolaşmak *zorunda* olduğunu söylüyordu:

> *"Kütle çevresindeki gradyan bölgesinde ortam tepkisiz değildir — **Euler denklemi gereği** gradyana cevap verir; ama cevabı düşmek değil **dolaşmaktır**: gradyan, dolaşımın merkezcil ivmesiyle siklostrofik dengede taşınır, ∇P/ρ₀ = v_θ²/r"*

Bununla ρₙ/ρ₀ = 4 birleşince **v_θ = 2v_yör tam** çıkıyor (Merkür yörüngesinde 95,76 km/s, Ω_m = 1,65×10⁻⁶ rad/s). Gözlem ise **Ω_m ≲ 1,4×10⁻¹⁸ rad/s** bırakıyor — **1,18×10¹² kat** aşım.

## 2. Teşhis: M-9 kohezyonsuz denklem kullanıyor

**Euler denklemi, kesme gerilmesi taşımayan (kohezyonsuz) akışkanın denklemidir.** Böyle bir ortamda gerçekten tek seçenek vardır: statik denge imkânsızdır (∇·σ = −∇P ≠ 0), o hâlde ya düşer ya dolaşır.

**Ama teorinin ortamı kohezyonsuz değildir.** Kitabın kendi kayıtları:
- **M-4:** ortam, basıncına ek olarak bir **kohezyon (çekme) dayanımı** Σ taşır.
- **M-5:** Σ, **kesme modülü** rolündedir — *"kohezyon kanalının elastik sinyal hızı, kesme-hızı formunun G_s → Σ karşılığıdır: v_m = √(Σ/ρ₀)"*. Ve Σ/P₀ > 10⁸ (Bell/Salart 2008).
- **M-5 Geçerlilik Sınırı:** *"v_m enerji/madde taşımaz; **ortam topografyasının (gradyan deseninin) ayar sinyalidir**."* — yani statik gradyan deseninin taşıyıcısı zaten kohezyon kanalı olarak ilan edilmiş.
- **M-46:** χ alanının zaman sektörü kohezyon kanalındadır (v_m > 10⁴c₀).

Kesme taşıyabilen bir ortam, basınç kuyusunu **dolaşmadan, statik elastik dengede** tutabilir.

## 3. Çözüm: statik kohezyon dengesi (tam türetim)

Gerilme tensörü σ_ij = −P δ_ij + τ_ij (τ izsiz). Statik denge ∇·σ = 0; küresel simetride radyal bileşen:

$$\frac{d\sigma_{rr}}{dr} + \frac{2\sigma_{rr}-\sigma_{\theta\theta}-\sigma_{\varphi\varphi}}{r} = 0$$

İzsizlik (τ_rr + 2τ_θθ = 0 ⇒ τ_rr − τ_θθ = 3τ_rr/2) ile:

$$\frac{d\tau_{rr}}{dr} + \frac{3\tau_{rr}}{r} = \frac{dP}{dr} = \frac{\rho_n\mathcal{G}M}{r^2} \;\Longrightarrow\; \frac{1}{r^3}\frac{d(r^3\tau_{rr})}{dr} = \frac{\rho_n\mathcal{G}M}{r^2}$$

Sonsuzda sönen çözüm:

$$\boxed{\;\tau_{rr} = \frac{\rho_n\mathcal{G}M}{2r} = \frac{\rho_n\Phi}{2} = \frac{\Delta P}{2}\;,\qquad \tau_{\theta\theta}=\tau_{\varphi\varphi}=-\frac{\tau_{rr}}{2}\;}$$

**Gereken kesme gerilmesi, basınç açığının tam yarısıdır.** Kohezyon dayanımıyla kıyas (`ortam_hiz_alani_sinavi.py`):

| Konum | Φ/c₀² | τ_rr (Pa) | τ_rr/Σ_min |
|---|---|---|---|
| Merkür yörüngesi | 2,55×10⁻⁸ | 3,10×10²⁶ | **5,1×10⁻¹⁶** |
| Dünya yörüngesi | 9,87×10⁻⁹ | 1,20×10²⁶ | 2,0×10⁻¹⁶ |
| Güneş yüzeyi | 2,12×10⁻⁶ | 2,58×10²⁸ | 4,2×10⁻¹⁴ |
| Dünya yüzeyi | 6,96×10⁻¹⁰ | 8,45×10²⁴ | 1,4×10⁻¹⁷ |
| Samanyolu (Güneş yarıçapı) | 4,45×10⁻⁷ | 5,40×10²⁷ | 8,9×10⁻¹⁵ |
| Nötron yıldızı yüzeyi | 0,172 | 2,09×10³³ | 3,4×10⁻⁹ |

**Σ'nın yalnız ALT SINIRIYLA bile 14–15 mertebe marj var** — nötron yıldızı yüzeyinde dahi 9 mertebe. Elastik zorlanma ε ~ τ/Σ ~ 10⁻¹⁶.

**Hüküm:** Ortam kuyuyu dolaşmadan tutabilir. Dolaşım bir *zorunluluk* değil, **serbest bir dinamik durumdur** (açısal momentumla belirlenir); kohezyon farkı kapatır. Genel denge:

$$\frac{1}{\rho_0}\frac{dP}{dr} = \frac{v_\theta^2}{r} + \underbrace{\frac{1}{\rho_0}\left(\frac{d\tau_{rr}}{dr}+\frac{3\tau_{rr}}{r}\right)}_{\text{kohezyon payı}}$$

v_θ = 2v_yör, kohezyon payının sıfır olduğu **kohezyonsuz üst sınırdır**; v_θ = 0 ise kohezyon tüm yükü taşır. İkisi arası her değer izinli.

## 4. Matter neden kohezyonu görmüyor (kritik tutarlılık kontrolü)

Doğal itiraz: ortam kendi içinde dengede (∂_jσ_ij = 0) ise, içine konan cisme etkiyen net traksiyon da sıfır olmaz mı — yani kütle-itim kaybolmaz mı?

**Hayır, ve gerekçe M-2'nin kendi ifadesinde:** *"Bir cisme etkiyen itim, cismin nükleonlarının **deplase ettiği hacimle** orantılıdır"* (M-2, Varsayım 2). Deplase edilen hacim bir **skalerdir** (izli/isotropik nicelik). Bir deplasman cebi, gerilme tensörünün **izine** (yani basınca) bağlanır; τ **izsizdir** ve saf hacim dışlamasıyla çiftlenmez. Dolayısıyla:
- Ortam kendini **kesmeyle** ayakta tutar (madde bunu görmez),
- Madde yalnız **basınç gradyanını** görür: a = −∇P/ρₙ (M-2 aynen geçerli).

M-2'nin işaret konvansiyonu bölümündeki *"∇P tek başına 'kuvvet' olarak adlandırılamaz; skaler basınç farkı ΔP ile gösterilir"* uyarısı, bu ayrımın kitapta zaten sezildiğinin kaydıdır.

## 5. Ortam hangi çerçevede durgun? — iç içe zarf yapısı

Statik olmak yetmez; **hangi çerçevede** statik? Cevap kitabın kendi zarf yapısında (Postülat 7 / DY-1 / 11.4.8.1'in Hill yarıçapı):

| Zarf | Erim | Sonuç |
|---|---|---|
| **Güneş'in galaktik zarfı** | R_Hill = **1,225 pc = 2,53×10⁵ AU** | Oort bulutu (~10⁵ AU) dahil **tüm Güneş sistemi içeride** ⇒ ortam Güneş çerçevesinde durgun |
| **Dünya'nın zarfı** | R_Hill = **234,9 R_⊕** | 11.4.8.1'in verdiği **235 R_⊕** ile birebir ✓ (bağımsız doğrulama) |
| GPS yörüngesi | 4,17 R_⊕ | Dünya zarfının **içinde** |
| Merkür yörüngesi | — | Güneş zarfının içinde, **kendi zarfının dışında** |

**Bu yapı iki hesabı birden doğru veriyor:**
- **Merkür:** kendi zarfının dışında, Güneş çerçevesinde durgun ortama göre V = 47,87 km/s ⇒ günberi hesabının kullandığı tam kurulum ✓
- **GPS:** Dünya zarfının içinde, Dünya çerçevesinde durgun ortama göre V = yörünge hızı ⇒ −7 µs/gün kinematik terim ✓

Yani "ortam merkezî cismin çerçevesinde durgundur" varsayımı keyfi değil, **zarf yapısının doğrudan sonucudur** — ve iç içe geçmiş olması, farklı ölçeklerde farklı referans çerçevesi kullanılmasını gerekçelendiriyor.

## 6. Kazanç: Merkür artık ortam dönüşünün en hassas ölçümü

| Nicelik | Değer |
|---|---|
| Ortam dönüşü üst sınırı (1σ) | **\|Ω_ortam\| ≤ 1,4×10⁻¹⁸ rad/s** |
| Merkür yörüngesinde teğetsel hız | **≤ 81 nm/s** |
| Güneş spinine oran | 4,8×10⁻¹³ |
| Bir tam tur | 1,4×10¹¹ yıl = evren yaşının **10 katı** |

**Teorinin yeni kaydı:** Güneş sisteminin ortamı, evren yaşı ölçeğinde bile fiilen dönmüyor. Bu, kohezyonla tutulan statik kuyunun doğal hâlidir; dolaşan bir vorteks olsaydı Merkür onu görürdü. **Merkür günberi kayması, teorinin ortam-dönüşü ölçüm aletidir** — GR'de karşılığı olmayan bir okuma.

## 7. Kitapta düzeltilmesi gerekenler

| Yer | Şimdi | Olacak |
|---|---|---|
| **M-9 Geçerlilik Sınırı** (`10_Ek_M_Blok_B:116-118`) | *"Euler denklemi gereği… cevabı düşmek değil **dolaşmaktır**… siklostrofik dengede"* | Yeniden yazılmalı: Euler **kohezyonsuz** limittir. Kohezyonlu ortamda (M-4/M-5, Σ/P₀>10⁸) **statik elastik denge** açıktır: τ_rr = ρₙΦ/2, Σ'nın 15 mertebe altında. Siklostrofik dolaşım **kohezyonsuz üst sınırdır**, zorunluluk değil. Gözlem (Merkür) statik kolu **seçer**. *"Madde düşer, ortam dolaşır"* → **"Madde düşer, ortam gerilir"** (ya da "ortam kesmeyle tutunur"). |
| **M-9 Açık Uçlar** | *"Siklostrofik denge profilinin v_θ(r) sürüklenme zarfıyla nicel eşlenmesi"* | Kalem **yeniden tanımlanır**: eşlenecek şey dolaşım değil, **kohezyon payı ile dolaşım payının bölüşümü**; Güneş sisteminde gözlem bölüşümü ~%100 kohezyona veriyor. |
| **M-37 profil teoremi** (v_θ = 2v_yör) | "teorem" | **Statüsü düşer:** kohezyonsuz üst sınır. Türetimi doğru (oran √(ρₙ/ρ₀) = 2 tam) ama *zorunluluk* değil. |
| **M-2** | — | Ek not: cisim gerilme tensörünün **izine** (basınca) bağlanır; izsiz kesme payı deplasman cebine kuvvet uygulamaz. Bu, ortamın kendini kesmeyle tutmasının madde dinamiğini etkilemediğinin kaydıdır. |
| **11.4.8.1 / Λ_kin** | *"V, maddenin yerel ortama göre hızıdır"* | Ek netleştirme: yerel ortam, **cismin kendi zarfının dışındaki** ambiyans ortamdır ve merkezî cismin çerçevesinde durgundur (Hill yarıçapı hiyerarşisi). Tam kavrama okuması (V=0) yanlıştır — müon/GPS zaman genleşmesini yok eder. |
| **Yeni kayıt** | — | Merkür günberi = ortam dönüşü ölçümü, \|Ω\| ≤ 1,4×10⁻¹⁸ rad/s. KARNE'ye sınav satırı. |

## 8. Kapanmayan / kontrol edilmesi gereken (dürüst kayıt)

1. **✅ GALAKTİK ZİNCİR KONTROLÜ — YAPILDI, TEMİZ ÇIKTI.** M-37 (`18_5:258-286`) okundu; kitap ayrımı **kendisi** yapmış:
   - `:265` **Madde profili** (gözlenen dönüş eğrisi): |a_madde| = (1/ρₙ)dP/dR ve v_yör²/R = |a_madde| ⇒ **v_yör = √(R|a_madde|)**. Girdileri yalnız **M-2 + akı geometrisi** (M-35 küresel / M-38 silindirik). Ortamın hız alanı **hiç girmiyor**.
   - `:268` **Ortam profili** v_θ = 2v_yör: ayrı bir kol, siklostrofik denge (M-22) varsayımıyla.
   - `:280` kitabın kendi cümlesi: *"**Gözlenen daima orta kolondur.** Sağ kolon ortamın kendi dolaşımıdır ve **görünmez olduğu için ölçülmemiştir**."*
   - `:286` üç bileşen listesi: *silindirik akı geometrisi (M-38) + ortamın kendi radyal dengesi (M-22) + maddenin gradyanda serbest düşmesi (M-2)* — ama türetimin fiilen kullandığı `:265`'te yalnız M-2 + akı geometrisidir; **M-22 madde kolonunda yük taşımıyor** (basınç profili χ-Poisson/akı yapısından gelir, ortamın dönüşünden değil).
   **⇒ Düz dönüş eğrisi, a₀, 163 galaksi fiti, W penceresi: HİÇBİRİ ortamın fiilen dolaşmasına dayanmıyor.** Kohezyon çözümü galaktik zinciri kırmıyor. Değişen tek şey **sağ kolonun statüsü**: türetilmiş öngörü değil, **kohezyonsuz üst sınır** (ve Güneş sisteminde gözlem onu ~0'a indiriyor).
   *Kalan küçük iş:* `:286`'nın üç-bileşen listesinden M-22'nin çıkarılması veya rolünün "işaret konvansiyonu, M-35 ile zaten redundant" diye netleştirilmesi. M-22'nin kendi varsayımı (`14_Ek_M_Blok_F:15`: *"makro girdap kararlı ve eksenel simetriktir; akış saf teğetseldir"*) artık **opsiyonel dinamik durum** olarak etiketlenmeli.
2. **Eş-düzlemlilik ve prograd yörüngeler.** Kitap bunları Güneş makro-vorteksine bağlıyorsa, dolaşım ≈ 0 ile bu anlatı yeniden kurulmalı. İyi haber: **F5 (yanal itim, sin2θ)** düzlem seçimini gövdenin *kendi dönüşünden* veriyor — dolaşıma ihtiyaç duymuyor gibi. **Doğrulanmadı (kalan iş).**
3. **Zarf sınırındaki kayma tabakası.** 11.4.8.1/7.4'ün kaydı (Dünya zarfı 30 km/s, Güneş zarfı 220 km/s). Statik resimde bunlar gerçek kesme tabakalarıdır; gereken gerilme ~ρ₀v² = 3,3×10²⁷ Pa ≪ Σ ⇒ taşınabilir. Yitim ve tork hesabı hâlâ açık (mevcut açık kalem, değişmedi).
4. **Σ'nın alt sınır olması.** Tüm marjlar Σ ≥ 10⁸P₀ alt sınırıyla hesaplandı; Σ'nın gerçek değeri serbest (Ek C). Marj 14-15 mertebe olduğundan sonuç Σ'ya duyarsız — ama kayda geçmeli.
5. **Statik çözümün tekliği.** τ_rr = ρₙΦ/2 + C/r³ ailesinin C = 0 kolu seçildi (sonsuzda sönme). C ≠ 0 kolları iç sınır koşuluna bağlı; kaynak içinde eşlenmesi yapılmadı.
