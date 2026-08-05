# 11.3 Kütle–Dönüş (Spin) İlişkisi: Zarf Rejimleri

Bir gök cisminin **kendi ekseni etrafındaki dönüşü** ile kütlesi arasında bir yasa var mıdır? Standart astrofizik bu soruya cisim sınıfı başına ayrı ve birbirine bağlanmayan cevaplar verir: gezegenler için "oluşum diskinin rastlantısal türbülansı", yıldızlar için "manyetik frenleme", nötron yıldızları için "çökmede açısal momentum korunumu", karadelikler için "Kerr metriğinin geometrik sınırı", asteroitler için "çarpışma geçmişi ve ışınım torkları". Evrenakı'da dönüşün kaynağı tektir — nükleonun **4B çift dönüşü** (Kısım 3 §3.4.4; Kısım 1 §1.4) — ve bu ayrı görünümler tek bir değişkenden çıkar: **zarf durumu.**

Bu bölüm dört iş yapar. Önce dört ana sınıfın ölçülmüş spin verisini tek eksende toplar (11.3.2–11.3.6); sonra yasanın yapısını, teorinin kendi ilkel nicelikleriyle yazılışını ve hangi kaleminin türetilip hangisinin türetilmediğini kayda geçirir (11.3.7); ardından zarf-bağımlı denklemi üç tavanla kurar (11.3.8); son olarak denklemi **yedi sınıf ve 734.000 gövdelik gerçek katalog verisiyle** sınar ve yasanın tanım alanını ölçer (11.3.9, altı sınav). Bölümün konusu yalnız spindir; yörünge hareketi ve kilitlenme ayrı mekanizmaların (M-37, M-43) konusudur ve burada yalnız spini etkiledikleri yerde anılır.

> **Gözlemsel Hedef.** Cisim sınıflarının ölçülmüş dönüşlerinde tek bir biçimin — $J=\mathcal{A}M^{2}$ — geçerli olduğunu, sınıflar arasındaki farkın üste değil **katsayıya** yazıldığını göstermek; ve katsayının kendisi yerel ortama bağlı olduğu için asıl değişmezi **oran** olarak kurmak:
> $$\frac{\mathcal{A}_0}{\mathcal{G}_{yerel}/c_{yerel}}=\frac{m_p}{2m_e}=918\quad\text{(yapısal sonuç)}\qquad\longleftrightarrow\qquad 898\quad\text{(beş gezegen)}$$
> Bu oranda hiçbir yerel nicelik yoktur — teoride $\mathcal{G}$ de $c$ de sabit olmadığı hâlde oran sabittir, çünkü ikisi birlikte kayar. Sabit $\mathcal{G}$ ve sabit $c$ varsayan bir çerçevede bu cümle kurulamaz.

<p style="margin:20px 0;padding:16px;border:1px solid #22c55e;border-radius:10px;background:rgba(34,197,94,0.07)"><a href="Simulasyon/kisim11/panel_kutle_spin.html" target="_blank" rel="noopener" style="display:inline-block;padding:12px 22px;background:#166534;color:#ffffff;border-radius:8px;font-weight:700;text-decoration:none;font-size:1.05em">&#9654;&#65039; ETKİLEŞİMLİ PANELİ AÇ — Kütle–spin sınavı (yedi sınıf, 93.224 gövde)</a><br><span style="color:#a1a1aa;font-size:0.9em;display:inline-block;margin-top:8px">Tarayıcıda ayrı sayfada, tam ekran açılır. <b>On bir kategori tek tek açılıp kapatılır</b> (asteroit, gezegen, yıldızaltı ×2, yıldız ×2, beyaz cüce, nötron yıldızı ×2, karadelik ×2) ve gerçek ölçümler teorinin eğrileriyle <b>birlikte</b> çizilir: yükleme yasası 𝒜₀, ufuk tavanı 𝒢/c, kırılma tavanı, dış tork izi ve ölçülmüş kütle tabanı. Dört eksen seçeneği vardır — 𝒜 = J/M² (iki yatay çizgi görünümü), J, η<sub>z</sub> ve dönme dönemi. 𝒜₀ çarpanı kaydırıcısı, seçili sınıfın hangi katsayıyı gerektirdiğini canlı gösterir. Rejim düğmeleri (R0…R4) yalnız o rejimi bırakır; imleç en yakın gövdenin M, 𝒜, J, η<sub>z</sub> ve P değerlerini okur. Tek dosya, dış bağımlılık yok.</span></p>

---

## 11.3.1 Soru, Ayrım ve Ölçüm Zemini

**Spin ile yörünge karıştırılmaz.** Ay'ın Dünya çevresindeki dolanımı yörüngedir; Dünya'nın 23 saat 56 dakikalık kendi dönüşü spindir. Bu bölümdeki her veri noktası ikincisidir.

Dört sınıfın spini dört farklı teknikle ölçülür ve güvenilirlikleri farklıdır:

| Sınıf | Ölçüm tekniği | Tipik hassasiyet | Veri kaynağı |
|---|---|---|---|
| Asteroit / küçük gövde | ışık eğrisi dönemi; çap ışınım ölçümünden | dönemde $10^{-3}$; kütle varsayılan yoğunluğa bağlı | **NASA-JPL SBDB** — 19.929 cisim (11.3.9, Sınav 6) |
| Gezegenler | doğrudan dönem (yüzey/manyetosfer/halka sismolojisi) | $10^{-4}$ ve üstü | IAU/NASA-JPL gezegen veri sayfaları |
| Yıldızlar | tayf çizgisi Doppler genişlemesi ($v\sin i$), leke dönemleri (Kepler/TESS) | ~%10–20 + $\sin i$ izdüşümü; leke dönemlerinde izdüşüm yok | Fukuda (1982); Głębocki & Gnaciński (2005); **Santos ve ark. (2021)** — 39.591 Kepler dönemi; **Gaia DR3** `vbroad`+FLAME — 671.765 yıldız (11.3.9, Sınav 5) |
| Nötron yıldızları | **pulsar zamanlaması** — atım periyodu | $10^{-15}$'e kadar; astrofiziğin en hassas ölçümü | ATNF Pulsar Kataloğu (Manchester ve ark., 2005) — **2.527 pulsar** (Sınav 6) |
| Karadelikler | X-ışını süreklilik/Fe Kα yansıması; GW dalga biçimi | $a^*$'da ±0,05–0,3 | Reynolds (2021); **LIGO-Virgo-KAGRA GWTC** — 273 birleşme (Sınav 6) |
| Yıldızaltı (kahverengi cüce, genç dev) | dönemsel parlaklık değişimi; yüksek çözünürlüklü tayf | ~%10–30 (kütleler model bağımlı) | Bryan ve ark. (2018); Tannock ve ark. (2021); Snellen ve ark. (2014) |

Kütle tarafında gezegenler ve çift sistemler (pulsar zamanlaması + Shapiro gecikmesi; GW dalga biçimi) hassastır; tek yıldızların kütlesi tayf türünden (~%10), kahverengi cücelerin kütlesi evrim modellerinden gelir — son satırın kütleleri bu yüzden en zayıf halkadır.

**Ortak para birimi.** Sınıflar kütlece 17 mertebe ayrıldığı için karşılaştırma iki türetik nicelikle yapılır:

$$j\equiv\frac{J}{M}\ \ [\mathrm{m^2/s}] \qquad\text{ve}\qquad \mathcal{A}\equiv\frac{J}{M^{2}}\ \ [\mathrm{m^2\,s^{-1}\,kg^{-1}}]$$

$\mathcal{A}$'nın seçimi keyfî değildir: hem gezegen yükleme katsayısı hem kompakt cisimlerin tavanı ($J_{max}=\mathcal{G}_{yerel}M^2/c_{yerel}$ — standart adıyla Kerr sınırı) **aynı $M^2$ biçimindedir.** O hâlde her sınıfın tek işareti katsayısıdır. Boyutsuz yazımı $a^*=cJ/\mathcal{G}M^2$'dir; kompakt olmayan cisimlerde 1'i aşabilir, çünkü yarıçapları itim yarıçaplarının çok üstündedir ve tavan onları bağlamaz.

> **Ölçüm birimi uyarısı — $\mathcal{G}$ ve $c$ burada sabit değildir.** Evrenakı'da ne kütle-itim katsayısı $\mathcal{G}$ ne de dalga hızı $c$ evrensel sabittir: $c_{yerel}=\sqrt{P/\rho_0}$ (Postülat 4) ve $\mathcal{G}=Cq_n/4\pi\rho_nm_n$ (M-35) — ikincisi ortamın yerel yoğunluğuyla ölçeklenir, M-45'in *"yerel ölçülen $G$"* ifadesi tam bunu söyler. Bu bölümdeki her $\mathcal{G}$ ve $c$, **ölçümün yapıldığı yerdeki** değerdir. Sonuçların yerel-bağımsız biçimi 11.3.7(c–d)'de kurulur.

---

## 11.3.2 Ana Diyagram: Dört Sınıf Tek Eksende

Aşağıdaki diyagram bölümün bütün iddiasını tek bakışta verir. Eksenler kütle (17 mertebe) ve özgül açısal momentum (13 mertebe); iki kesikli doğru **aynı eğime (1)** sahiptir çünkü ikisi de $J\propto M^2$ biçiminin $j$–$M$ düzlemindeki izidir; yeşil eğri ise zarflı gövdeleri bağlayan üçüncü sınırdır:

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 620" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Dort sinifta ozgul acisal momentum, yukleme dogrusu, kirilma ve Kerr tavanlari">
<rect x="0" y="0" width="940" height="620" fill="#0b0f19"/>
<line x1="90.0" y1="58" x2="90.0" y2="530" stroke="#182338"/>
<line x1="134.4" y1="58" x2="134.4" y2="530" stroke="#182338"/>
<text x="134.4" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁴</text>
<line x1="178.9" y1="58" x2="178.9" y2="530" stroke="#182338"/>
<line x1="223.3" y1="58" x2="223.3" y2="530" stroke="#182338"/>
<text x="223.3" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁶</text>
<line x1="267.8" y1="58" x2="267.8" y2="530" stroke="#182338"/>
<line x1="312.2" y1="58" x2="312.2" y2="530" stroke="#182338"/>
<text x="312.2" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁸</text>
<line x1="356.7" y1="58" x2="356.7" y2="530" stroke="#182338"/>
<line x1="401.1" y1="58" x2="401.1" y2="530" stroke="#182338"/>
<text x="401.1" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁰</text>
<line x1="445.6" y1="58" x2="445.6" y2="530" stroke="#182338"/>
<line x1="490.0" y1="58" x2="490.0" y2="530" stroke="#182338"/>
<text x="490.0" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10³²</text>
<line x1="534.4" y1="58" x2="534.4" y2="530" stroke="#182338"/>
<line x1="578.9" y1="58" x2="578.9" y2="530" stroke="#182338"/>
<text x="578.9" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁴</text>
<line x1="623.3" y1="58" x2="623.3" y2="530" stroke="#182338"/>
<line x1="667.8" y1="58" x2="667.8" y2="530" stroke="#182338"/>
<text x="667.8" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁶</text>
<line x1="712.2" y1="58" x2="712.2" y2="530" stroke="#182338"/>
<line x1="756.7" y1="58" x2="756.7" y2="530" stroke="#182338"/>
<text x="756.7" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁸</text>
<line x1="801.1" y1="58" x2="801.1" y2="530" stroke="#182338"/>
<line x1="845.6" y1="58" x2="845.6" y2="530" stroke="#182338"/>
<text x="845.6" y="548" fill="#8fa3c0" font-size="12" text-anchor="middle">10⁴⁰</text>
<line x1="890.0" y1="58" x2="890.0" y2="530" stroke="#182338"/>
<line x1="90" y1="530.0" x2="890" y2="530.0" stroke="#182338"/>
<text x="82" y="534.0" fill="#8fa3c0" font-size="12" text-anchor="end">10⁸</text>
<line x1="90" y1="496.3" x2="890" y2="496.3" stroke="#182338"/>
<line x1="90" y1="462.6" x2="890" y2="462.6" stroke="#182338"/>
<text x="82" y="466.6" fill="#8fa3c0" font-size="12" text-anchor="end">10¹⁰</text>
<line x1="90" y1="428.9" x2="890" y2="428.9" stroke="#182338"/>
<line x1="90" y1="395.1" x2="890" y2="395.1" stroke="#182338"/>
<text x="82" y="399.1" fill="#8fa3c0" font-size="12" text-anchor="end">10¹²</text>
<line x1="90" y1="361.4" x2="890" y2="361.4" stroke="#182338"/>
<line x1="90" y1="327.7" x2="890" y2="327.7" stroke="#182338"/>
<text x="82" y="331.7" fill="#8fa3c0" font-size="12" text-anchor="end">10¹⁴</text>
<line x1="90" y1="294.0" x2="890" y2="294.0" stroke="#182338"/>
<line x1="90" y1="260.3" x2="890" y2="260.3" stroke="#182338"/>
<text x="82" y="264.3" fill="#8fa3c0" font-size="12" text-anchor="end">10¹⁶</text>
<line x1="90" y1="226.6" x2="890" y2="226.6" stroke="#182338"/>
<line x1="90" y1="192.9" x2="890" y2="192.9" stroke="#182338"/>
<text x="82" y="196.9" fill="#8fa3c0" font-size="12" text-anchor="end">10¹⁸</text>
<line x1="90" y1="159.1" x2="890" y2="159.1" stroke="#182338"/>
<line x1="90" y1="125.4" x2="890" y2="125.4" stroke="#182338"/>
<text x="82" y="129.4" fill="#8fa3c0" font-size="12" text-anchor="end">10²⁰</text>
<line x1="90" y1="91.7" x2="890" y2="91.7" stroke="#182338"/>
<line x1="90" y1="58.0" x2="890" y2="58.0" stroke="#182338"/>
<text x="82" y="62.0" fill="#8fa3c0" font-size="12" text-anchor="end">10²²</text>
<rect x="90" y="58" width="800" height="472" fill="none" stroke="#8fa3c0"/>
<text x="490.0" y="572.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">kütle M [kg]</text>
<text x="26" y="294.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 294.0)">özgül açısal momentum j = J/M [m²/s]</text>
<text x="90.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.A — Tek biçim, iki katsayı: yükleme ile tavan arasındaki oran m_p/2m_e = 918</text>
<line x1="120.6" y1="530.0" x2="742.9" y2="58.0" stroke="#ffb84d" stroke-width="1.8" stroke-dasharray="7 5"/>
<text x="264.9" y="416.1" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">yükleme:  j = 𝒜₀M      (𝒜₀ ≈ 2×10⁻¹⁶ ; yerel ρ₀ ile ölçeklenir)</text>
<line x1="252.3" y1="530.0" x2="874.6" y2="58.0" stroke="#ff6b6b" stroke-width="1.8" stroke-dasharray="7 5"/>
<text x="558.2" y="293.5" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">tavan:  j = (𝒢_yerel / c_yerel) M      (a* = 1)</text>
<path d="M 263.3 405.7 L 266.2 404.6 L 269.0 403.5 L 271.9 402.4 L 274.7 401.4 L 277.6 400.3 L 280.4 399.2 L 283.3 398.1 L 286.1 397.0 L 289.0 396.0 L 291.8 394.9 L 294.7 393.8 L 297.5 392.7 L 300.4 391.6 L 303.2 390.6 L 306.1 389.5 L 308.9 388.4 L 311.8 387.3 L 314.6 386.2 L 317.5 385.2 L 320.3 384.1 L 323.2 383.0 L 326.0 381.9 L 328.9 380.8 L 331.7 379.8 L 334.6 378.7 L 337.4 377.6 L 340.3 376.5 L 343.1 375.4 L 346.0 374.3 L 348.8 373.3 L 351.7 372.2 L 354.5 371.1 L 357.4 370.0 L 360.2 368.9 L 363.0 367.9 L 365.9 366.8 L 368.7 365.7 L 371.6 364.6 L 374.4 363.5" stroke="#5ce6a8" stroke-width="1.8" stroke-dasharray="3 4" fill="none"/>
<text x="378.9" y="367.5" fill="#5ce6a8" font-size="12" text-anchor="start" font-weight="normal">kırılma tavanı (R ≈ R_J)</text>
<circle cx="305.7" cy="389.6" r="9" fill="none" stroke="#5ce6a8" stroke-width="2"/>
<text x="297.7" y="373.6" fill="#5ce6a8" font-size="12" text-anchor="end" font-weight="normal">kesişim ≈ 4 M_J</text>
<circle cx="125.9" cy="514.0" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="131.9" y="505.0" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Mars</text>
<circle cx="168.9" cy="496.6" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="174.9" y="511.6" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Dünya</text>
<circle cx="223.8" cy="456.4" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="214.8" y="446.4" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Neptün</text>
<circle cx="256.9" cy="424.8" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="263.9" y="439.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Satürn</text>
<circle cx="280.1" cy="416.8" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="269.1" y="406.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Jüpiter</text>
<circle cx="220.6" cy="456.4" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<text x="229.6" y="467.4" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Uranüs</text>
<path d="M 328.1 399.0 L 334.1 410.0 L 322.1 410.0 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="270.1" y="397.0" fill="#5ce6a8" font-size="11" text-anchor="start" font-weight="normal">β Pic b</text>
<path d="M 344.5 401.8 L 350.5 412.8 L 338.5 412.8 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="352.5" y="421.8" fill="#5ce6a8" font-size="11" text-anchor="start" font-weight="normal">Luhman 16B</text>
<path d="M 351.3 388.6 L 357.3 399.6 L 345.3 399.6 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="277.3" y="396.6" fill="#5ce6a8" font-size="11" text-anchor="start" font-weight="normal">2M1047+21</text>
<path d="M 357.5 385.4 L 363.5 396.4 L 351.5 396.4 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="366.5" y="385.4" fill="#5ce6a8" font-size="11" text-anchor="start" font-weight="normal">2M1219+31</text>
<circle cx="485.6" cy="328.4" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="493.6" y="323.4" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">O5</text>
<circle cx="448.7" cy="342.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="456.7" y="353.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">B5</text>
<circle cx="434.9" cy="352.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="423.9" y="343.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">A0</text>
<circle cx="423.5" cy="369.3" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="431.5" y="380.3" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">F0</text>
<circle cx="414.4" cy="366.7" r="5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="350.4" y="369.7" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">T Tauri</text>
<circle cx="414.4" cy="429.4" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="422.4" y="440.4" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">Güneş</text>
<circle cx="420.9" cy="463.4" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="428.9" y="474.4" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">Crab</text>
<circle cx="428.5" cy="428.1" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="436.5" y="432.1" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">J0740</text>
<circle cx="420.9" cy="416.9" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="368.9" y="407.9" fill="#b58cff" font-size="11" text-anchor="start" font-weight="normal">716 Hz</text>
<circle cx="450.8" cy="410.5" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="458.8" y="421.5" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">A0620</text>
<circle cx="473.3" cy="362.5" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="411.3" y="355.5" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Cyg X-1</text>
<path d="M 494.0 346.5 L 500.0 352.5 L 494.0 358.5 L 488.0 352.5 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="502.0" y="363.5" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">GW150914</text>
<path d="M 510.0 333.3 L 516.0 339.3 L 510.0 345.3 L 504.0 339.3 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="518.0" y="334.3" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">GW190521</text>
<rect x="704.2" y="188.6" width="10" height="10" fill="none" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="717.2" y="206.6" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Sgr A*</text>
<rect x="845.5" y="72.8" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="804.5" y="68.8" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">M87*</text>
<circle cx="112.0" cy="70.0" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="125.0" y="74.0" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">gezegenler (içi boş: hizasız)</text>
<path d="M 112.0 83.0 L 118.0 94.0 L 106.0 94.0 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="125.0" y="93.0" fill="#5ce6a8" font-size="12" text-anchor="start" font-weight="normal">yıldızaltı: kahverengi cüce / genç dev</text>
<circle cx="112.0" cy="108.0" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="125.0" y="112.0" fill="#4dd2ff" font-size="12" text-anchor="start" font-weight="normal">yıldızlar (içi boş: T Tauri)</text>
<circle cx="406.3" cy="496.6" r="5.5" fill="#ffffff" stroke="#ffffff" stroke-width="1.6"/>
<text x="398.3" y="486.6" fill="#ffffff" font-size="11" text-anchor="end" font-weight="normal">beyaz cüceler</text>
<circle cx="112.0" cy="127.0" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="125.0" y="131.0" fill="#b58cff" font-size="12" text-anchor="start" font-weight="normal">nötron yıldızları</text>
<circle cx="112.0" cy="165.0" r="5" fill="#ffffff" stroke="#ffffff" stroke-width="1.6"/>
<text x="125.0" y="169.0" fill="#ffffff" font-size="12" text-anchor="start" font-weight="normal">beyaz cüceler (n = 31, medyan)</text>
<circle cx="112.0" cy="146.0" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="125.0" y="150.0" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">karadelikler (◆ GW, ■ SMBH)</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.A: Dört sınıfın ölçülmüş özgül açısal momentumu. Yükleme doğrusu ve tavan aynı eğime (1) sahiptir — ikisi de J ∝ M²; aralarındaki 898 kat m_p/2m_e = 918'dir. Yeşil kesikli eğri, zarflı gövdeler için kırılma tavanı: yükleme doğrusunu ≈4 M_J'de keser, üstünde yıldızaltı cisimler (üçgen) her iki çizginin de altında kalır. Veri: IAU/NASA-JPL; Fukuda 1982; ATNF; Reynolds 2021; GWTC-3; Bryan 2018 / Tannock 2021.</em></p>
</div>

Okuma dört cümledir:

1. **Gezegenler yükleme doğrusuna oturur** — $J=\mathcal{A}_0M^2$: 4B yüklemenin tam ifadesi (rijit zarf, kapalı kanal).
2. **Karadelikler tavan doğrusuna yaslanır** — $J\le(\mathcal{G}_{yerel}/c_{yerel})M^2$: aynı biçim, ama tavanda. İki doğru paraleldir ve aralarında **898 kat** vardır; 11.3.7(d) bunun $m_p/2m_e$ olduğunu gösterecek.
3. **Yıldızlar ve nötron yıldızları iki doğrunun arasında, aşağı doğru kayar** — zarfları momentumu ortama geri sızdırır (yıldız: manyetize rüzgâr; NS: dipol ışıması).
4. **Yıldızaltı cisimler (üçgen) her iki çizginin de altındadır** — çünkü ≈4 $M_J$ üzerinde yükleme doğrusu **kırılma tavanını** keser; oranın üstünde yasa fiziksel olarak sürdürülemez (11.3.8).

| Sınıf | Zarf durumu | $\mathcal{A}=J/M^2$ | $a^*$ |
|---|---|---|---|
| Gezegenler (serbest) | rijit zarf, kanal kapalı | $(1{,}2$–$4{,}6)\times10^{-16}$ | 540–2100 |
| Yıldızaltı (kahverengi cüce, genç dev) | kırılma tavanının altında | $(1$–$2)\times10^{-17}$ | 50–90 |
| Yıldız doğumu (T Tauri, OBA) | plazma zarf, taze | $(1$–$3)\times10^{-18}$ | 5–16 |
| Güneş (4,6 Gyr) | konvektif zarf, kanal açık | $4{,}9\times10^{-20}$ | **0,22** |
| Nötron yıldızları | zarf fırlatılmış | $(0{,}001$–$0{,}09)\times10^{-18}$ | 0,006–0,42 |
| Karadelikler | zarf yok, ufuk var | $\le2{,}2\times10^{-19}$ | 0,12–0,99 ≤ 1 |

Dikkat çekici iki ayrıntı: Güneş bugün o kadar frenlenmiştir ki katsayısı bir karadeliğin **tavanının beşte birine** düşmüştür ($a^*_\odot=0{,}22$); en hızlı nötron yıldızı bile ($a^*=0{,}42$) tavanın yarısına varmaz. Tavanı yalnız karadelikler doldurur.

---

## 11.3.3 Gezegenler: Rijit Zarf — Korunan İfade

Veri IAU/NASA-JPL değerleridir; $L=\lambda MR^2\omega$ ile hesaplanır ($\lambda=I/MR^2$; Dünya/Mars'ta ölçüm, devlerde iç model):

| Gövde | $M$ (kg) | $P_{spin}$ | $v_{ekv}$ (m/s) | $L$ (kg m²/s) | $\mathcal{A}\times10^{16}$ |
|---|---|---|---|---|---|
| Mars | $6{,}42\times10^{23}$ | 24,62 sa | 241 | $1{,}91\times10^{32}$ | 4,6 |
| Dünya | $5{,}97\times10^{24}$ | 23,93 sa | 465 | $5{,}86\times10^{33}$ | 1,6 |
| Neptün | $1{,}02\times10^{26}$ | 16,11 sa | 2.683 | $1{,}57\times10^{36}$ | 1,5 |
| Satürn | $5{,}68\times10^{26}$ | 10,56 sa | 9.960 | $7{,}51\times10^{37}$ | 2,3 |
| Jüpiter | $1{,}90\times10^{27}$ | 9,93 sa | 12.572 | $4{,}33\times10^{38}$ | 1,2 |
| *Uranüs (hizasız, $\theta=98°$)* | $8{,}68\times10^{25}$ | 17,24 sa | 2.588 | $1{,}32\times10^{36}$ | 1,8 |
| **Merkür (bastırılmış)** | $3{,}30\times10^{23}$ | 58,65 gün | 3,0 | $8{,}4\times10^{29}$ | 0,077 |
| **Venüs (bastırılmış)** | $4{,}87\times10^{24}$ | 243 gün (retro) | 1,8 | $1{,}8\times10^{31}$ | 0,0076 |

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 540" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Gezegenlerde donme acisal momentumu">
<rect x="0" y="0" width="940" height="540" fill="#0b0f19"/>
<line x1="90.0" y1="50" x2="90.0" y2="460" stroke="#182338"/>
<text x="90.0" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²³</text>
<line x1="232.9" y1="50" x2="232.9" y2="460" stroke="#182338"/>
<text x="232.9" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁴</text>
<line x1="375.7" y1="50" x2="375.7" y2="460" stroke="#182338"/>
<text x="375.7" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁵</text>
<line x1="518.6" y1="50" x2="518.6" y2="460" stroke="#182338"/>
<text x="518.6" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁶</text>
<line x1="661.4" y1="50" x2="661.4" y2="460" stroke="#182338"/>
<text x="661.4" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁷</text>
<line x1="804.3" y1="50" x2="804.3" y2="460" stroke="#182338"/>
<text x="804.3" y="478" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁸</text>
<line x1="90" y1="460.0" x2="890" y2="460.0" stroke="#182338"/>
<line x1="90" y1="425.8" x2="890" y2="425.8" stroke="#182338"/>
<text x="82" y="429.8" fill="#8fa3c0" font-size="12" text-anchor="end">10³⁰</text>
<line x1="90" y1="391.7" x2="890" y2="391.7" stroke="#182338"/>
<line x1="90" y1="357.5" x2="890" y2="357.5" stroke="#182338"/>
<text x="82" y="361.5" fill="#8fa3c0" font-size="12" text-anchor="end">10³²</text>
<line x1="90" y1="323.3" x2="890" y2="323.3" stroke="#182338"/>
<line x1="90" y1="289.2" x2="890" y2="289.2" stroke="#182338"/>
<text x="82" y="293.2" fill="#8fa3c0" font-size="12" text-anchor="end">10³⁴</text>
<line x1="90" y1="255.0" x2="890" y2="255.0" stroke="#182338"/>
<line x1="90" y1="220.8" x2="890" y2="220.8" stroke="#182338"/>
<text x="82" y="224.8" fill="#8fa3c0" font-size="12" text-anchor="end">10³⁶</text>
<line x1="90" y1="186.7" x2="890" y2="186.7" stroke="#182338"/>
<line x1="90" y1="152.5" x2="890" y2="152.5" stroke="#182338"/>
<text x="82" y="156.5" fill="#8fa3c0" font-size="12" text-anchor="end">10³⁸</text>
<line x1="90" y1="118.3" x2="890" y2="118.3" stroke="#182338"/>
<line x1="90" y1="84.2" x2="890" y2="84.2" stroke="#182338"/>
<text x="82" y="88.2" fill="#8fa3c0" font-size="12" text-anchor="end">10⁴⁰</text>
<line x1="90" y1="50.0" x2="890" y2="50.0" stroke="#182338"/>
<rect x="90" y="50" width="800" height="410" fill="none" stroke="#8fa3c0"/>
<text x="490.0" y="500.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">kütle M [kg]</text>
<text x="26" y="255.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 255.0)">dönme açısal momentumu L [kg m²/s]</text>
<text x="90.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.B — L ∝ M² yapısal biçimi ile ölçüm  ·  bastırılmış ikili 300–4000 kat altta</text>
<line x1="118.6" y1="401.6" x2="875.7" y2="39.4" stroke="#ffb84d" stroke-width="1.8" stroke-dasharray="7 5"/>
<text x="625.7" y="131.6" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">yapısal biçim: L = 𝒜₀M² ,  𝒜₀ = C ℓ_ω³ / (4√2 m_n ρ₀ r_n)</text>
<line x1="147.1" y1="380.5" x2="832.9" y2="71.4" stroke="#8fa3c0" stroke-width="1.2" stroke-dasharray="2 5"/>
<text x="161.4" y="316.1" fill="#8fa3c0" font-size="11" text-anchor="start" font-weight="normal">ampirik fit: eğim 1,885 ± 0,065</text>
<circle cx="205.3" cy="347.9" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="213.3" y="341.9" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Mars</text>
<circle cx="343.7" cy="297.1" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="351.7" y="310.1" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Dünya</text>
<circle cx="520.0" cy="214.2" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="511.0" y="204.2" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Neptün</text>
<circle cx="626.4" cy="156.8" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="634.4" y="169.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Satürn</text>
<circle cx="701.2" cy="130.7" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="690.2" y="120.7" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Jüpiter</text>
<circle cx="509.8" cy="216.7" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<text x="519.8" y="229.7" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Uranüs</text>
<circle cx="164.1" cy="428.4" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="174.1" y="432.4" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Merkür</text>
<circle cx="331.0" cy="383.0" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="341.0" y="387.0" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Venüs</text>
<text x="140.0" y="415.6" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">girdap rekabetiyle bastırılmış (M-24):</text>
<text x="140.0" y="432.7" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">Merkür −%97,7 · Venüs −%100,3 (retrograd)</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.B: Gezegenlerde dönme açısal momentumu. Turuncu kesikli doğru yapısal biçimdir (𝒜₀ = C ℓ_ω³/4√2 m_n ρ₀ r_n), gri noktalı doğru ampirik fittir (eğim 1,885 ± 0,065). Bastırılmış Merkür/Venüs 300–4.000 kat altta; Uranüs (hizasız) içi boş.</em></p>
</div>

Beş serbest-hizalı gövdenin fiti $L\propto M^{1{,}885\pm0{,}065}$ ($R^2=0{,}996$) verir — tam kare ($M^2$) 1,8σ, $M^{5/3}$ 3,4σ uzaktadır; yani veri $M^2$'yi tercih eder ama tek başına dayatmaz. Katsayının geometrik ortalaması $\mathcal{A}_0=1{,}998\times10^{-16}$'dır. Kısım 3 §3.4.4'ün girdi setiyle üs $1{,}94$ çıkar; fark $\lambda$ ve dönem seçimlerinin payıdır.

Dört dürüstlük kaydı bağlayıcıdır:

- **Saçılma tabanı ±%30'dur** ve $\mathcal{A}$ tek tek gövdelerde 1,2–4,6 arasında gezinir ($\times10^{-16}$); "tek doğru" değil "tek güç yasası eğilimi" okunmalıdır. Yasanın ~2 kat hassasiyeti budur.
- **Merkür ve Venüs yasanın ihlali değil, ikinci mekanizmanın kanıtıdır:** Güneş girdabının kavraması (M-24) ifadeyi %97,7 ve %100,3 yutmuştur; doğrunun 300–4.000 kat altındadırlar ve kalıntı dönüşleri yerel girdap ritmine kilitlidir. Denklemde bu $(1-g)$ çarpanıdır (11.3.8, R1).
- **Uranüs hizasızdır** ($\theta\approx98°$): eksen devrilmesi yükleme verimini düşürür; fitte kullanılmaz, yine de banda yakın durması devrilme öncesi birikimin korunmasıyla tutarlıdır.
- **β Pictoris b yükleme rejiminde değildir.** Ölçülen $v_{ekv}=25$ km/s (Snellen ve ark., 2014 — bir ötegezegenin ilk spin ölçümü) yasanın verdiği 187 km/s'nin çok altındadır; ama bu bir başarısızlık değil **zorunluluktur**: 12 $M_J$'de yükleme doğrusu kırılma tavanının 1,5 katına çıkar (187 ↔ 125 km/s), yani orada yasa uygulanamaz. β Pic b kırılmanın 0,20'sinde döner — Jüpiter (0,30) ve Satürn (0,40) ile aynı banttadır. Ayrıntı 11.3.8'dedir.

---

## 11.3.4 Yıldızlar: Plazma Zarf — Açık Kanal ve Kraft Kırılması

Anakol yıldızlarında tayf türü başına ortalama dönme hızları (Fukuda, 1982; Głębocki & Gnaciński, 2005; $v\sin i$ izdüşüm ortalaması gerçek $v_{ekv}$'nun ~$\pi/4$'üdür):

| Tayf türü | $M$ ($M_\odot$) | $\langle v\sin i\rangle$ (km/s) |
|---|---|---|
| O5 | ~40 | ~190 |
| B0 | 16 | ~200 |
| B5 | 5,9 | ~220 |
| A0 | 2,9 | ~180 |
| A5 | 2,0 | ~150 |
| F0 | 1,6 | ~100 |
| **F5 — Kraft kırılması** | **1,3** | **~30** |
| G0 | 1,05 | ~8 |
| Güneş (G2) | 1,0 | 2,0 |
| K0–M0 | 0,85–0,5 | ~2–3 |

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 540" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Anakol yildizlarinda donme hizi ve Kraft kirilmasi">
<rect x="0" y="0" width="940" height="540" fill="#0b0f19"/>
<line x1="128.1" y1="50" x2="128.1" y2="460" stroke="#182338"/>
<text x="128.1" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">0.5</text>
<line x1="242.4" y1="50" x2="242.4" y2="460" stroke="#182338"/>
<text x="242.4" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">1.0</text>
<line x1="356.7" y1="50" x2="356.7" y2="460" stroke="#182338"/>
<text x="356.7" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">2.0</text>
<line x1="471.0" y1="50" x2="471.0" y2="460" stroke="#182338"/>
<text x="471.0" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">4</text>
<line x1="585.2" y1="50" x2="585.2" y2="460" stroke="#182338"/>
<text x="585.2" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">8</text>
<line x1="699.5" y1="50" x2="699.5" y2="460" stroke="#182338"/>
<text x="699.5" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">16</text>
<line x1="813.8" y1="50" x2="813.8" y2="460" stroke="#182338"/>
<text x="813.8" y="478.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">32</text>
<line x1="90" y1="460.0" x2="890" y2="460.0" stroke="#182338"/>
<text x="82.0" y="464.0" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">1</text>
<line x1="90" y1="381.2" x2="890" y2="381.2" stroke="#182338"/>
<text x="82.0" y="385.2" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">3</text>
<line x1="90" y1="302.3" x2="890" y2="302.3" stroke="#182338"/>
<text x="82.0" y="306.3" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">10</text>
<line x1="90" y1="223.5" x2="890" y2="223.5" stroke="#182338"/>
<text x="82.0" y="227.5" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">32</text>
<line x1="90" y1="144.6" x2="890" y2="144.6" stroke="#182338"/>
<text x="82.0" y="148.6" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">100</text>
<line x1="90" y1="65.8" x2="890" y2="65.8" stroke="#182338"/>
<text x="82.0" y="69.8" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">316</text>
<rect x="90" y="50" width="195.8" height="410" fill="#4dd2ff" opacity="0.06"/>
<line x1="285.8" y1="50" x2="285.8" y2="460" stroke="#4dd2ff" stroke-width="1.6" stroke-dasharray="6 5"/>
<rect x="90" y="50" width="800" height="410" fill="none" stroke="#8fa3c0"/>
<text x="490.0" y="500.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">kütle M [M☉]</text>
<text x="26" y="255.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 255.0)">ortalama dönme hızı ⟨v sin i⟩ [km/s]</text>
<text x="90.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.C — Kraft kırılması: konvektif zarf sınırında (1,3 M☉) dönüş 30 kat düşer</text>
<text x="275.8" y="72.0" fill="#4dd2ff" font-size="12" text-anchor="end" font-weight="normal">konvektif zarf — kanal açık</text>
<text x="295.8" y="72.0" fill="#4dd2ff" font-size="12" text-anchor="start" font-weight="normal">radyatif zarf — kanal kapalı</text>
<circle cx="852.7" cy="100.7" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="860.7" y="94.7" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">O5</text>
<circle cx="701.1" cy="97.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="709.1" y="91.1" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">B0</text>
<circle cx="536.0" cy="90.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="544.0" y="84.6" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">B5</text>
<circle cx="418.5" cy="104.4" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="426.5" y="98.4" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">A0</text>
<circle cx="357.1" cy="116.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="365.1" y="110.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">A5</text>
<circle cx="320.1" cy="144.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="328.1" y="138.6" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">F0</text>
<circle cx="285.8" cy="227.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="295.8" y="238.1" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">F5</text>
<circle cx="250.5" cy="317.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="260.5" y="328.6" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">G0</text>
<circle cx="242.4" cy="412.5" r="5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="252.4" y="423.5" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">Güneş</text>
<circle cx="215.5" cy="384.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="223.5" y="378.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">K0</text>
<circle cx="131.0" cy="384.8" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="139.0" y="378.8" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">M0</text>
<circle cx="242.4" cy="254.8" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<text x="251.4" y="248.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">T Tauri (1 Myr): genç Güneş 10 kat hızlıydı</text>
<path d="M 242.4 262.8 L 242.4 400.0" stroke="#ffb84d" stroke-width="1.2" stroke-dasharray="3 4" fill="none"/>
<text x="250.0" y="331.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Skumanich: ω ∝ t^(−1/2)</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.C: Anakol ortalama dönme hızları ve Kraft kırılması. Gölgeli bölge konvektif zarf (açık kanal): solda spin yaşla, sağda doğum ifadesiyle belirlenir.</em></p>
</div>

Tablo iki olgu barındırır ve ikisi de zarf dilinde tek cümledir:

1. **Kraft kırılması** (Kraft, 1967): $M\approx1{,}3\,M_\odot$'ta ortalama dönüş **30 kat** düşer. Bu kütle, yıldız yapısında **dış konvektif zarfın** ortaya çıktığı sınırdır. Konvektif zarf + manyetize rüzgâr = momentumu ortama sızdıran **açık kanal**; radyatif zarflı erken türlerde (O–A) kanal kapalıdır ve doğum ifadesi korunur. Spini belirleyen kütlenin kendisi değil, kütlenin dikte ettiği **zarf türüdür.** Kırılmanın keskinliği $\langle v\sin i\rangle$ ekseninde gerçektir; açısal momentuma çevrildiğinde $1{,}0$–$1{,}8\,M_\odot$ arasına yayılan bir yamaç olur (Sınav 5-ii).
   > **Keskinlik kaydı.** Kırılma $\langle v\sin i\rangle$ ekseninde keskindir; ama bu bölümün asıl niceliği olan $\eta_z$ ekseninde **keskin değildir.** 39.591 Kepler yıldızıyla ölçüldüğünde geçiş $1{,}0$–$1{,}8\,M_\odot$ arasına yayılan bir rampadır ve $1{,}3$'te süreksizlik göstermez (11.3.9, Sınav 5-ii). Nedeni yapısaldır: $\eta_z=L/\mathcal{A}_0M^2$ tanımı $R^2$ çarpanını içerir ve $R(M)$ artışı basamağı yayar. Zarf türünün anahtar olduğu iddiası ayakta kalır, "keskin süreksizlik" iddiası kalmaz.
2. **Açık kanallı yıldızlarda spin yaş fonksiyonudur** (Skumanich, 1972: $\omega\propto t^{-1/2}$; açık küme jirokronolojisiyle doğrulanmış). Bu yüzden geç-tip yıldızlar kütle–spin doğrusuna oturmaz ve oturmamalıdır — Kısım 3 §3.4.4'ün tanım alanı kaydı bu mekanizmanın ifadesidir.

Sızıntının nicel sağlaması bölümün en temiz sonuçlarından biridir. Güneş benzeri bir yıldızın katsayısı iki çağda ölçülebilir: T Tauri evresinde (1 Myr, $v\approx20$ km/s, konvektif $k^2\approx0{,}2$) $\mathcal{A}\approx3{,}5\times10^{-18}$; bugünkü Güneş'te ($J_\odot=1{,}92\times10^{41}$ kg m²/s, helyosismik — Pijpers, 1998) $\mathcal{A}=4{,}9\times10^{-20}$. Oran **72**; Skumanich yasasının öngörüsü $\sqrt{4600}=68$ — **%6 içinde.** Dört mertebelik zaman aralığında tek üslü sızıntı yasası tutmaktadır.

Doğum bandı da yerine oturur: kanal-kapalı erken türlerin katsayısı $(1$–$3)\times10^{-18}$, T Tauri ile aynı banttadır — yıldızlar **gezegen bandının ~100 kat altında doğar.** Bu açık, oluşumun kendisinde yaşanır: protoyıldız momentumunun çoğunu beslenme diskine ve disk-kilitlenmesine bırakır (teori dilinde: plazma zarf, kafesle rijit kuplaj kuramaz — deplasmanın $\phi$ kanalı zayıftır). Yıldız oluşumunun "açısal momentum problemi" olarak bilinen kalem, zarf çerçevesinde bir problem değil, plazma zarfının tanımlayıcı imzasıdır.

---

## 11.3.5 Nötron Yıldızları: Zarfını Fırlatmış Çekirdek

Kütlesi ölçülmüş pulsarlar (ATNF kataloğu; kütleler çift-sistem zamanlaması ve Shapiro gecikmesinden — NICER/Green Bank programları). $a^*$ sütunu her nesnenin **kendi ölçülen kütlesi ve kütlesine karşılık gelen yarıçapıyla**, $I\simeq0{,}35MR^2$ (gerçekçi NY durum denklemi) ile hesaplanmıştır — katalog geneli için kullanılan tekdüze varsayımdan farklıdır; ayrım aşağıda kayıtlıdır:

| Pulsar | $M$ ($M_\odot$) | $\nu$ (Hz) | $a^*$ | Sınıf |
|---|---|---|---|---|
| Vela | ~1,4 | 11,2 | 0,006 | genç |
| B1913+16 (Hulse–Taylor) | 1,440 | 16,9 | 0,008 | genç |
| Crab | ~1,4 | 29,9 | 0,015 | genç (doğumda ~50 Hz) |
| J0737−3039A (çift pulsar) | 1,338 | 44,1 | 0,025 | kısmen dönüştürülmüş |
| J1614−2230 | 1,908 | 317 | 0,12 | geri dönüştürülmüş |
| J0740+6620 | 2,08 | 347 | 0,11 | geri dönüştürülmüş |
| J0952−0607 | **2,35** | **707** | 0,20 | geri dönüştürülmüş |
| J1748−2446ad | (1,4 vars.) | **716** | 0,37 | geri dönüştürülmüş |

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 520" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Pulsarlarda boyutsuz spin dagilimi: yalitik ve cift sistem">
<rect x="0" y="0" width="940" height="520" fill="#0b0f19"/>
<line x1="183.3" y1="58.0" x2="183.3" y2="430.0" stroke="#182338" stroke-width="1.0"/>
<text x="183.3" y="448.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-4</tspan></text>
<line x1="360.0" y1="58.0" x2="360.0" y2="430.0" stroke="#182338" stroke-width="1.0"/>
<text x="360.0" y="448.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-3</tspan></text>
<line x1="536.7" y1="58.0" x2="536.7" y2="430.0" stroke="#182338" stroke-width="1.0"/>
<text x="536.7" y="448.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-2</tspan></text>
<line x1="713.3" y1="58.0" x2="713.3" y2="430.0" stroke="#182338" stroke-width="1.0"/>
<text x="713.3" y="448.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-1</tspan></text>
<line x1="890.0" y1="58.0" x2="890.0" y2="430.0" stroke="#182338" stroke-width="1.0"/>
<text x="890.0" y="448.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">0</tspan></text>
<line x1="95.0" y1="430.0" x2="890.0" y2="430.0" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="434.0" fill="#8fa3c0" font-size="12" text-anchor="end">%0</text>
<line x1="95.0" y1="371.9" x2="890.0" y2="371.9" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="375.9" fill="#8fa3c0" font-size="12" text-anchor="end">%5</text>
<line x1="95.0" y1="313.8" x2="890.0" y2="313.8" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="317.8" fill="#8fa3c0" font-size="12" text-anchor="end">%10</text>
<line x1="95.0" y1="255.6" x2="890.0" y2="255.6" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="259.6" fill="#8fa3c0" font-size="12" text-anchor="end">%15</text>
<line x1="95.0" y1="197.5" x2="890.0" y2="197.5" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="201.5" fill="#8fa3c0" font-size="12" text-anchor="end">%20</text>
<line x1="95.0" y1="139.4" x2="890.0" y2="139.4" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="143.4" fill="#8fa3c0" font-size="12" text-anchor="end">%25</text>
<line x1="95.0" y1="81.2" x2="890.0" y2="81.2" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="85.2" fill="#8fa3c0" font-size="12" text-anchor="end">%30</text>
<rect x="95" y="58" width="795" height="372" fill="none" stroke="#8fa3c0"/>
<text x="492.5" y="474.0" fill="#8fa3c0" font-size="14" text-anchor="middle">boyutsuz spin  a* = cJ/𝒢M²   (tekdüze M = 1,4 M☉ · R = 12 km · I = 0,4MR²)</text>
<text x="26" y="244" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 244)">sınıf içi pay</text>
<text x="95.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.D — 2.527 pulsar: besleme zarfı kuranlar 129 kat hızlı</text>
<path d="M 95.0 430.0 L 95.0 427.4 L 139.2 427.4 L 139.2 415.2 L 183.3 415.2 L 183.3 404.4 L 227.5 404.4 L 227.5 355.8 L 271.7 355.8 L 271.7 249.8 L 315.8 249.8 L 315.8 163.8 L 360.0 163.8 L 360.0 154.6 L 404.2 154.6 L 404.2 266.2 L 448.3 266.2 L 448.3 373.7 L 492.5 373.7 L 492.5 403.4 L 536.7 403.4 L 536.7 418.7 L 580.8 418.7 L 580.8 425.9 L 625.0 425.9 L 625.0 428.0 L 669.2 428.0 L 669.2 418.2 L 713.3 418.2 L 713.3 395.2 L 757.5 395.2 L 757.5 418.7 L 801.7 418.7 L 801.7 428.5 L 845.8 428.5 L 845.8 430.0 L 890.0 430.0 L 890.0 430.0 Z" fill="#b58cff" fill-opacity="0.22" stroke="#b58cff" stroke-width="1.8"/>
<line x1="362.5" y1="58.0" x2="362.5" y2="430.0" stroke="#b58cff" stroke-width="1.6" stroke-dasharray="6 5"/>
<text x="354.5" y="76.0" fill="#b58cff" font-size="12" text-anchor="end">yalıtık medyanı a* = 0.00103  (n = 2271)</text>
<path d="M 95.0 430.0 L 95.0 430.0 L 139.2 430.0 L 139.2 430.0 L 183.3 430.0 L 183.3 430.0 L 227.5 430.0 L 227.5 420.9 L 271.7 420.9 L 271.7 425.5 L 315.8 425.5 L 315.8 411.8 L 360.0 411.8 L 360.0 411.8 L 404.2 411.8 L 404.2 411.8 L 448.3 411.8 L 448.3 402.8 L 492.5 402.8 L 492.5 389.1 L 536.7 389.1 L 536.7 371.0 L 580.8 371.0 L 580.8 343.7 L 625.0 343.7 L 625.0 361.9 L 669.2 361.9 L 669.2 316.5 L 713.3 316.5 L 713.3 80.3 L 757.5 80.3 L 757.5 121.2 L 801.7 121.2 L 801.7 389.1 L 845.8 389.1 L 845.8 430.0 L 890.0 430.0 L 890.0 430.0 Z" fill="#ffb84d" fill-opacity="0.22" stroke="#ffb84d" stroke-width="1.8"/>
<line x1="735.3" y1="58.0" x2="735.3" y2="430.0" stroke="#ffb84d" stroke-width="1.6" stroke-dasharray="6 5"/>
<text x="743.3" y="76.0" fill="#ffb84d" font-size="12" text-anchor="start">çift sistemde medyanı a* = 0.133  (n = 256)</text>
<path d="M 362.5 90 L 735.3 90" stroke="#5ce6a8" stroke-width="1.4"/>
<path d="M 735.3 90 l -10 -4 l 0 8 z" fill="#5ce6a8"/>
<text x="548.0" y="84.0" fill="#5ce6a8" font-size="13" text-anchor="middle">129 kat</text>
<line x1="504.1" y1="430.0" x2="504.1" y2="418.0" stroke="#4dd2ff" stroke-width="2.0"/>
<text x="504.1" y="412.0" fill="#4dd2ff" font-size="10" text-anchor="middle">Vela</text>
<line x1="579.4" y1="430.0" x2="579.4" y2="418.0" stroke="#4dd2ff" stroke-width="2.0"/>
<text x="579.4" y="412.0" fill="#4dd2ff" font-size="10" text-anchor="middle">Crab</text>
<line x1="609.2" y1="430.0" x2="609.2" y2="418.0" stroke="#4dd2ff" stroke-width="2.0"/>
<text x="609.2" y="412.0" fill="#4dd2ff" font-size="10" text-anchor="middle">J0737A</text>
<line x1="760.6" y1="430.0" x2="760.6" y2="418.0" stroke="#4dd2ff" stroke-width="2.0"/>
<text x="760.6" y="412.0" fill="#4dd2ff" font-size="10" text-anchor="middle">J1614</text>
<line x1="822.1" y1="430.0" x2="822.1" y2="418.0" stroke="#4dd2ff" stroke-width="2.0"/>
<text x="822.1" y="412.0" fill="#4dd2ff" font-size="10" text-anchor="middle">J0952</text>
<line x1="823.1" y1="430.0" x2="823.1" y2="418.0" stroke="#4dd2ff" stroke-width="2.0"/>
<text x="823.1" y="412.0" fill="#4dd2ff" font-size="10" text-anchor="middle">J1748ad</text>
<text x="884.0" y="100.0" fill="#ff6b6b" font-size="12" text-anchor="end">a* = 1 ufuk tavanı →  2.527 pulsarın hiçbiri aşmıyor (en yüksek 0,418)</text>
<line x1="890.0" y1="58.0" x2="890.0" y2="430.0" stroke="#ff6b6b" stroke-width="2.5"/>
<text x="105.0" y="420.0" fill="#4dd2ff" font-size="11" text-anchor="start">mavi çentikler: kütlesi ölçülmüş pulsarlar</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.D: ATNF kataloğunun tamamı (2.527 pulsar), boyutsuz spine göre. Mor: yalıtık pulsarlar (n = 2.271, medyan a* = 0,00103). Turuncu: çift sistemdekiler (n = 256, medyan a* = 0,133). İki dağılım 129 kat ayrışır ve örtüşmesi azdır — besleme zarfı kurabilen nötron yıldızları momentumu geri yükler. Yalıtıkların sağ kuyruğu (a* > 0,1) çoğunlukla çifti dağılmış geri dönüştürülmüş pulsarlardır. Sağ kenardaki kırmızı çizgi ufuk tavanıdır: hiçbir pulsar aşmaz, en yüksek değer 0,418.</em></p>
</div>

Bu sınıf zarf çerçevesinin **üç ayrı sınavını** birden taşır:

**(i) Doğumda zorunlu boşaltma.** Çöken çekirdek gezegen-bandı katsayısını taşıyamaz: $\mathcal{A}_0$, kompakt tavanın 918 katıdır; yıldız-bandı katsayısı bile ($\sim10^{-18}$) tavanın ~10 katıdır. Çekirdek çökerken momentumun **>%99'unu bırakmak zorundadır** — teori bunu tavanın zorlamasıyla okur; gözlem tam bunu görür: genç pulsarlar $a^*\approx0{,}01$ ile doğar (Crab'ın geri-izlenen doğum dönemi ~19 ms), ve Kepler asterosismolojisi kırmızı dev **çekirdeklerinin** daha çökme başlamadan modellerin öngördüğünden 10–100 kat yavaş döndüğünü ölçmüştür (Mosser ve ark., 2012) — standart modellerin "kayıp fren" dediği kalem, tavana yaklaşan çekirdeğin erken salımıdır.

**(ii) Çıplak fren.** Zarfsız kalıntının tek kanalı manyetik dipol ışımasıdır: $\dot\omega\propto-\omega^n$, $n\approx3$ (Crab'da ölçülen $n=2{,}5$). $n=3$ integrali $\omega\propto t^{-1/2}$ verir — **açık kanallı yıldızların Skumanich üssüyle aynıdır.** İki bambaşka cisim sınıfında aynı $t^{-1/2}$: salım kanalı hangi fizikle açılırsa açılsın, momentumun ortama tek tip sızdığının işaretidir.

**(iii) Beslenme zarfı ve geri dönüş.** Yığışma diski kuran nötron yıldızları (düşük-kütleli X-ışını çiftleri) yeniden hızlanır ve milisaniye pulsarlarına dönüşür. Tablo bunun en sert biçimini gösterir: **en hızlı dönenler en ağır olanlardır** (J0952−0607: hem 707 Hz hem $2{,}35\,M_\odot$ — bilinen en ağır nötron yıldızı). Yığışan madde hem kütleyi hem dönüşü birlikte yükler; teori dilinde beslenme diski **geçici bir zarftır** ve zarf geri gelince kuplaj geri gelir. Sınıf içi kütle–spin korelasyonu böylece **pozitif** işaretle geri döner — zarf hipotezinin ters yönlü doğrulaması.

Bu madde artık popülasyon düzeyinde sınanmıştır. ATNF kataloğunun tamamı (2.527 pulsar) çift sistemde olma ölçütüne göre bölündüğünde, **çift sistemdekilerin medyan $a^*$'ı 0,1331, yalıtık olanların 0,00103 — arada 129 kat fark var** (Şekil 11.3.D). Ayrım tek yönlü, örtüşmesi az ve teorinin öngördüğü işarettedir: zarf kurabilen nötron yıldızı momentumu geri yükler, kuramayan yükleyemez. Bu, 8 nesneyle kurulan bir gözlemin 2.527 nesneyle ayakta kalmasıdır. Yalıtıkların içindeki hızlı kuyruk ($a^*>0{,}1$, ~%3) tabloyu bozmaz: bunlar çifti sonradan dağılmış geri dönüştürülmüş pulsarlardır, yani zarfı bir zamanlar var olmuş nesnelerdir.

Tavan burada da görünür: en hızlı pulsar (716 Hz) kırılma frekansının %43'ünde, yukarıdaki tablonun nesneye özgü kabullerine göre $a^*=0{,}37$'dedir.

> **İki hesap, iki sayı — ayrım kayda geçirilir.** Bu bölümün tablosu her nesnenin ölçülen kütlesi, ona karşılık gelen yarıçapı ve $I\simeq0{,}35MR^2$ ile yürür. Katalog geneli (Şekil 11.3.D ve 11.3.9c) ise 2.527 pulsarın hepsine **tekdüze** $M=1{,}4\,M_\odot$, $R=12$ km ve $I=0{,}4MR^2$ uygular; aynı 716 Hz'lik nesne orada $a^*=0{,}418$ çıkar. Fark tümüyle eylemsizlik çarpanıdır ($0{,}35$ ↔ $0{,}40$, oran $0{,}875$) ve **hiçbir sonucu etkilemez**, çünkü bütün $a^*$'lar aynı çarpanla ölçeklenir: çift/yalıtık 129 katı, $\eta_z$ merdiveni ve "hiçbiri tavanı aşmıyor" hükmü değişmez. Sınıfın en yüksek değeri olarak **0,418** okunmalıdır; 0,37 tablonun kendi kabullerine aittir.

Denge dönemi fiziği (yığışma torku ↔ manyetosfer) pulsarları tavana varmadan doyurur; tavanı dolduran tek sınıf bir sonrakidir.

---

## 11.3.6 Karadelikler: Zarf Yok — Tavanın Kendisi

Karadelik spini iki bağımsız teknikle ölçülür: X-ışını çiftlerinde iç disk yarıçapı (süreklilik uydurması / Fe Kα yansıması; Reynolds, 2021), birleşmelerde dalga biçimi (LIGO-Virgo). Boyutsuz spin $a^*=cJ/\mathcal{G}M^2$:

| Nesne | $M$ ($M_\odot$) | $a^*$ | Yöntem |
|---|---|---|---|
| A0620−00 | 6,6 | 0,12 | X-ışını sürekliliği |
| LMC X-3 | 7,0 | 0,25 | X-ışını sürekliliği |
| GRO J1655−40 | 6,3 | 0,70 | X-ışını sürekliliği |
| LMC X-1 | 10,9 | 0,92 | X-ışını sürekliliği |
| GRS 1915+105 | 12,4 | 0,98 | X-ışını sürekliliği |
| Cyg X-1 | 21,2 | >0,99 | iki yöntem uyumlu |
| GW150914 ürünü | 62 | 0,67 | GW halka-sönümü |
| GW190521 ürünü | 142 | 0,72 | GW halka-sönümü |
| NGC 1365 | $4{,}5\times10^6$ | 0,97 | Fe Kα |
| M87* | $6{,}5\times10^9$ | ~0,9 | EHT + jet gücü |

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 520" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Karadeliklerde boyutsuz spin: X-isini, AGN ve 273 GW birlesmesi">
<rect x="0" y="0" width="940" height="520" fill="#0b0f19"/>
<line x1="95.0" y1="58.0" x2="95.0" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="95.0" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">0</tspan></text>
<line x1="174.5" y1="58.0" x2="174.5" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="174.5" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">1</tspan></text>
<line x1="254.0" y1="58.0" x2="254.0" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="254.0" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">2</tspan></text>
<line x1="333.5" y1="58.0" x2="333.5" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="333.5" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">3</tspan></text>
<line x1="413.0" y1="58.0" x2="413.0" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="413.0" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">4</tspan></text>
<line x1="492.5" y1="58.0" x2="492.5" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="492.5" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">5</tspan></text>
<line x1="572.0" y1="58.0" x2="572.0" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="572.0" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">6</tspan></text>
<line x1="651.5" y1="58.0" x2="651.5" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="651.5" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">7</tspan></text>
<line x1="731.0" y1="58.0" x2="731.0" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="731.0" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">8</tspan></text>
<line x1="810.5" y1="58.0" x2="810.5" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="810.5" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">9</tspan></text>
<line x1="890.0" y1="58.0" x2="890.0" y2="440.0" stroke="#182338" stroke-width="1.0"/>
<text x="890.0" y="458.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">10</tspan></text>
<line x1="95.0" y1="399.1" x2="890.0" y2="399.1" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="403.1" fill="#8fa3c0" font-size="12" text-anchor="end">-0,2</text>
<line x1="95.0" y1="344.5" x2="890.0" y2="344.5" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="348.5" fill="#8fa3c0" font-size="12" text-anchor="end">0,0</text>
<line x1="95.0" y1="289.9" x2="890.0" y2="289.9" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="293.9" fill="#8fa3c0" font-size="12" text-anchor="end">0,2</text>
<line x1="95.0" y1="235.4" x2="890.0" y2="235.4" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="239.4" fill="#8fa3c0" font-size="12" text-anchor="end">0,4</text>
<line x1="95.0" y1="180.8" x2="890.0" y2="180.8" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="184.8" fill="#8fa3c0" font-size="12" text-anchor="end">0,6</text>
<line x1="95.0" y1="126.2" x2="890.0" y2="126.2" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="130.2" fill="#8fa3c0" font-size="12" text-anchor="end">0,8</text>
<line x1="95.0" y1="71.6" x2="890.0" y2="71.6" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="75.6" fill="#8fa3c0" font-size="12" text-anchor="end">1,0</text>
<rect x="95" y="58" width="795" height="382" fill="none" stroke="#8fa3c0"/>
<text x="492.5" y="482.0" fill="#8fa3c0" font-size="14" text-anchor="middle">kütle M [M☉]</text>
<text x="26" y="249" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 249)">a*  (GW olaylarında χ_eff)</text>
<text x="95.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.E — Tavan 290 kompakt nesnede aşılmıyor: 273 GW birleşmesi + 17 X-ışını/AGN</text>
<line x1="95.0" y1="71.6" x2="890.0" y2="71.6" stroke="#ff6b6b" stroke-width="2.2" stroke-dasharray="8 5"/>
<text x="884.0" y="63.6" fill="#ff6b6b" font-size="12" text-anchor="end">a* = 1  tavan</text>
<line x1="95.0" y1="72.2" x2="890.0" y2="72.2" stroke="#ffb84d" stroke-width="1.0" stroke-dasharray="2 5"/>
<line x1="95.0" y1="344.5" x2="890.0" y2="344.5" stroke="#8fa3c0" stroke-width="1.0" stroke-dasharray="3 4" opacity="0.6"/>
<text x="105.0" y="338.5" fill="#8fa3c0" font-size="11" text-anchor="start">χ_eff = 0</text>
<circle cx="217.4" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="205.9" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="186.6" cy="289.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="210.9" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="176.5" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="233.2" cy="265.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="216.9" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="213.5" cy="322.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="108.1" cy="344.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="217.6" cy="360.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.9" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="248.4" cy="159.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="205.9" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="209.7" cy="287.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="216.4" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="231.0" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="224.0" cy="371.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="120.6" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="255.8" cy="281.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="223.5" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="203.6" cy="339.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.7" cy="300.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="223.1" cy="366.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="221.7" cy="210.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="239.2" cy="254.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="253.4" cy="382.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="225.2" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.3" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="242.6" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="235.2" cy="251.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="217.9" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="232.8" cy="366.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="243.6" cy="268.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="181.1" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="198.1" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="219.3" cy="276.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="186.6" cy="292.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="180.2" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="221.4" cy="319.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="182.2" cy="309.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="223.9" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.3" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.3" cy="243.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="203.7" cy="344.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="214.6" cy="303.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="204.3" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="225.5" cy="344.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="215.3" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="225.5" cy="289.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="173.4" cy="366.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="170.1" cy="336.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="199.8" cy="319.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="223.3" cy="350.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="239.8" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="186.6" cy="292.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="180.2" cy="287.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="176.8" cy="350.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="239.1" cy="423.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="211.3" cy="344.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="181.1" cy="287.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="232.1" cy="295.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="176.8" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="209.2" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="179.9" cy="300.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="206.0" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="181.1" cy="314.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="213.7" cy="344.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="226.5" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="229.7" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.3" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="156.3" cy="385.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="224.2" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="217.3" cy="314.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="174.8" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.3" cy="363.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="230.8" cy="221.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.3" cy="377.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="204.9" cy="339.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="230.8" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.1" cy="366.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="249.2" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="221.4" cy="363.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="222.4" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="197.2" cy="377.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.4" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="210.4" cy="257.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="236.4" cy="300.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="217.0" cy="350.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="183.8" cy="309.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.6" cy="270.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="167.5" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="139.8" cy="371.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="238.6" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="193.6" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.2" cy="374.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="228.7" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.1" cy="382.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="208.9" cy="298.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="168.5" cy="339.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="215.2" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="230.8" cy="295.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="174.5" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="222.4" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="215.3" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="250.0" cy="270.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="191.4" cy="292.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.3" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="211.4" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="238.6" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="226.4" cy="322.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="214.7" cy="350.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="192.0" cy="393.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.3" cy="350.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="181.6" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="175.5" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="225.7" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="214.9" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="230.8" cy="322.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.1" cy="336.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="241.2" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="216.4" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="241.7" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="237.5" cy="287.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="232.1" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="225.7" cy="265.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="224.0" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="176.5" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="216.7" cy="350.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="236.4" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="209.2" cy="295.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="221.8" cy="336.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="244.5" cy="259.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="211.0" cy="339.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="217.8" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="201.2" cy="336.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="232.7" cy="235.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="217.3" cy="339.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="244.5" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="238.6" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="248.0" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="211.0" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="226.4" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="199.5" cy="295.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="179.6" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="180.8" cy="306.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="216.8" cy="336.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="251.9" cy="221.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="239.1" cy="306.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="236.9" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="181.4" cy="306.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="203.6" cy="366.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="197.4" cy="298.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="222.2" cy="254.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="234.0" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="179.6" cy="309.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="203.0" cy="322.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="198.4" cy="240.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="224.9" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="183.3" cy="322.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="264.9" cy="257.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="226.4" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="226.4" cy="336.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.3" cy="366.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.2" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.3" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.9" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.2" cy="388.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="180.5" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="178.1" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="172.0" cy="347.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="222.5" cy="366.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="232.1" cy="393.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="202.5" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="224.3" cy="319.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="235.8" cy="257.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="210.9" cy="363.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="166.4" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="221.3" cy="336.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="231.4" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="198.1" cy="336.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="221.1" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="213.6" cy="380.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="213.9" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="222.8" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="182.5" cy="306.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="205.3" cy="306.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.8" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="219.8" cy="216.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="239.1" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="213.7" cy="298.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="187.3" cy="284.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="231.4" cy="259.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="209.6" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="186.4" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="197.6" cy="306.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="215.7" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="231.4" cy="366.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="176.5" cy="319.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="233.4" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="216.8" cy="363.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="210.7" cy="268.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="223.7" cy="369.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="195.9" cy="276.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="178.1" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="210.8" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="217.2" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="228.0" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="222.6" cy="350.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="241.7" cy="322.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="184.1" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="180.5" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="205.3" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.6" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="222.2" cy="306.3" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="226.4" cy="369.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="177.5" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="177.5" cy="309.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="179.6" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="176.8" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.9" cy="350.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="205.7" cy="369.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="219.8" cy="355.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="179.3" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.3" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.2" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="170.9" cy="339.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="206.8" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="218.5" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.0" cy="371.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="205.6" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="219.3" cy="314.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="219.8" cy="319.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="182.8" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="215.9" cy="314.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="197.6" cy="208.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="223.2" cy="303.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="177.5" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="226.0" cy="369.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="224.4" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="163.6" cy="341.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="191.6" cy="429.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="206.5" cy="317.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="197.2" cy="208.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.9" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="178.7" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="241.7" cy="268.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="224.0" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="236.4" cy="319.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="238.5" cy="388.2" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="212.9" cy="298.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="212.3" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="178.1" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.9" cy="309.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="211.3" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="222.4" cy="363.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="181.9" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="233.8" cy="390.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="231.4" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="224.4" cy="382.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="240.7" cy="382.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="181.9" cy="322.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="212.4" cy="358.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="227.0" cy="314.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="232.7" cy="330.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.1" cy="374.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="221.5" cy="325.4" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="216.5" cy="352.7" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="217.0" cy="303.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="225.7" cy="333.6" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="175.5" cy="314.5" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="220.7" cy="311.8" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="216.5" cy="328.1" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="179.4" cy="319.9" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.55"/>
<circle cx="160.2" cy="311.8" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="168.2" y="315.8" fill="#ff6b6b" font-size="11" text-anchor="start">A0620</text>
<circle cx="162.2" cy="276.3" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="170.2" y="270.3" fill="#ff6b6b" font-size="11" text-anchor="start">LMC X-3</text>
<circle cx="158.5" cy="153.5" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="150.5" y="147.5" fill="#ff6b6b" font-size="11" text-anchor="end">GRO J1655</text>
<circle cx="177.5" cy="93.5" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="185.5" y="89.5" fill="#ff6b6b" font-size="11" text-anchor="start">LMC X-1</text>
<circle cx="181.9" cy="77.1" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="189.9" y="89.1" fill="#ff6b6b" font-size="11" text-anchor="start">GRS 1915</text>
<circle cx="200.4" cy="74.4" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="208.4" y="70.4" fill="#ff6b6b" font-size="11" text-anchor="start">Cyg X-1</text>
<rect x="618.9" y="74.8" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="633.9" y="75.8" fill="#ff6b6b" font-size="11" text-anchor="start">NGC 1365</text>
<rect x="617.4" y="93.9" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="612.4" y="112.9" fill="#ff6b6b" font-size="11" text-anchor="end">Sgr A*</text>
<rect x="699.2" y="93.9" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="714.2" y="94.9" fill="#ff6b6b" font-size="11" text-anchor="start">NGC 4151</text>
<rect x="759.0" y="197.6" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="774.0" y="206.6" fill="#ff6b6b" font-size="11" text-anchor="start">Fairall 9</text>
<rect x="870.1" y="93.9" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="865.1" y="94.9" fill="#ff6b6b" font-size="11" text-anchor="end">M87*</text>
<circle cx="112.0" cy="80.0" r="4.5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="125.0" y="84.0" fill="#ff6b6b" font-size="12" text-anchor="start">X-ışını çifti (●) · AGN (■) — a* ölçümü</text>
<circle cx="112.0" cy="100.0" r="3.2" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="0" opacity="0.7"/>
<text x="125.0" y="104.0" fill="#5ce6a8" font-size="12" text-anchor="start">GW birleşmesi (n = 273) — χ_eff, tek nesne spini değil</text>
<text x="125.0" y="124.0" fill="#8fa3c0" font-size="11" text-anchor="start">χ_eff medyanı +0,050 · saçılma 0,136 · |χ_eff| > 1 olan yok</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.E: Kompakt nesnelerde tavan sınavı. Kırmızı daireler X-ışını çiftlerinin, kareler AGN'lerin a* ölçümleridir; yarısı 0,9 üstüne, Thorne'un yığışma doyma noktasına (0,998, turuncu noktalı) yaslanır. Yeşil noktalar GWTC kataloğunun 273 birleşmesidir ve χ_eff eksenindedir — bu tek bir karadeliğin a*'ı değil, çiftin kütleyle ağırlıklı hizalı spin bileşenidir, dolayısıyla tavan sınavının zayıf biçimidir. Dağılım sıfır çevresinde toplanır (medyan +0,050, saçılma 0,136) ve 290 nesnenin hiçbiri tavanı aşmaz.</em></p>
</div>

Üç okuma:

1. **Tavan gerçektir ve doldurulur.** 17 nesnenin hiçbiri $a^*=1$'i aşmaz; X-ışını çiftlerinin yarısı 0,9'un üstüne, yığışma dengesinin kuramsal doyma noktasına (Thorne, 1974: $a^*=0{,}998$) yaslanır. $J=\mathcal{A}M^2$ biçimi burada saf hâliyle görünür: $\mathcal{A}\to\mathcal{G}_{yerel}/c_{yerel}$. Örneklem GWTC kataloğunun kütlesi ve $\chi_{eff}$'i olan 273 birleşmesiyle genişletildiğinde tablo değişmez: **290 kompakt nesnede tavan bir kez bile delinmez** (Şekil 11.3.E). $\chi_{eff}$ dağılımı sıfır çevresinde toplanır (medyan $+0{,}050$, saçılma 0,136, menzil $-0{,}31$…$+0{,}68$) — bunun bir tavan sınavı olarak zayıf biçim olduğu 11.3.9(d)'de kayıtlıdır, çünkü $\chi_{eff}$ tek bir karadeliğin $a^*$'ı değildir.
2. **GW birleşme ürünleri ~0,7'de kümelenir** — bu değer spinden değil, birleşen çiftin **yörünge** momentumunun yutulmasından gelir; birleşme öncesi bireysel spinler çoğunlukla düşüktür ($\chi_{eff}\approx0$–$0{,}3$). Yörünge–spin ayrımı burada da korunur.
3. **Teorinin okuması ve ayrıştırıcı öngörü.** Standart fizikte $a^*\le1$ Kerr geometrisinin mutlak sınırıdır. Evrenakı'da bu tavan, girdap çekirdeğinin **yerel** nicelikleriyle kurulur — $c_{yerel}=\sqrt{P/\rho_0}$ (Postülat 4) ve $\mathcal{G}_{yerel}$ (M-35) — yani **mutlak değil, ortama bağlıdır.** İki teori burada ilk kez ayrışır: tek bir kompakt nesnede $a^*>1$ güvenilir biçimde ölçülürse standart çerçeve çöker; Evrenakı bunu yerel ortam durumunun farklılaştığı bir bölge olarak okur. Bugünkü veri tavana saygılıdır; ayrım açık bir gözlemsel bahis olarak kayda geçirilir.

---

## 11.3.7 Yasanın Yapısı: İlkel Biçim, Değişmez Oran, Açık Mekanizma

Gözlem dört ana sınıfta aynı biçimi verdi (11.3.9'un popülasyon sınavları bunu yediye çıkarır). Bu alt bölüm ne iddia edip ne iddia etmediğini baştan söyler: **yasanın biçimi ve oranı yapısal olarak kurulur; üretici mekanizması türetilmemiştir.** Denenip elenen iki mekanizma da kayda geçirilir, çünkü ikisi de yeniden denenmeye açık yollardır.

### (a) Kaynak: tek 4B çift dönüş, iki izdüşüm

Kısım 1 §1.4'ün sonucu bağlayıcıdır: dört boyutta dönüş bir eksen etrafında değil **bir düzlem içinde** olur ve W içeren düzlemdeki bileşen 3B kesitimizde dönüş olarak *görünmez.* Nükleon tek bir 4B çift dönüş taşır; M-45'in H.0 köken haritası bunun iki izdüşümünü sayısal olarak çözmüştür:

| İzdüşüm | Nicelik | Değer | Ürettiği |
|---|---|---|---|
| $\omega_1$ — 3B-içi dönüş | dolaşım $\gamma_n=2\pi r_n v_t$ | $2{,}24\times10^{-6}$ m²/s | ortamın dolaşımı |
| $\omega_2$ — W-eksenli pulsasyon | debi $q_n=4\pi r_n^2u_r$ | $1{,}62\times10^{-19}$ m³/s | $\nabla P$ → **kütle-itim** |

İki kolun oranı serbest değildir; M-45 onu eş-güç ilkesinden kapatır: $u_r/v_t=\sqrt{m_p/m_e}$, eşdeğer olarak $\ell_\omega=q_n/2\gamma_n=r_n\sqrt{m_p/m_e}=36{,}05$ fm.

Bir iç tutarlılık kaydı: bu atamalarla iki kolun açısal momentumu **tam eşittir** ($m_pv_tr_n=m_eu_r\ell_\omega=5{,}97\times10^{-34}$), yani izoklinik okuma kendi içinde tutarlıdır. Ancak bu eşitlik M-45'in tanımlarından **cebirsel olarak zorunludur**; bağımsız bir doğrulama değil, yapının kendisiyle çelişmediğinin kaydıdır.

### (b) Üssün statüsü: gözlemsel `[G]`

Üs, ölçümden gelir: $L\propto M^{1{,}885\pm0{,}065}$, tam kare 1,8σ uzakta. Üssü üreten bir mekanizma **bulunamamıştır** ve iki aday açıkça elenmiştir:

**Elenen 1 — dolaşım toplanabilirliği.** M-35'in toplanabilirlik maddesi **skaler debi** için kuruludur ($Q=Nq_n$; debi bir kaynak yoğunluğudur, o yüzden toplanır). Dolaşım skaler kaynak değildir ve makro ölçekte toplanmaz: Dünya için $N\gamma_n=7{,}99\times10^{45}$ m²/s çıkar, oysa teorinin M-22'den gelen gerçek makro dolaşımı $4\pi\sqrt{\mathcal{G}MR}=6{,}34\times10^{11}$ m²/s'dir — **34 mertebe fark**, ve $N\gamma_n$ ile yüzey hızı $6{,}6\times10^{29}c$ gibi absürt bir değere çıkar. Doğru makro dolaşıma bağlanmak ise $L\propto M^{3/2}R^{1/2}$ verir, yani kırılma biçimini — gözlem bunu 5,2σ eler.

**Elenen 2 — nükleon spinlerinin izdüşümü.** Gövdenin spini nükleonların 4B momentumlarının eşli izdüşümü de olamaz: Dünya için toplam $N\ell_{3B}=2{,}13\times10^{18}$ kg m²/s, gözlenen $5{,}86\times10^{33}$ — **$2{,}8\times10^{15}$ kat eksik**, ve eksik çarpan $\propto M$ olduğundan sabit bir izdüşüm kesriyle kapatılamaz. Sonuç: makroskopik spin **biriktirilmiş** olmak zorundadır ve biriktirme süresinin kütle bağımlılığı türetilmemiştir.

Gözlemsel olarak ayakta kalan tek yapısal ifade $\omega\propto g$'dir (yani $\omega\propto M/R^2$; $L=\lambda MR^2\omega$'ya konduğunda $R^2$ sadeleşir ve $L\propto M^2$ çıkar). Rakiplerinden ikisi elenir, biri elenmez:

| Aday | Öngördüğü dizi üssü | Ölçülenden sapma |
|---|---|---|
| **$\omega\propto\mathcal{G}M/R^2$ (yani $\omega\propto g$)** | $M^{+0{,}182}$ | **0,9σ** ✓ |
| $\omega\propto\sqrt{M}/R$ | $M^{+0{,}091}$ | 1,0σ — *dizi boyunca ayrılamaz* |
| $\omega\propto\sqrt{\mathcal{G}M/R^3}$ (kırılma kesri) | $M^{-0{,}114}$ | **5,2σ** ✗ |
| $\omega\propto M/R^3$ (ortalama yoğunluk) | $M^{-0{,}227}$ | **4,2σ** ✗ |

### (c) İlkel biçim: $\mathcal{G}$ ve $c$ teoride sabit değildir

Katsayıyı $\mathcal{A}_0=\mathcal{G}m_p/2cm_e$ biçiminde yazmak yanıltıcıdır, çünkü sağ tarafın iki niceliği de yereldir. Teorinin ilkel niceliklerine açıldığında **$c$ tamamen sadeleşir**: $\mathcal{G}=Cq_n/4\pi\rho_nm_n$ ve $q_n=4\pi r_n^2u_r$, $u_r=\sqrt2\,c_{yerel}\sqrt{m_p/m_e}$ olduğundan $\mathcal{G}\propto c_{yerel}/\rho_0$'dır; $\mathcal{G}/c$ ise $c$ içermez. Sonuç:

$$\boxed{\;\mathcal{A}_0=\frac{1}{4\sqrt2}\cdot\frac{C\,\ell_\omega^{3}}{m_n\,\rho_0\,r_n}\;}$$

Sağ tarafta ne $\mathcal{G}$ ne $c$ vardır — yalnız $C$ (teorinin kendi kuplajı), $\ell_\omega$ (M-45), $r_n$, $m_n$ ve yerel ortam yoğunluğu $\rho_0$. Sayısal: $2{,}05\times10^{-16}$, gözlem $1{,}998\times10^{-16}$ (%2,4). Yani **yasa yerel dalga hızından bağımsızdır**, yerel ortam yoğunluğundan değil.

### (d) Değişmez: yükleme/tavan oranı $=m_p/2m_e$

Hem yükleme katsayısı hem tavan aynı $1/\rho_0$ ile ölçeklenir; dolayısıyla oranlarında hiçbir yerel nicelik kalmaz:

$$\mathcal{A}_0\propto\frac{1}{\rho_0}\ ,\qquad \frac{\mathcal{G}_{yerel}}{c_{yerel}}\propto\frac{1}{\rho_0}\qquad\Longrightarrow\qquad \boxed{\;\frac{\mathcal{A}_0}{\mathcal{G}_{yerel}/c_{yerel}}=\frac{m_p}{2m_e}=918{,}1\;}$$

Gözlenen oran **898**. Bölümün asıl sonucu budur: bir katsayı değeri değil, **saf kütle oranına eşit bir orandır** — ve tam da $\mathcal{G}$ ile $c$ sabit olmadığı için anlamlıdır, çünkü ikisi birlikte kayarken oran yerinde kalır.

Bu eşleşmenin rastgele bir sayı avı olmadığının kanıtı, aday uzayının ayrık ve dar olmasıdır. $\mathcal{A}_0=\kappa(\mathcal{G}/c)(m_p/m_e)^n$ yazılınca:

| $n$ | Gerekli $\kappa$ |
|---|---|
| $0$ | $1{,}1\times10^{-3}$ |
| $1/2$ | $0{,}048$ |
| $\mathbf{1}$ | $\mathbf{0{,}489}$ |
| $3/2$ | $87{,}6$ |
| $2$ | $3{,}8\times10^{3}$ |

Kütle oranının yalnız **birinci** kuvveti $O(1)$ katsayı verir; komşuları 20 ve 44 kat uzaktadır. Üs bu yüzden tekil olarak seçilir.

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 430" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Katsayinin kapanis sinavi: kappa degerleri">
<rect x="0" y="0" width="940" height="430" fill="#0b0f19"/>
<line x1="120" y1="340.0" x2="890" y2="340.0" stroke="#182338"/>
<text x="112.0" y="344.0" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,00</text>
<line x1="120" y1="288.1" x2="890" y2="288.1" stroke="#182338"/>
<text x="112.0" y="292.1" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,25</text>
<line x1="120" y1="236.3" x2="890" y2="236.3" stroke="#182338"/>
<text x="112.0" y="240.3" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,50</text>
<line x1="120" y1="184.4" x2="890" y2="184.4" stroke="#182338"/>
<text x="112.0" y="188.4" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,75</text>
<line x1="120" y1="132.6" x2="890" y2="132.6" stroke="#182338"/>
<text x="112.0" y="136.6" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">1,00</text>
<line x1="120" y1="80.7" x2="890" y2="80.7" stroke="#182338"/>
<text x="112.0" y="84.7" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">1,25</text>
<rect x="120" y="60" width="770" height="280" fill="none" stroke="#8fa3c0"/>
<text x="40" y="200.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 40 200.0)">κ = 𝒜₀ c m_e / 𝒢 m_p</text>
<text x="120.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.F — Oranın sınavı: κ = ½ (yükleme/tavan = m_p/2m_e) ile beş gezegen</text>
<line x1="120" y1="236.3" x2="890" y2="236.3" stroke="#5ce6a8" stroke-width="2.0" stroke-dasharray="8 5"/>
<text x="884.0" y="228.3" fill="#5ce6a8" font-size="12" text-anchor="end" font-weight="normal">κ = ½   ⇔   yükleme/tavan = m_p/2m_e   (öngörü)</text>
<line x1="120" y1="132.6" x2="890" y2="132.6" stroke="#ff6b6b" stroke-width="1.1" stroke-dasharray="2 6"/>
<text x="884.0" y="124.6" fill="#ff6b6b" font-size="12" text-anchor="end" font-weight="normal">κ = 1   (3,0σ dışlanır)</text>
<line x1="120" y1="288.1" x2="890" y2="288.1" stroke="#ff6b6b" stroke-width="1.1" stroke-dasharray="2 6"/>
<text x="884.0" y="280.1" fill="#ff6b6b" font-size="12" text-anchor="end" font-weight="normal">κ = ¼   (2,8σ dışlanır)</text>
<rect x="120" y="211.2" width="770" height="48.9" fill="#ffb84d" opacity="0.13"/>
<line x1="120" y1="238.6" x2="890" y2="238.6" stroke="#ffb84d" stroke-width="1.6"/>
<text x="130.0" y="229.6" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">geometrik ortalama 0,489  ± 1σ bandı</text>
<circle cx="248.3" cy="104.4" r="6" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="248.3" y="360.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">Mars</text>
<text x="259.3" y="108.4" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">1,136</text>
<circle cx="376.7" cy="256.6" r="6" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="376.7" y="360.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">Dünya</text>
<text x="387.7" y="260.6" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">0,402</text>
<circle cx="505.0" cy="264.3" r="6" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="505.0" y="360.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">Neptün</text>
<text x="516.0" y="268.3" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">0,365</text>
<circle cx="633.3" cy="222.2" r="6" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="633.3" y="360.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">Satürn</text>
<text x="644.3" y="226.2" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">0,568</text>
<circle cx="761.7" cy="279.0" r="6" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="761.7" y="360.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">Jüpiter</text>
<text x="772.7" y="283.0" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">0,294</text>
<text x="120.0" y="395.0" fill="#8fa3c0" font-size="12" text-anchor="start" font-weight="normal">κ = 𝒜₀ c m_e / 𝒢 m_p — beş girdi de ölçülmüştür, yani κ çapa seçiminden bağımsızdır. Türetilmemiştir.</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.F: Oranın sınavı. κ = ½ (yani yükleme/tavan = m_p/2m_e) beş gezegenin 1σ bandının içindedir; κ = 1 ve κ = ¼ ~3σ dışlanır. κ türetilmemiştir ve girdilerinin tümü ölçülmüş olduğu için M-45'in √2 çapa belirsizliğine de indirgenemez.</em></p>
</div>

$\kappa=0{,}489$'un neden $\tfrac12$ olduğu **türetilmemiştir** ve bir uyarı zorunludur: $\kappa=\mathcal{A}_0c\,m_e/\mathcal{G}m_p$ ifadesinin beş girdisi de ölçülmüş niceliklerdir, dolayısıyla $\kappa$ **M-45'in çözülmemiş $\sqrt2$ çapa seçiminden bağımsızdır** — çapa yalnız (c)'deki ilkel yazımın ön çarpanını oynatır ($1/4\sqrt2$ ↔ $1/8$), çünkü $C$ ile $q_n$ ters yönde değişip $\mathcal{G}$'yi sabit bırakır. Bu nedenle "$1/8$ daha temiz görünüyor" bir fizik argümanı değil, muhasebe artığıdır.

### (e) Yerel yoğunluk bağı: yeni bir yanlışlanabilir öngörü

$\mathcal{A}_0\propto1/\rho_0$ olması, sabit-$G$ çerçevesinde söylenemeyecek bir öngörü doğurur. Evrenakı'nın galaktik kenarlarda ve boşluklarda gerçekten seyreldiği teoride kayıtlıdır (Kısım 2 §2.4.4); seyrelmiş ortamda aynı kütleli bir gövde **daha çok spin yükler** ve orada **ölçülen $G$ de aynı çarpanla büyür.** Sınav bu yüzden tek nicelikte değil, iki niceliğin bağındadır:

$$\frac{\delta\mathcal{A}_0}{\mathcal{A}_0}=\frac{\delta\mathcal{G}_{yerel}}{\mathcal{G}_{yerel}}=-\frac{\delta\rho_0}{\rho_0}$$

**Spin fazlası ile yerel $G$ fazlası aynı işaretli ve aynı büyüklükte olmak zorundadır.** Ters işaret ya da bağımsız değişim, ilkel biçimi çürütür.

### (f) Dürüst kayıt: ne var, ne yok

| Kalem | Statü |
|---|---|
| $J\propto M^{2}$ biçimi | **gözlemsel** `[G]` — $1{,}885\pm0{,}065$; $M^2$ 1,8σ |
| İlkel biçim $\mathcal{A}_0=C\ell_\omega^3/4\sqrt2\,m_n\rho_0r_n$ | **yapısal** — $\mathcal{G}$ ve $c$ içermez; $c$ sadeleşir |
| Oran $\mathcal{A}_0/(\mathcal{G}/c)=m_p/2m_e$ | **yapısal sonuç** — yerel niceliklerden bağımsız; 918 ↔ 898 |
| Kütle oranı üssünün $n=1$ olması | **tekil seçilir** — komşular 20/44 kat uzak |
| $\rho_0$–$G$–spin bağı | **öngörü** `[F]` — sınanmadı |
| $\kappa=\tfrac12$ sayısı | **açık** — türetilmedi; çapa belirsizliğine sığınamaz |
| Üretici mekanizma | **açık** — iki aday elendi (b); en umutlu hat, 4B açısal momentum bivektörünün W bileşenlerinin 3B'ye sızması (Kısım 1 §1.4 aygıtı) |
| $\omega\propto M/R^2$ ↔ $\omega\propto\sqrt M/R$ | **dejenere** — gezegen dizisi ayıramaz; sabit yarıçaplı gövde gerekir (11.3.8, öngörü 2) |

Dürüst özet: elimizde **mekanizmasız bir yapısal örüntü** var. Örüntü güçlüdür (üs tekil seçilir, oran saf kütle oranıdır, iki yerel nicelik sadeleşir) ama üretici zincir kurulmamıştır ve bölüm bunu bir türetim gibi sunmaz.

---

## 11.3.8 Zarf-Bağımlı Denklem: Üç Tavan, Dört Rejim

Yükleme yasası bir *hedef*tir; gövdenin onu taşıyıp taşıyamayacağını zarf durumu belirler. Bütün sınıflar tek yapıda toplanır:

$$\boxed{\;L(M,t)\;=\;\min\Bigl[\;\underbrace{(1-g)\,\mathcal{A}_0M^{2}\,\eta_z(t)}_{\text{yükleme}}\;,\;\underbrace{\epsilon_k\,\lambda M\sqrt{\mathcal{G}MR}}_{\text{kırılma tavanı}}\;,\;\underbrace{\frac{\mathcal{G}M^{2}}{c_{yerel}}}_{\text{ufuk tavanı}}\;\Bigr]\;}$$

$g$ dış girdap kavraması (M-24), $\eta_z(t)$ zarf ifade çarpanı, $\epsilon_k$ kırılmaya yakınlık kesridir. Üç terimdeki $\mathcal{G}$ de yereldir (11.3.1 uyarısı).

> **Tanım alanı: denklemin ölçülmüş bir kütle tabanı vardır.** $\min[\cdot]$ yapısı bir *tavan* verir, dolayısıyla ancak gövdenin spinini kendi yüklemesi belirliyorsa geçerlidir. 19.929 asteroitte bu koşul sağlanmaz: gözlenen $J$, yükleme terimini $10^{3}$–$10^{6}$ kat **aşar** (11.3.9, Sınav 6a). Küçük gövdelerin spini yüklemeden değil dış torklardan (çarpışma geçmişi, ışınım torkları) gelir. Ölçülen sınır, dış tork izinin ($\mathcal{A}\propto M^{-1/3}$) yükleme çizgisini kestiği kütledir:
> $$M_{\text{taban}}=3{,}6\times10^{25}\ \text{kg}\ \approx\ 6\,M_\oplus$$
> Denklem yalnız $M\ge M_{\text{taban}}$ için iddia edilir. Bu tabanın altında teori spin için ayrı bir hesap vermez ve vermediğini söyler.

> **İki tavan aslında tek tavandır.** Kırılma tavanı olay ufkunda değerlendirilirse ($R=2\mathcal{G}M/c^2$) $\sqrt2\lambda\,\mathcal{G}M^2/c$ verir; $\lambda=0{,}4$ ile $0{,}57\,\mathcal{G}M^2/c$ — ufuk tavanıyla aynı biçim, katsayı 1,8 kat içinde. Yani "gövde kendi bağını aşan momentumu tutamaz" ilkesi, zarflı gövdede kırılma, çökmüş gövdede ufuk olarak görünür. Katsayının tam eşitlenmesi açık kalemdir.

| Rejim | Zarf durumu | $\eta_z(t)$ | Sonuç | Sınav |
|---|---|---|---|---|
| **R1** | rijit zarf, kanal kapalı | $\approx1$, sabit | $L=\mathcal{A}_0M^2$ | gezegen doğrusu (Şekil 11.3.B) |
| **R1′** | rijit zarf ama kırılma tavanına dayanmış | — | $L=\epsilon_k\lambda M\sqrt{\mathcal{G}MR}$ | yıldızaltı cisimler (Şekil 11.3.A üçgenler) |
| **R2** | plazma zarf, açık kanal | $\eta_i(1+t/\tau_z)^{-1/2}$; $\eta_i\sim10^{-2}$ | Skumanich; Kraft kırılması = kanal anahtarı | T Tauri→Güneş oranı 72 ↔ 68 |
| **R3** | zarf fırlatılmış | ufuk tavanına kırpılır; sonra dipol $t^{-1/2}$; beslenme zarfı kurulursa $\dot L=+\dot m\sqrt{\mathcal{G}MR_{iç}}$ | doğum $a^*\sim0{,}01$; çift/yalıtık pulsarda **129 kat** $a^*$ farkı (2.527 nesne); beyaz cüceler de aynı basamakta | Şekil 11.3.D, 11.3.H |
| **R4** | zarf yok, ufuk var | $=1$ **tavanda** | $a^*\to1$ doyması | Şekil 11.3.E |

Bu tablo $\eta_z$'yi **biçim** olarak verir. Her rejimin ölçülmüş **sayısal** karşılığı — $n$, $\eta_z$ ve saçılmasıyla — 11.3.9'un sonundaki *"Rejim sayıları — kategorik liste"* çizelgesindedir; o liste bu bölümün tek referans tablosudur ve altı sınavın hepsinden beslenir.

### R1′ — kırılma tavanının devreye girmesi

Yükleme doğrusu kırılma tavanını **3,8 $M_J$** ($R=R_J$) ile **6,8 $M_J$** ($R=1{,}8R_J$) arasında keser. Üstünde yasa fiziksel olarak sürdürülemez: 12 $M_J$'de 187 km/s isterken kırılma 125 km/s'dedir. Gözlem bu geçişi doğrular — yıldızaltı cisimler kırılmanın küçük bir kesrinde döner:

| Gövde | $M$ | $v_{ekv}/v_{kırılma}$ |
|---|---|---|
| Dünya | $0{,}003\,M_J$ | 0,06 |
| Jüpiter | $1\,M_J$ | 0,30 |
| Satürn | $0{,}3\,M_J$ | 0,40 |
| β Pic b | $12\,M_J$ | 0,20 |
| Luhman 16B | $28\,M_J$ | 0,11 |
| 2M1047+21 | $40\,M_J$ | 0,23 |
| 2M1219+31 | $55\,M_J$ | 0,24 |

**Dürüst kayıt.** Tavan, yıldızaltı cisimlerin yükleme doğrusunda *olamayacağını* açıklar; ama neden 1,0 değil 0,1–0,25'te durduklarını açıklamaz. Fark ikinci bir kayıp kanalını gerektirir ve adayı bellidir: kahverengi cüceler baştan sona konvektiftir ve manyetizedir, yani R1 değil **R2'ye geçiş** rejimindedir — büzülme geçmişi boyunca kanal kısmen açıktır. $\epsilon_k$'nın gövdeden gövdeye değeri ve kanal payının ayrıştırılması bu bölümün **açık kalemidir** `[F]`.

### Yanlışlanabilir öngörüler

1. **Oran sınavı.** Kütle menzili genişletildikçe (R1 rejiminde kalan genç dev ötegezegenler, izole kahverengi cüceler) $\mathcal{A}_0/(\mathcal{G}/c)$ oranı $m_p/2m_e=918$'e yakınsamalıdır. $m_p/m_e$ ya da $m_p/4m_e$'ye kayması, oran sonucunu çürütür.
2. **Dejenerasyonu kıran sınav: aynı kütle, farklı yarıçap.** Yapısal biçim $L$'nin yarıçaptan **bağımsız** olduğunu söyler; o hâlde şişmiş sıcak Jüpiter ($R\approx1{,}8R_J$) ile soğuk Jüpiter ($R\approx1{,}0R_J$) aynı $L$'yi taşımalı, yani şişmiş olan $\omega\propto1/R^2$ ile **3,2 kat yavaş** dönmelidir. Rakip $\omega\propto\sqrt M/R$ yalnız 1,8 kat öngörür. Ayrım bugünkü veriyle sınanabilir.
3. **$\rho_0$ bağı** (11.3.7e): spin fazlası ile yerel $G$ fazlası aynı işaretli ve aynı büyüklükte olmalıdır.
4. **Yıldızaltı cisimler kırılmanın altında kalmalıdır** — istisnasız. Tavanı aşan tek bir kahverengi cüce, denklemin ikinci terimini çürütür.
5. **Tek bir kompakt nesnede $a^*>1$:** standart çerçeve için ölümcül, Evrenakı için yerel ortam durumunun işareti — iki teoriyi ayıran en keskin bahis.
6. **MSP popülasyonunda kütle–frekans pozitif eğilimi** güçlenerek sürmelidir: kütlesi ölçülecek her yeni >500 Hz pulsarın $>1{,}8\,M_\odot$ çıkması beklenir.
7. **Eksen eğikliği–katsayı korelasyonu:** hizasız gövdelerin yükleme verimi düşükse, ötegezegen popülasyonunda eğiklik ile $\mathcal{A}$ arasında negatif korelasyon beklenir (Kısım 3 §3.4.4).
8. **Yaş-homojen örneklemde rampa kaybolmalıdır.** Sınav 5-ii'nin ölçtüğü $\eta_z\propto M^{3{,}44}$ rampası, kanalın yaşla sızdırmasının popülasyon izidir; kütle yasasının kendisi değildir. O hâlde **tek bir açık kümede** (yaş sabit) aynı ölçüm yapıldığında rampa düzleşmeli ve radyatif plato Kraft eşiğine kadar uzanmalıdır: kanal-kapalı yıldızlar $\eta_z\approx1{,}4\times10^{-2}$'de toplanır, kanal-açık olanlar kümenin yaşına karşılık gelen tek bir değerde toplanır — yani iki plato, aradaki yamaç olmadan. Sınav bugünkü veriyle yapılabilir (Pleiades ~120 Myr, Praesepe ~700 Myr, NGC 6811 ~1 Gyr, M67 ~4 Gyr dönme dönemi katalogları). Rampanın yaş-homojen örneklemde de sürmesi, bu okumayı çürütür.

---

## 11.3.9 Denklemin Sınavı: Asteroitten Karadeliğe

11.3.8'in denklemi bir hedef ve üç tavan verdi; şimdi gövde gövde hesaplanır. Sınav tek bir bağıntı üzerinden yürür — yükleme terimi $L=\mathcal{A}_0M^2$, $L=\lambda MR^2\omega$ ile birleştirilince **dönem öngörüsüne** döner:

$$\boxed{\;P_{\ddot{o}ng}=\frac{2\pi\,\lambda\,R^{2}}{\mathcal{A}_0\,M}\;}\qquad \mathcal{A}_0=2{,}044\times10^{-16}$$

*(Burada kullanılan $\mathcal{A}_0$, 11.3.7(c)'nin **ilkel niceliklerden hesaplanan** değeridir — gezegen fitinin verdiği $1{,}998\times10^{-16}$ değil. Aradaki %2,3, aşağıdaki $\eta_z$'lerin 1,00 yerine 0,98'de toplanmasının nedenidir.)*

Girdiler yalnız $M$, $R$ ve $\lambda$'dır; gövdeye özel hiçbir ayar yoktur. Ölçülenle oranı doğrudan zarf ifade çarpanını verir: $\eta_z=P_{\ddot{o}ng}/P_{g\ddot{o}z}=L_{g\ddot{o}z}/\mathcal{A}_0M^2$.

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 600" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Ongorulen ve gozlenen donme donemlerinin karsilastirmasi">
<rect x="0" y="0" width="940" height="600" fill="#0b0f19"/>
<line x1="139.4" y1="58" x2="139.4" y2="500" stroke="#182338"/>
<text x="139.4" y="518.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">0,1</text>
<line x1="95" y1="475.0" x2="880" y2="475.0" stroke="#182338"/>
<text x="87.0" y="479.0" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">0,1</text>
<line x1="287.5" y1="58" x2="287.5" y2="500" stroke="#182338"/>
<text x="287.5" y="518.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">1</text>
<line x1="95" y1="391.6" x2="880" y2="391.6" stroke="#182338"/>
<text x="87.0" y="395.6" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">1</text>
<line x1="435.7" y1="58" x2="435.7" y2="500" stroke="#182338"/>
<text x="435.7" y="518.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10</text>
<line x1="95" y1="308.2" x2="880" y2="308.2" stroke="#182338"/>
<text x="87.0" y="312.2" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">10</text>
<line x1="583.8" y1="58" x2="583.8" y2="500" stroke="#182338"/>
<text x="583.8" y="518.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">100</text>
<line x1="95" y1="224.8" x2="880" y2="224.8" stroke="#182338"/>
<text x="87.0" y="228.8" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">100</text>
<line x1="731.9" y1="58" x2="731.9" y2="500" stroke="#182338"/>
<text x="731.9" y="518.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">1000</text>
<line x1="95" y1="141.4" x2="880" y2="141.4" stroke="#182338"/>
<text x="87.0" y="145.4" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">1000</text>
<line x1="880.0" y1="58" x2="880.0" y2="500" stroke="#182338"/>
<text x="880.0" y="518.0" fill="#8fa3c0" font-size="12" text-anchor="middle" font-weight="normal">10000</text>
<line x1="95" y1="58.0" x2="880" y2="58.0" stroke="#182338"/>
<text x="87.0" y="62.0" fill="#8fa3c0" font-size="12" text-anchor="end" font-weight="normal">10000</text>
<rect x="95" y="58" width="785" height="442" fill="none" stroke="#8fa3c0"/>
<text x="487.5" y="540.0" fill="#8fa3c0" font-size="14" text-anchor="middle" font-weight="normal">gözlenen dönme dönemi P [saat]</text>
<text x="30" y="279.0" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 30 279.0)">öngörülen dönem P = 2πλR²/(𝒜₀M) [saat]</text>
<text x="95.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.G — Yasanın doğrudan sınavı: gezegenler köşegende, yıldızlar 65 kat altında</text>
<path d="M 95.0 474.9 L 880.0 32.9 L 880.0 83.1 L 95.0 525.1 Z" fill="#ffb84d" opacity="0.10"/>
<line x1="95.0" y1="500.0" x2="880.0" y2="58.0" stroke="#ffb84d" stroke-width="1.8" stroke-dasharray="8 5"/>
<text x="650.4" y="145.6" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">1:1   (η_z = 1)</text>
<text x="650.4" y="173.1" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">gölge: ±2 kat</text>
<line x1="363.1" y1="500.0" x2="880.0" y2="208.9" stroke="#4dd2ff" stroke-width="1.1" stroke-dasharray="2 6"/>
<line x1="628.2" y1="500.0" x2="880.0" y2="358.2" stroke="#4dd2ff" stroke-width="1.1" stroke-dasharray="2 6"/>
<text x="628.2" y="364.9" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">η_z = 1/65   radyatif yıldız platosu</text>
<text x="731.9" y="450.0" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">η_z = 1/4000   Güneş</text>
<circle cx="493.6" cy="245.8" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="502.6" y="239.8" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Mars</text>
<circle cx="491.8" cy="284.5" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="478.8" y="276.5" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Dünya</text>
<circle cx="466.3" cy="302.3" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="450.3" y="316.3" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Neptün</text>
<circle cx="439.2" cy="301.6" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="448.2" y="315.6" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Satürn</text>
<circle cx="435.2" cy="327.7" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="444.2" y="340.7" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Jüpiter</text>
<circle cx="470.7" cy="294.0" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="452.7" y="286.0" fill="#ffb84d" font-size="11" text-anchor="start" font-weight="normal">Uranüs</text>
<circle cx="753.9" cy="247.6" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="739.9" y="239.6" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Merkür</text>
<circle cx="845.3" cy="280.2" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="832.3" y="295.2" fill="#ff6b6b" font-size="11" text-anchor="start" font-weight="normal">Venüs</text>
<path d="M 422.1 398.0 L 428.1 409.0 L 416.1 409.0 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="431.1" y="398.0" fill="#5ce6a8" font-size="11" text-anchor="start" font-weight="normal">β Pic b</text>
<path d="M 394.6 451.1 L 400.6 462.1 L 388.6 462.1 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="403.6" y="461.1" fill="#5ce6a8" font-size="11" text-anchor="start" font-weight="normal">Luhman 16B</text>
<path d="M 323.2 471.6 L 329.2 482.6 L 317.2 482.6 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="243.2" y="480.6" fill="#5ce6a8" font-size="11" text-anchor="start" font-weight="normal">2M1047+21</text>
<path d="M 309.2 483.1 L 315.2 494.1 L 303.2 494.1 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="318.2" y="501.1" fill="#5ce6a8" font-size="11" text-anchor="start" font-weight="normal">2M1219+31</text>
<circle cx="551.1" cy="427.2" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="560.1" y="431.2" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">O5</text>
<circle cx="517.7" cy="421.5" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="526.7" y="415.5" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">B0</text>
<circle cx="469.4" cy="432.7" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="460.4" y="424.7" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">B5</text>
<circle cx="451.0" cy="442.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="419.0" y="456.1" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">A0</text>
<circle cx="444.1" cy="449.5" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="404.1" y="442.5" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">A5</text>
<circle cx="454.5" cy="459.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="463.5" y="472.6" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">F0</text>
<circle cx="526.9" cy="447.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="535.9" y="441.1" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">F5</text>
<circle cx="598.8" cy="458.9" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="607.8" y="462.9" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">G0</text>
<circle cx="699.8" cy="461.3" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="681.8" y="453.3" fill="#4dd2ff" font-size="11" text-anchor="start" font-weight="normal">Güneş</text>
<circle cx="112.0" cy="76.0" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="125.0" y="80.0" fill="#ffb84d" font-size="12" text-anchor="start" font-weight="normal">gezegenler (serbest, hizalı)</text>
<circle cx="112.0" cy="95.0" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="125.0" y="99.0" fill="#ff6b6b" font-size="12" text-anchor="start" font-weight="normal">bastırılmış (Merkür, Venüs)</text>
<path d="M 112.0 108.0 L 118.0 119.0 L 106.0 119.0 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="125.0" y="118.0" fill="#5ce6a8" font-size="12" text-anchor="start" font-weight="normal">kahverengi cüce / genç dev</text>
<circle cx="112.0" cy="133.0" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="125.0" y="137.0" fill="#4dd2ff" font-size="12" text-anchor="start" font-weight="normal">yıldızlar</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.G: Yasanın doğrudan sınavı. Öngörülen dönem yalnız M, R ve λ'dan hesaplanır. Serbest gezegenler 1:1 köşegeninin ±2 kat bandındadır; yıldızlar sistematik olarak ~65 kat, Güneş ~4000 kat altındadır — bu sapmalar hata değil, zarf ifade çarpanı η_z'nin ölçümüdür.</em></p>
</div>

### Sınav 1 — Gezegenler

| Gövde | $\lambda$ | $P_{\ddot{o}ng}$ (sa) | $P_{g\ddot{o}z}$ (sa) | $\eta_z$ |
|---|---|---|---|---|
| Mars | 0,364 | 55,93 | 24,62 | 2,27 |
| Satürn | 0,220 | 12,01 | 10,56 | 1,14 |
| Uranüs | 0,230 | 14,78 | 17,24 | 0,86 |
| Dünya | 0,331 | 19,24 | 23,93 | 0,80 |
| Neptün | 0,230 | 11,76 | 16,11 | 0,73 |
| Jüpiter | 0,254 | 5,84 | 9,93 | 0,59 |
| **Merkür** | 0,346 | 53,27 | 1.407,6 | **0,038** |
| **Venüs** | 0,337 | 21,65 | 5.832,5 | **0,0038** |

Serbest beşlide $\eta_z$'nin geometrik ortalaması **0,98**, bandı 0,59–2,27. Yani rijit zarflı gezegenler yükleme yasasının **tamamını** taşır.

**Bu satır dairesel; ama alt iki satır değil.** $\mathcal{A}_0$'ın katsayısı gezegenlerden okunduğu için $\eta_z\approx1$ çıkması zaten kaçınılmazdır. Buna karşılık Merkür ve Venüs'ün değerleri bağımsız bir sınavdır: $\eta_z=1-g$ olmalıdır ve $g$, Kısım 3 §3.4.4'te bambaşka bir yoldan (leave-one-out $v_{ekv}$ fiti) ölçülmüştür:

| Gövde | Bu bölüm: $1-\eta_z$ | Kısım 3 §3.4.4: $g$ |
|---|---|---|
| Merkür | 0,962 | 0,982 |
| Venüs | 0,996 | 1,003 |

İki bağımsız yol aynı kavrama derecesini %2 içinde verir. Bu, dönem öngörüsünün gezegen kalibrasyonundan bağımsız ilk doğrulamasıdır.

### Sınav 2 — Yıldızlar

Aynı bağıntı, yıldız eylemsizlik çarpanıyla ($k^2$). Gözlenen dönem $\langle v\sin i\rangle$'den $v_{ekv}=(4/\pi)\langle v\sin i\rangle$ izdüşüm düzeltmesiyle çıkarılır; Güneş için ölçülen $v_{ekv}=2{,}0$ km/s doğrudan kullanılır.

| Tayf | $M/M_\odot$ | $k^2$ | $P_{\ddot{o}ng}$ (sa) | $P_{g\ddot{o}z}$ (sa) | $\eta_z$ |
|---|---|---|---|---|---|
| O5 | 40 | 0,05 | 0,37 | 60,2 | $6{,}2\times10^{-3}$ |
| B0 | 16 | 0,06 | 0,44 | 35,8 | $1{,}23\times10^{-2}$ |
| B5 | 5,9 | 0,06 | 0,32 | 16,9 | $1{,}90\times10^{-2}$ |
| A0 | 2,9 | 0,06 | 0,25 | 12,7 | $1{,}95\times10^{-2}$ |
| A5 | 2,0 | 0,06 | 0,20 | 11,4 | $1{,}76\times10^{-2}$ |
| F0 | 1,6 | 0,06 | 0,15 | 13,4 | $1{,}14\times10^{-2}$ |
| **F5 — Kraft** | 1,3 | 0,08 | 0,22 | 41,3 | $5{,}2\times10^{-3}$ |
| G0 | 1,05 | 0,07 | 0,16 | 126 | $1{,}2\times10^{-3}$ |
| **Güneş** | 1,0 | 0,070 | 0,15 | 607 | $2{,}4\times10^{-4}$ |
| K0 | 0,85 | 0,10 | 0,18 | 270 | $6{,}5\times10^{-4}$ |
| M0 | 0,51 | 0,15 | 0,19 | 175 | $1{,}1\times10^{-3}$ |

Yasa yıldızlarda dönemi 50–4.000 kat kısa öngörür. **Bu bir başarısızlık değil, ölçümdür:** sapma tam olarak $\eta_z$'dir ve yapısı rastgele değildir.

Bölümün bu sınavdan çıkan **bağımsız sonucu** şudur: B0'dan F0'a — kütlede **10 kat** menzil — $\eta_z$ yalnız $1{,}14$ ile $1{,}95\times10^{-2}$ arasında gezinir, yani **1,7 kat içinde toplanır** (geometrik ortalama $1{,}56\times10^{-2}$). Radyatif zarflı yıldızlar tek bir platoya oturur. Dahası, T Tauri evresinin değeri ($1{,}71\times10^{-2}$) aynı platodadır: **yıldızlar bu değerle doğar ve kanalı kapalı olanlar orada kalır.** Kraft kırılmasıyla birlikte plato terk edilir — F5 üçte bire, G0 onda bire, Güneş altmışta bire iner; 11.3.4'ün Skumanich sızıntısı bu düşüşün ta kendisidir.

O5'in platonun altında kalması (6,2×10⁻³) beklenen bir sapmadır: çok masif yıldızlar çizgi-sürüklemeli güçlü rüzgârlarla ayrıca frenlenir, yani onlarda kanal radyatif zarfa rağmen kısmen açıktır.

### Sınav 3 — Zarf merdiveni

Bütün sınıflar aynı eksene konunca beş plato ve altı mertebe görünür (beyaz cüce ile nötron yıldızı tek basamağı paylaşır):

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 470" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Zarf ifade carpani merdiveni: alti sinif">
<rect x="0" y="0" width="940" height="470" fill="#0b0f19"/>
<line x1="269.2" y1="60.0" x2="269.2" y2="400.0" stroke="#182338" stroke-width="1.0"/>
<text x="269.2" y="418.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-6</tspan></text>
<line x1="365.5" y1="60.0" x2="365.5" y2="400.0" stroke="#182338" stroke-width="1.0"/>
<text x="365.5" y="418.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-5</tspan></text>
<line x1="461.7" y1="60.0" x2="461.7" y2="400.0" stroke="#182338" stroke-width="1.0"/>
<text x="461.7" y="418.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-4</tspan></text>
<line x1="558.0" y1="60.0" x2="558.0" y2="400.0" stroke="#182338" stroke-width="1.0"/>
<text x="558.0" y="418.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-3</tspan></text>
<line x1="654.2" y1="60.0" x2="654.2" y2="400.0" stroke="#182338" stroke-width="1.0"/>
<text x="654.2" y="418.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-2</tspan></text>
<line x1="750.5" y1="60.0" x2="750.5" y2="400.0" stroke="#182338" stroke-width="1.0"/>
<text x="750.5" y="418.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">-1</tspan></text>
<line x1="846.7" y1="60.0" x2="846.7" y2="400.0" stroke="#182338" stroke-width="1.0"/>
<text x="846.7" y="418.0" fill="#8fa3c0" font-size="12" text-anchor="middle">1</text>
<rect x="250" y="60" width="640" height="340" fill="none" stroke="#8fa3c0"/>
<text x="570.0" y="442.0" fill="#8fa3c0" font-size="14" text-anchor="middle">zarf ifade çarpanı  η_z = L(gözlenen) / 𝒜₀M²</text>
<text x="40.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.H — Zarf merdiveni: beş plato, altı mertebe</text>
<text x="236.0" y="99.0" fill="#8fa3c0" font-size="12" text-anchor="end">Gezegenler (serbest 5)</text>
<rect x="824.6" y="83.0" width="56.3" height="24" fill="#ffb84d" opacity="0.13"/>
<circle cx="824.6" cy="95.0" r="4.5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="833.5" cy="95.0" r="4.5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="837.4" cy="95.0" r="4.5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="852.2" cy="95.0" r="4.5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="881.0" cy="95.0" r="4.5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="810.6" y="99.0" fill="#ffb84d" font-size="11" text-anchor="end">plato 0,98</text>
<text x="236.0" y="154.0" fill="#8fa3c0" font-size="12" text-anchor="end">Yıldızaltı (kahverengi cüce)</text>
<rect x="684.0" y="138.0" width="44.1" height="24" fill="#5ce6a8" opacity="0.13"/>
<circle cx="684.0" cy="150.0" r="4.5" fill="none" stroke="#5ce6a8" stroke-width="1.6"/>
<circle cx="728.1" cy="150.0" r="4.5" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="740.1" y="154.0" fill="#5ce6a8" font-size="11" text-anchor="start">dönem △ 0,020 · vsini ▲ 0,059</text>
<text x="236.0" y="209.0" fill="#8fa3c0" font-size="12" text-anchor="end">Yıldız doğumu + radyatif anakol</text>
<rect x="659.7" y="193.0" width="22.4" height="24" fill="#4dd2ff" opacity="0.13"/>
<circle cx="676.6" cy="205.0" r="4.5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="667.7" cy="205.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="662.9" cy="205.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="681.0" cy="205.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="682.1" cy="205.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="677.8" cy="205.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="659.7" cy="205.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="694.1" y="209.0" fill="#4dd2ff" font-size="11" text-anchor="start">plato 0,0138 (Gaia, n = 19.659)</text>
<text x="236.0" y="264.0" fill="#8fa3c0" font-size="12" text-anchor="end">Kraft sonrası (konvektif, yaşlı)</text>
<rect x="499.2" y="248.0" width="127.7" height="24" fill="#4dd2ff" opacity="0.13"/>
<circle cx="626.9" cy="260.0" r="4.5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="565.6" cy="260.0" r="4.5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="499.2" cy="260.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="540.0" cy="260.0" r="4.5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="562.0" cy="260.0" r="4.5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="638.9" y="264.0" fill="#4dd2ff" font-size="11" text-anchor="start">yaşla düşer</text>
<text x="236.0" y="319.0" fill="#8fa3c0" font-size="12" text-anchor="end">Beyaz cüceler (n = 31)</text>
<circle cx="324.4" cy="315.0" r="4.5" fill="#ffffff" stroke="#ffffff" stroke-width="1.6"/>
<text x="336.4" y="319.0" fill="#ffffff" font-size="11" text-anchor="start">plato 3,7×10⁻⁶</text>
<text x="236.0" y="374.0" fill="#8fa3c0" font-size="12" text-anchor="end">Nötron yıldızları (n = 2.527)</text>
<circle cx="300.3" cy="370.0" r="4.5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="312.3" y="374.0" fill="#b58cff" font-size="11" text-anchor="start">plato 2,1×10⁻⁶</text>
<line x1="562.0" y1="60.0" x2="562.0" y2="400.0" stroke="#ff6b6b" stroke-width="1.6" stroke-dasharray="6 5"/>
<text x="554.0" y="78.0" fill="#ff6b6b" font-size="11" text-anchor="end">Kerr tavanı  η_z = 1,1×10⁻³</text>
<path d="M 302.2 384 L 327.3 384" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="2 3"/>
<text x="345.0" y="396.0" fill="#ffffff" font-size="11" text-anchor="start">beyaz cüce ↔ nötron yıldızı: 1,8 kat — ikisi de zarfını atmış</text>
<text x="40.0" y="456.0" fill="#8fa3c0" font-size="11" text-anchor="start">Gezegen platosunun 1'e oturması kalibrasyondur (dairesel). Bağımsız sonuçlar: radyatif platonun 19.659 yıldızla doğrulanması ve beyaz cüce–nötron yıldızı basamağının çakışması.</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.H: Zarf merdiveni, η_z = L(gözlenen)/𝒜₀M². Altı sınıf altı mertebeye yayılır ve sıralama tek yönlüdür: gövde ne kadar rijit ve kanalı kapalıysa yükleme yasasının o kadar büyük payını taşır. Yıldızaltı sınıfında içi boş daire gerçek dönme döneminden, dolu daire v sin i'den gelir; aradaki 2,9 kat v sin i örnekleminin hızlı dönenlere seçilmesidir. Merdivenin en alt basamağını beyaz cüceler ve nötron yıldızları 1,8 kat içinde paylaşır — yarıçapları 700 kat farklı olmasına rağmen, çünkü ortak özellikleri zarfını atmış olmaktır.</em></p>
</div>

| Sınıf | $\eta_z$ platosu | Zarf durumu |
|---|---|---|
| Gezegenler (serbest) | **0,98** | rijit, kanal kapalı — *(kalibrasyon)* |
| Kahverengi cüce / genç dev | **0,020** (dönem) · 0,055 ($v\sin i$, üst sınır) | tavana dayanmış, kanal kısmen açık |
| Yıldız doğumu + radyatif anakol | **0,015** — Gaia ile **0,0138** (Sınav 5) | plazma zarf, kanal kapalı |
| Kraft sonrası (konvektif, yaşlı) | $10^{-4}$–$5\times10^{-3}$ | kanal açık, yaşla düşer |
| **Beyaz cüceler** | $\mathbf{3{,}7\times10^{-6}}$ | **zarf atılmış** — nötron yıldızıyla aynı basamak |
| Nötron yıldızları | $2{,}1\times10^{-6}$ (2.527 pulsar) | zarf yok, çıplak fren |

Merdivenin okunuşu tek cümledir: **gövde ne kadar rijit ve kapalıysa yükleme yasasının o kadar büyük payını taşır.** Kerr tavanı bu eksende $\eta_z=1{,}1\times10^{-3}$'e düşer — Güneş'in bugünkü değeri bile tavanın altındadır.

### Sınav 4 — $\Omega_{makro}$ bandı

Yükleme yasası dönemi *hesaplar*; ama gözlemin kendisi daha çıplak bir olguyu gösterir. Kapalı zarflı ve serbest dönen gövdelerin dönemleri, kütleleri ne olursa olsun dar bir banda sıkışır:

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 560" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Omega makro bandi: asteroitten yildizlara donme donemi">
<rect x="0" y="0" width="940" height="560" fill="#0b0f19"/>
<line x1="115.9" y1="58.0" x2="115.9" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="115.9" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">13</tspan></text>
<line x1="199.6" y1="58.0" x2="199.6" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="199.6" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">15</tspan></text>
<line x1="283.3" y1="58.0" x2="283.3" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="283.3" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">17</tspan></text>
<line x1="367.0" y1="58.0" x2="367.0" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="367.0" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">19</tspan></text>
<line x1="450.7" y1="58.0" x2="450.7" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="450.7" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">21</tspan></text>
<line x1="534.3" y1="58.0" x2="534.3" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="534.3" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">23</tspan></text>
<line x1="618.0" y1="58.0" x2="618.0" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="618.0" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">25</tspan></text>
<line x1="701.7" y1="58.0" x2="701.7" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="701.7" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">27</tspan></text>
<line x1="785.4" y1="58.0" x2="785.4" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="785.4" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">29</tspan></text>
<line x1="869.1" y1="58.0" x2="869.1" y2="455.0" stroke="#182338" stroke-width="1.0"/>
<text x="869.1" y="473.0" fill="#8fa3c0" font-size="12" text-anchor="middle">10<tspan baseline-shift="super" font-size="9">31</tspan></text>
<line x1="95.0" y1="418.9" x2="890.0" y2="418.9" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="422.9" fill="#8fa3c0" font-size="12" text-anchor="end">1</text>
<line x1="95.0" y1="328.7" x2="890.0" y2="328.7" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="332.7" fill="#8fa3c0" font-size="12" text-anchor="end">10</text>
<line x1="95.0" y1="238.5" x2="890.0" y2="238.5" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="242.5" fill="#8fa3c0" font-size="12" text-anchor="end">100</text>
<line x1="95.0" y1="148.2" x2="890.0" y2="148.2" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="152.2" fill="#8fa3c0" font-size="12" text-anchor="end">1000</text>
<line x1="95.0" y1="58.0" x2="890.0" y2="58.0" stroke="#182338" stroke-width="1.0"/>
<text x="87.0" y="62.0" fill="#8fa3c0" font-size="12" text-anchor="end">10.000</text>
<rect x="95" y="58" width="795" height="397" fill="none" stroke="#8fa3c0"/>
<text x="492.5" y="497.0" fill="#8fa3c0" font-size="14" text-anchor="middle">kütle M [kg]</text>
<text x="30" y="256" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 30 256)">dönme dönemi P [saat]</text>
<text x="95.0" y="32.0" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.I — Ω_makro bandı 19 mertebe kütlede ayakta: asteroitten B5 yıldızına</text>
<rect x="95" y="293.4" width="795" height="104.7" fill="#ffb84d" opacity="0.10"/>
<text x="105.0" y="285.4" fill="#ffb84d" font-size="12" text-anchor="start">Ω_makro bandı: 1,7 – 24,6 saat</text>
<path d="M 104.4,302.1 L 140.4,295.1 L 177.3,303.6 L 216.7,301.0 L 259.6,301.9 L 302.2,303.8 L 341.2,304.5 L 385.3,332.3 L 385.3,351.7 L 341.2,336.8 L 302.2,332.6 L 259.6,342.2 L 216.7,352.9 L 177.3,361.1 L 140.4,360.3 L 104.4,360.6 Z" fill="#ff9ecd" opacity="0.18" stroke="none"/>
<path d="M 104.4 343.1 L 140.4 339.8 L 177.3 339.6 L 216.7 332.1 L 259.6 324.8 L 302.2 319.3 L 341.2 323.6 L 385.3 343.1" fill="none" stroke="#ff9ecd" stroke-width="2"/>
<text x="397.3" y="333.1" fill="#ff9ecd" font-size="11" text-anchor="start">asteroitler: n = 19.929  (bant: çeyrekler arası)</text>
<circle cx="426.1" cy="353.3" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="434.1" y="365.3" fill="#ffb84d" font-size="11" text-anchor="start">Vesta</text>
<circle cx="449.5" cy="332.5" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="441.5" y="326.5" fill="#ffb84d" font-size="11" text-anchor="end">Ceres</text>
<circle cx="568.1" cy="293.4" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="560.1" y="287.4" fill="#ffb84d" font-size="11" text-anchor="end">Mars</text>
<circle cx="608.7" cy="294.5" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="616.7" y="288.5" fill="#ffb84d" font-size="11" text-anchor="start">Dünya</text>
<circle cx="660.2" cy="310.0" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="668.2" y="324.0" fill="#ffb84d" font-size="11" text-anchor="start">Neptün</text>
<circle cx="691.4" cy="326.5" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="683.4" y="340.5" fill="#ffb84d" font-size="11" text-anchor="end">Satürn</text>
<circle cx="713.4" cy="329.0" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="721.4" y="341.0" fill="#ffb84d" font-size="11" text-anchor="start">Jüpiter</text>
<path d="M 758.5 331.9 L 763.5 346.1 L 753.5 346.1 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<path d="M 773.9 350.5 L 778.9 364.6 L 768.9 364.6 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<path d="M 780.4 391.5 L 785.4 405.7 L 775.4 405.7 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="790.4" y="400.5" fill="#5ce6a8" font-size="11" text-anchor="start">yıldızaltı</text>
<circle cx="848.3" cy="317.2" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="852.3" cy="323.5" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="859.1" cy="319.3" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="871.9" cy="308.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="879.9" y="300.1" fill="#4dd2ff" font-size="11" text-anchor="start">radyatif yıldızlar</text>
<circle cx="832.2" cy="286.4" r="5.5" fill="#ffffff" stroke="#ffffff" stroke-width="1.6"/>
<text x="822.2" y="290.4" fill="#ffffff" font-size="11" text-anchor="end">beyaz cüce (medyan)</text>
<path d="M 556.0 128.8 L 562.0 134.8 L 556.0 140.8 L 550.0 134.8 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.4"/>
<text x="568.0" y="138.8" fill="#ff6b6b" font-size="11" text-anchor="start">Merkür</text>
<path d="M 605.0 73.1 L 611.0 79.1 L 605.0 85.1 L 599.0 79.1 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.4"/>
<text x="617.0" y="83.1" fill="#ff6b6b" font-size="11" text-anchor="start">Venüs</text>
<path d="M 795.8 241.6 L 801.8 247.6 L 795.8 253.6 L 789.8 247.6 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.4"/>
<text x="807.8" y="251.6" fill="#ff6b6b" font-size="11" text-anchor="start">Trappist-1</text>
<path d="M 839.7 161.8 L 845.7 167.8 L 839.7 173.8 L 833.7 167.8 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.4"/>
<text x="851.7" y="171.8" fill="#ff6b6b" font-size="11" text-anchor="start">Güneş</text>
<text x="300.0" y="95.0" fill="#ff6b6b" font-size="12" text-anchor="start">◆ banttan kaçanlar: kanalı açık ya da kavranmış gövdeler</text>
<text x="95.0" y="528.0" fill="#8fa3c0" font-size="11" text-anchor="start">Not: asteroit bandının hafif eğimi ve yıldızaltı ucundaki daralma gerçektir; bant tam düz olsaydı L ∝ MR² olurdu. Beyaz cüce bandın içindedir ama açısal momentumu 10⁵ kat düşüktür — dönem darlığı L eşitliği anlamına gelmez.</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.I: Ω_makro bandı, artık 19 mertebe kütle boyunca. Pembe bant 19.929 asteroitin çeyrekler arası aralığı, pembe çizgi medyanıdır (8,3 saat); kütlede yedi mertebe boyunca bant neredeyse yatay kalır. Turuncu daireler gezegenler, yeşil üçgenler yıldızaltı cisimler, mavi daireler radyatif yıldızlar, beyaz daire beyaz cücelerin medyanıdır. Kırmızı eşkenar dörtgenler banttan kaçanlardır ve dördü de teorinin önceden ayırdığı sınıflardandır: Merkür ile Venüs kavranmış (M-24), Güneş ile Trappist-1 konvektif-açık kanallı. Dikkat: dönem darlığı açısal momentum eşitliği demek değildir — beyaz cüce bandın içindedir ama L'si 10⁵ kat küçüktür.</em></p>
</div>

Vesta'dan ($2{,}6\times10^{20}$ kg) B5 yıldızına ($1{,}2\times10^{31}$ kg) — kütlede **10,7 mertebe** — dönemler yalnız **1,7 ile 24,6 saat** arasındadır, yani 14 kat. Karşılaştırma için aynı gövdelerin açısal momentumları arasında $10^{11}$ kattan fazla fark vardır. Banttan kaçan dört gövdenin dördü de teorinin önceden ayırdığı sınıflardandır:

| Kaçan | $P$ (sa) | Bandın kaç katı | Nedeni |
|---|---|---|---|
| Trappist-1 (M8) | 79,2 | 3 | konvektif, kanal açık |
| Güneş (G2) | 607 | 25 | konvektif, kanal açık |
| Merkür | 1.408 | 57 | kavranmış (M-24) |
| Venüs | 5.833 | 237 | kavranmış (M-24) |

**Dürüst kayıt.** Bant tam düz değildir ve olmaması da gerekir: tam düz olsaydı $L\propto MR^2$ olurdu, yani $M^{1{,}75}$; gözlenen $M^{1{,}885}$'tir. Bandın içindeki hafif eğim, tam da bu farkın kendisidir. Yani "kilit" mutlak değil, dar bir kuşaktır — ama kuşağın darlığı (10,7 mertebeye karşı 14 kat) rastlantıyla açıklanamayacak kadar keskindir.

### Sınav 5 — İki katalog, 711.356 yıldız: plato doğrulanır, kırılma yumuşar

Buraya kadarki yıldız sınavı 11 tayf-türü **ortalamasına** dayanıyordu (Fukuda, 1982). Bu, bölümün en zayıf halkasıydı: $n=6$ ile kurulmuş bir plato. Aynı sınav artık tek tek yıldız düzeyinde, iki bağımsız katalogla tekrarlanabilir:

| Katalog | Dönüş ölçümü | $n$ | Güçlü olduğu yer |
|---|---|---|---|
| Santos ve ark. (2021) — Kepler | **gerçek $P_{rot}$** (leke modülasyonu), 0,24–187 gün | 39.591 | soğuk ve yavaş dönenler; $\sin i$ belirsizliği **yok** |
| Gaia DR3 (`vbroad` + FLAME) | çizgi genişlemesi, $\langle\sin i\rangle=\pi/4$ düzeltmeli | 671.765 | sıcak ve hızlı dönenler; kütle+yarıçap aynı tabloda |

İki katalogda $\eta_z=L_{g\ddot{o}z}/\mathcal{A}_0M^2$ aynı yolla hesaplanır. Kepler'de yarıçap $R=\sqrt{\mathcal{G}M/g}$ ile $\log g$'den, Gaia'da doğrudan `radius_flame`'den gelir; eylemsizlik çarpanı $k^2$ **her iki sette de Sınav 2'nin kütle atamasıyla aynıdır**, yani yeni bir serbest parametre girmez. Ölçüt yeniden yerel değildir: $\mathcal{A}_0$ hem yükleme hem $\mathcal{G}$ üzerinden yerel $\rho_0$ taşır (11.3.1 uyarısı), ama Güneş komşuluğundaki bir yıldız örnekleminde bu ortak çarpan sabit sayılabilir.

**(i) Radyatif plato doğrulanır — $n=6$'dan $n=19.659$'a.** Gaia'nın `vbroad` bağıl hatası %10'un altındaki yıldızlarıyla, $1{,}5$–$5{,}0\,M_\odot$ aralığında:

$$\eta_z=1{,}381\times10^{-2}\ ,\qquad \sigma=0{,}262\ \text{dex}\;(1{,}83\ \text{kat})\ ,\qquad n=19.659$$

Sınav 2 aynı platoyu, bambaşka bir veri zincirinden — 1982'nin altı tayf-türü ortalamasından — $1{,}56\times10^{-2}$ olarak verir. **İki bağımsız ölçüm arasındaki sapma %11,5.** Ve plato gerçekten düz: kütlede 3,3 kat menzil boyunca yalnız 1,29 kat oynar.

| $M/M_\odot$ | $n$ | $\eta_z$ | $\sigma$ (dex) | medyan `vbroad` (km/s) |
|---|---|---|---|---|
| 0,5–0,9 | 149 | $2{,}87\times10^{-3}$ | 0,253 | 10,5 |
| 0,9–1,1 | 388 | $3{,}27\times10^{-3}$ | 0,377 | 13,6 |
| 1,1–1,3 | 2.670 | $5{,}69\times10^{-3}$ | 0,280 | 28,9 |
| 1,3–1,5 | 7.924 | $8{,}09\times10^{-3}$ | 0,280 | 43,3 |
| **1,5–1,8** | 12.112 | $1{,}325\times10^{-2}$ | 0,250 | 89,3 |
| **1,8–2,2** | 3.458 | $1{,}365\times10^{-2}$ | 0,264 | 109,8 |
| **2,2–3,0** | 3.994 | $1{,}577\times10^{-2}$ | 0,286 | 145,9 |
| **3,0–5,0** | 95 | $1{,}715\times10^{-2}$ | 0,307 | 177,0 |

1982'nin tayf ortalamalarıyla 2022 Gaia'sının yirmi bin tek tek yıldızının %11,5'te buluşması, bu bölümün en güçlü bağımsız sonucudur — çünkü iki ölçüm zinciri (fotografik tayf çizgisi genişlemesi ↔ uzay teleskobu çizgi profili + FLAME evrim modeli) hiçbir girdiyi paylaşmaz.

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 560" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Iki katalogda zarf ifade carpani: rampa ve radyatif plato">
<rect x="0" y="0" width="940" height="560" fill="#0b0f19"/>
<line x1="132.5" y1="58" x2="132.5" y2="470" stroke="#182338"/>
<text x="132.5" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">0,5</text>
<line x1="246.4" y1="58" x2="246.4" y2="470" stroke="#182338"/>
<text x="246.4" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">1</text>
<line x1="360.4" y1="58" x2="360.4" y2="470" stroke="#182338"/>
<text x="360.4" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">2</text>
<line x1="511.0" y1="58" x2="511.0" y2="470" stroke="#182338"/>
<text x="511.0" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">5</text>
<line x1="625.0" y1="58" x2="625.0" y2="470" stroke="#182338"/>
<text x="625.0" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10</text>
<line x1="739.0" y1="58" x2="739.0" y2="470" stroke="#182338"/>
<text x="739.0" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">20</text>
<line x1="852.9" y1="58" x2="852.9" y2="470" stroke="#182338"/>
<text x="852.9" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">40</text>
<line x1="95" y1="413.2" x2="890" y2="413.2" stroke="#182338"/>
<text x="87" y="417.2" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻⁴</text>
<line x1="95" y1="345.4" x2="890" y2="345.4" stroke="#182338"/>
<text x="87" y="349.4" fill="#8fa3c0" font-size="12" text-anchor="end">3×10⁻⁴</text>
<line x1="95" y1="271.1" x2="890" y2="271.1" stroke="#182338"/>
<text x="87" y="275.1" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻³</text>
<line x1="95" y1="203.3" x2="890" y2="203.3" stroke="#182338"/>
<text x="87" y="207.3" fill="#8fa3c0" font-size="12" text-anchor="end">3×10⁻³</text>
<line x1="95" y1="129.0" x2="890" y2="129.0" stroke="#182338"/>
<text x="87" y="133.0" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻²</text>
<line x1="95" y1="61.3" x2="890" y2="61.3" stroke="#182338"/>
<text x="87" y="65.3" fill="#8fa3c0" font-size="12" text-anchor="end">3×10⁻²</text>
<rect x="95" y="71.9" width="795" height="74.4" fill="#5ce6a8" opacity="0.10"/>
<rect x="95" y="58" width="795" height="412" fill="none" stroke="#8fa3c0"/>
<text x="492.5" y="514" fill="#8fa3c0" font-size="14" text-anchor="middle">kütle M [M☉]</text>
<text x="26" y="264" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 264)">zarf ifade çarpanı  η_z = L(gözlenen) / 𝒜₀M²</text>
<text x="95" y="32" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.J — Radyatif plato 19.659 yıldızla doğrulanır; Kraft geçişi rampaya dönüşür</text>
<line x1="95" y1="101.6" x2="890" y2="101.6" stroke="#ffb84d" stroke-width="1.2" stroke-dasharray="2 6"/>
<text x="105" y="96" fill="#ffb84d" font-size="12" text-anchor="start">kitap Sınav 2 platosu 1,56×10⁻² (n = 6)</text>
<line x1="95" y1="109.1" x2="890" y2="109.1" stroke="#5ce6a8" stroke-width="2" stroke-dasharray="8 5"/>
<text x="105" y="135" fill="#5ce6a8" font-size="12" text-anchor="start">Gaia platosu 1,381×10⁻² ± 0,26 dex  (n = 19.659) → %11,5</text>
<line x1="289.6" y1="155" x2="289.6" y2="470" stroke="#8fa3c0" stroke-width="1.2" stroke-dasharray="5 5"/>
<text x="285" y="458" fill="#8fa3c0" font-size="11" text-anchor="end">Kraft 1,3 M☉</text>
<line x1="191.7" y1="277.9" x2="191.7" y2="372.0" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="218.5" y1="282.4" x2="218.5" y2="363.6" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="237.3" y1="273.2" x2="237.3" y2="360.1" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="253.8" y1="249.6" x2="253.8" y2="346.2" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="269.1" y1="216.8" x2="269.1" y2="318.8" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="282.9" y1="192.1" x2="282.9" y2="290.2" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="295.0" y1="172.8" x2="295.0" y2="270.5" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="306.7" y1="167.8" x2="306.7" y2="264.9" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="321.3" y1="147.6" x2="321.3" y2="249.9" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="342.4" y1="114.2" x2="342.4" y2="223.0" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<line x1="371.1" y1="60.0" x2="371.1" y2="184.5" stroke="#4dd2ff" stroke-width="1" opacity="0.45"/>
<circle cx="191.7" cy="325.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="218.5" cy="323.0" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="237.3" cy="316.6" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="253.8" cy="297.9" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="269.1" cy="267.8" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="282.9" cy="241.2" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="295.0" cy="221.7" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="306.7" cy="216.4" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="321.3" cy="198.8" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="342.4" cy="168.6" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<circle cx="371.1" cy="119.4" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<line x1="203.5" y1="170.1" x2="203.5" y2="242.0" stroke="#5ce6a8" stroke-width="1" opacity="0.45"/>
<line x1="250.2" y1="144.5" x2="250.2" y2="251.6" stroke="#5ce6a8" stroke-width="1" opacity="0.45"/>
<line x1="281.1" y1="124.1" x2="281.1" y2="203.7" stroke="#5ce6a8" stroke-width="1" opacity="0.45"/>
<line x1="302.5" y1="102.3" x2="302.5" y2="181.9" stroke="#5ce6a8" stroke-width="1" opacity="0.45"/>
<line x1="326.2" y1="76.2" x2="326.2" y2="147.2" stroke="#5ce6a8" stroke-width="1" opacity="0.45"/>
<line x1="357.8" y1="72.3" x2="357.8" y2="147.3" stroke="#5ce6a8" stroke-width="1" opacity="0.45"/>
<line x1="390.8" y1="60.3" x2="390.8" y2="141.6" stroke="#5ce6a8" stroke-width="1" opacity="0.45"/>
<line x1="444.4" y1="60.0" x2="444.4" y2="139.4" stroke="#5ce6a8" stroke-width="1" opacity="0.45"/>
<rect x="199" y="201.5" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<rect x="245.7" y="193.6" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<rect x="276.6" y="159.4" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<rect x="298" y="137.6" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<rect x="321.7" y="107.2" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<rect x="353.3" y="105.3" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<rect x="386.3" y="96.4" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<rect x="439.9" y="91.2" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<path d="M 852.9 152.5 L 858.9 163.5 L 846.9 163.5 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="843" y="150" fill="#ffb84d" font-size="11" text-anchor="end">O5</text>
<path d="M 702.3 110.3 L 708.3 121.3 L 696.3 121.3 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="711" y="112" fill="#ffb84d" font-size="11" text-anchor="start">B0</text>
<path d="M 538.3 83.4 L 544.3 94.4 L 532.3 94.4 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="547" y="86" fill="#ffb84d" font-size="11" text-anchor="start">B5</text>
<path d="M 421.5 81.8 L 427.5 92.8 L 415.5 92.8 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="430" y="76" fill="#ffb84d" font-size="11" text-anchor="start">A0</text>
<path d="M 360.4 88.2 L 366.4 99.2 L 354.4 99.2 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="352" y="84" fill="#ffb84d" font-size="11" text-anchor="end">A5</text>
<path d="M 323.7 115.0 L 329.7 126.0 L 317.7 126.0 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="315" y="112" fill="#ffb84d" font-size="11" text-anchor="end">F0</text>
<path d="M 289.6 163.4 L 295.6 174.4 L 283.6 174.4 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="299" y="166" fill="#ffb84d" font-size="11" text-anchor="start">F5</text>
<path d="M 254.5 253.9 L 260.5 264.9 L 248.5 264.9 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="264" y="256" fill="#ffb84d" font-size="11" text-anchor="start">G0</text>
<path d="M 219.7 291.7 L 225.7 302.7 L 213.7 302.7 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="229" y="294" fill="#ffb84d" font-size="11" text-anchor="start">K0</text>
<path d="M 135.7 259.2 L 141.7 270.2 L 129.7 270.2 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="145" y="262" fill="#ffb84d" font-size="11" text-anchor="start">M0</text>
<circle cx="246.4" cy="359.2" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="255" y="371" fill="#ff6b6b" font-size="11" text-anchor="start">Güneş</text>
<path d="M 379.2 239.1 L 386.2 246.1 L 379.2 253.1 L 372.2 246.1 Z" fill="none" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="391" y="243" fill="#ff6b6b" font-size="11" text-anchor="start">ötegezegen ev sahipleri (n = 388) — yavaş dönene seçilmiş, plato geçersiz</text>
<circle cx="112" cy="384" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<text x="125" y="388" fill="#4dd2ff" font-size="12" text-anchor="start">Kepler / Santos 2021 — gerçek P_rot (n = 39.591); çubuk: popülasyon σ</text>
<rect x="107.5" y="397.5" width="9" height="9" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<text x="125" y="406" fill="#5ce6a8" font-size="12" text-anchor="start">Gaia DR3 vbroad + FLAME, bağıl hata &lt; %10 (n = 30.790)</text>
<path d="M 112 415 L 118 426 L 106 426 Z" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="125" y="424" fill="#ffb84d" font-size="12" text-anchor="start">Fukuda 1982 tayf ortalamaları — kitabın Sınav 2 girdisi (n = 6 + 5)</text>
<circle cx="112" cy="438" r="4.5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.4"/>
<text x="125" y="442" fill="#ff6b6b" font-size="12" text-anchor="start">Güneş (helyosismik) · ◇ seçim etkili örneklem</text>
<text x="125" y="460" fill="#8fa3c0" font-size="11" text-anchor="start">Soğuk dilimlerde Gaia yeşilleri makrotürbülans tabanına oturur: üst sınırdır, ölçüm değil.</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.J: İki bağımsız katalogda zarf ifade çarpanı. Yeşil bant, Gaia'nın 19.659 yıldızlı radyatif platosu (1,381×10⁻² ± 0,26 dex); turuncu noktalı çizgi, kitabın altı tayf ortalamasından kurduğu platodur (1,56×10⁻²) — ikisi %11,5 içinde. Mavi daireler Kepler'in gerçek dönme dönemlerinden, yeşil kareler Gaia çizgi genişlemesinden gelir. Soğuk uçta iki katalogun ayrışması gerçek bir fark değil, Gaia vbroad'ının makrotürbülans tabanıdır. Boş kırmızı eşkenar dörtgen, ötegezegen ev sahibi yıldızların örneklemi: platonun 9 kat altında, çünkü hızlı dönenler geçiş ve dikine hız yöntemleriyle bulunamaz.</em></p>
</div>

**(ii) Kırılma keskin değil, rampa.** Kepler'in **gerçek dönme dönemleriyle** (dolayısıyla $\sin i$ belirsizliği olmadan) $0{,}75$–$2{,}0\,M_\odot$ aralığında $n=39.048$ yıldıza tek bir güç yasası uydurulur:

$$\log\eta_z=-3{,}173+(3{,}444\pm0{,}020)\,\log M\ ,\qquad \text{artık }\sigma=0{,}327\ \text{dex}$$

Buna karşı, "Kraft kırılması keskin bir süreksizliktir" okumasının doğal modeli $1{,}3\,M_\odot$'ta atlayan bir basamaktır: altta $\eta_z=6{,}26\times10^{-4}$, üstte $2{,}59\times10^{-3}$, yani **4,13 kat** basamak. İki model de iki serbest parametre kullanır, dolayısıyla doğrudan karşılaştırılabilir:

| Model | Serbest parametre | Artık kareler toplamı |
|---|---|---|
| basamak ($1{,}3\,M_\odot$'ta süreksiz) | 2 | 5.428,6 |
| **rampa** ($\eta_z\propto M^{3{,}44}$) | 2 | **4.172,6** |

**Rampa basamağı %23,1 farkla yener.** Yani $\eta_z$ ekseninde Kraft eşiği bir duvar değil, $1{,}0$–$1{,}8\,M_\odot$ arasına yayılan bir yamaçtır. **Zarf türünün anahtar olduğu iddiası ayakta, "keskin süreksizlik" iddiası değil.** Kraft'ın kendi keskinliği $\langle v\sin i\rangle$ ekseninde gerçektir; $\eta_z$'ye çevrildiğinde $R^2$ çarpanı onu yayar.

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 520" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Kraft gecisinde basamak modeli ile rampa modelinin karsilastirmasi">
<rect x="0" y="0" width="940" height="520" fill="#0b0f19"/>
<line x1="118.1" y1="58" x2="118.1" y2="430" stroke="#182338"/>
<text x="118.1" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">0,7</text>
<line x1="206.7" y1="58" x2="206.7" y2="430" stroke="#182338"/>
<text x="206.7" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">0,8</text>
<line x1="284.9" y1="58" x2="284.9" y2="430" stroke="#182338"/>
<text x="284.9" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">0,9</text>
<line x1="354.9" y1="58" x2="354.9" y2="430" stroke="#182338"/>
<text x="354.9" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">1,0</text>
<line x1="476.0" y1="58" x2="476.0" y2="430" stroke="#182338"/>
<text x="476.0" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">1,2</text>
<line x1="578.3" y1="58" x2="578.3" y2="430" stroke="#182338"/>
<text x="578.3" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">1,4</text>
<line x1="667.0" y1="58" x2="667.0" y2="430" stroke="#182338"/>
<text x="667.0" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">1,6</text>
<line x1="745.2" y1="58" x2="745.2" y2="430" stroke="#182338"/>
<text x="745.2" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">1,8</text>
<line x1="847.5" y1="58" x2="847.5" y2="430" stroke="#182338"/>
<text x="847.5" y="448" fill="#8fa3c0" font-size="12" text-anchor="middle">2,1</text>
<line x1="95" y1="413.6" x2="890" y2="413.6" stroke="#182338"/>
<text x="87" y="417.6" fill="#8fa3c0" font-size="12" text-anchor="end">3×10⁻⁴</text>
<line x1="95" y1="366.4" x2="890" y2="366.4" stroke="#182338"/>
<text x="87" y="370.4" fill="#8fa3c0" font-size="12" text-anchor="end">5×10⁻⁴</text>
<line x1="95" y1="302.5" x2="890" y2="302.5" stroke="#182338"/>
<text x="87" y="306.5" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻³</text>
<line x1="95" y1="238.5" x2="890" y2="238.5" stroke="#182338"/>
<text x="87" y="242.5" fill="#8fa3c0" font-size="12" text-anchor="end">2×10⁻³</text>
<line x1="95" y1="153.9" x2="890" y2="153.9" stroke="#182338"/>
<text x="87" y="157.9" fill="#8fa3c0" font-size="12" text-anchor="end">5×10⁻³</text>
<line x1="95" y1="89.9" x2="890" y2="89.9" stroke="#182338"/>
<text x="87" y="93.9" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻²</text>
<rect x="95" y="58" width="795" height="372" fill="none" stroke="#8fa3c0"/>
<text x="492.5" y="474" fill="#8fa3c0" font-size="14" text-anchor="middle">kütle M [M☉]   ·   Kepler / Santos ve ark. 2021, gerçek dönme dönemleri</text>
<text x="26" y="244" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 244)">η_z = L(gözlenen) / 𝒜₀M²</text>
<text x="95" y="32" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.K — Basamak mı rampa mı: 39.048 yıldız rampayı %23,1 farkla seçiyor</text>
<line x1="529.1" y1="58" x2="529.1" y2="430" stroke="#8fa3c0" stroke-width="1.2" stroke-dasharray="5 5"/>
<text x="524" y="72" fill="#8fa3c0" font-size="11" text-anchor="end">Kraft 1,3 M☉</text>
<path d="M 163.9 345.7 L 529.1 345.7 L 529.1 214.7 L 815.1 214.7" stroke="#ff6b6b" stroke-width="1.6" stroke-dasharray="2 5" fill="none"/>
<text x="180" y="322" fill="#ff6b6b" font-size="12" text-anchor="start">basamak modeli: 6,26×10⁻⁴ → 2,59×10⁻³ (4,13 kat) · RKT 5.429</text>
<line x1="166" y1="430" x2="815.1" y2="118.9" stroke="#5ce6a8" stroke-width="2" stroke-dasharray="8 5"/>
<text x="560" y="292" fill="#5ce6a8" font-size="12" text-anchor="start">rampa modeli: η_z ∝ M^(3,444±0,020) · RKT 4.173</text>
<line x1="134.0" y1="379.9" x2="134.0" y2="386.2" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="242.3" y1="379.5" x2="242.3" y2="380.7" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="318.0" y1="369.9" x2="318.0" y2="371.3" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="384.8" y1="341.6" x2="384.8" y2="343.5" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="446.5" y1="296.4" x2="446.5" y2="298.6" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="502.0" y1="256.5" x2="502.0" y2="258.8" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="551.2" y1="227.1" x2="551.2" y2="229.9" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="598.4" y1="218.5" x2="598.4" y2="222.5" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="657.4" y1="191.9" x2="657.4" y2="196.5" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="742.6" y1="144.7" x2="742.6" y2="153.4" stroke="#4dd2ff" stroke-width="1.6"/>
<line x1="858.5" y1="59.7" x2="858.5" y2="91.2" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="134.0" cy="383.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="242.3" cy="380.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="318.0" cy="370.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="384.8" cy="342.6" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="446.5" cy="297.5" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="502.0" cy="257.7" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="551.2" cy="228.5" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="598.4" cy="220.5" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="657.4" cy="194.2" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="742.6" cy="149.1" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="858.5" cy="75.4" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="105" y="76" fill="#4dd2ff" font-size="12" text-anchor="start">● kütle diliminde geometrik ortalama η_z  ·  çubuk: ortalamanın standart hatası (σ/√n)</text>
<text x="105" y="94" fill="#8fa3c0" font-size="11" text-anchor="start">Popülasyon saçılması çok daha geniştir (0,29–0,46 dex) ve dilim ortalamalarının kesinliğiyle karıştırılmamalıdır.</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.K: Kraft geçişinin biçimi. Onbir kütle diliminin geometrik ortalaması, ortalamanın standart hatasıyla; çubuklar noktadan küçüktür, yani eğilim son derece anlamlıdır. Kırmızı noktalı çizgi 1,3 M☉'ta süreksiz basamak modeli, yeşil kesikli çizgi tek güç yasası rampasıdır. İkisi de iki serbest parametre kullanır; rampanın artık kareler toplamı %23,1 küçüktür. Uydurma aralığı 0,75–2,0 M☉'dır; uçtaki iki nokta (0,72 ve 2,14) uydurmaya girmez.</em></p>
</div>

**(iii) Dört dürüstlük kaydı — hepsi bağlayıcı.**

- **Rampanın 3,444 eğimi bir yasa değildir.** Kepler örneklemi yaş-homojen değildir; açık kanallı yıldızlarda $\eta_z$ yaşın fonksiyonu olduğu için (R2 rejimi) gözlenen eğim, kütle yasasıyla yaş dağılımının çarpımıdır. Eğim ancak yaş-homojen bir örneklemde fizik olarak okunabilir — 11.3.8'in 8. öngörüsü tam bunu sınar.
- **Gaia `vbroad`'ın soğuk uçtaki değerleri üst sınırdır.** Yavaş dönen soğuk yıldızlarda çizgi genişlemesine makrotürbülans hâkimdir; ölçülen `vbroad` gerçek $v_{ekv}$'nun üstündedir. Kanıt bizzat veridedir: $0{,}7$–$1{,}1\,M_\odot$ diliminde $\eta_z$–yaş eğimi $+0{,}191\pm0{,}010$ çıkar, yani Skumanich'in $-0{,}5$'inin **ters işareti**. Bu dilimin sayıları sızıntı ölçümü olarak kullanılamaz; kullanılan yer yalnız $\ge1{,}5\,M_\odot$ platosudur.
- **Yaş sınavı bu veriyle yapılamaz.** Gaia'nın `age_flame` kolonu vardır ama yukarıdaki taban yüzünden konvektif tarafta işe yaramaz; Kepler'in gerçek dönemleri vardır ama bağımsız yaşı yoktur (jirokronoloji kullanmak daireseldir). Sınav, asterosismik yaşlı çok daha küçük bir örneklem gerektirir ve **açık kalemdir** `[F]`.
- **Örneklem seçimi platoyu 9 kat kaydırabilir.** Ötegezegen ev sahibi yıldızların gerçek ölçümlerinden kurulu 388 radyatif yıldız $\eta_z=1{,}55\times10^{-3}$ verir — Gaia platosunun dokuzda biri. Neden fizik değil yöntemdir: hızlı dönen yıldızlarda dikine hız ve geçiş ölçümleri bozulur, dolayısıyla ev sahibi katalogları **yavaş dönenlere seçilmiştir.** Aynı örneklemin konvektif tarafı ($3{,}10\times10^{-4}$) Güneş'in $2{,}45\times10^{-4}$'üyle uyumludur; sapma yalnız radyatif tarafta ve yalnız seçim yönündedir. Bu, platoyu ölçmek isteyen her çalışma için bağlayıcı bir uyarıdır.

Bir de kayda geçmesi gereken bir **eksik**: $k^2$ ataması iki katalogda da yıldız yapı modellerinden gelir ve baskın sistematiktir. Platonun mutlak değeri $k^2$ ile doğrusal ölçeklenir; $k^2$'yi 0,06 yerine 0,05 almak platoyu %17 aşağı çeker. Bu nedenle %11,5'lik uyum, iki zincirin **bağımsızlığından** gelen bir sonuçtur, mutlak kalibrasyon başarısı değildir.

### Sınav 6 — Bütün kütle ekseni: 26 mertebe, altı sınıf, 734.000 gövde

Buraya kadarki sınavlar sınıf sınıf yürüdü. Şimdi hepsi tek eksende toplanır ve **yasanın tanım alanı ölçülür.** Doğru değişken $\mathcal{A}=J/M^{2}$'dir, çünkü bu değişkende hem yükleme yasası hem ufuk tavanı **yatay doğruya** iner:

$$J=\mathcal{A}_0M^{2}\ \Longleftrightarrow\ \mathcal{A}=\mathcal{A}_0=\text{sabit}\ ,\qquad J\le\frac{\mathcal{G}}{c}M^{2}\ \Longleftrightarrow\ \mathcal{A}\le\frac{\mathcal{G}_{yerel}}{c_{yerel}}=\text{sabit}$$

Yani $\mathcal{A}$–$M$ düzleminde teorinin bütün iddiası **iki yatay çizgi ve aralarındaki 897,5 kat**tır. Her sınıf bu iki çizgiye göre nereye düştüğüyle okunur. Kullanılan altı popülasyon:

| Sınıf | Kaynak | $n$ | Kütle menzili (kg) | Dönüş ölçümü |
|---|---|---|---|---|
| Asteroit / küçük gövde | NASA-JPL SBDB (çap + dönme dönemi) | **19.929** | $1{,}8\times10^{4}$–$9{,}6\times10^{20}$ | ışık eğrisi dönemi |
| Gezegen | IAU/NASA-JPL | 8 | $3{,}3\times10^{23}$–$1{,}9\times10^{27}$ | doğrudan dönem |
| Yıldızaltı — dönem | Vos ve ark. (2022), Spitzer/TESS | **15** | $3{,}2\times10^{28}$–$1{,}2\times10^{29}$ | **gerçek $P_{rot}$**, 1,08–32,8 sa |
| Yıldızaltı — $v\sin i$ | BDKP V, Hsu ve ark. (2021), NIRSPEC | **37** | $3{,}2\times10^{28}$–$1{,}2\times10^{29}$ | $v\sin i$, 9–90 km/s |
| Yıldız | Santos 2021 + Gaia DR3 (Sınav 5) | **711.356** | $1{,}0\times10^{29}$–$8\times10^{31}$ | $P_{rot}$ / `vbroad` |
| **Beyaz cüce** | **Hermes ve ark. (2017), Tablo 4** | **31** (DAV) | $8{,}0\times10^{29}$–$1{,}7\times10^{30}$ | **asterosismik $P_{rot}$**, 1,9–74,7 sa |
| Nötron yıldızı | ATNF pulsar kataloğu (`B/psr`) | **2.527** | $\approx2{,}8\times10^{30}$ | atım periyodu |
| Karadelik | GWTC (LIGO-Virgo-KAGRA) + X-ışını derlemesi | **273** + 17 | $3\times10^{30}$–$1{,}3\times10^{40}$ | $\chi_{eff}$ / $a^*$ |

Bu altı popülasyonun tamamı, kategori kategori açılıp kapatılabilen bir panelde teorinin eğrileriyle birlikte incelenebilir: [▶️ Kütle–spin paneli](Simulasyon/kisim11/panel_kutle_spin.html) (ayrı sayfada açılır).

Yıldızaltı kütle ve yarıçapları **UltracoolSheet v2.0** (Best ve ark.) evrim-modeli değerlerinin tayf türü başına medyanından gelir — L0–L4 için 61,5 $M_J$ / 1,05 $R_J$, T5–T9 için 17,7 $M_J$ / 1,08 $R_J$ gibi. Bu sınıfın kütlesi doğrudan ölçüm değil, bölümün en model-bağımlı halkasıdır ve öyle kalır.

<div style="background:#0b0f19;border:1px solid rgba(0,240,255,0.2);border-radius:10px;padding:12px;margin:1.2em 0;">
<svg viewBox="0 0 940 560" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI,sans-serif" role="img" aria-label="Butun kutle ekseninde A=J/M2: iki yatay cizgi ve alti sinif">
<rect x="0" y="0" width="940" height="560" fill="#0b0f19"/>
<line x1="123.4" y1="58" x2="123.4" y2="470" stroke="#182338"/>
<text x="123.4" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10¹⁴</text>
<line x1="180.2" y1="58" x2="180.2" y2="470" stroke="#182338"/>
<text x="180.2" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10¹⁶</text>
<line x1="237.0" y1="58" x2="237.0" y2="470" stroke="#182338"/>
<text x="237.0" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10¹⁸</text>
<line x1="293.8" y1="58" x2="293.8" y2="470" stroke="#182338"/>
<text x="293.8" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁰</text>
<line x1="350.5" y1="58" x2="350.5" y2="470" stroke="#182338"/>
<text x="350.5" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10²²</text>
<line x1="407.3" y1="58" x2="407.3" y2="470" stroke="#182338"/>
<text x="407.3" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁴</text>
<line x1="464.1" y1="58" x2="464.1" y2="470" stroke="#182338"/>
<text x="464.1" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁶</text>
<line x1="520.9" y1="58" x2="520.9" y2="470" stroke="#182338"/>
<text x="520.9" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10²⁸</text>
<line x1="577.7" y1="58" x2="577.7" y2="470" stroke="#182338"/>
<text x="577.7" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁰</text>
<line x1="634.5" y1="58" x2="634.5" y2="470" stroke="#182338"/>
<text x="634.5" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10³²</text>
<line x1="691.2" y1="58" x2="691.2" y2="470" stroke="#182338"/>
<text x="691.2" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁴</text>
<line x1="748.0" y1="58" x2="748.0" y2="470" stroke="#182338"/>
<text x="748.0" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁶</text>
<line x1="804.8" y1="58" x2="804.8" y2="470" stroke="#182338"/>
<text x="804.8" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10³⁸</text>
<line x1="861.6" y1="58" x2="861.6" y2="470" stroke="#182338"/>
<text x="861.6" y="488" fill="#8fa3c0" font-size="12" text-anchor="middle">10⁴⁰</text>
<line x1="95" y1="470.0" x2="890" y2="470.0" stroke="#182338"/>
<text x="87" y="474.0" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻²²</text>
<line x1="95" y1="395.1" x2="890" y2="395.1" stroke="#182338"/>
<text x="87" y="399.1" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻²⁰</text>
<line x1="95" y1="320.2" x2="890" y2="320.2" stroke="#182338"/>
<text x="87" y="324.2" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻¹⁸</text>
<line x1="95" y1="245.3" x2="890" y2="245.3" stroke="#182338"/>
<text x="87" y="249.3" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻¹⁶</text>
<line x1="95" y1="170.4" x2="890" y2="170.4" stroke="#182338"/>
<text x="87" y="174.4" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻¹⁴</text>
<line x1="95" y1="95.5" x2="890" y2="95.5" stroke="#182338"/>
<text x="87" y="99.5" fill="#8fa3c0" font-size="12" text-anchor="end">10⁻¹²</text>
<rect x="95" y="58" width="795" height="412" fill="none" stroke="#8fa3c0"/>
<text x="492.5" y="514" fill="#8fa3c0" font-size="14" text-anchor="middle">kütle M [kg]</text>
<text x="26" y="264" fill="#8fa3c0" font-size="14" text-anchor="middle" transform="rotate(-90 26 264)">𝒜 = J / M²  [m² s⁻¹ kg⁻¹]</text>
<text x="95" y="32" fill="#e6eefb" font-size="15" text-anchor="start" font-weight="500">Şekil 11.3.L — Tek düzlemde bütün kütle ekseni: iki yatay çizgi, altı sınıf, 26 mertebe</text>
<line x1="95" y1="234.0" x2="890" y2="234.0" stroke="#ffb84d" stroke-width="2" stroke-dasharray="8 5"/>
<text x="105" y="222" fill="#ffb84d" font-size="12" text-anchor="start">yükleme yasası  𝒜₀ = 2,00×10⁻¹⁶   (η_z = 1 tavanı)</text>
<line x1="95" y1="344.6" x2="890" y2="344.6" stroke="#ff6b6b" stroke-width="2" stroke-dasharray="8 5"/>
<text x="105" y="360" fill="#ff6b6b" font-size="12" text-anchor="start">ufuk tavanı  𝒢/c = 2,23×10⁻¹⁹   ·   aradaki oran 897,5 ↔ m_p/2m_e = 918</text>
<line x1="95" y1="63.3" x2="526.6" y2="270.0" stroke="#ff9ecd" stroke-width="1.6" stroke-dasharray="3 5"/>
<text x="305" y="150" fill="#ff9ecd" font-size="12" text-anchor="start">dış tork izi:  𝒜 ∝ M^(−1/3)   (sabit dönem + sabit yoğunluk)</text>
<circle cx="451.5" cy="234.0" r="9" fill="none" stroke="#ff9ecd" stroke-width="2"/>
<circle cx="125.9" cy="78.0" r="5" fill="#ff9ecd" stroke="#ff9ecd" stroke-width="1.6"/>
<circle cx="163.4" cy="96.4" r="5" fill="#ff9ecd" stroke="#ff9ecd" stroke-width="1.6"/>
<circle cx="192.5" cy="111.1" r="5" fill="#ff9ecd" stroke="#ff9ecd" stroke-width="1.6"/>
<circle cx="221.4" cy="124.6" r="5" fill="#ff9ecd" stroke="#ff9ecd" stroke-width="1.6"/>
<circle cx="247.9" cy="134.3" r="5" fill="#ff9ecd" stroke="#ff9ecd" stroke-width="1.6"/>
<circle cx="271.9" cy="136.7" r="5" fill="#ff9ecd" stroke="#ff9ecd" stroke-width="1.6"/>
<text x="285" y="133" fill="#ff9ecd" font-size="11" text-anchor="start">asteroitler — yükleme çizgisinin 10³–10⁶ katı üstünde</text>
<circle cx="401.9" cy="220.3" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="429.4" cy="237.2" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="462.4" cy="236.1" r="5" fill="none" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="464.4" cy="238.6" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="485.5" cy="231.5" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<circle cx="500.4" cy="242.3" r="5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.6"/>
<text x="400" y="258" fill="#ffb84d" font-size="11" text-anchor="start">gezegenler (5 serbest) — çizgi üstünde</text>
<circle cx="393.7" cy="287.0" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="386" y="284" fill="#ff6b6b" font-size="11" text-anchor="end">Merkür</text>
<circle cx="426.9" cy="324.7" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="435" y="322" fill="#ff6b6b" font-size="11" text-anchor="start">Venüs — kavranmış (M-24)</text>
<path d="M 538.0 275.2 L 544.0 286.2 L 532.0 286.2 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.6"/>
<path d="M 540.9 291.3 L 546.9 302.3 L 534.9 302.3 Z" fill="none" stroke="#5ce6a8" stroke-width="1.6"/>
<text x="528" y="272" fill="#5ce6a8" font-size="11" text-anchor="end">yıldızaltı: vsini ▲ / dönem △</text>
<circle cx="581.1" cy="437.3" r="5.5" fill="#ffffff" stroke="#ffffff" stroke-width="1.6"/>
<text x="573" y="425" fill="#ffffff" font-size="11" text-anchor="end">beyaz cüceler (n = 31)</text>
<line x1="581.1" y1="437.3" x2="590.3" y2="446.7" stroke="#ffffff" stroke-width="1" stroke-dasharray="2 3" opacity="0.7"/>
<circle cx="586.2" cy="300.2" r="5" fill="none" stroke="#4dd2ff" stroke-width="1.6"/>
<circle cx="594.8" cy="303.7" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="604" y="296" fill="#4dd2ff" font-size="11" text-anchor="start">yıldızlar: doğum bandı + radyatif plato</text>
<circle cx="586.2" cy="369.2" r="5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.6"/>
<text x="578" y="366" fill="#4dd2ff" font-size="11" text-anchor="end">Güneş</text>
<circle cx="590.3" cy="446.7" r="5" fill="#b58cff" stroke="#b58cff" stroke-width="1.6"/>
<text x="599" y="450" fill="#b58cff" font-size="11" text-anchor="start">nötron yıldızları (n = 2.527) — tavanın 500 kat altında</text>
<circle cx="609.4" cy="379.1" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<circle cx="617.2" cy="344.9" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<circle cx="623.8" cy="344.8" r="5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<path d="M 637.0 345.1 L 643.0 351.1 L 637.0 357.1 L 631.0 351.1 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<path d="M 647.3 344.0 L 653.3 350.0 L 647.3 356.0 L 641.3 350.0 Z" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="660" y="374" fill="#ff6b6b" font-size="11" text-anchor="start">karadelikler — tavana yaslanır, hiçbiri aşmaz</text>
<rect x="769.5" y="341.3" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="782" y="333" fill="#ff6b6b" font-size="11" text-anchor="start">Sgr A*</text>
<rect x="859.8" y="341.3" width="10" height="10" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.6"/>
<text x="854" y="333" fill="#ff6b6b" font-size="11" text-anchor="end">M87*</text>
<circle cx="602" cy="80" r="4.5" fill="#ff9ecd" stroke="#ff9ecd" stroke-width="1.4"/>
<text x="615" y="84" fill="#ff9ecd" font-size="12" text-anchor="start">asteroit / küçük gövde (19.929)</text>
<circle cx="602" cy="100" r="4.5" fill="#ffb84d" stroke="#ffb84d" stroke-width="1.4"/>
<text x="615" y="104" fill="#ffb84d" font-size="12" text-anchor="start">gezegen (8) · içi boş: Uranüs</text>
<path d="M 602 115 L 608 126 L 596 126 Z" fill="#5ce6a8" stroke="#5ce6a8" stroke-width="1.4"/>
<text x="615" y="124" fill="#5ce6a8" font-size="12" text-anchor="start">yıldızaltı (4)</text>
<circle cx="602" cy="140" r="4.5" fill="#4dd2ff" stroke="#4dd2ff" stroke-width="1.4"/>
<text x="615" y="144" fill="#4dd2ff" font-size="12" text-anchor="start">yıldız (711.356) · içi boş: T Tauri</text>
<circle cx="602" cy="160" r="4.5" fill="#ffffff" stroke="#ffffff" stroke-width="1.4"/>
<text x="615" y="164" fill="#ffffff" font-size="12" text-anchor="start">beyaz cüce (31) — asterosismik P_rot</text>
<circle cx="602" cy="180" r="4.5" fill="#b58cff" stroke="#b58cff" stroke-width="1.4"/>
<text x="615" y="184" fill="#b58cff" font-size="12" text-anchor="start">nötron yıldızı (2.527)</text>
<circle cx="602" cy="200" r="4.5" fill="#ff6b6b" stroke="#ff6b6b" stroke-width="1.4"/>
<text x="615" y="204" fill="#ff6b6b" font-size="12" text-anchor="start">karadelik (290) · ◆ GW, ■ SMBH</text>
</svg>
<p style="font-size:0.9em;color:#8fa3c0;margin:10px 4px 2px;"><em>Şekil 11.3.L: Kütle–spin ilişkisinin tam haritası. 𝒜 = J/M² değişkeninde yükleme yasası (turuncu) ve ufuk tavanı (kırmızı) yatay doğrulardır; aralarındaki 897,5 kat, m_p/2m_e = 918'in gözlenen karşılığıdır. Pembe kesikli çizgi asteroitlerin dış tork izidir (𝒜 ∝ M^−1/3, yani sabit dönem + sabit yoğunluk) ve yükleme çizgisini açık daireyle işaretlenen noktada — 3,6×10²⁵ kg ≈ 6 Dünya kütlesi — keser. O kütlenin altında gözlem yasayı 10³–10⁶ kat aşar: yükleme yasasının bir <strong>kütle tabanı</strong> vardır. Tabanın üstünde hiçbir sınıf gezegen bandını kalibrasyonun ±2 katlık saçılmasından fazla aşmaz (Mars 2,27 ve Satürn 1,14 üst kenardadır) ve sınıflar zarf merdiveni boyunca aşağı iner; ufuk tavanını yalnız karadelikler doldurur ve hiçbiri aşmaz. Beyaz cüceler (beyaz daire) ile nötron yıldızları (mor) merdivenin en alt basamağını 1,8 kat içinde paylaşır — yarıçapları 700 kat farklı olmasına rağmen, çünkü ortak özellikleri tek şeydir: zarfını atmış olmak. Yıldızaltı sınıfında dolu üçgen v sin i tabanlı, içi boş üçgen gerçek dönem tabanlı ölçümdür; aradaki 2,9 kat, v sin i örnekleminin hızlı dönenlere seçilmesidir.</em></p>
</div>

**(a) Asteroitler yasanın kütle tabanını ölçer.** 19.929 küçük gövdede dönme dönemi medyanı **8,31 saat**, çeyrekler arası aralık 4,83–20,04 saattir; yani $\Omega_{makro}$ bandı (Sınav 4) 17 mertebe daha aşağıda da ayaktadır. Ama açısal momentum yükleme yasasına **uymaz**:

$$J\propto M^{1{,}637\pm0{,}003}\qquad(R^2=0{,}930,\ \text{artık }0{,}542\ \text{dex})$$

Bu üs $5/3$'ten 9,4σ, $2$'den **114σ** uzaktır. $5/3$'e yakınlığı yapısaldır: sabit dönem ve sabit yoğunlukta $J=\lambda MR^2\omega\propto M\cdot M^{2/3}$ verir. Sonuç $\eta_z=10^{3}$–$10^{6}$, yani gözlem yükleme yasasını milyon kata kadar **aşar**. §11.3.8'in $\min[\cdot]$ yapısı bunu açıklayamaz — çünkü $\min$ bir tavandır ve tavan aşılmıştır. Doğru okuma bir tanım alanı kaydıdır: asteroitlerin spini yüklemeden değil **dış torklardan** gelir (çarpışma geçmişi ve ışınım torkları), dolayısıyla yasanın alanı dışındadırlar. Dış tork izi yükleme çizgisini $3{,}6\times10^{25}$ kg'da (≈ 6 $M_\oplus$) keser; **ölçülen kütle tabanı budur.**

Aynı popülasyon teorinin ikinci terimini de doğrular: çapı 200 m'den büyük 19.903 cismin yalnız **%2,19'u** 2,2 saatlik kırılma bariyerinin altındadır, oysa 200 m'den küçük 26 cismin **%34,6'sı** bariyeri aşar. Kırılma tavanı, kendi bağını taşıyamayan gövdeler için gerçektir; monolitik küçük gövdeler için ise bağ kütle-itim değil malzeme dayanımıdır ve tavan kalkar. Denklemin $\epsilon_k\lambda M\sqrt{\mathcal{G}MR}$ terimi bu iki davranışı doğru ayırır.

**(b) Bir dürüstlük uyarısı: gezegen kalibrasyonu tam kesişimin üstündedir.** Kütle tabanı ($3{,}6\times10^{25}$ kg) ile gezegen dizisinin alt ucu (Dünya, $6{,}0\times10^{24}$ kg) aynı mertebededir. Yani $\mathcal{A}_0$'ın kalibre edildiği yer, dış tork izinin yükleme çizgisini kestiği bölgeye yakındır — ve bir kesişim bölgesinde her iki yasa da yerel olarak iyi uyar. Nitekim asteroit ilişkisi gezegenlere uzatıldığında $J$'yi 0,43–3,18 kat içinde verir; $\mathcal{A}_0M^2$ ise 0,60–2,32 kat içinde. **Mutlak değerde ikisi ayrılamaz.** Ayrımı yapan tek şey eğimdir: gezegenler $M^{1{,}885\pm0{,}065}$, asteroitler $M^{1{,}637\pm0{,}003}$ verir — aradaki fark **3,8σ**, yani iki rejim gerçekten ayrıdır ve gezegenler asteroit izinin devamı değildir. Bu ayrım kayda geçirilir ama zayıftır; güçlendirmenin yolu $10^{25}$–$10^{26}$ kg arasını (süper-Dünyalar, buz devleri) ölçülü spinle doldurmaktır.

**Ve buradan çıkan bir iç gerilim kayda geçmelidir.** Ölçülen taban $3{,}6\times10^{25}$ kg'dır; oysa $\mathcal{A}_0$'ın kalibre edildiği beş serbest-hizalı gezegenden **ikisi — Mars ($6{,}4\times10^{23}$) ve Dünya ($6{,}0\times10^{24}$) — bu tabanın altındadır.** Yani bölüm, aynı bölümde yasanın geçerli olmadığını söylediği kütlelerdeki gövdeleri katsayı kalibrasyonunda kullanmaktadır. Sonucu geçersiz kılmaz ama sayıyı oynatır: tabanın üstündeki üç gövde (Neptün, Satürn, Jüpiter) tek başına $\mathcal{A}_0=1{,}615\times10^{-16}$ verir — beşlinin $2{,}001\times10^{-16}$'sının **%19,2 altında.** Kaymanın kaynağı belirlidir: düşen iki gövdeden Mars, $\mathcal{A}=4{,}63\times10^{-16}$ ile bütün dizinin en yüksek değeridir ve $\eta_z=2{,}27$ aşımını da o üretir. Yani taban ölçütü uygulandığında bant hem daralır hem aşağı kayar, ve $\eta_z>1$ aşımı büyük ölçüde ortadan kalkar. Mantıksal sıra yine de terstir ve öyle kaydedilir. İki çıkış yolu vardır ve ikisi de bu bölümde seçilmemiştir: ya taban yalnız asteroit izinin geçerli olduğu bölge için okunur (gezegenler ayrı bir rejim sayılır), ya da $\mathcal{A}_0$ yalnız tabanın üstündeki gövdelerle yeniden kalibre edilir. **Seçim açık kalemdir** `[F]`.

**(c) Nötron yıldızları: besleme zarfı 2.527 gövdede doğrulanır.** ATNF kataloğunun tamamı (tekdüze $M=1{,}4\,M_\odot$, $R=12$ km, $I=0{,}4MR^2$ — 11.3.5'in nesneye özgü tablosundan farkı orada kayıtlıdır) şunu verir:

| Alt küme | $n$ | medyan $a^*$ |
|---|---|---|
| Çift sistemde | 256 | **0,1331** |
| Tek (yalıtık) | 2.271 | **0,00103** |

Fark **129 kat**, tek yönlü ve tam beklenen yönde. §11.3.5(iii)'ün "beslenme diski geçici bir zarftır ve zarf geri gelince kuplaj geri gelir" cümlesi, 8 nesne yerine 2.527 nesneyle sınandı ve ayakta kaldı. Milisaniye pulsarları (P < 30 ms, $n=337$) medyan $a^*=0{,}139$ ile aynı grubu oluşturur. Ve tavan: **2.527 pulsarın hiçbiri $a^*=1$'i aşmaz**; en yüksek değer 0,418, yalnız iki nesne 0,37'nin üstünde. Sınıfın $\eta_z$ geometrik ortalaması $2{,}10\times10^{-6}$, saçılma 0,818 dex.

**(d) Karadelikler: tavan 290 nesnede aşılmaz.** GWTC kataloğunun kütlesi ve $\chi_{eff}$'i olan 273 birleşmesinde etkin spin medyanı $+0{,}050$, saçılma 0,136, menzil $-0{,}31$…$+0{,}68$; **$|\chi_{eff}|>1$ olan tek olay yoktur.** X-ışını çiftleriyle birlikte 290 nesnede tavan bir kez bile delinmez. Uyarı zorunlu: $\chi_{eff}$ tek bir karadeliğin $a^*$'ı değil, çiftin kütleyle ağırlıklı hizalı bileşenidir — dolayısıyla bu, "$a^*>1$ yok" ifadesinin zayıf biçimidir. 11.3.6'nın $a^*>1$ bahsi bu veriyle **kapanmaz**, yalnız sıkışır.

**(e) Beyaz cüceler: önce öngörü kuruldu, sonra ölçüldü — tuttu.** Beyaz cüceler bölümün en keskin sınavını taşır: bir K cücesiyle aynı kütlede ama **yaklaşık 100 kat küçük yarıçapta** bir gövde, yasanın $R$'den bağımsız olduğu iddiasını uç noktada sınar (öngörü 2'nin en sert biçimi). Yasanın istediği hesaplanır: $0{,}6\,M_\odot$ ve $R=8{,}6\times10^{6}$ m için ($k^2=0{,}17$) $J=\mathcal{A}_0M^2=2{,}85\times10^{44}$, yani **$P=0{,}331$ saniye.** Gözlenen beyaz cüce dönemleri saatler mertebesindedir; dolayısıyla teorinin öngörüsü şuydu: beyaz cüceler gezegen ya da yıldız bandına değil, **nötron yıldızı bandına** düşmek zorundadır — çünkü beyaz cüce de zarfını atmış bir çekirdektir (gezegenimsi bulutsu evresi), yani R3 rejiminde olmalıdır.

Ölçüm Hermes ve ark. (2017) Tablo 4'ünden gelir: asterosismik dönme yarılmalarından belirlenmiş 31 DAV (soğumuş, hidrojen atmosferli pulsatör), kütleleriyle birlikte. Ayrıştırılan tablo kaynağın kendi özet değerini yeniden üretir — dönem ortalaması $33{,}1\pm25{,}0$ saat çıkar, makalenin bildirdiği $35\pm28$ saat ile aynıdır.

| Sınıf | $n$ | medyan $M$ | medyan $P_{rot}$ | $\eta_z$ (geo) | $\sigma$ |
|---|---|---|---|---|---|
| **DAV** (soğumuş beyaz cüce) | 31 | $0{,}66\,M_\odot$ | 29,4 sa | $\mathbf{3{,}74\times10^{-6}}$ | 0,428 dex |
| DOV (PG 1159, ön-beyaz cüce) | 5 | $0{,}55\,M_\odot$ | 28,0 sa | $4{,}50\times10^{-6}$ | 0,338 dex |
| DBV (helyum atmosferli) | 2 | $0{,}55\,M_\odot$ | 27,4 sa | $4{,}93\times10^{-6}$ | 0,366 dex |

**Öngörü tuttu ve sıkı tuttu.** Beyaz cücelerin $\eta_z=3{,}74\times10^{-6}$'sı, nötron yıldızlarının $2{,}10\times10^{-6}$'sının **1,8 katı içindedir** — yani iki sınıf, kütleleri benzer ama yarıçapları 700 kat farklı olmasına rağmen aynı hanededir. Gözlenen dönem, yasanın istediğinden $3{,}2\times10^{5}$ kat yavaştır; $a^*$ medyanı $2{,}6\times10^{-3}$, en yükseği $4{,}0\times10^{-2}$, yani tavandan çok uzaktadır. Zarf merdiveninin en alt basamağını iki bağımsız sınıf paylaşır ve ikisinin ortak özelliği tek şeydir: **zarfını atmış olmak.**

Üç kayıt: yarıçaplar dejenere kütle–yarıçap bağıntısından ($R\propto M^{-1/3}$, $0{,}6\,M_\odot$'da $8{,}6\times10^{6}$ m'ye çapalanmış) türetildi, ölçülmedi — $\eta_z\propto R^2$ olduğundan bu seçim doğrudan sonuca girer. Duyarlılık ölçüldü: aynı 28 nesne daha dik bir bağıntıyla ($R\propto M^{-0{,}705}$) yeniden hesaplandığında $\eta_z$ $3{,}74\times10^{-6}$'dan $3{,}84\times10^{-6}$'ya, yani **yalnız %2,8** kayıyor. Sonuç yarıçap modeli seçimine karşı sağlamdır. DOV'ler henüz soğuma koluna girmemiş, yarıçapları daha büyüktür; ayrı satırda tutulmalarının nedeni budur ve $\eta_z$'leri bu yüzden hafif yüksek çıkar. Ve örneklem pulsatörlerden oluşur, yani tüm beyaz cücelerin rastgele bir kesiti değildir.

**(e′) Yıldızaltı sınıfı: iki bağımsız yolla ölçüldü, ikisi ayrışıyor.** İki gerçek popülasyon şunu verir:

| Kaynak | Ölçüm | $n$ | $\eta_z$ (geo) | $\sigma$ |
|---|---|---|---|---|
| Vos ve ark. (2022) | **gerçek $P_{rot}$** ($\sin i$ yok) | 15 | $\mathbf{0{,}0204}$ | 0,531 dex |
| BDKP V (Hsu ve ark. 2021) | $v\sin i$ ($\langle\sin i\rangle=\pi/4$) | 37 | $0{,}0586$ | 0,295 dex |

İki değer 2,9 kat ayrışır ve **hangisinin daha güvenilir olduğu belirlidir: dönem tabanlı olan.** $v\sin i$ örneklemi iki yönden yukarı kayar — çizgi genişlemesi ~9 km/s altında ölçülemediği için yavaş dönenler örnekleme girmez, ve $\langle\sin i\rangle$ düzeltmesi tek tek nesnede geçerli değildir. Bu nedenle sınıfın platosu **$\eta_z=0{,}0204$** olarak alınır; $0{,}0586$ üst sınırdır. Sınıf merdivenin doğru basamağındadır: gezegenin (0,98) altında, radyatif yıldızın (0,0138) hemen üstünde.

**(f) Ortaya çıkan matematik.** Altı sınıf ve 734.000 gövde birlikte okunduğunda kütle–spin ilişkisi tek bir güç yasası değil, **tanım alanı sınırlı bir tavan ailesi**dir:

$$\boxed{\;\mathcal{A}=\frac{J}{M^{2}}=\begin{cases}\ \propto M^{-1/3}\ \ (\gg\mathcal{A}_0) & M<M_{\text{taban}}=3{,}6\times10^{25}\ \text{kg}\quad\text{— dış tork rejimi, yasa geçersiz}\\[6pt]\ \mathcal{A}_0\cdot\eta_z(\text{zarf},t)\ \le\ \mathcal{A}_0 & M\ge M_{\text{taban}}\ ,\ \text{zarf var}\\[6pt]\ \le\ \mathcal{G}_{yerel}/c_{yerel} & \text{ufuk var}\end{cases}\;}$$

Üç satırın da ölçülmüş içeriği vardır: taban $3{,}6\times10^{25}$ kg'da, $\mathcal{A}_0=2{,}00\times10^{-16}$, tavan $2{,}23\times10^{-19}$ ve **aralarındaki oran 897,5** — 11.3.7(d)'nin $m_p/2m_e=918$ yapısal sonucunun %2,2 içinde karşılığı. $\eta_z$ merdiveni ise tabanın üstündeki bütün kütle ekseninde tek yönlüdür: gezegen 0,98 → yıldızaltı 0,020 → radyatif yıldız 0,0138 → Güneş $2{,}4\times10^{-4}$ → beyaz cüce $3{,}7\times10^{-6}$ → nötron yıldızı $2{,}1\times10^{-6}$.

**$\eta_z=1$ sert bir tavan değil, ±2 katlık bir banttır.** Mars $\eta_z=2{,}27$ ve Satürn $1{,}14$ ile bandın üst kenarını aşar. Geçerli ifade şudur: **tabanın üstünde hiçbir sınıf, gezegen bandını kalibrasyonun ±2 katlık saçılmasından fazla aşmaz** (11.3.3'ün "saçılma tabanı ±%30" kaydıyla tutarlı), ve bandın altındaki sınıflar 6 mertebeye yayılır. Aşımın kendisi de bilgi taşır: $\mathcal{A}_0$ beş gezegenin geometrik ortalamasına kalibre edildiği için bant *ortalanmıştır*, dolayısıyla üstünde de altında da gövde bulunması beklenir. Tavan ancak ufuk tavanı için ($a^*\le1$) sert biçimde kurulabilir; orada 2.527 pulsar ve 290 kompakt nesnede istisna yoktur.

Kalan üç sistematik kayda geçer: asteroit kütleleri varsayılan $\rho=2200$ kg/m³ ile hesaplandı ve $\mathcal{A}\propto1/\rho$ olduğundan yoğunlukta 2 kat hata $\mathcal{A}$'yı 2 kat kaydırır (üs bundan etkilenmez); pulsar $a^*$ değerleri $M=1{,}4\,M_\odot$ ve $R=12$ km varsayımına dayanır ve $a^*\propto R^2/M$ olduğundan gerçek dağılım ~2 kat geniştir; $\chi_{eff}$ tek nesne spini değildir. Hiçbiri yukarıdaki üç satırın işaretini değiştirmez, hepsi mutlak değerlerini oynatır.

### Sonuç: kütle–spin ilişkisi var, ve iki değişkenli

Altı sınavın ardından bölümün başlığındaki soruya doğrudan cevap verilebilir. **Kütle ile spin arasında bir ilişki vardır** — ve bu, dizinin bir istatistik artığı değildir:

1. **Biçim ortaktır.** Tabanın üstündeki bütün sınıflarda $J$, $M^2$ ile ölçeklenen bir üst zarfın altında durur; iki uçta — serbest-hizalı gezegenlerde $M^{1{,}885\pm0{,}065}$ (1,8σ) ve karadeliklerde $M^{2{,}028\pm0{,}019}$ (1,5σ) — üs $M^2$'yle uyumludur.
   > **Hangi gezegen setinin kullanıldığı belirleyicidir.** Sekiz gezegenin tamamına uydurulursa üs $M^{2{,}248\pm0{,}263}$ çıkar ve $M^2$'den yalnız 0,9σ uzaklaşır — fakat bu **daha güçlü değil, daha zayıf bir sınavdır**: sete girmesi için Merkür ile Venüs'ün de sayılması gerekir, oysa bölüm ikisini de M-24'ün kavramasıyla %97,7 ve %100,3 bastırılmış sayar (11.3.3) ve $\eta_z$ hesabında yasanın dışında tutar. Bastırılmış çiftin saçılması hata çubuğunu dört kat şişirir; $\sigma$ küçüldüğü için değil, belirsizlik büyüdüğü için "$M^2$'ye yakın" görünür. Bölümün her yerinde kullanılan değer bu yüzden serbest beşlinin üssüdür.
2. **Ölçek doğrudur.** Biçimin katsayısı $\mathcal{A}_0=2{,}0\times10^{-16}$, teorinin ilkel niceliklerinden bağımsız olarak hesaplanan $2{,}05\times10^{-16}$ ile %2,4 içinde buluşur (11.3.7c).
3. **Tavanla oranı saf bir kütle oranıdır.** $\mathcal{A}_0/(\mathcal{G}/c)=897{,}5$, $m_p/2m_e=918$ ile %2,2 içinde (11.3.7d).

Ama ilişki **tek değişkenli değildir**, ve bu bir eksiklik değil, bölümün en baştan kurduğu iddianın kendisidir — başlığı zaten *"Kütle–Dönüş İlişkisi: Zarf Rejimleri"*dir. Kütle **biçimi ve üst sınırı** verir; katsayıyı **zarf durumu** verir. Sınav 6'nın en güçlü sayısı bunu gösterir: $M\approx10^{30}$ kg diliminde, yani *aynı kütlede*, $\mathcal{A}$ beş kategori arasında **7.621 kat** yayılır.

| Aynı kütlede ($M\approx10^{30}$ kg) | $\eta_z$ |
|---|---|
| Yıldız — Gaia (radyatif, kanal kapalı) | $1{,}07\times10^{-2}$ |
| Yıldız — Kepler (konvektif, kanal açık) | $7{,}6\times10^{-4}$ |
| Nötron yıldızı — besleme zarflı | $7{,}8\times10^{-5}$ |
| Beyaz cüce — zarf atılmış | $3{,}9\times10^{-6}$ |
| Nötron yıldızı — yalıtık, çıplak | $1{,}4\times10^{-6}$ |

Kütle bu yayılmayı açıklayamaz; zarf durumu açıklar, ve sıralaması tam olarak R1→R2→R3 hattıdır. İki bağımsız kanıtı vardır: beyaz cüce ile yalıtık nötron yıldızı aynı basamağı paylaşır (yarıçapları **700 kat** farklıdır), ve çift/yalıtık pulsar aynı nesne türünde, aynı kütle ve yarıçapta **129 kat** ayrışır.

Dolayısıyla bölümün çıktısı tek bir güç yasası değil, **iki değişkenli bir yapıdır:**

$$J=\underbrace{\mathcal{A}_0M^{2}}_{\text{kütlenin verdiği biçim ve tavan}}\times\underbrace{\eta_z(\text{zarf},t)}_{\text{zarfın verdiği katsayı}}\ ,\qquad M\ge M_{\text{taban}}$$

Standart astrofizikte bu iki değişken hiç birlikte yazılmaz: her cisim sınıfı kendi ayrı anlatısını taşır. Buradaki iddia, ikisinin tek çatı altında ve **tek bir ikinci değişkenle** yazılabildiğidir. Mekanizma açıktır (11.3.7b), $\kappa=\tfrac12$ türetilmemiştir (11.3.7f) ve taban ile kalibrasyon arasındaki gerilim kayıtlıdır (Sınav 6b) — ama biçimin, ölçeğin ve zarf sıralamasının ölçülmüş olduğu bu üç maddeyle sabittir.

### Rejim sayıları — kategorik liste

§11.3.8'in rejim tablosu $\eta_z$'yi **biçim** olarak verir ($\approx1$, $\eta_i(1+t/\tau_z)^{-1/2}$, "tavanda"). Altı sınav bittikten sonra aynı tablonun **sayısal** karşılığı yazılabilir. Aşağıdaki liste bölümün tek referans çizelgesidir: her rejim için ölçülen $\eta_z$, örneklem büyüklüğü ve hangi sınavdan geldiği.

| Rejim | Zarf durumu | Temsilci popülasyon | $n$ | ölçülen $\eta_z$ | $\sigma$ (dex) | Sınav |
|---|---|---|---|---|---|---|
| **R0** | *yasanın altı* — dış tork (çarpışma + ışınım) | asteroit / küçük gövde | 19.929 | $\approx1{,}0\times10^{4}$ | 0,70 | 6a |
| **R1** | rijit zarf, kanal kapalı, $g\approx0$ | gezegen (serbest, **Uranüs dâhil**) | 6 | $\mathbf{0{,}96}$ | band 0,59–2,27 | 1 |
| **R1-g** | rijit zarf ama dış girdap kavramış | Merkür, Venüs | 2 | $0{,}012$ | 0,0038 ve 0,038 | 1 |
| **R1′** | rijit, kırılma tavanına dayanmış | yıldızaltı — **gerçek dönem** | 15 | $\mathbf{0{,}0204}$ | 0,53 | 6e′ |
| R1′ | ″ — $v\sin i$ (hızlı dönene seçilmiş, üst sınır) | yıldızaltı | 37 | $0{,}0586$ | 0,30 | 6e′ |
| **R2-doğum** | plazma zarf, kanal henüz kapalı ($=\eta_i$) | radyatif anakol | 19.659 | $\mathbf{0{,}0138}$ | 0,26 | 5i |
| **R2-yaşlı** | plazma zarf, kanal açık (Skumanich) | Kraft sonrası konvektif | 33.994 | $\mathbf{6{,}2\times10^{-4}}$ | 0,37 | 5ii |
| **R3-çıplak** | zarf fırlatılmış, tek kanal dipol freni | yalıtık pulsar | 2.271 | $\mathbf{1{,}15\times10^{-6}}$ | — | 6c |
| R3-çıplak | ″ | beyaz cüce (DAV) | 31 | $3{,}74\times10^{-6}$ | 0,43 | 6e |
| **R3-besleme** | zarf geri gelmiş (yığışma diski) | çift sistem pulsarı | 256 | $\mathbf{1{,}48\times10^{-4}}$ | — | 6c |
| **R4** | zarf yok, ufuk var — tavanda | X-ışını çifti + AGN | 16 | $\mathbf{1{,}00\times10^{-3}}$ | — | 6d |
| R4 | ″ — $\chi_{eff}$ (tavan sınavının zayıf biçimi) | GW birleşmesi | 273 | $5{,}6\times10^{-5}$ | — | 6d |
| — | **ufuk tavanının kendisi** ($a^*=1$) | — | — | $1{,}114\times10^{-3}$ | — | 7d |

**Üç ayrı gövde sayısı dolaşır ve üçü de farklı kapsamdadır; karıştırılmamalıdır:**

| Sayı | Neyi kapsar |
|---|---|
| **734.000** | Bütün sınıfların **süzgeçsiz** toplamı — yıldız kataloglarının tamamı (671.765 Gaia + 39.591 Kepler = 711.356) artı asteroit, pulsar, beyaz cüce, karadelik ve yıldızaltı örneklemleri |
| **93.224** | Etkileşimli panelin çizdiği **katalog seti**, on bir kategori: 19.929 asteroit · 8 gezegen · 15+37 yıldızaltı · 39.591 Kepler + 30.790 Gaia (panel süzgeci) · 38 beyaz cüce · 2.271+256 pulsar · 16 karadelik · 273 GW |
| **76.489** | Aşağıdaki rejim listesi — her rejim kendi **kalite süzgeçli** alt kümesiyle temsil edilir (Gaia tarafında 19.659, Kepler tarafında 33.994) |

Aradaki farkların tamamı süzgeç sıkılığıdır; hiçbir gövde iki kez sayılmaz.

İki okuma kuralı bağlayıcıdır:

**(1) Merdiven bir soy içinde tek yönlüdür, rejimler arasında değil.** Rijit → plazma → fırlatılmış hattı boyunca $\eta_z$ kesintisiz düşer ($0{,}96\to0{,}0138\to1{,}15\times10^{-6}$). Ama R4 bu hattın devamı **değildir**: ufuk tavanı $1{,}0\times10^{-3}$'te durur ve yaşlı R2 yıldızları ($6{,}2\times10^{-4}$, Güneş $2{,}45\times10^{-4}$) bu değerin **altına** iner. Karadelikler en az spinli sınıf değil, tavanı **dolduran** sınıftır; onların altına düşen yıldızlar frenlenmişliğin ne kadar ileri gidebileceğinin ölçüsüdür.

**(2) Zarfın geri gelmesi $\eta_z$'yi yükseltir.** R3'ün iki alt durumu arasındaki 129 kat (yalıtık $1{,}15\times10^{-6}$ ↔ besleme zarflı $1{,}48\times10^{-4}$) merdivenin tek geri yönlü adımıdır ve mekanizmanın işaretini doğrudan verir: $\eta_z$ zarfın *varlığının* ölçüsüdür, gövdenin yaşının ya da türünün değil. Aynı nesne, aynı kütle, aynı yarıçap — yalnız zarf geri geldiği için 129 kat daha fazla yükleme taşıyor.

Bir de listenin **ayırt edici kalemi**: R3'ün iki farklı sınıfı — nötron yıldızı ve beyaz cüce — 1,8 kat içinde aynı sayıyı verir (Sınav 6e). Yarıçapları 700, kütleleri 2 kat farklıdır; ortak olan tek şey zarfını atmış olmalarıdır. Rejim etiketinin sınıf etiketinden daha temel olduğu iddiasının en somut kanıtı budur.

### Bu bölüm ne kanıtladı, ne kanıtlamadı

| Sonuç | Statü |
|---|---|
| Serbest gezegenlerde $\eta_z\approx1$ | **dairesel** — $\mathcal{A}_0$ oradan kalibreli |
| Merkür/Venüs'te $1-\eta_z$ ile M-24'ün $g$'si %2 içinde | **bağımsız doğrulama** ✓ |
| Radyatif yıldızların 10 kat kütle menzilinde 1,7 kat içinde platolaşması | **bağımsız sonuç** ✓ |
| **Aynı platonun Gaia DR3'ün 19.659 yıldızıyla %11,5'te doğrulanması** | **bağımsız doğrulama** ✓✓ — iki ölçüm zinciri hiçbir girdi paylaşmaz (Sınav 5-i) |
| T Tauri ile radyatif anakolun aynı $\eta_z$'yi vermesi | **bağımsız sonuç** ✓ |
| Kraft kırılmasının $\eta_z$'de görünmesi | **bağımsız sonuç** ✓ — ama **basamak değil rampa**, $1{,}0$–$1{,}8\,M_\odot$ (Sınav 5-ii) |
| $\Omega_{makro}$ bandının darlığı | **gözlemsel olgu** — mekanizması 11.3.7(f)'de açık |
| Platoların mutlak değerleri (0,055 · 0,015) | **açık** — türetilmedi, ölçüldü; $k^2$ baskın sistematik |
| Rampanın $\eta_z\propto M^{3{,}44}$ eğimi | **fizik olarak okunamaz** — yaş-homojen olmayan örneklemin kütle × yaş çarpımı |
| Konvektif tarafta $\eta_z$'nin yaş bağımlılığı | **sınanamadı** `[F]` — `vbroad` tabanı ters işaret veriyor; asterosismik yaş gerekir |
| $\eta_z$ saçılmasının rejim işareti olması | **elendi** ✗ — iki rejimde de 0,25–0,38 dex; ayırt edici değil |
| Tabanın üstünde $\mathcal{A}$'nın gezegen bandını aşmaması | **bağımsız sonuç** ✓ — ama bant ±2 kat; Mars 2,27 ve Satürn 1,14 üst kenardadır (Sınav 6f) |
| $\mathcal{A}$'nın **aynı kütlede** zarfa göre 7.621 kat yayılması | **bağımsız sonuç** ✓✓ — kütle bunu açıklayamaz; iddianın çekirdeği (Sınav 6f) |
| $\mathcal{A}_0$ kalibrasyon setinin iki üyesinin kütle tabanının altında olması | **iç gerilim** — Mars ve Dünya, aynı bölümün geçersiz saydığı kütlelerde (Sınav 6b) |
| Yükleme yasasının kütle tabanı $3{,}6\times10^{25}$ kg | **ölçüldü** — 19.929 asteroit; denklemin tanım alanı daraltıldı (Sınav 6a) |
| Kırılma bariyerinin çap eşiğinde açılıp kapanması | **bağımsız doğrulama** ✓ — D>200 m'de %2,2, D<200 m'de %34,6 aşım |
| Besleme zarfı: çift/yalıtık pulsarda 129 kat $a^*$ farkı | **bağımsız doğrulama** ✓✓ — 2.527 pulsar (Sınav 6c) |
| Tavanın 290 kompakt nesnede aşılmaması | **bağımsız sonuç** ✓ — ama $\chi_{eff}$ tek nesne spini değil; zayıf biçim |
| Gezegen dizisinin asteroit izinden ayrı olması | **zayıf ayrım** — yalnız eğimde 3,8σ; mutlak değerde ayrılamaz (Sınav 6b) |
| **Beyaz cücelerin nötron yıldızı bandına düşmesi** | **öngörü doğrulandı** ✓✓ — önce hesaplandı, sonra ölçüldü: $3{,}74\times10^{-6}$ ↔ $2{,}10\times10^{-6}$, 1,8 kat (Sınav 6e) |
| Yıldızaltı platosu $\eta_z=0{,}0204$ | **ölçüldü** — gerçek dönemle, $n=15$; $v\sin i$'nin verdiği 0,0586 seçim etkisi taşır ve üst sınırdır (Sınav 6e′) |
| Beyaz cüce yarıçapları | **türetilmiş** — dejenere $M$–$R$ bağıntısından; iki farklı bağıntı arasında $\eta_z$ yalnız %2,8 oynuyor, sonuç sağlam |

---

## 11.3.10 Hüküm

| | Standart fizik | Evrenakı |
|---|---|---|
| Asteroit spini | çarpışma geçmişi + YORP torkları | **aynı** — yasanın kütle tabanının altı; teori burada iddia etmez |
| Gezegen spini | disk türbülansı kalıntısı (rastlantı) | $\mathcal{A}_0M^2$; katsayı ilkel niceliklerle yazılı |
| Yıldızaltı spini | oluşum + büzülme geçmişi | yükleme doğrusu kırılma tavanını keser, gövde boşaltır |
| Beyaz cüce spini | çekirdek dönüşü + zarf kaybı (ayrı mekanizma) | **aynı yükleme, R3 rejimi** — nötron yıldızıyla aynı basamak; öngörülüp doğrulandı |
| Yıldız spini | manyetik frenleme (ayrı mekanizma) | aynı yükleme, açık kanallı plazma zarf sızdırır |
| NS spini | AM korunumu + dipol (ayrı mekanizma) | aynı yükleme, ufuk tavanı kırpar, beslenme zarfı geri yükler |
| Karadelik spini | Kerr geometrisinin mutlak sınırı | aynı $M^2$'nin tavan katsayısı; **yerel** $\mathcal{G}$ ve $c$ ile |
| Sınıflar arası bağ | **yok** — dört bağımsız anlatı | **tek biçim, tek değişken (zarf), tek oran** |
| Yasanın tanım alanı | soru sorulmaz — her sınıf ayrı | **ölçülmüş taban:** $M\ge3{,}6\times10^{25}$ kg; altında teori iddia etmez |

Dürüst kapanış üç cümledir. Parçaların çoğu — Skumanich yasası, dipol freni, Kerr sınırı, geri dönüştürme, kırılma sınırı — standart astrofizikte tek tek bilinir; teorinin bunları yeniden keşfetmesi bir zafer değildir. Teorinin katkısı çatı ve orandır: yedi sınıfın da $J=\mathcal{A}M^2$ biçimini paylaşması, katsayının zarf durumuyla kademelenmesi, iki tavanın tek ilkeye inmesi, iki bağımsız sınıfta aynı $t^{-1/2}$ sızıntı üssünün çıkması — ve en somutu, gezegen bandı ile kompakt tavan arasındaki 898 katın, hiçbir yerel nicelik içermeyen $m_p/2m_e=918$ oranıyla %2,2'de buluşması.

Yıldız tarafında en sağlam ayak Sınav 5'tir: radyatif plato, 1982'nin altı tayf ortalamasından da Gaia DR3'ün 19.659 tek tek yıldızından da aynı değeri (%11,5 içinde) verir — iki ölçüm zinciri hiçbir girdi paylaşmadığı için bu bir kalibrasyon değil, doğrulamadır. Aynı veri Kraft eşiğinin $\eta_z$ ekseninde keskin bir basamak değil, $1{,}0$–$1{,}8\,M_\odot$ arasına yayılan bir rampa olduğunu da gösterir.

Sınav 6 ise ilişkinin **içeriğini ve sınırını** birlikte vermiştir. Kütle–spin ilişkisi vardır: biçim ortaktır, iki uçta üs $M^2$'yle uyumludur (gezegenlerde 1,8σ, karadeliklerde 1,5σ), katsayının ölçeği teorinin ilkel niceliklerinden %2,4 içinde çıkar ve tavanla oranı saf bir kütle oranıdır. Ama ilişki **iki değişkenlidir** — kütle biçimi ve tavanı verir, katsayıyı zarf durumu verir — ki bölümün adı zaten bunu söyler. Kanıtı $M\approx10^{30}$ kg diliminde aynı kütlede görülen **7.621 katlık** yayılmadır; kütle bunu açıklayamaz, zarf açıklar. Sınırı ise ölçülmüştür: $3{,}6\times10^{25}$ kg'ın altında spin dış torklardan gelir ve yasa geçersizdir. Üç bağımsız doğrulama bu çatının en somut kanıtıdır: kırılma bariyerinin çap eşiğinde açılıp kapanması (D>200 m'de %2,2, altında %34,6); besleme zarfının 2.527 pulsarda çift/yalıtık ayrımıyla 129 kat $a^*$ farkı üretmesi; ve beyaz cücelerin — hesap önce yapılıp sonra ölçülerek — nötron yıldızlarıyla aynı basamağa, 1,8 kat içinde düşmesi. Son bulgu merdivenin okunuşunu da doğrular: iki sınıfın yarıçapı 700 kat farklıdır, ortak olan tek şey zarfını atmış olmalarıdır.

Ama bölüm bir türetim iddia etmez: üretici mekanizma açıktır, iki aday elenmiştir ve $\kappa=\tfrac12$ türetilmemiştir (11.3.7f). Elde olan, mekanizmasız ama dar ve sınırı ölçülmüş bir yapısal örüntüdür — ve altı bahsi vardır: oranın 918'de kalması, şişmiş-Jüpiter yarıçap sınavı, $\rho_0$–$G$–spin bağı, yaş-homojen bir kümede rampanın düzleşmesi, beyaz cücelerin $\eta_z\sim10^{-5}$ bandında çıkması ve $a^*>1$ arayışı. Altısı da önümüzdeki on yılın verisiyle sınanabilir.
